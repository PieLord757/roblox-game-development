---
name: marketing-launch
description: "How to launch and grow a Roblox game: the launch-day plan and timeline, creator outreach and deal norms with disclosure, Roblox Ads Manager and sponsored ads (prices unverified, so measure cost per play), the ad plan and suggested test budget, cross-promotion between your own games, Community (group), Discord and Reddit announcements, what works for players 16+, the hard rules, and LAUNCH-KIT-TEMPLATE.md. Use when planning a launch, a chapter release push, creator outreach or any ad spend. Loaded from the marketing router."
---

# Marketing: launch, creators, ads and community

Load `marketing` first if you haven't; it holds the approval rule, the spend gate and the policy facts. **Every post, message, upload, campaign and payment below is drafted, shown to the user, and done only after their OK.** Those steps are marked **(OK needed)**.

Labels: **Policy (official)** is from Roblox docs, Roblox Help or staff posts (and the FTC for disclosure); re-check the linked source before relying on it. **[3RD-PARTY]**, **[UNVERIFIED]**, **[CONFLICT]** and **[SYNTHESIS]** as in the router.

## 1. Before launch

**Store page (check every item; changes are (OK needed)):**
- icon 512 x 512 or larger, readable at 150 x 150;
- 2 to 5 thumbnails (16:9, 1920 x 1080, nothing important in the bottom strip, real game art);
- one gameplay video thumbnail (no voice-over, no lyrics, no claims);
- title and description that match the gameplay, with no reward bait; for older players, state the length ("Chapter 1, about 40 min") and that it plays solo;
- maturity label set (Moderate keeps 16+ and possibly 9 to 15; Restricted means age-verified 18+ only);
- Social Links set (shown to age-checked 16+ only).
- Run `de-ai-ui` and `de-ai-story` over every asset and line. `marketing-creative` has the craft and specs; `publish` and `publish-store-page` own the store page and the publishing order (publish private, test, user's OK, go public). Don't duplicate their work here; check it is done.

**Tracking:**
- Analytics verified in View Events (`live-ops-analytics`).
- **A Share Link per channel and per creator** (Creator Hub). Share Links track sign-ups and reactivations, which makes every channel and deal measurable.
- `marketing-log.md` started.

**Free reach (each submission is (OK needed)):**
- **Launch Experience Event** with Notify Me, made public and **submitted for Off-Platform Featuring at least 7 days before** start.
- **Standout Games** nomination if the game is genuinely novel.
- A private test with players from the community before launch to catch first-time-player problems (one blog suggests 50 to 100 testers [UNVERIFIED]); pair it with `testing-first-time-player`.

**Why external marketing pays the developer (Policy, official, Creator Rewards since July 24, 2025):**
- 5 Robux when an Active Spender plays 10+ minutes (only the first 3 games that user launches each day count);
- **35% of the first $100** a new or returning (60+ days inactive) user spends in their first 2 months, when you brought them in.
So clips and creators that bring genuinely new players earn money directly, on top of what those players spend.

## 2. Launch-day plan

**The principle: concentrate.** Event start, update announcement, thumbnails, clips, Discord and group posts, and creator videos all land inside one window of a few hours, so the spike is big enough for Home to notice the players who stay.

**Timeline** (chapter releases use the canonical dates in `live-ops-updates` section 4; this list adds the marketing beats on top and never moves those dates):

| When | Marketing beats |
|---|---|
| **T minus 14** | Trailer edit locked. Creator shortlist done, pitches drafted. Clip 1 (teaser) drafted. Ad creatives drafted |
| **T minus 7** | Event public and submitted for featuring (from `live-ops-updates`). Teaser clips start, about 3 a week. Discord and Community announcement. Creator pitches sent with early access **(OK needed)** |
| **T minus 2** | Confirm creator publish times. Load new thumbnails as drafts. Final launch-day checklist to the user as one approval list |
| **T 0** | Release at the fixed hour (a weekend morning in the US is a common choice [UNVERIFIED peak timing]). Update announcement, posts, clips, creator videos within the same 24 hours. For multiplayer-optional games, small servers early so lobbies look full, with bot fill as the fallback [UNVERIFIED tip] |
| **T 0 to +4 h** | Watch crash rate, Error Report, DataStore errors and the onboarding funnel (`live-ops`). Hot-fix through configs **(OK needed)** |
| **T +3 days** | KPI review. If D1 clears the gate in `marketing`, propose the ad test and paid creators. If not, keep the push small and fix onboarding |
| **T +7 days** | First `WEEKLY-REPORT.md`. Marketing log reviewed: which clip types, creators and channels brought players who stayed |

## 3. Creators: outreach, deals and disclosure

### How hits used creators [3RD-PARTY]
- **Dead Rails:** creators came organically *after* Roblox's official socials featured it. The developer had about 70 earlier games.
- **Grow a Garden:** a partnership with a creator with a huge audience (about 12M TikTok followers) when the game was small took it from about 500 CCU to roughly 100K in 2 weeks. A **distribution partner with an audience** is its own lever.
- **Doors:** grew mostly through reaction videos; merch came later and became content in turn.
- Many top creators cover games **for free when the game is trending, or genuinely scary or funny on camera** [SYNTHESIS]. Early access is the currency.

### The outreach process
1. **Shortlist 20 to 50 creators,** mostly small and mid YouTube and TikTok horror and Roblox channels with 5K to 500K average views. Check each one's recent videos: their audience age, whether they play this genre, and whether they disclose sponsorships. **Never pick creators whose audience is mainly under 13 for a 16+ game.**
2. **Write the pitch (the craft):**
   - **One paragraph.** Their name and a specific video of theirs you watched. What the game is in one line. Why it will be good on their channel (a scare their reactions suit, a mystery their viewers will theorize about).
   - The trailer link, an early-access or private-server invite, their personal Share Link, and the release date and embargo if any.
   - No attachments they didn't ask for, no follow-up more than once.
   - Run it through `de-ai-story`. A pitch that reads as a template gets ignored.
3. **Offer free early access first. Pay only after the game proves it retains players** (the gate in `marketing`).
4. Sending any pitch, DM or email is **(OK needed)**. Draft them all into the kit; the user approves the batch.

### Deal norms and prices [all UNVERIFIED; real deals are private]

| Tier | Typical structure | Reported price |
|---|---|---|
| Nano and micro Roblox channels (100 to 10K subs) | Shoutout or short playthrough via marketplaces | $1.50 to $10 a shoutout; a dedicated review about $200 |
| Mid channels (about 250K average views) | Dedicated video or integration | about $2.4K to $6.1K a video (estimate at $10 to $25 gaming CPM) |
| About 650K average views | Dedicated video | about $6.5K to $16K |
| Top Roblox creators | Often organic; paid only through agencies | no public data |

Treat every number as a hypothesis. Judge a deal by **joins through its Share Link, the D1 of that cohort, and cost per retained player**, logged in `marketing-log.md`.

### Disclosure (Policy, official: FTC and Roblox)
- Sponsored content must be **disclosed in the video itself**, clear and conspicuous ("ad", "#ad", "paid"). A description-box mention alone is not enough.
- **Free early access or items with real value count as payment.** A creator who got early access and a free pass is a sponsored creator.
- **The advertiser is liable** for the creator's failure to disclose (FTC precedent: the Warner Bros. *Shadow of Mordor* settlement).
- The creator must tick YouTube's **"contains paid promotion"** box.
- Roblox's Video Stars members must disclose any material connection to Roblox; a children's ad watchdog found earlier creator disclosures inadequate, and Roblox committed to creators using "paid".
- **Every paid or gifted deal has a written brief** that requires in-video disclosure and the paid-promotion box, the deliverables, the date, and the Share Link. Agreeing to a deal is **(OK needed)**.

## 4. Roblox Ads Manager

### What exists (Policy, official)
- **Formats:** Sponsored tiles on Home, placement in search results. Other products (rewarded video, Home feature brand ads, portal and immersive ads) exist with varying coverage.
- **Objectives:** **Plays**; **Earnings** (limited; finds likely spenders and reports ROAS); **Engagement** (beta since June 2026; targets players who count toward Highly Engaged Players, expect a higher cost per play, only for games not yet in Kids/Select).
- **Audiences:** All; New (not played in 180+ days); Recent (30 days, needs 10K+); Lapsed (30 to 180 days, needs 20K+). Advanced targeting by location, **age**, gender, genre, device. API age buckets `AGE_13_17`, `AGE_18_24`, `AGE_25_PLUS`.
- **Bidding:** auto-bid by default; engaging games may get "ads system discounts". Daily or lifetime budget. **[CONFLICT]** one source says pricing shows as CPM; the current Ads Manager page doesn't mention it.
- **Payment:** card (18+) or ad credits (13+), minimum 1 credit. **[CONFLICT]** the credit rate is given as 263 or 285 Robux per credit in different sources; the official page states neither. **Read the conversion preview in Ads Manager.** Converted Robux can't be reversed. A first card campaign charges $5 up front.
- **Review:** campaigns within 24 hours, asset moderation up to 48 hours.
- **Reports:** spend, impressions, clicks, plays, cost per play (CPP), playtime, earnings, ROAS. Plays and earnings are attributed over up to 30 days and can appear up to 48 hours late. Views include New, Recent and Resurrected (7D and 30D) users. Invalid traffic is refunded after about 16 days.
- **Open Cloud ads API:** campaigns can be created through the API; bid type only `AUTOMATED` in v1. Any API write is **(OK needed)**.

### What ads can and can't do (Policy, official)
- **Ad players don't count toward Home ranking.** They only help retrieval. Roblox says ads "should not harm organic distribution".
- **Clone-like games** (metadata or place similar to existing games) may get no spend, no conversions, or lower search rank.
- Best practice: give results **3 to 5 days**; if plays don't convert, fix onboarding first; test the launch URL; use launch data for ad-specific onboarding; judge on the Recent and Resurrected views, because All Users understates impact.

### Costs [UNVERIFIED: no official rate card]
- About **5,000 Robux a day** is a suggested floor for Sponsored; **3,000 to 4,000** in low-competition genres; **7,000 to 10,000** for obby and tycoon (one blog).
- About **4 to 12 Robux per visit**, attributed to unnamed DevForum developers (same blog).
- These are hypotheses. **Measure your own CPP** in the first test and plan from that.

### Building the ad plan and suggested budget [SYNTHESIS]
1. **Gate:** only after D1 clears the gate in `marketing`. Otherwise the plan says "not yet" and why.
2. **Objective:** Plays (Earnings once the game monetizes).
3. **Targeting:** age **18 to 24 and 25+** for a 16+ game, plus 13 to 17 if the game is rated Moderate. Device targeting if the game plays best on PC or console (older-skewing [UNVERIFIED]). New audience for launch; **Lapsed (30 to 180 days)** for chapter releases once the game has enough players.
4. **Creatives:** 3 to 5 thumbnails from `marketing-creative`, each testing a different idea.
5. **Budget:** a **3 to 5 day test**. Suggest a daily amount from the unverified range for the genre (for example 3,000 to 5,000 Robux a day for a niche horror or story game), times the test length, capped by the user's ceiling from `studio-profile.md`. State it in Robux and, using the Ads Manager conversion preview, in credits. Label the figure as derived from unverified ranges.
6. **Stop and scale rules, written before launch:** after 3 to 5 days, compare CPP and the New Users view's D1 against organic D1. Scale only if the payback (Creator Rewards plus earnings from that cohort) is plausible. Stop if CPP is high and the ad cohort's D1 is far below organic.
7. **Timing:** around launches, chapter releases and events. **Never during an experiment or a before/after measurement window** (`live-ops-analytics`).
8. Creating the campaign and spending are **(OK needed)**, separately.

### In-game ads and self-promotion (Policy, official)
- In-game ad integrations (anything published for pay, or with a call to action or off-platform promotion) must be **registered in Ads Manager at least 5 days before start**, are **labelled** (Roblox renders labels legible within 500 studs), and moderated (about 48 hours). **Self-promotion inside your own game counts.**
- **All ads are hidden from under-13 users** through `PolicyService` (`AreAdsAllowed`), and disclosed in plain language. Rewarded video ads go to 13+ only. Use `AdService:RegisterDisclosureButton` for interactive disclosures.
- Revenue share applies to campaigns starting on or after Jan 1, 2027.

## 5. Cross-promotion between your own games [SYNTHESIS with an official caveat]
- **Mechanisms:** an in-game portal or teleport to a sibling game, a "more from the studio" board, shared Community membership, update announcements.
- **Caveat:** the Ad integrations doc says registration and labelling apply "even if you're promoting your own content inside your game". It does not say clearly whether a portal to your own game counts. Until Roblox clarifies, either:
  - **register it** as an ad integration (5+ days ahead) and accept the label, or
  - keep cross-promotion to **neutral, non-call-to-action references** (a lore cameo, a poster in the world with no "play now").
- Teleport traffic counts as "Teleport" acquisition and helps retrieval only.
- Multi-game studios such as Splitting Point and Urbanshade carry audiences between titles [3RD-PARTY]. Which sibling games exist is in `studio-profile.md`.

## 6. Community, group and Discord announcements
- **Roblox Community (formerly Groups):** make the group own the game, so ad credits, permissions and events live in one place. Use Community announcements and group events (they appear on the Events tab and can be featured in About). **Shouts have low reach;** don't rely on them.
- **Update announcements:** 60 characters, one every 3 days (Policy, official).
- **Discord:** linked only through Social Links (16+). The launch post goes in `#announcements`, full notes in `#changelog`, clips in `#clips`. Structure is in `live-ops-updates`.
- **Reddit:** subreddit rules could not be checked during research. Read the sidebar and pinned posts before every post; look for a showcase or feedback thread. Post as **"seeking feedback"** with a clip or GIF and specific questions, not as an ad. r/robloxgamedev is for developers (show process: a lighting before and after, a monster design breakdown); r/roblox is for players (clips, following its rules); genre subs like horror gaming communities after reading their rules. **Never astroturf** (no alt accounts, no fake "I found this game").

**Writing an announcement (the craft):**
- **First line is the news,** in specific words: "Chapter 2 opens Saturday at 10am ET." Not "Hey everyone!!"
- **One image or clip** that shows the new thing.
- **What it is, how long it plays, what's new since last time,** in 3 short lines.
- **One action:** RSVP, play, or watch. Not five links.
- Same voice as the game; `de-ai-story` over every line. Every announcement is **(OK needed)**.

## 7. What works for players 16+
**Data [3RD-PARTY unless marked]:**
- Roblox: the 17 to 24 cohort is the fastest growing, and US 18+ users monetize more than 50% higher than under-18s (Q1 2026 filing). 18+ users grew about 50% year on year.
- Among age-checked users (about half of DAU, Q1 2026): 36% under 13, 38% 13 to 17, 26% 18+.
- Popular genres with older players include shooters, sandbox and simulation, with broad support for **horror, racing and survival**. Older players lapse to other games and come back.
- A 2026 study says the 16+ audience is "particularly driven by entertainment IP".
- A skeptical view argues self-reported ages are inflated. Treat age data as directional.

**Implications [SYNTHESIS]:**
- **Art direction that doesn't look like default Roblox is the hook.** Thumbnails must show the real thing.
- **Tone:** dry, specific and grounded in the setting. No all-caps hype, no brainrot. `de-ai-story`.
- **Channels:** TikTok and Shorts horror and atmosphere clips; Reddit genre communities; YouTube horror and let's-play creators (not only kids' Roblox channels); Discord; X for dev-process posts.
- **Respect their time:** say it plays solo, say how long a chapter is, show visible save points, no predatory monetization. Older players spend more, and post about dark patterns more.

## 8. Hard rules
> Nobody can waive these: not the user, a creator or a partner. The one exception is the first rule, which the user satisfies by giving their OK. If asked to break any other, explain the rule and stop.
> - **Never post, send, publish, upload, register or spend without the user's explicit OK** for that action.
> - **Never buy, bot or reward** likes, favorites, visits, followers or reviews. No alt accounts. No astroturfing.
> - **Never use "free Robux", giveaway or reward-bait** titles, descriptions, thumbnails or posts.
> - **Never post fake or enhanced thumbnails or trailers on-platform.** Real gameplay only.
> - **Never run undisclosed sponsorships.** In-video disclosure plus the paid-promotion box, every time, including gifted early access.
> - **Never target ads or creators at under-13 audiences** for a 16+ game. In-game ads are hidden from under-13s with `PolicyService`.
> - **Never direct players off-platform in game text,** signs or chat. Discord goes in Social Links only (shown to 16+).
> - **Never run an in-game ad or self-promotion** without registering it at least 5 days ahead, or keep it to neutral non-call-to-action references.
> - **Never use dark-pattern notifications** (fake urgency, bait-and-switch, disguised ads, trick purchases, gating on opt-in).
> - **Never clone another game's metadata,** name, characters or art.
> - **Never use copyrighted music** or footage you don't have rights to. Audio comes only from the legal sources in SG1 (`sound`) and SR10 (`sound-roblox`); Roblox's licensed library is for use on Roblox only, not in off-platform videos.
> - **Never store passwords, payment details or API keys** in the repo.

## 9. `LAUNCH-KIT.md`
Copy `LAUNCH-KIT-TEMPLATE.md` (in this folder) to `design/<game>/marketing/<launch-or-chapter>/LAUNCH-KIT.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). Fill every section. `marketing-creative` supplies the trailer shot list, clip scripts and thumbnail briefs; this skill supplies the rest.

## What great looks like
- A launch where event, featuring, announcement, thumbnails, clips and creator videos land in one window.
- Every channel and creator has a Share Link, and the log shows which ones brought players who stayed.
- A small, written ad test with stop rules set before it starts, judged on your own CPP.
- Creator pitches that read like a person who watched their videos wrote them.
- Every sponsored video disclosed on screen.

**Common mistakes:**
- buying ads on launch day before D1 is known
- quoting a blog's Robux-per-day figure as if it were Roblox's price
- one Share Link for everything, so nothing is attributable
- paying a creator before the game retains players
- forgetting that early access counts as payment for disclosure
- a sibling-game portal with a "Play now!" sign and no ad registration
- posting to a subreddit without reading its rules
- an announcement that starts with "Hey guys" and buries the date
- running ads during a before/after measurement window

## Output
1. **`LAUNCH-KIT.md`** filled in, with drafts in the same folder.
2. **`marketing-log.md`** entries for every post, pitch, deal and campaign.
3. **A chat overview:** the launch-day timeline (one line per beat), a table of the trailer cuts and 5 clips, the announcement drafts' first lines, the ad plan (objective, targeting, days, suggested budget in Robux, the stop rule, and "prices unverified"), the creator shortlist count and tiers, and a numbered list of every action waiting for the user's OK. Say plainly if the spend gate is not met.

## Tools
- Creator Hub (read only without approval): Share Links, Ads Manager reports, Analytics.
- `live-ops-analytics` for the gate and for cohort D1 by source.
- `marketing-creative` for assets, `de-ai-ui` and `de-ai-story` for look and voice, `de-ai-audit` before the kit goes to the user.

## Sources
- Ads Manager: https://create.roblox.com/docs/production/promotion/ads-manager
- Open Cloud advertising: https://create.roblox.com/docs/cloud/guides/advertising
- Ad integrations: https://create.roblox.com/docs/production/promotion/ad-integrations
- Advertising Standards: https://en.help.roblox.com/hc/articles/13722260778260
- Kids/Select launch (Engagement objective, social links 16+): https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717
- Content maturity: https://create.roblox.com/docs/production/promotion/content-maturity
- Creator Rewards: https://create.roblox.com/docs/creator-rewards
- Standout Games: https://create.roblox.com/docs/creator-programs/standout-games
- Experience events: https://create.roblox.com/docs/production/promotion/experience-events
- Communities: https://devforum.roblox.com/t/introducing-roblox-communities/3268307
- Video Stars: https://en.help.roblox.com/hc/articles/360026092011
- FTC disclosure [3RD-PARTY summary]: https://revisionlegal.com/internet-law/youtubers-ftc-endorsement-rules-compliance/ and https://www.ftc.gov/node/74130
- Grow a Garden interview [3RD-PARTY]: https://gamesbeat.com/janzen-madsen-interview/
- Older players [3RD-PARTY]: https://gamesbeat.com/data-shows-gamers-are-not-graduating-out-of-roblox-as-they-age-up/
- Ad budgets [UNVERIFIED]: https://rowatcher.com/news/roblox-ads-in-2026-the-minimum-budget-that-actually-works
- Creator prices [UNVERIFIED]: https://www.collabpals.com/hire/gaming/roblox-content
