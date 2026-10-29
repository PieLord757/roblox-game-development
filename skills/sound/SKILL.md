---
name: sound
description: "Start here for any sound, music, ambience, footstep, UI sound or audio-mix work in a Roblox game. Explains why audio is half of how a game feels and informs, the legal sourcing rule (a prioritized list of legal sources: Roblox's licensed library, audio we own, CC0, royalty-free game licenses, CC BY with credit, royalty-free no-attribution sites with proof; never copyrighted, NC or unknown-rights audio), the process (event list, SOUND-PLAN.md, sourcing and credits, buses, mix, audit), and which sound sub-skill to load (craft, roblox, audit). Use before adding, sourcing, uploading, mixing or reviewing any audio."
---

# Sound (start here)

## Why sound matters
Players judge a game by how it feels, and much of feel is sound. A hit with no sound did not land. A footstep that repeats the same sample sounds cheap within ten steps. A horror corridor with no sound is a corridor; the same corridor with a drip, a hum and something moving behind the wall is a level. Sound also carries information the screen can't: what is behind you, what is about to attack, whether your shot hit, whether a guard is suspicious.

On Roblox:
- Most games use the same handful of free sounds, so stock audio is recognized instantly and reads as low effort.
- Many players are on phone speakers with no bass, and many play muted. Every cue that matters must read on a phone and also have a visual counterpart.
- **Audio is a legal risk.** Uploading music you don't hold the rights to breaks the Terms of Use, can get assets removed and the account actioned. Since 2022 uploads are private by default, so a sound that plays in Studio can be silent in a live server.

`de-ai-feel` sets the floor: no silent actions, and 2-3 variations for any repeated sound. These skills go deeper: how to design, layer, mix, source and verify audio so the game sounds made on purpose for its world.

**The standard:** every action and event has a sound designed for this game's world; every threat can be heard before it acts; the mix puts what matters on top; and every asset has a known, legal source in the credits file.

## The legal rule (this blocks)
- **SG1** Audio comes only from these legal sources, in priority order (stop at the first that fits; the full table with each source's rules is SR10 in `sound-roblox`):
  1. the Roblox Creator Store's licensed library (Roblox and partner uploads), licensed for use on Roblox only;
  2. audio we own: made by us, or made for us under a written license that allows commercial game use on Roblox;
  3. CC0 audio;
  4. royalty-free game licenses (for example a game audio bundle whose license allows commercial game use);
  5. CC BY audio, credited in game and in the experience description;
  6. royalty-free "no attribution" sites, used under their license.

  For every third-party source (3 to 6), save the license proof.
- **Never** copyrighted music or sound we don't hold rights to: popular songs, film, TV or game soundtracks, ripped audio, "free for personal use" packs, non-commercial (NC) licenses, share-alike licenses (CC BY-SA, GPL), YouTube Audio Library tracks, random community uploads of unknown origin.
- Third-party files we upload stay **private** to our experiences and are never distributed on the Creator Store.
- If `studio-profile.md` sets a stricter rule (for example Creator Store and owned audio only), it wins.

The full source list, license rules and the credits workflow are in `sound-roblox`.

## What this skill produces
For each game:
1. **`SOUND-PLAN.md`** in the game folder (the path set in `studio-profile.md`, or `design/<game>/` by default), copied from `SOUND-PLAN-TEMPLATE.md` in this folder. It holds:
   - **every action and event with its sound** (the event list), including UI and threats
   - **the music direction with references** (what it should feel like, which strategy, and real reference tracks for direction only, never to upload)
   - **the mix levels**: bus volumes, ducking, voice caps and priority tiers
   - an audio map per area (ambience bed, spot emitters, one-shot pool, reverb, music state, silence moments)
2. **`CREDITS.md`** in `design/<game>/`, copied from `CREDITS-TEMPLATE.md`: every asset with its ID, source, license and attribution, plus the in-game credits text.
3. **The audio in the game**: buses, sounds, music system and a player settings menu with per-bus sliders.
4. **A chat overview** each time the plan or a sound pass is shown (see "Output").

## The process
Keep it in hours, not days.
1. **Event list.** From the game design and every `LEVEL-PLAN.md`, list every player action, threat tell, UI action, pickup, objective change and set piece. No silent actions.
2. **Direction.** Pick the music strategy, the UI sound family from the setting, the ambience per area, and 3-5 reference tracks or games for direction. Use `sound-craft`.
3. **Plan.** Fill in `SOUND-PLAN.md`. Show the user a chat overview of the direction (strategy, references, UI family, two or three signature sounds) before sourcing in bulk.
4. **Source.** Search the Creator Store first through the MCP tools, then owned audio, then licensed third-party audio. Preview before inserting. Log every asset in `CREDITS.md` as you go, not at the end. Use `sound-roblox`.
5. **Build.** Buses on the new Audio API, 3D emitters, variation banks, footsteps by material, ambience zones, the music system, ducking, the settings sliders, and the in-game credits screen. Use `sound-roblox`.
6. **Mix and verify.** Set levels by priority, run the repeat test and the log checks, and ask the user for the listening checks (phone speaker, fatigue, music fit) that an agent can't hear.
7. **Audit.** Run `sound-audit` with a fresh reviewer at the end of the milestone. Fix, re-audit, then show the user.

## Which sub-skill to load
| You need | Load |
|---|---|
| Music layering and re-sequencing, stingers, SFX layering and variation, audio as information, threat tells, the mix priority, ambience, silence, UI sounds from the setting, genre notes for horror, thriller, heist and arena | `sound-craft` |
| The new Audio API with a bus setup and code, ducking, 3D emitters, the legacy fallback, upload rules, the permissions gotcha, legal sources in priority order, the credits screen, the MCP search, preview, insert and log-credits workflow | `sound-roblox` |
| Reviewing a game's audio: coverage, variation, buses, logs, legality, visual counterparts, the user listening checks | `sound-audit` (run by a fresh reviewer subagent) |

Load `sound-craft` and `sound-roblox` together for any build. Also load `de-ai-feel` (the floor for every action) and, for each space, its `LEVEL-PLAN.md`.

## Rule index
| IDs | Area | Lives in |
|---|---|---|
| SG1 to SG4 | Gates (legal rule above, and below) | this file |
| SC1 to SC20 | Craft: music, SFX, information, mix, ambience, silence, UI, genres | `sound-craft` |
| SR1 to SR14 | Roblox: buses, wiring, variation code, uploads, permissions, sources, credits, MCP workflow | `sound-roblox` |

## The gates (these block)
- **SG1** The legal rule above. Any asset with an unknown, NC or ripped source fails the audit and blocks publishing.
- **SG2** Every asset in the game appears in `CREDITS.md` with its source and license, and every CC BY asset appears in the in-game credits and the experience description.
- **SG3** No silent player action and no threat without an audio tell, unless `SOUND-PLAN.md` gives a design reason.
- **SG4** Every critical cue (threat tells, objective changes, damage, detection) has a visual counterpart for muted players.

## What great sounds like
- **You could play with your eyes half closed.** Threats announce themselves with unique, learnable sounds before they act; footsteps tell you who and where.
- **Nothing repeats like a machine gun.** Frequent sounds have 3-5 variants, pitch spread, and never the same variant twice in a row.
- **The mix has a top.** Tells and dialogue sit over player feedback, over music, over ambience. When a lot happens, the important thing is still clear.
- **Places sound different.** Each area has its own bed, reverb and one-shots, and you could tell where you are with the screen off.
- **Music means something.** It is withheld, then it arrives, and its arrival is information. Silence is used on purpose.
- **It belongs to this world.** The UI clicks and the music could only belong to this game's setting, not any game.

## Common mistakes
- Default or stock free-model sounds that players have heard in a hundred games.
- One sample per action, played identically every time.
- Music playing constantly at the same level, so it becomes wallpaper and fatigues.
- Everything at full volume, so nothing reads.
- Important cues that are only bass, which vanish on phone speakers.
- Generic sci-fi bleeps for UI in a game that is not set in a spaceship.
- Sourcing first and logging credits "later", then nobody knows where a sound came from.
- Uploading a track because it was labeled "free" without reading the license.
- A sound that is silent in the live game because of permissions, found by players instead of the build thread.

## Output
1. **`design/<game>/SOUND-PLAN.md`** and **`design/<game>/CREDITS.md`**, kept current.
2. **A chat overview, as an explicit step,** whenever the plan is first written and after each sound pass. The user should understand the audio direction in under a minute without opening the file:
   - the music direction in one or two sentences, with the reference tracks or games named
   - the music strategy in plain words ("quiet ambience while exploring; drums come in when a guard is suspicious; full band when the alarm trips")
   - the UI sound family and why it fits the setting
   - three signature sounds the player will remember, one line each
   - sources used (how many Creator Store, owned, licensed third-party) and whether any attribution is required
   - anything silent, missing or unverified
   - what you need: listening checks from the user (see `sound-audit`), approval of the direction, or a choice between options
   Do not paste the whole plan into chat.

## Studio-specific facts
Who owns the experience (user or group), where uploads go, any stricter sourcing rules, the studio's preferred music partners, and the user's listening setup are studio-specific. Read `studio-profile.md` at the project root if it exists. If it doesn't, follow the defaults here and note your assumptions in `SOUND-PLAN.md`.

## Tools
- Searching and inserting audio: `search_asset` and `insert_asset` (built-in Roblox Studio MCP); `search_assets`, `preview_asset`, `get_asset_details` and `insert_asset` (community robloxstudio MCP).
- Building: `execute_luau`, `multi_edit`; `set_script_source`, `edit_script_lines`.
- Verifying: `solo_playtest`, `eval_client_runtime`, `eval_server_runtime`, `get_runtime_logs`, `get_scene_analysis` (including audio memory).
- Docs: `get_roblox_docs` for every audio class and property before relying on it. The audio API has changed across releases.

Tool name prefixes differ between installs. Use whatever prefix your session shows.

## Sources
The full source list with links is at the end of `sound-craft` and `sound-roblox`. Key ones: the Overwatch "Play by Sound" GDC talk, DOOM (2016) music GDC talk, Alien: Isolation GDC talks, Dead Space fear-emitter interviews, GDC 2021 talks on vertical and hybrid music structure, and the Roblox Creator Docs on audio objects, effects, assets and permissions.
