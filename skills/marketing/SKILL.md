---
name: marketing
description: "Start here for marketing a Roblox game: launch, chapter releases, events and ongoing growth. Explains the approval rule (nothing is posted, sent or paid for without the user's OK), the metric gate before any spend, the platform and legal rules (ads hidden from under-13s and labelled, in-game ad integrations registered 5+ days ahead, sponsored content disclosed, social links 16+ only), the launch kit it produces (trailer shot list, 5 clip ideas with scripts, announcement drafts, ad plan with a suggested budget), and which sub-skill to load: marketing-creative or marketing-launch. Use before making any trailer, clip, thumbnail, post, creator pitch or ad."
---

# Marketing (start here)

## Why this exists
Roblox games don't get found by being good. They get found when something pushes them past the point where Home recommendations take over. In the documented hits that push came from outside [3RD-PARTY]:
- **Dead Rails:** Roblox's own TikTok posted a clip, the game hit the front page, then big YouTubers piled on.
- **Grow a Garden:** partnered with a creator who had about 12M TikTok followers when it was at roughly 500 CCU; reveal moments were made for short video.
- **Doors:** spread through creator reaction videos, memes and theories about its monsters.
- **99 Nights in the Forest:** a familiar format, one iconic monster, and weekly updates once it caught.

None of them grew on ads alone. And marketing can't save a leaky game: **players who arrive from ads, social links or creators don't count in Home ranking** (Policy, official). They only get the game considered. If they leave in the first 3 minutes, the money is gone and Home learned nothing good.

**The standard:** every game launches with a **launch kit** (`LAUNCH-KIT.md`) built from real gameplay, in the game's own look and voice. Spend waits until the game proves it keeps players. Every post, message and dollar is approved by the user first.

## The approval rule (read this first)

> **Nothing is posted, sent, published or paid for without the user's explicit OK, given in chat for that specific action.** Draft it, show it, ask, then act. An earlier OK does not cover a later action.
>
> This covers, at minimum:
> - **posting** anywhere: TikTok, YouTube, Shorts, Reels, X, Reddit, Discord, the Roblox Community (group), Roblox Moments;
> - **sending** anything: emails or DMs to creators, update announcements, experience notifications, replies to comments;
> - **spending**: Ads Manager campaigns, ad credits, creator fees, boosts, any purchase, including "just $5 to test";
> - **creating** an ad campaign or registering an ad integration, even if it doesn't spend yet;
> - **uploading** or changing the icon, thumbnails, video thumbnail, title or description;
> - **creating or publishing** an Experience Event, ticking Submit for Featuring, nominating for Standout Games;
> - **agreeing** to anything with a creator or partner (price, deliverables, exclusivity).
>
> Writing drafts, shot lists, scripts, budgets and plans in the repo needs no approval.

When the user approves a batch ("post clips 1 to 3 on Tuesday"), confirm the exact list before acting, and do only that list.

## Gate before any spend
> **Do not buy ads or pay creators until the game keeps players** [SYNTHESIS from official facts]:
> - D1 is at or above the **50th percentile** on the game's own Benchmark scorecard (needs 100+ DAU), or, under 100 DAU, at or above the GameAnalytics median of **10.3%** [3RD-PARTY];
> - new-user first-session retention is healthy, and the onboarding funnel has no step losing a large share of players (see `live-ops-analytics`).
>
> Below the gate, marketing is free only: organic clips, free early access for creators, featuring submissions. Fix onboarding first.

## Platform and legal rules
**Policy (official, checked 2026-10):** from Roblox docs, Roblox Help, or staff posts, plus the FTC for disclosure. Re-check the linked source in the sub-skill before relying on one of these for a decision.

- **Ads are hidden from under-13 users.** Any in-game ad must be gated with `PolicyService` (`AreAdsAllowed`). Never target ads or creators whose audience is mainly under 13.
- **Ads are labelled in plain language** ("ad", "paid", "sponsored").
- **In-game ad integrations must be registered in Ads Manager at least 5 days before they start**, labelled (Roblox renders the label), and moderated (about 48 hours). Anything published for pay, or containing a call to action or off-platform promotion, counts. **This applies even to promoting your own content inside your own game.** Revenue share applies to campaigns starting on or after Jan 1, 2027.
- **Sponsored creator content must be disclosed in the video itself** ("ad", "#ad", "paid"), not only in the description. **Free early access or items with real value count as payment.** The advertiser (us) is liable when a creator doesn't disclose. YouTube's "contains paid promotion" box must be ticked.
- **Social and Discord links are shown only to age-checked users 16+,** and only through Social Links settings. Game text, signs and chat must never direct players off-platform.
- **Restricted maturity means age-verified 18+** only, and blocks some countries. A Moderate game keeps the 16+ pool (and 9 to 15 if it passes review).
- **Thumbnails and video thumbnails must show real gameplay.** No enhanced graphics, no unreleased features, no subjective claims.
- **No reward bait.** "Free Robux", giveaway and reward-implying metadata is not prioritized and is a scam pattern. Never buy, bot or reward likes, favorites, visits or followers. No clone metadata.

**Prices are unverified.** Roblox publishes no ad rate card. Every ad cost, budget floor and creator price in these skills is [UNVERIFIED] and is a starting hypothesis only. **Measure your own cost per play** and decide from that.

## The launch kit
Every launch (and every chapter release) gets a `LAUNCH-KIT.md`, from `LAUNCH-KIT-TEMPLATE.md` in `marketing-launch`. It contains:
1. **A trailer shot list,** in two cuts: the on-platform video thumbnail (15 to 30 s, real gameplay, no voice-over, no lyrics) and the off-platform trailer, plus vertical cutdowns.
2. **5 clip ideas, each with a script:** hook in the first second, beats, end card, captions, length and aspect ratio.
3. **Announcement drafts:** the Roblox Community (group) post, the Discord post, the 60-character update announcement, and the event text.
4. **An ad plan with a suggested budget:** a 3 to 5 day test campaign, its targeting, its creatives, the budget derived from the unverified ranges, and the cost-per-play rule for whether to continue.
5. **Store-page check, creator shortlist, launch-day timeline, and the approvals list.**

## Which sub-skill to load

| You need | Load |
|---|---|
| What makes a clip spread, the trailer craft and shot list, clip scripts, thumbnails and icon from a marketing angle, asset specs, thumbnail testing | `marketing-creative` |
| The launch-day plan, creator outreach and deal norms with disclosure, Ads Manager and the ad plan, cross-promotion, group and Discord announcements, what works for 16+, the hard rules, `LAUNCH-KIT-TEMPLATE.md` | `marketing-launch` |
| The chapter-release timeline (canonical dates), events, announcements, notifications | `live-ops-updates` |
| Whether the game is ready for spend (D1, funnels) | `live-ops-analytics` |
| The store page itself (title, hook, description, icon and thumbnail specs, publishing order, maturity and compliance) | `publish` and its sub-skills (`publish-store-page`, `publish-compliance`, `publish-launch`) |
| The look of every image and the voice of every line | `de-ai-ui`, `de-ai-story` |

## Who does what
- **The build thread** drafts the kit, captures footage and stills from real playtests, writes scripts and posts, and builds the ad plan.
- **The user** approves every post, message, upload and spend, and owns every account.
- **A fresh reviewer agent** checks the kit cold before it goes to the user: does each clip hook in the first second, does every asset show real gameplay, does anything read as AI-made, is every sponsored item disclosed.

## What great marketing looks like
- **Built from the game's best real moments.** A named monster, a near-miss chase, a twist. If the game has no clip-able moment, that is a design note for the build, not a marketing problem.
- **Looks like this game and nothing else.** For an older audience, art direction that doesn't look like default Roblox is the hook. Anything that looks generic or AI-made kills it.
- **Concentrated.** Event, featuring, announcement, new thumbnails, clips and creator videos land in the same 24 hours, so the spike is big enough to matter.
- **Measured.** A share link per channel and per creator, a log of every post and deal, and decisions made from cost per play and the D1 of each cohort.
- **Honest.** Real footage, disclosed sponsorships, no bait.

**Common mistakes:**
- spending before D1 clears the gate
- a trailer that opens on a logo or a slow pan
- fake or enhanced thumbnails (against the rules and a broken promise to the player)
- treating blog ad prices as targets
- paying a creator whose audience is mostly under 13 for a 16+ game
- a creator deal with no in-video disclosure
- "join our Discord" in game text
- self-promo portals to sibling games without registering them as ad integrations
- posting clips that are all intro and no hook
- spreading the launch over two weeks, so nothing spikes

## Output
1. **`design/<game>/marketing/<launch-or-chapter>/LAUNCH-KIT.md`** (or the place named in `studio-profile.md`), with drafts and assets in the same folder.
2. **`design/<game>/marketing/marketing-log.md`**: every post, clip, creator contact and campaign, with date, share link, views, joins and cost.
3. **A chat overview:** a table of the trailer cuts and the 5 clips (hook line, length, platform), the suggested ad budget with its test length and the stop rule, the creator shortlist count, the launch-day timeline in one line per beat, and a numbered list of every action waiting for the user's OK. Say plainly if the spend gate is not met.

## Studio-specific facts
The accounts and channels the studio owns, the group that owns each game, the Discord server, ad credit balance, budget limits the user has set, existing creator relationships, and the release slot are studio-specific. Read `studio-profile.md` at the project root if it exists. If it doesn't, ask the user for the budget ceiling and which channels exist, and write down what you assumed. Never store passwords, payment details or API keys in the repo.
