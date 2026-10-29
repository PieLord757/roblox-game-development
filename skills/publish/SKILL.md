---
name: publish
description: "Start here for publishing any Roblox game or changing its store page. The first rule: nothing is published, made public or changed on the live page without the user's explicit OK. Explains the publishing order (publish private, test, get the user's OK, go public), the 2026 platform facts that block publishing (age-checked creator account, 16+ tier, maturity labels, R15 Only), and which sub-skill to load: publish-store-page (title, hook, description, icon, thumbnails, A/B tests, localization), publish-compliance (maturity questionnaire, labels, age tiers, moderation risks, avatar setting) or publish-launch (soft launch, timing, Standout Games, day 0 to 7 watch list). Produces STORE-PAGE.md from STORE-PAGE-TEMPLATE.md. Use before any publish, any visibility change, and any store-page edit."
---

# Publish (start here)

## The go-public gate (read this first)

> **Nothing goes public without the user's explicit OK, given in chat for that specific action.** Draft it, show it, ask, then act. An earlier OK does not cover a later action. "The checklist passed" is not an OK.
>
> There are **two separate OKs** in every launch:
> 1. **Before the first private publish.** A private publish is still a publish.
> 2. **Before going public,** after the private build was tested and the user saw the test result and the store-page draft.
>
> Each of these also needs its own OK, because each is outward and some can't be undone:
> - **any publish** of the place, including updates and private test publishes
> - **any visibility or audience change:** Public on, Friends-only off, Recommended For You on or off, early-tester invites, playtester access
> - **submitting the maturity questionnaire,** and especially any answer that makes the game **Restricted** (irreversible)
> - **changing the genre** (locked for 3 months afterward)
> - **uploading a video thumbnail** (only 3 uploads a month; rejected uploads count)
> - **changing the title, description, icon, thumbnails, social links or localization** on the live page
> - **moving to the all-ages tier** (costs a subscription or Robux, plus ID and 2FA)
> - **submitting the Standout Games nomination survey**
> - **creating products or prices** (the `economy` approval rule)
> - **spending** Robux or money of any kind (publishing fee, expedited review, ads)
>
> MCP tools that make these changes (for example `manage_experience` and `manage_monetization`, under whatever prefix your session shows) count as outward actions. Call them only after the OK for that exact change.
>
> Drafting `STORE-PAGE.md`, making images locally, and reading dashboards need no approval.

If the user says "just ship it", read back the exact list of what will change (place version, visibility, page fields) before doing it.

## Why this exists
Most games on Roblox are never seen. Home recommendations test a new game on small groups of players and widen distribution only if those players click, stay past the first 3 minutes and come back. The store page decides the click; the first session decides the rest. A game launched straight to the public with a placeholder icon, a default thumbnail and an untested first minute gets its one early test wasted. With a default-only thumbnail it isn't even eligible for Home recommendation impressions.

2026 also added hard gates that stop a launch cold if nobody checked them: the creator's age check, the 16+ publishing tier, the maturity label, the R15 setting.

**The standard:** every launch has a `STORE-PAGE.md` holding the store-page draft (title, hook, description, icon, thumbnails, genre, maturity questionnaire answers) and the launch checklist. The game goes private, gets tested, gets the user's OK, then goes public in stages.

## The publishing order
**A game that has never been published:**
1. **Milestone testing passes** in Studio (Gate A in `publish-launch`): a `testing` milestone run with no Critical failure. Saving and analytics are marked "pending the private build", because DataStores, `PlaceId` and analytics only work once the place is published. That is not a pass and not a waiver. This is acceptable only because a private publish reaches nobody but the owner and collaborators.
2. **Store page drafted** in `STORE-PAGE.md` and shown to the user.
3. **OK 1:** publish privately.
4. **Test the published private build** (Gate B in `publish-launch`): the full `testing` pre-publish run (Phases 0 to 11, including the Phase 0 DataStore guard, which now protects real data) with `PREPUBLISH-CHECKLIST.md` complete. No Critical failure; no NOT RUN on saving or exploits. Early testers play (with OK for invites).
5. **OK 2:** go public. Then stage it: Public with Friends on, then Public excluded from Recommended For You, then Recommended For You on. Each step is a visibility change and needs its own OK. `publish-launch` has the flow and timing.

**An update to a game that is already public:** the full pre-publish run and `PREPUBLISH-CHECKLIST.md` pass **before** the publish (Gate B), then the OK, then publish.

## Platform facts that block publishing
**Policy (official, checked 2026-10):** from Roblox docs, staff DevForum posts and earnings letters. Re-check the linked source in the sub-skill before relying on one; Roblox changes these often.

- **The creator account must be age-checked to publish or update.** Since June 2026, publishing new content or pushing updates requires the publishing account to have passed Roblox's age check (Facial Age Estimation). If it hasn't, nothing ships. **Check this first.**
- **Publishing tiers (live since 2026-05-19):** "16+ and Trusted Friends" needs an age check, good standing and an account at least 2 days old. "All ages" also needs ID verification, 2FA, and either a Plus or Premium subscription or a refundable fee, plus an evaluation. **16+ is the default for 16+ games.**
- **Only about 51% of global DAU are age-checked** (65% in the U.S.; 26% of age-checked users are 18+, end of Q1 2026). Players who haven't age-checked can't see 16+ games. Plan reach accordingly.
- **Unrated games are unplayable** for everyone except their developers. The maturity questionnaire must be submitted before going public.
- **Target the Moderate label.** **Restricted means age-verified 18+ only, can't be changed afterward, and is unplayable in some regions** (including South Korea, Saudi Arabia and Türkiye).
- **Avatar setting "R15 Only"** for the U.S. 18+ DevEx rate ($0.0054 vs $0.0038).
- **At most 5 never-released games can be released per account per day.**
- Details for each are in `publish-compliance` and `publish-launch`.

## Studio facts
Read `studio-profile.md` at the project root if it exists. It holds which account or community (group) publishes, the audience, how to publish from a second Studio window, and the default path for game docs. These skills never hardcode them. If it doesn't exist, ask the user which account or community owns the game and confirm it is age-checked before you plan a launch.

## Which sub-skill to load

| You need | Load |
|---|---|
| Title, the 160-character hook, description, icon, thumbnails, video thumbnails, thumbnail A/B testing, localization, search | `publish-store-page` |
| The maturity questionnaire, labels, publishing tiers, the creator age check, genre rules, moderation risks, R15 Only, the compliance checklist | `publish-compliance` |
| Private publish, soft launch, going public, launch timing, Share Links, Standout Games nomination, the day 0 to 7 watch list | `publish-launch` |
| The output document | `STORE-PAGE-TEMPLATE.md` (in this folder) |
| Pre-publish testing | `testing` and its `PREPUBLISH-CHECKLIST.md` (required, not duplicated here) |
| Prices and products | `economy` |
| Analytics setup and the weekly report after launch | `live-ops` |
| Trailer, clips, announcements, ads | `marketing` |
| Making sure the icon, thumbnails and description don't look or read AI-generated | `de-ai-ui`, `de-ai-story` (if the project has them) |

## Who does what
- **The build thread** drafts `STORE-PAGE.md`, makes the images, runs the compliance checklist, and prepares each publish step.
- **A fresh reviewer agent** looks at the icon and thumbnails at real display size and reads the hook cold. It reports what the game seems to be and whether it would click. If its answer doesn't match the game, the page is wrong.
- **The user** gives every OK, and is the only one who can do the creator age check, ID verification and any payment.

## What a great launch looks like
- The store page shows the real game, and a stranger can say what it is from the icon and first line alone.
- Every hard gate (age check, tier, rating, R15) is confirmed before the launch date, not discovered on it.
- The first public players arrive into a build that a small audience already played.
- RFY is turned on at a time when the team can watch and fix things, before the weekend peak.
- Every OK was asked for specifically and recorded in `STORE-PAGE.md`.

## Common mistakes
- Treating a private publish as "not really publishing" and doing it without asking.
- Going public with the default thumbnail, which makes the game ineligible for Home recommendations.
- Answering the questionnaire optimistically, then getting the label replaced or removed by moderators.
- Discovering on launch day that the creator account isn't age-checked.
- Turning on Recommended For You before the first 3 minutes were tested.
- Writing "join our Discord" in the game or description instead of using the social-link fields.

## Output
Every publish pass ends with two things:
1. **`STORE-PAGE.md`** in the game's folder (the profile's default path, or `design/<game>/STORE-PAGE.md`), from `STORE-PAGE-TEMPLATE.md`. It holds the store-page draft and the launch checklist.
2. **A clear overview in chat.** The file holds the detail; the chat overview is what the user reads. Give, in this order:
   - **Checklist status:** the testing verdict (link to `TEST-REPORT.md`), then each hard gate (age check, tier, rating, R15, products match `ECONOMY.md`) as done or not done, one line each.
   - **Store-page preview:** the title, the 160-character hook exactly as players will see it, the genre and subgenre, the expected maturity label, and the icon and lead thumbnail (paths to the image files, or the images themselves).
   - **What will change** if the user says yes, as a short list.
   - **The ask:** one specific question, for example "OK to publish this build privately?" or "OK to make the game public, excluded from Recommended For You?" Then wait.
