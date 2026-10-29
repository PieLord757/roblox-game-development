---
name: level-design
description: Start here for any level, map, world, room, arena or hub work in a Roblox game. Explains why layout decides whether a game is fun, the process (references, LEVEL-PLAN.md, grey blockout in Studio, user approval of the blockout, art pass, audit), and which level-design sub-skill to load (craft, roblox, audit). Use before laying out, blocking out, dressing, or reviewing any playable space.
---

# Level design (start here)

## Why layout matters
The level is the game the player actually touches. The same mechanics feel brilliant in one layout and dull in another:
- A chase is only scary if the corridor bends before the player can see the end.
- A stealth game is only clever if there are three ways in and a place to watch from first.
- An arena is only fair if no spawn can see another spawn and every choke has a flank.
- A story only lands if the room tells it before any text does.

Players never say "the pacing was off" or "I had no landmark". They say "it got boring", "I got lost", "it was unfair", and they leave. On Roblox this is sharper than elsewhere:
- **Players are on phones** with a small screen and no shadows on low graphics settings, so guidance that relies on subtle detail disappears.
- **The first minute decides retention.** A player who is lost or bored in the first room never sees the good room.
- **Every Roblox map competes with a million free-model maps.** A space built from default parts and a grid of identical rooms reads as low effort at once.

**The standard:** every space has a reason for its shape. A player can always answer three questions within five seconds of entering it: where am I, where can I go, and what matters here. The layout teaches, paces and guides without a single arrow or tutorial line.

## What this skill produces
For each playable space (a level, a map, a hub, an arena, a run's room pool):
1. **`LEVEL-PLAN.md`** in `design/<game>/levels/<space>/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default), copied from `LEVEL-PLAN-TEMPLATE.md` in this folder. It holds, at minimum:
   - a **top-down sketch** (a grid sketch in the file, then the real top-down screenshot of the blockout)
   - the **pacing**: a beat list with intensity and duration in seconds
   - the **landmarks**: one per area plus the weenie that pulls toward the goal
2. **A grey blockout built in Studio**, with a screenshot sheet: the top-down view, the view from each area's entrance, and the critical path walked in a playtest.
3. **User approval of the blockout before any art goes on it.** This is a hard stop. Art on an untested layout is the most expensive mistake in level design.
4. **A chat overview** each time a plan or a blockout is shown (see "Output").

## The process
Keep it in hours, not days. A small space should go from reference to approved blockout in one working session.

1. **Reference.** Before drawing anything, collect 4-8 references for this space: shipped game levels that solve the same problem (top-down maps if you can find them), real places the setting is based on (floor plans, aerial photos, photos at eye height). Save them to `design/<game>/refs/levels/` with one line each on what you take from it (a loop, a sightline, a landmark, a scale). Designing from references, not imagination, is the biggest single fix for generic layouts.
2. **Plan.** Copy the template and fill it in: one-line goal per area, the layout archetype, the beat list and intensity curve, the teaching plan for each mechanic, landmarks, guidance, routes, the "what happened here" sentence. Use `level-design-craft` for every decision. Present the plan to the user as a chat overview. Small spaces can go straight to blockout; a whole map or a new archetype should get a quick OK first.
3. **Blockout.** Build the space in grey in Studio, to metrics, on a 5-stud grid, with one reserved accent color for anything usable. Follow `level-design-roblox` (the blockout workflow and the metrics).
4. **Test and iterate.** Walk the critical path in a playtest, time each beat, take the five-second screenshots, run bots through it if the game uses them. Change the blockout and test again. **At least three iterations before showing the user.** Log each iteration in the plan.
5. **User approval (stop here).** Send the screenshot sheet with a chat overview. Wait for an explicit OK. Log the approval or the requested changes in the game's `progress.md`. No art, lighting polish or dressing before this OK.
6. **Art pass.** Replace grey with the modular kit, keeping every metric and every sightline that the blockout proved. Then the lighting pass (guidance first, mood second), the sound pass (hand over the area list to the `sound` skill), and the performance pass. Load `de-ai-ui` for the art direction and `de-ai-story` for any text or prop storytelling.
7. **Audit.** Run `level-design-audit` with a fresh reviewer at the end of the milestone that built or changed the space. Fix, re-audit, then show the user.

If a change after approval moves a wall, a route, a spawn or a landmark, it goes back to step 4 and the user sees the change before art is redone around it.

## Which sub-skill to load
| You need | Load |
|---|---|
| Pacing and intensity curves, teaching through layout (the four steps), navigation, landmarks and weenies, light and color guidance, sightlines, density and verticality, environmental storytelling, set pieces, and the layout archetypes (linear, hub, vertical, dense room, districts, arena lanes, stealth rings) | `level-design-craft` |
| Roblox metrics and measuring your rig, the Studio blockout workflow, top-down screenshots, terrain vs parts, modular kits and Packages, StreamingEnabled, draw-call and memory budgets, lighting technology, PathfindingService for bots, set-piece implementation | `level-design-roblox` |
| Reviewing a blockout or a finished space: evidence, the blind five-second test, scoring, the report | `level-design-audit` (run by a fresh reviewer subagent) |

Load `level-design-craft` and `level-design-roblox` together for any build. Also load:
- `sound` when the space is ready for its audio pass (every area in the plan becomes an audio map there)
- `de-ai-ui` before the art and lighting pass
- `testing` before shipping, because the level's critical path becomes part of the playthrough test

## Rule index
Rules keep the same IDs in every file so the audit can cite them.

| IDs | Area | Lives in |
|---|---|---|
| LC1 to LC22 | Craft: pacing, teaching, navigation, light, sightlines, density, story, set pieces, archetype rules | `level-design-craft` |
| LR1 to LR16 | Roblox: metrics, blockout, terrain, kits, streaming, performance, bots, set pieces | `level-design-roblox` |
| LG1 to LG4 | Gates (below) | this file |

## The gates (these block)
- **LG1** No art, dressing or lighting polish before the user approves the blockout.
- **LG2** No blockout without a `LEVEL-PLAN.md` that has a top-down sketch, a beat list with seconds, and a landmark per area.
- **LG3** No user showing without at least three test-and-change iterations logged in the plan, with screenshots from a real playtest.
- **LG4** No milestone ends on a new or changed space without a `level-design-audit` run.

## What great looks like
- **The player always knows where to go and never feels told.** The exit is lit or framed; the landmark is in view; the wrong way is darker or cluttered, not walled off by an invisible barrier.
- **Time is designed, not space.** Every length in the plan is also written in seconds at the game's walk speed, and something happens every 15-40 seconds of travel.
- **Every peak has a valley after it.** The player gets a breath, a view or a safe room before the next push, and each push is a little bigger.
- **Each mechanic is introduced safely, developed, twisted, then retired.** Nothing is used to exhaustion.
- **The space tells a story on its own.** Three to five props imply what happened here; one thing does not fit, and that is the clue.
- **The blockout proved it.** Jumps, sightlines, routes and timings were tested in grey, so the art pass only adds beauty.

## Common mistakes
- Building art first and testing the layout after, so every fix is expensive and none gets made.
- A flat intensity curve: everything at 7 out of 10 reads as noise; everything at 3 reads as boredom.
- Grids of identical rooms and corridors with no landmark, so the player cannot build a mental map.
- Dead ends with nothing in them, and corridors that end in a blank wall.
- The accent color used on decor, so the player stops trusting it.
- Guidance that relies on shadows, which disappear on low graphics quality.
- Metrics guessed instead of measured, so jumps fail and the camera clips in narrow halls.
- Teaching a mechanic for the first time in a place where failing kills the player.
- An arena where a spawn can see another spawn, or a choke with no flank.
- Too many lanes or routes, so players never meet each other or the bots get lost.

## Output
1. **`design/<game>/levels/<space>/LEVEL-PLAN.md`** from the template, kept up to date through every iteration.
2. **The blockout screenshot sheet** in `design/<game>/screenshots/levels/<space>/<YYYY-MM-DD>/`:
   - the straight-down top-down view of the whole space
   - one eye-height shot from each area's entrance (the five-second shots)
   - the weenie or landmark framed at least once
   - phone-size shots of the two most important views
   Combine them into one image or a short ordered set and send it to the user (SendUserFile or the equivalent).
3. **A chat overview, as an explicit step,** in the message that carries the sheet. The user should understand the space in under a minute without opening the file:
   - the space's one-line goal and its layout archetype, in plain words
   - a short walk-through of the critical path: "you start at X, see Y, go through Z", with the total time
   - the pacing in one line: where the peaks are and where the player gets a breather
   - the landmarks, one line each
   - what changed across the test iterations and why
   - the open questions or risks, if any
   - what you need: "approve the blockout, or tell me what to change"
   Do not paste the whole plan into chat, and do not make the user open the file to understand the layout.
4. **Log the approval** (or the requested changes) in `progress.md`, with the date.

## Studio-specific facts
Where games live, the studio's preferred tools, the user's preferred camera and walk speeds, and any house rules for levels are studio-specific. Read `studio-profile.md` at the project root if it exists. If it doesn't, use the defaults in these skills and write down what you assumed in the plan.

## Tools
- Building and inspecting: `execute_luau`, `multi_edit`, `search_game_tree`, `inspect_instance` (built-in Roblox Studio MCP); `execute_luau`, `manage_instance`, `set_properties`, `search_objects`, `get_instance_properties` (community robloxstudio MCP).
- Screenshots: `screen_capture` in edit mode; `capture_screenshot`, `capture_device_matrix` during playtests; `selection` with `action=view` to frame an instance before a capture.
- Playtests and walking: `solo_playtest`, `multiplayer_playtest`, `character_navigation`, `eval_server_runtime`, `eval_client_runtime`.
- Performance: `get_scene_analysis`, `get_memory_breakdown`, `capture_micro_profiler`, `set_device_simulator`.
- Docs: `get_roblox_docs` before relying on any API you are unsure of.

Tool name prefixes differ between installs. Use whatever prefix your session shows.

## Sources
The rules rest on public talks, books and docs. The full list with links is at the end of `level-design-craft` and `level-design-roblox`. Key ones:
- "Level Design in a Day" sessions, GDC 2010-2015.
- Smith and Worch, "What Happened Here? Environmental Storytelling", GDC 2010.
- Koichi Hayashida on four-step level design (Super Mario 3D Land and 3D World).
- Scott Rogers, "Everything I Learned About Level Design I Learned from Disneyland", GDC 2009.
- Christopher W. Totten, *An Architectural Approach to Level Design*, 2nd ed., 2019.
- Roblox Creator Docs: environmental art curriculum, streaming, performance optimization, terrain.
