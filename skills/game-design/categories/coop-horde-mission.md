# Co-op horde mission (`coop-horde-mission`)

Read the `coop-horde-mission` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a small squad drops into a mission area, completes objectives against swarms, and extracts, with class roles and loadouts.

---

## What great looks like
- **A signature verb nobody else has.** Helldivers 2 makes you type arrow codes to call in an orbital strike, then accidentally kill your friend with it. Deep Rock Galactic lets you drill straight through the cave wall while bugs pour in. Those verbs, not the shooting, are why people remember them.
- **Objectives move you.** A mission is a route: get to the drill site, defend it, carry the core to the pod. Static wave defense gets stale fast.
- **The swarm is one readable threat.** Hundreds of small enemies move like a tide, and a few named specials (the one that grabs, the one that explodes) demand attention.
- **Extraction is the climax.** The timer starts, the swarm surges, and someone is sprinting for the pod with the objective. That run is the story players retell.

## The hook
- **First 10 s:** dropped into the mission with a weapon and the signature tool already available.
- **First 60 s:** first enemy contact and first use of the signature verb.
- **First 3 min:** first objective done, first swarm survived, a clear path to the next objective.

## Loop tuning
- **Mission length:** 15-25 min with 2-4 objectives and an extraction. If missions drag, cut an objective before cutting enemies.
- **Swarm rhythm:** waves every 2-4 minutes plus ambient enemies. Tension and relief, not a constant flood.
- **Specials:** 1-3 named special enemy types per mission, each with a tell and a counter.
- **Extraction timer:** 2-3 min of escalating pressure.
- **Difficulty tiers:** each tier adds enemies, specials or modifiers. Tune the lowest tier so a solo player with a helper finishes most runs.

## Depth and mastery
- **The skill chain:** shoot → manage ammo and cooldowns → use the signature verb well → handle specials → choose objective routes → loadout synergy with your squad or helper.
- **The depth multiplier:** loadout × mission modifier. A loadout that excels against swarms struggles against armored specials, so mission briefing should affect the pick.
- **Class roles** that each solve a problem the others cannot (the driller makes paths, the gunner holds chokepoints).
- **Destructible or reshaped terrain** is a strong source of emergent tactics.

## Retention engine
Pick at least two:
- **Difficulty tiers** that unlock as you clear them.
- **Weekly special missions** or a deep-dive chain with fixed modifiers.
- **Loadout and class unlocks** with mastery tracks.
- **A shared community goal** (a live front that moves based on all players' missions).

## Solo-first adaptation
This category is a **Variant**: solo with a helper drone or bot squad designed in from day one.
- **A helper drone or bot squadmates** that cover the jobs a squad would (revive, light the way, hold a flank). Deep Rock Galactic's Bosco drone is the model.
- **Scale the mission to the squad size:** fewer enemies and specials for one player, the same objectives.
- **Solo is the default path,** not an afterthought: tune and playtest solo first, then add squads.

## Roblox notes
- **Performance:** hundreds of enemies need batched movement and simple rigs. Use client-side rendering of swarms with server-authoritative positions at low frequency.
- **Mobile:** auto-fire option and big buttons for the signature verb. If the verb is an input sequence, make it tappable.
- **Evidence gap:** no sourced Roblox exemplar in the research. The space may be open, or demand may be weak.
- **Server size:** 1-4 player missions instanced from a lobby.

## Craft techniques
- **Swarm audio:** a rising chitter or roar before a wave hits, so players brace.
- **Signature verb juice:** the call-in or the drill gets its own sound, camera shake and visible world change.
- **Friendly fire as comedy,** if used: big and readable, low punishment.
- **Ping system** for objectives and specials so strangers and bots can coordinate without chat.

## Pitfalls
- No signature verb, so it reads as a generic horde shooter.
- Solo that is merely possible, not fun.
- Static defense missions.
- Swarms so dense that nothing reads on a phone.
- Specials with no tells.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| A signature verb nobody else has | Can a tester name the verb after one mission? Did they use it more than any other action? |
| Objectives move the squad | Map the route of one mission. Did the player cover most of the area? |
| Swarm reads as one threat, with named specials | Screenshot a wave on a phone view. Are specials distinguishable? |
| Extraction as climax | Record the extraction. Is it the most intense minute of the mission? |
| Solo helper tuned so solo is fun | Play solo with nobody online. Did the tester finish the lowest tier and enjoy it? |
| Difficulty tiers and loadout unlocks | After one mission, is the next tier or unlock named on screen? |
