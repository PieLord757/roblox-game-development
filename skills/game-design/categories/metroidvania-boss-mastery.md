# Metroidvania boss mastery (`metroidvania-boss-mastery`)

Read the `metroidvania-boss-mastery` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** explore an interconnected hand-made world where new movement abilities open old areas, punctuated by hard, readable bosses.

---

## What great looks like
- **You remember the ledge.** In Hollow Knight, a high ledge you could not reach in hour one becomes reachable in hour four after you find a new movement ability, and you remember exactly where it was. That "I can get there now" moment is the genre's core pleasure: discovery that comes from the player's own map memory.
- **The boss is a test you can learn.** A good boss shows each attack with a clear wind-up, punishes a mistake hard, and leaves a short window to strike back. After five deaths the player knows its patterns; after ten they beat it, and the win belongs to them.
- **Atmosphere does the storytelling.** Hollow Knight and Ori tell their worlds through places: a ruined city, a dead colony, a lonely bench. Lore comes from what you find, not from text boxes.
- **Scale is proven.** Hollow Knight: Silksong reached 587,150 `[SDB-press]`, and Hollow Knight 95,428 `[SC]`. The audience exists for this category when the feel is excellent.

## The hook
- **First 10 s:** controlling the character in an atmospheric space. Movement and the basic attack must feel good immediately.
- **First 60 s:** a first enemy beaten, a first locked path seen (a gap too wide, a door that will not open), and the map starting to fill.
- **First 3 min:** a first ability or item, a short backtrack to use it, and a first mini-boss or tough enemy. The structure (locks, keys, bosses) is visible inside the first session.

## Loop tuning
- **Ability cadence:** a new movement or traversal ability every 30-60 minutes of play in the early game. Each one should open at least two places the player has already seen. `[analysis]`
- **Backtracking distance:** returning to a locked spot after getting the key should take under 2-3 minutes, or shortcuts must open. Unlockable shortcuts are a reward in themselves.
- **Boss tuning:** aim for a first boss that most testers beat within 3-6 attempts. If testers beat it first try, raise damage or add one more pattern; if they need 15+, lengthen the wind-ups or widen the punish window before cutting health.
- **Death cost:** lose some currency or progress, recoverable by returning to the death spot. Never lose more than 5 minutes of exploration.
- **Save points:** close enough to bosses that a retry run is under 30-60 s.

## Depth and mastery
- **The skill chain:** move and attack → jump and dodge timing → reading enemy patterns → traversal chains (dash, wall jump, double jump in sequence) → boss pattern mastery → optional challenge rooms and speed routes.
- **The depth multiplier:** movement abilities × level geometry. Each ability should change how every old room can be crossed, and late areas should demand combinations.
- **Optional mastery:** hidden areas, hard optional bosses and challenge gauntlets (Hollow Knight's Pantheons) give veterans goals beyond completion.

## Retention engine
Pick at least two:
- **Completion percentage** and a map with visible unexplored edges.
- **Boss rush or challenge modes** that reuse bosses for mastery.
- **New regions** released as chapters, which works on Roblox where a finished single-player game has no tail.
- **Speedrun timers and leaderboards** per region or boss.

## Solo-first adaptation
- Natively solo. Other players fit best as asynchronous presence: messages or marks left at hard spots, ghosts of other players' boss attempts, or a shared counter of how many have beaten a boss.
- Optional co-op for bosses is a layer; the solo boss must be beatable and fair.

## Roblox notes
- **Camera:** a side view or a fixed 3D side camera gives the genre's readability. Free 3D cameras make platforming and boss reads much harder on phones.
- **Latency:** movement and the player's attacks must run on the client. Boss attacks can run on the server, but hit detection against the player should favor the player's view to avoid "it hit me from there?" moments.
- **Content cost:** hand-made worlds are expensive. Build the movement and one boss first, prove them, then build the world region by region.
- **Mobile:** jump, attack, dash and special as large buttons; test boss fights on a phone, because timing windows that work on a keyboard can be impossible on glass.
- **Monetization:** cosmetics or region purchases. Never sell boss skips or ability unlocks: they destroy the "I can get there now" pleasure.

## Craft techniques
- **Show the lock before the key.** Every ability should answer a question the player already asked ("how do I get up there?").
- **Landmarks and map:** distinct color palettes per region, unique landmarks in every large room, and a map that fills as you explore.
- **Boss tells:** each attack gets a distinct pose, sound and timing. Use the same "language" across bosses (a flash before an unblockable, a crouch before a leap).
- **Hit-stop and feedback:** short freeze frames on landing hits, a stagger on the boss when its pattern breaks, a distinct sound for a perfect dodge.
- **Benches and rest points:** a safe place with music and a save gives pacing and relief between tense stretches.

## Pitfalls
- Getting lost with no map or landmarks.
- Backtracking that is just walking: no shortcuts, no new enemies, no new paths.
- Bosses with unreadable or random attacks.
- Building a large world before the movement feels great.
- A linear world wearing metroidvania clothes, where abilities only open the next door forward.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Movement and combat feel good before upgrades | In the first minute, does the tester move and attack freely and say it feels good? |
| Visible locks seen early and opened later | Does the tester point out a place they cannot reach yet? Do they remember and return to it after the ability? |
| Readable bosses with a fair punish window | Count attempts to beat the first boss. Can the tester describe the boss's attacks afterward? |
| Map and landmarks prevent getting lost | Does the tester ever say "where am I?" or wander for more than 2 minutes without progress? |
| Atmosphere and lore through places | Does the tester comment on a place or ask about the world without reading a text box? |
