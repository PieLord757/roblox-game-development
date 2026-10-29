# Chase-round survival (`chase-round-survival`)

Read the `chase-round-survival` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a short round, something is after everyone, and how well you move decides whether you are still standing when the timer ends.

---

## What great looks like
- **Chased within seconds.** Evade (45K / 82K, 9.4B visits, 93.9% `[RBX]`) puts you in a round where the chasers are already moving. There is no setup, no class pick and no tutorial. Run.
- **Movement is the skill.** Evade's bunny-hop, slide and emote-dash give it a real ceiling. New players run in a straight line and get caught; veterans weave through a map at twice the speed. Clips of movement tech are how the game spreads.
- **Helping costs something.** Reviving a downed stranger means turning back toward the threat. That small risk, taken for someone you do not know, is the only cooperation the game asks for, and it works without voice.
- **Simplicity lasts.** Natural Disaster Survival (4.5B visits, created 2008 `[RBX]`) is a random disaster on a random map, survive it. It still runs after more than 15 years because the rules fit in one sentence and the chaos is different every time.

## The hook
- **First 10 s:** the round starts or is about to, and the threat is visible or audible. The player is moving.
- **First 60 s:** a near-miss. The player escapes a chaser or a falling building by a hair.
- **First 3 min:** a full round survived or lost, a currency payout, and the next map announced. The player has seen someone else do a move they want to learn.

## Loop tuning
- **Round length:** 2-4 min. Short enough that a death only costs a minute of spectating, long enough for a comeback.
- **Intermission:** 10-20 s between rounds, with a map vote or a preview. Longer and players leave.
- **Chaser speed:** slightly faster than a running player, slower than a player using movement tech. That single ratio is the whole skill ceiling. Tune it first, and tune it in big steps.
- **Downed state:** downed players should be revivable for 10-20 s, and reviving should take 2-4 s in the open.
- **Threat count:** scale threats with players alive, so a lone survivor at the end faces a fair finish rather than every chaser at once.
- **Map size:** big enough to run loops, small enough that chasers find you within 20 s.

## Depth and mastery
- **The skill chain:** run → use corners to break line of sight → jump timing → slide and hop to keep speed → chain tech across a map → juke chasers into each other → revive under pressure.
- **The depth multiplier:** movement tech × map geometry. Each map should reward different tech (slopes for slides, open fields for hops, corridors for jukes).
- **Readable tech:** every advanced move should be visible on others so players can learn by watching.

## Retention engine
Pick at least two:
- **Movement mastery** with personal stats (rounds survived, revives, distance).
- **Daily and seasonal events** with new maps or new threats.
- **Cosmetics** (emotes, trails) that show off and never change speed.
- **Map rotation** with community favorites.

## Solo-first adaptation
The threat is AI, so a solo player always has a full game. When the server is empty, fill with bot survivors who run and get caught believably, so the solo player still has others to revive and outlast.

## Roblox notes
- **Movement under latency:** player movement is client-authoritative by default on Roblox, which is good for feel. Validate speeds on the server to stop exploiters without fighting legitimate tech.
- **Mobile:** jump and slide as large buttons; emote-dash-style tech should have a button version, not only a keyboard trick.
- **Servers:** 10-20 players gives a crowd without chaos. Spectating the survivors after death keeps players in the server.
- **Monetization:** cosmetics and emotes. If an emote has movement utility, make it free or earnable.

## Craft techniques
- **Chaser presence:** a loud, distinct sound that grows with distance, so the player can track threats without looking.
- **Speed feel:** FOV kick and wind sound as the player gains speed. Speed should feel faster than it is.
- **Map landmarks:** each map has 3-4 big landmarks so players can plan routes in seconds.
- **Round-end moment:** a slow-motion beat on the last survivor and a short replay or highlight.

## Pitfalls
- Movement tech that only veterans know exists. Teach the first trick through a map element (a slide ramp) that new players use naturally.
- Map fatigue from too few maps.
- Chasers that can never be outrun, so skill does not matter.
- Long intermissions.
- Selling speed.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Chase within 10 s | Time from round start to first threat contact or sight. |
| Rounds of 2-4 min on varied maps | Median round length over 3 rounds; count distinct maps seen. |
| Movement skill ceiling | Can a tester see or learn a move that is faster than running? Compare a new player and a practiced one. |
| Low-cost help for strangers | Did the tester revive someone, or get revived, without talking? |
| Cosmetics only | Check the shop: does anything change speed or survival? |
