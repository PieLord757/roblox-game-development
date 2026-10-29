# Anomaly and rules check (`anomaly-rules-check`)

Read the `anomaly-rules-check` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** learn a baseline, then judge each new corridor, passenger or document against it, with the body, under rising subtlety.

---

## What great looks like
- **The rule fits on a sign.** The Exit 8: if anything is different, turn back; if nothing is, go forward. No tutorial needed. A viewer understands it from one loop.
- **Nothing is also an answer.** Many corridors in The Exit 8 are normal. Walking past a normal corridor with your heart racing is half the tension, because the player has to commit to "nothing is wrong".
- **The rules grow, and so does the weight.** Papers, Please adds a new rule each day and puts the player's family on the other side of every mistake. A stamp becomes a moral decision.
- **The anomaly is fair on replay.** When a player is sent back, they should be able to look again and see what they missed. "Oh, the poster's eyes moved" is a satisfying loss.

## The hook
- **First 10 s:** the player is in the baseline space, moving, with the one rule visible in the world (a sign, a supervisor's note).
- **First 60 s:** the first judgment made and its consequence shown. The first anomaly should be obvious, so the player learns the rule by succeeding.
- **First 3 min:** the first mistake and the reset. The player sees what they missed, understands the game is fair, and goes again.

## Loop tuning
- **One judgment every 20-60 s** `[analysis]`. Longer and the space feels empty; shorter and the player cannot study the baseline.
- **Anomaly rate:** roughly 50-70% of rooms or cases should contain an anomaly. Too few and the player stops looking; too many and "nothing is wrong" never comes up.
- **Difficulty curve:** obvious (a giant change), then medium (an object moved), then subtle (a sound, a timing, a reflection). Each new tier should be introduced with one easy example before hard ones appear.
- **Penalty size:** a wrong judgment should cost progress, not the whole run, once players are past the first few minutes. Sending a player back from stage 7 to 0 every time is fine for a 1-hour game and fatal for a game meant to be replayed daily.

## Depth and mastery
- **The skill chain:** learn the baseline → spot big changes → scan systematically → hear audio anomalies → spot timing and behavior anomalies → handle stacked rules.
- **The depth multiplier:** anomaly types × places or rule sets. An anomaly that is easy in a bright corridor is hard in a dark one. New rules that interact with old ones (a valid passport, but the photo is wrong) multiply the decision space.
- **Speed as a skill:** once accurate, the player can be challenged on speed: a timer, a queue that grows, a train that leaves.

## Retention engine
- Anomaly games decay fast without a generator. Pick one:
  - **Daily anomaly sets** with a shared seed and a board for fewest mistakes.
  - **Player-made anomalies**, reviewed and rotated in.
  - **Endless mode** with a streak record.
  - **New locations** on a visible cadence, each with its own baseline.

## Solo-first adaptation
- The category is solo by nature. Strangers can add social proof (a board of who got furthest today) without being needed.
- A co-op variant (one checks faces, another checks papers) is optional. The solo player must be able to do every check alone.

## Roblox notes
- **Cheap to build:** a baseline room plus a list of swappable anomalies. Build anomalies as small data-driven toggles on a room template, so adding one is minutes of work.
- **Mobile:** anomalies must be visible on a phone screen. Test each anomaly at phone resolution; a 2-stud change at 40 studs away is invisible.
- **Clone saturation:** Roblox ran a large anomaly wave in 2026 (Animal Hospital (Anomaly) peaked at 556K `[Rolimons]`, now 31.5K `[RBX]`). The rule or setting alone will not stand out; the judgment verb must be new.
- **Content maturity:** fear content changes the maturity label. Keep scares tied to anomalies, not random.

## Craft techniques
- **Make judgments physical:** walk back, slam a gate, stamp a paper on a real desk, refuse a passenger at the door. A menu with "Approve / Deny" buttons breaks the category's fit.
- **Teach the baseline by repetition, not text.** The first loop should be a slow, normal walk. Players learn the space by being in it.
- **Use all senses:** a footstep that stops a beat early, a light that hums, a clock that ticks once too many. Audio anomalies are the cheapest way to add subtle depth.
- **Keep an anomaly ledger:** for each anomaly, how visible it is (obvious, medium, subtle), where the player is looking when it appears, and the playtest catch rate. Retire or rework any anomaly under 10% or over 95% catch rate after the opening tier.
- **Stakes for wrong answers:** a consequence beyond "go back" gives weight. A wrong approval in Papers, Please costs money the player's family needs.

## Pitfalls
- Anomalies that are ambiguous. If players argue on replay about whether something changed, it was not fair.
- Running out of anomalies within an hour with no generator.
- Turning the check into a document panel or quiz screen.
- Jump scares with no rule behind them. Fear should come from not knowing whether you are right.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| A baseline learnable in under a minute | Can the tester describe the normal space after one minute? |
| Judgments made with the body | Count judgments made by moving or acting versus by menus or buttons. |
| Fair outcomes on replay | After each mistake, did the tester find the anomaly on a second look? |
| Escalating subtlety and new rules | Compare the first 3 anomalies with the last 3 in a session. Are new rule types introduced? |
| A long-tail generator | Is there a daily set, endless streak, player-made anomaly or new location system? |
