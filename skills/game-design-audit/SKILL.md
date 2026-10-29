---
name: game-design-audit
description: Design audit of an existing, playable game. Asks whether it is fun, deep and worth returning to. A fresh reviewer that never built or edits the game scores each must-have of the game's category 0-2 from real playtest evidence, then names the top 5 changes for fun and retention; the build thread fixes and a new reviewer re-checks. Use at each stopping point of a game in progress, or when a game feels flat or players do not return.
---

# Game design audit (existing games)

Load `game-design` first if you have not this session.

This audit is about **design**: is the game fun, deep, and worth coming back to? It is separate from any audit of whether the game looks or feels AI-made (for example `de-ai-audit`). Run both at milestones; they do not overlap.

## Why a separate reviewer
The thread that built a game cannot see it fresh. It knows what every system is *meant* to do and reads that into the playtest. So the scoring is done by a **fresh reviewer subagent** that:
- did not build the game
- never edits it
- is not told the builder's opinion of the game
- scores only from evidence

## Inputs
- `studio-profile.md` at the project root if it exists (audience, hard rules, default paths).
- The game's `GAME-DESIGN.md` if it has one. If it does not, write one first with `game-design-brief` (classification only; do not stop the audit for a verdict).
- `../game-design/CATEGORIES.md` and `../game-design/categories/<main slug>.md` (and the secondary's file if there is one).

## Step 1: gather evidence (the build thread does this)
Save everything to `design/<game>/audit/<YYYY-MM-DD>/` unless the profile names another path. Capture it in a **real playtest**, not edit mode, starting from a fresh save as a new player would.

**The first session, timed:**
- A screen recording or a screenshot every 10 s for the first 3 minutes, from join.
- The time to: the first use of the core verb, the first success, the first real decision, the first reward, the first sight of a long-term goal.
- Every moment of confusion: what was on screen and what the player did not know.

**The loop:**
- One full session-sized unit (a round, run, floor, day, chapter), timed.
- Every decision the player made in the first 5 minutes, with what the options were.
- Every failure or death, with its cause and whether the cause was visible on screen.
- What changed after the first reward: did the next loop play differently?

**Depth and return:**
- What is still unlearned after the session (the visible skill ceiling, locked content, unknown combinations).
- Every visible reason to come back tomorrow, as it appears on screen.
- A short later-game sample: load or grant mid-game progress and play 10 minutes, to see whether the loop changes or only the numbers.

**Solo and devices:**
- Play with nobody else online: queue times, bot quality, whether anything is blocked.
- One full loop on a phone view.

**Live data (if published):** D1, D7, session length, bounce under 60 s and 61-180 s, and funnel drop-off steps, with the benchmark band.

**Notes from real players (if any):** friend tests, comments, reviews. Quote them; do not summarize them into agreement.

Write a short `EVIDENCE.md` index that lists every file and timing. Do not write opinions in it.

## Step 2: the review (a fresh reviewer subagent does this)
Start the reviewer with the Agent tool. Give it:
- this file
- `../game-design/SKILL.md`, `../game-design/CATEGORIES.md` and the category deep files
- the game's `GAME-DESIGN.md`
- the audit evidence folder

**Do not** give it your opinion of the game, your fix ideas, or earlier audit scores.

The reviewer:
1. **Checks the classification.** Is the main category right for what the player actually does every 30 seconds? If not, it says so and scores against the right one.
2. **Scores each must-have** of the main category **0, 1 or 2**, using the "Playtest checks for the audit" table in the category's deep file:
   - **0:** missing or broken in the playtest.
   - **1:** present but weak, slow or unclear.
   - **2:** clearly present and working.
   Every score cites specific evidence: a timestamp, a screenshot, a timing, a quote. "Feels fine" is not evidence. If the evidence for a must-have is missing, the score is 0 and the gap is listed.
3. **Answers the three questions** with evidence:
   - **Fun:** is the core verb satisfying on its own? Did the first 60 s land? (Use the fun test from `game-design`.)
   - **Deep:** what is the player still learning after the session? Do two systems multiply each other? Is there a dominant strategy?
   - **Worth returning to:** what named return engine exists, is it visible in the first session, and does it change how the next session plays?
4. **Compares against the targets** in `GAME-DESIGN.md` or `CATEGORIES.md` (time to first fun, session length, and D1/D7 if live data exists).
5. **Writes the top 5 changes** that would most improve fun or retention, ranked by expected impact on the weakest must-haves and on the first 3 minutes. For each:
   - what is wrong, with the evidence
   - the concrete change, naming the replacement ("cut the 40-second intro walk; spawn with the weapon in hand at the first room, the way DOORS starts at door 1")
   - which must-have or target it moves
   - a rough cost in hours
   - how the next audit will see whether it worked

Ranking craft for the reviewer:
- **First-session problems first.** Most players are lost early, so a fix inside the first 3 minutes usually beats a fix at hour 3.
- **Toy before content.** If the core verb scores weak, more levels will not help; fix the verb.
- **Return engines that change play** beat ones that only pay out.
- **One change per item.** "Improve combat" is not a change; "add 6 frames of hit-stop and a heavier hit sound to the heavy attack" is.

## Step 3: fix and re-check (the build thread does this)
1. Apply the top 5, in order. Note what changed and where.
2. Gather fresh evidence the same way.
3. Run a **new** reviewer subagent, not the same one, with the same inputs and without the old report.
4. Repeat until every must-have scores at least 1, the first-session must-haves score 2, and no top-5 item is a 0-scored must-have, or until the user accepts the remaining gaps.

## Output: `DESIGN-REPORT.md`
Write `design/<game>/audit/<YYYY-MM-DD>/DESIGN-REPORT.md` (or the profile's design-audit path). It is named differently from any other audit's report on purpose.

```
# <Game>: design audit <date>

## Summary (for the user)
<5 plain-English lines: is it fun, is it deep, will people come back, the single biggest problem, the single best change>

## Classification
Main / secondary, and whether the reviewer agreed

## Must-have scores
| Must-have | Score 0-2 | Evidence |
Total: x / (2 x number of must-haves)

## Fun / Deep / Worth returning to
## Against targets
## Top 5 changes
1. Problem, evidence, change, must-have moved, hours, how to verify
...
## What was fixed (after Step 3)
## Re-check scores (new reviewer)
```

## Present it in chat
After writing the report, give the user a clear overview **directly in chat**: the 5-line summary, the score total with the weakest must-haves, and the top 5 changes in one line each. After a re-check, show the before and after scores side by side. The file is the detail; the chat overview is what the user reads.

## Common mistakes
- The builder scoring its own game.
- Playtesting from a developer save, skipping the first session.
- Scoring from the design doc instead of the playtest.
- A top 5 full of content additions when the core verb is weak.
- Treating a de-AI fix (fonts, art) as a design fix, or the reverse.
- Re-using the same reviewer for the re-check.
