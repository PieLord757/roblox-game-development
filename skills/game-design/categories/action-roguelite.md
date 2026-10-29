# Action roguelite (`action-roguelite`)

Read the `action-roguelite` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** responsive real-time combat through rooms, a reward choice at every door, death, and a hub that changes and talks back every time you return.

---

## What great looks like
- **Dying moves the story.** In Hades every death sends you home, and someone there has something new to say about how you died. A failed run still pays out in story, so the player never feels the 30 minutes were wasted.
- **The door shows the reward.** Hades marks each exit with the reward behind it. Choosing a door is a small, readable decision made every minute: more power now, more money for later, or a story item.
- **Two gifts that combine.** Duo boons in Hades only appear when you hold blessings from two specific gods. They are a reward for committing to a plan, and a surprise the first time.
- **Combat that is good with nothing equipped.** Dead Cells (14,880 `[SC]`, 17% ret) and Hades both feel good in the first room with the starting weapon. Builds amplify a good verb; they cannot rescue a weak one.
- **A hub that grows.** Cult of the Lamb (56,262 `[SC]`) wraps runs around a base you manage. The base is the reason to start the next run.

## The hook
- **First 10 s:** the player is in a room with an enemy and a weapon. The first hit has hit-stop, a sound and a stagger.
- **First 60 s:** the first room cleared and the first reward choice made. The choice must change something the player can see in the next room (a new effect on attacks, a dash that leaves fire).
- **First 3 min:** the first death or the first mini-boss, then the hub with one new line of dialogue or one new thing to buy. The player should leave the hub knowing what they want next.

## Loop tuning
- **Room length:** 30-90 s of fighting per room. Long rooms make the reward choice rare; short rooms make it trivial.
- **Run length:** 20-40 min for a full clear, split into 3-4 regions with a boss each. A first run should die in region 1 or 2 at 5-15 min.
- **Reward rate:** one meaningful choice per room. Alternate power rewards with economy and story rewards so the player chooses between now and later.
- **Death cost:** keep a meta currency that always comes home. Run-only power is lost; meta progress is not. If players quit after a death, the meta reward is too small or too slow.
- **Enemy telegraphs:** every enemy attack needs a wind-up the player can react to, typically 0.4-0.8 s for normal enemies and longer for big hits. Shorten telegraphs for late regions instead of adding damage.
- **Tune in big steps.** If a weapon is never chosen, double what makes it special before reworking it.

## Depth and mastery
- **The skill chain:** attack → dash through danger → cancel attacks into dashes → read enemy wind-ups → crowd control and positioning → build planning toward a synergy → adapting when the offers do not cooperate.
- **The depth multiplier:** weapons × boons (or abilities × modifiers). Each weapon should want different boons, so the same boon pool makes different builds per weapon.
- **Heat or modifiers:** a ladder of opt-in difficulty rules (enemies have more health, fewer healing rooms, a timer) gives veterans a long ceiling and lets them pick their pain.
- **Weapon aspects:** variations of a weapon that change one rule give mastery a new start without new content cost.

## Retention engine
Pick at least two:
- **Death advances the plot.** New dialogue after every run, with lines that react to how you died.
- **Permanent meta-upgrades** bought in the hub with a currency that always comes home.
- **A difficulty ladder** with visible tiers and a personal best per weapon.
- **Collection of synergies** (a codex that fills as you see new combinations).

## Solo-first adaptation
The genre is solo by nature. A co-op mode is a bonus: shared rooms, separate reward choices, and revives. Do not tune the base game around two players.

## Roblox notes
- **Combat feel under latency:** run the player's own attacks, dash and hit effects on the client, and confirm damage on the server. Test at 150 ms. A dash that rubber-bands is unacceptable.
- **Mobile:** attack, dash and special as three large buttons; aim follows movement direction by default with an optional aim stick.
- **Camera:** fixed angle (isometric or high third person) keeps rooms readable and cheap to light.
- **Content cost:** rooms are modular. Build 20-30 rooms per region from a small kit, and let enemy mixes vary them.
- **Monetization:** cosmetics, extra weapons as one-time unlocks with an earnable path, story chapters. Never sell run power.

## Craft techniques
- **Hit-stop:** 40-90 ms freeze on hits, longer on heavy hits and kills. Add a small camera push toward the hit direction.
- **The reward preview:** show what is behind each door with an icon in the world, not a menu.
- **Hub dialogue triggers:** write lines keyed to specific events (died to the first boss three times, used a weapon for the first time). One reactive line is worth ten generic ones.
- **Boss phases:** each boss has 2-3 phases, and each phase adds one new rule rather than more of the same.

## Pitfalls
- Long runs with no checkpoint.
- Rewards that are only stat bumps, so builds feel the same.
- A hub that never changes, so dying is just a loading screen.
- Content that tries to make each run longer instead of each run different.
- Enemy attacks without wind-ups, so deaths feel unfair.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Combat fun in a grey-box room | Five minutes in one room with the starting weapon and no rewards. Does the tester keep fighting willingly? |
| Visible reward choice each room | Count rooms with a choice the player could see before committing. |
| Build synergies that change play | Compare two runs: did the tester play differently because of their build? |
| Death advances something | After a death, what is new in the hub? Nothing scores 0. |
| Difficulty ladder | Is an opt-in harder mode visible after the first clear? |
| Runs of 20-40 min with a checkpoint | Time a full run. Note where a mobile player could stop. |
