---
name: de-ai-ui
description: Rules and process for HUD, menus, fonts, colors, icons, 3D art, lighting, and store images in Roblox games so nothing looks AI-generated. Use before designing or changing any screen, art direction, or thumbnail.
---

# De-AI: UI and art

## The core rule
**Every screen's look comes from the game's own world.** If you can swap your HUD into a different game and it still fits, it's generic.

Examples (illustrative settings, not real games):

| Setting | UI built from |
|---|---|
| A 1980s desert rally race | Roadbook pages with tulip diagrams, a dashboard trip meter, sponsor decals |
| A mountain rescue team | Topographic contour maps, laminated route cards, hi-vis orange tape |
| A medieval monastery scriptorium | Vellum, wax seals, illuminated margins, a scribe's ruled lines |

For every screen, write one line in `ART-DIRECTION.md`: **"This looks like ___ from the real world, because ___."** If you can't fill that in, redesign.

## Process
### 1. References first
Save 6-10 real references to `refs/`. Mix three kinds:
- **The real objects** your UI imitates, such as photos of real rally roadbooks or rescue route cards.
- **2-3 shipped games** with great UI in a similar mood.
- **1-2 film stills** for lighting and color.

Write `refs/README.md` with one line per image on what you're taking from it, whether that's the type, the shapes, the color, or the layout.

### 2. Avoid a studio house style
Before choosing a palette, read the other games' `ART-DIRECTION.md` palettes (find them through `studio-profile.md` if it exists, or in each game's folder). Run `python3 -I .claude/skills/character-design/palette_collisions.py design --target <game>`, where `design` is the folder that holds every game folder (from `studio-profile.md`, or `design/` by default). Deliberately pick a **different color family** from the most-used one across the studio. Overlap is a note, not a failure, but every game drifting into the same near-black, cream, brass and red formula makes the whole catalog look like one game.

### 3. Art direction doc (`ART-DIRECTION.md`)
- **Palette:** 5-6 named colors pulled from your references, with a stated role for each (background, text, accent, danger, highlight).
- **Fonts:** exactly 2 (display plus body), and why each fits the world. Check that both are available in Roblox (`Font.fromName` or FontFace). Never pick one off the banned list (`BANNED.md`, or any bans in `studio-profile.md`).
- **Shapes:** the panel and button shapes your world uses, for example "stamped paper tags with torn edges" or "riveted metal plates". Use at least 2 distinct shapes; not every panel is a rounded rectangle.
- **Lighting preset:** Future lighting, an Atmosphere tuned to the mood, plus subtle Bloom, ColorCorrection and SunRays. Write down the exact values.
- **Materials and texture:** what surfaces are made of. Avoid untextured plastic.
- **Motion:** how UI enters and leaves (snap, slide, stamp, flicker), matched to the world.

### 4. Build
- **The play HUD is tiny.** Show only what matters this second. Everything else lives in menus between rounds, or appears only when relevant.
- **Hierarchy:** one thing per screen is clearly the most important; size, color and position say what to read first.
- **Asymmetry and texture** beat perfect centered symmetry. Add small imperfections where the world has them: wear, stamps, handwriting, tape.
- **Readable on a phone:** body text at least 14px at phone size, tap targets at least 44px, nothing under the thumbs or the Roblox top bar.
- **The 3D world** has foreground, middle and background depth. No floating props, no default materials, no empty grey floors.
- **Icons** are drawn in one consistent style that matches the fonts. Never mix icon packs.

### 5. Check
- Screenshot every screen during a real playtest, then run `capture_device_matrix` for phone, tablet and desktop.
- Look at each screenshot cold and ask: **would a 17-year-old believe a person designed this?** If you hesitate, find what's generic and replace it.
- Check every element against `../de-ai/BANNED.md`, plus any bans in `studio-profile.md` if it exists.
- **The first time the UI is built in-game:** send the user a screenshot sheet and wait for their OK before building more on top.

## Store page (icon, thumbnails)
- **Icon:** one bold, readable shape, legible at 150 px (the smallest size Roblox shows it on the store; `publish-store-page` has the full icon rules), in the game's own palette and style. No text smaller than the icon can hold.
- **Thumbnails:** real gameplay moments or art in the game's actual style, showing the core mechanic. Use the game's own fonts.
- **No glossy, over-smooth AI-image style.** If you generate art, repaint, composite or stylize it until it matches the game's look.

## Output
1. **`ART-DIRECTION.md`** and **`refs/README.md`** in the game folder, kept current as the look changes.
2. **A clear overview in chat.** The file holds the detail; the chat overview is what the user reads. Give the "This looks like ___ from the real world, because ___" line, the palette and the two fonts with one reason each, any palette overlap with the studio's other games, and the screenshot sheet (phone view included). At the first UI and art build, end with the question and wait for the user's OK.
