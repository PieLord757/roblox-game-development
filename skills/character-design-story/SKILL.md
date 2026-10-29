---
name: character-design-story
description: "How to write Roblox game characters players remember: need, false belief and wound on top of de-ai-story's bible, voice drafts, reactive lines keyed to player state, secrets revealed in small pieces, characters told through what they left behind, and monsters designed as cue, rule and counter. Use when writing or revising any character, NPC, villain, or monster's story, lines, or behaviour. Load de-ai-story alongside it."
---

# Character design: story

Load `character-design` first for the process and the rule index. This skill owns rules **N1 to N6**.

**This extends `de-ai-story`; it does not replace it.** `de-ai-story` Step 1 already requires, for each character in `STORY.md`: what they want, their secret, what they fear, how they talk, and one specific detail. Its writing rules (short lines, subtext, distinct voices, no em dashes, the blind-dialogue test, the banned list) apply to every line here. Do those first. This skill adds the layer underneath that makes a character feel like a person rather than a function, and the techniques that make them memorable inside a game loop.

## 1. The layer under the want (N1)
From K.M. Weiland's character-arc framework:
- **Want:** what they chase (already in `de-ai-story`). It is often a bad goal.
- **False belief:** the lie about themselves or the world that makes them want it.
- **Need:** the truth they would have to accept to be OK.
- **Wound:** the past event that taught them the false belief.

| Character | Fields |
|---|---|
| **Major** (named, speaks a lot, drives the story, or a recurring villain) | All four, plus the `de-ai-story` fields |
| **Minor** (shopkeeper, guard, quest-giver) | Want plus one detail, and the detail is **visible in game** |
| **Monster** | Cue, rule and counter (section 6), plus a want if it has any mind at all |

**The false belief is never said out loud.** It shows in what the character does and how they talk around it. If a line names the false belief ("I've always believed I'm not good enough"), cut it.

### Weak vs strong
- **Weak:** "Marta is a grumpy shopkeeper with a mysterious past." (An adjective and a vague hint. Nothing to play.)
- **Strong:** Want: sell the shop before winter. False belief: the town only tolerated her because of her late brother. Wound: nobody came to his funeral but her. Need: people come in for her, not the stock. In play, she undercharges regulars and refuses to let them thank her. She never mentions the brother; his name is still painted on the sign, half scraped off.

## 2. How to write a memorable NPC (the craft)
1. **Start with a behaviour or an object, not an adjective.** "Re-ties his left shoe whenever he lies" or "keeps her dead dog's lead clipped to her belt", not "nervous" or "sentimental".
2. **Make the detail visible in the game** (N1). A custom idle, one hand prop, one repeated line. If it lives only in the doc, it doesn't exist for the player. In Roblox, one custom idle or one hand prop per NPC is cheap and very effective.
3. **Give them a life outside the player's story.** A hobby, a feud with another NPC, an errand they're always in the middle of. The player should feel they walked into this person's day.
4. **Let them want something from the player** that isn't the quest. Approval, silence, a favour, to be left alone.
5. **Give them one quotable line.** Read the character's lines aloud. If none would be repeated to a friend, sharpen one until it would.
6. **Cut anything borrowed.** If a detail reads like a famous character's, cut it, even if you love it. Small solo developers do this too (Toriel's horns were cut for resembling another game's creature).

## 3. Voice (N2)
- **Draft three voices for every major character and keep one.** Write the same short exchange three ways: different sentence length, different verbal habit, different thing they refuse to say. The first draft is usually the average voice. Pick the one that surprises you and still fits the wound.
- Run `de-ai-story`'s blind-dialogue test: cover the names on a page of dialogue. You should still know who's talking.
- **Voice shows the false belief.** Someone who believes they're only useful deflects every compliment into a task. Someone who believes nobody listens over-explains, then cuts themselves off.

| Weak | Strong (same beat, three drafts, one kept) |
|---|---|
| "I'm worried about the storm. We should get inside soon. It's very dangerous out here." | A: "Wind's turned." B: "You hear that? No? Good. Keep walking." C: "My dad used to count the seconds. I stopped counting." (Keep C for the character whose wound is her father; keep A for the one who never says more than he must.) |

## 4. Reactive lines (N4)
Lines that comment on what **this player** just did make a character feel alive, and they move the story forward even through failure (the pattern Supergiant used in Hades: characters comment on the weapon used, how you died, who you met). For a Roblox loop game this is the strongest cheap technique available.

**Every major NPC gets at least one reactive line pool** keyed to player state:
- last death cause, or how close the last run got
- item or tool held right now
- time taken, streak, or number of attempts
- who or what the player met last
- a first: first visit, first win, first time returning after a long break

**How to build it:**
- Store a few state fields per player (last death cause, held item, run count). Pick lines by matching the most specific state first, then fall back to general lines.
- Write 3 to 6 lines per state, so repeats are rare. Never repeat the same line twice in a row.
- Keep each line under 12 words. Most should be in character first and informative second.
- **Weak:** "You died. Try again!" **Strong:** "The stairs again? Third time. They don't move, you know."

## 5. Secrets revealed in pieces (N3)
A secret is stronger as a **trickle of small reveals** than as one twist (Disco Elysium reveals its partner character's traits gradually through many optional moments).
- Each major secret gets **at least three small reveals** spread across the game: an object, an overheard line, a reaction that doesn't fit, a document, a behaviour change.
- No single reveal gives it away. Together, a sharp player can put it together before the game says it.
- List each reveal in `STORY.md` with where and when the player can find it (this ties into `de-ai-story`'s twist clue list).
- **Weak:** a final cutscene where the villain explains everything. **Strong:** the station cook's recipe binder has one page torn out; later her coat has a second name stitched inside the collar; later still she flinches when the player says that name. The player says it before the game does.

## 6. Characters told through what they left behind (N6)
Absent, missing and dead characters can be the most memorable in the game, and they cost no model at all. The most important characters in Outer Wilds are long dead and characterised entirely through what they wrote.
- Use notes, recordings, graffiti, a locker's contents, a room's arrangement, a half-finished job, a mug with a chip in it.
- **Each object says one thing about the person**, and the set of objects contradicts itself a little, the way real people do.
- Write it in their voice (section 3 applies). A note sounds like the person, not like exposition.
- Let objects answer questions the player is already asking. Put them on the path the player walks anyway.
- **Weak:** a journal page reading "Day 12. The creature grows stronger. I fear for my life." **Strong:** a grocery list with "batteries (big ones)" underlined three times, "milk" crossed out, and a tally of 14 marks on the back.

## 7. Monsters are characters: cue, rule, counter (N5)
For a monster, the "character" is a **rule the player learns**. Doors shows this clearly: each entity owns one sense and one verb, and no two share both a cue and a counter. Most are visually simple (a face, a cloud, a light); the memorable part is the rule plus the sound.

Every monster has:
- **Cue:** how the player knows it is coming (a sound, a light change, a smell-proxy like particles, a UI or camera effect, a change in other NPCs).
- **Rule:** what it does (hunts by sound, only moves when unseen, follows light, punishes hiding).
- **Counter:** the verb that beats it (hide, look, look away, stay still, run, turn off your light, reverse direction).

**Within a game, no two monsters share both a cue sense and a counter.** Write the cue, rule and counter in `CHARACTERS.md`. If you can't explain the rule in one sentence, the player won't learn it.

**How to design one:**
1. Start from the counter verb you want the player to perform. A verb that's fun to do under pressure (hold your breath, snap a light off, freeze mid-step) makes a better monster than a scary look.
2. Pick a cue in a sense the game isn't already using for another monster.
3. Design the body last, around the cue. If the cue is light, the body can be mostly darkness around a lamp.
4. Give it a want if it has a mind. A monster that wants something (to be seen, to be fed, to finish a task it died doing) gives players something to talk about.

| Weak | Strong |
|---|---|
| "A fast monster that chases you and kills you if it catches you." | Cue: every radio in the level tunes to the same station a few seconds before it arrives. Rule: it follows the loudest sound. Counter: switch a radio on in another room and hide. Want: it is looking for the song that was playing when it died. |

## Output
- Additions to `STORY.md` (the false belief, need and wound for majors; the reveal list for each secret; reactive line pools) and the narrative fields in `CHARACTERS.md` (one-line personality, want, cue/rule/counter for monsters).
- **A chat overview for the user** alongside the character screenshot sheet: for each major character, one line on who they are and what they want, plus their best line; for each monster, the cue, rule and counter in one sentence. The files are the detail; the overview is what the user reads.
