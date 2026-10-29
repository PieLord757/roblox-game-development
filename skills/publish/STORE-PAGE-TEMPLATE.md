# STORE-PAGE.md template

Copy this into the game's folder (the default path in `studio-profile.md`, or `design/<game>/STORE-PAGE.md`). It holds the store-page draft and the launch checklist. Delete the guidance lines in italics when done. `publish-store-page` fills sections 1 to 6, `publish-compliance` fills sections 7 to 10, and `publish-launch` fills sections 11 and 12.

---

# <Game name>: store page and launch

**Status:** DRAFT / PRIVATE / PUBLIC (FRIENDS) / PUBLIC (RFY EXCLUDED) / PUBLIC (RFY ON)
**Last updated:** <YYYY-MM-DD>
**Publishing account or community:** <from studio-profile.md>
**Linked testing report:** <path to TEST-REPORT.md> **Verdict:** <publishing blocked / not blocked>
**Linked economy:** <path to ECONOMY.md> **Price list approved:** <date / no>

## Summary (5 lines, what the user reads first)
1. <the hook, exactly as players will see it>
2. <genre > subgenre; expected label; tier>
3. <hard gates: age check, rating, R15, tests: done / not done>
4. <current stage and the next step>
5. <what needs the user's OK now>

## 1. Title
**Title:** <title>
**Why this name:** <one line>
**Checks:** [ ] search for the exact name finds nothing confusingly similar [ ] no filtered or sensitive words [ ] reads in full on a phone tile

## 2. Hook (first 160 characters)
> <hook text>

**Character count:** <n> / 160
**Stranger test:** <what a fresh reviewer said the game is, after reading only this>

## 3. Description (1,000 characters max)
```
<full description as it will appear>
```
**Character count:** <n> / 1,000
**Checks:** [ ] no hashtags or tags [ ] no giveaway or money framing [ ] no controls list [ ] no off-platform directions [ ] every feature bullet is something in the current build

## 4. Icon
**File:** <path, 512×512 or larger>
**Subject:** <one line>
**Checks:** [ ] readable at 150 px [ ] reads in grayscale [ ] stands apart in a row of the genre's top 10 icons [ ] from the real game [ ] text (if any) legible at 150 px
**Variants made:** <paths>

## 5. Thumbnails
*At least 3 at launch, 1920×1080, real gameplay, nothing important at the bottom edge. Never the default.*

| # | File | Idea it tests | What it shows | Active? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Video thumbnail:** <none / file> (uploads used this month: <n> / 3) **Checks:** [ ] real gameplay [ ] no voice-over [ ] no lyrics [ ] no promotional claims [ ] no features the game lacks
**A/B plan:** <which variants stay active, when the next swap happens (next major update)>

## 6. Localization
| Language | Name | Hook | Key UI strings | Checked for tone by |
|---|---|---|---|---|
| Source: <language> | | | | |
| | | | | |

**`AutoLocalize` off on proper nouns:** [ ] done (list them)

## 7. Genre
**Genre > subgenre:** <from the list in publish-compliance>
**Why (core loop, not theme):** <one line>
**Locked until:** <date + 3 months after setting>

## 8. Maturity questionnaire
*Answer for the most extreme content. Evidence = a screenshot path of that moment.*

| Topic | Most extreme instance in the game | Answer | Evidence |
|---|---|---|---|
| Violence | | | |
| Blood | | | |
| Fear | | | |
| Crude humor | | | |
| Language | | | |
| Romance, alcohol, gambling-like content | | | |
| Free-form user creation / social spaces | | | |
| User-shared media / endless feeds | | | |
| Generative-AI interactions | | | |
| Paid random items / paid item trading | | | |

**Questionnaire Preview label:** <label> **Descriptors:** <list> **Non-compliant regions:** <list>
**Target:** Moderate or lower. **Restricted:** not chosen / chosen by the user on <date> (irreversible)
**Submitted:** <date, with the user's OK / not yet>

## 9. Tier and account
- [ ] Publishing account age-checked (confirmed by the user, <date>)
- **Tier:** 16+ and Trusted Friends / all ages (user's decision, <date>; requirements met by the user)

## 10. Avatar setting and compliance
- [ ] Avatar setting: R15 Only
- [ ] No R6 path (morphs, cutscene rigs, seat swaps checked): <result>
- [ ] Compliance checklist from `publish-compliance` complete (paste it here with ticks and evidence)

## 11. Launch checklist
**Gate A, before the first private publish (new game)**
- [ ] `TEST-REPORT.md` from a milestone run: no Critical failure (saving and analytics may be "pending the private build", not a pass)
- [ ] Products and prices match the approved table in `ECONOMY.md` (or nothing sold yet)
- [ ] Creator account age-checked; avatar setting R15 Only
- [ ] Sections 1 to 6 drafted

**Stage 1, private publish** (OK needed)
- [ ] OK given: <date>
- [ ] Published; version visible in Creator Hub history; `game.PlaceId` set

**Gate B, before going public (and before every update to a public game)**
- [ ] `TEST-REPORT.md` from a Phases 0 to 11 run on the published place: no Critical failure, no NOT RUN on saving or exploits
- [ ] `PREPUBLISH-CHECKLIST.md` (testing skill) complete; waivers dated by the user
- [ ] Analytics events arriving; live purchase path and save-on-rejoin checked through the Roblox client
- [ ] Live products and prices match `ECONOMY.md`
- [ ] Sections 1 to 10 complete; questionnaire submitted (with OK)

**Stage 2, early testers** (OK needed for invites)
- [ ] Testers chosen by the user; invited: <date>
- [ ] Findings: <confusion points, time to fun, would they return>
- [ ] Fixes re-tested and republished privately (OK: <date>)

**Stage 3, public, Friends only** (OK needed)
- [ ] OK given: <date>

**Stage 4, public, excluded from RFY** (OK needed)
- [ ] OK given: <date>
- [ ] Share Links created for every off-platform post
- [ ] Onboarding funnel loses under 30% before the first meaningful action
- [ ] First-play bounce causes examined and fixed
- [ ] No crash, softlock or save bug
- [ ] At least 2 thumbnails active

**Stage 5, RFY on** (OK needed)
- [ ] Planned for: <Thursday or Friday, U.S. afternoon, date>
- [ ] Someone available to watch and fix for 48 hours
- [ ] OK given: <date>

**After launch**
- [ ] Day 0 to 7 watch list running (`publish-launch`)
- [ ] First `WEEKLY-REPORT.md` on day 7 (`live-ops-analytics`)
- [ ] Standout Games survey drafted (after first traction, localization and a trailer); submitted with OK: <date>

## 12. Launch log

| Date | Action | Approved by the user in chat? | Result |
|---|---|---|---|
| | | | |
