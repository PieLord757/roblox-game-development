---
name: character-design-audit
description: "Audit a Roblox game's character cast. A fresh reviewer subagent that never edits scores every character against the character-design rules, runs a blind silhouette lineup and the cross-game distinctness check (palette script plus fingerprint comparison), and writes CHARACTER-REPORT.md with a 5-line summary and a ranked fix plan. Use after building or changing a cast, at the end of a milestone, before showing characters to the user, or at an existing game's next stopping point."
---

# Character design: audit

## Why a separate reviewer
The thread that designed a cast can't see it fresh, and it knows every character's name, so it will "recognise" silhouettes that a player never could. The audit is run by **fresh reviewer subagents** that:
- didn't design or build the characters
- **never edit** the game, the docs, or the models
- only gather judgements and write the report

## When to run it
- After step 12 of the `character-design` process, before the screenshot sheet goes to the user.
- At the end of every milestone that added or changed characters.
- **Existing games (D5):** at each game's next stopping point (the end of its current milestone, or before its next publish). Not retroactively all at once. If the game has no `CHARACTERS.md`, the build thread writes one from what is in the game first, then the audit runs.

## Step 1: gather evidence (the build thread does this)
Save everything to `design/<game>/audit/<YYYY-MM-DD>/characters/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default):
- **The blind lineup folder** (see step 2). Other games' casts live in other Studio places, so they are not staged together. Instead, every game keeps one flat-black PNG per character from its own V1 run in `screenshots/characters/<date>/silhouettes/`. Build the blind set from those files:
  - Pick the **two most recent other games**: the order in `studio-profile.md` if it lists one, otherwise the two other games whose `CHARACTERS.md` was modified most recently.
  - Copy this game's per-character silhouettes and theirs into a **new folder outside the audit folder** that holds only those images, for example `design/<game>/audit/<date>-blind/`. Rename every file to a shuffled number (`fig-01.png`, `fig-02.png`, ...). No names, labels, or telling file names.
  - Write the key (which figure is which game and character) to `silhouettes-key.md` **in the main audit folder**, never in the blind folder.
  - If another game has no saved silhouettes, run the lineup against fewer games and say so in the report. Don't block on it.
- `silhouettes-cast.png`: this game's cast only (V4).
- `colour-lineup.png`, `grayscale-*.png` (V3 in each area the character appears), and `phone-*.png` (V2 at phone size at the farthest reaction distance).
- Short clips or frame sequences of each named character's idle, locomotion and signature action, if possible.
- `palette.txt`: output of
  `python3 -I .claude/skills/character-design/palette_collisions.py design --target <game>`
  (both the near-match pairs and the colour-family table).
- `tris.txt`: triangle and texture sizes per character (R2, R3).
- `CHARACTERS.md`, `STORY.md`, `ART-DIRECTION.md` for this game, plus `studio-profile.md` if it exists, and every other game's `CHARACTERS.md` and `ART-DIRECTION.md` (find them as described in `character-design` "How the studio's other games are found").
- A list of any Creator Store or generated assets used, with the source and what was changed.

The build thread does not write opinions into the evidence folder.

## Step 2: the blind lineup (a separate reviewer, run first)
Start a fresh subagent with the Agent tool. Give it **only** the path to the blind folder (nothing else in that folder, and no other paths) and these instructions:
- "Group these figures by which ones look like they belong to the same game or the same character type. For each figure, say what role you think it plays (for example: shopkeeper, chaser, guard, hero). Note any two figures you could confuse."

Do not give it names, docs, the key, the audit folder path, or this file. Tell it to read only the images in the blind folder. Once a reviewer has read `CHARACTERS.md`, it can't do this test honestly. Save its answer as `blind-lineup.md`.

The build thread then maps its answer against the key:
- A figure from this game grouped with a figure from another game is a **lineup note**.
- Two figures from this game that it confused are a **V4 finding**.
- A role it could not guess is a **V1 finding**.

## Step 3: the scoring review (a second reviewer)
Start another fresh subagent. Give it:
- this file
- `../character-design/SKILL.md`, `../character-design-visual/SKILL.md`, `../character-design-story/SKILL.md`, `../character-design-roblox/SKILL.md`
- `../de-ai/BANNED.md` (plus any bans in `studio-profile.md` if it exists) and `../de-ai-story/SKILL.md`
- the evidence folder, including `blind-lineup.md` and `silhouettes-key.md`

**Do not** give it your opinion of the cast.

### 3a. Score each character against the rules
For every character, mark each rule that applies as **pass**, **weak**, or **miss**, and cite the evidence (a screenshot, a line in a doc, a measured number):
- **Required fields:** role, silhouette hook, shape language, palette colours, one-line personality all present in `CHARACTERS.md`.
- **Visual:** V1 to V10.
- **Narrative:** N1 to N6 (majors get all that apply; minors need want plus a visible detail; monsters need cue, rule and counter).
- **Roblox:** R1 to R7, and G1 to G6 for anything generated.
- **Avatar decision:** recorded with a reason; matches the decision rules in `character-design-roblox`; extreme-avatar test done if avatars are kept; bot appearance decided if the game uses bot fill.

Then give the cast an overall score per area, 0 to 2, in the same spirit as `de-ai-audit` (0 clearly generic, 1 passable but you can tell, 2 made on purpose by a person): silhouette and shape, colour and value, phone readability, story and voice, Roblox build and budget, animation and identity.

### 3b. Distinctness check against the studio's other games
Overlap is normal. **Everything here is a note unless it meets F1, F2 or F3.**

**Notes (flag, never block).** Thresholds are starting policy, to tune with data:
1. **Palette overlap** (from `palette.txt`): any accent or danger colour within deltaE 15 of another game's accent or danger colour; any other chromatic colour within deltaE 6.
2. **House-style drift** (from the colour-family table and the role formulas): four or more of the five palette roles (dark, light, accent, danger, light source) in the same families as another game; or the game uses the overused formula from D3 (near-black, cream, brass, oxblood, red danger). Note whether `CHARACTERS.md` gives a reason.
3. **Danger signal:** danger is again a saturated red around hue 20 to 45. Suggest an alternative threat language (another hue, a value inversion, a light behaviour, a sound-first cue, a pattern).
4. **Signature character material** matches another game's.
5. **Silhouette lineup** (from step 2): a figure grouped with another game's figure.
6. **Proportion scheme:** head:body ratio and height range both match another game.
7. **Rig and rendering:** the rig mix, rendering treatment and motion style all match another game.
8. **Monster cues:** a monster reuses both a cue sense and a counter from another of the studio's games.
9. **Names:** a repeated character name, or the same naming source (era, language, pattern) as the previous game.
10. **Generated assets:** a prompt with no world-specific words (G2).

**Fails (block that character until fixed):**
- **F1** the same base model as a character in another game, left unedited
- **F2** the same model plus the same palette plus the same proportions (a lineup note that also shares palette and proportions escalates here)
- **F3** an unedited free Creator Store character

Nothing else fails. Do not invent new fail conditions.

### 3c. The fix plan
List every finding, **worst first** (fails, then rule misses that hurt the 1 second read, then everything else). For each:
- what's wrong
- where (screenshot or file and line)
- a concrete fix that names the change, for example: "The guard and the porter are both default-height rectangles in flat black. Drop the porter's head to 1/4 of his height and give him the trolley as a permanent part of his outline."

Also list any new generic character tell that should go on `../de-ai/BANNED.md`, for the build thread to propose to the user.

## Step 4: fix and re-audit (the build thread does this)
1. Fix fails first, then misses, worst first. Notes are fixed only if the user or the build thread decides to; a note with a written reason in `CHARACTERS.md` is acceptable.
2. Gather fresh evidence and run **new** reviewers (a new blind lineup reviewer and a new scorer), never the same ones.
3. Repeat until there are no fails and no misses on V1, V2, V3, V5 and R5, or the user explicitly OKs an exception.
4. Save before/after images side by side in the audit folder.

## Output
**`design/<game>/audit/<YYYY-MM-DD>/CHARACTER-REPORT.md`**, written by the scoring reviewer. It **starts with a 5-line plain summary**, in this order, no jargon:
1. Overall verdict: how many characters, how many pass, and whether anything fails.
2. The strongest character and why, in plain words.
3. The weakest character and the single most important fix.
4. Distinctness: fails (if any) and the most important note about overlap with the studio's other games.
5. The avatar-vs-custom decision and whether it holds up.

Then: the per-character rule table, the area scores, the blind lineup result, the distinctness notes and fails table, the fix plan, what was fixed (after step 4), the before/after images, and any proposed banned-list additions.

**Then, as an explicit step, the build thread gives the user a chat overview** with the screenshot sheet attached. Keep it short and plain:
- the 5-line summary, lightly edited for chat
- any fail, what it means, and what is being done about it
- the top three fixes, and whether they are done
- what you need from the user (approve, pick between options, or OK an exception)

The report is the detail; the chat overview is what the user reads. Do not make the user open the file to learn the result.
