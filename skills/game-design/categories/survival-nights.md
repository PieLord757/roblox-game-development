# Survival nights (`survival-nights`)

Read the `survival-nights` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** prepare by day, survive by night, and push a counter (nights, kilometers) toward a goal that feels impossible at the start.

---

## What great looks like
- **The fire is the base and the clock.** In 99 Nights in the Forest (151K / 442K `[RBX]`, 2.09M `[Rolimons]` peak) the campfire is the safe zone, and feeding it grows the zone. The player always knows what to do with wood, and always knows the dark is coming.
- **The counter is the goal.** "Night 99" needs no explanation, and every night survived is a visible step. Players brag about the number.
- **The base moves.** Dead Rails (16.8K / 62K `[RBX]`) made the base a train crossing 80 km. Stops at towns are the day; defending the moving train is the night. Its strong runs were not enough on their own: with a shallow meta it fell to 2% of its peak.
- **Night has rules.** A good night threat has a pattern: it circles, it fears light, it comes from one direction. The player who learned it survives with less.

## The hook
- **First 10 s:** the player is next to the base (fire, train) with a tool, and the edge of the dark is visible.
- **First 60 s:** the first resources gathered and fed into the base, with a visible change (the fire grows, the train refuels).
- **First 3 min:** first dusk arriving, with a clear warning. The first night should come in under 5 min, and the first night should be survivable for anyone who prepared at all.

## Loop tuning
- **Day length:** 2-4 min early, enough to gather and build one thing. Do not let days get long as the game goes on; add more to do instead.
- **Night length:** 1-2 min early, growing slightly. Nights that drag become chores.
- **Preparation reward:** each day's work should visibly change the next night (a wall, a bigger safe radius, a better weapon). If preparing does not matter, nights are just waiting.
- **Threat scaling:** add one new threat type every few nights instead of only scaling numbers.
- **Failure:** losing a night should end the run or cost something large, but the run's meta currency always comes home.
- **Tune in big steps.** If players hoard and never build, halve resource costs before adding more resources.

## Depth and mastery
- **The skill chain:** gather → feed the base → craft tools → read night threats → position at night → plan days around the next night's threat → specialize with classes or roles.
- **The depth multiplier:** base upgrades × threat types. Each upgrade should counter some threats and not others, so the build order depends on what is coming.
- **Routes and efficiency:** experienced players learn where resources are and finish a day's work in half the time, leaving time for risky side trips.

## Retention engine
Pick at least two:
- **The counter as a personal best** (highest night, farthest distance).
- **Classes or roles** unlocked over runs, each changing how a day plays.
- **Base tiers** that unlock in a meta layer between runs.
- **Events** that change the night (a blood moon, a special threat).

## Solo-first adaptation
Tune the solo night first. A solo player needs either a smaller map, slower threats, or a helper (a dog, an NPC survivor) so they can gather and defend. Scale threats up with group size. A group should be more fun, not required.

## Roblox notes
- **Servers:** small servers (4-12) keep the group readable; larger servers (25) work only if the base is shared and big.
- **Mobile:** gathering is one button with auto-target; building is a few large choices placed in the world, not a grid menu.
- **Lighting:** the day-night switch is the game's signature. Make dusk look and sound distinct, and give the night a strong silhouette contrast so threats are visible against the dark.
- **Performance:** keep night threat counts modest and simulate distant ones cheaply.
- **Flags:** many versions are open-world or use vehicles. Check `studio-profile.md` hard rules before choosing that form; a small authored map works too.

## Craft techniques
- **The dusk warning:** a sound sting, a color shift and a UI cue 20-30 s before night. Players should never be surprised by night itself, only by what comes.
- **Night as a set piece:** each night has a small story (a wave, a boss, a rescue). "Survive 2 min" is not a story.
- **Resource readability:** each resource has a distinct shape and color, visible from a distance.
- **The morning payoff:** a sunrise beat, the counter ticking up, and a reward. It is the moment that sells the next day.

## Pitfalls
- Grind padding: long days spent chopping the same tree.
- A meta that runs out once the counter is reached.
- Solo play that is technically possible but miserable.
- Night threats with no pattern, so preparation feels pointless.
- Building menus that are grids of icons.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Day and night cycle | Is the switch from preparing to surviving obvious? Did the tester change behavior at dusk? |
| Base that visibly grows | Screenshot the base at night 1 and night 3. |
| Counter as the long goal | Is the counter on screen, and did the tester mention their number? |
| Scaling threats with readable rules | After a night, can the tester describe how a threat behaves? |
| Solo tuning | A solo tester survives night 1 and 2 with reasonable play. |
