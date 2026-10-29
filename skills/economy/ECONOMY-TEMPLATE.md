# ECONOMY.md template

Copy this into the game's folder (the default path in `studio-profile.md`, or `design/<game>/ECONOMY.md`). Fill every section. Delete the guidance lines in italics when done. `economy-design` fills sections 1 to 5; `economy-monetization` fills sections 6 to 11.

---

# <Game name>: economy

**Status:** DRAFT / PRICE LIST APPROVED (<date>, by the user in chat) / LIVE
**Last updated:** <YYYY-MM-DD>
**Game type:** <solo story / co-op / competitive / ...> **Audience:** <from studio-profile.md>
**Monetization model (one sentence):** <for example: free story, direct-buy cosmetics, a supporter pass, capped paid revives, a paid private server>

## Summary (5 lines, what the user reads first)
1. <currencies, one line>
2. <number of passes and products; price range>
3. <fairness verdict: PASS, or what was cut>
4. <expected earnings range and its main assumption>
5. <what needs the user's approval now>

## 1. Currencies
*At most one earnable soft currency and one premium cosmetic currency. Story and solo games: prefer none premium. Dashboard limit: 5.*

| Currency | Earned or bought | Used for | Why it exists (one line) | Logged as |
|---|---|---|---|---|
| | | | | `LogEconomyEvent` name |

## 2. Sources and sinks
*Every way a currency enters or leaves. Every source has a sink that scales with it. Cap anything that runs without the player.*

| Currency | Source or sink | Action | Amount | How often | Cap | Transaction type |
|---|---|---|---|---|---|---|
| | Source | | | | | Gameplay / Onboarding / TimedReward / IAP / ... |
| | Sink | | | | | Shop / Gameplay / ... |

## 3. Wallet curve (player who never pays)

| Point | Typical player balance | Heavy player balance | What they can afford / are saving for |
|---|---|---|---|
| End of session 1 | | | |
| Day 7 | | | |
| Day 28 | | | |

**Checks:** first choice of what to buy within 10 minutes? Most earnings spent by day 7? Still a goal at day 28?

## 4. Pacing

| Window | What new thing arrives | Free or paid |
|---|---|---|
| First minute | | Free |
| First 10 minutes | | Free |
| Each session | | |
| Each week | | |
| Each chapter or update | | |

**Free cosmetic(s) earnable by play:** <name, and when it is earned>

## 5. Instrumentation
*Every source and sink above has a `LogEconomyEvent` call. Shop funnel: opened, viewed item, prompted, purchased.*

- [ ] Economy events wired for every row in section 2
- [ ] Shop funnel wired
- [ ] Verified in a published test build (events don't record in Studio)

## 6. Product list (the price list for approval)
*Prices from the ladder: 49 / 99 / 149 / 199 / 249 / 299 / 399 / 499 / 699 / 799 / 999 / 1,499 / 1,799. Class: cosmetic, convenience, booster, second chance, random. Hard power is never listed.*

| # | Name (says exactly what you get) | Contents | Class | Type (pass / dev product / subscription / private server) | Robux | Gift variant? | Gate result | Roblox ID (after creation) |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | PASS | |

**Volume tiers (if any):** <tiers and value per Robux; top tier at most 2× the bottom>
**Private server price:** <Robux per month, or free> (changing it later cancels all subscriptions)
**Paid access:** <none / price; if used: no Robux gates anywhere, no private servers>

## 7. Fairness check
*Run the fairness gate in `economy-monetization` on every SKU.*

- **Free-player test:** <can a non-payer finish everything at normal difficulty in reasonable time? how long?>
- **Advantage over other players:** <none / explain>
- **Pressure UI:** <none; every paid option has a free option beside it>
- **Convenience and second-chance items, and why each is still fair:**
  - <item>: <reason, cap>
- **Reviewer verdict:** <PASS / items flagged, by a fresh reviewer agent, date>

## 8. Revenue estimate
*Never a promise. Show the assumptions.*

| Case | MAU | Payer conversion | ARPPU (Robux) | Creator Rewards (est.) | Monthly DevEx $ |
|---|---|---|---|---|---|
| Low | | | | | |
| Middle | | | | | |
| High | | | | | |

Formula: MAU × conversion × ARPPU × 0.70 × DevEx rate ($0.0038 standard, $0.0054 U.S. 18+ in R15-only games), plus Creator Rewards.

## 9. Policy compliance

- [ ] Avatar setting R15 Only; no R6 path
- [ ] No hard-coded prices; Dynamic Price Check run
- [ ] PolicyService flags checked on join
- [ ] Paid random items: none / disclosed and gated (describe)
- [ ] Rewarded ads: none / eligible, reward 3 to 10 Robux value, never a gate
- [ ] No fake timers, stock counts or always-on discounts
- [ ] No Premium-only perks; no cross-game sales
- [ ] Managed Pricing: opted in (date, with OK) / not yet / enrollment state checked in Creator Hub

## 10. Implementation status

- [ ] Idempotent `ProcessReceipt` (tested by replay)
- [ ] Pass ownership checked on join and after purchase; history persisted
- [ ] Studio purchase simulation guarded by `IsStudio()`
- [ ] Live product IDs and prices match section 6

## 11. Approval and change log

| Date | Change | Approved by the user in chat? |
|---|---|---|
| | Initial price list | |
