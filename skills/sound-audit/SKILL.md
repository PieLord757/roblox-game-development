---
name: sound-audit
description: Audit a Roblox game's audio. The build thread gathers evidence (event coverage against SOUND-PLAN.md, live bus wiring and levels, variant logs from repeated triggers, runtime load errors, the credits file and license proof, visual pairs for critical cues); a fresh reviewer subagent that never edits scores eight areas, treats any unlicensed or unknown-source asset as a blocking fail, marks the listening checks it cannot hear as user checks, and writes SOUND-REPORT.md with a 5-line summary and a ranked fix plan. Use at the end of every milestone that added or changed audio, and always before publishing.
---

# Sound: audit

## Why a separate reviewer, and what it can't do
The thread that built the audio has heard every sound a hundred times and knows what each one means, so it can't judge whether a player will. The audit is run by a **fresh reviewer subagent** that:
- didn't source or build the audio
- **never edits** the game, the plan or the credits
- judges only from the evidence

**An agent cannot listen.** It can't tell whether a sound is good, whether the mix is muddy on a phone, or whether the music fits. So the audit is built from what can be checked in data, and the listening checks are handed to the user. A listening check is never marked PASS by an agent. It is **USER CHECK** (with the result the user gave) or **NOT RUN** with the reason.

## When to run it
- At the end of every milestone that added or changed audio.
- Before every publish. Area 7 (legality) failing blocks the publish.

## Step 1: gather evidence (the build thread does this)
Save everything to `design/<game>/audit/<YYYY-MM-DD>/sound/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). Capture in a real `solo_playtest`, not edit mode.
- `SOUND-PLAN.md` and `CREDITS.md` (copies), and the `licenses/` folder listing.
- **`coverage.md`:** every row of the plan's event list, triggered in the playtest (fire the same remote or input the player does, from `eval_client_runtime`), with what actually played: the asset, the bus, and whether an AudioPlayer was playing at the moment (read live, not assumed). Also every player action found in the game that is missing from the plan. "Nothing played" is a finding.
- **`buses.md`:** the live bus graph read with `eval_client_runtime`: each AudioFader and its volume, each Wire's source and target, the ducking compressor and its sidechain source, the master, the output. Whether the settings sliders change the fader volumes (move each and read it back). Whether the automatic listener is off when custom listeners exist.
- **`variation.md`:** for each frequent sound (footsteps per surface, the core action, hits, pickups), trigger it 20 times in a row inside one `eval_client_runtime` call and log the variant index, PlaybackSpeed and Volume each time. Count the variants, any immediate repeats, and the pitch spread.
- **`threats.md`:** for each threat, the time between its tell starting and its action (measured inside one call), and the tell asset. Whether any two threats share a tell.
- **`visual-pairs.md`:** each critical cue (threat tells, detection, damage, objective change) and the visual that accompanies it, with a `capture_screenshot` of the visual. Note: BillboardGuis and Highlights don't show in captures; confirm those by reading their properties.
- **`logs.md`:** `get_runtime_logs` errors and warnings about audio, unfiltered, and any asset that failed to load. `get_scene_analysis` audio memory.
- **`ui-family.md`:** the list of UI sounds with their names and descriptions from the asset metadata, and the setting from `ART-DIRECTION.md`.
- **`assets-in-game.md`:** every audio asset ID found in the place (search all AudioPlayers, Sounds and scripts with `search_objects` and `grep_scripts`), so the reviewer can diff it against `CREDITS.md`.

The build thread writes no opinions into the evidence folder.

## Step 2: the review (the reviewer subagent does this)
Start the reviewer with the Agent tool. Give it:
- this file
- `../sound/SKILL.md`, `../sound-craft/SKILL.md`, `../sound-roblox/SKILL.md`, `../de-ai-feel/SKILL.md`
- `../de-ai/BANNED.md` if it exists, plus any bans in `studio-profile.md`
- the evidence folder
- `studio-profile.md` at the project root, if it exists (it may set a stricter sourcing rule)

**Do not** give it your opinion of the audio.

### 2a. Scores
Score each area **0** (broken, missing or generic), **1** (works, but a player will notice) or **2** (made on purpose and proven by the evidence), citing evidence for every score. Rules without evidence are **not verified**, never pass.
1. **Coverage (SG3, SC8):** every planned event plays its sound; no silent player action; no game action missing from the plan.
2. **Variation (SC5, SC6, SR4):** frequent sounds have 3-5 variants (any repeated sound at least 2-3), no immediate repeats in 20 triggers, pitch spread within about 0.94-1.06; footsteps change by surface.
3. **Information (SC7, SC9, SC19):** every threat has a unique tell; measured lead time is enough to react (0.5-2 s for the reaction needed); barks for every guard state where the game has guards; in PvP, enemy versus friendly treatment is in place.
4. **Mix structure (SC11, SC12, SR1 to SR3):** five buses wired as planned, ducking keyed correctly, voice caps in place, sliders work, 3D sounds routed through emitters to their bus and heard once. (This scores the structure, not how it sounds.)
5. **Visual pairs (SG4, SC10):** every critical cue has a visual counterpart.
6. **Setting fit (SC17, SC20):** judged from names, descriptions and the plan: is the UI family derived from the setting; are the music references and sources specific to this world; does anything match `BANNED.md` or read as stock (famous overused free tracks, generic sci-fi bleeps in a non-sci-fi game). Mark it "from metadata only; user check needed".
7. **Legality (SG1, SG2, SR9 to SR12):** every asset in `assets-in-game.md` appears in `CREDITS.md` with a source and license; no NC, unknown-rights, ripped or share-alike source; every CC BY asset is in the in-game credits and the description; license proof saved for third-party sources; third-party uploads private and not on the Creator Store. **Any failure here scores 0 and blocks publishing.**
8. **Health (SR14):** no failed asset loads in the logs; no sound silent live; audio memory reasonable.

### 2b. The listening checks (handed to the user)
List these in the report with **USER CHECK** and a one-line instruction each. The build thread asks the user in chat and writes the answers in:
- **Phone speaker:** play 5 minutes on a phone with no headphones. Can you hear every threat tell and the core action clearly?
- **Fatigue:** play 10 minutes. Does any sound, loop seam or stinger get annoying?
- **Music fit:** does the music feel like this game's world, and does its arrival mean something?
- **Repeat:** does any frequent sound still sound like a machine gun?
- **Ducking:** do voices and barks come through over the music?

If the user hasn't answered yet, they stay **NOT RUN: waiting for the user**. Never fill them in for the user.

### 2c. The fix plan
List every finding **worst first**: legality fails, then silent actions and missing tells, then broken routing or load errors, then variation, then setting fit. For each:
- what's wrong
- where (an evidence file row, an asset ID, a script)
- a concrete fix that names the change, for example: "The metal footstep bank has one variant and repeated 19 times in 20. Add four Creator Store metal footsteps from the same library and route them through the shuffle bag with ±5% pitch."

Also list any generic audio tell that should go on `BANNED.md`, for the build thread to propose to the user.

## Step 3: fix and re-audit (the build thread does this)
1. Fix legality first (remove or replace the asset, update the credits), then worst first.
2. Gather fresh evidence and run a **new** reviewer, never the same one.
3. Repeat until area 7 scores 2, no area scores 0, and coverage and information score 2, or the user explicitly OKs an exception. Legality has no exceptions.

## Output
**`design/<game>/audit/<YYYY-MM-DD>/SOUND-REPORT.md`**, written by the reviewer, next to any `LEVEL-REPORT.md` from the same date. It **starts with a 5-line plain summary**, in this order, without jargon:
1. Verdict: whether anything blocks publishing (legality, silent actions, load failures).
2. Coverage: how many events have sound, and how many are silent or missing.
3. The strongest part of the audio and the weakest, in plain words.
4. The single most important fix.
5. Which listening checks are waiting for the user.

Then: the area scores with evidence, the rule table, the variation and threat tables, the credits diff, the listening-check list with the user's answers, the fix plan, and what was fixed (after step 3).

**Then, as an explicit step, the build thread gives the user a chat overview:**
- the 5-line summary, lightly edited for chat
- anything that blocks publishing, and what is being done about it
- the top three fixes, and whether they are done
- **the listening checks, as a short list the user can do now**, each with its one-line instruction
- what you need from the user (the listening results, or an OK on an exception)

The report is the detail; the chat overview is what the user reads. Do not make the user open the file to learn the result.
