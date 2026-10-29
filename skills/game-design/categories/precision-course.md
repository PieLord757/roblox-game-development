# Precision course (`precision-course`)

Read the `precision-course` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** an authored course of jumps and timing where you die, respawn instantly and try again until your hands learn it.

---

## What great looks like
- **Failure costs nothing.** Celeste (7,720 `[SC]`, 24% ret) respawns you in a blink at the start of the screen. A hundred deaths on one screen feel like practice, not punishment.
- **The game does what you meant.** Celeste's coyote time and input buffering let a jump pressed a few frames late still work. Players never see this; they just feel the controls are "fair".
- **Player-made levels keep it alive.** Geometry Dash (108,707 `[SC]`, 40.3% ret) runs on a creator ecosystem of rated, ever-harder levels and creator celebrity. The developer could never make that much content.
- **Frustration has a price.** Tower of Hell (29.3B visits `[RBX]`) draws huge volume with no checkpoints and a reset timer, but sits at 73.6% liked. Rage drives clicks and costs goodwill.

## The hook
- **First 10 s:** the player is jumping. No menu, no story card.
- **First 60 s:** the first stage cleared and the first new idea introduced (a moving platform, a dash).
- **First 3 min:** several stages cleared, the stage counter climbing, and the first section that takes a few tries. The player has died and immediately retried without thinking about it.

## Loop tuning
- **Respawn:** under 1 s, at the start of the current section. Every extra second of respawn loses players.
- **Section length:** 5-20 s of play per section for hard content; longer sections only when easy.
- **Difficulty curve:** a sawtooth. Introduce an idea safely, test it, twist it, then drop difficulty when the next idea arrives.
- **Forgiveness numbers:** coyote time of about 0.1 s and a jump buffer of about 0.1 s are common starting points `[analysis]`; tune by feel. Hitboxes slightly smaller than the visible player, hazards slightly smaller than their art.
- **Checkpoints:** before every hard section, never after a long easy walk.
- **Tune in big steps.** If a jump feels floaty, double gravity on the way down before touching anything else.

## Depth and mastery
- **The skill chain:** run → jump → jump timing → air control → each new movement idea → combining ideas → speed tech and skips.
- **The depth multiplier:** movement verbs × level elements. Each new element (a spring, a conveyor, a wind zone) should combine with every verb in a new way.
- **Optional mastery:** collectibles off the main path, harder remixes of levels, time trials. The main path stays reachable for most players; the optional path holds the hardcore.

## Retention engine
Pick at least two:
- **Player-made levels** with ratings and difficulty tiers.
- **Time trials and leaderboards** per stage.
- **Collectibles** and harder remixes.
- **Daily or weekly courses** shared by everyone.

## Solo-first adaptation
The genre is solo by nature. Strangers on the same course are a bonus (racing, watching someone ahead fail the jump you are about to try). Ghosts of other players' best runs add competition without needing them online.

## Roblox notes
- **Crowded genre:** the classic obby is the most crowded format on the platform. A distinctive movement verb or structure is required to stand out.
- **Default movement:** Roblox's default character controller is serviceable but generic. Tune jump power, gravity and air control, or build a custom controller, for real precision.
- **Latency:** keep movement and hazards on the client where possible so jumps feel instant; validate progress on the server.
- **Mobile:** jump and one special move as large buttons. Avoid courses that need precise camera control on a phone.
- **Monetization:** skips and cosmetics are common. A paid skip should never be the only way past a section; it should save time, not replace skill.

## Craft techniques
- **Readable hazards:** one color or material language for "this kills you", used everywhere.
- **Teaching by layout:** place the first instance of a new hazard where failing is safe, before it appears over a pit.
- **Death feedback:** a quick, satisfying death effect and sound. Deaths happen hundreds of times; they must not be annoying.
- **Progress display:** stage number, a progress bar across the course, and a personal best.

## Pitfalls
- Floaty or laggy controls.
- Checkpoints in the wrong place, after long easy stretches.
- A first stage that is hard.
- No new content and no player-made content.
- Rage as the whole design, which buys volume and costs likes.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| Respawn under 1 s | Time from death to control again. |
| Tight controls with forgiveness | Record jumps pressed slightly late off an edge. Do they work? |
| Visible stage number or progress | Is progress on screen the whole time? |
| One idea per section, then a twist | Map the first 10 sections: what is each one's idea? |
| Optional harder content | Is there an optional route, collectible or time trial visible? |
| Long tail | Is there a daily course, a leaderboard or player-made levels? |
