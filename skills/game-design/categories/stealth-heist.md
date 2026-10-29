# Stealth heist (`stealth-heist`)

Read the `stealth-heist` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** get into a hand-made space, reach the objective unseen (or recover when you are seen), and get out with a rating that makes you want to do it cleaner.

---

## What great looks like
- **You can see what the guard sees.** Great stealth makes vision readable in the world: a cone of light, a head turn, a suspicion icon that fills. The player plans against information, not against luck.
- **Every room has three ways in.** A vent, a disguise, a distraction. The space is a puzzle with several answers, and the player's own answer is the one they remember.
- **Getting spotted is a story, not a reload.** Suspicion fills, a guard comes to look, an alarm rises in steps. A player who reacts well can still save the run, and that recovery is often the best moment of the session.
- **The rating invites a second run.** A disguise sandbox like Hitman `[UNV]` lives on the replay: same level, a cleaner route, a better rating. The first run is learning; the next ones are mastery.
- **Proven but small on Roblox.** Notoriety (1.7K `[RBX]`) and ROB IT (1.8K `[RBX]`) show demand. The niche is underserved or the demand is modest; a strong verb is what separates a new entry.

## The hook
- **First 10 s:** the player is outside or just inside the space, with the objective named and a guard visible.
- **First 60 s:** the first stealth move that works: slipping past a guard, a distraction that pulls one away.
- **First 3 min:** the objective reached or a full spot-and-recover sequence. The player has seen at least two possible routes.

## Loop tuning
- **Level length:** 5-15 min for a clean run, longer for a first run. Split long levels into sections with checkpoints.
- **Suspicion speed:** a guard should take 0.5-1.5 s to go from noticing to alert at mid range, less at close range. Instant detection removes counterplay.
- **Alarm stages:** at least three: suspicious (investigate), alert (search), full alarm (hunt or lockdown). Each stage gives the player a window to recover.
- **Tools:** 2-4 tools per level, each with a cost (limited uses, noise, time). A free tool with no cost becomes the only tool.
- **Patrols:** loops of 15-40 s. Long enough to learn, short enough that waiting is not boring.
- **Tune in big steps.** If players always go loud, double the reward for stealth before making loud harder.

## Depth and mastery
- **The skill chain:** move unseen → read vision and patrols → use one tool → chain tools → plan a full route → recover from mistakes → optimize for rating.
- **The depth multiplier:** tools × guard types. Each tool should work on some guards and not others (a distraction works on patrols, not on a camera).
- **Optional objectives:** a side target, a no-harm run, a time limit. They turn one level into several.

## Retention engine
Pick at least two:
- **Ratings per level** (stealth, time, harm), with a best-ever shown.
- **Unlocks** of tools or starting positions that open new routes on old levels.
- **Player-made contracts** (a target and rules on an existing level).
- **New levels** on a cadence, each with a new guard type or tool.

## Solo-first adaptation
The genre is solo by nature. A co-op mode can split roles, but the solo route through every level must exist and be the main tuned path.

## Roblox notes
- **AI quality is everything:** guards need vision cones, hearing, investigate states and believable search. Budget most of the build hours here.
- **Mobile:** crouch, interact and a tool button; no small precise aiming required for stealth success.
- **Vision readability:** world-space indicators above guards are clearer than screen-edge UI on a phone. Check that indicators stay readable at phone size.
- **Content cost:** levels are expensive. Build one great level fully before a second, and reuse guard and room kits.
- **Monetization:** cosmetics, extra contract slots, new chapters. Never sell a tool that skips the stealth.

## Craft techniques
- **Guard barks:** short lines when guards notice, search and give up. They tell the player the state without UI.
- **Light and shadow as rules:** dark areas reduce detection. Make the rule visible (a light meter on the player, or clear light pools).
- **The planning view:** let the player observe from a safe vantage at the start. Watching patrols is part of the fun.
- **Results screen:** route taken, times spotted, rating, and one hint at a route not found.

## Pitfalls
- AI too dumb for stealth to matter, or too sharp to counter.
- One intended route.
- Instant fail on detection.
- Trial and error with no way to read guards.
- Tactical controls that fail on phones.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Readable guard vision and patrols | Can the tester predict when a guard will see them? Ask before they move. |
| More than one way through | Watch two testers. Did they take different routes? |
| Tools with costs | List tools used. Was any one tool used for everything? |
| Spotted escalates, recovery possible | Get spotted on purpose. Is there a window to recover? |
| End-of-level rating | Does the results screen make the tester want to replay? Ask. |
