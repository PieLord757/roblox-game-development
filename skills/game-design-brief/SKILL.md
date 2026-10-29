---
name: game-design-brief
description: Writes GAME-DESIGN.md for a new game (category, must-haves, core loop, first-10-seconds hook, return engine, target numbers) and gives the idea a verdict of strong, needs work or weak. A weak verdict stops the build until the user decides. Use before building any new game or any newly approved pitch.
---

# Game design brief (new games)

Load `game-design` first if you have not this session. This skill turns an idea into a design that can be checked, and decides whether it is ready to build.

## Inputs
1. The idea: a pitch, a user message, or a one-line concept.
2. `studio-profile.md` at the project root if it exists: audience, hard rules, existing games, default paths. If it does not exist, ask for the hard rules and existing games before giving a verdict (see `game-design`).
3. `../game-design/CATEGORIES.md`, and the deep file for the chosen category, `../game-design/categories/<slug>.md`.

## Step 1: classify
Follow "How to classify a game" in `CATEGORIES.md`. Write down:
- **Main category** (slug) and **at most one secondary**, with one sentence each on why.
- The main category's **fit label and flags**.
- Check every flag against the profile's hard rules. A banned flag or a category labeled No is an automatic weak verdict (Step 5).

Craft note: classify by what the player *does every 30 seconds*, not by the theme. "A haunted hotel game" is not a category. "Walk the corridor and turn back when something is wrong" is (`anomaly-rules-check`). If the idea's first 3 minutes and its long-term loop belong to different categories, the first 3 minutes decide the main one.

## Step 2: copy the must-haves and decide the twist
- Copy the main category's 3-6 must-haves into the brief.
- For each, write **how this game meets it**, concretely ("a duel within 10 s: the lobby is a range that queues you as you walk in").
- Mark which **one or two** must-haves this game changes on purpose. That change is the twist. Changing more than two usually means the game has left the category and lost the reasons it works.
- If a must-have is missing and not deliberately replaced, it goes into the verdict reasons.

## Step 3: design the loop at three timescales
| Scale | Write | Good looks like |
|---|---|---|
| Moment (5-30 s) | the verb, the feedback, the micro-decision | "Peek, fire, hear the hit tick, decide to push or reset" |
| Session (5-30 min) | what a round, run, floor, day or chapter is, and how it ends | "First to 5 rounds; a match ends with a streak bonus and a challenge tick" |
| Meta (days) | what persists and why tomorrow is different | "Ranked tier, a weekly map rotation, a weapon tracker" |

Check each layer pays off on its own timescale, and that every reward changes how the **next** loop plays. Check for a dead moment after each big reward: the next goal must already be on screen.

## Step 4: hook, return engine and numbers
**The first-10-seconds hook.** Write it as one sentence a viewer would repeat ("shoot yourself or the dealer"; "notice what changed in the corridor"). Then write what happens by 60 s and by 3 min. Techniques that work:
- Start mid-action: no menu between joining and the verb.
- Make the first use of the verb succeed and look great.
- Put the long-term goal on screen by minute 3 (a counter, a locked door, a rank).
- Teach by level layout, not text. One concept at a time.

**The return engine.** Pick at least one from this list and say how it works in this game. "We will add updates" does not count.
- ranked ladder or seasons
- wipe or season reset
- daily seed or daily set with a leaderboard
- player-made content
- death or failure advances the story
- difficulty ladder (ascension, heat, hard modes)
- a collection of discoverable combinations or secrets
- persistent stash, base or world that the player is building
- chapter releases on a visible schedule (only paired with a repeatable layer)
- an async rivalry (ghosts, records, revenge)

**Target numbers.** Copy the category's targets from `CATEGORIES.md` (session length, D1, D7, time to first fun) and adjust with a reason if this game differs. These are aims for the audit to measure against, not promises.

## Step 5: verdict
Run the fun test from `game-design` (toy, hook, decision and stakes, runway, return, solo floor, story), plus any studio fun filter or extra rules in the profile. Then decide:

**Weak (stop)** if any one of these is true:
- the main category is labeled No, or a flag breaks a hard rule in the profile
- the core verb is not fun as a toy, or nobody can say why it would be
- there is no return engine from the list
- the idea shares a main mechanic, twist or setting with an existing game or pitch in the profile
- two or more must-haves are missing with no deliberate replacement
- the fun test has two or more blank answers

**Needs work** if:
- one must-have is missing or vague
- the hook takes longer than 60 s to show the verb
- the runway is thin (under about 5 hours of learnable patterns) with no plan for the tail
- a flag needs a mitigation that is not designed yet (bot fill, solo variant, a repeatable layer under authored content)
- the build estimate is far over what the profile allows

**Strong** if none of the above, every fun-test answer is concrete, and the twist changes at most two must-haves.

Give **3-5 reasons** for the verdict, each tied to a must-have, a fun-test answer or a profile rule.

### If the verdict is weak
**The build stops.** Do not start building.
1. Propose **2-3 concrete fixes**, each a specific change ("move deduction out of a notebook screen and into the world, with tools the player holds, as Phasmophobia does"; "add a daily seeded run with a board as the return engine"; "change the setting, because an existing game in the profile already uses it").
2. For each fix, say what verdict it would likely get and what it costs in hours.
3. Present the verdict and fixes to the user in chat and **wait for their decision**: apply a fix, change the idea, or go ahead anyway. Record the decision in `GAME-DESIGN.md`.

### If the verdict is needs work
Fix what you can inside the brief, re-run the verdict, and show the user what changed. If something needs the user's call (scope, a rule exception), ask before building.

## Output: `GAME-DESIGN.md`
Write it to the game's folder (the profile's default path, or `design/<game>/GAME-DESIGN.md`). Structure:

```
# <Game>: game design

## Summary (for the user)
<5 plain-English lines: what you do, why it is fun, why people come back, the verdict, the one biggest risk>

## Verdict: STRONG | NEEDS WORK | WEAK
- <reason 1>
- ...
<If weak: fixes proposed, and the user's decision with date>

## Category
- Main: <name> (`slug`), fit label, flags, why
- Secondary: <name> (`slug`) or none, why

## Must-haves
| Must-have | How this game meets it | Changed on purpose? |

## Core loop
- Moment / Session / Meta

## First 10 seconds, 60 seconds, 3 minutes

## How players keep coming back
- Return engine(s) and how they work here
- Depth multiplier: which two systems multiply each other

## Fun test
Toy / Hook / Decision / Runway / Return / Solo floor / Story

## Target numbers
| Metric | Target | Why |
(session length, D1, D7, time to first fun)

## Solo-first plan
## Risks and what would prove them wrong
## Build estimate (hours, from the profile's unit)
```

## Present it in chat
After writing the file, give the user a clear overview **in chat**: the 5-line summary, the verdict with its reasons, the category, the hook in one sentence, the return engine, and (if weak) the proposed fixes with the question of what they want to do. The file is the detail for the build thread; the chat overview is what the user reads.

## Common mistakes
- Picking the category from the theme instead of the verb.
- A hook that is a cutscene, a menu or a tutorial.
- "Players will come back for new content" as the return engine.
- Rewards that only raise a number.
- Copying the market leader's format with a new skin. Clones get 2-7% of the original.
- Writing a strong verdict because the story is good. Story is an arc, consumed once; the loop is what people return to.
- Estimating in weeks, or ignoring the profile's units.
