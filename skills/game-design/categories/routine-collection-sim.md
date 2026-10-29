# Routine collection sim (`routine-collection-sim`)

Read the `routine-collection-sim` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a daily routine (fish, farm, keep bees) fills a collection, the world changes while you are away, and a small skill game sits inside the routine.

---

## What great looks like
- **A skill moment inside the routine.** Fisch puts a reel minigame (keep a bar on the fish) inside every catch. That turns a sim into play, and it is why Fisch is the most action-friendly game in this family (46K / 103K `[RBX]`).
- **Depth and fairness can beat cadence.** Bee Swarm Simulator has the highest like ratio in the research set (95.6% `[RBX]`) with rare, large updates from a single developer. A deep hive puzzle and fair systems kept players for years.
- **Coming back to a changed world.** Grow a Garden's crops grow while the player is offline. Its creator calls it "the persistent world". The pull to check tomorrow is the retention engine.
- **A calendar of small goals.** Stardew Valley runs many goals in parallel inside each in-game day, so "one more day" is always a small, finishable step (21.5% ret `[SC]`).

## The hook
- **First 10 s:** the tool is in hand and the first action is possible: cast, plant, swing.
- **First 60 s:** the first catch or harvest, with the skill moment and a reveal of what you got.
- **First 3 min:** the first log entry and a visible gap in the collection, plus one thing the player can buy that opens somewhere new.

## Loop tuning
- **Action cycle:** 15-45 s from start to result.
- **Skill moment:** 3-8 s, with a clear success and a near-miss state. Make the minigame's difficulty depend on rarity, so rare catches feel earned.
- **Rarity curve:** the player should see a new entry every few minutes early, then every session, then rarely. Keep at least one visible "rare" in reach of a skilled player in session one.
- **Away-time:** offline change should be visible (grown crops, a full hive), but capped so it does not punish people who cannot log in every day.
- **Timed events:** weather or restocks every 10-30 minutes create a reason to be online now. Do not make the best items exclusive to tiny windows.

## Depth and mastery
- **The skill chain:** do the action → master the minigame → learn where and when rare things appear → plan tools and bait → chase specific entries.
- **The depth multiplier:** location × conditions (time, weather, bait). The same spot gives different results in different conditions, so knowledge of the world is mastery.

## Retention engine
- **The collection log** with gaps and rarity.
- **Offline change** and daily checks.
- **Timed events** and seasonal entries.
- **Tool progression** that opens new areas.
- **Trading** as an optional social layer.

## Solo-first adaptation
- **Required variant:** a real-time skill game inside the routine (the Fisch form). Pure timer growth with clicks fails the real-time axis.
- The routine is solo by nature; strangers add trading and showing off.

## Roblox notes
- **Young skew:** this family's biggest hits skew young (Grow a Garden, Minimal label). For an older audience, the skill moment, tone and fairness matter more than the timers.
- **Trend decay:** Grow a Garden is at about 1% of a 2.87M `[Rolimons]` peak. Do not build on a trend's timers alone.
- **Monetization:** sell convenience and cosmetics, not exclusive rares behind paywalls; older players punish FOMO.
- **Mobile:** the minigame must be one-thumb and readable on a phone.

## Craft techniques
- **Reveal with ceremony:** a short pause, a sound and a rarity color for each catch. The reveal is the reward.
- **Fill the log visibly:** silhouettes for unknown entries, with a hint line for where to look.
- **Make conditions readable:** weather, time and location shown in the world (rain, light, tide), not only on a HUD.
- **Bias perceived odds:** make near-misses visible and make the first rare arrive sooner than pure math would.

## Pitfalls
- A core action with no skill.
- Punishing absence harshly.
- Exclusive rewards in tiny timed windows.
- Tools that are only bigger numbers instead of new places.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| A real-time skill moment in the core action | Does the core action include a skill check with a visible fail state? |
| A collection log with gaps and rarity | Can the tester open the log and see what they are missing? |
| Something changes while away | Leave and return (or simulate time). What changed? |
| Timed events | Did an event happen in a 30-minute session, and did it change behavior? |
| Upgrades open new places | Does the first tool upgrade unlock a new area or condition? |
