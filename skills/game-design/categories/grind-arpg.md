# Grind ARPG (`grind-arpg`)

Read the `grind-arpg` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** level and grind toward power spikes (fruits, techniques, gear), fight bosses for drops, and roam a large world with optional PvP bounties.

**Flags reminder:** usually `open-world`, `ip-risk` and `content-hungry`. Check `studio-profile.md`. A zoned variant (islands or regions joined by travel) keeps the loop without a seamless open world, and an original setting removes the IP risk.

---

## What great looks like
- **The power spike is the product.** In Blox Fruits, eating a fruit gives you a new set of moves you can feel immediately: a new way to fight and move. That moment of "I am stronger and different now" is what players grind for. Blox Fruits holds 122K / 230K CCU with 65.1B visits, and 40%+ of its users were 17+ in 2021 `[RBX]`.
- **Bosses are worth the trip.** A boss that drops a rare power gives a reason to gather, wait and fight, and gives players a reason to meet each other.
- **There is always a next goal on screen.** A quest, a level threshold, a boss, a new island. The player never wonders what to do next.
- **Collecting powers is a long tail.** A large roster of powers or builds turns the game into "try them all," which lasts far longer than one progression line.

## The hook
- **First 10 s:** the character is in a vivid place with a quest giver or an enemy close by, and attacks feel good.
- **First 60 s:** a first quest accepted and a few enemies beaten, with the level bar moving visibly.
- **First 3 min:** a first level-up with a noticeable change (a new move, a big stat jump), and a first power or a clear path to one shown. If the first power spike is an hour away, the bounce windows will eat the game.

## Loop tuning
- **First power spike:** inside the first session, ideally within 10-20 minutes. Show the next one before the player gets the first. `[analysis]`
- **Level cadence:** frequent early levels (every 1-3 minutes in the first session), slowing over time. Each level should have a reward the player sees.
- **Grind-to-play ratio:** if testers spend most of a session killing the same mob, add variety (quests that move them, events, mini-bosses) or raise rewards. Repetition is the genre's main killer.
- **Boss timers:** world bosses on a visible schedule or a summon system, so players can plan. A boss that appears randomly with nobody around wastes its spectacle.
- **Drop rates:** rare drops should feel possible: show the rate, and use pity timers so bad luck has a ceiling.

## Depth and mastery
- **The skill chain:** basic combat → using a power's moves → combos → movement with powers → boss patterns → PvP matchups.
- **The depth multiplier:** powers × weapons or styles. If each power combines with fighting styles differently, the build space multiplies instead of adding.
- **PvP as optional mastery:** bounties and duels give skilled players a ladder, while PvE players progress untouched.

## Retention engine
Pick at least two:
- **Power collection:** a roster with visible gaps.
- **Boss drops** with rare tiers and pity.
- **New regions, powers or bosses** on a visible cadence.
- **Bounty or rank ladder** for players who opt into PvP.
- **Daily quests** that send players to different regions.

## Solo-first adaptation
- All PvE, including bosses, must be soloable, with group play making it faster rather than possible.
- PvP must be opt-in (a toggle, safe zones, or level protection). Being hunted while grinding drives casual players out.
- Strangers are best as presence and occasional help (joining a boss fight), not as requirements.

## Roblox notes
- **Large maps:** use streaming and keep phone performance in mind. Zoned islands with travel between them load better than one huge map.
- **Latency:** the player's own moves run on the client; damage is validated on the server. Big area powers should feel instant to the user.
- **IP risk:** anime-inspired powers are the genre's default. An original power system and setting avoids takedowns and reads as less derivative.
- **Monetization:** cosmetics, storage, fast travel, experience boosts with limits, and power rerolls are common. Selling the strongest powers outright breaks PvP and makes free players feel cheated.
- **Audience:** the genre reaches a wide age range; the setting and tone decide how old it skews.

## Craft techniques
- **Power reveal moment:** a short animation, a sound and the first use of the new move in a safe spot. Make it feel like a birthday.
- **Readable progression UI:** a level bar, a next-goal tracker and a power collection screen, all designed in the setting's own visual language.
- **Move feel:** each power move gets anticipation, impact, hit-stop and a distinct sound. A power that looks big but lands softly disappoints.
- **Boss spectacle:** a boss arena, an intro, phase changes. Bosses are where players remember the game.

## Pitfalls
- The first power spike too far away.
- Grinding one mob for long stretches.
- Forced PvP in grinding zones.
- Paid power that dominates PvP.
- Content that cannot keep pace with players, with no repeatable layer (collection, ladder, bosses) to fill the gap.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| A visible, fun power spike in the first session | Time from spawn to the first power or big new move. Does the tester react to it? |
| Bosses with drops worth chasing | Does the tester know a boss exists and what it drops? Do they choose to fight it? |
| A large set of powers or builds | Is the collection visible, with gaps? Does the tester say which one they want next? |
| A clear next goal on screen | At any moment, can the tester say what they are working toward? |
| Optional PvP that does not punish avoiders | Can a tester who avoids PvP grind uninterrupted? Count unwanted PvP deaths. |
