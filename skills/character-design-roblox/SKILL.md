---
name: character-design-roblox
description: "Roblox-specific character building: explicit rules for keeping, constraining, or replacing the player's avatar; choosing R6, R15, a custom rig, or no rig; HumanoidDescription and layered clothing; triangle and texture budgets; modeling and texturing well within limits; the Studio MCP generation tools and their real limits; Avatar Auto Setup; Creator Store risks; and animation as identity. Use when deciding avatar vs custom for a game, or when building, generating, rigging, texturing, or animating any character in Roblox."
---

# Character design: Roblox

Load `character-design` first for the process and the rule index. This skill owns rules **R1 to R7** and **G1 to G6**.

## 1. Avatar vs custom: the decision (R5)
Every game makes this decision explicitly and records it, with the reason, at the top of `CHARACTERS.md`. There are three answers.

### Keep the player's own avatar
Choose this only when **all** of these hold:
- The player is "themselves" in the fiction, not a named person or a specific role.
- Self-expression or cosmetics are part of the appeal (the player wants to be seen in their avatar).
- The game reads and plays fairly with any avatar shape, including tiny, huge and non-humanoid bundles.

**Required test:** play with at least 3 extreme avatars (a tiny one, a very tall or wide one, and a non-humanoid or oddly shaped bundle). Check readability at play distance and hitbox fairness. If any of them breaks the game, this is not the right answer.

When avatars are kept, **the game's identity lives in NPCs, monsters, effects, sound and UI.** Those get the full design treatment.

### Constrain the avatar
Keep the player's face, clothing and colours, but override scale, body parts, and/or animations with HumanoidDescription. Choose this when:
- roles or teams must read at a glance, or
- hitboxes and readability need a fixed size (competitive PvP, precise platforming), or
- the avatar is fine but the default animations break the game's feel.

Add a team or role read on top: a coloured accessory, a held tool, an effect. It must survive V2 (phone distance).

### Replace with custom characters
Use a `StarterCharacter`, or a role-locked model per role, when **any** of these hold:
- The player plays a specific named character or a story role.
- Roles are asymmetric and must look different (hunter vs hunted, staff vs intruder).
- The fiction's tone would break with arbitrary avatars (a period setting, a grounded horror, a specific job).
- The silhouette is gameplay information (the player must read another player's role or state from their shape).

### Always custom
- **NPCs and monsters are always custom.** Never use a default avatar or an unedited bundle for them.
- **Bot fill:** if the game fills empty slots with bots so solo play works, decide what bots look like. Options: the game's own designed characters, or constrained avatars generated from a small curated set of HumanoidDescriptions in the game's palette. Never random catalog avatars that make bots look like a different game. Record the choice.

### Recording it
In `CHARACTERS.md`: "Players: keep / constrain / replace, because ___. Bots: ___. Extreme-avatar test: passed on ___ (if keeping)."

## 2. Rig choice (R1)
| Option | Use when | Cost |
|---|---|---|
| **R6** (6 parts) | Combat and fighting where crisp, snappy, readable animation matters more than anatomy. Simple to animate. | Scale properties don't work; little deformation; layered clothing doesn't apply. |
| **R15** (15 parts) | Player avatars, human NPCs that need clothing, faces (dynamic heads), or HumanoidDescription scaling. | Heavier; default proportions make everyone look alike unless you push them. |
| **Custom rig** (Bones or Motor6D on MeshParts) | Monsters, creatures, quadrupeds, anything that must not read as an avatar. | You rig and animate it yourself; some Humanoid behaviours won't apply. |
| **No rig** (a scripted part, a light, a particle cloud, a face decal) | Entities that are mostly a cue. | Cheapest; relies on sound and effects to carry identity. |

Write the choice and reason per character. Key R15 skinning rules: LowerTorso and Root sit at the origin; at most 4 bone influences per vertex; no influences on Root.

## 3. HumanoidDescription and proportions
- Get one with `humanoid:GetAppliedDescription()`, `Players:GetHumanoidDescriptionFromUserId(id)`, or `Players:GetHumanoidDescriptionFromOutfitId(id)`.
- Edit scale (`HeightScale`, `WidthScale`, `DepthScale`, `HeadScale`, `BodyTypeScale`, `ProportionScale`), accessories, classic clothing, body parts, `BodyColors` fields, and animation-package IDs (catalog animation assets, see below).
- Apply with `Humanoid:ApplyDescription(desc)` on the server, or `Player:LoadCharacterWithHumanoidDescription(desc)` with `Players.CharacterAutoLoads = false`.
- **Don't mix** direct asset edits on the character with description changes; Roblox documents this as undefined behaviour.
- **Scale does nothing on R6.**

Constraining an avatar's proportions on spawn (server script):

```lua
local Players = game:GetService("Players")
Players.PlayerAdded:Connect(function(player)
	player.CharacterAppearanceLoaded:Connect(function(character)
		local hum = character:WaitForChild("Humanoid")
		if hum.RigType ~= Enum.HumanoidRigType.R15 then return end
		local d = hum:GetAppliedDescription()
		d.HeightScale, d.WidthScale, d.DepthScale, d.HeadScale = 1, 1, 1, 1
		d.BodyTypeScale, d.ProportionScale = 0, 0
		hum:ApplyDescription(d)
	end)
end)
```

**Custom animations are a separate step.** HumanoidDescription's animation fields (`IdleAnimation`, `WalkAnimation` and so on) are meant for catalog animation-package asset IDs, so animations you publish yourself from the Animation Editor may silently do nothing there (verify with `get_roblox_docs` before relying on either path). The dependable path: put a copy of the `Animate` LocalScript in `StarterPlayer.StarterCharacterScripts` with your own `AnimationId`s on its Animation objects (`idle`, `walk`, `run`, `jump`, `fall` and so on), or set those `AnimationId`s on the server when the character spawns. Animations played on the local player's own Humanoid replicate to other players; confirm it in `multiplayer_playtest`.

**Custom NPC proportions:** a custom mesh body can go well past avatar scale ranges, within the body bounding box limits (width 1 to 8 studs, height 4 to 10, depth 0.5 to 4 for avatar bodies). Use that range. A cast at default proportions is the most common Roblox look there is.

## 4. Layered clothing
- Bodies get a `WrapTarget` with an outer cage. Clothing gets a `WrapLayer` with inner and outer cages. Cage UVs must correspond.
- Custom cages with unique UVs can't go on the Marketplace but **are allowed for in-game assets**, so clothing made only for your own NPCs is fine.
- Avatar Auto Setup can generate cages for a custom body (section 8).
- Use layered clothing when the costume is part of the silhouette (a long coat, a wide skirt, a heavy apron). For tiny details, a texture is cheaper.

## 5. Budgets (R2, R3)
**Engine and Marketplace facts:**
- One mesh: at most 20,000 triangles.
- Marketplace avatar bodies: head 4,000; torso 1,750; each limb 1,248; body total 10,742.
- Avatar textures on the Marketplace: up to 2048x2048. The general texture docs have disagreed with themselves (both 1024 and 4096 appear); **verify the current limit with `get_roblox_docs`** before relying on anything above 1024. Their size guide: 256 for a 5 stud object, 512 for 10 studs, 1024 for 20 studs. The engine streams lower mips on weaker devices.
- One material per mesh, one UV set, UVs inside 0 to 1. `SurfaceAppearance` takes Color, Normal (OpenGL tangent space), Roughness, Metalness and an emissive mask.

**Starting policy for mobile (tune with profiling):**
| Asset | Triangles | Textures |
|---|---|---|
| Hero or player-role character | 8,000 or fewer total | one 1024 colour map; add normal and roughness only if they read at play distance |
| Major NPC or monster | 6,000 or fewer | 512 to 1024 |
| Minor or crowd NPC | 2,500 or fewer | 256 to 512, shared atlas or palette texture |
| All characters on screen at once | 60,000 or fewer | |

Check with `execute_luau`: sum the triangle counts reported by the generation result or the Studio mesh stats, and profile with `get_scene_analysis` and the micro profiler (robloxstudio).

## 6. Modeling and texturing well within limits (the craft)
- **Spend triangles on the silhouette, not the surface.** Edges that define the outline (a hat brim, a hunched back, a coat hem) deserve geometry. Flat areas inside the outline need almost none.
- **Spend texture on the 1 second read.** One painted focal area (face, chest emblem, lamp) at full resolution; everything else in flat palette colour.
- **Palette textures beat PBR for stylised characters.** A small swatch texture of the game's palette colours, with UVs dropped onto the right swatch, plus one hand-made detail map, is cheap, consistent across the whole cast, and distinct. Most stylised Roblox hits look the way they do because of this, not because of high-resolution PBR.
- **Matte over gloss.** High Metalness and low Roughness everywhere reads as plastic, the generated-art finish. Reserve shine for one material that earns it (a wet surface, a tool).
- **Three values per material** (shadow, mid, light), painted or baked, read better at phone distance than a noisy photo texture.
- **Reuse meshes and materials across the cast** where the player won't notice (hands, boots), and spend the savings on each character's primary trait.
- **Kitbash from primitives** for blockouts and even final stylised characters. A character built from a dozen well-chosen parts, coloured from the palette, often reads better at 30 points than a 10,000 triangle generated mesh.

| Weak | Strong |
|---|---|
| A 19,000 triangle generated knight with fine chainmail and a glossy 2048 texture; on a phone at 30 studs it is a grey blob. | A 4,500 triangle knight whose helmet plume is the tallest thing on screen, three flat palette values, one painted crest on the chest; it reads at 60 studs. |

## 7. The MCP generation tools and their real limits
Limits below come from the live tool schemas. Check the schema again if a call fails; tools change.

| Tool (server) | What it does | Limits and gotchas |
|---|---|---|
| `generate_procedural_model` (Roblox_Studio) | Builds a model from primitives (blocks, spheres, cylinders, wedges) with editable attributes; inserts into Workspace | Best tool for **silhouette blockouts** (step 7 of the process). `segmentation` auto, none or explicit; explicit takes `partNames`, max 8. Long-running: use `async: true`, then `wait_job_finished`. Can take a reference image. |
| `generate_mesh` (Roblox_Studio) | Text prompt to a textured mesh | **Always set `maxTriangles`** (12 to 20,000) to your R2 budget. `segmentation` auto, none or explicit, max 8 `partNames`. `size` sets the bounding box. Output is **static and unrigged**. Can run async. |
| `generate_texture` (Roblox_Studio) | Re-textures an existing MeshPart or Model from a prompt | **Replaces the source in place: duplicate first.** Optional `hintImage` (prefer one made from your palette or concept). `model` Fast (default) or Quality (a research preview; results vary). |
| `generate_material` (Roblox_Studio) | Makes a MaterialVariant | Needs `baseMaterial` (enum), `materialPattern` Regular or Organic, `materialId`, `materialDescription`. Set **both** `Material` and `MaterialVariant` on parts to use it. |
| `segment_mesh` (Roblox_Studio) | Splits a mesh into named parts | **Up to 5 parts.** Inserts a new Model beside the source; the source stays. |
| `generate_model` (robloxstudio) | Text or image to model | Has its own `max_triangles` and schema options; check its schema before use. |

**Rules (G1 to G6):**
- **G1** Always pass `maxTriangles` (or `max_triangles`) set to the R2 budget.
- **G2 World-specific prompts.** Build every prompt from the game's reference words: the world's materials, era, objects, and the character's primary trait. Generic prompts produce the statistical average in every game. **Banned in prompts unless followed by world-specific nouns:** scary, cool, epic, cyberpunk, fantasy, stylized, monster, warrior, futuristic. Log every prompt in `CHARACTERS.md`.
  - **Weak:** "scary monster, stylized". **Strong:** "a tall stooped orbital-station cook in a quilted pressure apron, apron hem frayed into strips, holding a magnetic ladle at knee height, hands too long, matte, three-tone flat colours".
- **G3** Duplicate the mesh before `generate_texture`. Prefer a `hintImage` from your own palette or concept over text alone.
- **G4 Never ship raw generated output.** At minimum: re-colour to the `ART-DIRECTION.md` palette, pass V1 to V3, and change or add the primary trait by hand (kitbash, primitives, or a modified mesh).
- **G5 Block out first.** Pass the silhouette test with `generate_procedural_model` or primitives **before** generating a detailed mesh. Then generate toward the blockout (use `size` to match it).
- **G6 Rigging path.** Humanoids from `generate_mesh` go through Avatar Auto Setup. Non-humanoids are rigged by hand, or built from segmented parts (`segment_mesh`, up to 5) joined with Motor6Ds.

## 8. Avatar Auto Setup
Turns a single contiguous body mesh into a rigged, skinned, caged, FACS-enabled R15 body. It is the bridge from a generated or hand-made humanoid mesh to an animatable character.
- Input must meet Roblox's auto-setup requirements: one contiguous mesh, a roughly humanoid T or A pose, sensible scale. Check the current requirements page before running.
- It does **not** help non-humanoid monsters. Rig those yourself.
- After setup, re-check the triangle budget (setup can add cage and head geometry) and re-run V1.

## 9. Creator Store risks (R6)
- Anyone can insert free models, so players have seen the popular ones many times. A recognisable free model reads as an asset flip instantly.
- Old uploads carry outdated meshes, high part counts, and **embedded scripts** (including malicious ones).
- **Rule:** never ship an unmodified store model as a character (that is F3, a fail). Every inserted asset is previewed first (`preview_asset` or `search_assets` on robloxstudio), stripped of all scripts, and changed in silhouette, material and colour. Record the source asset and what was changed in `CHARACTERS.md`.

Strip scripts after insertion:
```lua
local m = workspace:FindFirstChild("InsertedModel") -- edit
local n = 0
for _, d in ipairs(m:GetDescendants()) do
	if d:IsA("BaseScript") or d:IsA("ModuleScript") then d:Destroy(); n += 1 end
end
return n .. " scripts removed"
```

## 10. Animation as identity (R4)
On Roblox many characters share a rig, so **motion is one of the cheapest strong differentiators.** A default Roblox walk on a named NPC reads as unfinished.
- Every named character gets a **custom idle, a custom locomotion, and one signature action**.
- **Animate the primary trait.** The stooped janitor's walk leads with his head; the heavy one's idle shifts weight foot to foot; the nervous one's idle checks over a shoulder every few seconds.
- **Idle is the most-seen animation.** Give it a small story beat: a habit, a fidget, the visible detail from `STORY.md`. Use several idles chosen by weight so it doesn't loop visibly.
- Exaggerate timing: hold key poses, snap between them. Mushy evenly spaced motion reads as generated.
- Replace defaults through the character's `Animate` script (section 3). For NPCs, play animations from a server script on the NPC's Humanoid or AnimationController. **If animation changes only happen in a client-side copy that other clients never receive, other players won't see them.** Test in `multiplayer_playtest` (robloxstudio).
- Silhouette carries recognition first; animation is secondary and must not carry recognition alone.
- Pair each signature action with a sound (see `de-ai-feel`). A character's sound signature is part of their identity.

## 11. Separation and Highlight (R7)
`Highlight` is for game-state signals only (targeted, carrying the objective, spotted), never permanent decoration. The client renders a limited number at once (commonly cited as 31; **verify with `get_roblox_docs`**). Separate characters from the background with value contrast and lights instead.

## Output
- The avatar-vs-custom decision with reason, rig per character, triangle and texture counts, generation prompts, store-asset sources and changes, and animation list, all in `CHARACTERS.md`.
- **A chat overview for the user** with the screenshot sheet: the avatar decision and reason in one sentence, any character over budget, and anything that came from generation or the Creator Store and how it was changed. The file is the detail; the overview is what the user reads.
