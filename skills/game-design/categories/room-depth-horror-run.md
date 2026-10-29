# Room-depth horror run (`room-depth-horror-run`)

Read the `room-depth-horror-run` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** open the next room, hear something, apply the one rule that beats it, and push the number on the door higher.

---

## What great looks like
- **The number is the progress bar.** DOORS (31K / 100K, 8.0B visits, 93.0% `[RBX]`) counts doors from 1 to 100. Nobody needs to be told what progress means. "I got to 72" is a sentence players say to each other.
- **One tell, one rule.** In DOORS, a light flicker and a rushing sound mean hide in a closet now. Another entity means look away. Another means look at it. Each threat is a small rule the player learns once and then performs under stress. Fear turns into competence, which is why players come back instead of being scared off.
- **The first encounter is a lesson in disguise.** The first entity appears early, telegraphs loudly, and is survivable on a first try if the player reacts at all. The second encounter with the same entity is quieter.
- **Art direction carries tone.** Pressure (529 off-peak, Moderate label `[RBX]`) used an industrial deep-sea facility and won an older-leaning audience on mood. Its smaller audience shrank between content drops, which is the genre's main weakness.

## The hook
- **First 10 s:** the player is at door 1 with the counter visible and a door to open.
- **First 60 s:** several rooms opened, a light puzzle or item found, and something wrong noticed (a flicker, a distant sound).
- **First 3 min:** the first entity encounter, survived or not, with its tell clearly heard. If the player dies, the death screen names the entity and hints at the rule.

## Loop tuning
- **Room pacing:** 10-30 s per normal room. Every 5-10 rooms, a special room (a puzzle, a shop, a safe room, a set piece).
- **Entity introduction:** one new entity every 10-20 rooms early, then mix known entities. Never introduce two new entities in the same room.
- **Tell timing:** the tell should arrive 2-5 s before the threat, enough to react on a phone. Shorten it slightly in hard modes rather than removing it.
- **Run length:** 20-40 min per floor, with a checkpoint or a halfway save. A run that dies at room 90 with no checkpoint loses the player.
- **Quiet stretches:** 30-60 s of nothing between scares. Tension needs release, or the player stops being scared and starts being tired.
- **Tune in big steps.** If an entity kills almost nobody, halve its tell time; if it kills almost everybody, double it, then settle.

## Depth and mastery
- **The skill chain:** notice tells → apply rules → combine rules when two entities overlap → manage items (light, lockpicks) → route efficiently through rooms → run modifiers and hard mode.
- **The depth multiplier:** entities × room layouts. The same entity in a narrow corridor and in a library plays differently. Procedural room order makes the combinations fresh.
- **Overlap moments:** late runs should sometimes stack two entities whose rules conflict (hide versus keep moving). That is where mastery shows.
- **Modifiers:** opt-in rules (faster entities, no light, fewer hiding spots) for veterans.

## Retention engine
Pick at least two:
- **Depth record:** best door number reached, shown in the lobby.
- **Entity mastery:** an achievement or journal for surviving each entity a number of times.
- **Modifiers and hard mode** with their own records.
- **Floor drops:** new floors with new entities, planned before launch so the gap between drops is known.

## Solo-first adaptation
The genre is fully playable solo (DOORS is). Co-op adds revives and shared fear. Tune entity rules so a solo player has the same chance as a group; never require two players to beat a mechanic.

## Roblox notes
- **Procedural rooms:** build rooms as modules with an entry and exit, and assemble them at run time. 30-50 room modules per floor is a reasonable start.
- **Audio is the main channel:** use 3D positional sounds for tells. Test with phone speakers, where low bass disappears; give each tell a mid-range component.
- **Lighting:** darkness is cheap to render. Use a small player light and strong contrast; keep the rest of the scene simple for low-end phones.
- **Maturity label:** jump scares and mild fear fit the mid labels. Older players respond to grounded settings and dread, not gore.
- **Monetization:** revives, cosmetic lights, boosts for currency. A revive must never make a solo run trivially safe.

## Craft techniques
- **The tell checklist:** each entity has one sound, one visual and one rule. Write them in a table before building. If two entities share a sound, players will apply the wrong rule and blame the game.
- **The death card:** on death, show the entity's name and a one-line hint written in the setting's voice. It turns death into learning.
- **Fake-outs, sparingly:** an occasional flicker with no entity keeps players alert, but too many teach them to ignore tells.
- **Set-piece rooms:** one hand-built moment per 20-30 rooms that the procedural rooms cannot produce (a chase down a long hall, a flooded room).

## Pitfalls
- Jump scares with no counterplay. Fear without a rule is just a loss.
- Runs too long for a phone session.
- Content burnout between floor drops (Grace and Pressure both contracted between updates).
- Entities whose tells overlap.
- A first entity that kills on the first try with no hint.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Visible depth counter | Is the number always on screen or on every door? Did the tester mention their number? |
| One tell and one rule per entity | Ask the tester after a death: what was it and what should you have done? A correct answer scores 2. |
| Procedural room order | Play two runs. Were the first 10 rooms different? |
| First entity in about 2 min | Time to first entity from spawn. |
| Checkpoints or floors fit 20-40 min | Time a full floor; note the nearest checkpoint to any death. |
| Modifiers or hard mode | Is an opt-in harder mode visible to a returning player? |
