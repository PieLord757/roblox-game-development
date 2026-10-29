# <Game name>: characters

Copy this file to `design/<game>/CHARACTERS.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and fill it in. Delete these instruction lines and any section that does not apply. Use real hex codes from this game's `ART-DIRECTION.md` where `#RRGGBB` appears (lines still containing the placeholder are ignored by the palette script).

Status: draft / sheet sent <date> / approved by user <date>

## 1. Avatar vs custom (required, decide first)
- **Players:** keep / constrain / replace
- **Reason:** <one or two sentences, citing the decision rules in character-design-roblox>
- **Bots (if the game fills empty slots with bots):** <what bots look like and why>
- **Extreme-avatar test (only if keeping or constraining):** tiny ___, huge ___, non-humanoid ___; result ___
- **NPCs and monsters:** custom (always)

## 2. Palette choice (required)
- Other games lean on: <colour families from the palette script's family table>
- This game owns: <dominant family> with <accent family>, because <reason from this world's references>
- Overused combinations used anyway (D3), and why they suit this world: <or "none">

## 3. Cast (required: five fields for every character)
Every character, major or minor, has all five. Keep each to a line.

### <Character name>
- **Role:** <what they do in play and in the story>
- **Silhouette hook:** <the one thing you recognise them by in flat black at play distance>
- **Shape language:** dominant <circle / square / triangle> (<meaning>), secondary <shape> (<meaning>); subversion: <or none>
- **Palette colours:** #RRGGBB (<where on the body>), #RRGGBB (<where>); saturation budget sits on <area>
- **Personality (one line):** <a behaviour, not an adjective>

<repeat per character>

## 4. Majors and monsters only (recommended)
Skip for minor NPCs to keep the work in hours.

### <Character name>
- Primary trait (never changes) and why it fits the world:
- Read order: 1 s ___ / 3 s ___ / 10 s ___
- Proportions: height ___ studs, head:body ___, mass distribution ___
- Want / false belief / need / wound (majors): see `STORY.md` section ___
- Visible detail (how it shows in game: idle, prop or line):
- Monsters: cue ___ / rule ___ / counter ___
- Rig: R6 / R15 / custom / no rig, because ___
- Triangles ___ / textures ___ (budget: hero 8k, major 6k, minor 2.5k)
- Animations: idle ___ / locomotion ___ / signature action ___
- Sound signature:
- Measured on-screen height at farthest reaction distance (V2): ___ pt at ___ studs
- Generated or store assets: source, prompt (logged verbatim), what was changed by hand

## 5. Studio fingerprint (one block per game)
- Palette role formula: dark ___, light ___, accent ___, danger ___, light source ___
- Accent hue (degrees) and hex: #RRGGBB
- Danger signal: colour + sound + shape (or "no colour, uses ___")
- Signature character material(s):
- Rig types used:
- Proportion scheme: head:body ___, height range ___ studs, mass distribution ___
- Cast shape mix: circle __% / square __% / triangle __%
- Rendering treatment: PBR / palette texture / flat / emissive-led / other
- Motion style:
- Monster cue senses used:
- Naming scheme (source, era, pattern):

## 6. Checks
| Check | Result | Evidence |
|---|---|---|
| V1 silhouette | | screenshots/characters/<date>/ |
| V2 distance (phone) | | |
| V3 grayscale | | |
| V4 lineup | | |
| R2/R3 budget | | |
| R4 animations replicate (multiplayer playtest) | | |
| Latest audit | | audit/<date>/CHARACTER-REPORT.md |

## 7. Distinctness: notes and fails
Overlap is normal and is a note. Only F1 (same base model, unedited), F2 (same model + palette + proportions), F3 (unedited free Creator Store character) fail.

| Character | Other game | Kind (note # or F1/F2/F3) | What overlaps | Decision and reason |
|---|---|---|---|---|
| | | | | |

## 8. Screenshot sheet and approval
- Sheet: <path to silhouette lineup, colour lineup, grayscale, phone shots>
- Chat overview sent to user: <date>
- User response: <approved / changes requested: ___>
