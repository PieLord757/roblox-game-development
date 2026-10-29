# Platform fighter (`platform-fighter`)

Read the `platform-fighter` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** side-view brawls where damage raises knockback and you win by launching opponents off the stage.

---

## What great looks like
- **The kill threat is always readable.** A damage percentage climbs under each fighter. At 30% a hit is a nudge; at 140% the same hit sends them past the blast zone. Everyone watching knows when a fighter is in danger.
- **Being launched is not the end.** A good recovery (double jump, up-special, ledge grab) lets a launched fighter fight their way back, and the opponent has to choose between chasing off-stage and waiting at the ledge. Those edge-guard exchanges are where matches are won.
- **Kill hits feel like events.** The game freezes for a beat, the camera punches in, and the launched fighter streaks off screen. Super Smash Bros. `[UNV]` built a genre on that moment.
- **Fighters feel different from the first jump.** A heavy fighter falls fast and survives long; a light one gets three jumps and dies early. Picking a fighter changes how you play, not just how you look.

## The hook
- **First 10 s:** on stage, in control, with an opponent (bot or human). Moving and jumping feel good before any hit lands.
- **First 60 s:** land a few hits and watch the opponent's percentage climb; get launched once and recover.
- **First 3 min:** take a stock with a kill hit that triggers hit-stop and camera response, and finish a match.

## Loop tuning
- **Knockback curve:** tune so a strong move kills from mid-stage around 100-140%, and weak moves never kill below 200%. Players should be able to predict kill percent after a few matches. `[analysis]`
- **Hit-stop:** 3-9 frames on normal hits scaled by damage, longer (about 10-14 frames) on kill-launch hits, applied to both fighters. `[analysis]`
- **Stocks and match length:** 3 stocks for about 3-6 min matches. If matches run long, raise knockback growth; if they end before anyone recovers once, lower it.
- **Input forgiveness:** a short input buffer (about 4-6 frames) and coyote time on ledges and jumps. Players should never lose a stock to a dropped input.
- **Blast zones:** far enough that a mid-percent launch is survivable with a good recovery, close enough that edge-guards matter.

## Depth and mastery
- **The skill chain:** move and jump → attack directions → shield and dodge → grab → recover to the ledge → edge-guard → directional influence on knockback → fighter matchups.
- **The depth multiplier:** fighter × stage. Fighter weight, speed and recovery play differently on stages with platforms, walls or moving parts.
- **Directional influence:** letting the launched player steer their launch slightly turns every kill hit into a two-sided read.
- **Ledge play:** grab, climb, roll, jump, attack. Each ledge option should have a counter so ledge situations are mind games.

## Retention engine
Pick at least two:
- **A ladder or tower mode** of bot fights with escalating difficulty and a boss at the top.
- **Ranked online with tiers.**
- **Fighter mastery tracks** with cosmetic rewards per fighter.
- **New fighters or stages** on a visible cadence.

## Solo-first adaptation
- **Bots at several levels** that recover, edge-guard and shield like people. A bot that cannot recover teaches nothing about edge play; a bot that never misses is no fun.
- **The solo mode must be complete:** a ladder, a boss, unlocks and a reason to replay (harder levels, time trials).
- **Run the simulation locally for solo** so solo play has zero input lag; online is a layer on top.

## Roblox notes
- **Input lag kills this genre.** Run your own fighter's simulation on the client, and use a deterministic fixed-step simulation if you add online play.
- **Mobile:** a stick plus 3-4 buttons (attack, special, jump, shield). Test that a phone player can recover to the ledge.
- **Evidence gap:** there is no sourced Roblox platform fighter in the research, so first-mover space may exist, and so may weak demand.
- **Cautionary tale:** MultiVersus fell from 153,044 to 29 avg30 `[SC]` after a grind-heavy relaunch with a thin roster. Do not gate fighters behind grind.

## Craft techniques
- **Hit-stop on both fighters, with the victim shaking in place**, then the launch.
- **Camera framing:** keep all fighters in view; zoom out as they spread, punch in on kill hits, and briefly slow time on a final-stock kill.
- **Launch trails** and a distinct sound for kill-percent launches, so the crowd hears it.
- **Weight shown in animation:** heavy fighters land with dust and a thud, light ones barely touch down.
- **Readable damage HUD:** the percentage changes color or shakes as it reaches kill range.

## Pitfalls
- Floaty jumps or slow air control.
- Bots that cannot recover or never edge-guard.
- Too few fighters with real differences.
- Online play with input delay, shipped before solo is great.
- Grind-gated fighters.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Knockback scales visibly with damage | Record the same strong move at 30% and 130%. Is the difference obvious and predictable? |
| Recovery and edge play | Count recoveries in a match. Can a launched fighter get back, and does the opponent have options? |
| Hit-stop and camera on every hit, more on kills | Record a normal hit and a kill hit. Compare freeze and camera response. |
| Distinct fighters | Swap fighters. Do weight, speed and range change how a tester plays? |
| Full solo mode | With nobody online, what is there to do, and is the bot fun at more than one level? |
