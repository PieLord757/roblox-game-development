---
name: roblox-game-creation
description: "The single starting point for making a Roblox game, from idea to live game. Walks the whole pipeline in order (idea, design brief, characters, levels, UI and art, sound, feel, economy, testing, publishing, launch marketing, live ops) and says exactly which skill to load at each stage, which gates need the user's approval, and what each stage must produce. Use whenever starting a new game, resuming one, or asking what to do next on a game."
---

# Roblox game creation (start here)

This skill is the map. Each stage below names the skill that holds the real craft for that stage. Load that skill when you reach the stage. Don't try to do a stage from memory.

**Before anything else:**
- Load `developer-habits`. Its window, saving, data-safety and approval habits apply at every stage.
- Read `studio-profile.md` at the project root if it exists. It holds this studio's audience, hard rules, existing games, and where to publish. Wherever a skill and the profile disagree, the stricter rule wins.

## The two rules that run through every stage
1. **Teach yourself the craft, then do great work.** Every skill below explains how to do its area well, not just what document to write. A plan that's filled in but executed poorly still fails the audits.
2. **Show the user an overview in chat.** Every document a stage produces (brief, cast sheet, level plan, test report, audit) is also summarized for the user in chat, starting with a 5-line plain summary. The file holds the detail.

## The pipeline

| # | Stage | Load | Produces | Gate |
|---|---|---|---|---|
| 1 | **Idea** | `game-design-pitch` (if no idea yet) | 3 to 5 pitches (fewer if `studio-profile.md` sets a lower limit), each checked against existing games for repeats | The user picks |
| 2 | **Design brief** | `game-design`, then `game-design-brief` | `GAME-DESIGN.md`: category, must-haves, core loop, 10-second hook, return engine, target numbers, verdict | A **weak** verdict stops the build until the user decides |
| 3 | **Story** (if the game has one) | `de-ai-story`, `character-design-story` | `STORY.md`: cast, wants and secrets, the twist with every clue and payoff | Fair twist; no banned phrasing |
| 4 | **Characters** | `character-design` (routes to visual, roblox, audit) | `CHARACTERS.md`, avatar vs custom decision with its reason, a screenshot sheet | **The user approves the cast sheet** |
| 5 | **Levels** | `level-design` (routes to craft, roblox, audit) | `LEVEL-PLAN.md`, grey blockout in Studio, screenshots | **The user approves the blockout before any art goes on it** |
| 6 | **UI and art direction** | `de-ai`, `de-ai-ui` | `refs/`, `ART-DIRECTION.md` (palette checked against the studio's other games), HUD and menus | **The user approves the first UI and art screenshot sheet** |
| 7 | **Feel** | `de-ai-feel` | Tuned core action: instant response, sound, effects, freeze frames, one config module | The core action is fun with no UI and nobody online |
| 8 | **Sound** | `sound` (routes to craft, roblox, audit) | `SOUND-PLAN.md`, `CREDITS.md`, buses and mix | Every audio asset is legal and credited |
| 9 | **Economy** | `economy` (routes to design, monetization) | `ECONOMY.md`: currencies, sources and sinks, the price list, a fairness check | **The user approves the price list before any product is created** |
| 10 | **Milestone audits** | `de-ai-audit`, `game-design-audit`, `character-design-audit`, `level-design-audit`, `sound-audit` | Reports in `audit/<date>/`, each fixed and re-checked by a fresh reviewer | Every area passes, or the user signs off on the exception |
| 11 | **Testing** | `testing` (routes to run, exploits, devices-perf, first-time-player) | `TEST-REPORT.md` | **Any critical failure blocks publishing.** DataStore safety comes first |
| 12 | **Publish** | `publish` (routes to store-page, compliance, launch) | `STORE-PAGE.md`, maturity answers, publish private, test, then public | **Nothing is published or made public without the user's explicit OK** |
| 13 | **Launch marketing** | `marketing` (routes to creative, launch) | Launch kit: trailer shot list, 5 clips with scripts, announcement drafts, ad plan | **Nothing is posted, sent or paid for without the user's OK** |
| 14 | **Live ops** | `live-ops` (routes to analytics, updates) | Tracking set up before launch, a weekly `WEEKLY-REPORT.md`, `ROADMAP.md`, updates and chapters | **Every live change needs the user's OK** |

Stages 3 to 9 overlap in practice: you'll tune feel while blocking out levels, for example. The order shows what each stage depends on, not a strict sequence. The gates are strict: never build past an unapproved gate.

## Milestones
A typical first milestone is a vertical slice: the core loop playable solo from start to the first big moment, in one space, with real UI, sound and feel.

**At the end of every milestone:**
1. Run the audits in stage 10.
2. Run a `testing` milestone run.
3. Fix what they find, worst first.
4. Re-check with fresh reviewers.
5. Update `progress.md`.
6. Give the user a chat overview with screenshots and what's still open.

## Resuming a game
1. Read the game's `progress.md` and `HANDOFF.md`.
2. Find the earliest stage whose gate isn't passed. That's where you are.
3. Load that stage's skill and continue.
4. If a newer version of a skill exists than the one the game was built with, run that skill's audit at the next stopping point.

## Where files go
Each game has one game folder. Use the game folder path from `studio-profile.md` if it sets one; otherwise use `design/<game>/`. Every path written as `design/<game>/...` in these skills means that game folder, and `design/` means the folder that holds all the game folders. Inside the game folder:
- design docs at the top level
- `refs/`, `screenshots/`, `audit/<date>/`, `tests/<date>/`, `liveops/` and `marketing/` as subfolders

The place file lives wherever the studio keeps games, as stated in the profile.

## What this skill set is not
- It is not a substitute for playing the game. Every stage ends with real playtests and screenshots, never "it should work".
- It doesn't make choices that belong to the user: what to build, what to charge, what to publish, what to post or spend. It prepares those choices and asks.
