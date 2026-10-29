# Melee skill duel (`melee-skill-duel`)

Read the `melee-skill-duel` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** close-range fights decided by reading wind-ups and choosing parry, dodge, attack or feint under a stamina limit.

---

## What great looks like
- **Every exchange is a guess you can make smarter.** In Untitled Boxing Game a 1v1 is a string of reads: you saw them throw the heavy last time, so you slip and counter. Losing tells you exactly which read you got wrong.
- **The punish is the reward.** A clean parry freezes both fighters for a beat, the opponent staggers, and you get a short window to land a combo. That window is the moment players chase.
- **Styles change rhythm, not numbers.** A fast style with short wind-ups plays differently from a slow one that hits hard, and both can win.
- **Stamina makes patience a skill.** Spamming attacks drains you; the player who waits and reads wins the late exchanges.

## The hook
- **First 10 s:** a weapon or fists in hand, an opponent (human or sparring bot) in front of you, and the attack button shown in the world.
- **First 60 s:** the player lands a hit, gets hit, and pulls off one parry or dodge with a satisfying response. If they have only swung at air, the hook missed.
- **First 3 min:** a full round won or lost, a reward, and a clear "learn this next" (a feint, a heavy, a new style).

## Loop tuning
- **Wind-up length:** attacks must be reactable on a phone. Start around 300-500 ms for heavy attacks and 200-300 ms for light ones, and test on a phone at 150 ms latency. If parries feel like guesses, lengthen wind-ups before anything else. `[analysis]`
- **Parry window:** 150-250 ms, with a cost for a failed parry (a short vulnerable recovery). Without a cost, players spam parry. `[analysis]`
- **Stamina:** a full bar should allow about 4-6 actions before running dry, and refill in 2-3 s of rest. If fights are frantic button-mashing, cut the bar in half.
- **Round length:** 30-90 s per round, best of 3 or 5. A round that runs over 2 minutes means damage is too low or defense too strong.
- **Hit-stop:** 60-120 ms on clean hits, longer on parries and finishers. This sells weight more than any animation.

## Depth and mastery
- **The skill chain:** attack → block or parry → dodge → punish → manage stamina → feint → read the opponent's habits → condition them (show a pattern, then break it).
- **The depth multiplier:** move timing × style. Each style's wind-ups and ranges create different read problems against each other style, so matchups matter.
- **The feint:** a cancellable wind-up that costs stamina is the single biggest depth tool. It turns reaction into prediction.
- **Range control:** spacing (staying just outside the opponent's reach) is the veteran skill that beginners do not see. Make ranges visible in the animation.

## Retention engine
Pick at least two:
- **Ranked 1v1 with tiers** and protected new-player matchmaking.
- **Style or weapon unlocks** earned in play, each with a mastery track.
- **Win streaks** and round-win stats shown in the lobby.
- **Weekly challenges** that push style variety.

## Solo-first adaptation
- **A sparring bot that reads like a person.** Bots should have habits (likes to heavy after a block, dodges left), reaction times with variance, and occasional mistakes. A bot that parries everything teaches nothing.
- **A bot gauntlet:** named opponents, each built to teach one read (the feinter, the turtle, the rusher). This doubles as the tutorial.
- **Fill queues with bots in under 6 s**, labeled honestly; ranked points only from humans.

## Roblox notes
- **Latency:** resolve your own wind-ups and parries on your client for feel, confirm on the server, and show the opponent's wind-up as early as possible. Test parries at 150 ms and 300 ms; if they fail, lengthen wind-ups rather than tightening windows.
- **Mobile:** separate large buttons for attack, parry and dodge; a swipe for dodge direction. Timing games die on phones when buttons are small.
- **Skill-gap calcification:** Combat Warriors fell from a 1.46B-visit game to 1.2K CCU after new players kept getting stomped `[RBX]`. Protect the first matches.
- **Monetization:** styles earned in play, cosmetics for sale. Gacha spins for styles are common on Roblox and generate complaints; if you use them, make every style viable.

## Craft techniques
- **Readable wind-ups:** exaggerate anticipation poses (shoulder back, weapon raised) and add a short audio cue for heavies.
- **Four feedback channels on a clean hit:** a heavy impact sound, hit-stop, a stagger animation and a camera nudge. A parry gets a distinct metallic or slap sound and a flash.
- **Ragdoll finishers** for round-winning hits; they are the clip.
- **A death recap** showing the last exchange slowed down: "you parried early."

## Pitfalls
- Wind-ups that look identical for light and heavy attacks.
- A parry with no cost, so defense always wins.
- Stamina that never matters.
- Matching new players into veterans.
- Selling styles that are strictly better.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Readable wind-up, reactable on a phone | Record heavies on a phone view at 150 ms. Can a tester react to them? |
| Parry, dodge, stamina triangle | Does each option beat one and lose to another? Did any one option win most exchanges? |
| Earned punish window | After a clean parry, is there hit-stop, a stagger and time to hit back? |
| 1v1 with protected matchmaking | Who did a new account face in its first 5 matches? |
| Style variety changes timing and range | Compare two styles on video. Do wind-ups and reach differ? |
