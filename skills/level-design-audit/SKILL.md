---
name: level-design-audit
description: Audit a Roblox game's level blockout or finished space. The build thread gathers evidence (top-down and five-second screenshots, a timed playthrough of the critical path, bot path results, performance numbers); a blind reviewer runs the five-second test on unlabeled screenshots; a fresh scoring reviewer that never edits scores eight areas against the level-design rules and writes LEVEL-REPORT.md with a 5-line summary and a ranked fix plan. Use before showing a blockout to the user, at the end of any milestone that built or changed a space, and before publishing.
---

# Level design: audit

## Why a separate reviewer
The thread that built a space knows where the exit is, so it will always "see" it. It walked the path twenty times, so the pacing feels fine to it. The audit is run by **fresh reviewer subagents** that:
- didn't plan or build the space
- **never edit** the game, the plan or the blockout
- judge only from the evidence: screenshots, the playthrough log and the numbers

## When to run it
- Before the blockout goes to the user (step 5 of the `level-design` process), as a light pass: areas 1-6 only.
- At the end of every milestone that built or changed a space, as a full pass.
- Before publishing, on every space a new player sees in the first ten minutes.

## Step 1: gather evidence (the build thread does this)
Save everything to `design/<game>/audit/<YYYY-MM-DD>/levels/<space>/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). Capture in a real `solo_playtest` where the step says so, not only in edit mode.
- `LEVEL-PLAN.md` (copy of the current plan, including the iteration log).
- `topdown.png`: the straight-down view (LR4), with roofs hidden. A second copy, `topdown-annotated.png`, with the critical path, beats and landmarks marked.
- `five-second/` folder: one eye-height shot from each area's entrance (LR5), **file names numbered only** (`01.png`, `02.png`), with no area names. Keep the key in `five-second-key.md`, which the blind reviewer never sees. Add the same shots at the low graphics quality or low-end device profile if the art pass is done.
- `phone/`: `capture_device_matrix` shots of the two most important views.
- `playthrough.md`: the timed walk of the critical path (LR6). One row per segment: from beat, to beat, measured seconds, planned seconds, what happened. Also every required jump tested, with pass or fail.
- `bots.md` (games with bots or patrols): every node pair tested with PathfindingService and the result; where bots got stuck in a watched round, with screenshots.
- `perf.md`: draw calls, memory and frame time in the densest area from `get_scene_analysis`, `get_memory_breakdown` and `capture_micro_profiler`, against the budgets in `testing-devices-perf`. Mark mobile as "real-device check still needed" unless a person has played on a phone.
- `logs.md`: errors from `get_runtime_logs` during the walk.
- For a finished space: `ART-DIRECTION.md`, and `refs/levels/`.

The build thread writes no opinions into the evidence folder.

## Step 2: the blind five-second test (a separate reviewer, run first)
Start a fresh subagent with the Agent tool. Give it **only** the `five-second/` folder and the top-down image without annotations. Do not give it the plan, the key, area names or this file. Instructions:
- "For each numbered screenshot, imagine you just walked in. In one line each: where would you go next, what do you think is important here, and what is the tallest or most noticeable thing you can see? Then look at the top-down image and say which screenshot you think was taken where, and draw the route you would expect to take from start to finish in words."

Save its answer as `blind-five-second.md`. The build thread maps it against the key:
- A wrong "where would you go next" is a **navigation finding** on that area (LC9 to LC11).
- No landmark named, or the wrong one, is a **landmark finding** (LC7, LC8).
- An expected route that differs from the critical path is a **readability finding** on the top-down layout.

Once a reviewer has read the plan it can't do this honestly, so this reviewer is never reused.

## Step 3: the scoring review (a second reviewer)
Start another fresh subagent. Give it:
- this file
- `../level-design/SKILL.md`, `../level-design-craft/SKILL.md`, `../level-design-roblox/SKILL.md`
- the evidence folder, including `blind-five-second.md` and `five-second-key.md`
- `studio-profile.md` at the project root, if it exists

**Do not** give it your opinion of the space.

### 3a. Rule check
For each rule that applies (LG1 to LG4, LC1 to LC22 for the archetypes in use, LR1 to LR16), mark **pass**, **weak**, **miss** or **not applicable**, and cite the evidence: a screenshot, a row in `playthrough.md`, a line in the plan, a measured number. A rule with no evidence is **not verified**, never pass.

### 3b. Area scores
Score each area **0** (broken or generic), **1** (works, but a player will notice the problem) or **2** (made on purpose and proven by the evidence). Cite evidence for every score.
1. **Plan:** the plan has a top-down sketch, a beat list in seconds, a teaching plan, landmarks and a "what happened here" per area; it matches what was built.
2. **Navigation:** the blind reviewer found the exit and the landmark in most shots; no empty unlit dead ends; wrong ways discouraged without invisible walls.
3. **Pacing:** measured beat gaps within 15-40 s of travel (or the arena's first contact within about 8 s); rising peaks, real valleys after each.
4. **Teaching:** each mechanic introduced safely, developed, twisted and retired; the first failure is survivable; the accent color is never on decor.
5. **Archetype rules:** the checklist for the archetype in use (LC16 to LC22) is met, or the plan gives a reason.
6. **Metrics and build:** jumps tested at the documented metric; corridors and ceilings fit the camera; streaming boundaries at occluders; interactables Atomic; critical edges not on terrain; bot paths succeed where bots are used.
7. **Story and set pieces:** props imply the area's sentence; set pieces are telegraphed, controllable, checkpointed and followed by a valley (finished spaces only; score blockouts on the plan).
8. **Performance and devices:** numbers within budget in the densest area; guidance still reads at low quality and at phone size.

For a light pass before showing the user, score 1-6 and mark 7-8 NOT RUN with the reason "blockout pass".

### 3c. The fix plan
List every finding **worst first**: anything that gets a player lost or stuck, then anything unfair or untestable, then pacing, then the rest. For each:
- what's wrong
- where (a screenshot, a playthrough row, a plan line)
- a concrete fix that names the change, for example: "Area 3's exit is a dark doorway on the left wall that the blind reviewer missed. Move the exit to the far wall in line with the entrance, and put the warm accent light over it."

## Step 4: fix and re-audit (the build thread does this)
1. Fix worst first. Change the blockout, then re-walk and re-shoot.
2. Gather fresh evidence and run **new** reviewers (a new blind tester and a new scorer). Never reuse one.
3. Repeat until no area scores 0, navigation and pacing score 2, and the blind reviewer finds the exit in every shot, or the user explicitly OKs an exception.
4. Save before and after images side by side in the audit folder.

## Output
**`design/<game>/audit/<YYYY-MM-DD>/LEVEL-REPORT.md`**, written by the scoring reviewer. It **starts with a 5-line plain summary**, in this order, without jargon:
1. Verdict: which spaces were audited, light or full pass, and whether anything scores 0.
2. Navigation: could a fresh eye find the way and the landmark, in plain words.
3. Pacing: the longest stretch with nothing happening, and where the best peak is.
4. The single most important fix.
5. What was not verified (for example a real phone, a full bot round) and why.

Then: the area scores with evidence, the rule table, the blind test mapped to the key, the playthrough timing table, the fix plan, what was fixed (after step 4), and the before and after images.

**Then, as an explicit step, the build thread gives the user a chat overview** with the before and after sheet attached:
- the 5-line summary, lightly edited for chat
- the top three fixes and whether they are done
- anything that blocks the art pass or publishing
- what you need from the user (approve the blockout, choose between two layouts, or OK an exception)

The report is the detail; the chat overview is what the user reads. Do not make the user open the file to learn the result.
