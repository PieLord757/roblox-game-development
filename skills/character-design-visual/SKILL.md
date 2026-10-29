---
name: character-design-visual
description: "How to visually design Roblox characters that are striking, readable on a phone, and not AI-looking: silhouette, shape language, proportion, read order, colour and value, costume, the AI-look tells to avoid, and runnable Studio checks (silhouette, distance, grayscale, lineup) with Luau. Use when designing, iterating on, or checking how any character, NPC, or monster looks."
---

# Character design: visual

Load `character-design` first for the process and the rule index. This skill owns rules **V1 to V10** and teaches the craft behind them.

## The idea in one paragraph
A character is read in layers, fast to slow: **colour mass** (friend, foe, team), then **silhouette** (role, threat), then **detail** (personality, story). Design in that order. If the flat black shape doesn't say who this is, no amount of texture will. On a phone at play distance, a character is often 20 to 50 points tall, so only the outline, one or two big colour masses, a bright point of light, and motion survive. Spend the design where the camera can see it.

## 1. How to design a striking character (the craft)

### Start from the job, not the look
Write three lines before drawing anything:
- **What the player must know in 1 second** (usually: threat or not, friend or not).
- **In 3 seconds** (role: the one who heals, the one who chases, the one who sells).
- **In 10 seconds** (personality: the nervous one, the vain one).

The loudest contrast in the design goes on the 1 second read. For a monster that is usually the threat state (is it hunting?), not its anatomy.

### Pick one primary trait and exaggerate it (V5)
Every great game character has **one** thing you'd draw first: TF2's Heavy is mass, the Scout is lean speed, the Medic is a long coat. Pick the trait that carries the character's job or personality, exaggerate it far past realism, and keep everything else quiet. Write it down; it never changes across skins, variants or redesigns (the Riot rule).
- The trait should come from the world. A desert survey camp's cook might carry a permanent lean from hauling water drums; a suburban crossing guard's might be a stop paddle so tall it is part of her outline. A trait borrowed from the trope shelf (hood, mask, katana) says nothing about this world.

### Shape language (V6)
| Shape | Reads as |
|---|---|
| Circle | soft, harmless, approachable, changeable |
| Square | solid, dependable, stubborn, immovable |
| Triangle | sharp, dynamic, dangerous, unpredictable |

- Give each character **one dominant shape** (roughly 60% or more of the silhouette area) and one secondary shape. Write both down and what each means for this character.
- For triangles, **where the points aim** matters. Points aiming at the player threaten; points aiming up are ambition or alarm; too many points muddy the message.
- **Spread the cast across shapes.** If everyone is triangle-dominant, nothing reads as dangerous, because everything does.
- **Subversion is allowed if written down:** a round, soft character who is the real villain is a strong choice. Note which shape it is and what it hides.
- Echo the outline inside: folds, seams and panel lines should repeat the silhouette's shapes (TF2's rule), so detail reinforces the read rather than fighting it.

### Proportion is your cheapest tool
Roblox's default avatar proportions are the most common character shape on the platform. A cast at default proportions is invisible.
- Vary across the cast in **head-to-body ratio**, **mass distribution** (top-heavy, bottom-heavy, even) and **height**, not only clothes.
- Exaggerate the one trait; leave the rest near neutral so the trait stands out.
- Facing direction must read from the silhouette (a nose, a hat brim, a hunch, a lantern held forward), so the player can tell approaching from leaving.

### Iterate on silhouettes, don't settle on the first
The first silhouette is usually the average one. The process that beats it:
1. **Block out 3 to 5 versions** of each major character from primitives (parts or `generate_procedural_model` with named parts). Each one pushes a different idea: one exaggerates height, one mass, one the head, one a held object, one a non-humanoid posture.
2. **Black them out** with the V1 script and put them side by side.
3. **Squint test:** shrink the screenshot to the phone size from V2. Which ones still say something?
4. Keep the strongest, then **push it 20% further** in the direction that made it work, and black it out again. Most good designs come from the second or third push, not the first idea.
5. **Kill your darling if it collides.** If it reads like another cast member (V4), or like a famous character, change the primary trait, not the shirt.

### Colour and value (V7, V10)
- **Colour comes from the game's palette.** Every character hex comes from `ART-DIRECTION.md`. A new colour is added there first, with a role (V10).
- **Saturation is a budget.** Muted colours dominate; small areas of saturation sit at the 1 second read (head, chest, threat feature, a lantern). Saturated everywhere is noise; all-grey "gritty" with no accent is mud.
- **Value structure:** darker lower body, higher-contrast upper torso and face, so the eye lands where information is (TF2's read order).
- **Shadows are tinted, never black.** No `#000000` on characters. Cool shadows and warm highlights give form without outlines.
- **Separate from the background by value**, not by outlines. Test it on every map or area where the character appears; a colour that reads in one room vanishes in another.
- **One big colour mass reads best at distance.** Busy value patterns (lots of small light and dark patches) collapse into grey at 20 points.
- **Threat colour is a choice, not a default.** Saturated red at hue 20 to 45 is the most overused danger signal (see D3 in `character-design`). Consider a value inversion, a light behaviour (flicker, colour-temperature shift), a pattern, or a sound-first cue instead.

### Costume tells a story (V8)
Every visible costume element answers **"why is this on this person?"** with something from their job, history, status or secret.
- A borrowed hat implies who they've been with. A sleeve worn through at one elbow implies a desk job. A badge one rank below what their age suggests implies a story.
- **Anything that can't answer the why is decoration, and decoration is where AI-looking noise comes from.** Delete it.
- Concentrate detail in one focal area (usually chest or head). Leave the rest calm.

## 2. Weak vs strong (before and after)
These show principles. Do not reuse them.

| Weak (the average) | Why it fails | Strong (the same character, designed) |
|---|---|---|
| "Mysterious hooded stranger in a dark cloak with glowing eyes" | Every model's default. The hood hides the head, the best read area. Glowing eyes are the most-used monster tell. Nothing about this world. | A school janitor who is 1.5x too tall for the corridors, so he stoops permanently; a ring of keys the size of a dinner plate swings at his hip when he walks. Dominant shape: a tall thin rectangle bent into a hook. Read at 1 s: the hook silhouette. |
| A cast of four at default R15 proportions, one in red, one in blue, one in green, one in yellow | Colour-swapped avatars. In flat black, all four are identical (V4 fail). | Same four roles, but one is a squat circle (head 1/3 of height), one a tall triangle, one a wide square with a short head, one hunched with a long reach. Colour then carries team, not identity. |
| A "scary monster": teeth, claws, spikes, red eyes, hunched | The statistical average monster. No rule, no cue, nothing specific. | A monster whose only visible feature is a lamp it carries at knee height; the light sweeps the floor before it rounds a corner. The 1 s read is the sweeping light, which is also the gameplay cue. |
| Shopkeeper covered in belts, pouches, straps, a scarf, gloves, goggles | Over-detailing with no hierarchy. Nothing answers the why. | Shopkeeper with one oversized ledger chained to her wrist and ink stains up one forearm. Everything else plain. |
| Hero texture: high-detail fabric everywhere, glossy highlights | Detail is invisible at 30 points and the gloss reads as plastic AI art. | Flat palette colours in three values, one hand-painted detail on the chest emblem, matte materials. |

## 3. Phone-distance readability (V2)
**Camera math (estimate, measure for real):** at the default 70 degree vertical FOV, the visible height at distance `d` studs is about `1.4 x d` studs. A 5 stud character on a landscape phone with about 390 points of height is roughly `1390 / d` points tall:

| Distance (studs) | On-screen height on a phone |
|---|---|
| 12.5 (around default follow distance) | about 110 pt |
| 30 | about 45 pt |
| 60 | about 23 pt |
| 100 | about 14 pt |

At about 20 points only the outline, one or two colour masses, a bright emissive point, and motion survive. Faces, logos, belts, straps, small accessories and texture detail do not. This is why the best Roblox monsters lean on light, sound and motion.

**Separation tools:** value contrast against floor and walls, a `PointLight` or `SurfaceLight` on the character, rim-like environment lighting. `Highlight` is for game state only (R7 in `character-design-roblox`).

## 4. AI-look tells to avoid (V9)
None of these may appear without a written reason in `CHARACTERS.md`:
- Perfect bilateral symmetry on everyone.
- Everyone the same height and build: default avatar proportions with a different shirt.
- "Cool" pieces that answer no why: belts and straps everywhere, random glowing lines, hoods, masks, katanas, scarves blowing in no wind, goggles on the forehead.
- Same face: one head shape and one expression for the whole cast.
- Detail spread evenly over the body with no focal area.
- Saturated colour everywhere, or the opposite: all-grey grit with no accent.
- Glossy, plastic, over-smooth surfaces (the generated-art finish).
- Default Roblox materials as the "style": untextured SmoothPlastic or Neon as the main material.
- Glow lines as decoration.
- The generic monster: teeth, claws, spikes, red eyes, with nothing specific to this world.
- A default Roblox walk, run or idle on a named NPC.
- Names and props from the trope shelf (check `../de-ai/BANNED.md`, plus any bans in `studio-profile.md` if it exists).

## 5. Rules (checkable)
- **V1 Silhouette test.** Flat black on white at the game's real camera angle. **Pass:** a fresh reviewer can name the character's role from the silhouette alone. **Fail:** two cast members could be confused.
- **V2 Distance test.** Measure on-screen height at the farthest distance the player must react to this character, at phone size. The primary trait and facing direction both still read. Record the measured height in `CHARACTERS.md`.
- **V3 Grayscale test.** In the real environment and lighting with saturation at -1, the character separates from the background and from every other cast member by value alone.
- **V4 Lineup test.** The whole cast in silhouette at equal scale. Each pair differs in at least two of: height, mass distribution, head shape, dominant shape.
- **V5 One primary trait,** written, tied to the world, never removed by skins or variants.
- **V6 Shape intent:** dominant and secondary shape written with meaning; subversions say what they hide.
- **V7 Saturation budget:** the most saturated, highest-contrast area sits on the 1 second read; the rest is muted; no pure black.
- **V8 Costume why-test:** every visible element has a written reason; delete the rest.
- **V9 Anti-generic list:** none of section 4 without a written reason.
- **V10 Palette source:** every character hex comes from `ART-DIRECTION.md`.

## 6. Runnable Studio checks
All four checks work on a **clone**. Never modify the real character. Every script cleans up after itself; leftover check objects in a place file break builds and audits. Run with `execute_luau` (either Studio MCP server), then screenshot with `screen_capture` (Roblox_Studio, edit mode) or `capture_screenshot` (robloxstudio).

### V1 and V4: silhouette and lineup
Edit `NAMES` to the cast's model paths. This makes a white stage far from the map, places black clones side by side at equal height, and points the camera at them.

```lua
local NAMES = {"Workspace.Cast.Janitor", "Workspace.Cast.Clerk"} -- edit
local function resolve(path)
	local inst = game
	for seg in string.gmatch(path, "[^%.]+") do
		if inst == game and seg ~= "Workspace" then inst = game:GetService(seg) else inst = inst:FindFirstChild(seg) end
		if not inst then return nil end
	end
	return inst
end
local old = workspace:FindFirstChild("_SilhouetteCheck"); if old then old:Destroy() end
local root = Instance.new("Folder"); root.Name = "_SilhouetteCheck"; root.Parent = workspace
local ORIGIN = Vector3.new(0, 5000, 0)
local wall = Instance.new("Part"); wall.Anchored = true; wall.Size = Vector3.new(200, 80, 1)
wall.Color = Color3.new(1, 1, 1); wall.Material = Enum.Material.SmoothPlastic
wall.CFrame = CFrame.new(ORIGIN + Vector3.new(0, 30, -20)); wall.Parent = root
local floor = wall:Clone(); floor.Size = Vector3.new(200, 1, 80); floor.CFrame = CFrame.new(ORIGIN + Vector3.new(0, -0.5, 0)); floor.Parent = root
local x = -(#NAMES - 1) * 6
for _, path in ipairs(NAMES) do
	local src = resolve(path)
	if src then src.Archivable = true end -- player characters are not archivable by default
	local c = src and src:Clone()
	if not c then warn("could not clone " .. path) else
		c.Parent = root
		for _, d in ipairs(c:GetDescendants()) do
			if d:IsA("BasePart") then
				d.Color = Color3.new(0, 0, 0); d.Material = Enum.Material.SmoothPlastic; d.Anchored = true
				if d:IsA("MeshPart") then d.TextureID = "" end
			elseif d:IsA("Decal") or d:IsA("Texture") or d:IsA("SurfaceAppearance") or d:IsA("Shirt")
				or d:IsA("Pants") or d:IsA("ShirtGraphic") or d:IsA("Highlight") or d:IsA("ParticleEmitter")
				or d:IsA("Light") or d:IsA("Script") or d:IsA("LocalScript") or d:IsA("BodyColors")
				or d:IsA("CharacterMesh") then
				d:Destroy()
			elseif d:IsA("SpecialMesh") then d.TextureId = ""
			end
		end
		local hum = c:FindFirstChildOfClass("Humanoid"); if hum then hum.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None end
		local _, size = c:GetBoundingBox()
		c:PivotTo(CFrame.new(ORIGIN + Vector3.new(x, size.Y / 2, 0)))
		x += math.max(12, size.X + 4)
	end
end
local cam = workspace.CurrentCamera
cam.CFrame = CFrame.lookAt(ORIGIN + Vector3.new(0, 4, 45), ORIGIN + Vector3.new(0, 4, 0))
return "staged " .. #NAMES .. " silhouettes"
```

- **Also save one PNG per character** (frame each figure alone, or crop) to `screenshots/characters/<date>/silhouettes/`, named by character. The audit's blind lineup across games is built from these files, so future audits of other games can reuse them.
- Screenshot from the front, then rotate the camera to the game's actual angle (top-down, three-quarter, first person) and screenshot again. A silhouette that only reads from the front fails if the game is played top-down.
- For V4, compare each pair: do they differ in at least two of height, mass distribution, head shape, dominant shape?
- **Lighting can wash out the white stage.** If the screenshot is grey, temporarily set the wall and floor `Material` to `Neon` (white) for the shot.
- **Cleanup:** `workspace._SilhouetteCheck:Destroy()`.

### V2: distance test
Place the character (or a clone) at the farthest reaction distance from the camera in the real map, then take a phone-size screenshot (`capture_device_matrix` on robloxstudio in a playtest, or Studio's Device Emulator). Measure the on-screen height in the image and record it.

```lua
-- Prints the predicted on-screen height in points for a character at distance d.
local d, charHeight, screenPts = 60, 5, 390 -- edit: reaction distance, character height (studs), phone height (pt)
local fov = math.rad(workspace.CurrentCamera.FieldOfView)
local visible = 2 * d * math.tan(fov / 2)
return string.format("~%.0f pt tall at %d studs (FOV %.0f)", screenPts * charHeight / visible, d, workspace.CurrentCamera.FieldOfView)
```
The prediction is a sanity check. The screenshot is the proof.

### V3: grayscale test
Do this in the real environment, with the game's actual lighting, during a playtest or with the character placed in the scene.

```lua
local Lighting = game:GetService("Lighting")
local old = Lighting:FindFirstChild("_GrayscaleCheck"); if old then old:Destroy() end
local cc = Instance.new("ColorCorrectionEffect"); cc.Name = "_GrayscaleCheck"; cc.Saturation = -1; cc.Parent = Lighting
return "grayscale on"
```
Screenshot each area where the character appears. **Pass** if it separates from the background and from other cast members by value alone. **Cleanup:** `game.Lighting._GrayscaleCheck:Destroy()`. Never leave this in the place.

### Colour lineup
Run the V1 staging script but skip the blackout (comment out the `d.Color`, `Material`, `TextureID` and destroy lines) and put the stage in the game's real lighting. This is the second image on the screenshot sheet.

### Cleanup check before you finish
```lua
local left = {}
for _, n in ipairs({"_SilhouetteCheck"}) do if workspace:FindFirstChild(n) then table.insert(left, n) end end
if game.Lighting:FindFirstChild("_GrayscaleCheck") then table.insert(left, "_GrayscaleCheck") end
return #left == 0 and "clean" or ("LEFTOVER: " .. table.concat(left, ", "))
```

## Output
- The visual fields in `CHARACTERS.md` (silhouette hook, shape language, palette colours, primary trait, read order, measured V2 height).
- The silhouette lineup, colour lineup, grayscale and phone screenshots for the screenshot sheet.
- **A chat overview for the user** with the sheet (as described in `character-design` "Output"): for each character, what you'll recognise it by in one line, and which checks passed or failed. The file is the detail; the overview is what the user reads.
