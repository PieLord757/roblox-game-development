---
name: level-design-roblox
description: Roblox-specific level building. Character metrics and how to measure your own rig, the grey blockout workflow in Studio through the MCP tools (grid, colors, folders, top-down and five-second screenshots, timed walk tests), terrain vs parts, modular kits and Packages, StreamingEnabled settings and streaming boundaries, draw-call, texture and memory budgets, lighting technology and low-quality fallbacks, PathfindingService for bot routes and cover tagging, and set-piece implementation. Use while blocking out, building, optimizing or adding bots to any space.
---

# Level design: Roblox

Load `level-design` first for the process and the gates, and `level-design-craft` for the design decisions. This file is how to build it in Roblox. Rules have IDs (LR1 to LR16).

Evidence tags:
- **[doc]** comes from the Roblox Creator Docs.
- **[derived]** is computed from engine defaults. Recompute it if the game changes the Humanoid.
- **[observed]** is a pattern seen in practice. Test it.

Before relying on any property or method named here, check it with `get_roblox_docs`. Engine APIs change.

## 1. Metrics
Engine defaults [doc]: WalkSpeed 16 studs/s, JumpHeight 7.2 studs (JumpPower 50), Gravity 196.2 studs/s², MaxSlopeAngle 89°. A default R15 character is about 5 studs tall and about 2 studs wide at the shoulders.

Derived from the defaults [derived]: launch velocity about 53 studs/s, airtime about 0.54 s, horizontal jump distance at walk speed about 8.7 studs.

**LR1 Measure your own rig and speeds before blocking out.** Most games change walk speed, add a sprint, or use custom rigs. Start a `solo_playtest` and run this with `eval_server_runtime`:

```lua
local player = game.Players:GetPlayers()[1]
local char = player.Character
local hum = char:FindFirstChildOfClass("Humanoid")
local g = workspace.Gravity
local jumpHeight = hum.UseJumpPower and (hum.JumpPower ^ 2) / (2 * g) or hum.JumpHeight
local launch = math.sqrt(2 * g * jumpHeight)
local airtime = 2 * launch / g
return {
	walkSpeed = hum.WalkSpeed,
	jumpHeight = jumpHeight,
	airtime = airtime,
	jumpDistanceAtWalk = hum.WalkSpeed * airtime,
	characterSize = tostring(char:GetExtentsSize()),
}
```

Then fill in the metrics table with the game's numbers. The defaults below assume walk 16 and sprint 24.

| Metric | Default value | Why |
|---|---|---|
| Required gap jump | ≤ 6 studs (sprint 24: ≤ 9) | leaves about 30% tolerance for real players and lag |
| Required ledge climb by jumping | ≤ 5 studs | 7.2 is the theoretical maximum; leave margin |
| Wall that must stop jumping | ≥ 9 studs; 12 for hard bounds | plus margin for tools and tricks |
| Corridor, third-person camera | min 6, comfortable 8-10 studs | narrower and the camera collides and pops in |
| Corridor, two players passing or PvP | ≥ 10-12 studs | |
| Ceiling, third person | ≥ 10-12 studs | low ceilings force the camera in; use them on purpose for dread, or lock first person there |
| Doors | 4-6 wide, 8-9 tall | reads human-scale for 5-stud avatars; bot-used doors see section 8 |
| Stairs | 1-stud rise per step, or a wedge ramp under decorative steps | prevents snagging |
| Full cover (hides a standing character) | ≥ 6 studs tall | |
| Half cover | about 3 studs | only meaningful with a crouch |
| Travel time | 160 studs ≈ 10 s at 16 studs/s | plan a beat every 15-40 s (LC1) |

**LR2 Put the metrics in one shared ModuleScript** (for example `ReplicatedStorage.LevelMetrics`) so every builder, script and bot uses the same numbers, and write the measured values into `LEVEL-PLAN.md`:

```lua
return {
	Grid = 5,
	WalkSpeed = 16, SprintSpeed = 24,
	MaxGap = 6, MaxGapSprint = 9, MaxLedge = 5,
	BlockingWall = 9, HardBoundWall = 12,
	CorridorMin = 6, CorridorComfort = 8, CorridorPvP = 10,
	CeilingMin = 10, DoorWidth = 5, DoorHeight = 9,
	FullCover = 6, HalfCover = 3,
}
```

Design in studs and seconds, not meters. The docs treat 1 stud as about 0.28 m at avatar scale, but gravity and jump arcs are game numbers, not real ones.

## 2. The blockout workflow in Studio
The blockout is cheap on purpose. It tests pacing, routes, sightlines, jumps and timing before anything costs real effort.

**LR3 Blockout conventions:**
- Snap to a **5-stud grid and 90° rotations** while blocking out, the same as the Roblox environmental art curriculum. [doc]
- Plain parts in **two neutral greys** (lighter floors, darker walls) with `SmoothPlastic`, plus **one reserved accent color** for interactables and climbables, the same hue the final art will use (LC6). Never put the accent on anything else.
- One Model per space, one Folder per area inside it: `Workspace.Blockout.<Space>.<Area>`. (The space is a Model so `GetBoundingBox` works for the top-down shot.) Roofs and ceilings get `BlockoutRole = Roof` so they can be hidden for top-down shots.
- Mark roles with attributes, not names alone: `BlockoutRole` = `Floor`, `Wall`, `Roof`, `Interactable`, `Landmark`, `Spawn`, `Cover`, `Beat`. Number beats with an `Order` attribute so scripts can walk the critical path.
- Landmarks get a distinct shape and size even in grey. If the landmark only works once textured, it is not a landmark yet.
- Anchor everything. No scripts beyond what the test needs (doors that open, a moving hazard stand-in).

Build with `execute_luau` in edit mode for repeated or measured geometry (corridors to metric widths, a ring of cover, a row of rooms), and `multi_edit` or `manage_instance` for one-offs. A small helper keeps it on grid:

```lua
local GRID = 5
local function snap(v) return Vector3.new(
	math.round(v.X / GRID) * GRID, math.round(v.Y / GRID) * GRID, math.round(v.Z / GRID) * GRID) end
local function block(parent, name, size, pos, role, color)
	local p = Instance.new("Part")
	p.Name, p.Anchored, p.Material = name, true, Enum.Material.SmoothPlastic
	p.Size, p.Position = size, snap(pos)
	p.Color = color or Color3.fromRGB(163, 162, 165)
	p:SetAttribute("BlockoutRole", role)
	p.Parent = parent
	return p
end
```

**LR4 The top-down screenshot.** The plan's top-down sketch must be replaced or confirmed by a real straight-down view of the blockout. In edit mode with `execute_luau`:

```lua
-- hide roofs (remember each part's transparency), then point the camera straight down
for _, p in workspace.Blockout.MySpace:GetDescendants() do
	if p:IsA("BasePart") and p:GetAttribute("BlockoutRole") == "Roof" then
		p:SetAttribute("SavedTransparency", p.Transparency)
		p.Transparency = 1
	end
end
local cam = workspace.CurrentCamera
local cf, size = workspace.Blockout.MySpace:GetBoundingBox()
cam.FieldOfView = 20 -- narrow field from high up gives a near-orthographic view
local height = math.max(size.X, size.Z) / (2 * math.tan(math.rad(cam.FieldOfView / 2))) + size.Y
cam.CFrame = CFrame.new(cf.Position + Vector3.new(0, height, 0)) * CFrame.Angles(-math.pi / 2, 0, 0)
```

Then `screen_capture`. **Put the roofs back afterwards** (set each roof part's `Transparency` back to its `SavedTransparency` attribute and clear the attribute) and restore the camera's field of view to 70. Never leave a place with hidden geometry. Annotate the screenshot (or the grid sketch in the plan) with the critical path, the beats and the landmarks.

**LR5 The five-second shots.** For each area, put the camera at eye height (about 4.5 studs above the floor for a default character) in the entrance, facing in, and capture. Each shot must answer: where is the exit, where is the landmark, what matters here. If you can't answer from the shot alone, fix the lighting or framing before showing anyone. Use `selection` with `action=view` or set `CurrentCamera.CFrame` directly.

**LR6 The timed walk.** In a `solo_playtest`, walk the critical path through the `Beat` markers in order with `Humanoid:MoveTo` from `eval_server_runtime` (or `character_navigation`). Record the time for each segment inside the call, not across calls: each MCP call costs 1-3 s of game time. Keep each call under about 25 s and walk the path in several calls. Compare the times to the beat list; any gap over 40 s of travel without a beat is a finding. Test every required jump at the documented metric with a real jump, not by reading the numbers.

Gotchas (from `testing`):
- The first frame after Play is often black. Retake it after 2 s.
- BillboardGuis do not show in captures, so do not label the blockout with billboards for screenshots. Annotate the image afterwards or use colored parts.
- A Studio window in the background renders at about 15 fps; its frame times are not evidence.
- Close the playtest when done (`solo_playtest stop`, then `reset_simulation_state`).

**LR7 Iterate at least three times** (LG3). Each iteration: change, re-walk, re-shoot, and write one line in the plan's iteration log saying what changed and why.

## 3. Terrain vs parts
Terrain is 4×4×4-stud voxels with materials. It is cheap for large organic areas, blends without seams, and can import heightmaps (1 pixel = 4 studs, up to 4096²). [doc]
- **LR8** Use terrain for natural ground, cliffs, caves, rock masses, water and snow. Use parts and meshes for anything architectural, anything with exact metrics, and anything that moves. Never put a critical gameplay edge (a jump, a cover line, a stealth boundary) on terrain; 4-stud resolution is too coarse.
- Terrain water gives free swimming. Design around it or avoid it.
- Terrain grass decoration costs performance on mobile. Use it sparingly.

## 4. Modular kits
The art pass builds from a kit, not from one-off parts. [doc: environmental art curriculum]
- **LR9 Kit rules:**
  - consistent pivot points so pieces snap at fixed increments
  - dimensions divisible by the kit's smallest unit (the curriculum uses 5×5 and 15×5 pieces), matching the blockout grid
  - each piece converted to a **Package** so a fix propagates everywhere
  - each mesh uploaded once and duplicated in Studio; re-importing gives a new mesh ID and breaks instancing
- **Kit contents:** walls (straight, corner, T, door, window), floors and ceilings, stairs and ramps, trim and pipe strips, props, and one hero piece per area (the landmark).
- **Variation without new meshes:** tint through `SurfaceAppearance.Color` or part color, rotation, decals at seams, prop dressing and lighting changes.
- Kits enforce metrics: if the door piece is the right width, every door is.
- Replayable room-chain runs need a kit plus a room pool; each room prefab has an entrance and an exit anchor (an attachment or a part with a known CFrame), the next room is pivoted to the previous exit, and rooms far behind are removed. [observed]

## 5. StreamingEnabled
Facts [doc]: on by default for new places; streams only Workspace descendants. `StreamingMinRadius` default 64 (never streamed out, highest priority), `StreamingTargetRadius` default 1024. Streamed-out instances are parented to nil.

- **LR10 Streaming settings:**
  - Leave StreamingEnabled on.
  - `Workspace.StreamingIntegrityMode = PauseOutsideLoadedArea`.
  - `Workspace.ModelStreamingBehavior = Improved`; consider `StreamOutBehavior = Opportunistic` to save memory.
  - Interactables (doors, puzzles, pickups with parts) are **Atomic** models, so a door never arrives without its handle.
  - **Persistent** only for what must always exist (objective markers, an arena's whole layout); wait for `Workspace.PersistentLoaded` on the client. Use it sparingly.
  - Client scripts must tolerate parts appearing and disappearing: use `WaitForChild` on the model, `CollectionService` instance-added signals, and never cache a part forever.
- **LR11 Put streaming boundaries at occluders.** Corners, doors, airlocks, elevators and tunnels hide stream-in pop, so they are the natural seams between areas. This is one more reason the linear-pearl connectors and the hub's spoke doors exist.
- A PvP arena under about 128×128 studs barely needs streaming; keep it Persistent or within the min radius so no player fights an unloaded wall.
- Distant landmarks disappear past the target radius. For a skyline or a far weenie, use a low-poly Persistent stand-in or `LevelOfDetail = StreamingMesh` imposters on the model.
- Pre-stream before teleports and set pieces with `Player:RequestStreamAroundAsync(position)`.

## 6. Performance: draw calls, textures, memory
Draw calls, not part count, are the main render budget. [doc] There is no official part limit; measure.
- Identical meshes (same mesh, same SurfaceAppearance or texture, same material) instance into one draw call. Decals, textures and particles batch poorly.
- Texture memory scales with pixels: 1024² costs four times a 512².
- Layered transparent parts cause overdraw. Do not stack glass, fog and window parts.

**LR12 Defaults for every decor part** (run over a dressing folder with `execute_luau` after the art pass):

```lua
for _, p in workspace.Level.Decor:GetDescendants() do
	if p:IsA("BasePart") then
		p.CanCollide = false; p.CanTouch = false; p.CanQuery = false
		if p.Size.Magnitude < 4 then p.CastShadow = false end
		if p:IsA("MeshPart") then
			p.CollisionFidelity = Enum.CollisionFidelity.Box
			if p.RenderFidelity == Enum.RenderFidelity.Precise then p.RenderFidelity = Enum.RenderFidelity.Automatic end
		end
	end
end
```

(Collision fidelity on a MeshPart may need to be set in Studio rather than at run time; verify with `get_roblox_docs` and check the result.)

- Textures ≤ 512 for most surfaces, ≤ 256 for minor ones.
- Lights only where they guide or set mood. Shadows only on key lights. Limit light range and count, and switch off lights in areas the player is not in.
- **LR13 Measure the densest area** with `get_scene_analysis`, `get_memory_breakdown` and `capture_micro_profiler`, and at a low-end phone profile with `set_device_simulator` and `capture_device_matrix`. Compare against the budgets in `testing-devices-perf` (frame time, memory, textures) and the level budgets below, and record the numbers in the plan. Studio cannot emulate a phone's GPU, so say "real-device check still needed" until a person has played it on a phone.

**Level budgets.** Roblox publishes no official draw-call or part limit. These are **starting policy**, not doc numbers: record the first measured baseline in the plan, then tune them per game (or in `studio-profile.md`).
| Metric, in the densest view | Starting target |
|---|---|
| Draw calls (Render Stats, Shift+F2 in the client) | about 1,000 or fewer; about 600 if phones are the main audience |
| Shadow-casting lights in view | about 8 or fewer |
| Unique textures in view | as few as the art allows; none over 1024², most 512² or less |
| Stacked transparent layers on any line of sight | 2 or fewer |
| Regression vs the recorded baseline | no metric worse by more than 20% (same rule as `testing-devices-perf`) |

## 7. Lighting technology and guidance that survives low quality
- `Lighting.Technology = Future` gives per-light shadows and the best mood for story spaces; test it on the low-end profile. Arenas and large open maps may prefer a cheaper technology.
- **LR14** Shadows are disabled below graphics quality 4 [doc], so on many phones guidance that depends on shadow shape disappears. Guide with light color, emissive surfaces (Neon or emissive textures) and contrast. Every objective has one emissive element (LC11). Check the five-second shots again at low quality.
- Fog and atmosphere hide draw distance and stream-in, and set mood. Use them on purpose, not as a default haze. [observed]

## 8. PathfindingService for bots
When the game fills empty slots with bots, or has NPC patrols, the bots must use the layout as designed.

- **LR15 Bot routes are part of the blockout, not added after art.** Build a path with the agent's real size:

```lua
local PathfindingService = game:GetService("PathfindingService")
local path = PathfindingService:CreatePath({
	AgentRadius = 2, AgentHeight = 5, AgentCanJump = true, AgentCanClimb = false,
	WaypointSpacing = 4,
	Costs = { Danger = math.huge, Water = 20 },
})
path:ComputeAsync(startPos, goalPos)
if path.Status ~= Enum.PathStatus.Success then warn("NoPath", startPos, goalPos) end
local waypoints = path:GetWaypoints()
```

- **Narrow doors return NoPath.** Pathfinding works on a coarse grid, so a door a player walks through easily can block a bot (the `testing` skill sees the same problem). Make bot-used doors and corridors wider than the player minimum (start at 6 studs and test), or add a `PathfindingLink` through the opening.
- Use `PathfindingModifier` parts to label regions (a `Label` matched in `Costs`, for example "Danger" around a hazard) or mark see-through blockers with `PassThrough`. Use `PathfindingLink` for jumps, ladders and teleports that the grid can't infer.
- **Shape lanes so the cheapest path is the intended one.** If bots ignore a lane, add a cost to the shortcut they prefer rather than adding invisible walls.
- **Tag cover and points of interest** with `CollectionService` and attributes so bot logic reads the level instead of hard-coded positions: tag `Cover` with `CoverHeight` (`Full` or `Half`) and a facing; tag `PowerPosition`, `Flank`, `Pickup`, `PatrolNode` (with `Order` and `WaitTime` for stealth patrols).
- **Test every pair.** In a playtest, compute paths between all spawns, lane nodes and objectives from `eval_server_runtime` and report any that fail. Then watch bots play one full round in a playtest and screenshot where they get stuck.
- Cache waypoints between fixed nodes at server start; recompute only when a door or blocker changes (`path.Blocked`).
- `Humanoid:MoveTo` stops after 8 seconds if the target isn't reached; re-issue it per waypoint.

## 9. Set pieces in Roblox
- **LR16** Pre-stream the area with `RequestStreamAroundAsync` before the trigger. Animate with `TweenService` or constraints (`AlignPosition`, `AlignOrientation`) on anchored or constrained assemblies. Run purely visual motion on the client; keep the server's truth simple (the door is open, the floor is gone). Telegraph with a light and sound change at least 2 seconds ahead (LC15), and put a checkpoint just before.
- Server-side tweens replicate every frame; tween on the client.

## Output
This skill feeds `LEVEL-PLAN.md` and the blockout screenshot sheet; it has no document of its own. Present the work to the user with the chat overview defined in the Output section of `level-design`.

## Common mistakes
- Blocking out at default metrics when the game uses a sprint or a custom rig.
- Leaving roofs hidden, or a camera field of view changed, after a top-down capture.
- Labeling blockouts with BillboardGuis and then wondering why the screenshots are blank.
- Re-importing a kit mesh instead of duplicating it, which silently breaks instancing.
- Critical edges on terrain.
- Interactables streamed Nonatomic, so a door arrives without its button.
- Guidance that only works with shadows on.
- Bots added after art, then the doors are too narrow and the art has to be rebuilt.

## Sources
- Streaming: https://create.roblox.com/docs/workspace/streaming
- Performance: https://create.roblox.com/docs/performance-optimization/improve
- Terrain: https://create.roblox.com/docs/parts/terrain
- Environmental art curriculum (greybox, polished assets, asset library): https://create.roblox.com/docs/tutorials/curriculums/environmental-art ; https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment ; https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets ; https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library
- Character pathfinding: https://create.roblox.com/docs/characters/pathfinding
- Humanoid and StarterPlayer reference pages for the default metrics.
- Community room-chain generator (pattern reference only): https://devforum.roblox.com/t/doors-room-generator-package/3157691
