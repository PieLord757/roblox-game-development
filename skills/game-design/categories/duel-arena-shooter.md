# Duel arena shooter (`duel-arena-shooter`)

Read the `duel-arena-shooter` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** matchmade 1v1 to 5v5 duels in small arenas, first to N short rounds, where aim and movement decide every fight.

---

## What great looks like
- **You are fighting before you have read anything.** RIVALS puts you in a duel about 10 s after joining. The lobby is a shooting range you walk through on the way to the queue, so even the wait is aim practice.
- **A round is a complete story in 60 seconds.** Spawn, peek, trade, clutch or lose, then reset. A 1v3 clutch in a 90-second round is a clip; the same fight spread over 15 minutes is not.
- **The loadout pick is a read, not a power choice.** Picking a shotgun says "I'll hold this close corner." The opponent can see it and adjust. Power stays flat, so the choice is about style and counterplay.
- **Your weapon remembers you.** A stat tracker on a wrap ("1,204 eliminations") turns a cosmetic into a record of your skill. Older players care far more about that than about a rarer color.

## The hook
- **First 10 s:** spawn in a range or a live duel with a weapon already equipped. The first shot must feel great: sound, recoil, impact and a hit marker.
- **First 60 s:** a full round against a human or a bot, won or lost. If the player has not fired at an opponent within 60 s, you are inside the bounce window with nothing to show.
- **First 3 min:** a full match finished, a visible reward (currency, rank progress, a key), and one obvious next goal on screen ("2 more wins to unlock the sniper").

## Loop tuning
- **Round length:** aim for 30-90 s of live fighting. If rounds run long, shrink the arena or add a late-round pressure (a closing zone, a sudden-death capture point). Do not add a timer that ends rounds in a draw: draws feel like nothing happened.
- **Match length:** first to 3 for 1v1 (about 4-6 min), first to 5 for team modes. If players leave mid-match often, the match is too long.
- **Time to kill:** this sets the whole feel. Too short and positioning dominates (one peek kills). Too long and the better aimer always wins, so upsets disappear. Start around 0.6-1.0 s of sustained accurate fire for a primary weapon and tune by watching playtests: there should be time to react to being shot, but not time to walk away. `[analysis]`
- **Respawn and reset:** reset between rounds in under 3 s. A dead player in a team mode should spectate a teammate with a clear view of what killed them.
- **Tune in big steps.** If the shotgun feels weak, double its close damage, then pull back. Ten-percent nudges hide whether a change mattered.

## Depth and mastery
- **The skill chain:** aim → crosshair placement → movement while shooting → peeking and angles → weapon matchups → map control → reading the opponent's habits. Each layer should be something a player can feel themselves get better at in a week.
- **The depth multiplier:** weapons × maps. Each map should favor different weapons in different areas, so the loadout pick depends on the map and the opponent. If one weapon is best on every map, the decision collapses.
- **Movement tech:** a slide, a slide-jump or a wall kick gives veterans a ceiling. Keep the basic version available to everyone and let the tech be an extension, not a requirement.
- **Counterplay for every tool:** every utility item (smoke, flash, grenade) needs a readable tell and an answer.

## Retention engine
Pick at least two:
- **Ranked ladder with visible tiers and seasonal resets.** Resets bring people back on a date.
- **Weapon-attached cosmetics with stat trackers.** The cosmetic is a skill record.
- **Win streaks** shown on the player's nameplate in the lobby.
- **Daily and weekly challenges** that push players onto new weapons or maps ("win 3 rounds with the bow"). This also stops the meta from settling on one loadout.

## Solo-first adaptation
- **Bot fill that feels human.** Bots should miss, hesitate, peek and reposition. A bot that tracks perfectly through walls is worse than no bot. Give bots a skill rating and matchmake them like players.
- **Fill fast.** If no human joins within about 6 s, start against a bot, and keep the queue open in the background so a human can take the next match.
- **Label bots honestly** (a small tag on the nameplate) so a win against a bot is not mistaken for a ranked win. Ranked points should come from human matches; bot matches still give currency and challenge progress.
- **A solo ladder:** a gauntlet of named bot opponents with styles gives the solo player a goal when servers are empty.

## Roblox notes
- **Latency:** do client-side hit prediction for the shooter's own feedback (hit marker and sound instantly) and confirm on the server. Test at 150 ms and 300 ms. Rubber-banding on a kill is the fastest way to lose an older player.
- **Mobile:** aim assist (slowdown near targets), an auto-fire option, and large buttons for jump, slide and reload. Test the whole match on a phone before calling a build done.
- **Servers:** a lobby of 20-40 players with small instanced matches inside it gives the "full server" feel without long queues.
- **Monetization:** cosmetics, finishers, wraps, kill effects. Never sell damage, fire rate or a better weapon. RIVALS is the #1 earning game on the platform without selling power.
- **Discovery:** the hook in the title and thumbnail is the duel itself: two players, one shot. Non-unique clones are demoted, so the twist must be mechanical, not visual.

## Craft techniques
- **Hit feedback on four channels:** a sharp hit sound with pitch variance, a hit marker, a small flinch on the target, and a damage number or bar change. A kill gets a distinct sound and a brief camera response.
- **Readable silhouettes:** opponents must stand out from every map's background at 50 studs on a phone screen. Pick a map palette that leaves room for player colors.
- **Map design for duels:** three lanes, mirrored or near-mirrored, with one power position that can be contested from two angles. Sightlines no longer than the longest weapon's effective range.
- **Kill cam or death recap:** two seconds that show where the shot came from. It turns "that was unfair" into "I peeked wide."

## Pitfalls
- Adding abilities or heroes before the gunplay is great. The gunplay is the game.
- Shipping with 2 maps. Map fatigue sets in within a day; aim for 5+ at launch, each with a clear identity.
- Matching new players into veterans. Protect the first 10 matches with bots or a new-player pool.
- Rewarding time played instead of skill. A daily login chest is fine; a rank that rises with hours played is not.
- Copying the market leader's exact format. The leader owns it, and clones get 2-7% of the original.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| In a match within 10 s | Time from spawn to first shot at an opponent. Under 10 s scores 2; under 60 s scores 1. |
| Short rounds, first to N | Median round length from 3+ rounds. A reset over 5 s counts against. |
| Near-flat power | Did a starter loadout win any round against an upgraded one? Is any unlock strictly better? |
| Hit feedback | Record a hit on video. Count the feedback channels. Check it at 150 ms latency. |
| Return hook | After one match, is the next goal named on screen? |
| Bot fill and mobile | Time to a match with nobody else online; a full match played on a phone view. |
