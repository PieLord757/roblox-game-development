---
name: testing-run
description: The full phased test process for a Roblox game (Phases 0 to 11) with measurable pass/fail criteria, the severity scale, the fix-and-retest loop, and the TEST-REPORT.md template that starts with a 5-line plain summary. Use for any test run, from a quick check to a pre-publish run; the testing router says which phases to run.
---

# Test run

Load `testing` first if you haven't. It holds the Phase 0 safety rule and says which phases this run needs.

## Setup
1. Read `studio-profile.md` at the project root if it exists. It says:
   - how to sync from disk, and the sync mode that includes test modules
   - the name of the project-identity attribute on `workspace`
   - where the DataStore name is set
   - what the dev hooks are called
2. Create `design/<game>/tests/<YYYY-MM-DD>/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). If a run already exists for today, add a suffix (`2026-03-14b`). Every screenshot, log excerpt and profiler summary from this run goes in this folder.
3. Read the game's design doc for the core loop and the economy targets. Expected values come from the design, never from what the code does now.
4. Read the previous `TEST-REPORT.md` for this game, if there is one: last run's unit test count, performance baselines, known engine noise in the logs, and waivers.

### Dev hooks the game should expose
Scripted tests need a Studio-only door into the game. The game should have a module, guarded by `RunService:IsStudio()`, that offers:
- `getState()`: a plain-table snapshot of round phase, timer, scores, and each player's profile
- `skipTo(phase)`, `setClock(t)`, `hold(flag)`: for timed beats
- `spawnBots(n)`: for solo fill
- funnel timestamps: the first time each player reaches each onboarding step (joined, understood goal, first core action, first reward), recorded with `os.clock()` on the server

A BindableFunction returns copies of tables, so re-read the state after every action. If the hooks are missing, file it as a **High** bug ("no dev hooks: Phases 3 to 10 can't be scripted reliably"), add them if the build thread owns the code, and only then go on. Don't silently skip phases.

## Severity scale
Rank every bug by severity, then by how many players hit it.

| Severity | Meaning | Examples |
|---|---|---|
| **Critical** | Blocks publishing. No waiver. | Any state change from a hostile remote. A write to the real DataStore during tests, or the real name not restored. The solo loop can't complete. A phase gets stuck. A server error in the core loop. Any unit `[FAIL]` or `[TIMEOUT]`. Progress lost on rejoin. A reward granted twice. |
| **High** | Most players notice; fix before publish unless the user waives it in writing. | A main button off-screen or under the notch on a phone. A late joiner sees a broken HUD. The loop fails under the `poor` network profile. Memory grows every round. Missing dev hooks. |
| **Medium** | Some players notice; fix this milestone if time allows. | Truncated text on a secondary menu. A recurring first-time-player confusion point with a workaround. A function over budget that doesn't drop frames yet. |
| **Low** | Polish. | A 40 px touch target on a rarely used button. A one-off warning in the logs. |

## Stop rules
- **Phase 0 fails:** hard stop. Run nothing else. The report says why.
- **Phases 1 to 4 fail:** fix and re-run that phase before moving on, because later phases depend on them. The original failure still goes in the bug list, marked "fixed during run".
- **Phases 5 to 10:** run all of them and collect every failure. Fix afterwards in the fix loop.

## The phases

Each phase writes its verdict, evidence and bugs straight into the report as you go, so a crash halfway still leaves a useful report.

### Phase 0: Preflight and DataStore safety (always)
1. `list_roblox_studios` (built-in) and `get_connected_instances` (robloxstudio). Pick your Studio by name. Read the project-identity attribute on `workspace` with `execute_luau` and confirm it matches this game. If two windows could be yours, or none clearly is: **FAIL**, ask the user.
2. **Sync first**, using the test-inclusive sync from `studio-profile.md`. Before syncing, check that the sync server is serving *this* game's files (for example its manifest names this game's folder). Another app or another session may hold the port.
3. **Then swap the store.** In Studio only, set the DataStore name to `<Game>_test<unix time>`. Record the original name in the report.
4. Stop any device simulation, and `reset_simulation_state`.
5. Start Play (`solo_playtest action=start mode=play`, or `start_stop_play` if that returns "Unknown error"). Wait about 5 s.
6. **Store guard:** `eval_server_runtime` reads the store name the live server is actually using (the config module, or the name passed to `GetDataStore`). It must equal the test name.
7. Note `game.PlaceId`. If it is 0 (the place is not published), Studio can't reach DataStores at all. Live save tests in Phase 4 will be NOT RUN, and the report must say so.
8. Check "Enable Studio Access to API Services" if the place is published. Error code 403 in the logs means it is off.

**PASS:** the right Studio is confirmed, the sync reported success, and the live store name is the test name. **FAIL:** anything else. Hard stop.

### Phase 1: Unit tests
1. Detect the framework: `script_grep` for `JestGlobals`, `TestEZ`, `RunUnitTest`, `.spec`. Conform to what exists. Never install packages yourself; if a framework the code references is missing, report it and stop this phase. The `rbx-unit-test` skill covers the built-in harness.
2. With Play running, run the suite with `execute_luau` (`datamodel_type="Server"`), for example `require(ServerStorage.UnitTest.RunUnitTest)(nil, 5)` or the project's runner. Read `get_console_output`.
3. Every pure module (rules, economy, round state, damage) should have a test with normal, boundary (empty, nil, 0, negative, huge, duplicate) and error cases. Missing tests for a new module are a **Medium** bug.
4. Economy invariants that should exist as unit tests: currency never negative; a purchase charges and grants both or neither; the same receipt never grants twice; no buy-then-sell profit; earning rates match the design curve.

**PASS:** the summary shows 0 failed and 0 timeout, and the run count is at least last run's (no tests silently lost). **FAIL:** any `[FAIL]` or `[TIMEOUT]`, a case module that didn't return a function, or a lower test count. Report each failure as `input / expected / actual`. **Never weaken a test to make it pass.** A test that exposes a real bug did its job. Use `rbx-debug` to investigate.

### Phase 2: Solo smoke
1. Fresh Play. `get_runtime_logs` unfiltered for the first 20 s. Check the `level` field; a filter for "rror" misses Luau errors.
2. `capture_screenshot`. If black, retake once after 2 s, then fall back to `screen_capture`.
3. `eval_server_runtime`: `getState()` returns the expected starting phase.

**PASS:** 0 errors or warnings from game scripts (ignore engine noise listed in the previous report), a non-black frame showing the expected first screen, and a starting state that matches the design.

### Phase 3: Agent playthrough (solo with bots)
This is the "full playthrough by an agent" area.
1. Write the core loop as ordered beats from the design doc. Example: spawn, reach the lobby pad, round starts, core action ×N, win or lose, results, reward, back to lobby.
2. For each beat:
   - **Drive** it the way a player would reach it. Move with `Humanoid:MoveTo` and poll inside one `eval_client_runtime` call (20 s max per call). Press buttons by firing the remote the button fires, with the same arguments. Use `skipTo`, `setClock` and `hold` for timed beats instead of racing the clock.
   - **Assert on the server** with `eval_server_runtime` and `getState()`: the transition is legal and in order, timers, scores and rewards are right.
   - **Assert on the client** with `eval_client_runtime`: HUD text and visibility match server state after a 1 s settle, `TextFits` is true, and elements are inside the viewport.
   - **Capture** one screenshot per beat, saved as `p3-<beat>.png`.
3. Run the loop **3 times back to back** in the same session. Count event handlers or log lines per event in rounds 1 and 3.
4. Edge cases worth one pass each: the player dies or resets during the countdown; the timer hits 0 the instant the objective completes; a seated player is teleported.

**PASS:** every beat happens in order, within its design time plus 5 s; rewards are granted exactly once per round; bots fill the solo game; 0 runtime errors; round 3 behaves like round 1 (same handler counts, no duplicated UI). **FAIL:** a stuck phase, a missing or double reward, an illegal transition, or a HUD that disagrees with the server. A solo loop that can't complete is **Critical**.

### Phase 4: Saving and economy
**Re-run the store guard first** (Phase 0 step 6). If the live store name isn't the test name, stop.

If `game.PlaceId` is 0, live saving can't be tested: run steps 4 and 5 only (fake-store unit tests and economy simulation), and mark the saving area **NOT RUN (place unpublished; pending the private build)** with the unit evidence attached. That is not a PASS. It is allowed only for the first private publish (Gate A in `publish-launch`); going public needs this phase passed on the published place (Gate B).

1. Read the player's server profile. Play through real actions that change currency, inventory and progress. Read it again (A).
2. Leave and rejoin (`multiplayer_playtest action=leave_client`, then `add_players`; or stop and start Play). Read the profile (B). Also call the save-all / `BindToClose` path directly once, because Studio's shutdown behaves differently from a live server.
3. Remove the test key (test store only) and rejoin: a brand-new player gets the defaults.
4. Unit level with an injected fake store: an old-schema profile migrates; corrupt or partial data doesn't wipe the profile; a store that throws (simulated throttle or outage) retries with backoff and never overwrites good data with defaults; replaying the same receipt id grants once.
5. Economy simulation in `eval_server_runtime`: run the reward functions for N simulated rounds. Check currency per hour and time to each unlock against the design bands.

**PASS:** B deep-equals A on every saved field; defaults load for a new player; no DataStore error codes in the logs; purchases are atomic and idempotent; the economy is inside the design bands. Lost progress or a double grant is **Critical**.

### Phase 5: Multiplayer
1. `multiplayer_playtest action=start numPlayers=3`. Run the core loop with all clients acting (target `client-1`, `client-2`, `client-3` with `eval_client_runtime`).
2. **Replication:** after each beat, compare key state on the server and every client. Equal after a 1 s settle.
3. **Late join:** `add_players` with 1 mid-round. The new client's HUD and state match the server within 2 s. The usual bug is state sent once by a RemoteEvent before they joined.
4. **Leave:** `leave_client` for `client-2` mid-round. The server's player-keyed tables no longer hold that player, their connections are gone, and the round continues or ends as designed.
5. **Race:** two clients claim the same pickup or the last stock at once. Exactly one succeeds. (See `testing-exploits` for how to fire in the same frame.)
6. **Intro gate:** the intro still plays for a slow client. Remotes fired before the client connects are lost, so the game should wait for a client "hello".

**PASS:** all of the above, and 0 errors in `get_runtime_logs` with the `multiplayer_group_id`.

### Phase 6: Exploits
**Re-run the store guard first.** The burst tests write a lot. Then load `testing-exploits` and run its full suite.

**PASS:** no hostile call changes currency, inventory, score or round state; rejections are clean returns, not server errors; the rate limiter engages; nothing the server trusts lives in ReplicatedStorage. **Any state change from a hostile call is Critical.**

### Phase 7: Lag
Load `testing-devices-perf` (network section). Re-run the Phase 3 loop under `poor` and under the custom profile, plus the late-join part of Phase 5.

**PASS:** the loop completes; no UI waits more than 10 s; no double actions from repeated input; legitimate laggy actions aren't rejected by server distance or timing checks. Finish with `reset_simulation_state`.

### Phase 8: Phone and devices
Load `testing-devices-perf` (device section). Run the device matrix and the in-code UI measurement on every device.

**PASS:** 0 interactive elements off-screen or under the safe-area inset; 0 truncated labels on the core HUD and menus; 0 touch targets under 44 px; no overlaps or illegible text in the captures; every button reachable by gamepad. A main action unreachable on a phone is **High** at least.

### Phase 9: Performance
Load `testing-devices-perf` (performance section). Profile during the scripted loop with 3 clients; take memory after rounds 1 and 3.

**PASS:** inside every budget in that skill, no growth across rounds, and no regression over 20% against the last baseline. Client frame times from a background window are never evidence. Mark "real-device phone check still needed" until a person confirms it on a phone.

### Phase 10: First-time player
Load `testing-first-time-player` and run 3 blind testers, one after another.

**PASS:** at least 2 of 3 reach the first core action within 10 actions and the first reward within 25 actions (that skill explains why actions, not seconds); no confusion point recurs in 2 or more testers; no tester gets stuck with no way forward. A recurring confusion point is a design bug, at least **Medium**; a dead end is **High**.

### Phase 11: Restore and pre-publish (before going public or updating a public game: Gate B in `publish-launch`)
1. Stop Play. Run a **plain** sync from disk (not the test-inclusive one). It strips the test modules and restores the real store name.
2. In edit mode, `execute_luau` confirms: the DataStore name equals the original recorded in Phase 0; the unit test folder and cases are gone; the dev hooks are guarded by `RunService:IsStudio()`.
3. Clear the device simulator and `reset_simulation_state`.
4. Go through `../testing/PREPUBLISH-CHECKLIST.md`. Every box is checked or has a written waiver from the user.

**PASS:** both checks pass and the checklist is complete. A store name that isn't restored is **Critical**.

## Craft: how to test well

### Writing good unit tests
- **Test the contract, not the code.** Take expected values from the design doc, the function's name, its docstring and its callers. If you read the implementation and copy what it returns into the assertion, the test can never fail and proves nothing.
- **One behaviour per case, Arrange, Act, Assert.** A case named `sell_negative_quantity_is_rejected` that fails tells you the bug from its name.
- **Go to the edges.** Most bugs live at 0, 1, the maximum, empty, nil, negative, duplicate, and "exactly at the boundary". A test suite of only happy paths is a smoke test.
- **Make it deterministic.** Inject the clock, the random generator (seeded `Random.new(seed)`) and the DataStore. A test that passes 9 times in 10 is worse than no test, because people learn to ignore it.
- **Fresh state per case.** `require` caches module state for the whole Play session. Build a new instance per case or call a reset.
- **Assert invariants, not just examples.** "Currency is never negative after any sequence of buys and sells" catches bugs no single example would. Loop over every item in the config: every price above 0, every unlock reachable.
- **Every fixed bug gets a test** that would have caught it. That is how a suite gets good.

### Designing a thorough playthrough
- **Start from the player's journey, not the code.** List every beat a real player goes through, from joining to their second round, including menus, the shop, dying and respawning.
- **Assert at every beat, on the server.** A playthrough that only checks "no errors" misses a round that gives 0 coins. Read the state after each beat and compare with the design.
- **Then break the order.** Real players do things out of order: open the shop mid-countdown, die during the results screen, leave during a purchase, press the button twice. One deliberate "wrong order" pass per beat finds more bugs than three more happy paths.
- **Go round three.** Many bugs only appear on the second or third round: handlers connected twice, UI cloned twice, timers not reset, rewards stacking.
- **Solo first, always.** The game must be complete with one player and bots. Multiplayer is the extra.

### Finding the bugs that matter
Spend your time where a bug costs players the most. In order:
1. **Data:** anything that can lose, duplicate or corrupt a save.
2. **Economy and security:** anything that gives currency or items, and every remote that does.
3. **The core loop:** anything that gets a round stuck or ends it wrong.
4. **The first minute:** the join, the intro, the first action. Every player sees it.
5. **Phone:** most players are on one.
6. Everything else.

Look hardest at **state transitions** (round start and end, join and leave, death and respawn), **anything timed**, **anything with two players touching the same thing**, and **code added late** in the milestone. Those are where bugs cluster.

### Common mistakes
- Using `execute_luau` to read live game state. It runs in its own VM and sees empty tables. Use `eval_server_runtime`.
- Clicking GUI buttons with synthetic input, getting no response, and filing a bug. Fire the remote the button fires.
- Long waits inside one `eval_*` call. Over about 25 s it fails with "Unknown error".
- Asserting on timing across MCP calls. Each call costs 1 to 3 s of game time.
- Calling a missing billboard in a screenshot a bug. Captures don't show BillboardGuis or Highlights.
- Weakening a failing test to get green.
- Forgetting the store guard after a re-sync.
- Writing "PASS" without evidence, or "PASS" for something that wasn't run.
- Leaving playtest windows open; the next run talks to the wrong one.

## Teardown (every exit path, including failures)
- `solo_playtest action=stop`, `multiplayer_playtest action=end`, or `start_stop_play` to stop.
- `set_network_profile` back to normal and `reset_simulation_state`.
- Stop the device simulator.
- Confirm with `get_connected_instances` that no playtest windows of yours are still open. Close them if so.
- **Restore the store, every run** (quick check and milestone too, not only before publish): run a plain sync from disk, then confirm in edit mode with `execute_luau` that the DataStore name equals the original recorded in Phase 0. Record `restored: yes` in the report. If the restore fails, that is a Critical bug and the first line of the chat overview.

## The fix loop
1. Fix bugs worst first. Each fixed bug gets a unit test or a playthrough assertion that would have caught it.
2. **Every fix means a re-sync from disk, and every re-sync restores the real store name.** Re-swap the store and re-run the store guard before re-running Phase 4 or 6.
3. Re-run Phases 0, 1, 2 (regression), then every phase that failed.
4. At most 3 fix rounds per run. Anything still failing goes under "Left unfixed" with what was tried.
5. Update the same report: mark each bug fixed (with the round) or left unfixed. Keep the original failure evidence.

## Writing evidence
Evidence is something another agent could check:
- a screenshot file name in the run folder
- a quoted log line with its level
- a number with its source (`get_memory_breakdown`: LuaHeap 41.2 MB after round 1, 41.9 MB after round 3)
- a state snapshot before and after

"Looked fine" is not evidence.

## Report template
Write `design/<game>/tests/<YYYY-MM-DD>/TEST-REPORT.md`. Optionally append one line per run to `design/<game>/tests/TEST_LOG.md` as an index.

```markdown
# Test report: <game>, <YYYY-MM-DD>

## Summary
1. Verdict: <READY TO PUBLISH | NOT READY: n critical | MILESTONE PASSED | MILESTONE FAILED>.
2. Passed <n> of 8 areas; failed: <list or "none">; not run: <list or "none">.
3. Worst problem: <one plain sentence, or "none found">.
4. First-time players: <n of 3> reached the fun, median <s> s; main confusion: <one phrase>.
5. Left unfixed: <count and one phrase, or "nothing">.

## Run
- Run type: quick check | milestone | pre-publish
- Studio window: <name>, identity attribute confirmed: yes/no
- DataStore: original `<name>`, test `<name>`, live guard confirmed at Phase 0 / 4 / 6: yes/yes/yes, restored and verified in edit mode: yes (anything else is Critical)
- PlaceId: <id or 0 (unpublished)>

## Areas
| Area | Phase | Verdict | Evidence |
|---|---|---|---|
| Unit tests | 1 | PASS/FAIL/NOT RUN (reason) | `[SUMMARY] 84 run, 84 passed, 0 failed` |
| Agent playthrough | 2, 3 | | screenshots p3-*.png, 3 rounds, 0 errors |
| Multiplayer | 5 | | |
| Phone | 8 | | matrix-*.png, UI scan results |
| Lag | 7 | | |
| Performance | 9 | | numbers vs budget and baseline |
| Exploits | 6 | | remote table below |
| Saving | 4 | | profile A vs B diff |

## First-time player
| Tester | Understood goal | First core action | First reward | Would quit at | Stuck? |
|---|---|---|---|---|---|
| 1 | 0:42 | 0:58 | 2:31 | never | no |

Recurring confusion: <points seen in 2 or more testers>.
Tool limits that may have affected this: <BillboardGui cues, click quirks>.

## Bugs (worst first)
| # | Severity | Area | What happens | Evidence | Status |
|---|---|---|---|---|---|
| 1 | Critical | Exploits | `SellItem` with `0/0` sets coins to NaN | log line, state diff | fixed (round 1) |

## Remote table
<from testing-exploits>

## Performance baselines
<numbers to compare against next time>

## Left unfixed
<each item: severity, what it is, what was tried, what the user needs to decide>

## Waivers
<anything the user explicitly accepted, with date>
```

The 5-line summary is plain language. No jargon the user would have to look up.

## Output
1. Write `TEST-REPORT.md` from the template above, with every area filled in and every bug ranked worst first. Save all evidence in the same run folder.
2. **Present an overview in chat.** The file is the detail; the chat overview is what the user actually reads. Give them:
   - the 5-line summary, as written in the report
   - "Left unfixed": each item in one plain sentence, with its severity and what they need to decide
   - the path to the full report

   Nothing else unless they ask. Don't paste the whole report, the tables or the logs into chat.
3. If any Critical bug is unfixed, say clearly in the chat overview that publishing is blocked, and why.
