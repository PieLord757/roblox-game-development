# Rage climb (`rage-climb`)

Read the `rage-climb` entry in `../CATEGORIES.md` first. It holds the must-haves, exemplars and targets. This file is the craft: how to make this kind of game as good as it can be.

**In one line:** a vertical climb with an awkward but precise control scheme, where one mistake can drop you far below and every fall is your own fault.

**Evidence note:** sourced data is thin (Getting Over It 4,959 `[SC]`, Chained Together 92,186 `[SC]`, Only Up! `[UNV]`). Much of this guide is `[analysis]` from how those games are built and why they spread through streams.

---

## What great looks like
- **The controls are the content.** Getting Over It gives you one verb: a hammer swung with the mouse. It feels impossible for ten minutes, then suddenly it doesn't. That "I can do this now" moment is the whole reward, and it comes from the player's hands, not from an unlock.
- **A fall is a story.** The best falls drop you past three sections you remember clearing. Watching it happen (to yourself or a streamer) is painful and funny at once. That reaction is why the genre spreads through clips.
- **The map is a ladder of named places.** Players say "I lost it at the orange" or "I made it past the furniture." Landmarks give a fall its weight and give progress its language.
- **Nothing is random.** On replay, every fall was a misjudged swing or jump. The game is harsh but never unfair, so anger points at yourself and you try again.

## The hook
- **First 10 s:** the player is moving with the unusual verb, and the first small ledge is reachable. The verb must be in the player's hands immediately, with no menu.
- **First 60 s:** a first clear "I did that" climb of a few meters, and a first small fall that costs a few seconds, so the player learns falls exist before they cost much.
- **First 3 min:** the first real landmark reached, the height counter visibly higher, and a view upward showing how far there is to go.

## Loop tuning
- **Fall cost curve:** early falls should cost 10-30 s of progress. The first fall that can cost 5+ minutes should come only after the player has demonstrated control (roughly after the first 10-15 minutes). Ramp the cost, don't start with it. `[analysis]`
- **Section length:** design in sections of 20-60 s of climbing for a skilled player, each with one new obstacle idea. A section that takes a skilled player over 2 minutes is too long to retry.
- **Catch ledges:** place "safety nets" below the hardest sections so most falls land a section down, not at the bottom. Remove or narrow them higher up for the climax. The placement of catches is the main difficulty dial.
- **Verb tuning:** the verb should have a learning period of about 5-10 minutes before it feels controllable. If playtesters still feel helpless at 20 minutes, the verb is too hard; if it feels natural at 2 minutes, there is no climb.
- **Tune in big steps:** if a section causes too many bottom-falls, move the catch ledge, don't shave the gap by a few studs.

## Depth and mastery
- **The skill chain:** basic control of the verb → reliable small moves → recovering mid-fall → committing to big moves → optimized routes → speedrun tech.
- **The depth multiplier:** verb × terrain types. Each surface (slippery, moving, sloped, tiny) should change how the verb behaves, so the same verb gets new problems all the way up.
- **Hidden tech:** let skilled players discover moves the game never teaches (a launch, a slingshot). Speedrunners turn these into a second game.

## Retention engine
Pick at least two:
- **Personal best height and best time**, always on screen.
- **Leaderboards** for summit time, with ghost replays of the top runs.
- **A summit reward** that is visible on the player afterwards (a cosmetic, a title, a mark in the lobby).
- **New climbs** on a cadence, or player-made climbs. A single solved climb has no tail (Chained Together's single level faded faster than games with variety `[analysis]`).

## Solo-first adaptation
- The genre is natively solo. Other players are best as an audience: seeing someone else's height in the same server, or a ghost of a friend, adds tension without adding requirements.
- Shared servers where everyone climbs the same tower create spectators for every fall, which is the comedy, without any co-op dependence.
- Avoid physical interaction between players (knocking others off) in the main mode. It moves the blame for a fall from the player to someone else and breaks the core promise.

## Roblox notes
- **Physics ownership:** the climbing body must be simulated on the client the player controls, or swings and jumps will feel delayed. Validate positions loosely on the server to stop teleport cheats.
- **Mobile:** an analog verb (a swing, an aim) needs a dedicated touch control, such as a drag-to-swing area. Test with a thumb before committing to the verb.
- **Saving:** save height and a recent checkpoint periodically, so a disconnect does not feel like a fall. A disconnect is the game's fault; a fall is the player's.
- **Monetization:** cosmetics and summit flair. Never sell checkpoints or skips in the main climb: that sells away the meaning of the summit. Optional practice tools are fine.
- **Discovery:** a thumbnail of someone mid-fall from a great height says the whole game.

## Craft techniques
- **Make height readable:** a height meter, plus visual bands in the world (color shifts, weather, sky changes) so a screenshot tells you how high someone is.
- **Fall feedback:** a whoosh that rises in pitch with fall speed, a heavy landing sound, and a camera that stays on the player during the fall. Never cut away; the fall is the drama.
- **Commentary or voice:** a narrator or ambient lines that react to falls (as in Getting Over It) give the frustration a companion. Keep lines rare so they stay sharp.
- **Landmark design:** each section has a distinctive object or color so players can name it.
- **Recovery moments:** design spots where a skilled player can catch themselves mid-fall. These become the best clips.

## Pitfalls
- Random physics (a jitter, a joint that sometimes snaps) causing falls. One unexplained fall can end a session for good.
- A verb that is awkward but not precise. Awkward is the starting state; precise is the destination. If it never becomes precise, it is just bad controls.
- One climb and nothing after the summit.
- Selling skips. It cheapens the summit for everyone, including those who paid.
- Making the first 5 minutes punishing. Players must taste control before they taste loss.

## Playtest checks for the audit
| Must-have | What to look for in the playtest |
|---|---|
| One unusual, precise verb | Does a new tester go from helpless to in control within 10 minutes? Record their first and tenth minute. |
| Visible, dramatic, non-random loss | Watch 5 falls. Can the tester say why each happened? Any "I don't know what happened" scores 0. |
| Height and personal best always shown | Is height on screen at all times, and is the best height shown? |
| Funny or spectacular falls | Does the camera stay on the fall? Does a tester laugh or react aloud? |
| Every fall is the player's fault on replay | Rewatch recorded falls. Count any caused by jitter, lag or randomness. |
