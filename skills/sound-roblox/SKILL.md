---
name: sound-roblox
description: Roblox-specific audio building and sourcing. The new Audio API (AudioPlayer, AudioEmitter, AudioListener, AudioFader, AudioCompressor, Wire) with a five-bus setup and ducking in code, 3D emitters and attenuation, a variation and shuffle-bag helper, footsteps by FloorMaterial, synced music layers and bar-boundary switching, the legacy Sound fallback, upload rules, the private-audio permissions gotcha, legal sources in priority order with license rules, the credits file and in-game credits screen, and the MCP search, preview, insert and log-credits workflow. Use while sourcing, uploading, wiring or debugging any audio.
---

# Sound: Roblox

Load `sound` first for the legal rule and the gates, and `sound-craft` for the design decisions. This file is how to build and source it on Roblox. Rules have IDs (SR1 to SR14).

**Verify before relying on anything here.** The audio API has changed across releases. Check every class, property, method and event with `get_roblox_docs` before writing code against it, and read the result in a live session. In particular, **the AudioPlayer's asset property has been named both `Asset` and `AssetId` in different releases; verify it with `get_roblox_docs`.** The code below marks each place that depends on it.

Facts marked "as of" are volatile. Re-check them when they matter.

## 1. Which API
- **New Audio API (preferred).** Audio objects connected by wires: producers (AudioPlayer), effects (AudioFader, AudioCompressor, AudioEqualizer, AudioReverb, AudioEcho, AudioPitchShifter, AudioChorus, AudioDistortion, AudioFlanger, AudioTremolo, AudioAnalyzer), spatial objects (AudioEmitter, AudioListener) and the consumer (AudioDeviceOutput). The docs now discourage the legacy objects in favor of these.
- **Legacy (still works):** Sound, SoundGroup and SoundEffects. Use it only for a quick prototype or an existing game that already uses it (see section 9). Acoustic Simulation does not support legacy Sound.

Wiring patterns [doc]:
- **2D:** AudioPlayer → Wire → a bus → AudioDeviceOutput.
- **3D:** AudioPlayer → Wire → AudioEmitter (parented to a part or attachment). An AudioListener hears emitters and is wired onward to the output.
- **Bus:** many AudioPlayers → one AudioFader → effects → output. AudioFader replaces SoundGroup.
- **Ducking:** an AudioCompressor's "Sidechain" input pin, fed by the bus that should cause the duck.

## 2. The bus setup
**SR1** Build the bus graph **on the client**, once per player, in a LocalScript (for example `StarterPlayerScripts/Audio`). Output and player volume settings are per player.

**SR2** Five buses (Music, Ambience, SFX, Dialogue, UI), each an AudioFader, into one gentle master compressor and then the output. Music and Ambience pass through a ducking compressor keyed by Dialogue. Expose a slider per bus in the settings menu.

```lua
-- StarterPlayerScripts/Audio/Buses (ModuleScript). Verify every class, property
-- and default with get_roblox_docs before relying on it.
local SoundService = game:GetService("SoundService")

local function wire(source, target, targetName)
	local w = Instance.new("Wire")
	w.SourceInstance = source
	w.TargetInstance = target
	if targetName then w.TargetName = targetName end -- "Sidechain" for ducking
	w.Parent = target
	return w
end

local root = Instance.new("Folder")
root.Name = "AudioBuses"
root.Parent = SoundService

local output = Instance.new("AudioDeviceOutput")
output.Parent = root

local master = Instance.new("AudioCompressor") -- gentle catch-all limiter
master.Name = "Master"
master.Threshold = -6 -- dB; check units and defaults in the docs
master.Ratio = 10
master.Parent = root
wire(master, output)

local buses = {}
for _, name in { "Music", "Ambience", "SFX", "Dialogue", "UI" } do
	local fader = Instance.new("AudioFader")
	fader.Name = name
	fader.Parent = root
	buses[name] = fader
end

-- Music and Ambience dip when Dialogue (barks, voice) plays.
local duck = Instance.new("AudioCompressor")
duck.Name = "DialogueDuck"
duck.Threshold = -30
duck.Ratio = 4
duck.Parent = root
wire(buses.Music, duck)
wire(buses.Ambience, duck)
wire(buses.Dialogue, duck, "Sidechain")
wire(duck, master)

-- Everything else goes straight to the master. Dialogue needs its own wire
-- to be heard; the sidechain wire only controls the duck.
wire(buses.SFX, master)
wire(buses.Dialogue, master)
wire(buses.UI, master)

return { root = root, buses = buses, wire = wire, output = output }
```

Tune the duck by ear (with the user, see `sound-audit`) toward a 3-8 dB dip on Music and Ambience. Set starting bus volumes from the mix table in `SOUND-PLAN.md`.

**Routing 3D sound into buses.** An emitter is heard through a listener, so to keep 3D SFX, Ambience and Dialogue on their own buses, use one listener per bus with matching interaction groups:

```lua
-- One listener per 3D bus, on the camera (or the character's head; pick one
-- and write it in the plan). Emitters set the same AudioInteractionGroup.
local Buses = require(script.Parent.Buses)
local camera = workspace.CurrentCamera
for _, name in { "SFX", "Ambience", "Dialogue" } do
	local listener = Instance.new("AudioListener")
	listener.Name = name .. "Listener"
	listener.AudioInteractionGroup = name
	listener.Parent = camera
	Buses.wire(listener, Buses.buses[name])
end
```

With custom listeners, turn off the engine's automatic listener so sounds are not heard twice. The SoundService property that controls it has been named `ListenerLocation` or `DefaultListenerLocation`; verify with `get_roblox_docs` and set it to `None`. Then confirm in a live session that a 3D sound is heard once and that moving each bus slider affects it.

`AudioInteractionGroup` is also how to make a sound only some listeners hear (a radio for one player, a hallucination).

## 3. Playing sounds: 3D, variation, voice limits
**SR3** Every 3D sound goes through an AudioEmitter on the part or attachment that makes it, with the emitter's interaction group set to its bus and a distance attenuation curve per category (starting points from the research; tune them):
| Category | Audible range |
|---|---|
| Footsteps | about 40-80 studs (a balance number in PvP and stealth) |
| Gunshots and explosions | about 200+ studs, with a far variant past about a third of that |
| Ambient spot emitters | about 20-40 studs |
| Threat tells | far enough to react in time (SC7); test it |

`AudioEmitter:SetDistanceAttenuation` takes a curve of distance to volume; verify the exact format with `get_roblox_docs`.

**SR4** A variation helper: shuffle bag (no immediate repeats), pitch spread and volume spread, used for every repeated sound.

```lua
-- StarterPlayerScripts/Audio/Play (ModuleScript)
local Buses = require(script.Parent.Buses)
local Play = {}
local bags = {}

local function nextIndex(key, count)
	local bag = bags[key]
	if not bag or #bag.items == 0 then
		local items = table.create(count)
		for i = 1, count do items[i] = i end
		for i = count, 2, -1 do
			local j = math.random(i)
			items[i], items[j] = items[j], items[i]
		end
		local last = bag and bag.last
		if last and count > 1 and items[count] == last then
			items[count], items[1] = items[1], items[count] -- never repeat across refills
		end
		bag = { items = items, last = last }
		bags[key] = bag
	end
	local index = table.remove(bag.items)
	bag.last = index
	return index
end

-- bank = { key = "Footstep_Metal", assets = { "rbxassetid://<id>", ... },
--          bus = "SFX", volume = 0.8, pitch = 0.05 }
function Play.at(bank, parent)
	local i = nextIndex(bank.key, #bank.assets)
	local player = Instance.new("AudioPlayer")
	player.Asset = bank.assets[i] -- VERIFY: Asset or AssetId (get_roblox_docs)
	player.PlaybackSpeed = 1 + (math.random() * 2 - 1) * (bank.pitch or 0.05)
	player.Volume = (bank.volume or 1) * (1 + (math.random() * 2 - 1) * 0.1)
	local emitter = Instance.new("AudioEmitter")
	emitter.AudioInteractionGroup = bank.bus
	emitter.Parent = parent
	player.Parent = emitter
	Buses.wire(player, emitter)
	player:Play()
	player.Ended:Once(function() emitter:Destroy() end) -- VERIFY the event name
	return player
end

function Play.ui(bank) -- 2D, straight into a bus
	local i = nextIndex(bank.key, #bank.assets)
	local player = Instance.new("AudioPlayer")
	player.Asset = bank.assets[i] -- VERIFY: Asset or AssetId
	player.PlaybackSpeed = 1 + (math.random() * 2 - 1) * (bank.pitch or 0.02)
	player.Parent = Buses.root
	Buses.wire(player, Buses.buses[bank.bus or "UI"])
	player:Play()
	player.Ended:Once(function() player:Destroy() end)
	return player
end

return Play
```

- For very frequent sounds (footsteps, rapid fire), pool and reuse AudioPlayers per variant instead of creating new ones, and preload the assets (`ContentProvider:PreloadAsync`) so the first play has no delay.
- **Voice limits (SC12):** keep a count of live players per bank; when the cap is reached, stop the oldest before starting a new one.
- Log the chosen variant index in debug builds (for example as an attribute or a print behind a debug flag). The audit uses this to prove there are no immediate repeats.

**SR5 Footsteps by surface.** Read `Humanoid.FloorMaterial` on each step (or raycast down from the foot for custom surfaces tagged with an attribute) and pick the bank. Drive the step timing from the walk animation's markers (`AnimationTrack:GetMarkerReachedSignal`) so steps land on the feet, or from distance travelled. Running uses a louder, longer-range bank.

## 4. Music and ambience in code
**SR6 Layered music.**
- Start all stems on the same frame (create and load them first, then call `Play` on each in one loop). Stems are the same length and loop.
- Fade layers with a tween on each stem's own AudioFader (`TweenService` on `Volume`), 1-4 s.
- Long assets can drift. If drift is audible, re-sync every few seconds: set each stem's `TimePosition` to the master stem's.
- **Bar boundaries:** `barLength = 60 / bpm * beatsPerBar`; the next boundary is `math.ceil(master.TimePosition / barLength) * barLength`. Switch segments (horizontal) there, never mid-bar.
- Stingers play on the Music bus above the bed, or on SFX if they must cut through ducking.
- Uploads are capped at 7 minutes, so keep stems and segments under that and loopable.

**SR7 Ambience zones.** Mark each area with a zone part (or use the level's area folders). On the client, when the listener enters a zone, crossfade the bed over 1-3 s, start that zone's spot emitters, and schedule one-shots from its pool every 5-30 s at random positions around the listener (an emitter on a temporary attachment). Set reverb per zone with an AudioReverb on the Ambience and SFX path, or `SoundService.AmbientReverb` as the simple option.

**Acoustic Simulation (optional).** As of late 2026, Roblox describes it as a client beta usable in published experiences: enable `SoundService.AcousticSimulationEnabled` and emit through AudioEmitter, and thicker parts occlude and muffle more. Lower-end devices may degrade or disable it. Use it only for 3D emitters in stealth and horror spaces, never make a gameplay-critical cue depend on it, and test on low-end devices. Check its current status before relying on it.

## 5. Uploads
**SR8 Upload rules** [doc, as of late 2026; check the current limits before a big batch]:
| Rule | Value |
|---|---|
| Formats | .mp3, .ogg, .wav, .flac; single track |
| File size | under 20 MB |
| Length | 7 minutes or less |
| Sample rate | 48 kHz or less (export at 44.1 or 48 kHz) |
| Channels | mono, stereo, 3.0 or 5.1 |
| Monthly quota | about 2,000 per 30 days for ID-verified accounts, about 100 for unverified |
| Classification | auto-classified as sound effect or song; must pass moderation and copyright checks before use |
| Mono or stereo | mono for anything spatialized (3D emitters); stereo for music and 2D beds |
| Preparation | trim silence at the head; make loops sample-accurate (cut at zero crossings or crossfade the tail); normalize (beds about −18 LUFS, one-shot peaks ≤ −1 dBTP); prefer .ogg for size |

Studio transcodes imports; an import error usually means a malformed file. Re-export it from an up-to-date tool.

**SR9 The permissions gotcha.** Since March 2022, uploaded audio is **private** to its owner (the user or group that uploaded it).
- An experience can only play private audio its owner owns, or audio that has been granted to it. Grants are by **experience (universe)**, not by place.
- **Upload under the same owner as the experience** (the group, if the game is group-owned), so permissions are automatic.
- **A sound that plays in Studio but is silent in a live server is almost always a permissions problem.** Check it before anything else.
- Someone else's private audio ID will be silent. Only use Creator Store assets or your own uploads.
- Creator Store assets, including Roblox's licensed partner library, are usable in any experience.

Who owns the studio's experiences, and where uploads should go, are studio-specific: read `studio-profile.md` at the project root if it exists. Never put account names or IDs in shared files.

## 6. Legal sources, in priority order
**SR10** Source in this order, and stop at the first that fits:
| # | Source | Commercial game use | Attribution | Rules |
|---|---|---|---|---|
| 1 | **Roblox Creator Store, Roblox and partner uploads** (Roblox's licensed library, including Pro Sound Effects, APM Music, Monstercat, and as of mid 2026 Too Lost) | yes, **on Roblox only** | no | No upload or permissions work. Licensed music may not be downloaded or exported. Prefer Roblox-created or verified partner results. |
| 2 | **Audio we own**: recorded, synthesized or composed by the studio, or made for us under a written work-for-hire or license | yes | per the contract | Keep the contract or a note of who made it. |
| 3 | **CC0** (for example Kenney audio packs, Freesound filtered to CC0) | yes | no | Generic packs need processing to fit the setting (SC20). |
| 4 | **Royalty-free game licenses** (for example the yearly Sonniss GDC Game Audio Bundle) | yes | usually no | No redistribution of raw files; keep uploads private. Read the current license text. |
| 5 | **CC BY** (for example Freesound CC BY, Incompetech) | yes | **required** | Credit in game and in the experience description (SR12). Incompetech tracks are heavily overused; avoid them for anything signature. |
| 6 | **Royalty-free "no attribution" sites** (for example Pixabay) | yes, by their license | no | No standalone redistribution. Some tracks have triggered Content ID claims elsewhere; keep proof of the license and the download. |

**Never:**
- NC (non-commercial) licenses of any kind, including Freesound CC BY-NC and legacy Sampling+ (treat as NC). Monetized games are commercial.
- CC BY-SA and GPL audio (share-alike terms are awkward for game assets).
- BBC Sound Effects (non-commercial), the YouTube Audio Library (licensed for YouTube videos), "free for personal use" packs.
- Popular music, film, TV or game audio, and anything ripped.
- Random community uploads on the Creator Store with unknown rights; they may be re-uploads of copyrighted material.
- AI-generated audio, unless the generator's terms grant commercial rights and the result passes the de-AI check (SC20).

**Third-party files we upload stay private** to our experiences. Never distribute them on the Creator Store; that is redistributing the raw sound.

If a source's license page can't be read, don't use the source until it can.

## 7. Credits
**SR11 Log every asset in `CREDITS.md` at the moment you add it**, from `CREDITS-TEMPLATE.md` in the `sound` folder: asset ID, name, where it is used, source, source URL, license, attribution text, where the license proof is saved, date, and (for uploads) which owner uploaded it and whether it is private. Save license proof (a screenshot of the license page or the download receipt) to `design/<game>/licenses/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default).

**SR12 The in-game credits screen.** Every CC BY asset, and any asset whose license asks for credit, appears in an in-game Credits screen and in a credits line or link in the experience description: title, author, source, license. Build the screen from one ModuleScript so it can't drift from the file:

```lua
-- ReplicatedStorage/Credits (ModuleScript): generated from CREDITS.md
return {
	{ title = "<track or sound title>", author = "<author>", source = "<site>", license = "CC BY 4.0", url = "<link>" },
}
```

The Credits screen lists each entry as "Title by Author, Source, License". A minimal builder, to open from the settings or pause menu:

```lua
-- StarterPlayerScripts/UI/CreditsScreen (ModuleScript, required once by the
-- menu's LocalScript). Replace the plain styling
-- with the game's own fonts, colors and frame art (de-ai-ui).
local Players = game:GetService("Players")
local Credits = require(game:GetService("ReplicatedStorage"):WaitForChild("Credits"))

local gui = Instance.new("ScreenGui")
gui.Name, gui.ResetOnSpawn, gui.Enabled = "Credits", false, false
gui.Parent = Players.LocalPlayer:WaitForChild("PlayerGui")

local list = Instance.new("ScrollingFrame")
list.Size, list.Position = UDim2.fromScale(0.6, 0.7), UDim2.fromScale(0.2, 0.15)
list.AutomaticCanvasSize, list.CanvasSize = Enum.AutomaticSize.Y, UDim2.new()
list.Parent = gui
local layout = Instance.new("UIListLayout")
layout.Padding = UDim.new(0, 6)
layout.Parent = list

for _, c in Credits do
	local line = Instance.new("TextLabel")
	line.Size, line.AutomaticSize = UDim2.new(1, -12, 0, 0), Enum.AutomaticSize.Y
	line.TextWrapped, line.BackgroundTransparency, line.TextScaled = true, 1, false
	line.TextXAlignment = Enum.TextXAlignment.Left
	line.Text = string.format("%s by %s, %s, %s", c.title, c.author, c.source, c.license)
	line.Parent = list
end

return gui -- the menu toggles gui.Enabled
```

Style it with the game's UI language (`de-ai-ui`); a credits screen is still part of the game, and it must be readable on a phone (`capture_device_matrix`). Roblox and partner library audio needs no credit, but a "Sound effects courtesy of the Roblox Creator Store" line is a reasonable courtesy if the studio wants one.

## 8. The MCP workflow: search, preview, insert, log credits
**SR13** Two MCP servers can search and insert audio. Use whichever your session has.
- **Built-in Roblox Studio MCP:** `search_asset` with `assetType = "Audio"`, `scope = "creator_store"`, `priceFilter = "free"`, and `audioMinDuration` / `audioMaxDuration`, `verifiedCreatorsOnly`, `maxResults` (up to 20). `scope = "auto"` searches the experience, then group, then user inventory, then the Creator Store. `insert_asset` inserts. It warns when a result's creator is not the place owner: for Roblox-created or verified partner library audio that is expected; for any other creator, ask the user before inserting.
- **Community robloxstudio MCP:** `search_assets` with `assetType = "Audio"`, a query, `sortBy` (for example `Relevance` or `AudioDuration`) and `robloxCreatedOnly`. Results include the asset ID, name, a description (partner tracks include duration, category and a "Courtesy of" line) and duration. `preview_asset` can return an inline preview; `get_asset_details` gives more detail; `insert_asset` inserts.

Steps:
1. **Search with sound-designer words:** "interior", "room tone", "distant", "loop", "one shot", the material, the era, the place. Use a minimum duration of about 30 s for beds and a maximum of about 3 s for one-shots.
2. **Prefer** Roblox-created and partner results, then verified creators. Skip anything with an unknown uploader.
3. **Preview** (`preview_asset`, or play it in Studio). Check the description and metadata for: loop cleanliness, a watermark voice, music under an SFX, length. An agent can't judge how it sounds; when the choice matters (music, signature sounds, threat tells), shortlist 2-3 and ask the user to listen.
4. **Insert.** As of late 2026, inserting audio through the MCP was not yet tested in this studio's research. Check what was actually created (a legacy Sound or an AudioPlayer) with `search_objects` or `inspect_instance`, then move its asset into the bus structure (an AudioPlayer on the right bus, through an emitter for 3D). Delete the inserted helper object if you only needed the ID.
5. **Log** the asset in `CREDITS.md` immediately (SR11).
6. **Test in a live session** (SR14).

**SR14 Verify in a live session.** In a `solo_playtest`:
- Read `get_runtime_logs` for failed asset loads.
- Read with `eval_client_runtime` that each AudioPlayer's `IsReady` (or the current equivalent; verify) is true and that it is playing when it should.
- Any sound that is silent live but plays in Studio: check permissions first (SR9).
- `get_scene_analysis` with its audio memory mode once per milestone.

## 9. Legacy fallback
For an existing game on legacy audio:
- **Sound:** `SoundId`, `Volume`, `PlaybackSpeed`, `Looped`, `TimePosition`, `RollOffMode`, `RollOffMinDistance`, `RollOffMaxDistance`, `SoundGroup`. Parent to a part or attachment for 3D; to SoundService or a GUI for 2D.
- **SoundGroup** is the bus; effects parented to it apply to everything in it.
- **Ducking:** `CompressorSoundEffect.SideChain` takes a SoundGroup.
- `SoundService:PlayLocalSound(sound)` plays a client-only 2D sound (good for UI).
- Migrate to the new API when the game next gets a sound pass. Do not mix both for the same bus.

## Output
This skill feeds `SOUND-PLAN.md` and `CREDITS.md`; it has no document of its own. Present the work to the user with the chat overview defined in the Output section of `sound`.

## Common mistakes
- Assuming a property name from memory instead of checking `get_roblox_docs`.
- Building buses on the server, so per-player volume sliders can't work.
- Leaving the automatic listener on alongside custom listeners, so 3D sounds play twice.
- Uploading under a personal account when the game is group-owned, then finding every sound silent live.
- Logging credits at the end of the project.
- Using a "free" track without reading its license, or a community upload of unknown origin.
- Stereo files on 3D emitters (they don't spatialize as expected); use mono.

## Sources
- Audio objects: https://create.roblox.com/docs/audio/objects
- Audio effects: https://create.roblox.com/docs/audio/effects
- Audio assets, upload limits and permissions: https://create.roblox.com/docs/audio/assets
- Class references: https://create.roblox.com/docs/reference/engine/classes/AudioCompressor ; https://create.roblox.com/docs/reference/engine/classes/Wire ; https://create.roblox.com/docs/reference/engine/classes/AudioEmitter
- Audio privacy change, 2022: https://devforum.roblox.com/t/1701697
- Acoustic Simulation: https://devforum.roblox.com/t/beta-acoustic-simulation/3634265 ; https://devforum.roblox.com/t/full-release-acoustic-simulation-emit-audio-with-presence/4307121
- Licensed music: https://en.help.roblox.com/hc/articles/360000927163 ; https://devforum.roblox.com/t/launching-music-on-the-game-details-page-and-new-songs-from-too-lost/4760221
- Free sources and licenses: https://gdc.sonniss.com/ ; https://freesound.org/help/faq/ ; https://pixabay.com/service/license-summary/ ; https://kenney.nl ; https://opengameart.org ; https://incompetech.com
