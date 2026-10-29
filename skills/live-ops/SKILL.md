---
name: live-ops
description: "Start here for running a Roblox game after it is built: tracking set up before launch, the launch window, and the weekly loop after launch. Explains the approval rule (nothing live changes without the user's OK), the platform policy facts that block updates, the three phases, and which sub-skill to load: live-ops-analytics (instrumentation, funnels, Home recommendation signals, benchmarks, WEEKLY-REPORT.md) or live-ops-updates (cadence, patch notes, events, notifications, chapter releases, configs and experiments, community, ROADMAP.md). Use before launch, at launch, and every week a game is live."
---

# Live ops (start here)

## Why this exists
Launching a Roblox game is the start of the work, not the end. Home recommendations, the main source of free players, score a game on what its players do each day: whether they stay past the first 3 minutes, whether they come back on days 2 to 7 and 8 to 28, and how long they play. A game that ships and then goes quiet loses its slot to games that keep improving.

Two things go wrong for small teams:
- **They fly blind.** No funnels were logged before launch, so when 70% of new players leave, nobody knows where. You can't add tracking after the fact and get the launch week back.
- **They update by gut.** They add a new mode because it sounds fun, while the real leak is a confusing door in the first room.

**The standard:** tracking is in and verified before the game goes public. After launch, every week ends with a one-page `WEEKLY-REPORT.md` (who came back, where players quit, the one thing to fix or add next) and an up-to-date `ROADMAP.md`. Every change is chosen from data plus a second signal, shipped on a schedule players can learn, and announced in specific words.

## The approval rule (read this first)

> **No outward or live action without the user's explicit OK, given in chat for that specific action.** Draft it, show it, ask, then act. An earlier OK does not cover a later action.
>
> This covers, at minimum:
> - **publishing** the place, including a private publish to check analytics (it is still a publish), and publishing any update;
> - **publishing a config** or rolling one back (it changes the live game within minutes);
> - **starting, stopping or completing an experiment**;
> - **creating, making public or editing an Experience Event**, and ticking **Submit for Featuring**;
> - **sending an update announcement or an experience notification**, or creating notification strings;
> - **posting** anywhere: Discord, the Roblox Community (group), Reddit, X, YouTube, TikTok;
> - **replying publicly** to reviews or players;
> - **changing the title, description, icon, thumbnails, maturity answers, Social Links or prices**;
> - **any Open Cloud write call** (configs, experiments, notifications, ads);
> - **spending** Robux or money of any kind.
>
> Reading dashboards, pulling read-only analytics, and writing drafts and reports in the repo need no approval.

If the user says "just ship it", confirm the exact list of what will change before you do it.

## Platform policy that shapes everything
**Policy (official, checked 2026-10):** facts from Roblox docs and staff posts. Re-check the linked source before relying on one of these for a decision; Roblox changes them often. The source links are in `live-ops-analytics` and `live-ops-updates`.

- **Updates need an age-checked creator account.** Since the Kids/Select launch (June 2026), pushing updates or publishing new content requires the publishing account to have passed Roblox's Facial Age Estimation. If it hasn't, no cadence is possible. **Check this before you plan a single update.**
- **Social links are shown only to age-checked users 16+** (since June 30, 2026). Discord, YouTube and other links go only in the Social Links settings. Game text, signs, chat messages and UI must never direct players off-platform ("join our Discord", invite codes). Developers have been warned for this.
- **Maturity labels decide who can play.** Minimal and Mild reach Kids and Select; Moderate reaches Select (9 to 15) and standard (16+); "Content May Vary" reaches age-checked 16+; **Restricted means age-verified 18+**, which shrinks the audience sharply and blocks some countries. Use Restricted only if the content truly needs it.
- **Experience notifications** are 13+ only, capped at one per user per experience per day, and ban dark patterns (fake urgency, disguised ads, bait-and-switch, trick purchases, gating gameplay on opt-in).
- **Update announcements** are 60 characters, at most one every 3 days.
- **Analytics only records from the server in a published place.** Studio and client calls do nothing. Limits are in `live-ops-analytics`.
- **The Analytics Query, Configs and Experiments Open Cloud APIs are beta.** Schemas may change; check the reference before building on them.

## The three phases

| Phase | When | What happens | Load |
|---|---|---|---|
| **Pre-launch** | From "the loop is fun" to the public release | Age-check confirmed. Maturity questionnaire done. Funnels, custom events and economy events planned against the limits, then built with `rbx-instrument-analytics`. Every tunable value moved into configs with `rbx-configs-experimentation`. Private publish (with OK) and verify events in View Events. KPI log and `ROADMAP.md` started. | `live-ops-analytics`, then `live-ops-updates` |
| **Launch** | Launch day to day 7 | First 4 hours: watch crash rate, Error Report, DataStore errors and the onboarding funnel. Hot-fix through configs (with OK). Day 3: first read of D1 and bounce. Day 7: first `WEEKLY-REPORT.md`. Marketing timing lives in `marketing`. | `live-ops-analytics`, `live-ops-updates` |
| **Post-launch** | Every week while the game is live | Pull KPIs, write `WEEKLY-REPORT.md`, pick one fix, update `ROADMAP.md`, triage bugs and feedback, plan the next drop, chapter or event. | both |

## Which sub-skill to load

| You need | Load |
|---|---|
| What to track and why, the funnel plan for chapters, the analytics limits budget, reading Home recommendation signals, benchmarks, turning drop-off into a fix, the weekly KPI pull, `WEEKLY-REPORT.md` | `live-ops-analytics` |
| Update cadence, patch notes, events and notifications, the chapter-release playbook, configs and experiments, bug intake, negative feedback, `ROADMAP.md` | `live-ops-updates` |
| The actual Luau for `AnalyticsService` events | built-in Roblox skill `rbx-instrument-analytics` (load with the `skill` tool) |
| The actual Luau for `ConfigService` and experiments | built-in Roblox skill `rbx-configs-experimentation` (load with the `skill` tool) |
| Trailers, clips, ads, creators, launch-day promotion | `marketing` |
| Testing a fix before it ships | `testing` |
| Publishing order, store page, maturity questionnaire and compliance | `publish` |
| Changing any price, product or reward | `economy` (the user approves the price list) |

The built-in skills cover how to write the code. These skills cover what to track, what to tune, how to read the results and what to do next. Don't copy their code here.

## Who does what
- **The build thread** instruments, pulls data, writes the report and roadmap, and drafts every announcement, event and notification.
- **The user** approves every live action (see the approval rule) and reads the chat overview each week.
- **A fresh reviewer agent**, when the stakes are high (a chapter launch, a price change), reads the weekly report cold and checks that the chosen fix follows from the numbers.

## What great live ops looks like
- **Tracking exists before players do.** The launch week is the most valuable data you will ever get. It is gone if the funnels weren't live.
- **One fix a week, chosen from data.** The biggest absolute loss in a funnel, confirmed by a second signal, with a written hypothesis. Not five changes at once, which makes every result unreadable.
- **A rhythm players learn.** Same weekday, same hour. The day after a release is reserved for fixes.
- **Specific words.** "Chapter 3: The Lower Wards is open" beats "Big update!". "Fixed the lift in the pumping station that trapped players on mobile" beats "bug fixes".
- **Configs over republishes.** A difficulty or timer change through a config takes minutes and can be rolled back. A republish takes a release slot.
- **The game respects the player.** No fake timers, no bait notifications, no rewards for likes. Players 16+ notice dark patterns and post about them.

**Common mistakes:**
- launching without funnels, then guessing
- acting on one day of data, or on the first 24 hours of an experiment
- reading D7 before the cohort has had 7 days
- comparing a story game's D30 against simulator benchmarks
- running an experiment at 200 DAU, where nothing can reach significance
- shipping three changes to the same area in one week, then crediting whichever you liked
- vague patch notes and too many announcements
- putting "join our Discord" anywhere in the game
- arguing with reviewers or banning critics

## Output
Every live-ops session ends with files in the repo and an overview in chat.

**Files** (in `design/<game>/liveops/` unless `studio-profile.md` names another place):
- `INSTRUMENTATION.md`: the tracking plan (pre-launch), from `live-ops-analytics`.
- `kpi-log.md`: one dated row of numbers per week.
- `<YYYY-MM-DD>/WEEKLY-REPORT.md`: the one-page weekly report.
- `ROADMAP.md`: from `ROADMAP-TEMPLATE.md` in `live-ops-updates`.
- `changelog.md`: every shipped change and config publish, with the date and the reason.

**The chat overview** is what the user reads. The file is the detail.
- **Weekly:** the report's 5-line summary, the one fix chosen with its hypothesis, the next 3 roadmap drops with dates, and a list of actions waiting for the user's OK.
- **Pre-launch:** the funnel list, the limit budget used (for example "4 of 10 funnels, 9 of 100 event names"), the configs created, and whether events were verified in View Events.
- Say plainly if something blocks updates or launch (for example, the account is not age-checked).

## Studio-specific facts
Which account publishes, whether it has passed the age check, the group that owns each game, the Discord server, the Open Cloud API key location (never the key itself), release weekday and hour, and where game folders live are studio-specific. Read `studio-profile.md` at the project root if it exists. If it doesn't, ask the user for the age-check status and the release slot, use the default paths above, and write down what you assumed. Never write API keys into any file in the repo.
