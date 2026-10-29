# Party elimination (`party-elimination`)

Read the `party-elimination` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a crowd plays short obstacle or minigame rounds, and each round cuts the field until one winner is left.

---

## What great looks like
- **A round explains itself.** In Fall Guys a spinning bar sweeps the stage, and you know to jump it. Nobody reads a rule.
- **Losing is funny.** Wobbly bodies tumbling off a ledge make an elimination a laugh, not a defeat. That is why the format spread through clips in its launch summer.
- **The final round is a show.** A field of 60 becomes a handful, and the last round is tense enough that everyone eliminated watches.
- **Players make the rounds.** Ultimate Chicken Horse has each player place a trap before the race, so the level is new every round and the competition is in the design.

## The hook
- **First 10 s:** in a round, moving, with the goal visible ahead.
- **First 60 s:** at least one round finished, qualified or eliminated, with a funny fall along the way.
- **First 3 min:** 3+ rounds of different types and a final, or a clear placement and reward.

## Loop tuning
- **Round length:** 30-120 s. Transition to the next round in under 10 s, with a quick round title card.
- **Cut rate:** cut 30-50% of the field per round so a show lasts 4-6 rounds.
- **Round variety:** race, survival, team and final types. Do not repeat a round in one show.
- **Field size:** start at 20-60. Eliminated players spectate the rest of the show or requeue instantly.
- **Chaos versus skill:** most outcomes should be skill (routes, timing, grabs), with chaos as flavor. If a tester cannot say why they lost, there is too much chaos.

## Depth and mastery
- **The skill chain:** move and jump → time obstacles → find faster routes → use grabs and bumps → read the crowd to avoid pile-ups → master each round type.
- **The depth multiplier:** round type × crowd behavior. The same round plays differently at 40 players and at 6.
- **Shortcuts and risky routes** reward regulars without blocking new players.
- **Player-made rounds** are the long-term answer to content fatigue.

## Retention engine
Pick at least two:
- **New rounds on a visible cadence** or a player round editor.
- **Crowns or wins** as a counted status.
- **Seasonal cosmetic tracks.**
- **Daily challenges** tied to round types.

## Solo-first adaptation
This category is a **Variant**: solo-viable only with bot racers that look and fail like people, plus a solo progression.
- **Bots that make human mistakes:** misjudged jumps, pile-ups, hesitation. Perfect bots or bots that all fail the same way both kill the illusion.
- **Fill the field with bots** at any CCU so a show always starts in seconds.
- **A solo path:** daily solo courses, personal bests per round, and a progression that does not need wins against humans.

## Roblox notes
- **Physics ownership:** let each client own its own character for responsive movement; resolve collisions with obstacles locally and validate on the server.
- **Cheating:** the format was hit by cheaters. Server-check finish times and positions.
- **Mobile:** stick plus jump plus grab. Keep obstacles readable on a small screen.
- **Trend risk:** licensed-feeling elimination trends spike and collapse (Ink Game is at about 3% of its peak, 79.2% liked `[RBX]`).

## Craft techniques
- **Round title cards** that name the round with an icon, shown for 2 s.
- **Ragdoll falls with a comic sound** on elimination.
- **A crowd counter** on screen ("23 remaining" with a cut line).
- **Camera:** chase cam behind the player; switch to a wide shot of the leaders after elimination.

## Pitfalls
- Too few round types, so the show repeats within an hour.
- Rounds decided by luck.
- Long waits between rounds.
- A thin skill ceiling with no way to improve.
- Relying on a trend theme instead of round design.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Round explained in 3 s by what you see | Show a naive tester a new round. Did they know the goal before it started? |
| Rounds of 30-120 s with fast transitions | Time 4 rounds and their transitions. |
| Physical comedy that makes losing funny | Record eliminations. Do testers laugh or groan? |
| Round variety or player-made rounds | Count distinct round types seen in 3 shows. |
| A skill edge a regular can feel | Did a tester's results improve over 3 shows? Can they name a better route? |
