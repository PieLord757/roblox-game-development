---
name: de-ai
description: Start here for any Roblox game work. Explains the de-AI standard and which de-AI skill to load (UI/art, story, feel, audit) so the game never looks, reads, or feels AI-generated. Use when building, polishing, or reviewing any game, UI, story, or store page.
---

# De-AI (start here)

## Why this exists
Roblox players, and especially the older 16+ audience these skills assume (the real target audience is in `studio-profile.md` if it exists), spot AI-made work in seconds: a generic sci-fi HUD, a font every AI picks, dialogue that sounds like a chatbot, a thumbnail with that glossy AI-art look. Once they spot it, they assume the whole game is low-effort and leave.

**The failures these skills prevent:**
- A game whose theme was only a setting, with no satisfying moment in its core action, flopped as unfun.
- A first HUD built from the default generated sci-fi kit (a "futuristic" display font, thin glowing bars, "READY" status labels) was called "very AI-generated" on first sight.

The studio's own history, if it keeps one, is in `studio-profile.md`. These skills exist so that it doesn't repeat.

**The standard:** every choice should look like a specific person made it on purpose, for *this* game's world. Generic is the enemy. Defaults are the enemy. "Looks fine" is not the bar. The bar is "a 17-year-old would believe a real studio made this."

## Which skill to load
| You're working on | Load |
|---|---|
| HUD, menus, fonts, colors, icons, 3D art, lighting, VFX look, store icon and thumbnails | `de-ai-ui` |
| Story, characters, dialogue, names, item and ability text, tutorials, store description | `de-ai-story` |
| Controls, movement, combat, timing, sound, effects, camera, mobile controls | `de-ai-feel` |
| End of a milestone, before showing the user, or checking an existing or live game | `de-ai-audit` |

Most work touches more than one. Load every skill that applies.

## Rules for every game
1. **Solo-first.** The game must be fun and complete with nobody else online, because new games start with empty servers. Other players are a bonus. (If `studio-profile.md` sets stricter rules, they win.)
2. **Real references before design.** Before any art or UI work, save 6-10 real reference images to `refs/` in the game folder (the path set in `studio-profile.md`, or `design/<game>/refs/` by default): shipped games, film stills, photos of real objects your UI is based on. Write one line each on what you're taking from it. Designing from references, not from imagination, is the single biggest fix for generic output.
3. **Screenshots are the proof.** Never claim something looks good without a screenshot from a real playtest (`capture_screenshot`, or `screen_capture` in the built-in Studio MCP), including a phone view (`capture_device_matrix`).
4. **Stop for the user at the first UI and art build.** When the HUD, menus, and art direction first exist in-game, send the user a screenshot sheet (SendUserFile) and wait for their OK before building more on top.
5. **Run `de-ai-audit` at the end of every milestone.** A fresh reviewer scores the game, you fix, it re-checks.
6. **Follow `BANNED.md`** (next to this file), plus any bans in `studio-profile.md` if it exists. Never use anything on them.
7. **Process:** one Studio window per game, closed when idle. Never publish without the user's explicit OK. Copy proven loops, never another game's name, characters, art, or audio.

## The banned list
`BANNED.md` is shared by every game. **Anything the user says looks AI-made goes straight onto it**, with a short generic reason (what makes it read as AI-made), never a game name or a date. If the audit reviewer catches the same tell in two different games, add it too. Only the user removes entries. Bans that only make sense for one studio (its own past games, house rules) may live in `studio-profile.md` instead; read it if it exists and treat its bans exactly like `BANNED.md`.

## Tools that help (robloxstudio MCP)
- `capture_screenshot`: viewport proof in playtests.
- `capture_device_matrix`: phone, tablet, and desktop in one go.
- `set_network_profile`: feel under lag.
- `eval_client_runtime`: check what the UI actually shows.
- `get_scene_analysis` and the profilers: performance.
- `solo_playtest` and `multiplayer_playtest`: real sessions.

The built-in Roblox skills `rbx-device-simulator-lua`, `rbx-unit-test`, `rbx-perf-profiling` and `rbx-docs-search` also help.
