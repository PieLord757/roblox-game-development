# Evidence investigation (`evidence-investigation`)

Read the `evidence-investigation` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** gather evidence with tools or by looking, then name the culprit, ghost or cause, under pressure.

---

## What great looks like
- **The evidence is a behavior, not a label.** In Phasmophobia the ghost type is told apart by evidence and by how it acts. At the hardest difficulty fewer clues show, so experts read behavior instead. That is mastery that never fully runs out, because behavior varies.
- **Looking is the verb.** Return of the Obra Dinn `[UNV]` is remembered for frozen scenes the player walks through to work out who is who from posture, clothing and where people stand. The deduction lives in the space.
- **You talk, and the case answers.** Phasmophobia's voice recognition lets the ghost hear its name spoken aloud. A tool or action that makes the scene react to the player is the category's best clip material.
- **Committing is scary.** Naming the answer should feel like stepping off a ledge: the player has enough to be confident but not certain.

## The hook
- **First 10 s:** the player is inside the scene with one tool in hand and something specific to look at (a body outline, a cold breath, a smashed glass).
- **First 60 s:** the first piece of evidence found by moving or using the tool, with a clear sound and visual that says "this counts".
- **First 3 min:** a first narrowing: the player can rule something out. If the first 3 minutes are setup and briefing, the category's known failure (slow starts) hits.

## Loop tuning
- **Case length:** 10-25 minutes for a single case `[analysis]`. Longer cases need a mid-point where the player can save a partial theory.
- **Evidence count:** 3-5 key pieces per case, with 1-2 red herrings that can be ruled out by a careful player. Fewer and it is a lookup; more and players drown.
- **Pressure cadence:** a pressure event (a hunt, a suspect moving, a clock) every 2-4 minutes keeps the scene alive. Make pressure readable in advance (lights flicker before a hunt).
- **Randomization:** randomize culprit, clue placement or ghost behavior per case so a memorized table is not enough. Hold the rules fixed and vary the instance.

## Depth and mastery
- **The skill chain:** find obvious clues → use each tool correctly → rule out options → read behavior → act under pressure → solve with partial evidence.
- **The depth multiplier:** tools × behaviors. Each tool reveals a different slice; each culprit or ghost type responds differently to each tool. Expert play is choosing which tool to use next.
- **Difficulty by subtraction:** harder modes remove clues or tools, not add hit points. Experts should solve with less.

## Retention engine
- **Case variety:** randomized instances of a fixed rule set give near-endless replay.
- **Difficulty tiers** with visible badges.
- **Weekly challenge cases** with modifiers (no lights, one tool).
- **A case log** that records solves, times and rare outcomes.
- **Chapter cases** for authored mysteries, punctuating the systemic ones.

## Solo-first adaptation
- **Required variant:** solo play, with deduction done in the world (pointing at, walking up to, arranging evidence on a board in the room) instead of a notebook screen.
- Tune the pressure for one player: a solo investigator cannot split up, so hunts must be survivable alone with a readable hiding option.
- Co-op is optional. If it exists, it splits roles (one watches cameras, one walks the scene), but every role must be doable solo.

## Roblox notes
- **Moderate content label** is the ceiling for most investigation horror (Blair and Specter are Moderate `[RBX]`). Show crime through posture, objects and debris, not gore.
- **Small public audience today** (Specter 99, Blair 436, Demonology 3.5K `[RBX]`). This means the format is underserved or that demand is weak. The hook must be clear from a thumbnail.
- **Voice:** Roblox voice chat is not available to all players. A voice-reactive feature must have a non-voice fallback.
- **Mobile:** tools need one-tap use and a clear readout in the world (a needle, a light), not a tiny panel.

## Craft techniques
- **Every clue answers one question.** Write the question each clue answers ("was the shooter left-handed?"). Clues with no question are clutter.
- **Plant red herrings fairly.** A red herring must be disprovable by another clue the player can find. Otherwise it is a trap.
- **Let the player state a theory in the world.** Pin evidence to a board, stand next to a suspect, or place items on the table. The act of arranging makes reasoning visible and satisfying.
- **Confirm without spoiling.** When a clue is found, confirm it counts (a sound, a mark) without saying what it means.
- **Twists through the evidence.** If the case has a larger story, let the twist come from evidence that does not fit (a witness who could not have seen what they describe, a timestamp that contradicts a receipt). Avoid stock twists such as "the investigator was the culprit all along" unless the mechanic makes it specific and earned.

## Pitfalls
- A slow briefing before the scene.
- Deduction moved into a notebook menu or a multiple-choice quiz.
- A fixed evidence table that is solved once and posted online.
- Pressure that kills the player before they can learn anything.
- Clues only readable on a big monitor.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Evidence found by moving and looking | Count clues found in the world versus read from a list or menu. |
| Answer reasoned, no guess | Ask the tester to explain their answer from what they saw. |
| A pressure source | Did a hunt, clock or departing suspect change what the tester did? |
| Committing is a physical act with stakes | How did the tester submit the answer, and what was at risk? |
| Variety per case | Play two cases. Did the culprit, clue placement or behavior change? |
