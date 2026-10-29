---
name: live-ops-analytics
description: "How to track and read a live Roblox game: the instrumentation plan (onboarding funnel, one funnel per chapter, custom and economy events) budgeted against AnalyticsService limits, how Home recommendation signals work, benchmarks and what good looks like, how to turn funnel drop-off into one confirmed fix, and the weekly KPI pull that produces WEEKLY-REPORT.md with a 5-line summary first. Use before launch to plan tracking, and every week after launch. Loaded from the live-ops router."
---

# Live ops: analytics

Load `live-ops` first if you haven't; it holds the approval rule and the policy facts. This skill covers **what to track, why, and how to read it**. For the Luau that logs events, load the built-in Roblox skill `rbx-instrument-analytics` with the `skill` tool. It has an audit mode (read-only plan) and an instrument mode (it builds a `ServerScriptService.Analytics` module and edits scripts). Don't rewrite its code here.

Labels used below: **Policy (official)** is from Roblox docs or staff posts. **[3RD-PARTY]** is credible but not from Roblox. **[UNVERIFIED]** is a blog or forum claim; never treat it as a target. **[CONFLICT]** means sources disagree; both values are given. **[SYNTHESIS]** is a recommendation built from the facts, not a platform rule.

## 1. How Home recommendations score a game
Home "Recommended for You" is the main source of free players. Its ranking signals, in Roblox's own order of importance (Policy, official):

**Most important**
- **Play-through rate:** plays divided by impressions in that sort.
- **First-play bounce:** a negative signal, measured at under 60 s and at 61 to 180 s.
- **Play days per user:** day 1, days 2 to 7, days 8 to 28.
- **Playtime per user**, capped at **60 minutes per user, per game, per day**.

**Important**
- intentional co-play days per user, qualified play sessions per user, spend days per user, Robux spent per user.

**Rules that follow (Policy, official)**
- Signals are **averages per user**, not totals. A small game with loyal players can outrank a big leaky one.
- **Players who arrive from ads, search, friends, social links or curation don't count in the ranking stage.** Those sources only help the game get considered. You can't buy your way into Home ranking.
- A **custom thumbnail is required** to get Home impressions.
- Metadata implying monetary reward ("free Robux", giveaway titles) is not prioritized.
- Play-through rate dips when impressions rise. That is expected, not a failure.

**What this means for design and reading the data [SYNTHESIS]**
- **The first 3 minutes are scored.** The two bounce windows (0 to 60 s and 61 to 180 s) are a direct ranking signal. Roblox's Retention docs say to get new players to the fun "ideally in 5 minutes or less". Onboarding is the highest-leverage thing you will ever fix.
- **Return days beat marathons.** Because playtime is capped at 60 minutes a day, a 3-hour binge earns no more than one hour. A reason to come back tomorrow (a chapter cliffhanger, a daily goal, a timed event) is worth more than a longer session.
- **Solo games can rank.** Co-play is only an "important" signal. Play days and playtime are top tier.

## 2. The instrumentation plan (pre-launch)

### The limits you are budgeting against (Policy, official)

| Limit | Value |
|---|---|
| Global rate | **120 + 20 x CCU** requests per minute. Extra events are **dropped silently** |
| Funnels | **10** |
| Steps per funnel | **100** |
| Custom event names | **100** |
| Custom fields per event | **3** (CustomField01 to 03) |
| Unique combined field values | **8,000**, then values group as "Other" |
| Currencies | **[CONFLICT]**: class reference says **5**, the event-types doc says **10**. Design for 5 or fewer |
| `transactionType` / `itemSku` | Unlimited, but only 20 / 100 are shown before "Other" |
| Funnel user expiry | 180 days inactive, then the user counts as new |
| Data retention | 90 days after the last event |

**Behavior (Policy, official):** calls work **only from the server, in a published place**. Studio and client calls are no-ops, so you cannot verify events in a Studio playtest. Charts appear about **24 hours** after the first event. Verify with **View Events** on the Funnel, Economy or Custom page (near real time); errors appear in the Error Report.

### Which method for what

| Method | Use it for |
|---|---|
| `LogOnboardingFunnelStepEvent` | The one-time first-session funnel, steps 1 to 100. Logged once per player, ever |
| `LogFunnelStepEvent` with a `funnelSessionId` | Recurring runs: a chapter attempt, a shop visit, a round. Make a new `HttpService:GenerateGUID()` per run. Repeated steps in one session are ignored, and **skipped steps count as completed** |
| `LogEconomyEvent` | Sources and sinks of in-game currency. `amount` positive, `endingBalance` is the balance after. Log only after the transaction succeeded |
| `LogCustomEvent` | Anything the dashboards don't track: deaths by location, hints used, ending reached |
| `LogProgression*Event` | **Avoid.** Not shown in Roblox-provided charts. Use funnels for chapter beats |

### Writing good funnel steps (the craft)
- **A step is a moment the player chose or achieved,** not a moment the code ran. "Picked up the lantern" is a step. "Lantern script loaded" is not.
- **Steps must be strictly ordered on the main path.** Because skipped steps count as completed, an optional side room in the middle of a funnel makes the step after it look better than it is. Optional content goes in custom events, not funnel steps.
- **Put a step on both sides of every risk.** Before and after the first chase, the first puzzle, the first purchase prompt, the first loading screen. Churn between two adjacent steps is only useful if those steps bracket exactly one thing.
- **8 to 12 onboarding steps, with the first 3 inside the first 60 seconds.** That is the bounce window Home scores.
- **Name steps so a stranger can read the chart:** `03_first_objective_shown`, not `step3`. Number them so they sort.
- **Never re-log what Roblox already measures:** DAU, session length, retention, purchases of passes and products. `rbx-instrument-analytics` lists these.

### Story and chapter games: the default plan [SYNTHESIS, within the 10-funnel cap]
- **Funnel 1, onboarding (8 to 12 steps):** join, first input, first objective shown, first objective done, first story beat (cutscene ends), first danger or encounter, first save or checkpoint, chapter 1 midpoint, chapter 1 end.
- **Funnels 2 to 9, one per chapter**, with a new `funnelSessionId` per attempt: start, each set piece, puzzle or chase, boss, ending, next-chapter teaser seen. That covers 8 chapters. If the game will have more, group later chapters (one funnel per "book" of chapters, with a chapter number in a custom field on the custom events).
- **Funnel 10, shop** (only if monetized): open, view item, prompt shown, purchase succeeded.
- **Custom events:**
  - `ChapterDeath` (field: encounter or location ID);
  - `HintUsed` (field: puzzle ID);
  - `ChapterDurationSec` (value: seconds);
  - `EndingReached` (field: ending ID);
  - `SoloOrParty` as a custom field on chapter start.
- **Economy events** only if the game has a currency, with 5 currency names at most.

For non-story games, keep the same shape: an onboarding funnel, one funnel per core loop (a round, a run, a build cycle), a shop funnel, and custom events for failures and choices.

### Budget the field values
8,000 unique combined field values sounds large, but `location x encounter x device` grows fast. Use short, fixed IDs (`ch2_pump_room`), never free text, player names or timestamps. Never put personal data in any field.

### `INSTRUMENTATION.md`
Write the plan to `design/<game>/liveops/INSTRUMENTATION.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) before any code is written:
1. A table of every funnel: number, name, every step in order, and which script and event fires it.
2. Every custom event: name, value meaning, the three fields and their allowed values.
3. Every currency and economy event.
4. The budget line: funnels used of 10, event names of 100, currencies of 5, worst-case field combinations of 8,000, and the expected peak event rate against 120 + 20 x CCU.
5. The verification log (filled in after the private publish).

Then load `rbx-instrument-analytics` in instrument mode to build it, and run `testing` on the result.

### Verify before launch
1. Ask the user for OK to publish privately (or to testers). This is a publish and needs approval.
2. Play every funnel path once in the published place.
3. Confirm each event appears in **View Events**, and that the Error Report is clean.
4. Wait about 24 hours and confirm the charts populated.
5. Record what you saw in the verification log. A funnel that was never seen in View Events is NOT VERIFIED; say so in chat.

## 3. Benchmarks: what good looks like

**There is no official genre retention table.** Roblox's dashboard compares you to "similar experiences" through the **Benchmark scorecard**, which needs **100+ DAU**. Above 100 DAU, your scorecard percentile is the best benchmark you have.

Third-party reference (GameAnalytics, Aug 2025 to Jul 2026, 500+ games) [3RD-PARTY]:

| Metric | Median | Top 1% |
|---|---|---|
| D1 | 10.3% | 22.2% |
| D7 | 1.6% | 9.1% |
| D30 | 0.5% | 4.7% |

Other GameAnalytics medians [3RD-PARTY]: session 9.8 min (top 5%: 16.6), 1.56 sessions per day, 22.4 min playtime per player per day, payer share 3.8%.

**Do not use** the widely repeated "20% D1 is good, 40% is excellent". GameAnalytics calls it inflated by survivor samples. Genre ranges from blogs are [UNVERIFIED] opinion.

**Working targets [SYNTHESIS, not platform facts]:**

| Metric | Floor (keep iterating) | Good (start promoting) | Hit territory |
|---|---|---|---|
| D1 | 10% or more | 15% or more | 22% or more |
| D7 | 2% or more | 4% or more | 9% or more |
| D30 | 0.5% or more | 1.5% or more | 4.7% or more |
| Avg session | 10 min or more | 15 min or more | 20 min or more |

**Story-game caveat [SYNTHESIS]:** a chapter game with finite content shows a natural D7 and D30 cliff once players finish. Read D7 against **chapter-completion rate**, and use the dashboard's similar-experiences benchmark, which compares you to other story and horror games. A 4% D7 with 60% chapter completion is a healthy game waiting for its next chapter; a 4% D7 with 15% completion is a leak.

## 4. Turning drop-off into a fix (the craft)

### Which metric points at which system (Policy, official, Retention docs)

| Weak metric | Look at |
|---|---|
| First-play bounce and D1 | Core loop, first-time experience, performance |
| D7 | Progression, chapter pacing |
| D30 | The "ending system": endgame, replay, social features |

### The method [SYNTHESIS]
1. **Find the biggest absolute loss.** Lay out each funnel's steps with users reaching each. Compute players lost between adjacent steps. The step that loses the most players is fix number one, even if a later step has a worse percentage. Example: step 2 to 3 loses 400 of 1,000 (40%); step 7 to 8 loses 60 of 150 (40%). Same rate, but step 2 to 3 costs 6x more players. Onboarding is "likely where you lose the majority of your users" (Roblox funnel docs).
2. **Confirm with a second signal before changing anything.** Pick at least one:
   - new-user first-session retention (5 and 10 minute buckets);
   - `RFYDuration0To60` bounce;
   - the device split (phone vs PC);
   - Feedback dashboard comments that mention that area;
   - Error Report and crash logs for that area;
   - watching a real, unaware player (or a blind first-time-player agent from `testing-first-time-player`).
   **High churn plus errors is a bug. High churn with no errors is a design problem:** unclear goal, too hard, or boring. Phone-only churn is usually UI or controls.
3. **Write a hypothesis:** "Change X, expect metric Y up by Z, because W." Example: "Move the flashlight pickup into the first room. Expect step 02 to 03 churn down from 38% to under 25%, because 6 of 9 Feedback comments say 'too dark, can't find the way'."
4. **Change one thing, through a config if possible.** Tag the change in the config publish message and `changelog.md`. Don't touch the same area with anything else in that window.
5. **Compare 7 full days before and after,** with the same weekday mix, excluding days with ads, influencer spikes or a big event.
6. **Segment by acquisition source before panicking.** Since Oct 2025 the Retention page breaks down by source. A D1 drop is often just a traffic-mix change: ad and external-link players retain worse than Home players.

### Never act on
- one day of data;
- a cohort that hasn't finished (a D7 value appears 7 days after the cohort started; D30 after 30);
- the first 24 hours of an experiment (except an early-harm stop);
- a non-significant experiment result;
- the lifetime like ratio (watch the **daily** ratio in the Feedback dashboard instead);
- a dip right after a big influx of new players or impressions, which Roblox says is normal.

## 5. The weekly KPI pull

### Where the numbers come from
**Option A, the dashboard** (Creator Hub, read only, no approval needed): Overview, Retention, Engagement, Acquisition (including the Home Recommendations signal dashboard), Funnel, Feedback, Thumbnails, Performance.

**Option B, the Analytics Query API** (Open Cloud, **beta**, read only):
- `POST https://apis.roblox.com/analytics-query-api/v1/universes/{universeId}/metrics` (plus `/dimension-values`). Slow queries return an operation; poll it until `done`.
- Scope `universe.analytics:read`, sent in the `x-api-key` header. The key's location comes from `studio-profile.md`; never write the key into the repo or into chat.
- Granularity `OneDay` works for every metric. History goes back up to 4 years; performance metrics only 28 days.
- A `429` with code `3000` means you exceeded the data-point budget. Narrow the range or the breakdowns.
- To find funnel step IDs, query `FunnelUserTotalCount` with a `FunnelStep` breakdown and a `FunnelName` filter over 90 days.
- Check the metrics reference before each new query; beta schemas change.

**Dashboard only (not confirmed in the API):** Feedback comments, the View Events stream, Benchmark percentiles, Ads Manager reports, per-product sales tables, and retention by acquisition source (untested; try it and record whether it works).

### The weekly metric set

| Group | Metrics (API names) |
|---|---|
| Retention | `ForwardD1Retention`, `ForwardD7Retention`, `ForwardD30Retention` |
| Engagement | `DailyActiveUsers`, `AverageSessionLengthMinutes`, `AveragePlayTimeMinutesPerDAU`, `TotalSessionsEndedInBucket` (first-session retention) |
| Home signals | `RFYPlayThroughRate`, `RFYDuration0To60`, `RFYDuration61To180`, `RFYD2To7PlayDays`, `RFYD8To28PlayDays` |
| Funnels | `FunnelUserChurnRate` and `FunnelStepCompletionRate` by `FunnelStep`, for onboarding and the newest chapter |
| Store page | `ThumbnailQualifiedPTR`, `ThumbnailImpressions`, `ThumbnailWinningSegments` |
| Health | client crash rate, FPS percentiles, memory, `TotalAbuseReports` |
| Money (if monetized) | `DailyRevenue`, `PayingUsersCVR`, `AverageRevenuePerPayingUser` |
| Feedback | daily positive and negative ratings, and every comment, tagged by theme (dashboard) |

Append one dated row to `design/<game>/liveops/kpi-log.md` each week, with the same columns every time, so trends are a glance.

### Tagging feedback comments
Tag each comment with one theme: **bug, difficulty, confusion, performance, content length, monetization, praise**. Count the themes. The top negative theme is a candidate second signal for step 2 of the method. Abusive comments can be reported or hidden; that is a dashboard action, so list them for the user rather than acting.

## 6. `WEEKLY-REPORT.md`
One page. Write it to `design/<game>/liveops/<YYYY-MM-DD>/WEEKLY-REPORT.md` with this shape:

```markdown
# <Game>: weekly report, <start date> to <end date>

## Summary (5 lines)
1. Players: <DAU avg> DAU (<+/-x%> vs last week), <new users> new.
2. Came back: D1 <x%> (target <y%>), D7 <x%> (cohort of <date>, complete / not yet complete).
3. Biggest leak: <funnel> step <a> to <b> lost <n> players (<x%>); second signal: <what>.
4. Fix chosen: <one change>, via <config / next update>; expect <metric> to move <how much>.
5. Blockers or decisions for the user: <age check, approval needed, nothing>.

## Who returned
Table: D1, D7, D30 (mark incomplete cohorts), session length, playtime per DAU, sessions per day, vs last week and vs target. Benchmark percentile if 100+ DAU, otherwise "under 100 DAU: compared to GameAnalytics medians [3RD-PARTY]". Story games: chapter completion rate next to D7.

## Where players quit
The onboarding funnel and the newest chapter funnel: each step, users, players lost, churn %. Bold the biggest absolute loss. Home signals: play-through rate, 0 to 60 s and 61 to 180 s bounce. Device split if it differs.

## What players said
Feedback dashboard: daily rating ratio trend, comment themes with counts, two or three short representative quotes. Discord bug triage counts (new, confirmed, fixed).

## What to fix or add next
1. The one fix: hypothesis "Change X, expect Y by Z, because W", how it ships, how it will be measured, when it will be read.
2. Last week's fix: what happened (before and after numbers, same weekday mix) and the verdict (kept, reverted, inconclusive).
3. Roadmap changes this week, if any (link to ROADMAP.md).

## Needs the user's OK
Every live action proposed: config publishes, experiment starts, events, announcements, notifications, posts. One line each.

## Data notes
Anything that makes this week's numbers unreliable: ads running, a creator video, a holiday, an outage, an incomplete cohort, a metric that failed to load.
```

## What great looks like
- **The 5-line summary stands alone.** A user who reads only those lines knows whether the game is getting better and what happens next.
- **Every number has a comparison:** last week, the target, or the benchmark. A bare "D1 12%" says nothing.
- **One fix, with a falsifiable hypothesis,** and last week's fix graded honestly, including "inconclusive".
- **Incomplete data is labelled,** not quietly compared.
- **Absolute losses, not just percentages,** drive the choice.

**Common mistakes:**
- logging events from the client (they're dropped) or before a transaction succeeds
- a funnel with optional steps in the middle, which inflates the next step because skipped steps count as completed
- free-text custom field values that blow the 8,000 combination limit
- re-logging DAU or purchases
- verifying analytics in Studio, where every call is a no-op
- choosing the fix by worst percentage instead of most players lost
- calling a D1 drop a design problem when the traffic mix changed
- a report that lists 12 problems and picks none

## Output
1. **Pre-launch:** `INSTRUMENTATION.md`, verified events, and a chat overview: the funnel list, the limit budget used, and anything NOT VERIFIED.
2. **Weekly:** `WEEKLY-REPORT.md`, a new row in `kpi-log.md`, and a chat overview: the 5-line summary, the fix chosen with its hypothesis, last week's verdict, and the list of actions waiting for the user's OK. Then hand the fix to `live-ops-updates` for the roadmap.

## Tools
- Built-in Roblox skills (load with the `skill` tool): `rbx-instrument-analytics` (event code, audit and instrument modes), `rbx-configs-experimentation` (config code, for shipping fixes).
- `script_grep` or `grep_scripts`: find existing `AnalyticsService` calls before planning, so nothing is logged twice.
- `testing-first-time-player`: blind agents whose stuck points are a second signal.
- Open Cloud Analytics Query API (beta) for the weekly pull, read only.

## Sources
- Discovery: https://create.roblox.com/docs/discovery
- Analytics overview: https://create.roblox.com/docs/production/analytics
- Retention: https://create.roblox.com/docs/production/analytics/retention
- Benchmarks: https://create.roblox.com/docs/production/analytics/developer-statistics
- Event types: https://create.roblox.com/docs/production/analytics/event-types
- Funnel events: https://create.roblox.com/docs/production/analytics/funnel-events
- AnalyticsService: https://create.roblox.com/docs/reference/engine/classes/AnalyticsService
- Analytics Query API (beta): https://create.roblox.com/docs/cloud/guides/analytics and https://create.roblox.com/docs/en-us/cloud/guides/analytics/metrics
- Retention by source (Oct 2025): https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157
- Feedback dashboard: https://devforum.roblox.com/t/new-feedback-dashboard-see-detailed-feedback-from-your-community/3588091
- Analytics essentials: https://create.roblox.com/docs/production/game-design/analytics-essentials
- GameAnalytics benchmarks [3RD-PARTY]: https://www.gameanalytics.com/reports/2025-roblox-report
