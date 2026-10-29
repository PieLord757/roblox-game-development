---
name: de-ai-audit
description: Full audit of a Roblox game for anything that looks, reads, or feels AI-generated. A fresh reviewer gathers evidence, scores eight areas, and writes a ranked fix plan; the build thread fixes and re-audits. Use at the end of every milestone, before showing the user, or to check an existing or live game.
---

# De-AI audit

## Why a separate reviewer
The thread that built the game can't see its own work fresh. A build thread that audits its own game will score it generously (one gave itself 15/18 and called it done while players still saw a generic game). The audit is therefore run by a **fresh reviewer subagent** that:
- didn't build the game
- never edits it
- whose only job is to find what looks, reads or feels AI-made

## Step 1: gather evidence (the build thread does this)
Save everything to `design/<game>/audit/<YYYY-MM-DD>/de-ai/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). Capture it during a real playtest (`solo_playtest`), not in edit mode:
- **Screenshots:**
  - every screen: menus, HUD, results, settings, shop
  - key gameplay moments, including the game's best moment
  - `capture_device_matrix` for phone, tablet and desktop on the main screens
- **Feel under lag:** play the core loop at 150 ms and 300 ms latency (`set_network_profile`), and write down what felt wrong.
- **All text:** every piece of in-game text exported to `text.md`, including dialogue, UI labels, item names, tutorials and the store description.
- **Store page:** the icon, the thumbnails and the description.
- **Sound:** a list of every player action and the sound it makes ("none" counts as a finding).
- **Errors and performance:** `get_runtime_logs` errors, plus a `get_scene_analysis` summary.
- **Design docs:** `ART-DIRECTION.md`, `STORY.md` and `refs/`.

## Step 2: the review (the reviewer subagent does this)
Start the reviewer with the Agent tool. Give it:
- this file
- `../de-ai/BANNED.md`, plus any bans in `studio-profile.md` if it exists
- `../de-ai-ui/SKILL.md`, `../de-ai-story/SKILL.md` and `../de-ai-feel/SKILL.md`
- the audit folder

**Do not** give it your opinion of the game.

It scores each area **0** (clearly AI or generic), **1** (passable, but you can tell), or **2** (feels made by a person on purpose). For every score it cites a specific screenshot, line of text or moment:

1. **UI and fonts:** designed by a person, rooted in the game's world; hierarchy is clear.
2. **Art and lighting:** a consistent direction; nothing default, placeholder or untextured; scenes have depth.
3. **Writing:** sounds human; distinct voices; no exposition dumps or banned phrasing.
4. **Feel and sound:** every action has sound and effects; big moments land; it holds up under lag.
5. **First 10 seconds:** fun right away, solo, without reading a tutorial.
6. **Phone:** readable, reachable, nothing overlapping.
7. **Store page:** the icon, thumbnails and description look like a real studio made them.
8. **Banned list:** zero matches against `BANNED.md` and any bans in `studio-profile.md`. Any match makes this a 0. This includes a search of all exported text and store copy for the em dash `—`.

## Step 3: the fix plan (the reviewer writes this)
List every problem, **worst first**. For each one:
- what's wrong
- where it is (a screenshot or a file)
- a concrete fix that names the replacement, for example: "Replace the Orbitron title with the stamped serif from ART-DIRECTION.md, and swap the thin bar for the rally trip-meter readout."

Also list any new AI tell it found that isn't in `BANNED.md` yet.

## Step 4: fix and re-audit (the build thread does this)
1. Apply the fixes, worst first.
2. Gather fresh evidence and run a **new** reviewer subagent, not the same one.
3. Repeat until every area scores 2, or the user explicitly OKs an exception.
4. Save before/after screenshots side by side in the audit folder.

## Output
**`design/<game>/audit/<YYYY-MM-DD>/DE-AI-REPORT.md`**, written by the reviewer, next to the other audits' reports from the same date (`DESIGN-REPORT.md`, `CHARACTER-REPORT.md`, `LEVEL-REPORT.md`, `SOUND-REPORT.md`). It **starts with a 5-line plain summary** (overall verdict, the worst area, the 3 worst problems in one line, what was fixed, what still needs the user), then contains:
- the scores
- the evidence links
- the fix plan
- what was fixed
- the before/after images
- any new tells added to `BANNED.md`

**Always present a clear overview in chat** to the user: the scores, the 3 worst problems, what was fixed, and the before/after sheet. The file holds the detail; the chat overview is what the user reads.
