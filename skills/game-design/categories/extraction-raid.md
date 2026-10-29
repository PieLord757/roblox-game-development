# Extraction raid (`extraction-raid`)

Read the `extraction-raid` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** bring gear in, grab what you can, and get out alive; die and you lose everything you carried.

---

## What great looks like
- **The walk to the exit is the best part.** A full bag turns a quiet corridor into the most tense minute of the session. The loot is the same; what changed is what you stand to lose.
- **Solo PvE found a huge audience.** Escape from Duckov (301,322 `[SC]`) made a top-down, solo, PvE take on a famously punishing PvP genre. Players who were scared of being hunted by other humans still wanted the push-or-leave tension.
- **Greed is a decision every minute.** "One more room" is the core question. The game should make the answer genuinely unclear: the next room might hold the rare item, or the thing that ends the run.
- **The stash makes the loss mean something.** Loot only matters if it visibly improves something you keep: a hideout, a base, a set of tools. Without that, losing a bag is just a reset.

## The hook
- **First 10 s:** the player is inside the raid area with a basic loadout, and a pickup is in view.
- **First 60 s:** the first loot grabbed and the first threat sensed (a sound, a patrol, a meter rising). The player should already feel "I could lose this."
- **First 3 min:** the first extraction attempt, successful or not. Show the haul landing in the stash with a visible upgrade bought or close to bought. A first raid should be short and kind; the stakes come once the player has something to lose.

## Loop tuning
- **Raid length:** 5-15 min. Long raids make each loss too painful; short raids make the stash grow too fast.
- **Threat curve:** threat rises with time inside and with greed (noise, carried value). The safest moment should be the start and the most dangerous the extraction.
- **Push-or-leave pressure:** give the player a reason to stay (rarer loot deeper in, bonus for full bags) and a reason to go (a rising meter, a timer, a hunter that wakes). Tune until playtesters disagree about when to leave.
- **Insurance:** let the player protect one slot or a small amount. A total loss early in the game drives quits; a total loss with a full bag late in a raid is the drama.
- **Extraction design:** the exit should be known, reachable, and contested (a final gauntlet, a wait at the exit point, a door that takes 5 s to open).
- **Tune in big steps.** If nobody ever pushes deep, double the deep loot value before touching anything else.

## Depth and mastery
- **The skill chain:** move quietly → read threats → route through the map efficiently → value loot at a glance → manage bag space → time extraction against the threat curve → pick loadouts for the plan.
- **The depth multiplier:** loadout × map threat. What you bring in should change which areas are worth visiting, so preparing is a real decision.
- **Map knowledge:** fixed maps with randomized loot and threat placement. Players learn routes; the run stays uncertain.
- **Risk ladders:** harder zones or harder entry tickets pay more, so veterans choose their own risk.

## Retention engine
Pick at least two:
- **Persistent stash or base at risk.** The base grows with every successful raid.
- **Collection** (a log of rare finds with gaps).
- **Daily contracts** ("extract with three of this item") that push players into different areas.
- **A risk ladder** of harder zones unlocked by the base.

## Solo-first adaptation
**Required variant: solo PvE.** The threat is AI, not other players. Other humans can appear as co-op partners, never as hunters required for the game to work. Tune the AI threat so a careful solo player can win and a greedy one loses.

## Roblox notes
- **Instanced raids:** one raid per player or party, launched from a shared lobby where others can see your haul. The lobby gives social presence; the raid stays fair.
- **Mobile:** a big "grab" button and a clear bag-full indicator. Inventory management should never need a grid menu during the raid; use auto-stacking and a simple swap prompt.
- **Saving:** write the stash only on extraction or death, server-side, so disconnects cannot duplicate loot.
- **Monetization:** cosmetics, stash space, one-time base upgrades. Never sell loot that skips the risk.
- **Crowded settings:** fantasy-dungeon extraction is crowded on the platform `[UNV]`. Pick a setting and a threat type that make the extraction moment new.

## Craft techniques
- **Make value readable:** loot rarity in color and sound, and a running total of the bag's value on screen. The player should know exactly what is at stake.
- **Sound as the threat channel:** footsteps, a breathing monster, a meter that ticks louder. Audio makes the player feel watched without UI clutter.
- **The extraction sting:** a distinct sound and a slow-motion beat when the player crosses the exit with a full bag. It is the payoff of the whole loop.
- **The loss screen:** show exactly what was lost and what killed you, then put the player back in the lobby within seconds with a cheap way to try again.

## Pitfalls
- Required PvP. It shrinks the audience to the hardcore.
- Raids so long that a loss feels like an hour gone.
- A stash that does not change how the next raid plays.
- Inventory screens mid-raid.
- Copying a market leader's setting. Late entries into a crowded field fade fast (Marathon fell under 4% of its peak by month five).

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Carried gear at risk and visible | Is the bag's value on screen? Did the tester know what they would lose? |
| Push-or-leave decision every minute | Ask testers at minute 3 and 6: "would you leave now?" Disagreement scores 2. |
| Tension peaks at extraction | Was the last minute the most tense? Watch input speed and comments. |
| Stash or base improves visibly | After one extraction, did something the player keeps change? |
| PvE threat enough without humans | Play a full raid with nobody else online. Was there real danger? |
