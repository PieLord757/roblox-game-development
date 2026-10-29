---
name: economy-monetization
description: "Craft and rules for a Roblox game's paid layer: every product type (passes, developer products, private servers, subscriptions, paid access, Roblox Plus, Creator Rewards, rewarded ads), price psychology and the Robux price ladder, the fairness gate every SKU must pass, the recommended model for story/solo and for competitive games, a live price table from top games (examples only), revenue math, and 2026 policy compliance (loot-box odds, PolicyService, ads, R15 Only). Writes the product list and fairness check of ECONOMY.md. Use after economy-design and before creating any product (load economy first for the approval rule)."
---

# Monetization

Load `economy` first (approval rule, output format) and `economy-design` (the free economy). This skill covers what to sell, at what price, and how to stay inside Roblox's rules.

**Nothing in this skill authorizes creating a product.** The user approves the price list in chat first. See `economy`.

## How facts are marked
- **Policy (official, checked 2026-10):** from Roblox Creator Hub docs, earnings letters or staff DevForum posts. Re-check the source link at the bottom before a decision; Roblox changes these often.
- **[3P-est]:** a third-party tracker estimate. Trackers disagree with each other by 2 to 5×. Order of magnitude only.
- **[UNVERIFIED]:** could not be confirmed against a primary source.
- **Design judgment:** a recommendation, not a measured fact.

---

## 1. Product types

**Policy (official, checked 2026-10).**

| Type | What it is | Key rules | Best use |
|---|---|---|---|
| **Pass** | One-time purchase, owned forever | Check `UserOwnsGamePassAsync` on join and after `PromptGamePassPurchaseFinished`. Icon up to 512×512, shown inside a circle. Passes promoted outside the game must cost 50 to 800 Robux and can't grant paid random items. | Cosmetic sets, supporter pack, photo mode, soundtrack player, a cosmetic season row |
| **Developer product** | Repeatable or consumable purchase | 1 to 1B Robux. Granted only through `ProcessReceipt` in one server Script. Roblox audits `ProcessReceipt` and hides a broken listed product from the Shop. | Single cosmetic items, capped revives, gifts, tip jar, temporary boosters (solo only) |
| **Subscription** | Monthly auto-renew | Robux: at least 49, creator gets 70%. Local currency: $2.99, $4.99, $7.99, $9.99 or $14.99; 70% in month 1, then **100% from month 2**. One tier only (no Bronze/Silver/Gold). At most 50 per game. Price changes at most every 60 days, with 30 days' notice. Benefits honored for the full term and identical on every platform. Can't gate benefits behind extra tasks (battle passes excepted). Local currency is not sold in some countries (including AR, CN, IN, ID, JP, RU, TR, VN). | A monthly cosmetic drop, or a cosmetic battle pass. Never story access or power. |
| **Private server** | Free, or a monthly Robux fee | The game must be public. **Changing the price cancels all active subscriptions.** Can't be combined with paid access. Roblox Plus subscribers use paid private servers free, and the creator still earns up to 100 Robux per subscriber per month. | "Play alone or with friends, no strangers." Excellent fit for solo and co-op games. |
| **Paid access (Robux)** | Entry fee, 25 to 1,000 Robux | Account at least 30 days old. Not on Xbox. No refunds. Disables private servers and place copying. | A finished premium game, or a short paid closed beta |
| **Paid access (local currency)** | $9.99, $29.99 or $49.99 | Creator gets 50%, 60% or 70%. Desktop and web purchase only. 48-hour refund window, 60-day escrow. Creator needs ID verification, 13+, and Tipalti. **Buyers must get the entire game; Robux can't gate other parts.** Item purchases are still allowed. | A polished premium title with an existing fanbase |
| **Creator Rewards** (replaced Premium Payouts on 2025-07-24) | Paid by Roblox automatically | **Daily Engagement:** 5 Robux per Active Spender per day, if your game is among their first 3 that day and they play at least 10 minutes. An Active Spender spent at least $9.99 in the last 60 days and isn't new or reactivated. **Audience Expansion:** 35% of the first $100 a new or reactivated (60+ days lapsed) user spends anywhere on Roblox in their first 60 days, when they arrive through your Share Link, a direct link or a search for your game's name and play 10+ minutes. Your game must average at least 100 DAU, and the owner must be ID-verified. 60-day hold. | Free money for deep sessions. Use a Share Link in every off-platform post. |
| **Roblox Plus incentives** (Plus launched 2026-04-30, $4.99 a month) | Funded by Roblox | Plus subscribers get 10% off, rising to 20% from month 3; **Roblox pays the discount**, so the creator still gets 70 on a 100-Robux item. 250 Robux a month for the first 3 paid months of each Plus sign-up made through `PromptRobloxSubscriptionPurchase` (60-day hold). Up to 100 Robux per subscriber who spends 60+ minutes in your paid private server. 10% of Robux transfers made through `PromptRobuxTransferAsync` (10 to 500 Robux each). Roblox reports paying creators more than 300M Robux in the first 4 months. | Prompt Plus at a natural moment (opening the private-server menu), never mid-play |
| **Rewarded video ads** | Player opts in to a 6 to 30 s ad for a small reward | See section 7. | A hint, retry token or small top-up at a safe moment |
| **Immersive ads** | Billboards and portals in the world | Public game, ID + 2FA, approved questionnaire, at least 2,000 monthly unique visitors. Gate with `PolicyService.AreAdsAllowed`. | Usually wrong for immersive story worlds. Skip unless the setting has real billboards. |

**Discontinued; never design around these:**
- Engagement-based **Premium Payouts** (ended 2025-07-24, replaced by Creator Rewards).
- The **Creator Affiliate** program (became Audience Expansion).
- **Cross-game pass and developer-product sales** (disabled from 2026-05-30).
- **Roblox Premium** "will soon be discontinued" (staff announcement, 2026-04-13). No Premium-only perks. Premium's 10% purchase bonus was reportedly removed on 2026-05-30 [UNVERIFIED].

### Pass or developer product?
- **Pass:** bought once, owned forever (an outfit set, a weapon skin pack, a supporter badge, photo mode).
- **Developer product:** bought again, or used up (a single item from a rotating shop, a revive, a gift for a friend, a temporary booster).
- **Roblox does not store either per user for you.** Persist ownership and every receipt yourself in DataStores.
- For personalized shop ordering, `RankProductsAsync` and `RecommendTopProductsAsync` exist. Call them once at join (rate limits). The second returns nothing without a sale in the last 28 days.

---

## 2. Price psychology and the Robux ladder

### The ladder
Use charm prices from this ladder: **49 / 99 / 149 / 199 / 249 / 299 / 399 / 499 / 699 / 799 / 999 / 1,499 / 1,799.** These dominate top games (see the price table in section 6).

- **A first "yes" at 49 to 99.** A small, clearly good item. The hardest purchase is the first one; make it easy and worth it.
- **The core at 199 to 499.** Named cosmetic sets, the supporter pack, a season's cosmetic row.
- **One premium bundle at 799 to 1,499** for players who want everything cosmetic this season. Make it a real bundle, not an anchor.
- **Volume tiers rise smoothly.** Better value per Robux at higher tiers, but the **top tier is at most 2× better per Robux than the bottom** (design judgment). A bigger spread makes small packs look like a rip-off. One top game's revive pack runs from 40 down to 19 Robux each (about 2×, feels fair); another game's currency packs run from 13 down to 2.8 Robux per unit (4.6×, small packs feel punishing).

### What to show
- **What the item is**, with a preview (on the character, in the world).
- **The Robux price and what the player keeps forever** ("Yours permanently").
- **"View Item" over "GET IT NOW".** Roblox asks for this, and bans fake stock warnings and inaccurate countdowns.
- **Exact contents** in the name and description. "Ashwood Outfit (coat, boots, lantern skin)" beats "Mystery Bundle".

### What older players read as cynical
- Anchor items priced only to make other prices look small (a 100,000-Robux joke item, a 6,999-Robux level skip).
- Currency rates that hide the real price (7 gems per Robux).
- Packs that leave leftover currency that never divides into item prices.
- Discounts that are always on.

### Gift variants
Mirror every cosmetic with a gift version (a developer product that grants the item to a chosen player in the server). Top games do this for everything. It turns spending into generosity instead of status.

### Prices must be dynamic (Policy, official, checked 2026-10)
- **Read every displayed price live** with `MarketplaceService:GetProductInfoAsync` (or the batch equivalent) on the client. Run Roblox's Dynamic Price Check tool.
- Hard-coded prices show the wrong number to Plus subscribers and regional buyers, and block price optimization.
- **Managed Pricing** (2026-06-15) combines regional pricing and price optimization:
  - Regional prices are held between 30% and 100% of the default price.
  - Subscriptions and private servers are regionalized automatically.
  - Whether new games and items are enrolled automatically is **unresolved**: the announcement says yes, the FAQ says creators pick items during onboarding. **Check Creator Hub > Monetization > Managed Pricing.**
  - Results reported by Roblox: regional pricing in the top 2,500 games in 2025 gave +4 to 10% overall Robux spend and +43 to 52% pass purchases in discounted regions. Price optimization gave about +4% median earnings.
  - Price optimization tests need about 60,000 transactions in 30 days, run about 3 weeks, and repeat at least every 90 days. Players aren't told and can't opt out. Prices are adopted only if total revenue rises.
  - **Opting in is an outward action: ask first** (see `economy`). Recommend opting in at launch.
  - With gifting or trading, regional prices allow arbitrage. Use `GetUsersPriceLevelsAsync` to set transfer rules.

---

## 3. The fairness rules

### Classify every SKU

| Class | Definition | Policy |
|---|---|---|
| **Cosmetic** | No gameplay effect | **Primary revenue.** Always allowed. |
| **Convenience** | Saves time or friction without raising the power ceiling or giving an advantage over anyone | Allowed if the effect is small, affects only the buyer's own play, and the free path is reasonable. Examples: an extra save slot, extra storage, a sandbox mode that disables progression. |
| **Soft power / booster** | Multiplies earn rate | Never in competitive modes. In solo games, only if the game is balanced for a player who never buys it, and the boost doesn't feed a leaderboard. |
| **Hard power** | Directly stronger (damage, health, better weapons) | **Never.** This is the pay-to-win line. |
| **Second chance** | Revive or continue | Solo only, only if checkpoints are generous and free revives are earnable. Cap paid revives per chapter or run. Never on a final boss. Never in PvP. Never tune difficulty around it. |
| **Paid random** | Crates, eggs, spins, rerolls bought with Robux or Robux-bought currency | Avoid. If used at all: cosmetic only, full odds disclosure, `PolicyService` gating (section 7). |

### The fairness gate: every SKU must pass every line
- [ ] **Class** is cosmetic, convenience or (solo only) a capped second chance or booster. **Reject hard power.** Reject paid random unless cosmetic-only, disclosed and gated.
- [ ] **Free-player test:** a player who never pays can finish the whole game at normal difficulty in reasonable time, and earn at least one desirable cosmetic.
- [ ] **No advantage over another player** in any shared mode, leaderboard or PvP.
- [ ] **No pressure UI:** no fake timers, no stock counts, no death-screen-only offers. A free option always sits beside a paid one.
- [ ] **Price** is on the ladder; volume tiers stay within 2× value per Robux.
- [ ] **Type** is a pass if permanent, a developer product if repeatable.
- [ ] **Gift variant** exists for each cosmetic.
- [ ] **Name and description** say exactly what the player gets.
- [ ] **If paid access is used:** no Robux gate on any part of the game, and no private servers.

Write the result of the gate for every SKU in `ECONOMY.md`. If any line fails, the item is cut or redesigned before the user sees the list.

### What 16+ players call fair vs predatory
Evidence: Petrovskaya and Zendle, "Predatory Monetisation?" (*Journal of Business Ethics*, 2022: 1,104 players, 35 techniques); a 2025 interview study of user-generated-game players including Roblox (themes: felt manipulation, monetized relationships, hidden total cost); Catt Small, "Respect the Player" (GDC 2019). No Roblox-specific survey of 16+ fairness views was found; the lists below are synthesis.

**Fair:** cosmetics that don't affect outcomes; one-time purchases with a clear, permanent result; supporter packs; clear Robux prices; earnable versions of most items; optional honest rewarded ads; cosmetic season passes with retroactive claim; a full game playable free (or one clear entry price); gift options; sandbox toys that disable progression.

**Predatory (never):**
- pay-to-win in PvP or on leaderboards
- paid random items with power, or with hidden or misleading odds
- obfuscated currencies; leftover-currency packs
- fake timers or stock warnings (also a Roblox rule)
- purchase prompts mid-combat, or on death with no free option
- energy or stamina gates on story
- paywalls disguised as difficulty spikes
- selling the ending
- social pressure ("your friends bought this"), or paid status flaunted in shared spaces
- paid revives the game is tuned around
- exclusive power items that expire

---

## 4. Recommended models

### Story, chapter and solo games (free-to-play, cosmetic-led)
1. **The story is free.** Every chapter playable without paying. New chapters ship as updates, which are discovery events.
2. **Optional early access to the next chapter for a fixed window** (for example 7 days), then it becomes free for everyone. Label it plainly with the date it turns free. Bundle it with a permanent cosmetic so buyers keep something. This is the one time-based access item; never sell a "permanent" pass whose benefit expires.
3. **Direct-buy cosmetics** (passes and developer products, no randomness): outfits, weapon and tool skins, lantern or UI themes, emotes and finishers, a photo-mode filter pack.
4. **A supporter pack pass at 299 to 499:** soundtrack player, concept-art gallery, a name in the credits, a cosmetic badge.
5. **A chapter cosmetic row** (season-like): a free row plus a 99 to 199 Robux cosmetic row per chapter, with retroactive claim.
6. **A paid private server** at a modest monthly price for "play alone or with friends". Plus subscribers earn the creator up to 100 Robux each a month.
7. **Fair second chances:** free checkpoints, earnable revives, an optional paid revive capped per chapter at about 25 to 40 Robux. Never on the final boss.
8. **A rewarded ad** for an optional hint, retry token or small cosmetic-currency top-up at chapter breaks.
9. **An optional Robux subscription** for a monthly cosmetic drop. Never story or power.
10. **Share Links** in every off-platform post, so Audience Expansion pays for new players you bring.
11. **R15 Only** for the U.S. 18+ DevEx rate.

**Why:** Creator Rewards pays for deep, returning sessions; Home recommendations reward 28-day retention and "deeper, returnable games for older players". A free story maximizes both. Paid access and private servers are mutually exclusive, and paid access must include the whole game, so chapter paywalls are impossible anyway.

**Alternative premium model:** paid access at 100 to 300 Robux for a polished, finished story, with cosmetics on top and no private servers. Use it only once the game has reviews and a fanbase: it cuts reach and the signal volume Home recommendations need. A temporary paid closed beta is a documented use.

**Template from top games:** the horror-escape game DOORS. Cosmetic skins and a 99-Robux cosmetic event-pass row, revives as the main consumable (40 Robux for 1 down to about 19 each in a 25-pack), free revives through codes and group join, and a 499-Robux sandbox Admin Panel that explicitly disables all progression.

### Competitive and skill games
1. **Cosmetics are the business:** weapon and character skins, a rotating daily skin shop (direct-buy, prices shown), finishers, emotes.
2. **Every gameplay item is earnable with play.** If weapons are also sold, they must be side-grades at most, and the earn path must be reasonable for a free player within days, not months.
3. **A cosmetic season pass** with a free row containing at least one desirable cosmetic, retroactive claim, no expiry pressure (finishable in under 50% of the season at normal play, or a grace period), and level skips priced linearly (no exponential top skip).
4. **No boosters that affect ranked play or leaderboards.**
5. **No paid revives in PvP.** No paid random items with power.
6. Private servers for practice and friends.

**Template from top games:** RIVALS, the top-earning game on Roblox in late October 2026, sells mostly cosmetics in a skill game. Weapons are buyable but also earnable with keys; skins and a daily skin shop drive spend. Note what to avoid even there: its 6,999-Robux season-level skip reads as an anchor.

### Battle and season passes (any genre)
- For most players, including payers, a pass is mainly a retention tool. Rewards are typically valued at 10 to 20× the price (Deconstructor of Fun, 2022).
- Pitfalls: grind that causes regret near expiry; cannibalizing other purchases; a free row so rich nobody pays; including enough premium currency to buy the next pass; passes are hard to remove once added.
- Fair rules: cosmetic-only premium row, retroactive claim, no expiry pressure, linear level skips, a desirable free cosmetic.
- A battle pass may be sold as a subscription.

---

## 5. Revenue math
Use this to set expectations in `ECONOMY.md`. Never promise a number to the user; show the range and the assumptions.

**Policy (official, checked 2026-10):**
- Creator share: 70% of Robux on passes, products and Robux subscriptions.
- DevEx: $0.0038 per earned Robux standard; $0.0054 for U.S. 18+ verified spend in R15-only games.
- Roblox's own framing: creators receive 26.6% of in-game spend, or 37.8% for U.S. 18+ spend. (That implies about $0.01 of consumer spend per Robux.)
- DevEx eligibility: 13+ (facial age estimation or ID), verified email, a DevEx portal account, a tax form on file, at least 30,000 earned Robux (= $114 at the standard rate).
- Holds: passes and products about 5 days; Creator Rewards 60 days; local-currency paid access at least 60 days.

**Worked examples (derived):**
- A 99-Robux pass nets 69 earned Robux, about $0.26.
- A 499-Robux pass nets 349 earned Robux: $1.33 standard, or $1.89 at the U.S. 18+ rate.
- Creator Rewards Daily Engagement: 5 Robux, about $0.019, per qualifying Active Spender per day.
- Consumer price of Robux: roughly 400 for $4.99 on mobile and about 500 on web, so $0.010 to 0.0125 per Robux to the buyer [UNVERIFIED; check roblox.com/upgrades/robux].

**A simple estimate formula:**
`monthly DevEx $ ≈ MAU × payer conversion × ARPPU (Robux) × 0.70 × DevEx rate + Creator Rewards`

Pick payer conversion and ARPPU from the game's own Monetization tab once live. Before launch, state them as assumptions and show a low, middle and high case.

**Keep expectations honest:**
- Roblox reports about $1.7B paid to creators in the 12 months to 2026-06-30.
- The median DevEx creator earned about $1,500 in that period, across more than 42,000 participants [press, citing RDC 2026; not on Roblox's own page]. Top-10 averages are tens of millions. **Plan around the median, not the top.**

**Coming payout changes:** Roblox Wallet (daily real-currency payouts for eligible U.S. creators 18+, announced RDC 2026 for later in 2026); a Roblox Card in 2027. A "transition away from DevEx in the U.S. in mid-2027" was reported by press [UNVERIFIED].

---

## 6. What top games sell (examples only)
**[API 2026-10-29]:** names and prices read from Roblox's public APIs on 2026-10-29. **Prices change often; re-check before citing.** These are examples of pricing structure, not recommendations to copy; several sell power, which the fairness gate forbids.

| Game | Passes (Robux) | Notable developer products (Robux) |
|---|---|---|
| DOORS | 99 cosmetic second row of an event pass; 299 skin bundle; 499 Admin Panel (sandbox, progression disabled) | Revives 1 for 40, 5 for 145, 10 for 239, 25 for 479. Knobs (run currency) 250 for 49 up to 16,000 for 1,799 (5.1 to 8.9 per Robux). 5× knob boost 59. +1 save slot 50. Cosmetic currency 25 to 499. A 100,000-Robux joke anchor. Gift versions of everything. |
| Adopt Me! | 50 (event candy boost), 285, 295, 480 VIP, 765, 795 | Currency 85 / 550 / 1,175 / 3,910 for 180 / 1,375 / 3,000 / 10,000 (2.1 to 2.6 per Robux). Heavily discounted variants at 9 / 65 / 138 / 460, likely targeted first-purchase offers (inference). |
| Blox Fruits | 350 to 450 for 2× boss drops, money and mastery; 1,200 a mythical sword; 2,700 an item notifier | Permanent power items 100 to 5,000. Money and mastery packs 50 to 1,499. Cosmetic auras 88 to 350. |
| RIVALS | 59 starter; 95 to 1,425 weapon bundles | Daily skin shop about 299 / 385 to 449 / 479 to 599 by rarity. Season levels +1 for 99 up to +70 for 6,999. Event bundles 499 to 799. |
| Grow a Garden | none | Premium eggs 149; seed packs and chests 199, or 10 for 1,249 to 1,699 (paid random, odds disclosure applies). Slot upgrades 249 to 1,699. |
| Dead Rails | 95 storage; 148 to 175 starting guns | Currency 5 for 65 up to 200 for 565 (13 down to 2.8 Robux per unit). Self-revive 45; team revive 200. Starter pack 149. |
| Pet Simulator 99 | 175 auto-farm; 275 stacking luck; 400 VIP; 625 to 3,250 luck, shiny and hunter passes | Eggs 60 to 90 single, 290 to 485 for 10. Enchant slots 400 to 2,400. |

**Revenue evidence (all [3P-est] or single press reports; no developer or Roblox publishes per-game revenue):** RIVALS about $1.7M to $15M a month depending on tracker; Grow a Garden about $12M in May 2025 alone [press], now far lower; Adopt Me! about $41M to $60M a year; DOORS about $60M lifetime across the studio's games.

**Takeaways:**
1. The biggest earners sell power, competitive edge or collectible status. Cosmetic-led games earn less per player, but keep trust and longevity.
2. RIVALS shows a skill game can top the charts with mostly cosmetics and earnable weapons.
3. DOORS is the best structural template for story or horror: cosmetic rows, capped consumable revives, a progression-disabled sandbox.
4. Trend games earn huge sums briefly, then fall to 1 to 10% of peak within months. Durable earners have depth.

---

## 7. Policy compliance

### Paid random items (Policy, official, checked 2026-10)
- **Scope:** any random outcome bought directly or indirectly with Robux (including Robux-bought currency, keys, tickets and rerolls): capsules, eggs, chests, wheels, upgrades with a success chance, combining, and probability modifiers (luck boosts, pity, rate-up). Random rewards earned free are exempt.
- **Disclosure:** every outcome with numerical % odds summing to exactly 100% (disclaimer if rounded). A long list may sit in a popup, but behind a **labeled** button ("Details" or "Info"); a bare (i) icon is not enough. Disclose before currency is spent. Luck items state their numerical effect, and displayed odds update while active. Once-per-user outcomes update the remaining odds.
- **Per-player gating:** call `PolicyService:GetPolicyInfoForPlayerAsync(player)` on join.
  - `ArePaidRandomItemsRestricted` true: offer a free earnable path, a fixed disclosed order, the outcome sold directly at expected value, hide the item, block the purchase with an error, or keep the player out of areas with paid random items.
  - `IsPaidItemTradingAllowed` false: the player must not trade paid items.
  - `AreAdsAllowed`: gate all ads.
  - Roblox publishes no country list. **Always use the flags, never your own country list.**
- The maturity questionnaire asks about paid random items and paid item trading; declare them (`publish-compliance`).

### Rewarded video ads (Policy, official, checked 2026-10)
- **Game eligibility:** public and unrestricted; no free-form user creation; ads questionnaire approved (**resubmitting it pauses ads eligibility during review**); at least 2,000 unique visitors a month; publisher 13+, in good standing, ID-verified, with 2FA. (The August 2025 launch bar of 100K average DAU is replaced by these.)
- **Viewers:** only users 13+ see ads.
- **UX:** a clear player action before each ad; reward disclosed before; granted immediately after; **never a progress gate**; no screen takeover during gameplay (show only in safe zones or with damage paused).
- **Reward:** a developer product you would normally sell, about **3 to 10 Robux** of value. No Robux, no random items, no economy inflation, no misleading description.
- **APIs:** `AdService:GetAdAvailabilityNowAsync(Enum.AdFormat.RewardedVideo)` right before showing; `AdService:CreateAdRewardFromDevProductId(id)`; `AdService:ShowRewardedVideoAdAsync(player, reward)` and check for `ShowCompleted`; grant through `ProcessReceipt`.
- **Economics:** earnings are EPM × impressions; completion rates of 90%+ and Minimal ratings earn higher EPM. Roblox expected rewarded video to add up to 3% of earnings early on. Treat it as a small extra.

### Other rules (Policy, official, checked 2026-10)
- **Discounts must be genuine.** No false scarcity, no inaccurate timers, no pushy calls to action aimed at minors.
- **Subscriptions:** no misleading offers; the same benefits on every platform; never direct users to buy elsewhere.
- **Creator Rewards fraud** (bots, teleport manipulation, encouraging alt accounts, chargebacks) forfeits rewards or terminates accounts.
- **No off-platform purchase directions** anywhere in the game.
- **R15 Only** avatar setting for the U.S. 18+ DevEx rate; any R6 spawn or swap during play disqualifies the game. Custom humanoid rigs need at least 15 parts or joints; a game with no visible player character qualifies. Eligibility is checked automatically.

---

## 8. Implementation checklist
Build to this after the price list is approved. The `testing` skill verifies it before publish (receipt idempotency is Critical in `PREPUBLISH-CHECKLIST.md`).

- [ ] **One** server-side `MarketplaceService.ProcessReceipt`:
  - If the player isn't in the server, return `NotProcessedYet` (it retries when they rejoin).
  - Look up `receiptInfo.PurchaseId` in a DataStore. If already granted, return `PurchaseGranted`.
  - Otherwise grant, persist with `UpdateAsync`, then return `PurchaseGranted`.
  - On any failure, return `NotProcessedYet`.
  - **Never grant on `PromptProductPurchaseFinished`.**
  - The Roblox docs sample is **not** idempotent. Write your own.
- [ ] **Passes:** `UserOwnsGamePassAsync` on join and on `PromptGamePassPurchaseFinished`; cache the result; persist your own purchase history.
- [ ] **Prices:** every displayed price read live with `GetProductInfoAsync` (or the batch call). Nothing hard-coded. Dynamic Price Check tool run.
- [ ] **PolicyService** checked on join; `ArePaidRandomItemsRestricted`, `IsPaidItemTradingAllowed` and `AreAdsAllowed` respected.
- [ ] **Random cosmetics** (if any): odds in %, summing to 100, labeled "Details" button, shown before spending, live updates.
- [ ] **Rewarded ads** (if any): player-initiated, reward disclosed, 3 to 10 Robux value, never random, never a gate, safe zones only, availability checked right before showing.
- [ ] **Roblox Plus prompt** at a natural moment only.
- [ ] **Avatar setting R15 Only**, with no R6 path anywhere (morphs, cutscene rigs).
- [ ] **Analytics:** `LogEconomyEvent` on every source and sink; a shop funnel with `LogFunnelStepEvent` (opened shop, viewed item, prompted, purchased). Server-only, published games only. See `live-ops-analytics`.
- [ ] **Studio purchase simulation** guarded by `RunService:IsStudio()`.
- [ ] **Product IDs and prices** in the live game match the approved table in `ECONOMY.md` (the `testing` pre-publish checklist checks "products exist, are on sale, and have the right prices"; this table is the reference).

## 9. Launch and tuning
1. **Pre-launch:** the source and sink sheet with the day 1, 7 and 28 wallet curve; the SKU list with classes and prices; user approval.
2. **Week 1:** cosmetics and the supporter pack only. Measure payer conversion and ARPPU (Monetization tab). Don't launch boosters.
3. **Week 2 onward:** check the Economy tab. A growing median wallet means add sinks (rotate the cosmetic shop). If D1 retention is below benchmark (Overview scorecard, needs 100+ DAU), fix gameplay before adding SKUs.
4. **Managed Pricing at launch,** with the user's OK. Review each price-test result before accepting (also an OK).
5. **Each chapter or season:** a new cosmetic row, new thumbnails (`publish-store-page`), an optional early-access pass that turns free. New SKUs go back through the gate and the approval.

## What great looks like
- Every SKU has a class, a gate result and a one-line reason a fan would want it.
- The cheapest item is a genuinely good deal, and the most expensive is a real bundle, not an anchor.
- A reviewer reading the shop cold finds nothing to call manipulative.
- Prices displayed in-game always match what the purchase prompt shows.

## Common mistakes
- Calling a damage boost "convenience".
- A paid revive as the only option on the death screen.
- Volume tiers with a 4× or wider value spread.
- Hard-coded prices.
- A battle pass whose free row has nothing anyone wants.
- Paid access plus "buy chapter 3" (not allowed) or paid access plus private servers (not possible).
- Forgetting gift variants.
- Odds hidden behind an unlabeled (i) icon.
- Creating products before the price list is approved.

## Output
Write these sections of `ECONOMY.md`: Model, Product list (with class, type, price, gate result, gift variant), Fairness check, Revenue estimate, Policy compliance, Implementation status. Then present the chat overview defined in `economy` and wait for approval of the price list.

## Sources
Roblox Creator Hub (read 2026-10-29): monetization overview, passes, developer products, subscriptions, private servers, paid access (Robux and local currency), paid random items, Roblox Plus, Creator Rewards, rewarded video ads, immersive ads, managed pricing, price optimization, Developer Exchange, U.S. 18+ DevEx rate, economy events. All under `https://create.roblox.com/docs/production/monetization/` and `https://create.roblox.com/docs/creator-rewards`.
DevForum staff posts: Creator Rewards (2025), rewarded video expansion (2025-07/08), Managed Pricing (2026-06-15), regional pricing for developer products, publishing requirements (2026-04-13).
Roblox investor relations: Q1 2026 shareholder letter; RDC 2025 and RDC 2026 newsroom posts; regional pricing newsroom post (2025-04-22).
Ethics: Petrovskaya and Zendle (2022), doi:10.1007/s10551-021-04970-6; Catt Small, "Respect the Player" (GDC 2019); Deconstructor of Fun on battle passes (2022).
