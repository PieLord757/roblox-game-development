# Pre-publish checklist

Run this in Phase 11 of a pre-publish test run on the published place, after a plain sync from disk. It is part of Gate B in `publish-launch`: before going public, and before every publish of an already-public game. The first private publish of a new game follows Gate A instead, because saving can't be tested on a place that was never published. Every box must be checked, or carry a written waiver from the user (with the date) in `TEST-REPORT.md`. **Any Critical item that isn't checked blocks publishing. Critical items can't be waived.**

Roblox publishes no official pre-publish checklist. This one combines Roblox's documentation with common launch failures.

Never publish without the user's explicit OK, even when every box is checked.

## Data and saving
- [ ] **(Critical)** The DataStore name equals the original recorded in Phase 0, confirmed in edit mode with `execute_luau` after a plain sync from disk.
- [ ] **(Critical)** Studio was re-synced from disk after the last edit made during testing, so the place matches the files on disk.
- [ ] **(Critical)** Saving passed in Phase 4 on the published place (not NOT RUN). Rejoin keeps all progress.
- [ ] New, old-schema and corrupted profiles all load without wiping data.
- [ ] `BindToClose` saves every player in the server.
- [ ] Saves retry with backoff, and a failed load never leads to defaults being saved over real data.
- [ ] Rejoining quickly into another server can't duplicate items (session lock, or an equivalent guard).

## Economy and monetization
- [ ] **(Critical)** `ProcessReceipt` is idempotent: replaying a receipt grants once.
- [ ] Developer products and game passes exist, are on sale, and have the right prices.
- [ ] Studio-only purchase simulation is guarded by `RunService:IsStudio()`, and the live path is the real one.
- [ ] No buy-then-sell or trade loop makes a profit. The earning curve matches the design.

## Security
- [ ] **(Critical)** Exploits passed in Phase 6 (not NOT RUN): no hostile call changed any state.
- [ ] Every remote is in the remote table with validation, a rate limit and a PASS verdict.
- [ ] No server logic or trusted data under ReplicatedStorage or Workspace.
- [ ] No `loadstring`, debug remotes, admin commands or HttpService debug paths reachable in a live build.
- [ ] **(Critical)** Dev hooks are inert outside Studio (the `IsStudio()` guard is verified, not assumed).
- [ ] The unit test folder and test cases are gone from the place.

## Flow
- [ ] **(Critical)** The full loop completes solo with bots, 3 rounds in a row, 0 errors.
- [ ] The loop works with 2 to 3 clients, including a mid-round join and a mid-round leave.
- [ ] Intros wait for the client to say it's ready. No first-frame remotes are lost.
- [ ] Respawning, resetting and dying work in every phase. A seated player can be teleported.
- [ ] First-time-player test: at least 2 of 3 reached the fun; no dead ends.

## Platform and UI
- [ ] Phone, tablet, console and the smallest device pass the UI scan. Portrait checked if the game allows it.
- [ ] The HUD clears the top bar, the notch and the thumb controls. Legacy chat doesn't cover the HUD.
- [ ] Gamepad navigation reaches every button. Touch targets are at least 44 px.
- [ ] Text responds to `PreferredTextSize` (code check), or a manual large-text check is waived in writing.
- [ ] Visuals that depend on BillboardGuis, Highlights or SurfaceGuis were checked by property, since captures don't show them. SurfaceGui faces point the right way.

## Performance
- [ ] No growth in `LuaHeap` or instance count across 3 rounds. Server heartbeat about 60 at the player cap.
- [ ] No regression over 20% against the last baseline.
- [ ] StreamingEnabled is set on purpose, with the reason written down.
- [ ] A person has checked the game on a real phone, or the gap is waived in writing.

## Publishing
- [ ] The place being published is the one linked to the live experience (`game.PlaceId` is not 0). A reopened local file isn't linked.
- [ ] Analytics funnel steps are logged from the server (they only send from published games, not Studio).
- [ ] Icon, thumbnails, description and age rating are set.
- [ ] After publishing, the new version appears in Creator Hub version history.
- [ ] All playtest windows are closed, and network and device simulation are reset.

Studio-specific steps (how to sync, how to publish from a second Studio window, where version history lives) belong in `studio-profile.md` at the project root, if it exists.

---

# Launch-day bugs to pre-empt

These are the bugs that most often hit a Roblox game in its first day live. Before publishing, check that each cause has been ruled out, and name the test that ruled it out.

| Bug players see | Usual cause | Ruled out by |
|---|---|---|
| Players lose their progress | Test DataStore name left in; no `BindToClose`; saves on `PlayerRemoving` throttled at scale (the budget is 60 + 40 × players requests per minute per server) | Phase 11 store check; Phase 4 save-all and rejoin |
| First players to join see a broken intro | A remote fired before the client connected | Phase 5 intro gate with a slow client |
| Exploiters max out currency on day one | NaN or negative amounts accepted on a sell or claim remote | Phase 6 non-finite and range attacks |
| Mobile players can't press the main button | It sits under the notch or the jump button, or is offset-sized off-screen | Phase 8 UI scan on the smallest phone |
| Server memory climbs until the server crashes | Player tables never cleared; connections never disconnected | Phase 9 round 1 vs round 3 memory |
| Items are duplicated | No session lock when rejoining quickly into another server | Phase 4 quick-rejoin case |
| A purchase grants twice, or not at all | `ProcessReceipt` not idempotent, or the grant can half-fail | Phase 1 receipt test; Phase 6 replay |
| The game stalls for players with bad connections | A RemoteFunction with no timeout; a spinner that never ends | Phase 7 under `poor` and custom profiles |
| Old servers keep running old code after an update | Saves aren't robust across schema versions | Phase 4 old-schema migration test; plan how servers move to the new version before shipping a schema change |

List any unchecked box or waiver in the chat overview at the end of the run, one plain sentence each.
