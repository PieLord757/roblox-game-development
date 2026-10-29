# Lane runner (`lane-runner`)

Read the `lane-runner` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** auto-forward runs where you steer between lanes or gates, growing, shrinking or dodging, in levels of 30-120 s.

**Evidence note:** sourced data is thin (DONT SPLASH 61K `[RBX]`; the mobile gate runners such as Count Masters and Mob Control are `[UNV]`). Treat the numbers below as `[analysis]` starting points to tune in playtests.

---

## What great looks like
- **The ad is the game.** The gate-runner format became famous through mobile ads because one glance explains it: a crowd runs, hits a "×2" gate, doubles, then smashes into an enemy crowd. If your game cannot be explained by a 5-second clip with no text, it is not using the format's strength.
- **The choice is always slightly painful.** The best gates offer "+20" on the left and "×2" on the right when you have 15 followers, so the player does arithmetic under pressure. A gate pair with an obvious answer is decoration.
- **The ending is a spectacle.** The run builds a number; the finale spends it. A crowd of 300 pouring into a castle and knocking it down is the payoff that makes "one more level" automatic.

## The hook
- **First 10 s:** the player is already running and steering. No menu, no tutorial text: the first gate pair is so obvious ("+5" vs "-5") that the hand learns before the head.
- **First 60 s:** a full level finished with a spectacle finale and a result (a number, stars, coins).
- **First 3 min:** 3-4 levels played, one upgrade bought that changes the next run's start (a bigger starting crowd, a new runner), and a visible goal ("level 10 unlocks the boss").

## Loop tuning
- **Level length:** 30-60 s early, up to 120 s later. Shorter is better for "one more". `[analysis]`
- **Decision rate:** one meaningful choice every 2-4 s. Fill the gaps between gates with small dodges or pickups so the thumb is never idle.
- **Gate math:** make roughly a third of gate pairs real dilemmas, where the right answer depends on your current count or the next hazard. The rest can be warm-ups and traps that punish autopilot.
- **Run speed:** fast enough that the player has to commit before reading every gate twice, slow enough to read once. If testers miss gates they wanted, slow down 20-30%; if they look bored, speed up.
- **Fail rate:** early levels should be cleared on the first try about 90% of the time; later levels around 60-70%. Failure should come from a choice, not from a reaction they could not make. `[analysis]`

## Depth and mastery
- **The skill chain:** steering → reading gates → mental arithmetic under speed → planning two gates ahead → routing for bonus gates → optimizing for the finale.
- **The depth multiplier:** gate types × finale types. A finale that rewards a big crowd, one that rewards a small fast crowd, and one that rewards a specific unit type make the same gates mean different things.
- **Hidden routes:** locked bonus gates, breakable walls or shortcuts that need a certain count give skilled players something to find.

## Retention engine
Pick at least two:
- **Level count with a visible map** and boss levels every 10.
- **Upgrades that change the opening** of every run (starting count, runner type, gate luck).
- **Daily level or daily seed** with a leaderboard.
- **Async races against ghosts** of other players on the same level.

## Solo-first adaptation
- The core is single-player. A race mode is a layer: put other players (or bots) in parallel lanes, visible but not required.
- If players can affect each other (sabotage gates, steal followers), keep it optional and fair: a sabotaged player should still be able to finish.
- Bots in race modes should make human-looking mistakes (taking a bad gate now and then), not run perfect math.

## Roblox notes
- **Rendering crowds:** draw followers on the client with cheap parts and bulk movement; replicate only the count. Hundreds of physics characters will not survive a phone.
- **Server authority:** the server resolves gates from the player's lane position so the count cannot be spoofed; the client only sends steering.
- **Mobile:** steering by drag across the whole screen, not small buttons.
- **Monetization:** skins for the crowd and runner, cosmetic finale effects, a level skip only for levels already cleared. Avoid selling count multipliers in competitive modes.
- **Audience:** this format skews young on mobile and Roblox. If the target audience is older, the setting, tone and finale must carry it.

## Craft techniques
- **Number juice:** the count should pop, scale and change color on every gate, with a rising pitch for gains and a dull thud for losses.
- **Crowd feel:** followers should bunch, stretch around obstacles and spill when hit. A crowd that moves as one rigid block reads as a number, not a crowd.
- **Readable gates:** large numerals, distinct colors for good and bad operations, and a glance-able size at running speed on a phone.
- **Finale escalation:** show the crowd's size against the obstacle before impact, so the player knows if they will win a split second before they do.

## Pitfalls
- Gates with an obvious best choice every time.
- A finale that is just a number on a screen.
- Copying the ad format with no twist, in a format already crowded on Roblox and mobile.
- Long levels that kill the "one more" rhythm.
- Physics-simulated crowds that drop the frame rate on phones.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| One-thumb steering, no instructions | Does a new tester steer correctly in the first 5 s without reading anything? |
| A choice every 2-4 s | Time the gaps between decisions over one level. Count gate pairs with an obvious answer. |
| Payoff at the end of each run | Does every level end in a visible spectacle? Does the tester react? |
| Levels of 30-120 s | Time 3+ levels. Does the tester start the next one without being prompted? |
| Upgrades change the next run's opening choices | After an upgrade, is the next run's first 10 s different in a way the tester notices? |
