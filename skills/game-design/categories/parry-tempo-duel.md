# Parry-tempo duel (`parry-tempo-duel`)

Read the `parry-tempo-duel` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a single timed input against a threat that speeds up every exchange, until one player misses.

---

## What great looks like
- **A stranger understands it from one exchange.** Blade Ball's homing ball turns red toward a player, they click, it flies to someone else faster. Nobody needs a tutorial; watching one deflection teaches the game.
- **The last two players are a show.** When the field is down to a 1v1, the ball is moving so fast that each parry is a coin flip of nerve. Everyone dead is watching, and that rally is the clip people post.
- **The tension curve is built into the physics.** Every successful parry raises the speed, so every round climbs from calm to frantic without any designer scripting it.
- **Abilities change the read, not the result.** A dash, a curve shot or a brief freeze gives you a way to bait an opponent's timing, but a perfect parry still beats any ability.

## The hook
- **First 10 s:** the player is in a round or a practice lane, and the threat targets them within seconds. The parry input is one button or one tap, shown once on screen next to the threat, not in a menu.
- **First 60 s:** at least 3 successful parries and one miss. The miss should feel fair: the player saw the tell and was late.
- **First 3 min:** a full round, a placement, a currency payout, and a visible next unlock (an ability or a cosmetic trail).

## Loop tuning
- **Parry window:** start generous (about 250-350 ms of valid input) at low speed and shrink it as speed rises, down to about 120-150 ms at the top. If players feel robbed at high speed, the window shrank faster than the visual tell did. Tune both together. `[analysis]`
- **Speed ramp:** each parry multiplies speed by a fixed step. Tune the step so a typical round lasts 60-120 s. If rounds drag, double the step; if the first exchange already feels frantic, halve it.
- **Target selection:** the threat should pick a target with a clear rule (nearest, last to parry, random among living). Random is fine if it is announced with a tell before it moves.
- **Round reset:** rematch in under 10 s. Dead players should respawn into a lobby where they can practice parries against a slow ball while they wait.
- **Lobby size:** 6-16 players per round. Fewer than 6 and rounds end too fast; more than 16 and most players wait too long between targets.

## Depth and mastery
- **The skill chain:** react to the tell → parry early enough → parry late on purpose (to send it faster) → aim the parry toward a specific opponent → bait with movement → read the other player's rhythm in a 1v1.
- **The depth multiplier:** parry timing × positioning. Where you stand changes how much time you get, so distance becomes a resource. Abilities multiply this by moving you or the opponent.
- **Late parries should be stronger.** A parry at the last frame sending the threat faster or curving it rewards nerve and creates a real skill gradient.
- **Avoid a single dominant ability.** If one ability wins most rounds, the parry stops being the skill.

## Retention engine
Pick at least two:
- **Win streaks** on the nameplate, reset on loss.
- **Ranked 1v1 mode** with visible tiers for the players who want only the duel.
- **Ability and cosmetic unlocks** earned by playing (trails, parry effects, explosion effects).
- **Daily challenges** that push variety ("win a round without using an ability").

## Solo-first adaptation
- **Bot opponents with human timing.** Give each bot a reaction time and a variance (for example 180-260 ms with jitter) and a chance to panic-parry early at high speed. A bot with perfect timing ends every round in a stalemate.
- **A solo ladder:** named bot duelists with styles (the early parrier, the curver, the baiter) give the empty-server player a goal.
- **Fill with bots in under 6 s** and keep the public queue open for humans.
- **Practice lane** with a speed slider so a player can train the high-speed window alone.

## Roblox notes
- **Latency is the whole game.** Judge parries on the client that owns the parry and validate on the server with a tolerance, or high-speed parries will feel stolen at 150 ms. Show the target's own client a slightly earlier tell to compensate. Test at 150 ms and 300 ms.
- **Mobile:** one large parry button in the thumb zone. A one-tap input is why this format works on phones.
- **Monetization:** abilities as side-grades earned in play, cosmetic sword and explosion effects for sale. Selling abilities that win rounds is the category's main failure.
- **Discovery:** the thumbnail is one player mid-parry with a streaking threat. The title names the verb.

## Craft techniques
- **The tell is audio plus visual.** A rising tone as the threat closes on its target, plus a color or outline change on the target player. Players parry by ear at high speed.
- **Hit-stop on the parry:** freeze both the threat and the parrying player for 40-80 ms on a successful parry, scaled by speed. It makes each parry feel like a hit.
- **Camera:** pull back slightly as speed rises so the player keeps the threat in view.
- **Spectator view:** when the final two remain, switch dead players' cameras to a wide shot of the duel, with a speed readout.
- **Miss feedback:** show where the window was (a brief flash on a timing bar) so the player learns whether they were early or late.

## Pitfalls
- A parry window that does not shrink, so high-speed rallies never end.
- Visual effects so heavy at high speed that the threat disappears in them.
- Abilities that stun or teleport the threat with no counter.
- Rounds where dead players wait 2+ minutes with nothing to do.
- Server-only parry checks that ignore latency.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| One input, legible in one exchange | Show a naive viewer one exchange on video. Can they explain the rule? |
| Tempo rises each exchange | Log threat speed per exchange across one round. Does it climb until a miss? |
| Clear target tell and window | Record a high-speed parry. Is there an audio and a visual tell before the threat arrives? |
| Rematch under 10 s | Time from round end to the next round's first target. |
| Abilities as side-grades | Did any ability win most rounds across 5+ rounds? Does a no-ability player still win? |
| Final 1v1 shown to everyone | When two remain, what do dead players see? |
