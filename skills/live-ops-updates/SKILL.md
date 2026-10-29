---
name: live-ops-updates
description: "How to keep a live Roblox game improving and coming back to life: update cadence and patch notes that players read, Experience Events, update announcements and experience notifications (with their caps and dark-pattern bans), the chapter-release playbook for story games, configs and experiments (with the thresholds that make them worth running), bug intake, handling negative feedback, and ROADMAP.md. Use when planning any update, event, chapter, config change, experiment, announcement or community reply. Loaded from the live-ops router."
---

# Live ops: updates, events and community

Load `live-ops` first if you haven't; it holds the approval rule and the policy facts. **Every step below that touches the live game or the public is drafted, shown to the user, and done only after their OK.** Those steps are marked **(OK needed)**.

Labels: **Policy (official)** is from Roblox docs or staff posts; re-check the linked source before relying on it. **[3RD-PARTY]**, **[UNVERIFIED]**, **[CONFLICT]** and **[SYNTHESIS]** mean what they mean in `live-ops-analytics`.

> **Policy (official): updates need an age-checked creator.** Pushing updates or publishing new content requires the publishing account to have passed Roblox's Facial Age Estimation. Confirm this (from `studio-profile.md` or by asking the user) before you put a single date on the roadmap.

## 1. Update cadence

**What Roblox says (Policy, official):**
- Smaller updates every **2 to 4 weeks**, larger feature updates every **2 to 3 months** (Retention docs).
- Cadence ranges from weekly to monthly depending on team capacity (LiveOps Essentials).
- **Cadence updates build only on existing systems:** art-led content such as maps, items, quests, cosmetics. **Major updates add new systems.** Quality-of-life and bug fixes ship as needed.

**What the top charts do [3RD-PARTY]:** Grow a Garden and 99 Nights in the Forest ran weekly updates. 99 Nights hosted a 45-minute "Update Party" session before each update, where the devs played with the community, handed out items and found bugs. (Later reports say 99 Nights moved to every two weeks [UNVERIFIED].) Doors spaced big content drops many months apart and filled the gaps with modifiers, events and quality-of-life updates.

**Default cadence for a small team [SYNTHESIS]:**
- a small content or quality-of-life update every **1 to 2 weeks** (weekly only if it can be kept up without crunch);
- for story games, a **new chapter every 4 to 8 weeks**;
- a major system update every **2 to 3 months**.

**The craft of cadence [3RD-PARTY: LiveOps Essentials pt 2, GDC "Effective LiveOps"; SYNTHESIS]:**
- **Fixed weekday and hour.** Players learn "Saturday, 10am Eastern" and show up. Read the slot from `studio-profile.md`, or ask.
- **Release on day N, keep day N+1 for fixes.** Never release the day before nobody can work.
- **Rate each drop's intensity from 1 to 10 and alternate peaks and troughs** (for example 2, 4, 7, 3, 8, 10, 4). Back-to-back peaks burn out both players and the team.
- **Plan 3 months at most.** Beyond that, the roadmap is guessing.
- **Track how long things really took,** and plan the next quarter from that, not from hope.
- **A missed date is announced, not hidden.** Slip a week with a specific reason rather than ship something broken.

## 2. Patch notes that players read

**Policy (official):** be specific (name new areas, skills, achievements). "Bug fixes" is called out as too vague. Avoid many announcements in a short period.

**Where notes go [SYNTHESIS]:**
1. **In-game update log** in the game's own visual language: a journal page, notice board, radio log, ship's manifest. Shown once per new version, on join. Load `de-ai-ui` for the look and `de-ai-story` for the voice.
2. **Game description:** the top 2 or 3 lines carry the current version and headline content. Keep it accurate; metadata must match gameplay. **(OK needed)**
3. **Update announcement:** 60 characters at most, one every 3 days (Policy, official). **(OK needed)**
4. **Discord #changelog:** the full notes, including known issues. **(OK needed)**
5. **Title tag** such as `[CHAPTER 3]` or `[EVENT]` while it is new, removed when the event ends. Standard on the charts. **(OK needed)**

**Good vs bad (the craft):**

| Bad | Good |
|---|---|
| "Big update!!" | "Chapter 3: The Lower Wards is open" |
| "Bug fixes and improvements" | "Fixed the pump room lift that trapped phone players at the top" |
| "Balanced the monster" | "The Tallyman now pauses for 2 seconds after losing sight of you (it used to turn instantly)" |
| "Added new stuff" | "4 new notes in the archive explain where the evening crew went" |

Rules for a note:
- **Lead with what the player will feel or see,** not the system you changed.
- **Credit reporters** ("thanks to the players who reported the lift bug in #bug-reports"). It turns critics into collaborators.
- **"You said X, we changed Y."** When a fix answers feedback, say so.
- **Every price, odds or drop-rate change gets a line.** Never change them silently.
- **Known issues are listed,** with a plain "we're on it".
- **No hype words, no all-caps, no emoji walls.** Run the copy through `de-ai-story`.
- **No off-platform direction in in-game notes.** Never "see our Discord" in game text (Policy, official).

## 3. Events, announcements and notifications

### Experience Events (Policy, official)
- Creator Dashboard, Engagement, Events & Updates. Up to **10** ongoing or upcoming events.
- Each has a title, subtitle, description, category, **a unique thumbnail**, start and end times, and an optional **custom start place**. Events can stay **private until ready**.
- Players click **Notify Me** to RSVP, get an inbox notification at start, and can opt into push.
- **Trending Events chart:** started within the last 7 days, **1,000+ RSVPs**, public.
- **Off-Platform Featuring** (free): tick "Submit for Featuring" **at least 7 days before start**. The event must be time-limited or a significant update. Best events run **7 to 30 days**. You get a performance report.
- **Attribution:** `player:GetJoinData().GameJoinContext.EventId` tells you a player came from the event. Log it as a custom field.

Creating, publishing or submitting an event is **(OK needed)**.

### Update announcements (Policy, official)
Sent to opted-in followers. **60 characters, at most one every 3 days.** Stats include views, visit rate and **unfollow rate**. A rising unfollow rate means you are announcing too often or too vaguely.

### Experience notifications (Policy, official)
- Personalized, sent through Open Cloud. **13+ only**, and the game needs at least 100 visits.
- **One per user per experience per day.**
- Strings are created in the dashboard: **99 characters**, with `{parameters}`. Launch data up to 200 bytes.
- The opt-in prompt (`PromptOptIn`) uses standard text, appears at most once per 30 days, and is not shown to under-13s.
- **Banned:** disguised ads, **false time pressure**, **bait-and-switch rewards**, tricking users into purchases, and **gating gameplay on opt-in**.

**Writing a good notification (the craft):**
- **Personal and true:** "Your save at {checkpoint} is waiting. Chapter 4 is out." Not "Something big is happening, come back NOW!"
- **One per real reason.** A new chapter, an event starting, a friend's result. Not "we miss you".
- **Point at the exact place:** use launch data to drop the player into the new chapter or event place.
- **A/B by writing a second string,** and compare visit rates. That is the only experiment most small games can afford.
- Creating strings and sending is **(OK needed)**, every time.

### Roblox Moments (Policy, official)
Roblox's in-app short-video feed (30-second clips, 13+, not shown to Kids or Select). Viewers can jump straight into the game. Use the **Captures API** to prompt a capture at the chapter climax or a rare event. `marketing-creative` covers what makes a moment worth capturing.

## 4. Chapter-release playbook (story games)

This is the **canonical timeline**. `marketing-launch` adds marketing beats to it and never changes these dates. No Roblox doc covers chapter live ops directly; this is [SYNTHESIS] from the tooling above and from Piggy, The Mimic and Doors, which prove the episodic model [3RD-PARTY].

**T minus 21 days: content lock**
- The chapter is playable end to end in a private place. `testing` milestone run passed.
- Chapter funnel planned in `INSTRUMENTATION.md` (`live-ops-analytics`); chapter-unlock flag and all tunables are configs, defaulting to locked.

**T minus 14 days: event and teaser**
- Draft a **private** Experience Event "Chapter N: <name>" with a unique thumbnail and a custom start place if the chapter has its own place. **(OK needed)**
- Build the in-game teaser: a locked door, a radio message, a cliffhanger screen with the release date. No off-platform links.
- Hand the trailer brief to `marketing-creative`.

**T minus 7 days or earlier: go public**
- Make the event public and tick **Submit for Featuring** (must be 7+ days ahead). **(OK needed)**
- Push Notify Me through the in-game teaser. Target 1,000+ RSVPs for Trending Events.
- `marketing-launch` starts the teaser clips and announcements.

**T minus 1 to 0: release party (optional)**
- A live session modeled on the 99 Nights Update Party: devs play with the community, catch last bugs, give out a cosmetic.

**Day 0, at the fixed hour** (each item **(OK needed)**, ideally approved as one list the day before):
- publish the update (if the chapter needs code), then flip the chapter-unlock config;
- update announcement, at most 60 characters, for example "Chapter 3: The Lower Wards is open";
- title tag and top description lines;
- 2 or 3 new thumbnails added, old winners kept active (see `marketing-creative`);
- changelog to Discord;
- one experience notification to opted-in players;
- Moments capture prompt live at the chapter climax.

**Day 0, first 4 hours:** watch crash rate, Error Report, DataStore errors and the chapter funnel. Hot-fix through configs. **(OK needed, but prepare the fix and ask fast.)**

**Day 1 to 7:** read the chapter funnel daily. Fix the top absolute drop-off step through configs. The day-7 `WEEKLY-REPORT.md` covers the chapter.

**Between chapters: fill the gap with low-cost content on existing systems [SYNTHESIS]:**
- modifiers or a hard mode;
- time trials with ghost runs;
- alternate endings;
- seasonal reskins of existing spaces;
- lore collectibles;
- one limited event lasting 7 to 30 days.

Alternate intensity. Never stack two high-pressure events back to back.

## 5. Configs and experiments

For the code, load the built-in Roblox skill `rbx-configs-experimentation` with the `skill` tool. This section covers what to put in configs, and when an experiment is worth running.

### Configs (Policy, official)
- Key-value pairs (string, number, boolean, JSON) that change without republishing. Up to **1,000 active configs**; strings and JSON up to 100k characters.
- Conditions: up to 100 per game, 20 per key. **The first matching rule wins, and rule order is global.** Targeting includes country, language, new vs returning, traffic source, time since first play, payer status, platform.
- **Propagation [CONFLICT]:** docs say about 15 seconds to 1 minute after "Publish now" (or a 15-minute gradual rollout); the launch post and the built-in skill say up to 5 minutes. **Plan for 5 minutes.**
- Changes go staged, Studio test, then publish with a message. History allows restore.
- Server only. `GetConfigForPlayerAsync(player)` is needed for experiments. Snapshots don't auto-update: connect `UpdateAvailable` and call `Refresh()`. Wrap the first load in `pcall` with hard-coded fallbacks.

**What belongs in a config [SYNTHESIS]:** difficulty, monster speed and sight range, timers, reward amounts, prices, drop rates, hint timing, event on/off switches, chapter-unlock flags, notification copy keys. If you might tune it after launch, it is a config.

**The craft:**
- **Refresh at safe moments:** between chapters, rounds or respawns. Never mid-chase, mid-cutscene or mid-purchase.
- **Fallbacks are the shipped values,** not zeros. A failed config load must leave a playable game.
- **Every publish message says why:** "Tallyman sight 40 to 32: step 05 churn 31%, see WEEKLY-REPORT 2026-11-07". Mirror it in `changelog.md`.
- **Publishing a config is a live change. (OK needed.)** So is a rollback, though in an emergency you prepare it and ask immediately.

**Open Cloud Configs API (beta):** `/creator-configs-public-api/v1/configs/universes/{id}/repositories/{repo}`, scopes `universe:read` and `universe:write`. **Trap: a key without the write scope may return success without applying the change.** Always read back after a write and confirm the value changed.

### Experiments (Policy, official)
- Run **14 to 60 days**, up to **2 variants plus 1 control**. Up to **10 in-game experiments** and 1 matchmaking experiment at once. One experiment per config key.
- Metrics tracked for every experiment: D1, D7, playtime, ARPU, ARPPU, payer conversion, session time. Updated every 24 hours; results typically appear 24 to 48 hours after start.
- **Significant** means the confidence interval of the % change excludes 0.
- **Early-harm flags:** playtime down 10%, ARPU down 20%, payer conversion down 20%. They apply only with **10,000+ enrolled players** and only in the **first 24 hours**.
- **Sample Ratio Mismatch alert:** stop and restart the experiment.
- **Enrollment happens on the first `GetValue()`** on a player's snapshot. Call it only when the player reaches the feature, or the test is diluted with players who never saw it.
- **Minimum audience [CONFLICT]:** docs say games under **1,000 DAU** "may struggle"; the launch post says under **500 DAU** should grow first. Check the **minimum detectable effect (MDE)** shown at setup: over 100% means pointless.
- Experiments API (beta): `/creator-configs-public-api/v1/experimentation/universes/{id}/experiments` with `:start`, `:schedule`, `/stats`, `:complete`. Stats only after 24 hours, with an `isSrmDetected` flag.

**When to run one [SYNTHESIS]:** only if DAU is at least 1,000 (or 500 per the launch post) **and** the MDE shown at setup is under about 20% (our threshold; the docs only say over 100% is hopeless). Otherwise **use configs with a 7-day before/after comparison** (same weekday mix, no ads, segmented by source) and accept the noise. Most early games are in this second group.

Starting, stopping and completing an experiment are each **(OK needed)**. Never act on non-significant results or on the first 24 hours (except an early-harm stop).

## 6. Community: bug intake and negative feedback

### Discord
> **Policy (official):** Discord and other social links appear only through **Social Links** settings on the game, community or profile, and are shown only to age-checked users 16+. Never write "join our Discord", invite codes or any other off-platform direction in game text, signs, chat or UI. Developers have been warned for this.

**Server structure [3RD-PARTY vendor guides, SYNTHESIS]:**
- `#announcements`, `#changelog`, `#known-issues`, `#bug-reports`, `#suggestions`, `#spoilers` (essential for story games), `#clips`.
- `#bug-reports` as a forum channel or ticket threads with a pinned template: Roblox username, device and platform, chapter or area, steps, expected vs actual, a clip or screenshot.
- `#known-issues` cuts duplicate reports. Keep it current.
- Triage at least **twice a week**: confirm, reproduce, move to `#known-issues`, fix, credit the reporter in the changelog.

Every Discord post or reply is **(OK needed)**; draft them in the repo or in chat.

### In-game bug reports
**Discord blocks webhook calls from live Roblox servers,** and free public proxies are unreliable or dead [3RD-PARTY DevForum]. Don't build on them. **The safer pattern [SYNTHESIS]:** an in-game report button (no off-platform mention) writes a short structured report (player ID, place version, chapter, position, device, a player-written line) to a DataStore or MemoryStore, rate-limited per player. Pull reports with Open Cloud (read only) during triage. Follow the DataStore safety rule in `testing` when testing it.

### Ratings and negative feedback
- **Ratings are lifetime-cumulative** [3RD-PARTY], so a buggy launch drags the ratio for months. Watch the **daily** ratio in the Feedback dashboard, not the lifetime number.
- **Never reward likes, favorites or visits,** and never buy or bot them. Reward-implying metadata is deprioritized (Policy, official) and incentivized engagement is scam-adjacent [SYNTHESIS].
- Creators can report or hide inappropriate comments (Policy, official). List abusive comments for the user; don't act alone.

**The playbook (the craft):**
- **Read for the reason, not the request.** Roblox's LiveOps doc says to focus on the reasoning behind suggestions. "Add a sprint button" often means "the walk to the next objective is boring". The fix might be a shorter path.
- **Answer with changes, not arguments.** "You said the second floor was too dark to navigate; this update adds lamp light at every junction."
- **Fix the top-cited issue in the next update** and say so in the changelog.
- **Never argue in public, never retaliate,** never ban a critic for criticism.
- **Spoilers and story theories are a gift** for a story game. Give them a channel; don't shut them down.
- **Studio conduct is a live-ops risk.** A public dispute can take a game offline [3RD-PARTY: Pressure, 2026]. Keep every public word calm and factual.

## 7. `ROADMAP.md`
Copy `ROADMAP-TEMPLATE.md` (in this folder) to `design/<game>/liveops/ROADMAP.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and keep it current every week.

Rules:
- **3 months at most,** with dates only for the next 3 drops. Later items are "next" and "later", not dates.
- **Every item says why:** a weekly-report finding, a feedback theme, the chapter plan, or the cadence (filler between chapters).
- **Every item is tagged** cadence (existing systems), major (new system) or fix, with an intensity 1 to 10.
- **Every live action on the roadmap lists its approval status.**
- **Done items move to the log** with what happened to the metric they targeted.

## What great looks like
- Players can predict when the next update lands, and it lands then.
- Every patch note names a thing the player will notice.
- Chapter launches stack the event, featuring, announcement, thumbnails, notification and clips into one concentrated window.
- Notifications get opened because they have always meant something.
- Bugs are acknowledged within days, fixed in the next drop, and reporters are credited.
- Tuning happens through configs, with a reason in every publish message.

**Common mistakes:**
- planning a cadence before confirming the creator account can push updates
- weekly updates that collapse into crunch, then a month of silence
- "bug fixes and improvements"
- announcing every 3 days because you can, and watching the unfollow rate climb
- a notification with fake urgency, or one that gates a reward on opting in
- making the chapter event public less than 7 days out, which misses featuring
- reading config values once at server start and never refreshing
- calling `GetValue()` in a lobby script, which enrolls everyone and dilutes the experiment
- running an experiment at 300 DAU and reading noise as a result
- a Discord webhook for bug reports that silently fails in live servers
- arguing with a reviewer in public

## Output
1. **`ROADMAP.md`**, updated, plus `changelog.md` entries for anything shipped.
2. **Drafts** for every update, announcement, event, notification and Discord post, in `design/<game>/liveops/drafts/<YYYY-MM-DD>/`, each with its character count where a cap applies.
3. **A chat overview:** the next 3 drops with dates and intensity, what changed in the roadmap and why, and a numbered list of drafts and live actions waiting for the user's OK. Say plainly if updates are blocked (age check, open Critical bug).

## Tools
- Built-in Roblox skills (load with the `skill` tool): `rbx-configs-experimentation`, `rbx-instrument-analytics`.
- `testing` before anything ships, including config-only changes that alter difficulty or prices.
- `de-ai-story` for every patch note and announcement, `de-ai-ui` for the in-game update log and event thumbnails.
- Open Cloud (beta): Configs API, Experiments API, experience notifications. Every write needs the user's OK; read back after every write.

## Sources
- Retention (cadence): https://create.roblox.com/docs/production/analytics/retention
- LiveOps essentials: https://create.roblox.com/docs/production/game-design/liveops-essentials
- Experience events: https://create.roblox.com/docs/production/promotion/experience-events
- Experience notifications: https://create.roblox.com/docs/production/promotion/experience-notifications
- Configs: https://create.roblox.com/docs/production/configs
- Experiments: https://create.roblox.com/docs/production/experiments
- Configs and Experiments launch: https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385
- Configs API (beta): https://create.roblox.com/docs/cloud/guides/configs
- Experiments API (beta): https://create.roblox.com/docs/cloud/guides/experiments
- Kids/Select launch and age check for updates: https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717
- Off-platform warning thread: https://devforum.roblox.com/t/warned-for-directing-users-off-platform-i-have-2-questions/3909424
- 99 Nights creator spotlight: https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940
- Moments: https://about.roblox.com/newsroom/2025/09/roblox-moments-user-generated-discovery
- Cadence principles [3RD-PARTY]: https://www.gamedeveloper.com/business/liveops-essentials-part-2-the-cadence
- Discord webhook threads [3RD-PARTY]: https://devforum.roblox.com/t/discord-webhook-not-working-http-403-error/1494977
