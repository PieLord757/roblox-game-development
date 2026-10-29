# Job-sim empire (`job-sim-empire`)

Read the `job-sim-empire` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** do a mundane job by hand, satisfyingly, then grow it into an empire with hiring and automation.

---

## What great looks like
- **The job is a toy.** Supermarket Simulator's hook is scanning items with satisfying beeps. A player who does not care about business still enjoys the physical action.
- **Mixing is a discovery game.** Schedule I's ingredient combinations change a product's effects and price, so the job hides a recipe puzzle. Players share recipes, which spreads the game.
- **Stakes make it a story.** Schedule I adds a light police-heat system. A delivery becomes a risk, and a mundane job becomes something players retell.
- **The audience out-plays the original.** A Roblox cleaning game peaked at 83,591 CCU `[press]`, beating the Steam game that inspired it. A proven job loop transfers, if its feel is right.

## The hook
- **First 10 s:** the player is holding the tool and doing the job. No hiring screen, no shop tour.
- **First 60 s:** the first payout, with a satisfying sound and number.
- **First 3 min:** the first upgrade bought and it visibly changes the job (a faster scanner, a wider mop, a second register). Only 60% of players bought the first upgrade in one creator's data, and fixing first-session progression lifted D1 from 6-8% to about 16% `[UNV: self-reported]`.

## Loop tuning
- **Action cycle:** one complete job unit (a customer, a delivery, a room) every 20-60 s.
- **First upgrade price:** affordable in 2-3 job units. Later upgrades every 3-5 minutes in the first session.
- **Pressure:** a quota, a queue, a timer, spreading mess or heat. Without pressure the job becomes chores. Tune pressure so a focused player keeps up and a distracted player feels it.
- **Automation timing:** the first hire or machine around minute 10-20, freeing the player to take on a harder job, not leaving them with nothing to do.

## Depth and mastery
- **The skill chain:** do the job → do it faster → route efficiently → handle pressure spikes → manage helpers → optimize the layout or recipe.
- **The depth multiplier:** job tasks × pressure events. Each pressure event (a rush, an inspection, a spill) asks the player to reprioritize tasks.
- **Recipes or combinations** add a discovery layer that players trade knowledge about.

## Retention engine
- **Expansion:** new locations or job types every few sessions.
- **Daily orders** with specific twists.
- **Rank and title** progression with visible cosmetics.
- **Offline progress** from helpers, as a layer only.
- **Server events** where the whole server works one big job together.

## Solo-first adaptation
- The category is natively solo. Co-op crews are a bonus layer that makes it more fun to stream.
- Scale the job to the player count so one player is never overwhelmed.

## Roblox notes
- **Tycoons already exist on Roblox.** The plain "earn and expand" version has no edge. The edge is the feel of the hands-on job plus real stakes.
- **Mobile:** job actions should be one tap or one hold with a clear target.
- **Performance:** many customers or mess tiles need batched updates; never one remote per item.
- **Monetization:** sell speed-ups that do not remove the job (a cosmetic uniform, a helper), never something that skips the pressure.

## Craft techniques
- **Juice the job:** a sound, a visual change and a number for every unit of work. Cleaning needs a visible before and after; scanning needs a beep and a bag filling.
- **Make mess or demand visible in the world**, not in a bar. A queue of customers, piles, smoke.
- **Theme with a moment.** The theme should generate one moment people retell ("the police showed up mid-delivery"). Ask what that moment is before choosing the theme.
- **Let automation reveal a new layer.** When the old job runs itself, the player should be pulled into a new, harder job, not a waiting room.

## Pitfalls
- A grim, fiddly execution of the job.
- A static mess with no pressure: the player finishes and leaves.
- Upgrades that are only bigger numbers.
- A theme with no moment.
- Automating so early that the hands-on job never gets learned.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| The hands-on job is satisfying as a toy | Does the tester keep doing the job when nothing pushes them? Count feedback channels per action. |
| First upgrade inside 3 minutes changes the job | Time to first upgrade; does the job look or play differently after it? |
| Pressure or stakes in the job | Did a quota, queue, heat or mess change what the tester did? |
| Automation frees the player for a harder job | After the first hire or machine, what does the tester do next? |
| A themed moment people retell | Ask the tester to tell you about the session. Did they describe a moment? |
