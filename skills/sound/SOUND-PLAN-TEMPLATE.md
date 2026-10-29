# <Game name>: sound plan

Copy this file to `design/<game>/SOUND-PLAN.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and fill it in. Delete these instruction lines and any section that does not apply. Rule IDs (SG, SC, SR) refer to the sound skills.

Status: draft / direction approved by user <date> / sourced / mixed / audited <date>

## 1. Sound identity (required)
- **Setting in one line:** <where and when; from ART-DIRECTION.md>
- **What the game should sound like, in one sentence:** <for example "close, dry and mechanical, with long silences broken by something in the walls">
- **Three signature sounds** the player will remember:
  1.
  2.
  3.
- **Sourcing rule:** default (SG1 priority list: Creator Store library, owned, CC0, royalty-free game licenses, CC BY with credit, no-attribution sites with proof) / stricter rule from `studio-profile.md`: <rule>

## 2. Music direction (required)
- **Strategy (SC1):** vertical layers / horizontal segments / hybrid / fear emitters / sparse. Why: <one line>
- **What drives it:** <intensity value, state machine, proximity to threats, heist phase, round state>
- **Where music is withheld (SC3):** <areas or states that run on ambience only>
- **Instrumentation and feel:** <instruments, tempo range, mood words specific to this world>
- **References (direction only; never upload these):**
  | Reference (track, score or game) | What we take from it |
  |---|---|
  | | |
- **Sources for the actual music:** Creator Store library search terms / owned or commissioned / licensed third-party

### States, layers and segments
| State or intensity | Layers or segment playing | Enters when | Leaves when | Transition (fade s, bar switch, stinger) |
|---|---|---|---|---|
| | | | | |

- BPM and beats per bar (for bar-boundary switching, SR6):
- Stingers:
  | Stinger | Event | Bus |
  |---|---|---|
  | | | |
- **Silence moments (SC15):** <where the music drops to room tone, and why>

## 3. Event list (required: every action and event with its sound)
No silent actions (SG3). Every threat has a unique tell (SC7). Every critical cue has a visual pair (SG4).
Priority tier: 1 tells and dialogue, 2 player feedback, 3 enemies and others, 4 music, 5 ambience, 6 decor.

| Event | Trigger | Sound (what it should sound like) | Layers (SC4) | Variants | 2D/3D | Bus | Range (studs) | Tier | Visual pair | Asset IDs | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Footstep, metal | step on Metal | | | 4+ | 3D | SFX | 40-80 | 2 | n/a | | | |
| <core action> | | | | | | | | | | | | |
| <threat> tell | <s> before it acts | | | | 3D | SFX | | 1 | | | | |
| UI confirm | button press | | | 2-3 | 2D | UI | n/a | 2 | n/a | | | |

### Footstep banks (SC6, SR5)
| Surface (FloorMaterial or tag) | Walk bank | Run bank | Landing |
|---|---|---|---|
| | | | |

### Barks (stealth and AI games, SC9)
| State | Line(s) | Variants |
|---|---|---|
| Unaware | | |
| Suspicious | | |
| Searching | | |
| Alert | | |
| Lost you | | |

### UI sound family (SC16, SC17)
- Family and source material, derived from the setting: <for example "rotary dial, register drawer, tape deck clunk">
- Confirm (rising) / cancel (falling) / navigate (neutral) / error / reward:

## 4. Audio map per area (required for each area in the level plans, SC14)
### <Area name> (from `levels/<space>/LEVEL-PLAN.md`)
- Bed:
- Spot emitters (2-4):
- One-shot pool and interval (5-30 s):
- Reverb character:
- Music state:
- Silence moments or "life stops" tells:
- Crossfade to neighbors (1-3 s):

## 5. Mix levels (required)
| Bus | Default volume | Ducked by | Duck amount (dB) | Voice cap per sound type | Notes |
|---|---|---|---|---|---|
| Music | | Dialogue | 3-8 | n/a | |
| Ambience | | Dialogue | 3-8 | | |
| SFX | | set-piece moments | | footsteps ≤ 4, shots ≤ 6 | |
| Dialogue / barks | | none | | | |
| UI | | none | | | |
| Master | compressor threshold <dB>, ratio <n> | | | | |

- Loudness prep before upload: beds about −18 LUFS, one-shot peaks ≤ −1 dBTP (SC11)
- Listener position: camera / character head (SR2)
- Player settings sliders: Music, Ambience, SFX, Dialogue, UI

## 6. Build notes
- API: new Audio API / legacy (reason)
- Acoustic Simulation: off / on for <areas>, never gameplay-critical
- Owner for uploads (user or group): see `studio-profile.md`
- Credits: `CREDITS.md`; in-game credits screen location:

## 7. Listening checks (filled in by the user, see sound-audit)
| Check | Date | Result |
|---|---|---|
| Phone speaker | | |
| Fatigue (10 min) | | |
| Music fit | | |
| Repeat | | |
| Ducking | | |
