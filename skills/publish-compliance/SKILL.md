---
name: publish-compliance
description: "The 2026 rules a Roblox game must meet to be published and stay visible: the creator age check, publishing tiers (16+ vs all ages), the Maturity and Compliance questionnaire, content labels (target Moderate; Restricted is 18+, irreversible and region-blocked), genre rules, the R15 Only avatar setting for the 18+ DevEx rate, and the common moderation and reduced-exposure risks, with a compliance checklist. Writes the compliance sections of STORE-PAGE.md. Use before the first publish, after any content change, and whenever a label, genre or tier decision comes up (load publish first for the approval gate)."
---

# Compliance

Load `publish` first for the approval gate. **Submitting the questionnaire, changing the genre, changing the avatar setting on a live game, and changing tiers each need the user's OK.** Drafting answers in `STORE-PAGE.md` does not.

## Why this matters
In 2026 compliance is no longer paperwork at the end. It decides who can see the game at all. An unrated game can't be played. A game labeled Restricted loses every player under 18 and every player who never verified, forever. A creator account without an age check can't push a single update. Get these wrong and the best store page in the world shows to nobody.

## How facts are marked
**Policy (official, checked 2026-10):** from Roblox Creator Hub docs, staff DevForum posts and earnings letters. Re-check the source before a decision; Roblox changes these often. **[UNVERIFIED]** marks claims not confirmed against a primary source.

---

## 1. The creator account
**Policy (official, checked 2026-10):**
- **The publishing account must be age-checked to publish or update.** Since June 2026, publishing new content or pushing updates requires the account to have passed Roblox's age check (Facial Age Estimation). Without it, nothing ships.
- Only the user can do this. Ask early, not on launch day.
- Audience Expansion (Creator Rewards) and local-currency paid access need the owner to be **ID-verified**. Rewarded and immersive ads need ID verification and 2FA.
- If the game is owned by a community (group), check which account publishes and that it meets these. `studio-profile.md` says which, if it exists.

## 2. Publishing tiers (live since 2026-05-19)
**Policy (official, checked 2026-10):**

| Tier | Who can play | Creator requirements |
|---|---|---|
| Personal use | You and your collaborators | none |
| **16+ and Trusted Friends** | Age-checked players 16+, plus Trusted Friends | Age check; account in good standing; account at least 2 days old |
| All ages (adds Roblox Kids 5 to 8 and Roblox Select 9 to 15) | Everyone, subject to the label | All of the above, plus ID verification, 2FA, and **either** an active Plus or Premium subscription (2 consecutive months per the docs) **or** a fee: a refundable 1,000-Robux publishing fee, or a 50,000-Robux expedited review (48 hours). The fee is refunded after 60 or 90 days with 25 highly engaged players and no moderation. The game must also pass an evaluation and hold a Minimal, Mild or Moderate label. |

**The all-ages evaluation:** age-checked 16+ players play the game first. Roblox checks that engagement is authentic (account age, play history, spend), and its real-time moderation system reviews gameplay and reports. No minimum player count is published. A third-party guide claims "500 highly engaged players in 60 days" [UNVERIFIED].

**Reach (Policy, official, checked 2026-10):**
- **Only about 51% of global DAU are age-checked** (65% in the U.S.), as of the end of Q1 2026. 26% of age-checked users are 18+.
- **Players who haven't age-checked can't see 16+ games.** They default to content-restricted accounts.
- Since early June 2026: Roblox Kids accounts (5 to 8) see only Minimal and Mild; Roblox Select (9 to 15) sees up to Moderate; 16+ get the full library except Restricted.

**Decision rule:**
- **16+ and Trusted Friends is the default** for games aimed at 16+. It is free and immediate.
- Going all-ages adds 9 to 15-year-olds (for Moderate content), but costs money or a subscription, ID, 2FA and an evaluation. **It is the user's decision,** not the agent's, and every payment step is the user's to do.

## 3. The Maturity and Compliance questionnaire
**Policy (official, checked 2026-10):**
- **Where:** Creator Dashboard > the game > Publish settings > Content rating > Start (or Restart) > Save and Continue on each page > Questionnaire Preview (shows the label, descriptors and any non-compliant regions) > Submit.
- **Answer for the most extreme content in the game,** not the typical moment.
- **Resubmit after any update that changes an answer.**
- **Unrated games are unplayable** for everyone except their developers. (The date this took effect, reported as 2025-09-30, is [UNVERIFIED]; the rule itself is in the docs.)
- **Resubmitting pauses rewarded-ads eligibility** while it is under review. Plan resubmissions around that.
- The questionnaire also asks about **paid random items, paid item trading, user-shared media, endless feeds and generative-AI interactions.** Declare any AI-driven NPC chat.
- **Inaccurate answers** lead to moderator review, the label being replaced or removed (removal makes the game unplayable), and action against the game or account. Appeals go through roblox.com/report-appeals.

**Process:**
1. Before opening the form, list every piece of content in the game that touches a descriptor: violence, blood, fear, crude humor, language, gambling-like mechanics, romance, alcohol, user creation, social spaces, AI chat, paid random items, trading.
2. For each, find the most extreme instance and screenshot it. Write the answer and the evidence in `STORE-PAGE.md`.
3. Use the Questionnaire Preview to confirm the label before submitting.
4. Show the user the answers, the previewed label and any non-compliant regions. **Submit only with their OK.**

## 4. Labels
**Policy (official, checked 2026-10):**

| Label | Content allowed (summary) | Who can play |
|---|---|---|
| Minimal | Occasional mild violence; light unrealistic blood; occasional mild fear | Kids, Select, 16+ (Kids and Select only through the all-ages tier) |
| Mild | Repeated mild violence; heavy unrealistic blood; mild fear; mild crude humor | Kids, Select, 16+ |
| **Moderate** | Moderate violence; light realistic blood; moderate fear; moderate crude humor; unplayable gambling content | Select (9 to 15) and 16+ |
| Content May Vary | Answered "no age-restricted content" to the first question only | Age-checked 16+ only |
| **Restricted** | Strong or realistic violence; heavy realistic blood; romantic themes; alcohol; strong language; unplayable gambling content | **Age-verified 18+ only** |

**Target Moderate.** It allows tense action, moderate fear and light realistic blood, and keeps every 16+ player (and 9 to 15 if the game later goes all-ages).

**Restricted is a one-way door. Never answer toward it without the user's explicit sign-off.**
- The creator must verify they are 18+ with ID before answering for Restricted.
- When a game becomes Restricted, servers restart and remove players not verified as 18+, and unverified collaborators are removed from Team Create.
- **The Restricted label can't be changed afterward,** only its descriptors.
- **Restricted games are unplayable in some regions,** including South Korea, Saudi Arabia and Türkiye.
- The rule changed over time: "17+" experiences launched in 2023, and a 2025 policy post still used 17+ wording. **Current docs and the Q1 2026 earnings letter say Restricted means age-verified 18+.** Use 18+.

**Content that pushes a game to Restricted:** strong violence, heavy realistic blood, strong language, alcohol, romantic themes. If a design needs one of these, raise it with the user before building it, not at publish time.

**Other rules that matter:**
- Free-form user creation needs 16+. Social hangouts need 16+, or 18+ with private spaces.
- "Sensitive issues" games are 16+ and not recommended to players who aren't age-verified.
- Content that implies sexual activity is banned outright. Playable gambling is banned.

**IARC is coming.** Roblox is moving to regional IARC ratings (ESRB, PEGI, USK, GRAC) "later this year" (2026). Expect a new questionnaire; re-check this section when it lands.

## 5. Genre
**Policy (official, checked 2026-10):**
- Pick the genre that matches the **core loop**, not the theme.
- **The genre can be changed only once every 3 months** (Publish Settings > Game Details). Write down the reason for the choice in `STORE-PAGE.md`.
- Roblox may re-genre the game and email you; you get one appeal.
- Genre feeds the genre Top and Trending charts. Changes take a few days to show.

**The genre list:**
- **Action:** Battlegrounds & Fighting, Music & Rhythm, Open World Action
- **Adventure:** Exploration, Scavenger Hunt, Story
- **Education**
- **Entertainment:** Music & Audio, Showcase & Hub, Video
- **Obby & Platformer:** Classic Obby, Runner, Tower Obby
- **Party & Casual:** Childhood Game, Coloring & Drawing, Minigame, Quiz
- **Puzzle:** Escape Room, Match & Merge, Word
- **RPG:** Action RPG, Open World & Survival RPG, Turn-based RPG
- **Roleplay & Avatar Sim:** Animal Sim, Dress Up, Life, Morph Roleplay, Pet Care
- **Shooter:** Battle Royale, Deathmatch Shooter, PvE Shooter
- **Shopping:** Avatar Shopping
- **Simulation:** Idle, Incremental Simulator, Physics Sim, Sandbox, Tycoon, Vehicle Sim
- **Social**
- **Sports & Racing:** Racing, Sports
- **Strategy:** Board & Card Games, Tower Defense
- **Survival:** 1 vs All, Escape
- **Utility & Other**

**Examples:** story-led solo games fit Adventure > Story; combat-led ones RPG > Action RPG or Action > Open World Action; horror escape Survival > Escape (DOORS uses this). Standout Games calls RPG, strategy, puzzle and shooter "heavily underrepresented".

## 6. Avatar setting: R15 Only
**Policy (official, checked 2026-10):**
- The **U.S. 18+ DevEx rate is $0.0054 per earned Robux** (vs $0.0038 standard), effective 2026-06-08, on spend from U.S. players verified as 18+ (products, passes, subscriptions, private servers).
- It applies **only if the game is 100% R15:** Avatar settings set to "R15 Only", and **no R6 spawn or swap during active play.**
- Custom humanoid rigs need at least 15 parts or joints. A game with no visible player character qualifies.
- Eligibility is checked automatically.
- Standout Games also favors R15 or custom rigs.

**Check:** search for every morph, cutscene rig, vehicle seat swap and character-replacement script. Each must produce an R15 (or 15+ part) rig. Record the result in `STORE-PAGE.md`. Set the setting before the first publish so it never changes on a live game.

## 7. Moderation and reduced-exposure risks
**Official causes (Policy, official, checked 2026-10):**
- Inaccurate maturity answers (label replaced or removed; game unplayable; account action).
- Restricted content without a Restricted label.
- Metadata leading with giveaways or monetary rewards (reduced exposure, Creator Dashboard banner).
- Misleading thumbnails or metadata; non-unique, cloned games.
- Thumbnail or video rule breaks (fake gameplay, real footage, lyrics, voice-over, promotional claims).
- A faulty `ProcessReceipt` (product hidden from the Shop).
- Rewarded-ad abuse (payouts revoked, eligibility lost).
- Creator Rewards fraud (bots, alts, teleport manipulation, chargebacks).
- Misleading subscriptions (taken down); fake urgency in discounts; undisclosed odds.
- Directing players off-platform.

**Platform enforcement:** a real-time multimodal moderation system shuts down about 5,000 violating servers a day; servers with heavy violating behavior are shut down automatically.

**Anecdotal cases from creators (not policy, but cheap to prevent):**
- Old free-model assets containing a phone number or social handle got popular games suspended. **Scan every imported asset.**
- A merch billboard was treated as "directing users off-platform".
- Automated gore detection flagged a game.
- Words in a title tripped filters.
- Vague "Misusing Roblox Systems" and "Real-World Sensitive Events" takedowns.

IP and DMCA takedowns are a known cause but weren't verified in the research behind this skill. Use only owned or properly licensed assets and audio.

## 8. Compliance checklist
Copy into `STORE-PAGE.md` and tick each with evidence. This complements the `testing` `PREPUBLISH-CHECKLIST.md` (which checks that the age rating is set); it does not replace it.

- [ ] Publishing account is age-checked (the user confirmed).
- [ ] Tier chosen: 16+ and Trusted Friends (or all-ages, by the user's decision, with every requirement met by the user).
- [ ] Questionnaire answered for the most extreme content, with evidence screenshots; Questionnaire Preview label recorded; **submitted only with OK.**
- [ ] Label is Moderate or lower, or Restricted by the user's explicit, written decision (owner and collaborators 18+ and ID-verified first).
- [ ] Generative-AI NPCs, user-shared media and free-form creation declared (or none).
- [ ] Paid random items and paid trading declared and gated by `PolicyService` (or none).
- [ ] No sexual content; no playable gambling.
- [ ] Genre and subgenre chosen from the list, with the reason written down.
- [ ] Avatar setting R15 Only; no R6 path found.
- [ ] Every imported asset scanned: no external links, handles, phone numbers or real-world sensitive references.
- [ ] Social links only in the official social-link fields; nothing in-game directs players off-platform; no "buy cheaper elsewhere".
- [ ] Rewarded ads only if eligible (see `economy-monetization`).
- [ ] Description and thumbnails pass the rules in `publish-store-page`.

**Ongoing:** re-run the questionnaire whenever content changes (remember it pauses ads eligibility during review); watch the Creator Dashboard for "reduced exposure" banners and moderation messages; watch for the IARC questionnaire.

## What great looks like
- Every gate is confirmed weeks before launch, with the user's own steps (age check, ID) done early.
- The questionnaire answers are backed by screenshots of the most extreme moment, so a moderator review changes nothing.
- The label is the one the design intended, chosen on purpose.
- Nothing in the game or on the page can be read as sending players off Roblox.

## Common mistakes
- Answering for the typical moment instead of the worst one.
- Adding a gorier death animation in an update without resubmitting.
- Drifting into Restricted because one line of dialogue swears.
- Picking a genre for its chart instead of the core loop, then being stuck with it for 3 months.
- A cutscene that swaps to an R6 rig and quietly loses the 18+ rate.
- Leaving a free-model asset with a creator's social handle on a sign.

## Output
Fill these sections of `STORE-PAGE.md` (from `publish/STORE-PAGE-TEMPLATE.md`): Genre, Maturity questionnaire, Tier and account, Avatar setting, Compliance checklist. In the chat overview defined in `publish`, give the expected label, the tier, the age-check status and the R15 result, one line each.

## Sources
Roblox Creator Hub (read 2026-10-29): content maturity (`https://create.roblox.com/docs/production/promotion/content-maturity`), publish experiences (`.../production/publishing/publish-experiences-and-places`), genres (`.../production/publishing/experience-genres`), U.S. 18+ DevEx rate (`.../production/monetization/18-plus-devex-rate`), Standout Games (`.../creator-programs/standout-games`).
DevForum staff posts: new publishing requirements and evaluation (2026-04-13); alternate publishing requirements for Roblox Kids and Select.
Roblox investor relations: Q1 2026 shareholder letter; newsroom post on romantic and sexual content policy (2025-08-15); U.S. 18+ DevEx rate announcement (2026-04-30).
