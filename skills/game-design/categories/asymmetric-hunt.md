# Asymmetric hunt (`asymmetric-hunt`)

Read the `asymmetric-hunt` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** one hunter against several survivors or hiders, who win by finishing objectives, hiding or escaping.

---

## What great looks like
- **The hunter role is a fantasy people queue for.** In Dead by Daylight the killer is powerful, scary and readable. Players want to be it, and survivors want to outplay it.
- **Objectives drag survivors into danger.** Generators make noise, keys are in the far corner. Survivors cannot just hide; they have to take risks, and every risk is a decision.
- **Chases have counterplay.** A survivor running a loop around a wall, dropping a pallet at the right second, and breaking line of sight is a skill fight, not a footrace. Violence District reaches 93.0% liked `[RBX]` on that structure.
- **Small servers mean every player matters.** In a 1 vs 5 round, each survivor's fate is visible to all.

## The hook
- **First 10 s:** a role is revealed (hunter or survivor) and the player is in the map, with their first objective or first target in view.
- **First 60 s:** a survivor hears or sees the hunter and has to decide to run, hide or keep working; a hunter finds a first trail.
- **First 3 min:** a chase. If a player has had no chase or near-miss within 3 minutes, the map is too big or the hunter too slow.

## Loop tuning
- **Round length:** 5-10 min. Long enough for 3-4 chases, short enough that being caught early does not mean a long wait.
- **Objective count and time:** tune so survivors need to work 3-5 objectives, each taking 30-80 s of exposed time. If survivors finish without a chase, raise objective time; if they never finish, lower it.
- **Hunter speed:** slightly faster than survivors in the open (about 10-15%), so loops and obstacles are what save survivors. `[analysis]`
- **Server size:** 5-9 (1 hunter plus 4-8 survivors).
- **Caught players:** give them something to do (spectate, a rescue mechanic, a ghost role) so they do not leave.

## Depth and mastery
- **Survivor skill chain:** work objectives → hide → read the hunter's direction from audio → run loops → use pallets and stuns → rescue teammates → bait the hunter off others.
- **Hunter skill chain:** track by audio and marks → cut off loops → zone objectives → use the power → choose which survivor to pressure.
- **The depth multiplier:** character kit × map. Each map's loops and objectives change which powers and perks shine.
- **Hide-and-seek variant:** if the survivor verb is disguise (painting, prop forms), the craft is in the disguise being a skill: blending well should be a visible achievement.

## Retention engine
Pick at least two:
- **Character roster unlocks** with distinct kits for both sides.
- **Role mastery tracks** (hunter levels, survivor levels).
- **Daily and weekly challenges** per role.
- **Cosmetics** on the hunter that survivors see and fear.

## Solo-first adaptation
This category is a **Variant**: solo-viable only as a solo hunter against bot survivors, or a solo survivor against a bot hunter with authored behavior. Pure hide-and-seek against humans is No.
- **Bot hunter:** give it patrol routes, sound investigation, line-of-sight chase and a readable power. It should make mistakes (lose you behind a wall) so loops work.
- **Bot survivors:** they work objectives, panic, run loops badly or well by skill level, and rescue each other. A hunter beating dumb bots is not a game.
- **Fill missing seats** with bots in under 10 s, and swap in humans between rounds.

## Roblox notes
- **Queue tilt:** nobody, or everybody, wants to be the hunter. Use a hunter-chance meter that grows each round you survive, and reward the less-wanted role.
- **Small servers:** 5-9 players per round, which also works at low CCU.
- **Mobile:** sprint and interact as big buttons; a clear prompt for pallets and doors.
- **Maturity label:** the format reaches older players at Mild or Moderate with tension, not gore.

## Craft techniques
- **Terror radius:** a heartbeat or music layer that grows as the hunter approaches. It turns audio into information.
- **Scratch marks or footprints** so the hunter can track and survivors know they leave a trail.
- **Chase music** that kicks in on line of sight and fades when broken.
- **Stun and pallet drops** with hit-stop and a big sound: the survivor's moment of triumph.
- **Hunter first-person or close camera** for fear; survivor third-person for awareness.

## Pitfalls
- A hunter who wins most rounds or loses most rounds.
- Maps too big, so rounds are empty walking.
- Caught players waiting with nothing to do.
- Bots so weak that solo play is pointless.
- Hide-and-seek with no meta progression (easy to clone, hard to keep).

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Aspirational hunter role | Play as hunter. Is the power fun and readable? Do testers want to play it again? |
| Objectives pull survivors into danger | Count chases that start at objectives versus elsewhere. |
| Chases with counterplay | Record a chase. Did the survivor use an obstacle or loop to escape at least once? |
| Small servers | Server size and how often each player is in view of the action. |
| Bots fill either side | With nobody online, play a full round on each side. Was it fun? |
