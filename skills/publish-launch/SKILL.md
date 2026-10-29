---
name: publish-launch
description: "The launch flow for a Roblox game: the testing gate, private publish, early testers, the staged soft launch (private, then public with Friends only, then public excluded from Recommended For You, then fully public), when to go public, Share Links, Standout Games nomination, and the day 0 to day 7 watch list with what each signal means. Writes the launch checklist in STORE-PAGE.md. Use when planning or running any launch or major chapter release (load publish first for the go-public gate)."
---

# Launch

Load `publish` first. **Every step below that publishes, changes visibility, invites testers or submits anything needs the user's OK for that step.** The flow has at least two: before the private publish, and before going public. Each stage of the soft launch is also a visibility change and gets its own OK.

## Why a staged launch
Home recommendations test a new game on small cohorts and widen distribution if they engage. Roblox says a weak start isn't penalized and the system keeps retesting, but each test spent on a broken first minute is wasted time at the moment the game is newest. A staged launch finds the crash, the confusing door and the phone layout bug with a few dozen known players instead of the first thousand strangers.

## How facts are marked
**Policy (official, checked 2026-10):** from Roblox docs and staff posts; re-check before a decision. **Measured (third-party):** traffic data from a tracker, not from Roblox. **Design judgment:** reasoning, not measured.

---

## Stage 0: The testing gates (block everything)
There are two gates, because some checks can only run on a published place: DataStores don't work in Studio on a never-published place, `game.PlaceId` is 0 until the first publish, and analytics only record from published games.

**Gate A, before the first private publish of a new game:**
- [ ] A `testing` milestone run produced a `TEST-REPORT.md` with **no Critical failure.** Saving and analytics may be marked "pending the private build". That is not a pass and not a waiver; Gate B must clear them. This is acceptable only because a private publish reaches nobody but the owner and collaborators.
- [ ] Products and prices in the place match the **approved** price table in `ECONOMY.md` (or the game sells nothing yet).
- [ ] The creator account is age-checked, and the avatar setting is R15 Only (`publish-compliance`).
- [ ] The store-page draft in `STORE-PAGE.md` exists with a real icon and at least 3 real thumbnails.

**Gate B, before going public (and before every publish of an already-public game):**
- [ ] A `testing` run of **Phases 0 to 11 on the published place** produced a `TEST-REPORT.md` with **no Critical failure** and **no NOT RUN on saving or exploits.** On a published place the Phase 0 DataStore guard protects real data; never skip it.
- [ ] **`PREPUBLISH-CHECKLIST.md`** (in the `testing` skill folder) is complete, with any waivers written and dated by the user. Critical items can't be waived.
- [ ] The DataStore name was restored and confirmed after testing (the checklist's first Critical item).
- [ ] Products and prices in the live game match the approved table in `ECONOMY.md`.
- [ ] The compliance checklist in `publish-compliance` is complete and the questionnaire was submitted (with OK).

Don't copy the testing checklist into `STORE-PAGE.md`; link the `TEST-REPORT.md` and record its verdict.

If any box is open, stop and tell the user what is blocking. Never publish around a failing gate.

## Stage 1: Private publish (OK 1)
**Policy (official, checked 2026-10):**
- First publish is File > Publish in Studio: name, genre and subgenre, description, icon, thumbnail.
- Places are capped at 100 MB.
- **At most 5 never-released games can be released per account per day.**
- New games are private: the owner, Edit collaborators and permitted community roles only.
- The publishing account must be age-checked.

**Steps:**
1. Gate A is clear. Ask: "OK to publish this build privately?" Wait.
2. Publish. For a game that was published before, confirm first that the open place is the one linked to the live experience (`game.PlaceId` is not 0). How to publish from a second Studio window is studio-specific: read `studio-profile.md`.
3. After publishing, confirm the new version appears in Creator Hub version history, and that `game.PlaceId` is now set in the open place.
4. **Run Gate B on the published private place:** the full `testing` pre-publish run, plus a join through the Roblox client (not Studio) to check that analytics events arrive (`live-ops-analytics` has the checks), that a real purchase path works, and that saving works across a rejoin. Fix, re-test, and republish privately (each publish with OK) until Gate B is clear.

## Stage 2: Early testers
**Policy (official, checked 2026-10):**
- Playtest tab: turn on playtesters. Edit and Playtest collaborators plus invited early testers can play.
- Invite up to **10** friends or Trusted Friends as early testers. Age-pairing rules apply (for example, 18+ users can add 16+ friends). A preview watermark shows. Manage them through Manage Collaborators.

**Steps (each invite and access change needs OK):**
1. Ask the user who to invite. Never pick testers yourself.
2. Ask testers for three things only: where they got confused, when they first had fun, and whether they'd come back tomorrow.
3. Fix what they find, re-run the relevant `testing` phases, republish privately (with OK).

## Stage 3: Public, Friends only (OK 2)
**Policy:** in the Public tab, the "Friends" setting limits play to friends and Playtest users.
1. Gate B is clear. Show the user the testing verdict, the store-page preview and the early-tester findings (the overview format in `publish`).
2. Ask: "OK to make the game public, limited to friends?" Wait.
3. Watch the first sessions. Fix anything Critical before widening.

## Stage 4: Public, excluded from Recommended For You
**Policy:** Audience > Advanced Settings can exclude a public game from Recommended For You.
1. With OK, turn Friends off and keep RFY excluded.
2. Drive a small known audience: the game's community (group), Discord, DevForum, and **Share Links** in every off-platform post (they attribute traffic and earn Audience Expansion rewards; see `economy-monetization`). Posting anywhere is a `marketing` action and needs its own OK.
3. Read the onboarding funnel and D1 retention (`live-ops-analytics`).
4. Optional: a small Ads Manager test. **Policy:** sponsored traffic doesn't count toward RFY signals and doesn't hurt them, so it is a safe way to measure thumbnail pull. It costs money: ask first.
5. Optional: a paid-access closed beta is a documented use, but it blocks private servers.

**Soft launch length:** 1 to 2 weeks (design judgment).

**Gates before turning RFY on (design judgment; the docs' example treated a 70% drop as a problem):**
- [ ] The onboarding funnel loses under 30% of players before the first meaningful action.
- [ ] First-play bounce (leaving within 3 minutes) has been examined and the obvious causes fixed.
- [ ] No crash, softlock or save bug reported in the soft launch.
- [ ] At least 2 active thumbnails for personalization (`publish-store-page`).

## Stage 5: Public with RFY on
**Policy (official, checked 2026-10):** the algorithm tests the game on small cohorts and widens distribution if they engage. Only players who arrive organically from RFY count, and all signals are per-user averages, so small games aren't disadvantaged.

**When (design judgment, based on measured traffic):**
- Roblox's docs give **Saturday** as the weekly peak. A third-party tracker (RoWatcher, 89 days) measured the peak at about **Saturday 19:00 UTC** (~16M concurrent) and the trough at about Tuesday 08:00 UTC (~7.3M); weekend days average 12.2 to 12.5M, weekdays 8.7 to 9.8M, with Friday and Monday higher than Tuesday to Thursday. [Measured, third-party]
- **Turn RFY on Thursday or Friday, U.S. afternoon.** Bugs surface before the weekend, and the cohort tests run into peak traffic.
- **Ship chapter updates Friday or Saturday, 15:00 to 17:00 UTC,** before the peak.
- Avoid launching against platform-wide mega-events or the opening week of a trend wave, unless you can ride it.
- Late June to August and the December holidays bring more traffic and more competition. Roblox's seasonality notes include a U.S. back-to-school dip.
- Only launch when someone can watch and fix for the next 48 hours.

Ask: "OK to turn on Recommended For You at <day, time>?" Wait.

## Day 0 to day 7 watch list
The full analytics process (pulling KPIs, benchmarks, the weekly report) lives in `live-ops` and `live-ops-analytics`. This list is what to look at during launch week and what each signal says about the **launch and store page.**

| When | Watch | Where | If it's bad, it usually means | Do |
|---|---|---|---|---|
| First 4 hours | Crashes, error reports, DataStore errors, purchase failures | Error Report, server logs, Monetization | A bug the soft launch missed | Hot-fix (config if possible, republish with OK). Pause wider promotion. |
| First 4 hours | Onboarding funnel step 1 to 3 | Funnels | Players don't understand the first action | Fix the first minute before anything else |
| Day 1 to 3 | **Play-through rate (PTR)** vs benchmark | Acquisition > Home Recommendations | The icon or thumbnails don't earn the click, or show the wrong audience | Add or swap thumbnail variants (`publish-store-page`, with OK) |
| Day 1 to 3 | **First-play bounce** (leaving in under 60 s or 61 to 180 s) | Home Recommendations | The page promised something the first 3 minutes don't deliver, or the first 3 minutes are slow | Make the page more honest, or make the opening faster. **The first 3 minutes decide the signal.** |
| Day 1 to 3 | Impressions trend | Home Recommendations | Normal lag of a few days after changes | Don't panic-change things; impression changes lag |
| Day 2 to 7 | **D1 retention and D2 to 7 play days** | Retention, Home Recommendations | No reason to come back | Add a return hook (next-chapter teaser, a daily objective) |
| Day 2 to 7 | Playtime per user (capped at 60 minutes per user per game per day for ranking) | Engagement | Sessions end early; content runs out | Check where sessions end in the funnels |
| Day 3 to 7 | Payer conversion, shop funnel | Monetization, Funnels | Shop hidden, or prices misjudged | Review with `economy`; never add power to fix it |
| Day 7 | Everything above | | | First `WEEKLY-REPORT.md` with `live-ops-analytics` |
| Daily | "Reduced exposure" banners, moderation messages | Creator Dashboard | A compliance or metadata problem | Fix per `publish-compliance`; tell the user the same day |

**Policy facts behind the table (official, checked 2026-10):** RFY's most important signals are PTR, first-play bounce, play days per user (D1, D2 to 7, D8 to 28) and playtime per user. Also important: intentional co-play days (private and reserved server sessions count since December 2025), qualified play sessions, spend days and Robux spent per user. In 2026 Roblox is optimizing for **28-day retention** and ranks "deeper, returnable games for older players" higher. Naming drift: the docs say PTR plus first-play bounce, while the thumbnail docs still say qPTR (qualified play-through rate); the dashboard moved to session-level qPTR, which reads lower.

**One change at a time.** Changing the thumbnail, the opening and the shop in one day makes the week's data unreadable.

## Standout Games nomination
**Policy (official, checked 2026-10):** Standout Games is a hand-curated row of "novel" games on the second row of Home, with video previews. Nomination is by a survey, reviewed on a rolling basis.

**What Roblox asks for:**
- underrepresented genres (RPG, strategy, puzzle, shooter)
- deep mechanics with a metagame
- distinctive visuals
- console and mobile optimization; R15 or custom rigs; regular updates and events

**Prepare:** gameplay footage, a trailer (`marketing`), localization (`publish-store-page`), and thumbnails reviewed against Roblox's best practices.

**When:** after first traction and localization, once the game has shipped at least one update (design judgment). For a distinctive, deep 16+ game this is often the best organic lever available.

**Submitting the survey is an outward action: draft the answers in `STORE-PAGE.md`, show the user, submit only with OK.**

## Chapter and major updates
Each is a small launch:
- re-run the `testing` gate
- new thumbnails showing the new content, plus a one-line update note in the description (`publish-store-page`)
- resubmit the questionnaire if any answer changed (`publish-compliance`)
- new cosmetic row and any new SKUs through `economy`
- an update announcement and event through `live-ops-updates`
- ship before the weekend peak; every publish needs OK

## What great looks like
- The first stranger to play gets a build that dozens of players already finished.
- RFY goes on with every gate green, on a Thursday or Friday, with someone watching.
- Launch-week changes are one at a time, each tied to a signal.
- Every OK is recorded with its date in `STORE-PAGE.md`.

## Common mistakes
- Going straight from private to fully public.
- Turning on RFY on a Saturday night, then finding a save bug on Sunday with nobody around.
- Reading day-1 impressions as a verdict; they lag.
- Posting off-platform without Share Links, losing attribution and Audience Expansion rewards.
- Hitting the 5-new-releases-per-day limit by publishing test copies as new games.
- Nominating for Standout before localization and a trailer exist.
- Treating the soft-launch OK as permission for every later stage.

## Output
Fill the Launch checklist and Launch log sections of `STORE-PAGE.md` (from `publish/STORE-PAGE-TEMPLATE.md`). At each stage, give the chat overview defined in `publish`, ending with the one specific question for the next step.

## Sources
Roblox Creator Hub (read 2026-10-29): publish experiences and places, discovery and discovery FAQ, Standout Games, analytics. All under `https://create.roblox.com/docs/`.
DevForum staff post on the improved Recommended For You algorithm and analytics (2025-03-31, updated 2025-12-11).
Roblox investor relations: Q1 2026 shareholder letter; RDC 2026 newsroom post.
RoWatcher weekly traffic map (third-party measurement).
