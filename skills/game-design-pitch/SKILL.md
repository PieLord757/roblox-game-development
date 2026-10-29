---
name: game-design-pitch
description: Generates 3-5 new game ideas from categories that fit the studio's rules, each with a unique verb, premise, 3-act arc with a twist found through the mechanic, a concrete 30-second moment, why it works solo, how it keeps going and hours to build. Checks every idea against existing games and pitches and drops collisions. Use when asked for new game ideas or a new round of pitches.
---

# Game design pitch

Load `game-design` first if you have not this session.

## Inputs
1. `studio-profile.md` at the project root if it exists. Read it in full: the audience, the hard rules, the **existing games and pitches** (main mechanic, twist, setting) and any **taken twist families**. If it does not exist, ask the user for the hard rules and the existing games before pitching.
2. `../game-design/CATEGORIES.md` and the deep files of the categories you draw from.
3. Any brief from the user (a theme, a genre, a reference game, a time budget).

## Step 1: choose categories that are allowed
- Use only categories labeled **Yes** or **Variant** in `CATEGORIES.md`. For a Variant, the pitch must be that variant.
- Drop any category whose flags break a hard rule in the profile (for example `open-world` or `air-combat` if banned).
- **Never pitch a category labeled No**, even as a "twist on" it.
- Prefer categories with strong evidence (many sourced exemplars, good retention) over thin ones, unless the user asked for something specific.

## Step 2: generate wide, then cut hard
Generate 10-15 raw ideas privately before choosing. If the profile lists extra pitch rules or a studio fun filter, every idea must pass those too. Good sources:
- **A proven loop plus one new verb.** Take a category's must-haves and change one pillar with a verb no game in that category asks you to do. Megabonk changed the *space* of a horde survivor (3D, jumping) and nothing else; Balatro removed the enemy from a deckbuilder and made the score the opponent.
- **A famous single level stretched into a game.** A mechanic players remember from one level of a bigger game, built out with a full skill chain.
- **A mundane action given stakes.** Papers, Please made document checking tense with mounting rules and a family to feed.
- **An unscripted moment from a co-op hit, made solo.** Quota pressure, rule-based monsters, a fragile carry: moments that came from friends, rebuilt so one player can have them.

For each raw idea, write the verb in one line and run the fun test from `game-design`. Drop any idea that cannot answer all seven questions.

## Step 3: collision check (mandatory, before writing any idea up)
For every surviving idea, compare against **every** row in the profile's existing games and pitches, and against the other ideas in this batch:
| Check | Collision if |
|---|---|
| Main mechanic | the core verb does the same job, even under a new name (swinging on a grapple and swinging on a vine are the same job: travel by swinging) |
| Twist | the reveal is in the same family as an existing twist (see below), even in a new setting |
| Setting | the same place type, era and social situation (a ski lodge and a mountain cabin in a blizzard are close; two 1920s speakeasies in different cities are close) |

**Drop any idea that collides on any one of the three.** Do not "fix" a collision by renaming. Write the dropped ideas and the reason in a short "cut" list at the end of the file, so the user can see the filter worked.

### Banned twist families
These are stock reveals. Never use them, and never reuse any family already listed in the profile:
- **"It was you all along"**: the mystery figure, the killer, the ghost or the person in the photo is the player.
- **"You are the copy, clone, reflection or AI"** and its sibling "the copies are real people".
- **"Your own employer, agency or department is the villain."**
- **"The person you are helping is the culprit, and the threat was the rescue."**
- **"It was all a simulation, a dream, a coma or a test."**
- **"Everyone was dead the whole time."**

No twist family may appear twice **within one batch**, either.

### What a good twist does instead
- It is **discovered through the mechanic.** The player finds it by using the verb (Inscryption's card game starts breaking its own rules; Undertale's characters remember that you spared someone), not from a cutscene.
- It is **planted in Act 1** in plain sight, so a sharp player can call it early and everyone else feels it was fair.
- It **changes how the verb is used** in Act 3, not just what the story means.
- It **raises a choice**, rather than only explaining the past.

## Step 4: write up 3-5 ideas, properly
Present **3-5 ideas at most**, or fewer if the profile sets a lower limit. Lead with the experience, not the numbers. No numbers-first menus, no score tables at the top. Each idea uses this skeleton, in prose and short bullets:

```
## <Name> (<what you are, in four words>)

**The verb:** <what the player physically does, in one or two sentences. This is the thing nobody else asks them to do.>

**The premise:** <who you are, where, and what you want, in 2-3 sentences.>

**The arc:**
1. Act 1: <learning the verb and the place; the twist is planted here>
2. Act 2: <the verb's rules deepen; something stops adding up>
3. Act 3, the twist: <what the player discovers through the verb, and the choice it leaves them>

**30 seconds of play:** <one concrete moment, second by second, with real objects and timings. A reader should be able to picture the screen.>

**Why it works solo:** <why one person is the right number of players for this verb>

**How it keeps going:** <the return engine from the brief skill's list, plus the depth multiplier>

**Category:** <main slug> (+ <secondary slug>), and which must-have the twist changes

**Build:** <hours for chapter 1 or the first playable, and the one hardest technical part>

**Evidence:** <the closest proven games with numbers and source tags, and an honest note where there is no precedent>
```

Craft notes for the write-up:
- **The 30-second moment is the pitch.** Use specific nouns and timings ("the sentry's lamp swings left every 6 seconds, so you cross the courtyard on the fourth swing"). If the moment could be from any game, the idea is not specific yet.
- **Name the verb as an action**, not a system ("you throw your voice", not "a voice-projection system").
- **One idea, one twist family, one setting.** Vary settings and eras across the batch.
- **Honest evidence beats hype.** If nothing like it has succeeded, say so, and say what the closest proven loop is.

## Step 5: pick
End with a short recommendation: which idea you would build first and why, in two or three sentences (clearest verb, cleanest build, strongest return engine).

## Output
Save to the profile's pitch path, or `design/pitches/<YYYY-MM-DD>-<topic>.md`. The file starts with a **5-line plain-English summary** for the user (how many ideas, the one-line verb of each, your pick), then the ideas, then the cut list.

**Present it in chat.** After saving, give the user a clear overview directly in chat: each idea's name, verb, and 30-second moment in two or three lines, your pick and why, and how many ideas the collision check dropped. The file is the detail; the chat overview is what the user reads.

When the user picks an idea, run `game-design-brief` on it before building, and add it to the profile's existing games and pitches.

## Common mistakes
- Pitching a theme instead of a verb ("a haunted lighthouse game").
- Reusing a twist family because the setting is new.
- Five ideas from the same category, or the same tone and era.
- A 30-second moment that is a cutscene or a menu.
- A "how it keeps going" that is only "more chapters".
- Leading with tables of CCU numbers before the reader knows what the game is.
