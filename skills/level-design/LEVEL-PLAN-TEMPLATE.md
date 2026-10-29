# <Game name>: <space name> level plan

Copy this file to `design/<game>/levels/<space>/LEVEL-PLAN.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and fill it in. Delete these instruction lines and any section that does not apply. Rule IDs (LC, LR, LG) refer to the level-design skills.

Status: draft / blockout iteration <n> / blockout sent <date> / blockout approved by user <date> / art pass / audited <date>

## 1. Goal and archetype (required)
- **One line:** what the player does, feels and learns in this space.
- **Archetype:** linear pearls / hub-and-spoke / vertical stack / dense investigation room / districts with onion targets / arena lanes / stealth rings / mix (say which parts)
- **Why this archetype:** <one sentence tied to what the game asks the player to do>
- **Players:** solo / solo with bot fill / up to <n>. How it plays solo: <one line>

## 2. References (required)
4-8 references saved in `refs/levels/`. One line each on what you take (a loop, a reveal, a sightline, a scale), never the whole floor plan.
| File | Source | What we take |
|---|---|---|
| | | |

## 3. Metrics (required, measured per LR1)
| Metric | Value | Measured or default |
|---|---|---|
| Walk / sprint speed | | |
| Jump height / distance at walk | | |
| Max required gap / ledge | | |
| Corridor min / comfort | | |
| Ceiling min | | |
| Door size (player / bot) | | |
| Cover full / half | | |
| Grid | 5 studs | |

## 4. Top-down sketch (required)
Scale: 1 cell = <n> studs (5 or 10 is typical). North is up. Keep it rough; its job is to fix the routes, areas and landmarks before building. After the blockout, add the real top-down screenshot below it (LR4) and update the sketch if they differ.

Legend: `#` wall, `.` floor, `D` door, `S` spawn or start, `E` exit or goal, `L` landmark, `W` weenie, `*` beat, `!` set piece, `^` stairs or ramp up, `v` down, `H` hiding spot or cover, `P` observation perch, `=` shortcut (locked until opened), `~` hazard, `X` contradiction or key prop

```
##########################
#S....*...#......L.......#
#.........D.......*......#
######D####......!.......#
#.....*...#..............D==
#..H......#.......^......#
#.........D..............#
##########################E
```

Top-down screenshot: `../../screenshots/levels/<space>/<date>/topdown.png`

## 5. Areas (required, one block per area)
### <Area name>
- **Goal:** what the player does, feels and learns here
- **Size and time:** <w × d × h studs>; crossing time <s> at walk speed
- **Landmark:** <the one unique silhouette seen from most of this area> (LC7)
- **District identity:** color <name>, material <name>, sound <bed>
- **Entrance / exit:** how the exit is lit or framed (LC10, LC11)
- **Guidance:** light on the path, breadcrumbs, negative guidance on wrong ways (LC9, LC11)
- **Sightlines:** longest line and its counter (LC12)
- **Vertical routes:** <stairs, ladders, lifts> (LC13)
- **What happened here:** <one sentence>; props: cause and effect ___, routine trace ___, contradiction ___ (LC14)
- **Streaming boundary:** <which door, corner or airlock> (LR11)

## 6. Critical path and pacing (required)
Every peak is followed by a valley of at least 20 s; peaks rise until the climax; a beat every 15-40 s of travel (LC1, LC2).
| # | Beat | Area | Intensity 1-10 | Duration (s) | Levers used | Planned travel time to next (s) | Measured (s) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

Intensity curve (rough, one column per beat):
```
10 |
 8 |           #        #
 6 |     #     #        ##
 4 |  #  ##    ##   #   ##
 2 | ##  ###  ###  ### ####
   +----------------------
```

Valleys are enforced by: fixed rest spaces / a director that blocks threats for <s> after a peak (LC3)

## 7. Teaching plan (required for each new mechanic)
| Mechanic | Introduce (safe) | Develop | Twist | Conclude, then retire | Soft first failure? |
|---|---|---|---|---|---|
| | | | | | |

Affordance color: <hue and hex>. Never used on decor (LC6).

## 8. Landmarks and weenies (required)
| Landmark or weenie | Area | Why it stands out (taller, brighter, moving, unique color) | Where it is framed | Where it is hidden and re-revealed |
|---|---|---|---|---|
| | | | | |

## 9. Archetype checklist
Copy the checklist for the archetype in use from `level-design-craft` (LC16 to LC22) and mark each item done, or why not.

## 10. Routes, bots and patrols (stealth, PvP, bot fill)
- Routes to each objective (ground, high, low):
- Chokes and their flanks:
- Spawns and what each can see:
- Power position and its 3+ angles:
- Bot agent size and door width used:
- Tagged points: Cover / PowerPosition / Flank / Pickup / PatrolNode
- Patrol loops and timing windows (s):

## 11. Set pieces
| Set piece | Telegraph (sound, light, ≥ 2 s) | Player control | Checkpoint | Valley after | Pre-stream point |
|---|---|---|---|---|---|
| | | | | | |

## 12. Build notes
- Terrain used for: <or none> (LR8)
- Kit pieces needed, and the hero piece per area (LR9):
- Streaming: Atomic models ___; Persistent ___ (LR10)
- Lighting technology and the low-quality guidance check (LR14):
- Performance numbers in the densest area (LR13):

## 13. Iteration log (required, at least three before showing the user)
| # | Date | What changed | Why (what the test showed) | Screenshots |
|---|---|---|---|---|
| 1 | | | | |

## 14. Approval
- Blockout sheet sent: <date>
- User response: <approved / changes requested: ...>
- Logged in `progress.md`: yes / no
