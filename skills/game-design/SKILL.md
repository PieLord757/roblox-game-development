---
name: game-design
description: Start here for every new game and every design decision. Explains what makes a game fun, deep and worth returning to, classifies the game into one of 40 specific categories, and routes to the brief (new game), pitch (new ideas) and audit (existing game) skills. Use before building anything, when pitching, or when a game feels flat.
---

# Game design (start here)

## Why this exists
Most games fail for design reasons that are visible before a line of code: the core action is not fun on its own, nothing changes after 20 minutes, the first minute is setup, or nobody has a reason to come back tomorrow. Polish cannot fix those. This skill set makes the design case explicit, checks it against what actually works on Steam and Roblox, and keeps checking it once the game is playable.

**The rule: every new game starts here.** No build starts until `game-design-brief` has written `GAME-DESIGN.md` and its verdict is not weak (or the user has explicitly chosen to go ahead anyway).

## Studio facts
Read `studio-profile.md` at the project root if it exists. It holds the audience, the hard rules, the existing games and pitches, the default paths and the publishing rules. These skills never hardcode them.

If it does not exist, ask the user before pitching or giving a verdict:
1. Who is the audience (age, platform)?
2. What are the hard rules (for example: solo play required, no menus, no open world)?
3. What games and pitches already exist (mechanic, twist, setting)?

Then offer to save the answers as `studio-profile.md`.

## Which skill to load
| You are | Load |
|---|---|
| Starting a new game, or about to build a pitched idea | `game-design-brief` |
| Asked for new game ideas | `game-design-pitch` |
| At a stopping point in a game that is already playable, or the game feels flat, or players are not coming back | `game-design-audit` |
| Classifying any game, or checking what a category needs | `CATEGORIES.md`, then `categories/<slug>.md` |
| Designing or tuning a specific system in a category | `categories/<slug>.md` (craft guidance for that category) |

**How this relates to the `de-ai` skills (if the project has them):** design comes first and decides *what* the game is. The de-AI skills come during the build and decide whether it *looks, reads and feels* hand-made. Run `game-design-brief` before the first build; load the de-AI skills while building; run `game-design-audit` and `de-ai-audit` at milestones. They check different things and neither replaces the other.

## Files in this skill
- `CATEGORIES.md`: the 40 categories, each with loop, motivations, must-haves, failure modes, exemplars with numbers, targets and a fit label, plus how to classify a game.
- `categories/<slug>.md`: deep craft guidance for every category that is not labeled No: what great looks like, the hook, loop tuning, depth, retention, solo-first adaptation, Roblox notes, techniques, pitfalls and playtest checks.

---

## What makes a game good
These are the principles that recur across 18 design frameworks (MDA, LeBlanc, Bartle, Quantic Foundry, Self-Determination Theory, Schell, Koster, Flow, Swink, core-loop research, Meier, Hodent, Sylvester, juice, Cook, GMTK and Extra Credits, Lazzaro, Adams). They are ranked by how many frameworks state them. Each comes with the check that makes it usable.

1. **Challenge matched to skill (14 of 18 frameworks).**
   - Near-guaranteed success in the first minute.
   - Then a sawtooth curve: introduce, practice, test, relief.
   - Optional harder routes or modifiers for challenge seekers.
   - Difficulty is not the main engine for most players: readable progress and novelty are.
2. **Rich, immediate feedback (12/18).** The core action gives feedback on at least 4 channels (sound, visual, camera, UI number, world change) within 100 ms of input. On Roblox, predict the player's own actions on the client.
3. **Learning and mastery are the fun (12/18).** Fun is the feeling of learning a pattern, and boredom arrives when the pattern runs out. Draw the skill chain for the first 30 minutes. Add a new skill or a new combination every 3-5 minutes early on, and know where the long tail comes from: opponents, emergent systems or build combinations.
4. **Mechanics, fiction and feel agree (11/18).** The rules express the setting. Feedback comes from the setting's materials: a pickaxe on rock throws chips and dust, not generic sparkles.
5. **Interesting decisions (10/18).** Every minute holds a choice with a trade-off and enough information to reason about it. Hunt down dominant strategies; players will optimize the fun out of a game if the efficient path is boring.
6. **The core action is fun as a toy (10/18).** In an empty grey-box room, with no goals, UI or rewards, the core verb is fun for 5 minutes. If it is not, nothing built on top will save it.
7. **Clear goals, taught by doing (9/18).** No text tutorials. The level teaches the rule; one concept at a time; check understanding before adding the next. Every moment of confusion in a playtest is a design bug, not a player skill issue.
8. **Discovery, novelty and surprise (9/18).** Secrets, systemic surprises and new combinations keep curiosity alive.
9. **Social connection without obligation (9/18).** Other people make games last, but cooperating with strangers is the least preferred way to play. A fun solo or parallel mode is the floor; optional low-commitment ways to interact (race, trade, help, show off) sit on top.
10. **Design from the target experience backward, and playtest early (9/18).** Write the 2-3 target feelings first, then the dynamics that produce them, then the mechanics. Test with people who have never seen the game.
11. **Pick a target player (8/18).** Name 1-2 player types and their top motivations (see the motivation table in `CATEGORIES.md`). Cut features that serve none of them.
12. **Visible progression (8/18).** Several kinds at once (skill, options, collection, status, world). Every reward should change how the next loop *plays*, not just raise a number. In PvP, prefer sideways progression to raw power.
13. **Fair, cheap, informative failure (8/18).** Fast retry, a visible cause of death, and odds that feel fair (players credit themselves for wins and blame the game for losses, so bias perceived odds slightly toward the player).
14. **Depth from simple rules (7/18).** Few rules with many interactions beat many rules with few. Ask: what stories will players tell each other after a session?
15. **Game feel and juice (7/18).** Tune movement and the core verb first; add juice proportional to importance. Juice amplifies a good loop and cannot rescue a bad one.
16. **Intrinsic over extrinsic (7/18).** Rewards that tell players they are getting better beat rewards that pay them for time. No dark patterns (forced grinding, play-by-appointment as the core, pay to skip frustration you created). Older players see through manipulation and say so.
17. **Pacing and an interest curve (7/18).** Each session has a hook, rising and falling tension, a peak and a tease for next time.
18. **A channel for self-expression (7/18).** At least one: building, customizing, playstyle or a build.

### What fading games have in common
Use this as a red-flag list on any design:
- The core verb is not satisfying alone.
- The pattern space runs out fast: one skill and nothing that builds on it.
- Rewards are numbers that do not change how the next loop plays.
- Decisions are obvious, or made without information.
- The first session hides the fun behind setup, tutorial text or grind.
- Multiplayer *requires* cooperation with strangers.
- Losses feel unfair or unexplained.
- Manipulative loops stand in for satisfaction.
- Nothing happens that anyone would tell a friend about.

---

## The fun test (run it on every idea, brief and audit)
A game passes only if it can answer all seven with something concrete. The brief and pitch skills use this as a gate. If `studio-profile.md` has its own fun filter, run that as well; a game must pass both.

1. **Toy:** what is the core verb, and why is it fun in an empty room with no goals?
2. **Hook:** what does the player do in the first 10 seconds, and what do they feel by 60 seconds?
3. **Decision and stakes:** what is the first real choice with a trade-off, does it come within 5 minutes, and what can the player lose?
4. **Runway:** what will the player still be learning after 5 hours (opponents, emergent systems, combinations, a skill ceiling)?
5. **Return:** what specific reason brings them back tomorrow? It must be a named engine from the brief skill's list. "Updates" does not count.
6. **Solo floor:** is the full loop fun with nobody else online?
7. **Story:** what moment would a player describe to a friend or clip?

## Platform facts that shape every design
These come from Roblox's own discovery documentation (Oct 2026) and GameAnalytics' 2026 benchmarks. They apply to any Roblox game:
- **First-play bounce is scored at under 60 s and at 61-180 s.** The hook must land inside a minute, and the loop must complete inside 3.
- **Play days per user beat long sessions.** Playtime counts only up to 60 minutes per user per day, so design for "come back tomorrow", not "stay four hours".
- **Intentional co-play is a ranking signal.** Even solo-first games should ship invites, a party queue and a "play with friends" option.
- **Exact clones are demoted.** A trend take needs its own mechanic.
- **Benchmarks:** D1 median 10.3%, top 1% 22.2%; D7 median 1.6%, top 1% 9.1%; session median 9.8 min, top 5% 16.6 min.
- **Roblox clones Steam hits within weeks**, and the clones draw players. A proven Steam loop that has not been ported is the best opening; a mechanic that is easy to copy will be copied.
- **Proven loop plus one twist beats novelty.** Change one or two pillars of a category, not all of them.

## Output rule for every sub-skill
Every document these skills write starts with a **5-line plain-English summary** for the user, followed by the detail for the build thread. After writing the file, the agent **presents a clear overview of the result directly in chat**: the file is the detail; the chat overview is what the user reads. Write it for someone who will not open the file.

## Writing style
Plain, specific sentences. Numbers over adjectives. No em dashes. Name the replacement when you name a problem.
