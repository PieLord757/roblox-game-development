# Horde survivor (`horde-survivor`)

Read the `horde-survivor` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** you only move, your attacks fire on their own, and every 20-40 s you pick 1 of 3 upgrades while the screen fills with enemies, until your build turns into fireworks.

---

## What great looks like
- **Minute 1 is weak on purpose, minute 15 is absurd.** Vampire Survivors starts you with one slow whip. By the end of a run the screen is a storm of your own projectiles. The gap between those two states is the whole fantasy, and the player built it.
- **The secret combination.** In Vampire Survivors a weapon plus the right passive evolves into something new, and the game never tells you the recipe. Finding one yourself, or hearing about one from a friend, is the moment people retell.
- **The reward reveal is a show.** The chest opening borrows slot-machine timing: a spin, rising sound, a burst of light. The developer came from the gambling industry and applied that sequencing on purpose. The same reward handed over silently is worth half as much.
- **Space changes the game, not the art.** Megabonk (116,969 `[SC]`) took the formula into 3D with jumping, verticality and drops. That made positioning matter in a new way, which is why it read as new when hundreds of 2D clones did not.
- **Waves and a shop as a different rhythm.** Brotato (38,761 `[SC]`, 18.8% ret) cut runs into 20-60 s waves with a shop between them. Same genre, different breathing pattern.

## The hook
- **First 10 s:** the player is moving and enemies are already walking in. The first kill happens without pressing any attack button. Pickups fly to the player with a satisfying pull.
- **First 60 s:** the first level-up and the first pick-1-of-3. The pick should already feel different (a second weapon, not +5% damage).
- **First 3 min:** a visible power jump (two weapons firing, area damage) and the first dangerous moment (a swarm closing a gap, an elite enemy). End the first run, if it ends, with unlock progress shown immediately.

## Loop tuning
- **Upgrade cadence:** a level-up every 20-40 s early, slowing toward 40-60 s late as XP requirements climb. If players stop reading the choices, upgrades are too frequent; if the middle of a run feels flat, they are too rare.
- **Run length:** 15-30 min, with a clear end (a boss at a fixed time, a final wave). A run with no end becomes a test of patience, not skill.
- **Enemy density curve:** a sawtooth, not a ramp. Build to a swarm, give 10-20 s of relief while the player collects, then the next swarm or an elite. Constant max pressure is noise.
- **Choice quality:** of the 3 offered, at least one should be a real "which do I want" question. Guarantee that one option fits the current build when possible, so the player can commit to a plan.
- **Damage numbers:** show them small early and let them scale up with the build. If the screen is unreadable at minute 20, cut particle count before cutting damage numbers; numbers are the player's proof of power.
- **Tune in big steps.** If a weapon is never picked, double its effect and see if it becomes a pick. Then pull back.

## Depth and mastery
- **The skill chain:** dodge contact → kite a swarm in a circle → herd enemies into your area damage → route to pickups under pressure → plan a build toward a known evolution → adapt when the offer does not give you the plan.
- **The depth multiplier:** weapons × passives (or items × items). Every passive should make at least two weapons better in different ways. If each weapon only cares about its own stat, there is no build, only a list.
- **Hidden recipes:** keep some combinations undocumented in-game until found, then record them in a collection screen. Discovery is a motivation, not a bug.
- **Characters as starting rules:** each unlockable character should change one rule (starts with a different weapon, gains XP differently, moves differently), which changes which builds work.

## Retention engine
Pick at least two:
- **A long unlock list** (characters, weapons, stages) with visible locked slots and their conditions ("survive 10 min with only one weapon").
- **Collection of discoverable combinations**, shown as a grid with gaps.
- **A difficulty ladder** (curse levels, modifiers) for players who have cleared the base game.
- **A daily seeded run** with a leaderboard, so everyone faces the same offers.

## Solo-first adaptation
The genre is solo by nature. Co-op is a layer: shared XP, separate builds, and a revive. Make sure scaling for more players does not make the solo run feel underpowered; tune solo first and scale enemy count up for groups.

## Roblox notes
- **Mobile:** one thumb steers. Never require a second input to attack. Put the upgrade choice in large cards that can be tapped without the run continuing underneath (pause during the pick in solo; in co-op, give a short timer and auto-pick).
- **Performance:** hundreds of enemies will break a naive build. Simulate enemies as data on the client or server and render with bulk moves; avoid a Humanoid per enemy. Test on a low-end phone at minute 20 of a run.
- **Readability:** low-poly enemies with strong silhouettes and one accent color per enemy type. Your own projectiles should never be the same color as enemy threats.
- **Discovery:** the thumbnail is the late-run screen full of your power. The title should name the verb or the twist, not "survivors".
- **Monetization:** cosmetics, extra character slots or stages as one-time purchases. Never sell rerolls that turn a skill choice into a paid one in competitive modes.

## Craft techniques
- **The pickup magnet:** XP gems should accelerate toward the player once in range, with a rising pitch as several are collected in a row. This tiny thing is a large part of the feel.
- **Weapon identity in one glance:** each weapon needs a distinct shape, color and sound so the player can hear their build. A run at minute 15 should sound like the build.
- **Elite enemies with one rule:** a charger, a splitter, a shooter. Each forces movement in a new way, which keeps "only moving" interesting.
- **The end-of-run screen:** damage by weapon, time survived, what you unlocked, and the next locked item with its condition. That screen is the bridge to the next run.

## Pitfalls
- Copying the 2D top-down formula and changing only the art. The space, the verb or the structure must change.
- Upgrades that are only stat bumps. "+10% damage" is not a decision.
- Visual noise that hides enemy attacks on a phone.
- No content plan after launch. Megabonk held only 2.6% of its peak.
- Runs longer than 30 minutes with no checkpoint. Mobile sessions break.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| One main verb | Can the run be played with one thumb only? Any required second input scores 0. |
| Pick-1-of-3 every 20-40 s | Log level-up times for one run. Median gap in range scores 2. |
| Discoverable combinations | Does any combination exist that the game does not show up front? Did the tester find or hear of one? |
| Absurd power by minute 10-15 | Screenshot at minute 2 and minute 15. Is the difference obvious to someone who has never played? |
| Long unlock list | After one run, how many locked items are visible with conditions? |
| Readable at peak density on a phone | Phone-view capture at peak density. Can the tester point at the thing that killed them? |
