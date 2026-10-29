---
name: level-design-craft
description: The craft of level design for Roblox games, platform-independent. Pacing and intensity curves, teaching mechanics through layout (the four steps), navigation and landmarks, weenies, guiding with light and color, sightlines, density and verticality, environmental storytelling, set pieces, and the seven layout archetypes (linear pearls, hub-and-spoke, vertical stack, dense investigation room, districts with onion targets, arena lanes, stealth rings) with their rules and failure modes. Use while planning any space in LEVEL-PLAN.md and while judging a blockout.
---

# Level design: craft

Load `level-design` first for the process and the gates. This file teaches how to make each decision well. Rules have IDs (LC1 to LC22) so the plan and the audit can cite them.

Evidence tags used below:
- **[talk]** comes from a GDC talk, a developer interview or a published book.
- **[observed]** is a pattern seen in successful games without a developer source. Treat it as a hypothesis to test, not a fact.

## 1. Think in time, not space
A level is experienced as a sequence of moments. Lengths only matter because of how long they take.
- **LC1** Write every distance in the plan twice: in studs and in seconds at the game's walk speed. At the default walk speed of 16 studs/s, 160 studs is 10 seconds. In story and exploration spaces, put a **beat** (an encounter, a reveal, a pickup, a choice, a view) every 15-40 seconds of travel. In an arena, the first contact should come within about 8 seconds of spawning.

A beat is anything that changes what the player knows, feels or can do. A corridor with nothing in it is not a beat, but a corridor with a sound behind a wall is.

## 2. Pacing and intensity
**The interest curve (sawtooth).** Good levels alternate tension and release. Each peak sits a little higher than the last, and after each peak comes a real valley: a safe room, a quiet corridor, a vista. Valleys let the player process what happened and make the next peak feel big. Flat high intensity reads as noise; flat low intensity reads as boredom. [talk: Level Design in a Day, GDC]

- **LC2** Draw the curve before building. List the beats with an intensity of 1-10 and a duration in seconds. Every peak is followed by a valley of at least 20 seconds. Each peak is at least as high as the previous one until the climax. Then one long valley after the climax (the reward, the view, the results screen).

**The levers you pull to change intensity:**
| Lever | Raises tension | Releases tension |
|---|---|---|
| Space size | tight, low ceiling | open, high, a view |
| Light | dark, flickering, one source | bright, warm, many sources |
| Music and sound | more layers, a pulse, then sudden silence | ambience only, room tone |
| Threat density | more enemies, closer | none in sight |
| Time pressure | a timer, a closing door, a chase | no clock |
| Verticality | looking down at a drop | solid ground |
| Information | an unknown threat, a sound with no source | the threat seen and understood |

Use two or three levers at once for a peak. One lever alone rarely moves the player.

**The director pattern for replayable solo runs.** Left 4 Dead's AI Director tracks each player's "intensity" (raised by damage taken and nearby threats), builds to a peak, holds it for 3-5 seconds, then forces a relax phase of about 30-45 seconds where no new threats spawn, then builds again. [talk: Mike Booth, "The AI Systems of Left 4 Dead", 2009] This is the right model when a run is assembled from parts (rooms from a pool, random events): the layout supplies the spaces, the director enforces the sawtooth.
- **LC3** If a space is assembled or populated at run time, the plan names who enforces the valleys: fixed rest rooms after set pieces, or a director that blocks threats for a set time after a peak.

**Common pacing mistakes:**
- Starting at full intensity. Early rooms of a run should be quiet so the first threat is felt.
- Valleys that are only empty, not restful. A valley should give something: a view, a shop, a save, a story prop.
- Back-to-back set pieces. Two peaks with no valley merge into one long noisy one.

## 3. Teaching through layout
**The four steps (kishotenketsu).** Koichi Hayashida builds each Mario level around one gimmick in four acts borrowed from four-panel comics. [talk: Game Developer, "The secret to Mario level design"; GMTK, "Super Mario 3D World's 4 Step Level Design"]
1. **Introduce:** show the mechanic where failure costs nothing.
2. **Develop:** use it again with one small complication (a gap, a timer, a second hazard).
3. **Twist:** recombine it with another mechanic, invert it, or raise the stakes.
4. **Conclude:** one show-of-mastery beat, then retire it.

- **LC4** One new mechanic per area. For each, the plan names the room or beat for each of the four steps. Do not reuse a gimmick to exhaustion; retire it and teach the next.

**Teaching without text:**
- **Safe-room demo.** Let the player watch the threat act on something else before it can touch them: it eats a crate, it breaks a light, it drags a mannequin. The player learns the rule by watching.
- **LC5 Soft first failure.** The first time a lethal mechanic appears, it must be survivable (a slower version, a checkpoint just before, a damage-only first hit).
- **LC6 One affordance color.** Pick one hue that means "you can use, climb or open this". Teach it once, never break it, and never use it on decor. Mirror's Edge's red and the yellow ledges in climbing games are the classic examples. [talk]
- **Gating.** The player cannot leave the teaching room until they have done the thing once. Use the geometry for the gate (the only exit needs the mechanic), not a text prompt.

## 4. Navigation: making a space you can hold in your head
Kevin Lynch's *The Image of the City* names five things people use to build a mental map. Totten applies them to levels. [talk: Totten, *An Architectural Approach to Level Design*]
| Element | What it is in a level | Use it to |
|---|---|---|
| Paths | corridors, streets, tracks, the critical path | carry the player; give each a different feel |
| Edges | walls, rivers, cliffs, fences, the map boundary | contain without invisible walls |
| Districts | areas with one identity (color, material, sound) | let the player say "I'm in the red area" |
| Nodes | junctions, plazas, hubs, stairwells | decision points; make them memorable |
| Landmarks | one unique object visible from far away | orient against it |

**Landmarks.**
- **LC7** Every area has one landmark: a unique silhouette visible from most of the area (a tower, a crane, a dome, a broken bridge, a giant sign). Each district has its own color and material identity so players can navigate by "the green part" without a map.
- **Hide and reveal.** A landmark should leave view and come back from a new angle. Each reveal confirms progress and is a small reward.
- **Framing.** Doorways, pillars and arches frame a target like a picture, and the eye goes inside the frame. Naughty Dog guides players through Uncharted largely with framing and composition. [talk: GMTK, "Why Nathan Drake Doesn't Need a Compass"]
- **Composition.** A corridor that ends in a lit doorway is a sentence with a full stop. A corridor that ends in a blank wall reads as a dead end even when it turns.

**Weenies.** Walt Disney's term for a tall visual magnet (the castle at the end of Main Street) that pulls people down a path. Arriving at one reveals the next. [talk: Scott Rogers, GDC 2009]
- **LC8** Put a weenie at the end of every major path. It must be taller, brighter, moving or uniquely colored compared with its surroundings. Motion (a rotating beacon, smoke, a flickering sign, a turning fan) pulls the eye harder than brightness. Chain them: arriving at one reveals the next.

**Breadcrumbs and negative guidance.**
- Breadcrumbs lead the eye and the feet: debris trails, cables, pipes, rails, footprints, a line of lights, a blood trail.
- Negative guidance discourages without blocking: darkness, clutter, low ceilings, hazard color, a sound you don't want to walk toward.
- **LC9** Prefer negative guidance to invisible walls. Where a hard boundary is needed, make it a visible edge that belongs in the world (a fence, a drop, rubble).

**Dead ends.**
- **LC10** No unlit, empty dead ends. A dead end must hide a reward (a pickup, a story prop, a view, a shortcut) or not exist. Every space has an entrance that is visible from its exit side and an exit that is lit or framed.

## 5. Guiding with light and color
- **Players move toward light** in dark spaces. Valve's levels put lit doorways, pools of light along the route, and a colored light on the exit. [talk: Valve Developer Community, Half-Life 2 level design]
- **Contrast beats brightness.** One warm light in a cool scene is louder than ten neutral lights.
- **LC11** Light the critical path: warm or accent light on exits and goals, darker and cooler side areas. Every objective carries one emissive element (a glowing panel, a neon strip, a lit sign) that reads even when shadows are off.
- **Do not guide with shadow shapes.** Roblox disables shadows below graphics quality 4, so on many phones a guidance trick built on a shadow pattern simply vanishes. Light color and emissive surfaces survive every quality level. (Details in `level-design-roblox`.)
- **Color is a language.** Danger, affordance, objective and district colors are set once in the plan and never swapped. If red means danger, a red couch is a lie.

## 6. Sightlines
Sightline length is a design value, not an accident.
- **Stealth and PvP:** sightline length is difficulty. Long lines favor observers and snipers; short, broken lines favor ambush and close play. Give both, deliberately, in different places.
- **Horror:** break long sightlines on purpose. What you can't see down the corridor is the fear. A bend, a door, a curtain, fog.
- **Exploration:** long sightlines to the landmark, short ones in the local space so there is always something near to look at.
- **LC12** Every height advantage and every long sightline has a counter: another angle that sees it, or a way up that is itself exposed.

## 7. Density and verticality
- **Density follows attention.** Cluster detail where the player should look (goals, chokes, vignettes) and keep the rest calmer. Uniform density reads as noise and costs draw calls everywhere.
- **Verticality** adds tactical options (stealth perches, high ground), landmark visibility and drama. In a vertical layout, height is progress: show the drop (glass floors, open atriums, windows down) so height is felt.
- **LC13** Every vertical route is planned explicitly. Roblox characters cannot climb by default (only TrussParts are climbable), so stairs, ramps, ladders, elevators and ziplines are drawn on the sketch, not assumed.

## 8. Environmental storytelling
Harvey Smith and Matthias Worch: players infer a story from clues and connect them in their heads, and that active problem solving creates investment. The tools are prop placement, scripted events, texturing, lighting and composition. [talk: "What Happened Here?", GDC 2010]

Techniques:
- **Staged vignettes:** a frozen tableau that implies a sequence of events.
- **Cause and effect pairs:** a scorch mark, a broken window, and glass *inside* the room means something came in.
- **Traces of routine:** a half-eaten meal, a calendar with a circled date, a coat still on the hook. Life interrupted.
- **Contradiction:** one object that doesn't fit. In an investigation game, that object is the clue.
- **Layered readability:** the first glance gives the mood, a second look the situation, close inspection the specifics.
- **Repetition with change:** the same room revisited, altered. The change is the story.

- **LC14** Every area has a "what happened here" sentence in the plan, and 3-5 props placed to imply it: at least one cause and effect pair, one trace of routine, and (where the game is about noticing) one contradiction. No filler props in a story space; every prop either supports a thread or is plain set dressing in a calm area.
- Load `de-ai-story` for any text the props carry (notes, signs, labels). Prop stories fail the same way writing does when they are generic: the skeleton with a note saying "they're coming" is a cliche.

## 9. Set pieces
A set piece is a scripted, high-production moment at the peak of the curve: a floor collapsing, a lockdown with alarms, a vault opening, a vehicle splitting apart.
- **LC15** For every set piece:
  - telegraph it at least 2 seconds ahead with sound and light, so the player looks the right way
  - keep the player in control (no or very short cutscenes; let them move)
  - make it survivable on the first try, or checkpoint just before it
  - follow it with a valley
- Uncharted's playable cinematics are the reference: the layout and camera make the player look at the event while still moving. Build the space so the event happens in front of the direction of travel, framed by the geometry.

## 10. Layout archetypes
Pick the archetype from what the game asks the player to do, then follow its rules. A large game mixes them (a hub whose spokes are linear runs; a district map whose targets are stealth rings).

| Archetype | Use when the game is about | Strengths | Main risk |
|---|---|---|---|
| Linear pearls | authored pacing, set pieces, runs | tight pacing, easy to stream | feels on rails |
| Hub-and-spoke | progression, unlocking, returning | orientation, gating, backtracking with new keys | repetitive hub trips |
| Vertical stack | climbing, ascent or descent as progress | visible progress, drama, natural ramp | navigation confusion, boring stairs |
| Dense investigation room | noticing, deduction, replay | every prop matters | pixel hunting |
| Districts with onion targets | player-made plans, open play | emergent play, freedom | getting lost, streaming cost |
| Arena lanes | repeatable fights, PvP, bot matches | replayable, readable | spawn camping, stalemates |
| Stealth rings | infiltration, social stealth | many solutions, observation play | unreadable guards, all-or-nothing failure |

### Linear pearls (string of pearls)
A chain of distinct spaces (pearls) joined by short connectors (string). Each pearl has one gimmick and one beat at its peak. Examples of the shape: carriages of a vehicle in sequence, floors of a descent, rooms of a run drawn from a pool.
- **LC16** Each pearl differs from the last in at least two of: size, light, gimmick, sound. Connectors are short valleys and natural streaming and loading boundaries (doors, airlocks, gaps).
- For replayable runs, author a pool of room prefabs that each have a fixed entrance and exit anchor, chain them at run time, and place hand-authored set-piece rooms at fixed positions in the chain. Doors and Pressure use this pattern. [observed]
- Mistake: every pearl is the same room with a different hazard. The player stops noticing.

### Hub-and-spoke
A central space the player returns to, with spokes that unlock over time. Gone Home is the canonical small example; metroidvanias and Dark Souls the large ones. [talk: The Level Design Book, circulation]
- **LC17** Every spoke ends with a shortcut that opens back to the hub (a door that unlocks from the far side, a lift, a ladder down). This is the single best fix for hub tedium.
- The hub shows the spokes' landmarks, so from the hub the player can see where they have not been.
- The hub changes as the game progresses (new NPCs, opened doors, damage), so returning is itself a beat.
- Mistake: a hub that is only a corridor junction. The hub should be the most memorable space in the game.

### Vertical stack
Floors or levels stacked on each other: a tower, a shaft, a mine, a descent.
- **LC18** One vertical landmark is visible from every floor (an atrium, an outside shaft, a central lift, a window wall) so the player always knows how high they are. Floors are chapters, each with its own identity.
- Make the vertical move itself a beat (an elevator ride with a view, a climb with a reveal). Plain stair flights between floors are dead time; keep them short or replace them.
- Show the drop. Height is only felt if the player can see down.
- Mistake: floors that look alike, so the player loses count.

### Dense investigation room
One room or one small block, packed with meaning, explored closely and often replayed. Crime scenes, frozen moments, escape rooms.
- **LC19** Every prop supports one of 3-5 story threads or is clearly background (lower detail, out of the main lighting). An inspect-to-confirm interaction (highlight, zoom, a sound) tells the player they found something, so they are not guessing at pixels.
- Frozen-moment scenes read best with mid-motion props held in place (a falling glass, a splash, a thrown paper) anchored in the air.
- Layer the room: what you see from the door (mood), what you see on a lap of the room (situation), what you find on close inspection (specifics).
- Mistake: filling the room with random clutter to look "detailed". It hides the clues and reads as a free-model dump.

### Districts with onion targets
An open map made of districts, each with a strong identity, containing targets (scores, objectives) that are themselves layered rings. Jailbreak's city is a well-known Roblox example of districts with strong silhouette and color identity and self-contained robbery sites. [observed]
- **LC20** Each district has its own landmark, color, material and sound. Each target has an entry, an inner problem, and an escape, and is built as a stealth ring (below) or a set piece. Roads and paths between districts double as chase lanes.
- Mistake: a big open map with nothing to orient by. Size without districts is just getting lost.

### Arena lanes
A contained combat space built from lanes and loops. Most competitive maps use 1-3 lanes; Treyarch's standard is two side lanes and a central lane between spawns, and "every lane needs a purpose". [talk] Doom 2016's arenas are asymmetric, vertical, and full of loops so the player keeps moving and never gets cornered. [talk: GDC 2018, "Embracing Push Forward Combat"]
- **LC21** Arena checklist:
  - 1-3 lanes, each with a different identity (long sightline, close quarters, vertical)
  - loops, no dead ends
  - at least 2 height levels joined by fast traversal
  - every choke point has at least one flank route
  - pickups placed to pull players into exposed positions (risk for reward)
  - spawns never visible from another spawn
  - a central power position visible and contestable from 3 or more angles
  - mirror the layout, or balance the asymmetry and test it
  - reduce visual clutter so silhouettes read
- When empty slots are filled with bots, the lanes double as the bot routes. Design them so pathfinding naturally runs through the intended chokes, and tag cover points (`level-design-roblox`).
- Mistake: too many lanes, so players never meet. A maze is not an arena.

### Stealth rings (the onion)
Layered rings of increasing security around a target: public, then staff, then restricted, then the target. Disguises, keys or tools open the rings. Hitman's levels are designed this way, as "a volume filled with connections", with optional guided threads ("mission stories") for new players. Dishonored gives every objective at least three routes. [talk: IOI at GDC Europe 2016 and GDC 2019; Arkane at GDC 2017]
- **LC22** Stealth checklist:
  - at least 3 routes to each objective: ground or social, high, low
  - an observation perch before each guarded zone, where the player can watch safely
  - patrol loops that cross the player's routes with timing windows of 3-8 seconds
  - guard vision readable from light, posture and audio barks
  - hiding places and shadows that are legible (a world or UI indicator)
  - a hiding spot or escape route within 20 studs of every point where the player can be detected
  - detection leads to an escape or a fight, not instant game over
- NPCs and their routines are part of the level geometry. Plan patrols on the sketch, not after.
- Mistake: one route, so stealth becomes a timing puzzle with one answer.

## What great looks like (a checklist for your own plan)
- I can trace the critical path on the sketch and say the time for each part.
- The intensity curve has rising peaks and real valleys.
- Each mechanic has four named beats and is then retired.
- Every area has a landmark, a district identity, and a lit or framed exit.
- Every dead end hides something.
- Every long sightline or height advantage has a counter.
- Every area has a "what happened here" sentence and the props to prove it.
- Every set piece is telegraphed, controllable, survivable and followed by a valley.
- The archetype's checklist is met, or the plan says why not.

## Output
This skill feeds `LEVEL-PLAN.md`; it has no document of its own. Present the work to the user with the chat overview defined in the Output section of `level-design`.

## Common mistakes
- Designing in plan view only. A sketch that looks clear from above can be a maze at eye height. Check every decision with an eye-height screenshot.
- Symmetry everywhere. Perfect symmetry outside a competitive arena makes every direction look the same and kills orientation.
- Overscaled spaces. Huge empty rooms take seconds to cross and feel cheap. Scale to the character and the camera, then add size only where a view or a fight needs it.
- Generic set dressing in a story space, which hides the clues.
- Copying a reference level's exact layout. Take its principle (a loop, a reveal, a ring), not its floor plan.

## Sources
- Level Design in a Day, GDC 2010-2015: https://gdcvault.com/play/1012660/Level-Design-in-a-Day ; https://gdcvault.com/play/1016327/Level-Design-in-a-Day ; https://gdcvault.com/play/1017639/AAA-Level-Design-in-a ; https://gdcvault.com/play/1022117/Level-Design-in-a-Day
- Mike Booth, "The AI Systems of Left 4 Dead", 2009: https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf
- Four-step level design: https://www.gamedeveloper.com/design/the-secret-to-i-mario-i-level-design ; https://www.mcvuk.com/development/video-nintendos-level-design-secrets-in-four-steps
- Christopher W. Totten, *An Architectural Approach to Level Design*, 2nd ed., CRC Press, 2019; Kevin Lynch, *The Image of the City*, 1960.
- Scott Rogers, Disneyland and level design, GDC 2009: https://boingboing.net/2009/03/27/gamedesign-lessons-f.html
- Half-Life 2 level design (Valve Developer Community): https://developer.valvesoftware.com/wiki/Half-Life_2_level_design
- Smith and Worch, "What Happened Here?", GDC 2010: https://gdcvault.com/play/1012647/What-Happened-Here-Environmental
- The Level Design Book, circulation: https://book.leveldesignbook.com/process/layout/flow/circulation
- Treyarch on lanes: https://news.xbox.com/en-us/2025/10/27/how-treyarch-crafts-multiplayer-maps-call-of-duty-black-ops-7/
- Warframe PvP level design: https://www.warframe.com/en/amp/building-warframe-pvp-20-level-design
- Doom 2016, push-forward combat, GDC 2018: https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in
- Hitman: https://gdcvault.com/play/1023849/Level-Design-in-HITMAN-Guiding ; https://gdcvault.com/play/1025879/Level-Design-Workshop-Hitman-Levels ; https://80.lv/articles/the-snail-structure-of-hitmans-levels
- Dishonored 2: https://www.gamedeveloper.com/design/level-design-deep-dive-i-dishonored-2-s-i-clockwork-mansion ; https://gdcvault.com/play/1024301/
- Roblox examples (Doors, Pressure, Jailbreak, Deepwoken) are observation only; no developer write-ups were found.
