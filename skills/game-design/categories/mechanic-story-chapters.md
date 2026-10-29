# Mechanic-led story chapters (`mechanic-story-chapters`)

Read the `mechanic-story-chapters` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a story released in chapters, where one unusual verb drives every puzzle and the plot is discovered by using that verb.

---

## What great looks like
- **The mechanic is the meaning.** Undertale lets the player spare every enemy, and the whole story responds to whether they did. The jokes, the characters and the ending only land because of that one verb.
- **The rules change, and that change is the plot.** Inscryption is a card game first. When its rules start to break, the player feels the story through the cards they hold.
- **A strong toy in an empty room.** Before any story exists, the verb (spare an enemy, rewind time, flip gravity) is fun to mess with for five minutes. That is the test that separates a game from a premise.
- **Chapters as events.** Piggy built 14.4B visits `[RBX]` largely on chapter releases. Each chapter was a reason for the whole audience to come back on the same day.

## The hook
- **First 10 s:** the player is in a specific place, in control, with one thing that invites the verb.
- **First 30 s:** the first use of the verb, and it does something no other game does. This is the screenshot and the clip.
- **First 3 min:** the verb used to solve a small problem in two different ways, plus the first story question ("why does this enemy know my name?", "why does the scene not match?"). The player should want both more verb and more answers.

## Loop tuning
- **Puzzle cadence:** a new use, a new constraint or a new combination of the verb every 3-5 minutes. Use the kishotenketsu pattern: introduce safely, develop, twist, conclude.
- **Room size:** small, dense spaces beat big ones. Every room should have a reason to use the verb and something to learn.
- **Chapter length:** 30-60 minutes for a first playthrough `[analysis]`. Long enough to feel substantial, short enough to finish in one or two sessions.
- **Story beats:** a story beat every 5-10 minutes, delivered by what the verb reveals. If more than 2 minutes pass with the player not touching controls, cut.

## Depth and mastery
- **The skill chain:** use the verb → use it on different targets → chain it → use it under pressure → use it to solve a problem in an unexpected way.
- **The depth multiplier:** verb × space. Each space is designed around a twist on the verb (a room where the verb is limited, a room where two uses must happen at once).
- **Multiple solutions:** each puzzle should have at least two routes. Track which routes playtesters use; if 100% use one, the room is a corridor.
- **Mastery ratings:** "no deaths", "pacifist", "under 5 minutes" give experts a reason to replay without new content.

## Retention engine
- **Chapter cadence:** announce the next chapter's date in-game. A visible countdown turns the wait into anticipation.
- **Ratings and boards** per chapter.
- **Secrets** that need the verb used in odd ways (enough that most players find fewer than half on a first playthrough) `[analysis]`.
- **Player-made challenges** using the verb, if the verb supports it.
- Expect D7 to drop between chapters and spike on drops. Measure success by chapter-launch returns, not steady CCU.

## Solo-first adaptation
- The category is natively solo. A verb that only works with two players (or a story that needs another person) breaks it.
- Optional sharing: ghosts of other players' routes, boards, or async notes.

## Roblox notes
- **Building the verb:** prototype it in a grey-box place first and play it for 5 minutes with no story. If it is not fun, change the verb before writing a line of plot.
- **Camera and controls** often change with the verb (switching viewpoints, time or gravity). Test camera transitions at 150 ms latency and on a phone.
- **Small hand-made spaces** keep content cost under control and suit mobile performance.
- **Discovery:** the thumbnail shows the verb happening, not a moody portrait. Titles that state the verb get clicked.

## Craft techniques
- **Plant every twist in chapter 1.** Keep a setup-and-payoff ledger: the plant, why a first-time player walks past it, and the payoff. A twist with no plant feels like a cheat.
- **Discover the twist through the mechanic.** The best twist changes what the verb means (what sparing an enemy really changes, what the cards in your hand really are). If the twist could be told in a cutscene with no change to play, rework it.
- **Ban stock twists.** "The mystery figure was you", "you were dead all along", "it was a simulation", "the helper was the villain" and "your own employer did it" are expected. Never reuse a twist family the studio has already used; check `studio-profile.md`.
- **Characters revealed by action.** People show who they are by what's in their pockets, what they do when unwatched, and how they react to the verb. No one explains the plot to another character.
- **End chapters on a question, not a cliffhanger fight.** A strong question ("whose handwriting is this?") brings players back; a fight cut off mid-swing annoys them.

## Pitfalls
- A gimmick verb that stops changing after the first 15 minutes.
- Cutscenes and text panels carrying the plot.
- A dead game between chapters with nothing to do.
- A twist that is the only content; once spoiled, nothing is left.
- Writing the whole story before the verb is proven fun.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| The verb is fun as a toy | Give the tester an empty room with the verb for 3 minutes. Do they keep playing with it? |
| First use within 10-30 s | Time from spawn to first use of the verb. |
| More than one solution per puzzle | Did testers solve the same room in different ways? |
| Story delivered through the verb | Count story beats delivered by play versus by cutscene or text panel. |
| A twist planted in chapter 1 | Can the reviewer find the plants in chapter 1? Did any tester suspect the twist early? |
| A replay or return layer | Is there a rating, secret set or visible chapter date? |
