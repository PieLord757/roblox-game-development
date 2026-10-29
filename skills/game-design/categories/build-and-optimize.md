# Build and optimize (`build-and-optimize`)

Read the `build-and-optimize` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** place and connect buildings or machines to grow output, and fix the bottleneck that growth reveals.

---

## What great looks like
- **Watching it run is the reward.** Factorio's hook is watching a belt you designed run by itself. The player made something that works without them.
- **Each solution creates a bigger problem.** Factorio's automation unlocks a bigger logistics problem every tier, so the game never runs out of puzzles (118,166 `[SC]`).
- **The body in the factory.** Satisfactory moved the genre into first person and peaked higher (185,957 `[SC]`). Walking under your own conveyor lines makes scale felt, not read.
- **Long life at low CCU.** Classic Roblox tycoons (Theme Park Tycoon 2 1.9K, Lumber Tycoon 2 1.7K `[RBX]`) live for years with wide age ranges, because building something of your own is durable.

## The hook
- **First 10 s:** the player is in the world with a tool and something to place or harvest.
- **First 60 s:** the first machine placed and running, producing something visible.
- **First 3 min:** the first bottleneck seen in the world (a pile-up, an idle machine) and fixed by the player.

## Loop tuning
- **Hand-work phase:** keep it to 2-5 minutes before the first automation. Grind before automation is the most common failure.
- **New problem cadence:** a new resource, machine or constraint every 5-10 minutes early, every session later.
- **Throughput feedback:** show rates in the world (items per minute on a sign or meter by the machine) so optimizing is visible.
- **Content wall:** plan tiers so the player always has a next bigger problem. A tycoon whose plot fills up is finished.

## Depth and mastery
- **The skill chain:** place → connect → balance ratios → route logistics → design compact layouts → scale.
- **The depth multiplier:** recipes × space. Recipes set what must connect; space limits how. Both together create layouts worth sharing.

## Retention engine
- **Tiers that unlock bigger problems.**
- **A world the player owns** that persists and can be shown to others.
- **Blueprints or shared layouts** as a social layer.
- **Goals per tier** (launch the rocket, open the ride) to give endpoints.

## Solo-first adaptation
- **Required variant:** first- or third-person building in real time (the Satisfactory form). Top-down placement menus fail the non-menu axis.
- The category is solo by nature. Visitors and co-op builders are a bonus.

## Roblox notes
- **Performance at scale** is the main risk. Move items with batched updates, simulate off-screen production as numbers, and cap visible items.
- **Mobile:** precise placement is hard on phones. Use snapping grids, large rotate buttons and an undo.
- **Plot instancing:** each player's build lives on a plot or in a private instance; save it reliably and often.
- **Monetization:** cosmetic building parts, extra plots, never resources that skip the puzzle.

## Craft techniques
- **Make bottlenecks visible in the world:** piles, idle machines with a light, a belt that backs up. The player should find the problem by looking.
- **Satisfying motion:** machines that animate, items that move smoothly, sounds that layer into a hum as the factory grows.
- **Undo and move freely:** rebuilding should be cheap so players experiment.
- **One new idea per tier:** each tier adds one concept (splitting, priority, power) that combines with earlier ones.

## Pitfalls
- Grind before automation.
- An unreadable UI of numbers instead of a readable world.
- Frame rate collapse at scale.
- A finite plot that ends the game.
- Placement only through menus.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Hand-work gives way to automation early | Time to first automated production. |
| A visible bottleneck in the world | Did the tester find a problem by looking at the world rather than a menu? |
| Each tier unlocks a bigger problem | After a tier-up, what new problem appears? |
| Watching the machine run is satisfying | Did the tester stop to watch their build? Count motion and sound feedback. |
| Building in first or third person with the body | Count placements done in the world versus from a top-down menu. |
