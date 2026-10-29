---
name: sound-craft
description: The craft of game audio for Roblox games, platform-independent. Adaptive music (vertical layering, horizontal re-sequencing, hybrids, fear emitters, stingers), SFX layering and variation, distance versions, footsteps by surface, audio as information (threat tells, confirmations, state barks, relevance), the mix priority, ducking, voice limits and loudness, ambience beds and one-shots, silence as a tool, UI sounds derived from the setting, and genre notes for horror, thriller, heist and arena games. Use while writing SOUND-PLAN.md, choosing or designing any sound, and mixing. Extends de-ai-feel; load both.
---

# Sound: craft

Load `sound` first for the legal rule, the process and the gates. `de-ai-feel` sets the floor for every action (instant response, no silent actions, 2-3 variations, heavier sounds for big moments). This file goes deeper. Rules have IDs (SC1 to SC20). How to build each technique in Roblox is in `sound-roblox`.

Evidence tags: **[talk]** comes from a GDC talk, interview or developer article; **[observed]** is a pattern seen in successful games without a developer source.

## 1. Adaptive music
Music in a game should respond to what is happening. There are three tools, and most good scores combine them.

**Vertical layering (re-orchestration).** One piece is split into synchronized stems (pad, percussion, bass, lead). All stems play from the start on the same timeline; the game fades layers in and out with intensity. Transitions are seamless because the stems never stop. [talk: GDC 2021, "Pure Vertical Layering"]
- Best for **continuous** intensity: alertness in stealth, distance to a chaser, how many enemies are near.
- Write or pick stems that sound complete at every layer count. The bottom layer alone must work as an exploration bed.

**Horizontal re-sequencing.** Music is cut into segments (explore, tension, combat, victory) and the game picks the next segment at a musical boundary (the end of a bar or phrase). Seams must be inaudible. [talk: Winifred Phillips; Crowley on Elias]
- Best for **discrete** state changes: exploring, then fighting, then won.
- Every segment needs an exit at bar boundaries, and ideally a short transition piece (a fill, a riser) into the next.

**Hybrid.** Segments for states, with layers inside each segment. This is what most shipped games do. [talk: GDC 2021, "Hybrid Horizontal-Vertical Structure"]

**Fear emitters (proximity-driven layers).** Dead Space attached a "fear" value to threats and scripted spots; the summed fear near the player mixed four layers of dread music in real time. The music feels reactive without explicit states. [talk: Don Veca interviews] This is vertical layering driven by distance instead of a state machine, and it suits horror and stealth well.

**Stingers.** Short one-shots over the bed that mark an event (discovery, detection, death, a door opening) without changing the bed.

**DOOM (2016).** Exploration gets ambient beds; arenas get full-power tracks that track the fight; when the arena is cleared, the music resolves and the silence afterward is part of the reward. [talk: Mick Gordon, GDC 2017]

- **SC1** Pick a music strategy per game and write it in the plan: which states or intensity values exist, what drives them, which layers or segments play in each, and what the stingers are. Default choices:
  | Game shape | Strategy |
  |---|---|
  | Linear run with threats | vertical layers by danger; stingers on threat reveals |
  | Hub with dangerous wings, or a vertical climb | fear-emitter layers, with long ambience-only stretches |
  | Investigation or memory sequences | sparse, held textures; music only for discoveries |
  | Heist or open sandbox with phases | vertical stems by phase (casing, inside, alarm, escape) |
  | Arena or round-based PvP | horizontal tracks per round state; a round-end stinger |
- **SC2** Music changes only on musical boundaries (bars), never mid-phrase, except stingers. Fades between layers take 1-4 seconds; a cut is a deliberate effect, not a default.
- **SC3** Music is withheld somewhere. If music plays all the time, it stops meaning anything. Exploration runs on ambience; music arriving is itself information.

## 2. SFX design: layering and variation
**Layering.** A good sound is built from 2-4 layers:
- **transient or attack:** the click, snap or crack that tells the ear "now"
- **body:** the material and weight (a thump of wood, a ring of metal)
- **tail:** reverb, debris, the room
- **sweetener (optional):** a low sub for impact, a tonal ring for magic or technology, a whoosh before a swing

Each layer can vary on its own, which multiplies the combinations. Big moments get more layers and more low end; small actions get fewer and shorter.

- **SC4** Every important sound (the core action, the signature threat, the biggest reward) is designed from layers chosen for this game's world, not a single stock sample. Name the layers in the plan.

**Variation.** Identical repeats ("the machine-gun effect") are the most obvious sign of cheap audio.
- **SC5** Frequent sounds (footsteps, shots, hits, pickups) get 3-5 variants; any repeated sound gets at least 2-3 (the `de-ai-feel` floor). Randomize pitch by ±3-8% (PlaybackSpeed 0.94-1.06) and volume by about ±10%. Never play the same variant twice in a row (a shuffle bag, not plain random).

**Distance versions.** Gunshots, explosions and other loud events have a near and a far sample. Past a distance, swap to the far sample (duller, with a delayed tail), not just a quieter near one. Real distant sounds lose their high end and gain room.

**Footsteps by surface.** Pick the bank from what the foot is on: metal, concrete, wood, carpet, gravel, snow, glass, water.
- **SC6** One footstep bank per surface in the level's palette, each with 4+ variants. Running is louder, longer-range and heavier than walking. Landing from a jump is its own sound.

Overwatch gives each hero distinct footsteps so players can identify who is coming by ear. [talk: Lawlor and Neumann, GDC 2016] In a game with distinct enemies or classes, footsteps are identity.

## 3. Audio as information
Overwatch's audio pillars were a clear mix, pinpoint accuracy and gameplay information. Its mix ranks sounds by **relevance to this listener now**: enemies louder than friends, threats aimed at you louder than others, ultimates announced with distinct friendly and enemy voice lines. [talk: GDC 2016]

- **SC7 Threat tells.** Every threat gets a unique, learnable wind-up sound before it acts, early enough to react (0.5-2 s depending on the reaction needed). Players learn the threat by its sound: Doors' entities announce themselves with distinct sounds and light flicker, and players react by ear. [observed] Two threats never share a tell.
- **SC8 Confirmations.** Every successful action confirms itself: hit markers, kill confirms, pickups, objective progress, a door unlocking. Small actions get small sounds, big moments get heavier layered ones. Failure has its own sound too (a dull clunk for a locked door), so the player knows the input registered.
- **Footsteps as stealth information.** The player's noise should be legible: louder on metal, louder when running. Enemy footsteps reveal position. In PvP, footstep volume and range are balance levers; write them in the plan.
- **SC9 State barks.** In stealth and AI-heavy games, guards voice their state: unaware, suspicious ("Huh?"), searching, alert ("There!"), lost you. These are core readability, as in Hitman and Dishonored. Write them with `de-ai-story`.
- **SC10 Visual pairs.** Every critical cue has a visual counterpart (a subtitle, a direction indicator, a light change). Many mobile players play muted.

## 4. The mix
**Priority order, high to low:**
1. critical gameplay cues, tells and dialogue
2. player-action feedback
3. enemy and other-player actions
4. music
5. ambience
6. decorative one-shots

- **SC11** Set bus levels by this priority and write them in the plan. When a higher tier plays, lower tiers dip (ducking): music and ambience dip 3-8 dB under dialogue and barks; everything dips briefly under a set-piece explosion.
- **HDR audio** (DICE's Battlefield approach): only the loudest relevant sounds play at full level; quieter ones are lowered or culled. You can approximate it with voice limits and ducking.
- **SC12 Voice limits.** Cap concurrent instances per sound type (for example ≤ 4 footsteps, ≤ 6 gunshots audible). When the cap is hit, steal the oldest or quietest voice. Fifty overlapping sounds are mud.
- **Loudness.** Sony's ASWG-R001 recommendation is about −24 LUFS integrated for home and about −18 LUFS for portable devices (industry guidance; verify with your own device tests). Roblox has a large mobile share, so mixing toward about −18 to −16 LUFS overall is reasonable. Normalize files before upload (music beds about −18 LUFS, one-shot peaks ≤ −1 dBTP) so in-engine volumes stay meaningful.
- **Frequency space.** Carve room with EQ: music gives up some of 1-4 kHz where dialogue and tells live; ambience gives up lows so footsteps and impacts read.
- **SC13 Phone speakers** have almost no output below about 200 Hz. Every important sound needs mid and high content (1-4 kHz) to read on a phone. A sub-bass impact needs a click or crack on top.

## 5. Ambience
Ambience defines a place more than music does.
- **Bed:** a continuous room tone or exterior wash (engine rumble, ventilation hum, traffic, wind).
- **Spot loops:** positioned emitters (a buzzing light, a dripping pipe, a radio, machinery).
- **Random one-shots:** scheduled at random positions around the listener every 5-30 s (a distant door, a creak, a siren, a bird).
- **Reverb per space:** a small room is dry and close; a hall or atrium is long; a stairwell echoes; outdoors is almost dry.

- **SC14** Every area in the level plans gets an audio map: a bed, 2-4 spot emitters, a one-shot pool, a reverb character, the music state, and any silence moments. Beds crossfade over 1-3 s at area boundaries.
- **Diegetic music** (a radio, a jukebox, a record player in the world) is ambience and worldbuilding at once. Filter it (band-pass EQ) so it sounds like it comes out of the device, and position it in 3D. It must still follow the legal rule.

## 6. Silence
- **Contrast creates impact.** Drop to near-silence before a scare or a reveal, after clearing an arena, at a story beat.
- **SC15** "Silence" means room tone only, music out. Full digital silence sounds broken.
- **Sudden absence is a tell.** Ambient creatures or machinery stopping means a threat is near. It is cheap, diegetic and very effective.
- Plan the silences in the sound plan the same way peaks are planned in the level plan. A silence is a beat.

## 7. UI sounds
- **SC16** UI sounds are short (≤ 150-250 ms), soft, from one consistent family (same source material, same treatment). Pitch encodes meaning: rising for confirm, falling for cancel, neutral for navigation. No hover sounds on touch devices. Throttle repeated sounds (scrolling a list).
- **SC17 Derive the UI family from the setting.** Generic sci-fi bleeps are the audio version of a generic AI HUD. Examples by setting type:
  | Setting | UI sound family |
  |---|---|
  | Rail or vintage travel | ticket punch, carriage latch, a station bell |
  | Research facility or bunker | relay click, CRT tick, a pneumatic door |
  | Tower or office | elevator chime, a desk bell, a lift button |
  | Investigation or noir | camera shutter, typewriter key, a file drawer |
  | Period city or heist | rotary dial, cash register, tape deck clunk |
  | Fantasy | a page turn, a wooden latch, a bowed string pluck |
  | Competitive arena | crisp, short, readable game sounds; clarity over theme |
- UI sounds are non-spatial and go on their own bus, so the player's sliders control them.

## 8. Genre notes
### Horror
Alien: Isolation was built around "seeing with your ears": the creature's movement in the vents is audible and locatable, the motion tracker beeps, the foley is heavy and physical, and music reacts to the creature's proximity and state. Dead Space was an explicit inspiration. [talk: GDC 2015, "Building Fear in Alien: Isolation"; GDC foley talk]
- **Uncertainty:** off-screen sounds with no visible source.
- **Ambiguous positioning:** behind, above, inside the walls.
- **Low drones and dissonant beds:** sub rumbles, clusters, detuned strings, metal scrapes. Always pair lows with mid-range texture for phones (SC13).
- **Diegetic misdirection:** a phone ringing in an empty room, a radio that turns on.
- **The player's body:** breathing and heartbeat rising with danger. Use sparingly or it becomes a cliche.
- **SC18 Jump-scare budget:** at most one loud jump stinger per 10 minutes of play. Overuse teaches players to turn the volume down, and that kills all the other sound design. Telegraph with sound before sight; stop ambient life before a threat.

### Thriller and stealth
- Tension lives in the pulse layer: a low rhythmic element that enters when a guard is suspicious and builds with alertness.
- Detection gets a clear, unique stinger and a music change. Losing pursuit gets a resolving cue, so the player knows they are safe.
- Barks carry state (SC9). The music should never cover them; they sit at the top of the mix.

### Heist
- Vertical stems by heist phase: a groove bed while casing, a percussion layer when inside, the full band when the alarm trips, and a stinger when the vault or target opens. A period setting calls for that period's instruments, recording sound and tempos, taken from licensed or owned sources only, never from the era's real hit records.
- Tools and locks get satisfying mechanical foley; the moment a lock gives is a core reward sound.

### Arena and PvP
- Clarity beats atmosphere. Footsteps, reloads, ability wind-ups and hits must cut through.
- **SC19** Enemy sounds are louder or brighter than friendly ones, and threats aimed at the listener are louder than others (Overwatch's relevance rule). Footstep range is a balance number in the plan.
- Horizontal music per round state, a countdown that is readable without looking, and a round-end stinger. Music ducks hard under combat information.

### Memory, flashback or frozen-time sequences
- Sounds hang mid-decay: a held reverb tail, a sustained note. Replayed memories use filtered, pitched-down or smeared versions of the real event. Pitch shift, reverb, EQ and echo effects cover this.

## 9. What great sounds like (a checklist for your own plan)
- Every event in the game has a row in the event list.
- Every threat has a unique tell, early enough to react, and a visual pair.
- The core action's sound is layered and specific to this world.
- Frequent sounds have 3-5 variants with pitch spread and no immediate repeats.
- Areas sound different with the screen off.
- Music is withheld somewhere, and the silences are planned.
- The mix order is written down and the ducking supports it.
- The UI family comes from the setting.
- **SC20** The de-AI check: could this music and these UI sounds belong to any other game? If yes, re-source or re-process (EQ, layering, pitch, a recorded sweetener) until they belong to this one.

## Output
This skill feeds `SOUND-PLAN.md`; it has no document of its own. Present the work to the user with the chat overview defined in the Output section of `sound`.

## Common mistakes
- Picking music first and designing everything else around it. Start with the event list and the ambience.
- Loud, constant music. It covers the information and tires the player.
- A beautiful sound that tells the player nothing. Information first, beauty second.
- Threat tells that sound like ambience, so players can't learn them.
- Bass-only impacts that disappear on phones.
- Overused famous free tracks that 16+ players recognize at once.
- Mixing on headphones only. The mix must also be checked on a phone speaker, by a person.

## Sources
- Overwatch, "The Elusive Goal: Play by Sound", GDC 2016: https://gdcvault.com/play/1023010/Overwatch-The-Elusive-Goal-Play ; https://blog.audiokinetic.com/overwatch-game-audio-using-wwise-1/
- DOOM music, GDC 2017: https://gdcvault.com/play/1024068/-DOOM-Behind-the ; https://www.gamedeveloper.com/audio/video-making-the-music-of-i-doom-i-
- Alien: Isolation: https://gdcvault.com/play/1021852/Building-Fear-in-Alien ; https://www.gdcvault.com/play/1023223/Foley-in-Alien-Isolation-Gears ; https://www.pcgamer.com/the-audio-of-alien-isolation
- Dead Space fear emitters: https://gameinformer.com/b/features/archive/2009/12/11/feature-noises-in-the-dark-exploring-the-sounds-of-dead-space ; https://www.killscreen.com/dead-space-3s-fear-system-most-horrifying-audio-youll-ever-not-see/
- Adaptive music: https://www.gamedeveloper.com/game-platforms/pure-vertical-layering-for-game-music-composers-from-spyder-to-sackboy-gdc-2021- ; https://www.gamedeveloper.com/game-platforms/hybrid-horizontal-vertical-structure-for-game-music-composers-from-spyder-to-sackboy-gdc-2021- ; https://gamedeveloper.com/audio/music-game-plan-tactics-for-the-video-game-composer-part-two- ; https://gamedeveloper.com/audio/composing-adaptive-music-for-video-games-using-elias
- Sony ASWG-R001 loudness recommendation (industry guidance, not fetched; verify on devices).
- Roblox examples (Doors and similar) are observation only.
