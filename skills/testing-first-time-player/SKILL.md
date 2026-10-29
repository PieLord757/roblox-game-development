---
name: testing-first-time-player
description: How to run blind first-time-player tests on a Roblox game with fresh agents that can only see screenshots and send input. Includes the restricted agent definition, the exact prompt, calibration, what to measure (time to understand the goal, first core action, first reward, confusion, stuck points, would-quit moment), and how to turn results into fixes. Use in Phase 10 of every milestone test run and before every publish.
---

# First-time-player test

Load `testing` first. This is Phase 10 of a test run.

## Why
The build thread knows where everything is, so it can't see what a new player can't see. A blind tester that has never seen the source, the design doc or the dev hooks shows where a real first-time player gets lost. It measures the most important number for a Roblox game: **how long until it's fun.** Players who don't find the fun in their first minutes don't come back.

**Limits, so you read the results honestly:**
- An agent reads text more patiently than a 13-year-old and can't feel controls. Its confusion is a **lower bound**: if it's confused, real players are more confused.
- It is not a fun verdict. Whether the game is fun still needs a person.
- It can't see BillboardGuis or Highlights in captures. Onboarding that depends on them must be checked separately (see calibration).
- The game keeps running while the agent thinks, so its seconds are much slower than a human's. Server time measures model latency as much as onboarding. **Pass criteria therefore use action counts.** Server time-to-fun is still recorded and reported, and compared across runs of the same game.
- Timed intros, countdowns and prompts that vanish may expire between the tester's screenshots. If a tester missed one, check whether it was on screen long enough for a human before calling it a game bug.

## Blindness is enforced by tools, not by asking nicely
A general subagent told "don't look at the code" isn't blind. It has seen the conversation, and it can read files. The tester must be a **custom agent definition whose tool allowlist holds only screenshot and input tools.** No `Read`, no `Bash`, no `script_read`, `get_script_source`, `grep_scripts`, `execute_luau` or `eval_*`.

If `.claude/agents/blind-playtester.md` doesn't exist in the project, create it with this content. Adjust the tool name prefixes to match the MCP server names in your session.

```markdown
---
name: blind-playtester
description: A first-time Roblox player who has never seen this game. Plays only through screenshots and input, then reports confusion, stuck points and timings. Used by the testing-first-time-player skill.
tools: mcp__robloxstudio__capture_screenshot, mcp__Roblox_Studio__screen_capture, mcp__robloxstudio__simulate_keyboard_input, mcp__robloxstudio__simulate_mouse_input, mcp__Roblox_Studio__character_navigation, mcp__Roblox_Studio__user_keyboard_input
---

You are a player trying a Roblox game for the first time. You only know what a
player would know: what is on the screen and what you are told in your brief.
You cannot read code, files or game state. Play honestly: don't guess at
developer intent, react to what you see.
```

## Step 1: prepare (the orchestrator does this)
1. Phase 0 is done and the store guard passed. Start a fresh solo session (`solo_playtest action=start mode=play`), on the desktop viewport, with no device simulator and no network profile.
2. **Check that funnel timestamps work.** The game's dev hooks should record, on the server, the first time each player reaches: joined, first core action, first reward, and any other onboarding steps in the design. Read them once with `eval_server_runtime` to confirm they reset for a new player. If they don't exist, add them before testing, or the timings will be guesses.
3. **Calibrate input.** Take a `capture_screenshot`, click the main menu button at its screenshot coordinates with `simulate_mouse_input`, and confirm with `eval_client_runtime` that it registered. Write down what you learn:
   - Buttons that act on `Activated` may fire only on every other synthetic click. Buttons that act on `InputBegan` fire every time.
   - Mouse coordinates may include the 58 px top-bar inset.
   - If the main buttons don't respond to synthetic clicks at all, the test can't run fairly. Fix the input path or report the area as NOT RUN.
4. **List tool-blind cues.** Note every onboarding cue that uses a BillboardGui or Highlight (arrows over objectives, glowing targets). The tester can't see them; check them yourself by reading their properties, and don't score the tester's confusion at those points as a game bug without checking.
5. **Write the brief inputs,** and nothing else:
   - The store description, exactly as a player would read it on the game page.
   - The controls a player would know: standard Roblox movement (WASD, Space, mouse) plus any controls the game itself shows on screen. Don't explain the goal or the UI.
   - The tool plumbing: the `instance_id` and `studio_id` of your Studio window (from `get_connected_instances` and `list_roblox_studios`), and the input notes from calibration (for example "mouse coordinates are screenshot pixels" or "add 58 to y"). This is not game knowledge, so it doesn't break blindness. Without it, a tester may drive the wrong Studio window.
6. **Dry run.** An agent definition created mid-session may not be available as a `subagent_type` until the session restarts, and its MCP tools may need loading. Before tester 1, start one `blind-playtester` with the prompt "Take one screenshot with capture_screenshot and describe it in one sentence." If the agent type isn't found, or it can't call its tools, stop and tell the user (a session restart usually fixes it). **Never fall back to a general-purpose agent;** it isn't blind.

## Step 2: run 3 testers, one after another
- **One fresh Agent call per tester** with `subagent_type: "blind-playtester"`. Never continue a previous tester with SendMessage; it has already learned the game.
- **Sequentially, never in parallel.** Testers driving one Studio at once fight over the camera and input.
- **Reset between testers:** stop Play, clear the tester's test profile (test store only), start Play fresh. Each tester must start as a brand-new player.
- Note the server clock (`os.clock()` via `eval_server_runtime`) right before each tester starts, so you can line up its log with the server timestamps.

### The exact prompt
Give each tester this prompt, filling only the three placeholders. Add nothing about the game.

```text
You just found a Roblox game on the home page and joined it. You have never
played it before. This is everything you know:

Game page description:
"""
<STORE DESCRIPTION, VERBATIM>
"""

Controls you know: <STANDARD ROBLOX CONTROLS, PLUS ANY THE GAME SHOWS ON SCREEN>

The game is already running in Roblox Studio. You can only:
- take screenshots with capture_screenshot (use screen_capture if a frame is
  black or doesn't change),
- press keys with simulate_keyboard_input,
- click with simulate_mouse_input, using pixel coordinates from your most
  recent screenshot,
- walk to a spot with character_navigation.

Tool setup (not about the game): <INSTANCE_ID, STUDIO_ID AND INPUT NOTES FROM CALIBRATION>
Pass these ids on every tool call.

Play for 40 actions. An action is one key press, click or walk.

Rules:
1. Take a screenshot before every action, and describe what you see.
2. After every screenshot, write one line: what you think you are supposed to
   be doing right now, in your own words. If you don't know, write
   "I don't know what to do".
3. If a click seems to do nothing, try it once more before deciding it is
   broken.
4. Don't assume anything you can't see on screen. If text is unclear, say what
   you thought it meant.
5. Act like a real player: if you would give up, say "I would quit here" and
   why, then keep playing so we can see what happens next.

When you finish, return this report:

ACTION LOG
One line per action: action number, what you did, what you saw, what you
thought you were supposed to do.

TIMELINE (action numbers)
- Understood the goal at action: <n>, in my words: "<goal>"
- First did the main thing the game is about at action: <n>, which was: <...>
- First got a reward or felt progress at action: <n>, which was: <...>
- Would have quit at action: <n or "never">, because: <...>

CONFUSION
Every moment you didn't know what to do, misread something, pressed
something that did nothing, or went back and forth. Action number and what
happened.

STUCK
Any point where you could not find a way forward at all.

FIRST IMPRESSION
Three honest sentences: what you think this game is, whether you would keep
playing, and the single thing that would have helped most.
```

## Step 3: measure (the orchestrator does this)
After each tester returns, read the funnel timestamps with `eval_server_runtime` and combine them with the tester's log.

| Measure | Source |
|---|---|
| Time to understand the goal | the tester's "understood the goal" action number, matched to the clock |
| Time to first core action | server funnel timestamp (truth), cross-checked with the tester's log |
| Time to first reward ("time to fun") | server funnel timestamp |
| Actions to first core action and first reward | the tester's action log |
| Confusion points | the tester's CONFUSION list, plus signals in its log: "I don't know what to do", walking back and forth, opening and closing the same menu, pressing keys that do nothing, dying in the same place twice |
| Stuck points | the tester's STUCK list, and any funnel step never reached |
| Would-quit moment | the tester's timeline |
| Misread text | anything it described differently from what the text means |

Also check the tester's stated goal against the real goal. A tester that "understood" the wrong goal is a confusion point.

### Pass criteria
These targets come from the industry rule of thumb that a player should reach core play within about 60 to 90 s, converted to actions because agent seconds aren't human seconds. Tune them per game in `studio-profile.md` if the studio has its own.
- At least 2 of 3 testers reach the first core action within 10 actions and the first reward within 25 actions.
- No confusion point recurs in 2 or more testers.
- No tester gets stuck with no way forward.

## Craft: turning results into fixes
- **Recurring confusion is a design bug, not a tester problem.** One tester confused might be noise. Two at the same spot is the game. File it at least Medium; a dead end is High.
- **Fix the earliest drop first.** Confusion at action 3 hides everything after it.
- **Prefer showing over telling.** The usual fix is a clearer target in the world, a prompt in context at the moment it's needed, or removing a step, not a longer tutorial text. Check the fix against the `de-ai-story` rules if the project has them.
- **Get to the fun faster.** If the first reward is slow, lower the first threshold, hand out a starter item, or move the first big moment earlier.
- **Re-test with new testers.** After a fix, run fresh testers. Never reuse one that already played.

## Common mistakes
- Giving the tester a "helpful" hint about the goal. That ruins the test. The brief is the store description and the controls, nothing more.
- Using a general-purpose subagent with a "please don't peek" instruction.
- Running testers in parallel on one Studio.
- Scoring confusion at a BillboardGui cue as a game bug without checking whether it was a tool blindness.
- Trusting the tester's own sense of time. Use server timestamps.
- Treating "the agent had fun" as proof the game is fun.

## Output
1. Write the results into the run's `TEST-REPORT.md` under "First-time player": the per-tester table, recurring confusion, stuck points, tool limits that may have affected the run, and bugs (with severity) in the bug list. Save each tester's full report as `ftp-tester-<n>.md` in the run folder.
2. **Standalone runs only** (when this test is run on its own): give the user a short chat overview. Inside a full `testing-run`, the results go into line 4 of the 5-line summary and the single overview at the end of the run. The overview covers how many of 3 testers reached the fun and how fast (median), the top recurring confusion point in one plain sentence, and any dead end.
