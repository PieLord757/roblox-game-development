# Boss-gated survival sandbox (`boss-gated-sandbox`)

Read the `boss-gated-sandbox` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** gather, build and craft in a large world, with each biome's boss unlocking the next tier of materials, tools and threats.

**Flags reminder:** this category is usually `open-world` and `content-hungry`. Check `studio-profile.md` before pitching it. A compact variant (a set of hand-made islands or zones joined by a hub) keeps the loop without a seamless open world.

---

## What great looks like
- **There is always a next boss.** Valheim gives each biome a boss whose trophy unlocks the next tier. The player always knows the answer to "what am I working toward?" Survival games that copied the gathering and hunger but dropped the boss chain lost that pull. Valheim reached 498,478 `[SC]` and still held 18.2% retention.
- **Each tier changes how you play.** Terraria's tiers bring new movement, new enemies and new building blocks, not only bigger numbers. A tier that only multiplies damage is a treadmill. Terraria reached 486,918 `[SC]`.
- **Your base is yours.** A longhouse you built by hand, on a hill you chose, with a view you like, is the reason to log back in. Building is self-expression, and it persists.
- **Atmosphere pays for exploring.** Subnautica's dark water below and Valheim's low-poly light make the next ridge or trench worth seeing for its own sake. Subnautica reached 50,876 `[SC]` as a solo, story-led take.
- **The cautionary case:** Palworld hit 2,101,535 `[SC]` with a meme hook and kept 2.0%. A hook without a deep tier chain spikes and fades.

## The hook
- **First 10 s:** standing in a beautiful, readable place with an obvious first action (a tree to chop, a rock to pick up).
- **First 60 s:** the first tool crafted from gathered materials, and the first small building piece placed.
- **First 3 min:** a first shelter or fire, a first threat survived, and the first boss or its altar shown or hinted, so the long goal is visible in the first session.

## Loop tuning
- **First tool:** craftable within 60 s of spawning. Every minute of gathering before the first craft is bounce risk. `[analysis]`
- **Tier length:** each biome and boss tier should take roughly 1-3 hours for a new player. Shorter tiers burn content; longer ones feel like a wall.
- **Gathering rates:** tune so a full tier's materials take about a third of the tier's time; exploration, building and fighting take the rest. If testers spend most of their time hitting rocks, double the yield.
- **Survival meters:** hunger and stamina should shape decisions (bring food before a boss), not interrupt play. A meter that forces a chore every 5 minutes is padding.
- **Death cost:** drop carried items at the death spot, recoverable by going back. Never delete the base or crafted gear.

## Depth and mastery
- **The skill chain:** gather and craft → build shelter → prepare for a threat (food, gear, a route) → fight the boss → plan the move to a new biome → master building systems (structural integrity, automation, farming).
- **The depth multiplier:** biome materials × crafting recipes × threats. Each new biome's materials should combine with old ones into new options, so old content stays relevant.
- **Building depth:** systems like structural support (Valheim) turn building from decoration into a puzzle.

## Retention engine
Pick at least two:
- **The boss chain** itself, with the next boss visible.
- **The persistent base** that grows and can be shown to others.
- **New biomes or bosses** released as updates, each with new materials.
- **Seasonal or alternate worlds** (a new seed with modifiers) for players who finished the chain.

## Solo-first adaptation
- The whole chain must be beatable alone. Tune bosses for one player and scale health or adds for groups, not the other way around.
- Friends are optional: shared worlds, visiting bases, trading. Strangers fit best as neighbors in a shared server rather than as required partners.
- Give solo players helpers when a task is pure labor (a companion that carries, a workbench that automates a chore).

## Roblox notes
- **Performance:** large worlds with many player-built pieces strain phones. Use streaming, cap building pieces per plot, and merge static geometry.
- **Saving:** bases must save reliably. A lost base ends a player's interest permanently.
- **Crowding:** survival crafting is crowded on Roblox `[UNV]`. The twist must be in the loop (a new tier mechanic, a new kind of boss chain), not in the art.
- **Mobile:** building placement on a phone needs snapping, a clear preview and an undo. Test it early.
- **Monetization:** cosmetic base pieces, character cosmetics, extra base slots. Avoid selling tier skips: they remove the boss chain, which is the game.
- **Studio rules:** if open worlds are banned, build the compact variant: a hub base plus separate hand-made zones, each with its boss.

## Craft techniques
- **Make the next goal physical:** the boss altar, the locked gate, the glowing trench should be visible in the world, not just in a quest log.
- **Gathering feel:** each material gets its own hit sound, chips and debris from its own substance, and a satisfying final break.
- **Lighting as reward:** dusk, fog and night change the mood of each biome. Players screenshot beautiful moments; that is free marketing.
- **Boss summoning:** let the player choose when to fight, with a ritual (placing a trophy, ringing a bell). Choosing the moment builds tension and lets players prepare.

## Pitfalls
- No boss or clear next goal: gathering becomes a grind with no point.
- Hunger and thirst meters that turn play into chores.
- Tiers that only add bigger numbers.
- A late-game content cliff with nothing after the last boss.
- Building tools that are fiddly on phones.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| A clear next goal at all times | At any point, ask the tester what they are working toward. Can they answer? |
| Building as persistent self-expression | Does the tester spend time building something they did not need? Does it save across sessions? |
| Each tier changes how you play | After the first boss, list what is new: tools, travel, threats. Is anything more than a bigger number? |
| Atmosphere that makes exploring worth it | Does the tester stop to look, explore off the path or take a screenshot? |
| Friends optional, solo complete | Can a solo tester beat the first boss? How many attempts? |
