---
name: de-ai-feel
description: Rules and tuning process for controls, movement, combat, timing, sound, effects, camera, and mobile controls in Roblox games so playing feels hand-tuned rather than generic. Use before building or tuning any player action.
---

# De-AI: game feel

## Why
A game can look great and still feel generic. Generic feel looks like this:
- floaty movement
- silent actions
- hits that don't land
- the same default Roblox jump
- menus that pop in with no motion

Games fail on feel even with a good theme: a chore-like core action with no satisfying moment (scrubbing a mess with no pop, no splash, no payoff) makes players quit. Feel is the first thing a player judges, within 10 seconds.

## The core rule
**The core action must feel good with no UI, no upgrades, and nobody else online.** Build and tune it first, before any feature, progression or menu. If the bare action isn't fun to repeat for a minute, nothing on top will save it.

## Every player action needs
- **Instant response.** Input is acted on the same frame. Use client-side prediction for anything timing-sensitive; the server checks the result afterwards.
- **Anticipation:** a short wind-up or squash, so the action reads.
- **Sound:** layered and varied, at least 2-3 variations per action so repeats don't sound robotic. Use no silent actions.
- **A visual effect:** particles, a flash, a trail or a decal at the point of impact.
- **For big moments:**
  - hit-stop, a 40-90 ms freeze
  - screen shake sized to the impact
  - a small camera punch or FOV kick
  - a heavier sound
- **Follow-through:** recovery frames, settling dust, a lingering mark.

## Movement and camera
- Replace or tune Roblox defaults on purpose: walk speed, acceleration, jump arc and air control should all be chosen for this game.
- The camera frames the action deliberately (offset, smoothing, collision) and never fights the player.
- UI motion matches the world, whether that's a snap, stamp, slide or flicker. Nothing just appears.

## Tuning process
1. Put every feel number in **one config module**: speeds, timings, forces, shake strength, hit-stop length.
2. Tune in short loops: play 30 seconds, change one number, play again. Write down what changed and why in `progress.md`.
3. **Test under lag** with `set_network_profile` (e.g. 150 ms and 300 ms). Solo timing must still feel fair, and online play must stay readable.
4. **Test mobile controls** in the Device Simulator (`rbx-device-simulator-lua`, `capture_device_matrix`): thumb reach, button size, and no accidental taps.
5. **Check performance** with `get_scene_analysis` and the profilers. Stutter kills feel.

## Check it
Record or screenshot the best moment of a play session. Would someone clip it and share it? If not, push the feedback further: more contrast between small and big moments, a better sound, a stronger freeze.
