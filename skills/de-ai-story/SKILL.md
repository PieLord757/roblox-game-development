---
name: de-ai-story
description: Process and rules for story, characters, dialogue, names, item text, tutorials, and store descriptions in Roblox games so the writing never reads as AI-generated. Use before writing or editing any in-game text.
---

# De-AI: story and writing

## Why
AI writing has a recognizable voice: smooth, vague, over-explained, every character equally articulate, and big words like "testament" and "tapestry". Older players (16+) notice it immediately, and it kills a story game. Story games live or die on writing that feels sharp and human.

## Step 1: the story bible (`STORY.md`), before any scene is built
**For each character:**
- What they **want** tonight.
- Their **secret**.
- What they're **afraid of**.
- **How they talk:**
  - sentence length
  - a verbal habit
  - words only they would use
  - what they never say
- **One specific detail** that makes them real, like "re-ties his left shoe whenever he lies" or "keeps her late father's library card in her wallet".

**For the twist:**
- List every clue planted early, and where and when the player can find it.
- List where each clue pays off.
- Test it: could a sharp player guess it on a replay? It must be fair.

**For each scene or loop:** what the player learns, and how they learn it *by playing*.

## Step 2: writing rules
- **Specific beats vague.** Not "a mysterious past", but "a pawn ticket for a wedding ring, dated last Tuesday."
- **Short lines.** Most dialogue is under 12 words. Real people interrupt, dodge, trail off, answer a different question, and don't say what they mean.
- **Subtext over text.** Characters almost never state their feelings or the plot directly. The player puts it together.
- **Show it through play.** Overheard conversations, objects, documents and timing carry the story. No speeches that explain the plot, and no villain monologues.
- **Distinct voices.** Cover the names on a page of dialogue: you should still know who's talking.
- **Earn emotion.** Don't tell the player something is sad or shocking. Set it up, then let the moment land.
- **No em dashes (—) at all.** Use a comma, period, colon, or parentheses. This applies to every player-facing word.
- **No neat lesson at the end.** Leave something unresolved or uncomfortable.
- **Names** fit the setting and era, and are a little unusual but believable. Check `../de-ai/BANNED.md`, plus any bans in `studio-profile.md` if it exists.
- **UI and tutorial text** is written in the world's voice, never documentation voice. Not "Press E to interact", but a note pinned to a mountain hut door: "Latch sticks. Lift, then pull. E."

## Step 3: check it
- Read every line out loud. If it sounds like a movie trailer, a chatbot, or a press release, rewrite it.
- Search all game text for the banned words and patterns in `BANNED.md` (and any bans in `studio-profile.md`), and for the em dash character `—` (must be zero matches).
- Ask: is there one line in this scene a player would quote to a friend? If not, sharpen it.
- **Content:** a 16+ tone (or the audience set in `studio-profile.md`) within Roblox's content rules. Tension, stakes, crime and danger are fine. No gore, no slurs.

## Output
1. **`STORY.md`** in the game folder: the bible from Step 1, kept current as scenes are built.
2. **A clear overview in chat.** The file holds the detail; the chat overview is what the user reads. Give the premise and the twist in two plain sentences, one line per main character (what they want and their best line), how the twist is clued, and anything still undecided that the user should weigh in on.
