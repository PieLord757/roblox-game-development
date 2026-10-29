# <Game name>: launch kit, <launch or "Chapter N: name">

Copy this file to `design/<game>/marketing/<launch-or-chapter>/LAUNCH-KIT.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and fill it in. Delete these instruction lines and any section that does not apply. Every item that posts, sends, uploads, registers or spends is a draft until the user approves it.

Status: draft / sent to user <date> / approved <date> (list of what was approved)
Release: <YYYY-MM-DD, hour, time zone> (dates from ROADMAP.md; chapter timeline from `live-ops-updates` section 4)

## 0. Gate check
- D1: <x%> vs gate <50th percentile on Benchmark scorecard / 10.3% GameAnalytics median under 100 DAU> = met / not met
- Onboarding funnel: worst step <a to b>, <n> players lost (<x%>)
- **Spend allowed:** yes / no (if no: organic and free-access only)

## 1. Store page check
- [ ] Icon 512 x 512+, readable at 150 x 150 (checked among real Home icons)
- [ ] 2 to 5 thumbnails, 16:9, 1920 x 1080, nothing in the bottom strip, real game art, each testing a different idea
- [ ] Video thumbnail: real gameplay, no voice-over, no lyrics, no claims (uploads used this month: <n> of 3)
- [ ] Title and description match gameplay, no reward bait, state solo play and length
- [ ] Maturity label: <label>
- [ ] Social Links set (16+ only); nothing in game text points off-platform
- [ ] `de-ai-ui` and `de-ai-story` run over every asset and line

## 2. Trailer shot list

**Cut A, on-platform video thumbnail:** <15 to 30> s, real gameplay, no voice-over, no lyrics, logo at end.
**Cut B, off-platform trailer:** <45 to 75> s, voice-over and licensed music allowed. Vertical cutdowns: <list>.

| # | Cut (A / B / both) | Duration | On screen | Camera | How to capture (place, dev hook, config) | Sound | On-screen text |
|---|---|---|---|---|---|---|---|
| 1 | both | 0 to 2 s | <the hook: monster, set piece> | | | | |
| 2 | | | | | | | |
| ... | | | | | | | |
| End | both | 1.5 s+ | Logo, "Free on Roblox" (B: plus date) | | | | |

Hook line (B): "<one line>"
Audio rights: <owned / licensed from Roblox library / list>

## 3. Five clip ideas with scripts
Each: vertical 9:16, 9 to 20 s, captions on, real gameplay, ends on game name and "Free on Roblox". Five different types (scare, chase, twist, monster reveal, failure compilation, atmosphere).

### Clip 1: <working title>
- **Type:** <scare / near-miss chase / twist / monster reveal / failure compilation / atmosphere>
- **Length and aspect:** <n> s, 9:16 (plus 16:9 version for <X / Reddit>: yes / no)
- **Hook (0 to 1 s):** <exact first frame>
- **Setup (1 to 4 s):** on-screen text "<line>"
- **Payoff (4 to <n> s):** <what happens, cuts>
- **Button:** <reaction, freeze, line>
- **End card:** <game name>, "Free on Roblox"
- **Caption:** "<post caption>" **First comment:** "<question>"
- **Capture plan:** <place, setup, dev hook>
- **Platforms and date:** <TikTok, Shorts, Reels, X, Reddit>, <date>
- **Share Link:** <per-channel link name>

### Clip 2: <working title>
<same fields>

### Clip 3: <working title>
<same fields>

### Clip 4: <working title>
<same fields>

### Clip 5: <working title>
<same fields>

## 4. Announcement drafts
- **Update announcement (60 characters max, one per 3 days):** "<text>" (<n> characters)
- **Experience Event:** title "<>", subtitle "<>", description "<>", thumbnail <file>, start <>, end <>, custom start place <yes / no>, Submit for Featuring <date, at least 7 days ahead>
- **Roblox Community (group) announcement:**
  > <first line is the news> ...
- **Discord #announcements:**
  > <first line is the news> ...
- **Discord #changelog:** link to the full notes from `live-ops-updates`
- **Experience notification (99 characters max, one per user per day, 13+):** "<text with {parameters}>" (<n> characters); variant B: "<>"
- **Reddit (only after reading the subreddit's rules):** subreddit <>, rules read <date>, format <showcase / feedback thread>, draft:
  > <post>

## 5. Creator outreach
- Shortlist: <n> creators (<n> nano and micro, <n> mid, <n> large), audiences checked for age and genre. List in `marketing-log.md`.
- Offer: free early access / private server, embargo <date>, Share Link per creator
- Pitch draft (one paragraph, personalized per creator):
  > <draft>
- Paid deals (only if the gate is met): <none / creator, deliverable, price [UNVERIFIED norm: <range>], in-video disclosure and paid-promotion box in written brief: yes>

## 6. Ad plan with suggested budget
- **Gate met:** yes / no (if no: "No paid ads yet. Reason: <>.")
- **Objective:** Plays / Earnings
- **Audience:** New / Lapsed (30 to 180 days); age 18 to 24, 25+ (plus 13 to 17 if Moderate); device <>; location <>
- **Creatives:** <3 to 5 thumbnails, the idea each tests>
- **Test length:** <3 to 5> days, starting <date>, not overlapping any experiment or measurement window
- **Suggested budget:** <n> Robux a day x <n> days = <total> Robux (about <n> ad credits at the rate shown in the Ads Manager preview). **Derived from unverified third-party ranges; no official rate card exists.** User ceiling: <from studio-profile.md or the user>
- **Measure:** cost per play, playtime, D1 of the New Users view vs organic D1, earnings and Creator Rewards from the cohort
- **Stop rule:** <e.g. stop if CPP above <n> Robux and ad-cohort D1 under half of organic after 3 days>
- **Scale rule:** <e.g. double for 5 more days if payback within <n> days is plausible>

## 7. Cross-promotion
<none / neutral non-call-to-action reference in <place> / registered ad integration, registered <date, at least 5 days ahead>>

## 8. Launch-day timeline

| When | Beat | Owner | Approved |
|---|---|---|---|
| T-14 | | | |
| T-7 | | | |
| T-2 | | | |
| T 0, <hour> | | | |
| T 0 to +4 h | Watch crash rate, errors, onboarding funnel | build thread | n/a |
| T+3 | KPI review, ads and creator decision | | |
| T+7 | WEEKLY-REPORT.md, marketing log review | | |

## 9. Waiting for the user's OK
Numbered, one line each, exact wording or file attached:
1. <e.g. Post clip 1 to TikTok and Shorts on <date>>
2. <e.g. Make Experience Event public and Submit for Featuring>
3. <e.g. Create ad campaign: Plays, 18+, 4,000 Robux a day x 4 days>
