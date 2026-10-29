---
name: testing
description: Start here for testing any Roblox game. Explains why we test, what to run for a quick check, a milestone or a publish, the DataStore safety rule that comes before everything, and which testing sub-skill to load (full run, exploits, devices and performance, first-time player, pre-publish checklist). Use before any test run, at every milestone, and always before publishing.
---

# Testing (start here)

## Why this exists
A Roblox game is judged in its first session. If the loop gets stuck, the phone layout hides the main button, or a player loses their save, they leave and don't come back. Worse failures are invisible until launch day:
- an exploiter fires a "sell" remote with `NaN` and maxes out their currency
- a test DataStore name gets published and every player starts from zero
- server memory climbs until the server crashes

Reading the code doesn't catch these. Playing the game through the tools, attacking it, and measuring it does.

**The standard:** every test run produces `TEST-REPORT.md`, with a PASS, FAIL or NOT RUN verdict and evidence (screenshots, log lines, numbers) for each of eight areas:
1. unit tests
2. a full playthrough by an agent
3. multiplayer
4. phone
5. lag
6. performance
7. exploits
8. saving

Bugs are ranked worst first. A fresh first-time-player agent also plays blind and reports where it got confused or stuck, and how long it took to reach the fun.

## Phase 0 safety rule (read this before touching a playtest)

> **A Studio playtest of a published place reads and writes the REAL DataStore.** The exploit burst and the save tests will damage real player data unless the store name is swapped first.
>
> 1. **Sync from disk first.** A sync restores the real store name from disk, so it must come before the swap, never after.
> 2. **Then swap the store name** to a test name (`<Game>_test<unix time>`), in Studio only. Write down the original name.
> 3. **Then verify it live.** After Play starts, read the store name the running server is actually using with `eval_server_runtime`. If it is not the test name, stop. Run nothing else until it is.
> 4. **Re-check before Phase 4 (saving) and Phase 6 (exploits), and after every re-sync.** Every bug fix that re-syncs from disk silently puts the real name back.
> 5. **Restore at the end of every run,** quick checks included. Stop Play, run a plain sync from disk (it restores the real name), and confirm it in edit mode with `execute_luau`. Never leave a place holding the test name.
>
> If you can't tell which Studio window is yours, or where the store name lives, stop and ask. Never guess.

Where the store name lives, how to sync, and what the project-identity attribute is called are studio-specific. Read `studio-profile.md` at the project root if it exists. If it doesn't, find the store name by searching scripts for `GetDataStore` (`script_grep` or `grep_scripts`), and record what you found in the test report.

## When to run what

| Trigger | What to run | Load |
|---|---|---|
| Any code change (quick check) | Phases 0, 1, 2 | `testing-run` |
| Gameplay or system change | Phases 0 to 4 | `testing-run` |
| New or changed remote | Phases 0, 1, 6 | `testing-run`, `testing-exploits` |
| UI change | Phases 0, 2, 8 | `testing-run`, `testing-devices-perf` |
| **End of every milestone** | Phases 0 to 10, full `TEST-REPORT.md` | all sub-skills |
| **Before the first private publish of a new game** | Phases 0 to 10 (a milestone run); saving and analytics may be marked "pending the private build" | all sub-skills; see Gate A in `publish-launch` |
| **Before going public, and before every publish of an already-public game** | Phases 0 to 11 on the published place, plus the checklist | all sub-skills, plus `PREPUBLISH-CHECKLIST.md`; Gate B in `publish-launch` |

A quick check still writes a short `TEST-REPORT.md`; areas not run are marked NOT RUN with the reason "quick check".

**Any Critical failure blocks publishing,** including the first private publish. **NOT RUN on saving or exploits blocks going public and blocks every update to a public game:** "we didn't test it" is not a pass. The one exception is the first private publish of a never-published game, where saving can't be tested yet (`game.PlaceId` is 0): that publish follows Gate A in `publish-launch` (also summarized in `publish`), and the full block applies again on the published private build before it goes public (Gate B).

## Which sub-skill to load

| You need | Load |
|---|---|
| The full phased process, pass/fail criteria, the report template, severity scale and the fix loop | `testing-run` |
| The exploit suite: the remote table, hostile arguments, bursts, replays, races | `testing-exploits` |
| The device matrix, measuring UI in code, network profiles, performance budgets | `testing-devices-perf` |
| The blind first-time-player testers: the agent definition, the exact prompt, what to measure | `testing-first-time-player` |
| The pre-publish checklist and the launch-day bug table | `PREPUBLISH-CHECKLIST.md` (in this folder) |

`testing-run` is the backbone. Load it for any run, then load the others when you reach their phases.

## Who does what
- **The build thread** runs the tests, fixes the bugs, re-tests, and writes the report.
- **Fresh blind subagents** play as first-time players. They never see source, design docs or dev hooks.
- **The user** sees the 5-line summary at the top of `TEST-REPORT.md`, plus anything left unfixed. Nothing else, unless they ask.

## What great testing looks like
- **Assert on truth, not on pictures.** Server state read through `eval_server_runtime` is the truth. Screenshots prove layout and look; they don't prove a reward was granted.
- **Drive the game the way a player reaches it.** Fire the same remote the button fires, walk with `MoveTo`, and go through the real menus. A test that calls internal functions directly skips the bugs between the button and the server.
- **Be the player who does it wrong.** Wrong order, twice in a row, mid-transition, while dead, while lagging, on the smallest phone. Happy paths rarely find launch-day bugs.
- **Attack it.** Every remote gets hostile arguments. Exploiters will do it on day one.
- **Measure, then compare.** Numbers against a budget and against last run's baseline. "Feels fine" is not a result.
- **Spend time where bugs hurt most:** saves, economy and remotes, the core loop, the first minute, phones. In that order.
- **A failing test is a success.** It found a bug before a player did. Never weaken a test to make it pass.

**Common mistakes:**
- skipping the store guard after a re-sync
- reading live state with `execute_luau`
- writing PASS for an area that wasn't run
- quoting background-window frame rates
- leaving playtest windows open

## Output
Every run ends with two things:
1. **`TEST-REPORT.md`** in `design/<game>/tests/<YYYY-MM-DD>/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). It starts with a 5-line plain summary; `testing-run` has the template.
2. **A clear overview in chat.** The file is the detail; the chat overview is what the user reads. Give the 5-line summary, then anything left unfixed (one plain sentence each, with severity), then the report path. Say plainly if publishing is blocked.

## Tools

**Built-in Roblox Studio MCP**
- `list_roblox_studios`: find your Studio window by name.
- `start_stop_play`: the fallback when `solo_playtest` returns "Unknown error".
- `execute_luau`: edit-mode checks and unit tests. **It runs in its own VM** with fresh `require` copies, so it cannot see live game state.
- `get_console_output`: unit test output.
- `screen_capture`: the fallback when `capture_screenshot` returns a black or stale frame.
- Built-in skills (load with the `skill` tool): `rbx-unit-test`, `rbx-device-simulator-lua`, `rbx-perf-profiling`, `rbx-debug`.

**Community robloxstudio MCP**
- `get_connected_instances`: pick the right Studio process and playtest peer.
- `solo_playtest`, `multiplayer_playtest`: real sessions, 1 to 8 clients.
- `eval_server_runtime`, `eval_client_runtime`: **the only way to read or drive live state.** They share the running game's `require` cache.
- `get_runtime_logs`: read unfiltered, check the `level` field.
- `capture_screenshot`, `capture_device_matrix`: evidence.
- `set_network_profile`: lag, jitter, packet loss.
- `capture_script_profiler`, `capture_micro_profiler`, `get_memory_breakdown`, `get_scene_analysis`: performance and leaks.

Tool name prefixes differ between installs (for example `mcp__robloxstudio__eval_server_runtime`). Use whatever prefix your session shows.

## Gotchas that shape every test
- **Multiple Studio windows.** Several Studio processes may be open. Call `list_roblox_studios` and `get_connected_instances`, pick yours by name, then confirm the project-identity attribute on `workspace` (named in `studio-profile.md`) before any write. Pass the right `instance_id` or `studio_id` on every call.
- **BillboardGuis and Highlights don't show in captures.** A missing billboard in a screenshot is not a bug by itself. Check those visuals by reading their properties with `eval_client_runtime`.
- **The first frame after Play is often black.** Retake it once after 2 s; if it is still black, use `screen_capture`.
- **`eval_*` fails with "Unknown error"** in the first few seconds after Play starts, or if one call waits about 60 s. Wait about 5 s after start, and keep each call under 25 s. Loop with several calls instead of one long wait.
- **Listeners die when an `eval_client_runtime` call returns.** Poll inside one call: `while not cond and t < 20 do task.wait(0.1) end`.
- **Synthetic GUI clicks are unreliable.** Test a button by firing the remote it fires, from `eval_client_runtime`, then assert on the server.
- **Move characters with `Humanoid:MoveTo`**, not pathfinding. Pathfinding returns NoPath through narrow doors that players walk through fine.
- **A background Studio window renders at about 15 fps.** Its client frame times are not evidence.
- **Each MCP call costs 1 to 3 s of game time.** Use dev hooks for anything timed. Never assert on wall-clock timing across calls.
- **Close playtest windows after every test,** including after a failure: `solo_playtest stop`, `multiplayer_playtest end`, or `start_stop_play`. Then `reset_simulation_state`. Stray playtest windows steal focus and input from the next run.
