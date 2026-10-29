---
name: character-design
description: "Start here for any character, NPC, enemy, monster, or player-avatar work in a Roblox game. Gives the rules and the 13-step process for designing characters that are memorable, readable on a phone, and distinct from the studio's other games, and says which character-design sub-skill to load (visual, story, roblox, audit). Use before designing, building, re-skinning, or reviewing any character, and before deciding whether a game uses the player's own avatar."
---

# Character design (start here)

## Why characters matter
Players remember characters long after they forget levels. A character is how a game gets drawn in fan art, clipped, turned into a meme, and recognised in a thumbnail on the Discover page. On Roblox this matters even more, because:
- Most games share the same rig and the same default avatar proportions, so a character that looks like "a Roblox avatar in a different shirt" disappears into a million other games.
- Players are on phones. A character is often 20 to 50 points tall on screen. Detail does not survive that; silhouette, colour mass, light and motion do.
- Players aged 16 and up have seen every popular free model and every generic AI-generated "scary monster". A borrowed or averaged character reads as low effort in seconds, and they leave.

**The standard:** every character should look and act like a specific person designed it on purpose, for this game's world and this game's camera. "Looks fine" is not the bar.

## What this skill gives (and what it never gives)
- It gives **rules and a process**. It never gives a fixed look, a house style, or a character to copy. Every example in these skills illustrates a principle. Copying an example is a failure; if an example leans on "one signature prop", the next game should probably reach for a different lever entirely.
- **Per game, it produces:**
  1. `CHARACTERS.md` next to the game's `ART-DIRECTION.md` (copy `CHARACTERS-TEMPLATE.md` from this folder). It holds the avatar-vs-custom decision with its reason, and five required fields per character: **role, silhouette hook, shape language, palette colours (from that game's palette), one-line personality.**
  2. A **screenshot sheet** made in Studio: the silhouette lineup, the colour lineup in real lighting, and in-game phone screenshots. **The user approves the sheet before anything more is built on top of the characters.**
  3. A **chat overview** for the user (see "Output" below). The file is the detail; the chat overview is what the user actually reads.

## Which sub-skill to load
| You are working on | Load |
|---|---|
| Silhouette, shape, proportion, read order, colour and value, phone readability, AI-look tells, the runnable Studio checks (silhouette, distance, grayscale, lineup) | `character-design-visual` |
| Want, need, false belief, wound; voice; reactive lines; secrets revealed in pieces; characters told through what they left behind; monsters as cue, rule and counter | `character-design-story` (it extends `de-ai-story`; load both) |
| Player avatar vs custom, R6 / R15 / custom rig / no rig, HumanoidDescription, layered clothing, triangle and texture budgets, the MCP generation tools and their limits, Avatar Auto Setup, Creator Store risks, animation as identity | `character-design-roblox` |
| Reviewing a cast: scoring against the rules and the cross-game distinctness check | `character-design-audit` (run by a fresh reviewer subagent) |

Most character work touches all three build skills. Load every one that applies. Also load `de-ai-ui` (it owns the palette and `ART-DIRECTION.md`) and `de-ai-story` (it owns `STORY.md`).

## Rule index
Rules keep the same IDs in every file so the audit can cite them.

| IDs | Area | Lives in |
|---|---|---|
| V1 to V10 | Visual: silhouette, distance, grayscale, lineup, primary trait, shape intent, saturation budget, costume why-test, anti-generic list, palette source | `character-design-visual` |
| N1 to N6 | Narrative: need/false belief/wound, three voice drafts, secret trickle, reactive lines, monster cue-rule-counter, left-behind characterisation | `character-design-story` |
| R1 to R7 | Roblox technical: rig choice, triangle budget, textures, custom animation, avatar decision, Creator Store, Highlight use | `character-design-roblox` |
| G1 to G6 | AI generation: triangle cap, world-specific prompts, duplicate before texturing, never ship raw output, block out first, rigging path | `character-design-roblox` |
| D1 to D6 | Studio distinctness (below) | this file |
| F1 to F3 | The only three fails (below) | this file |

## Studio distinctness: notes, not fails
Overlap between a studio's games is normal. Two games can both have a tall thin villain or both use amber light. **Overlap is logged as a note for the user, never as a failure.**

A character **fails** only when it is basically the same as a character in another of the studio's games. That means exactly one of:
- **F1** the same base model, left unedited
- **F2** the same model plus the same palette plus the same proportions
- **F3** an unedited free Creator Store character

**Distinctness rules:**
- **D1** Write `CHARACTERS.md`, including the studio fingerprint block for majors, before building any character.
- **D2** Run the distinctness check (in `character-design-audit`) against every other game. Notes go to the user. Only F1 to F3 block a character.
- **D3 Avoid drifting into a house style.** When a studio builds many games, each one carefully on its own, the palettes quietly converge. The usual drift is a role formula: a near-black "ink", a warm cream "paper", brass or gold, oxblood, and one saturated red (hue about 20 to 45 degrees) as "danger", often with a sodium or amber light. Each game looks fine; together they read as one studio template, and players who play two of your games feel it. Treat these as **overused combinations to be noted, not banned**:
  - the near-black, cream, brass, oxblood and red role formula
  - saturated red at hue 20 to 45 as the danger signal
  - brass or gold as the signature character material

  When a game uses one, `CHARACTERS.md` says why it suits this world. Update this list from the palette script's family table as games ship.
- **D4** A fresh reviewer agent runs the unlabelled silhouette lineup. The build agent never grades its own cast.
- **D5** Existing games are audited against this check at each game's next stopping point (the end of the current milestone, or before the next publish), not retroactively all at once.
- **D6 Choose the palette family on purpose.** Before a game's palette is picked, read the other games' palettes and choose a different colour family deliberately (process step 3).

## How the studio's other games are found
These skills are generic. They never hard-code game names. To find the other games:
1. If `studio-profile.md` exists at the project root, read it first. It may list the studio's games, their folders, and anything already decided about house style. Do not edit it from this skill.
2. Scan `design/*/CHARACTERS.md` and `design/*/ART-DIRECTION.md`. Every folder with either file is a game for the distinctness check. If the studio keeps games somewhere else, `studio-profile.md` should say where; use that path instead.

## The process (in order)
Steps are short on purpose. The craft for each lives in the sub-skill named.

1. **Read** the game's `ART-DIRECTION.md` (palette, materials, lighting) and `STORY.md`, plus `studio-profile.md` and every other game's `CHARACTERS.md` fingerprint. List which D3 overused combinations already exist so you know what will be flagged.
2. **Define the cast's job.** What must the player tell apart, from how far, and how fast? For each character write the **1 second, 3 second and 10 second reads**: what the player must know at each (usually: threat or friend, then role, then personality). (`character-design-visual`)
3. **Pick the palette family deliberately (D6).** Before choosing colours, run
   `python3 -I .claude/skills/character-design/palette_collisions.py design`
   (`design` is the folder that holds every game folder; use the path from `studio-profile.md` if it sets another) and read the colour-family table. Any family marked "house style" is where the studio is drifting. Choose this game's dominant and accent families from what the world's own references support **and** what the other games are not already using. Write one line in `CHARACTERS.md`: "Other games lean on ___; this game uses ___ because ___."
   - **If the game has no locked palette yet:** do this before `ART-DIRECTION.md`'s palette is written, and hand the chosen families to whoever writes it (palettes belong to `de-ai-ui`).
   - **If the palette is already locked:** do not reopen it. Run the script with `--target <game>`, record the overlaps as notes, and spend your freedom where characters still have it: which palette colours characters own, the saturation budget, the threat signal, and materials.
   - A reused family is still allowed. It is a note with a written reason, never a fail.
4. **Decide avatar vs custom** using the decision rules in `character-design-roblox`, and write the choice and the reason at the top of `CHARACTERS.md`. Include bot-fill appearance if the game fills empty slots with bots for solo play.
5. **Write the fingerprint** (majors and monsters only) and the five required fields for every character. Record where the fingerprint overlaps other games and why that suits this world.
6. **Narrative pass.** Need, false belief and wound on top of `de-ai-story`'s fields; voice drafts; the secret trickle; reactive lines; monster cue, rule and counter. (`character-design-story`)
7. **Thumbnail silhouettes.** Block out 3 to 5 per major character from primitives or `generate_procedural_model`, run V1 and V4, keep the strongest, push it further. (`character-design-visual`)
8. **Lock shape, proportion and primary trait** in writing (V5, V6).
9. **Colour.** Apply the palette with a saturation budget (V7). Run V3 in the real environment.
10. **Build the model.** Hand-made parts, a generated mesh from world-specific prompts (G1 to G6), or a heavily modified store asset (R6), within budget (R2, R3). (`character-design-roblox`)
11. **Animate.** Custom idle, locomotion and one signature action, plus a sound signature (R4).
12. **Verify in game.** V2 at phone size, V3 in real lighting, a multiplayer playtest for animation replication. Then run `character-design-audit` with a fresh reviewer.
13. **Show the user** the screenshot sheet and the chat overview, and wait for approval before building more on top.

Keep it in hours, not days. Minor NPCs need only the five required fields and one visible detail; the fingerprint and the deeper fields are for majors and monsters.

## Output
1. **`design/<game>/CHARACTERS.md`**, from `CHARACTERS-TEMPLATE.md`.
2. **The screenshot sheet** in `design/<game>/screenshots/characters/<date>/`: the silhouette lineup (V4), the colour lineup in real lighting, the grayscale shot (V3), and phone-size in-game shots at the farthest reaction distance (V2). Combine them into one image or a short ordered set and send it to the user (SendUserFile or the equivalent).
3. **A chat overview, as an explicit step.** In the chat message that carries the screenshot sheet, give the user a plain overview they can read in under a minute:
   - the avatar-vs-custom decision and its reason, in one sentence
   - one line per character: name, role, and its silhouette hook (what you will recognise it by)
   - the palette choice: which colour family this game owns and how it differs from the other games
   - distinctness: any fails (F1 to F3) and the two or three most important notes, in plain words
   - what you need from the user: "approve the sheet, or tell me which character to change"

   Do not paste the whole `CHARACTERS.md` into chat, and do not make the user open the file to understand the cast. The file is the detail; the overview is what the user reads.
4. **Wait for approval** before building more on top. Log the approval (or the requested changes) in the game's `progress.md`.

## Tools
- Studio inspection and edits: `execute_luau`, `inspect_instance`, `search_game_tree` (Roblox_Studio server), or `execute_luau`, `search_objects`, `get_instance_properties` (robloxstudio server).
- Screenshots: `screen_capture` (Roblox_Studio) in edit mode; `capture_screenshot` and `capture_device_matrix` (robloxstudio) during playtests.
- Generation: `generate_procedural_model`, `generate_mesh`, `generate_texture`, `generate_material`, `segment_mesh` (Roblox_Studio); `generate_model` (robloxstudio). Limits are in `character-design-roblox`.
- Palette evidence: `palette_collisions.py` in this folder (stdlib Python; run with `python3 -I`; `--help` for options).

## Sources
The rules rest on these public sources. Primary sources are a studio's own paper, talk, post or docs.
- Mitchell, Francke, Eng, *Illustrative Rendering in Team Fortress 2* (NPAR 2007): the flat-black silhouette test, read order, cool shadows, rim light. https://www.advances.realtimerendering.com/s2007/Mitchell-IllustrativeRenderingInTF2(Siggraph07%20Course%20Notes).pdf
- Game Developer, "How Valve makes art to enhance gameplay" (TF2 and Left 4 Dead): https://www.gamedeveloper.com/art/in-depth-how-valve-makes-art-to-enhance-gameplay
- Riot, "Clarity in League" and "Ask Riot: Let's Talk Clarity": one primary trait, facing direction, clarity on every map. https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/
- GDC Vault, *The Art of Overwatch* (2017), and Blizzard's Overwatch 2 art recap: everything in the design says something; redesigns keep palette, silhouette and motion. https://gdcvault.com/play/1024268/The-Art-of-Overwatch-Evolving
- Walt Disney Family Museum, *Shape Language*: https://waltdisney.org/sites/default/files/2020-04/T&T_ShapeLang_v9.pdf
- K.M. Weiland on want, need, the lie and the ghost: https://www.helpingwritersbecomeauthors.com/character-arcs-3/
- Roblox docs: character specifications https://create.roblox.com/docs/art/characters/specifications ; character appearance and HumanoidDescription https://create.roblox.com/docs/characters/appearance ; modeling specifications https://create.roblox.com/docs/art/modeling/specifications ; texture specifications https://create.roblox.com/docs/art/modeling/texture-specifications ; Avatar Auto Setup https://create.roblox.com/docs/avatar-setup/auto-setup-requirements ; animations https://create.roblox.com/docs/animation/using ; Creator Store https://create.roblox.com/docs/production/publishing/creator-store
- Secondary: 80.lv on TF2 vs Overwatch readability; coverage of Hades (Supergiant), Disco Elysium, Outer Wilds, Undertale; public guides to Doors, Pressure, Piggy, Dandy's World, Forsaken, The Strongest Battlegrounds, Deepwoken and Blade Ball. These are pattern analysis, not developer intent.
