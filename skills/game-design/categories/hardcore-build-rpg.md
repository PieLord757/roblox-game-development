# Hardcore build RPG (`hardcore-build-rpg`)

Read the `hardcore-build-rpg` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a punishing action RPG with deep stat and talent builds, skill-based combat and permanent stakes (permadeath or lives).

**Flags reminder:** often `open-world` and `content-hungry`. Check `studio-profile.md`. A layered or zoned world (descending layers, separate regions joined by a hub) keeps the loop without a seamless open world.

---

## What great looks like
- **Stakes make every fight matter.** Deepwoken's permadeath (lives, then a wipe) means a routine fight can end a character you spent days on. Fear of loss turns ordinary combat into tense, careful play. The audience that wants this is small but deeply engaged: over 60% of Deepwoken's fans were 17+ in Roblox's 2021 data `[RBX]`.
- **Builds are a second game.** Players argue on wikis about stat splits and talent combos. A build is a theory the player tests with their own hands, and a good build system makes every new character a fresh experiment.
- **Skill beats stats, but stats change the fight.** A skilled player with a weak build can still win by parrying well; a strong build changes how fights play, not just how fast they end.
- **Older-skewing players pay for this.** Bloodlines is the #5 top earner on about 9K Sunday players, with paid access `[RBX]`. Depth and stakes earn more per player than broad appeal.

## The hook
- **First 10 s:** character creation that matters (a race, an origin or a starting trait shown with its effect), kept under a minute, or a quick start with a default build.
- **First 60 s:** a first fight that teaches the core combat (parry, dodge or block) through a readable enemy.
- **First 3 min:** the stakes shown clearly ("you have 3 lives") before anything can be lost, a first meaningful build choice (a stat point, a talent), and the next layer or region visible as a goal.

## Loop tuning
- **Onboarding protection:** the first 30-60 minutes should be protected (no permanent loss, or a guaranteed safe zone). Brutal onboarding is this category's main bounce cause. Keep the difficulty, delay the permanence. `[analysis]`
- **Build choice cadence:** a meaningful choice (a talent, a stat milestone, a new ability) every 15-30 minutes early on.
- **Loss tuning:** players should lose a character only after warnings and a chance to retreat. Make the moment of loss clear and dramatic, and keep something across lives (knowledge, an account unlock, a legacy item) so loss stings without erasing everything.
- **Combat timing:** parry windows around 150-250 ms read as fair on keyboard; on phones widen them or add a visual cue. Tune from playtest recordings, not intuition. `[analysis]`

## Depth and mastery
- **The skill chain:** basic attacks → reading wind-ups → parry and dodge timing → stamina management → build synergies → choosing fights (when to retreat) → PvP reads.
- **The depth multiplier:** build options × enemy types. Different builds should find different enemies easy or hard, so the world feels different with each character.
- **Theorycraft fuel:** publish exact numbers in game (or let players find them) so the community can calculate. Hidden math frustrates this audience.

## Retention engine
Pick at least two:
- **Permadeath or lives** that make each character a story, and each new one a fresh run.
- **Build variety** large enough that the next character is a different game.
- **Layered progress:** deeper layers or regions released over time.
- **Account-level legacy:** unlocks that persist across characters (new origins, starting options), so loss also opens doors.

## Solo-first adaptation
- The PvE path must be fully playable alone, including bosses. Party play is optional.
- PvP must be opt-in or confined to zones. Griefing a solo player's permadeath character is the fastest way to lose this audience.
- If the world is shared, other players work best as rare encounters and helpers, not threats the solo player cannot avoid.

## Roblox notes
- **Latency:** parry-based combat needs client-side input response and server validation with a small tolerance. Test at 150 ms and 300 ms; unfair parries at lag kill trust in permadeath.
- **Saving:** character data must be robust. A lost character from a save bug is far worse than a death.
- **Content maturity:** this genre's tone often lands at Moderate. Restricted would cut the audience to ID-verified adults only.
- **Monetization:** cosmetics, appearance rerolls, private servers, extra character slots, or paid access. Never sell lives or protection from permadeath in PvP contexts.
- **Mobile:** combat buttons sized for thumbs, with lock-on. Test a full fight on a phone.

## Craft techniques
- **Show the stakes before the risk:** lives as visible objects (beads, candles, marks) that the player watches go out.
- **Death as an event:** a slow, heavy death sequence and a record of what the character achieved. Make the end of a character feel like the end of a story.
- **Readable enemies:** each enemy telegraphs with a pose and a sound. A fair hard game teaches; an unfair one loses players.
- **Build preview:** let players see what a talent will do before committing (a short demo or exact numbers).

## Pitfalls
- Permadeath before the player understands the combat.
- PvP that lets veterans erase new players' characters.
- Hidden or random math that the community cannot reason about.
- Builds where one combination dominates every situation.
- Save loss or rollback bugs. In a permadeath game, these are catastrophic.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Real stakes shown before the risk | Before the first possible loss, can the tester say what they would lose? |
| Builds that change how combat plays | Compare two builds in the same fight. Does the tester play differently? |
| Skill-based combat with readable enemies | Can the tester name what each enemy is about to do? Count deaths they call unfair. |
| Onboarding that teaches the brutality | Does a new tester survive and learn the core combat in the first 30 minutes? Where do they quit? |
| Layers or regions that gate progress | Is the next layer visible and the requirement to reach it clear? |
