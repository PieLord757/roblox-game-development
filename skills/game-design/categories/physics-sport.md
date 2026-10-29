# Physics sport (`physics-sport`)

Read the `physics-sport` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a one-sentence sport goal played through deterministic physics, with a skill ceiling that keeps rising.

---

## What great looks like
- **The goal fits in one sentence.** Rocket League is "hit the ball into the goal." A viewer understands a match in seconds, and the same viewer can still be amazed by an aerial ten years later.
- **The same touch gives the same result.** Because the ball behaves the same way every time, players can practice a shot and then rely on it. That is what lets the ceiling keep rising.
- **Short matches make "one more" easy.** Five-minute matches mean a loss is quickly forgotten and a win quickly repeated.
- **Signature skills have names.** Aerials, flip resets, spikes and curves become words the community uses. Volleyball Legends and Blue Lock Rivals sit at 95.2% and 96.6% liked `[RBX]` with that structure.

## The hook
- **First 10 s:** the player is on the field with the ball near them. The first touch has a satisfying sound and the ball reacts with weight.
- **First 60 s:** a shot on goal, ideally a goal. Kickoff positions should put the new player near the action.
- **First 3 min:** a full short match, a goal scored or saved, and a visible next skill or reward.

## Loop tuning
- **Match length:** 2-5 minutes, with overtime on ties. If matches feel long, shrink the field before cutting time.
- **Team size:** 1v1 to 3v3. Bigger teams dilute each player's touches.
- **Ball physics:** tune ball weight and bounce so that a beginner's touch moves it meaningfully and a skilled touch can place it precisely. Change one value at a time and replay the same shot to compare.
- **Reset after a goal:** a short celebration (2-4 s), then kickoff. A replay of the goal is worth the time only if skippable.
- **Boost or stamina:** a limited resource for speed or jumps adds decisions. If players never run out, it is not a resource.

## Depth and mastery
- **The skill chain:** touch the ball → aim the touch → position for a pass or rebound → time a jump or aerial → read the ball's bounce early → rotate with teammates → signature tech.
- **The depth multiplier:** player movement × ball physics. More movement options (jumps, dashes, flips) multiply the ways to touch the ball.
- **Defense matters:** saves, blocks and positioning should be as satisfying as goals.
- **Style systems (if any)** should change how you touch the ball, not how strong you are.

## Retention engine
Pick at least two:
- **Ranked matches with tiers** and seasonal resets.
- **Training packs or skill challenges** with personal bests.
- **Cosmetics** (trails, goal explosions) earned and bought.
- **Style or ability unlocks** that are side-grades.

## Solo-first adaptation
This category is a **Variant**: it is solo-viable only with competent bot teammates and opponents plus a training mode that is fun alone.
- **Bots that rotate, pass and miss** like people. A team of bots that all chase the ball is worse than no bots.
- **Free play and training packs:** shooting drills, saves, aerial courses with times. Rocket League's free-play is the model.
- **Fill matches with bots** under 6 s, and swap bots for humans between matches.

## Roblox notes
- **Physics ownership:** give network ownership of the ball to whoever is touching it, or simulate the ball on the server with client prediction. A ball that teleports at 150 ms ruins the category.
- **Mobile:** a stick plus 2-3 big buttons. Aim assist toward the goal on shots for phone players.
- **Style gacha** is common on Roblox sports games and draws pay-to-win complaints. If you sell styles, keep them side-grades.
- **Adult growth:** Roblox has said sports is a target genre for older players `[RBX]`.

## Craft techniques
- **Ball feel:** a strong impact sound scaled by hit speed, a brief ball squash, and a trail at high speed.
- **Camera:** a ball-cam toggle (camera keeps the ball in view) is essential once play gets aerial.
- **Goal moment:** a big sound, a field-wide effect and a short slow-motion replay.
- **Readable field:** goal lines, ball shadow on the ground to judge height.

## Pitfalls
- Random bounces from physics jitter.
- A low skill ceiling (Fall Guys's lesson).
- Requiring full human teams with no bots.
- Styles or abilities that decide matches.
- Shipping without a training mode.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| One-sentence goal | Can a naive viewer state the goal after one goal on video? |
| Deterministic physics | Repeat the same touch 5 times. Does the ball do the same thing? |
| Matches of 2-5 min, 1v1 to 3v3 | Time 3 matches. |
| Visible skill ceiling | Is there at least one named advanced skill a tester can see or try? |
| Fun solo training or free play | With nobody online, is there a mode a tester enjoyed for 5 minutes? |
