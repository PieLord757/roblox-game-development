---
name: testing-devices-perf
description: Device, network and performance testing for a Roblox game. Covers the device matrix (phone, tablet, console, smallest screen, portrait), measuring UI in code instead of eyeballing it, network profiles for lag, jitter and packet loss, performance budgets, leak checks, and which numbers can and can't be trusted from Studio. Use in Phases 7, 8 and 9 of a test run, after any UI change, and before every publish.
---

# Devices, lag and performance

Load `testing` first. This skill covers three areas of the report: **phone** (Phase 8), **lag** (Phase 7) and **performance** (Phase 9).

## Part 1: devices and UI (Phase 8)

### The device matrix
Pick devices by archetype, by name from the device list, never by a hard-coded id (ids change).

| Archetype | Why | Orientation |
|---|---|---|
| Latest phone (notch or Dynamic Island) | the biggest share of players; notch and home bar eat edges | landscape |
| Latest phone, portrait | **only if** `StarterGui.ScreenOrientation` is `Sensor` or `Portrait`. Portrait is where layout bugs hide. | portrait |
| Latest tablet | different aspect ratio; offset-sized UI looks tiny | landscape |
| Console (TV) | 5 to 10% overscan per edge, read from about 3 m, gamepad only | landscape |
| Lowest-resolution device (about 800×360) | offset-sized UI runs off-screen here first | landscape |
| VR (optional) | nearly square view | n/a |

### Tools
- `capture_device_matrix` (up to 6 entries, with `target` and `settleSeconds`): screenshots of several devices in one call. Save as `matrix-<device>.png`.
- `set_device_simulator` (target `edit`, `client-N` or `all-clients`): switch a device during a playtest. It works during Play because it targets the client.
- `get_device_simulator_state`, and `reset_simulation_state` to clean up.
- The built-in `rbx-device-simulator-lua` skill covers `StudioDeviceSimulatorService` through `execute_luau`. Its setters error during Play on the server, so set the device before Play when using it. Wait 0.2 s after each setter.
- **No synthetic mouse input arrives while the Device Simulator is active.** Check layout under the simulator, and check input separately on the desktop viewport.
- BillboardGuis and Highlights don't show in captures. Check world-space UI by reading properties, not by looking.

### Measure, don't eyeball
At each device, during Play, walk every visible `GuiObject` in `PlayerGui` from `eval_client_runtime` and flag:

| Check | How | Fail when |
|---|---|---|
| Off-screen | compare `AbsolutePosition` and `AbsoluteSize` with `workspace.CurrentCamera.ViewportSize` | any part of an interactive element is outside, ±2 px |
| Truncated text | `TextFits` | `false` on any core HUD or menu label |
| Small touch targets | `AbsoluteSize` of buttons | either side under 44 px |
| Overlaps | rectangle intersection between interactive elements | two interactive elements overlap |
| Under the inset | compare with `GuiService:GetGuiInset()` and the device safe area; `ScreenGui.ScreenInsets` | interactive element under the notch, home bar or top bar |
| Console overscan | outer 5% of each edge | anything interactive there |
| Under thumb controls | the default jump button (bottom right) and thumbstick (bottom left) areas | an important button underneath them |

Only count elements that are actually visible: walk up the ancestors and check `Visible` and the `ScreenGui`'s `Enabled`. Save the scan output as JSON in the run folder.

**Insets:**
- Interactive UI should use `DeviceSafeInsets` or `CoreUISafeInsets`. `None` is for background art only.
- With `IgnoreGuiInset = true`, keep the HUD below the 58 px top bar.
- Legacy chat can cover a top-left HUD.

**Text size:** `GuiService.PreferredTextSize` is read-only and can't be set in Studio. Check in code: every text element on the HUD and menus either uses `TextScaled` or listens to `GetPropertyChangedSignal("PreferredTextSize")`. If not, it needs a manual check on a real device at the largest setting, with a written waiver until then.

**Gamepad:** every interactive button is `Selectable` and reachable through `GuiService.SelectedObject` navigation, and nothing depends on hover. The Controller Emulator helps.

**Touch keyboard:** a focused TextBox must not sit under the on-screen keyboard (`PortraitKeyboardHeight` and `LandscapeKeyboardHeight` in the device info).

### Craft: what makes UI break on devices
- **Offset sizes.** `UDim2.fromOffset(400, 80)` fits a laptop and runs off an 800×360 phone. Use Scale with `UIAspectRatioConstraint` or `UISizeConstraint`.
- **Horizontal lists** overflow narrow screens. Check the widest row on the smallest device.
- **A UIScale on a full-screen root** shrinks the root itself; set the root's size to `1/k`.
- **Corners are taken.** Top left has the Roblox menu, top right has core buttons, bottom corners have the thumbstick and jump button on touch.
- **The main action** belongs within thumb reach on the right side for touch, and never at the very edge.

## Part 2: lag (Phase 7)

### Profiles
- `set_network_profile` with `profile=poor` and `target=all-clients`.
- Then `profile=custom`: about 250 ms inbound and outbound delay, about 50 ms jitter, and loss at the schema maximum. (The schema caps loss at 0.5; whether that's a fraction or a percent isn't documented, so record the value you used.)
- Confirm with `get_simulation_state`. Finish with `reset_simulation_state`.

### What to run
Re-run the Phase 3 loop solo, plus the late-join part of Phase 5, under each profile. Then play the core action yourself for a minute and note anything that feels wrong.

### What to look for
- The loop still completes.
- **No stuck "waiting" UI.** Every RemoteFunction has a timeout or fallback; every spinner ends within 10 s.
- **No double actions.** A player who clicks twice because nothing happened must not buy twice. Fire the remote twice quickly under lag; the server must be idempotent and the button debounced.
- **Legitimate players aren't rejected.** Server distance and timing checks need slack for lag. A laggy honest player failing a hit or pickup check is a High bug.
- UnreliableRemoteEvents carry only data that can be lost.
- If `Workspace.AuthorityMode` is `Server`, check prediction and rollback under `poor`: input delay and snapping.

**PASS:** all of the above hold under both profiles.

## Part 3: performance (Phase 9)

### What to capture
During the scripted loop with 3 clients:
1. `capture_script_profiler` with `target=server`, `duration_ms=10000`, then the same for `client-1`. Top functions by time.
2. `capture_micro_profiler` with `action=capture`, `target=server`, `spike_frames=3`, and a `summary_output_path` in the run folder. Pass `baseline_path` pointing at last run's summary to compare.
3. `get_memory_breakdown` with `target=all` after round 1 and after round 3.
4. `get_scene_analysis` with `mode=unparented_instances` after rounds 1 and 3 (finds leaks directly). Also `instance_composition`, `triangle_composition` and `audio_memory` once per milestone.
5. For deep analysis, load the built-in `rbx-perf-profiling` skill. Annotate suspect code with `debug.profilebegin` and `debug.profileend`.

### Budgets
These are rules of thumb unless marked as Roblox guidance. Tune them per game in `studio-profile.md` if the studio has its own.

| Metric | Budget | Source |
|---|---|---|
| Server frame time | ≤ 16.67 ms outside spike frames (heartbeat about 60) | Roblox guidance |
| Any one game function | ≤ about 2 ms per frame on average | rule of thumb |
| LuaHeap, round 3 vs round 1 | within about 10% | rule of thumb |
| Instance count, round 3 vs round 1 | within about 10% | rule of thumb |
| Unparented instances | not growing | rule of thumb |
| Server memory | under 50% of about 6.25 GiB + 100 MiB × peak players | Roblox guidance |
| Textures | none over 1024²; aim for 512² (256² for minor images) | Roblox guidance |
| Remotes | none fired every frame | rule of thumb |
| Regression vs baseline | no metric worse by more than 20% | rule of thumb |

### What you can't trust
- **Client frame times from a Studio window that isn't in front.** Background windows render at about 15 fps. Use script cost instead: script profiler totals, or `os.clock()` around the work.
- **Mobile performance.** Studio on a desktop can't emulate a phone's CPU or GPU. Use proxies (script time, draw calls, shadow-casting lights, texture sizes, StreamingEnabled, a stable heap), and keep "real-device phone check still needed" in the report until a person checks on a phone.
- **Averages with one big spike.** A single 600 ms stall dominates an average. Analyze spikes separately from steady state.

### Craft: where performance goes
- Work in `Heartbeat`, `RenderStepped` or `PreRender` that doesn't need to run every frame. Spread big work across frames.
- Connections that are never disconnected, and player tables never cleared on `PlayerRemoving`. These grow every round, which is why you compare round 3 with round 1.
- Unanchored static parts, precise collision on decoration, `CastShadow` on hundreds of small parts, and `CanTouch` left on where nothing listens.
- NPCs with every Humanoid state enabled. Disable unused states, use an AnimationController for static NPCs, and pool NPCs.
- Server-side tweens replicate every frame. Tween on the client.

## Common mistakes
- Eyeballing a phone screenshot and calling it fine. Run the scan; screenshots miss a button 10 px under the notch.
- Testing input under the Device Simulator and concluding a button is broken. Input doesn't arrive there.
- Testing only landscape when the game allows portrait.
- Quoting background-window FPS as evidence.
- Profiling an idle lobby. Profile during the busiest moment of the loop with 3 clients.
- Forgetting `reset_simulation_state`. The next test inherits your lag and device.

## Output
1. Write the matrix screenshots, scan JSON, profiler summaries and memory numbers to the run folder, and the verdicts for phone, lag and performance (with numbers against budget and baseline) into `TEST-REPORT.md`. Record this run's numbers under "Performance baselines" for next time.
2. **Standalone runs only** (for example a UI-change check): give the user a short chat overview. Inside a full `testing-run`, these results go into the single overview at the end of the run instead. The overview covers which devices passed, the worst layout problem in one sentence, whether the game holds up under lag, and the key performance numbers against budget.
