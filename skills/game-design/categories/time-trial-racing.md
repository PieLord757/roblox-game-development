# Time-trial racing (`time-trial-racing`)

Read the `time-trial-racing` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** race a vehicle or a fast body along a short track against the clock, ghosts or other racers, and restart instantly.

**Evidence note:** the research holds no sourced racing exemplar. Trackmania and Mario Kart are `[UNV]`, and Roblox lists Racing as an official subgenre with no sourced numbers. This guide is `[analysis]` from well-known design practice. Check the studio profile's flags: this category always carries `vehicles`.

---

## What great looks like
- **A lap is a skill test you can finish in a minute.** Trackmania's short tracks are learned like a song: every corner has a right line, and shaving a tenth off is a real achievement. `[UNV]`
- **The ghost is the opponent.** Racing your own best run, shown as a translucent car, makes solo play competitive every time. A split timer that turns green or red at each checkpoint tells you instantly whether you are winning.
- **Handling has character.** Drifting into a corner, holding a boost through the exit, and slipstreaming on a straight make driving fun even with no opponent. If driving feels good on an empty track, the game works.

## The hook
- **First 10 s:** in the vehicle on a track, already moving or counting down. The first corner should be easy and the first boost or drift should trigger naturally.
- **First 60 s:** a complete lap with a time, and a ghost of that lap ready for the next try.
- **First 3 min:** a personal best beaten, a medal earned (bronze, silver, gold against set times), and the next track visible.

## Loop tuning
- **Lap length:** 30-90 s. Short enough to retry many times, long enough to have 6-12 decisions (corners, shortcuts, boost uses). `[analysis]`
- **Restart:** one button, under 1 s, from anywhere on the track.
- **Medal times:** set bronze so most players get it on the first or second try, silver after learning the line, gold for clean play, and a hidden "author" time for experts. Tune by recording testers: if fewer than half reach bronze in 3 tries, bronze is too tight.
- **Speed feel:** speed is sold by camera field of view, motion blur or speed lines, sound pitch and scenery passing close. Raising the actual speed is often worse than raising the sense of speed.
- **Tune in big steps:** if drifting feels pointless, double its exit boost and then pull back.

## Depth and mastery
- **The skill chain:** throttle and steering → braking points → racing line → drift and boost timing → shortcuts → chaining boosts through sections.
- **The depth multiplier:** handling techniques × track features. Every track should reward a different technique (a drift-heavy track, a jump track, a high-speed track), so mastery on one does not solve the others.
- **Shortcuts:** risky, faster lines that need skill to land. They are the clips.

## Retention engine
Pick at least two:
- **Ghosts and leaderboards** per track: friends, server, global.
- **Medals** per track, and a medal total that unlocks new tracks or vehicles.
- **A daily or weekly track** with its own leaderboard.
- **Player-made tracks** for a long tail, if a track editor is feasible.

## Solo-first adaptation
- Time trials are natively solo. Ghosts make solo competitive without anyone online.
- Live races are a layer. Fill empty grids with bots that drive good lines but brake a little early and miss some boosts.
- Avoid collision between racers in time-trial modes: ghosts pass through you.

## Roblox notes
- **Physics:** vehicle physics must be simulated on the owning client with network ownership set to the driver, or steering feels delayed. Validate lap times on the server against minimum possible times to stop cheats.
- **Latency:** in live races, show other cars smoothed and slightly behind; never let another player's lag shove your car.
- **Mobile:** tilt or on-screen steering, auto-accelerate as an option, large brake and drift buttons. Test on a phone early: racing handling that only works on keyboard will bounce most players.
- **Monetization:** vehicle cosmetics, trails, horns. If vehicles have stats, keep them side-grades and separate leaderboards by class.
- **Flags:** vehicles. If the studio profile bans vehicles, the fast-body variant (running, sliding, grappling along a track) keeps the same loop.

## Craft techniques
- **Checkpoint splits:** show the delta against your best at every checkpoint with a color and a sound.
- **Surface feedback:** each surface (asphalt, dirt, ice) gets its own sound, particle and handling change.
- **Track readability:** corners announced by signs, color or barrier shape ahead of time, so speed does not mean guessing.
- **Countdown and finish ceremony:** a clean 3-2-1, a strong finish sound, and the time shown big with the delta.

## Pitfalls
- Handling that feels the same on every surface and every corner.
- Physics jitter or rubber-banding under latency.
- Too few tracks at launch, with no editor and no daily track.
- Long tracks that make a mistake cost a minute.
- Paid vehicles that are simply faster on the same leaderboard.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Handling that feels good, better in corners | Does a tester drift or boost without being told? Do they say the driving feels good on an empty track? |
| Visible split time against best or ghost | Is the delta shown at each checkpoint? Is a ghost present from the second attempt? |
| Instant restart | Time from pressing restart to driving again. |
| Short, learnable tracks | Lap time on 3 tracks. Does the tester improve on the second and third try? |
| Async competition | With nobody online, is there a ghost or leaderboard to beat? |
