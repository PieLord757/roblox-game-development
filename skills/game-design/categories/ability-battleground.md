# Ability battleground (`ability-battleground`)

Read the `ability-battleground` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a large free-for-all where each player picks a kit of about 4 moves plus an ultimate and brawls with whoever is nearby.

---

## What great looks like
- **No menu between dying and fighting.** In The Strongest Battlegrounds you respawn and the nearest fight is a few steps away. The game never asks you to wait.
- **A new player finds a combo in two minutes.** Move 1 launches, move 2 catches them in the air. The first time a player strings two moves, they feel strong, and that is the hook.
- **Veterans have tech beginners cannot see.** Dash cancels, ragdoll extensions and tech chases let skilled players show off, which drives the clip culture.
- **The ultimate is an event.** A meter fills, the screen changes, and everyone nearby knows to run or to fight.

## The hook
- **First 10 s:** spawn with a kit equipped and other players (or dummies) in view. The four move keys are shown once, inside the HUD, not in a tutorial screen.
- **First 60 s:** land a 2-move combo on someone and take a hit. A big, readable hit effect on the first landed move.
- **First 3 min:** a kill, a death, a respawn straight back in, and the ultimate meter visibly filling.

## Loop tuning
- **Cooldowns:** core moves at 4-12 s, so a player always has something available but must choose. If players mash everything off cooldown, lengthen the longest two. `[analysis]`
- **Ultimate meter:** fill in about 60-120 s of active fighting. Faster and ultimates stop being events; slower and many players never see theirs.
- **Time to kill:** a full combo should take 20-35% of a health bar. Kills should take 2-4 exchanges, so a fight has a turn or two of comeback.
- **Respawn:** under 3 s, near but not inside an active fight, with 1-2 s of spawn protection.
- **Server size:** 12-20 players so there is always a fight, but not a crowd so dense nobody can read anything.

## Depth and mastery
- **The skill chain:** single moves → a 2-move combo → block and counter → dash-cancel → combo extensions → reading which kit an opponent is and what they will do → baiting cooldowns.
- **The depth multiplier:** kit × kit. Each pair of kits should create a different matchup problem (a zoner against a rusher). Combined with player tech, this is where the game's life lives.
- **Defense must exist.** A block or counter with a clear window keeps fights from being "whoever hits first."
- **One "tech" per kit** that rewards practice keeps players learning after they have the basics.

## Retention engine
Pick at least two:
- **A new kit on a visible cadence**, announced in the title tag.
- **Kill streaks** shown on the nameplate and announced server-wide.
- **Kit mastery tracks** with cosmetic rewards (an alternate color, a finisher).
- **Emotes as flex**, earned or bought.

## Solo-first adaptation
- **Bot brawlers** that roam, pick fights and use their kits with human-like timing, so an empty server still plays.
- **A training room** with dummies that block, dodge and counter on settings, so a player can learn combos alone.
- **Fill new servers with bots** until humans arrive, and remove them as the server fills.

## Roblox notes
- **Readability at scale:** 15 players using effects at once turns into soup. Scale effects to importance: ultimates big, basic moves small.
- **Latency:** resolve your own hits on the client for feel; use server confirmation with lag compensation. Combos that drop at 150 ms will be blamed on the game.
- **IP risk:** the category grew on recognizable anime kits. Original kits with a strong theme avoid takedowns and stand out from the clones.
- **Like ratio:** The Strongest Battlegrounds sits at 83.7% `[RBX]`, lower than most hits. Balance swings and new-player stomping drag it down.
- **Monetization:** cosmetics, emotes, private servers. Never sell a kit that is stronger than free ones.

## Craft techniques
- **Hit-stop and camera nudge** on every landed move, larger on launchers and ultimates.
- **Ragdoll** on knockout for the comedic and clip value.
- **Unique silhouettes per kit:** a player should recognize a kit from its first move animation.
- **Audio identity per kit:** each kit gets its own impact sound family.
- **Kill feed with kit icons**, so players learn which kits are beating them.

## Pitfalls
- Dropping a new kit that beats every existing one.
- Effects that hide hitboxes.
- No block or counter, so fights are coin flips.
- Spawn camping with no protection.
- Building kits on someone else's IP.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Spawn straight into a fight | Time from death to next landed hit. |
| 4 moves, an ultimate, a findable combo | Did a naive tester land a 2-move combo within 2 minutes without help? |
| Tech depth for veterans | Is there at least one cancel or extension per kit? Can a tester describe it? |
| Big readable hit effects, scaled | Screenshot a 6+ player fight on a phone view. Can you see who is hitting whom? |
| New kit on a visible cadence | Is the next kit or update named anywhere in game? |
