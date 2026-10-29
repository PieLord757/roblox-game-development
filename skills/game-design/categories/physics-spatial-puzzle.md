# Physics and spatial puzzle (`physics-spatial-puzzle`)

Read the `physics-spatial-puzzle` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** short levels solved by acting on physics or space (drawing a shape, placing an object, bending a rule) in real time, where the player's own idea works.

**Evidence note:** the only sourced exemplar is Human Fall Flat 127,516 `[SC]`. Draw-to-solve mobile games (Brain It On, Save the Doge) and Portal 2 are `[UNV]`. Treat the tuning numbers here as `[analysis]`.

---

## What great looks like
- **The problem reads in one look.** A draw-to-save level shows a small creature, a swarm and a few seconds of ink. Nobody needs a sentence to know what to do.
- **Your idea works, even if it is not the designer's.** Human Fall Flat's levels let a player stack boxes, swing on a rope or throw a friend to cross the same gap. The pleasure is "I solved it my way," and that only happens when physics is consistent and the level allows more than one answer.
- **Failure is funny and informative.** A drawn wall that topples and lets the swarm in shows exactly why it failed: it was too thin, too short or unsupported. The next attempt is better because the physics taught something.
- **One idea per level, then a twist.** Portal introduces a mechanic safely, practices it, then flips it. `[UNV]` A level that combines three new ideas teaches none of them.

## The hook
- **First 10 s:** the first level is on screen and the player can act (draw, place, push) with no text.
- **First 60 s:** two or three levels solved, each finishing with a clear success moment.
- **First 3 min:** a level where the obvious idea fails and a second idea works, which is the moment the player learns the game is about thinking, plus a visible level map or star count.

## Loop tuning
- **Level length:** 10-60 s to solve for an experienced player; early levels under 20 s. `[analysis]`
- **Retry:** instant, with the previous attempt optionally shown faded so the player can adjust rather than start from nothing.
- **Difficulty curve:** sawtooth. Introduce an idea with an easy level, practice it 2-3 times, test it with a harder one, then drop difficulty as the next idea arrives.
- **Resource limits:** ink, pieces or moves are the main dial. If testers solve every level with brute force, tighten the limit; if they never find any solution, loosen it or add a visual hint in the level layout.
- **Solve-rate target:** most levels solved within 3 attempts by most testers; one level in five should take longer and feel like an achievement. `[analysis]`

## Depth and mastery
- **The skill chain:** acting on the world → predicting physics → using constraints (weight, balance, friction) → combining tools → optimizing (less ink, fewer pieces, faster).
- **The depth multiplier:** tools or materials × level hazards. If each material behaves differently (heavy, bouncy, brittle, sticky) and each hazard tests a different property, the combinations stay fresh for many levels.
- **Efficiency as mastery:** stars or scores for solving with fewer resources give experts a reason to replay solved levels.

## Retention engine
Pick at least two:
- **Stars or efficiency scores** per level, and a total that unlocks new worlds.
- **A daily puzzle** with a leaderboard for fewest resources or longest survival.
- **An endless or survival mode** where the same tools face escalating pressure.
- **Player-made levels** if an editor is feasible; this is the strongest long tail for puzzle games.

## Solo-first adaptation
- Natively solo. Other players are best as a comparison (see how others solved the same level, a replay of the best solution) rather than as co-solvers.
- If a co-op mode exists, every level must still be solvable alone.

## Roblox notes
- **Run physics locally.** Objects the player creates should be simulated on the client for instant response; the server only records results and validates scores loosely.
- **2D on Roblox:** a fixed side camera with objects held to a plane gives a convincing 2D look with the real physics engine doing the work.
- **Stability:** drawn or built objects made of many welded pieces jitter. Merge segments, cap piece counts, and tune density and friction before tuning levels.
- **Mobile:** drawing and placing with a finger suits phones well. Test finger precision on a real phone, not just a mouse.
- **Content cost:** describe levels as data (pieces, hazards, goals) so variants are cheap to make.

## Craft techniques
- **Teach with layout, not text.** Place the first gap exactly one box wide next to one box.
- **Make physics legible:** show weight with size and material, show brittleness with cracks, show stickiness with texture. The player should predict behavior from looks.
- **Success moment:** a clear sound, a short slow-motion on the decisive moment, and the score. Make the solve feel earned.
- **Failure replay:** let players watch the last attempt fail in slow motion. It turns frustration into learning.

## Pitfalls
- Physics jitter making a correct idea fail. This is the fastest way to lose trust.
- Levels with exactly one intended solution.
- Text tutorials before the first level.
- Running out of levels with no endless, daily or editor mode.
- Introducing two new ideas in one level.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Readable at a glance with no text | Does a new tester act correctly on level 1 within 10 s without reading? |
| Multiple valid solutions | Watch 3 testers solve the same 3 levels. Count distinct solutions. |
| Consistent physics | Repeat the same action 5 times. Do results match? Note any jitter-caused failure. |
| One idea per level, then a twist | Map the first 10 levels: which idea each introduces or twists. |
| A replay reason | After finishing a level, is there a visible reason to replay it (stars, score, daily mode)? |
