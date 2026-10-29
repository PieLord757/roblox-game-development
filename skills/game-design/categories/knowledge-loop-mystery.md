# Knowledge-loop mystery (`knowledge-loop-mystery`)

Read the `knowledge-loop-mystery` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a reset (a time loop, a death, a new day) wipes everything except what the player knows, in a hand-made world where every clue fits.

---

## What great looks like
- **The player could finish in minutes if they knew how.** Outer Wilds can be completed in about 20 minutes by someone who knows the answer. Every hour before that is learning. That is the purest form of the category: knowledge is the only upgrade.
- **The world runs on a schedule, and the schedule is the puzzle.** A sandy planet drains into its twin over the 22-minute loop `[UNV: exact length]`, so a tunnel that is buried at minute 2 is open at minute 15. The player who notices that has learned something no item could give them.
- **The reveal is assembled, not shown.** The ending of Outer Wilds lands because the player put the pieces together across dozens of loops. A cutscene that explains it would have thrown that away.
- **The rules of the game become the plot.** Inscryption's card game is fun on its own, and then its rules start to change, and the change is the story. The mechanic carries the twist, so the twist cannot be skipped.

## The hook
- **First 10 s:** something wrong and specific in a place the player can move through. A clock face, a ticking sound, a stranger who glances at the player too long. Movement and looking must work immediately.
- **First 60 s:** the player learns one fact that will matter later ("the guard leaves the door at 2:10") even if they do not know yet that it matters.
- **First 3 min:** the first reset. The player wakes in the same place, sees the same opening beat, and realizes the fact they learned still works. That moment ("I knew that would happen") is the category's core pleasure. If the first reset comes after 10 minutes, most players never feel it.

## Loop tuning
- **Loop length:** 5-12 minutes of real time is the workable range for a session-friendly game `[analysis]`. Under 5 and the world cannot hold enough events; over 15 and every failed idea costs too much.
- **Reset cost:** under 5 s from failure to control, with a skippable opening. The 30th loop must not replay a 40-second intro.
- **Events per loop:** aim for a scheduled event the player can witness every 30-60 s somewhere in the space. Fewer and loops feel empty; many more and the player cannot track them.
- **Shortcuts:** once the player has proven they know something (opened a lock once), let them skip the busywork (the code is remembered, the door opens with one action). Knowledge should cut time, not add chores.
- **Tune by watching stuck players.** If a playtester circles for 5+ loops without a new fact, the world needs a louder hint at that point, not a text tooltip.

## Depth and mastery
- **The skill chain:** move and look → notice a scheduled event → predict it → be in position for it → change it → chain several changes in one loop → find a route that solves everything.
- **The depth multiplier:** schedule × space. Each event matters because of where it happens, and each place matters because of when. The interesting decisions are "where do I need to be at 4:10?"
- **Layered clues:** each important fact should be reachable two or three ways (an overheard line, a document, an observed action), so players who missed one are not stuck.

## Retention engine
- **"I need to know"** drives D1. It is strong but finite.
- **After the solve:** add a repeatable layer so the game does not die once solved. Options: speed and fewest-loop boards; a daily seeded variant where the schedule shifts; a draft layer like Blue Prince's room drafting; optional secrets that only make sense once the main mystery is known.
- **Chapters:** new places or new loops with the same rules extend the life. Ship the first chapter complete, and show the next chapter on a visible schedule.

## Solo-first adaptation
- The category is natively solo: a loop only makes sense for one mind. Keep it that way.
- Other players can appear as async helpers without breaking the fiction: leave a mark on the wall for strangers, or show where other players died or stood at a moment, as hints a player can opt into.
- Never require a second player to see a clue.

## Roblox notes
- **Resetting cleanly** is the main technical risk. Keep world state in one data table the server can rebuild from, and rebuild NPCs and doors from it on every reset instead of undoing changes one by one.
- **NPC schedules:** drive them from a single timeline module keyed on loop time, so a change to one character's route does not break another's.
- **Mobile:** clues must be readable at phone size. A note in 10-point text on a desk is invisible on a phone; zoom on interact.
- **Low concurrent players are normal.** Outer Wilds peaked at 7,936 `[SC]`. Plan monetization and success measures around play days and chapter launches, not peak CCU.
- **Spoilers:** a solved mystery spreads on video. Randomize a small part of each playthrough (which room hides the key, which passenger lies) so a video helps but does not finish the game.

## Craft techniques
- **Plant, then pay off, in a ledger.** Keep a table of every clue: where it is, why a first-time player walks past it, and what it means later. If a payoff has no plant in the first act, players call the twist a cheat.
- **Twist through the mechanic.** The best reveal changes how the player understands the loop itself (why it resets, who else is affected, what the reset protects). If the twist could be delivered in a different game, it is decoration.
- **Avoid stock twists.** "It was you all along", "you were dead the whole time" and "it was all a simulation" are expected by experienced players. If one is unavoidable, the mechanic has to make it feel earned and specific, and it must not repeat a twist the studio has used before.
- **Show the schedule in the world.** Clocks, bells, train announcements and lighting changes let the player feel time without a HUD timer.
- **Reward curiosity with facts, not items.** Every time a player goes somewhere odd, give them a fact, a line of dialogue or a view that changes their model of the world.

## Pitfalls
- Gating progress behind items or combat. It turns a knowledge game into a grind and kills the "aha".
- Puzzles that need a guess. If the answer cannot be reasoned from things the player saw, it is a coin flip.
- Text dumps that explain the mystery. Let the player read it from events.
- A twist that is the only content. Once spoiled, the game should still be fun to play for its loop.
- A long opening before the first reset. The first reset is the hook.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Knowledge is the only progression | After 3 loops, can the tester name facts they now use? Is any progress gated by items or stats? |
| Fast, cheap resets | Time from failure to control. Under 5 s scores 2; under 20 s scores 1. Can the opening be skipped? |
| A fixed, exploitable schedule | Does the same event happen at the same time across loops? Did the tester use one on purpose? |
| Clues point to each other | Ask the tester why they went somewhere. A reason from an earlier clue scores; "I guessed" does not. |
| A reveal the player assembles | Did the tester state part of the truth before the game showed it? |
| A repeatable layer after the solve | Is there a board, daily variant, draft layer or secret set that works after the main mystery? |
