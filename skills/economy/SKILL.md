---
name: economy
description: "Start here for any Roblox game's economy and monetization. Explains the fairness standard (cosmetics and convenience only, never pay-to-win), the approval rule (the user approves the price list before any product, pass or price is created), the 2026 money facts that shape every decision, and which sub-skill to load: economy-design (currencies, sources and sinks, inflation, pacing, generosity) or economy-monetization (product types, pricing, fairness gate, revenue math, policy). Produces ECONOMY.md from ECONOMY-TEMPLATE.md. Use when designing any currency, reward, shop, pass or product, and before creating anything in Creator Hub."
---

# Economy and monetization (start here)

## Why this exists
An economy decides how a game feels long before anyone spends a Robux. Rewards that come too slowly feel like a chore; rewards that come too fast make every number meaningless by day 3. Then the shop decides whether players trust the game. Older players (16+) notice manipulation fast: a revive prompt on the death screen with no free option, a currency that hides the real price, a "limited" timer that resets every day. They leave and say so in reviews.

Done well, it works the other way. A generous economy keeps players returning, which is exactly what Roblox's Home recommendations reward in 2026 (28-day retention and play days). Roblox's Creator Rewards then pays for deep sessions even from players who never buy. Fair cosmetics sold to happy players earn more over a game's life than power sold to angry ones.

**The standard:** every game has an `ECONOMY.md` that lists:
- every currency, with every source and sink
- the expected wallet curve
- every pass and product, with its class, its type and its Robux price
- a fairness check, item by item: **cosmetic and convenience only, never pay-to-win**

The user approves the price list in chat before anything is created.

## The approval rule (read this first)

> **Nothing is created, priced or changed on Roblox without the user's explicit OK, given in chat for that specific action.** Draft it in `ECONOMY.md`, show the price table in chat, ask, then act. An earlier OK does not cover a later action.
>
> This covers, at minimum:
> - **creating** any pass, developer product, subscription or paid private server
> - **setting or changing any price**, including putting an item on or off sale
> - **enabling paid access** or changing its price
> - **opting into Managed Pricing**, or accepting or rejecting a price-optimization result
> - **enabling rewarded or immersive ads** and submitting the ads questionnaire
> - **uploading** pass or product icons
> - **spending** Robux or money of any kind
>
> MCP tools that make these changes (for example `manage_monetization` and `manage_experience`, under whatever prefix your session shows) count as outward actions. Call them only after the OK for that exact change.
>
> Writing `ECONOMY.md`, writing shop code, and testing purchases in Studio need no approval.

If the user says "just set it all up", read back the exact list of items and prices that will be created before you do it.

**Changing a private-server price cancels every active subscription.** Say so when you ask for approval of that change.

## Studio facts
Read `studio-profile.md` at the project root if it exists. It holds:
- the audience
- hard rules (for example, solo play required)
- the default path for game docs
- which account or community owns the game

These skills never hardcode them. If it doesn't exist, ask the user:
- the audience age
- whether the game is solo, co-op or competitive
- whether any monetization is off-limits

Then offer to save the answers as `studio-profile.md`.

## Money facts that shape every decision
**Policy (official, checked 2026-10):** facts from Roblox docs, earnings letters and staff posts. Re-check the source in `economy-monetization` before you rely on one for a decision; Roblox changes these often.

- **The creator keeps 70%** of pass, developer product and Robux subscription sales. A 100-Robux item earns 70 Robux.
- **The standard DevEx rate is $0.0038** per earned Robux (since 2025-09-05).
- **The U.S. 18+ DevEx rate is $0.0054** (since 2026-06-08). It applies to spend from U.S. players verified as 18+, on products, passes, subscriptions and private servers, **only if the game's avatar setting is "R15 Only"** and no R6 rig appears during play. Set R15 Only from the start; `publish-compliance` has the details.
- **Premium Payouts ended on 2025-07-24.** They were replaced by **Creator Rewards**: 5 Robux per Active Spender per day who plays at least 10 minutes and has your game among their first 3 of the day, plus Audience Expansion (a 35% share of what new or returning players you bring in spend in their first 60 days). Deep sessions now earn money with no sale at all.
- **Roblox Plus** ($4.99 a month, launched 2026-04-30) pays creators for Plus sign-ups prompted in-game and for Plus subscribers who use a paid private server. Plus discounts are paid by Roblox, not the creator. Roblox Premium "will soon be discontinued": design no Premium-only perks.
- **Cross-game pass and product sales are disabled** (since 2026-05-30). Sell inside the game that grants the item.
- **Paid access must include the whole game.** No chapter paywalls inside a paid-access game. Paid access and private servers can't be combined.
- **Paid random items (loot boxes) need full odds disclosure** and `PolicyService` gating per player. Rewarded ads have strict reward rules. Both are in `economy-monetization`.
- **Prices must never be hard-coded in UI.** Plus subscribers, regional pricing and price tests all show different prices; read them live.

## Which sub-skill to load

| You need | Load |
|---|---|
| Currencies, sources and sinks, inflation control, the wallet curve, progression pacing, how to make an economy feel generous, `LogEconomyEvent` plan | `economy-design` |
| Product types (passes, developer products, private servers, subscriptions, Plus, Creator Rewards, rewarded ads, paid access), price psychology, the fairness gate, the recommended model for story/solo and for competitive games, the top-game price table, revenue math, policy compliance, the implementation checklist | `economy-monetization` |
| The output document | `ECONOMY-TEMPLATE.md` (in this folder) |
| The actual Luau for purchases and receipts | built-in Roblox skills if your session has them (load with the `skill` tool), plus the implementation checklist in `economy-monetization` |
| Testing purchases and receipts before publish | `testing` (receipt idempotency is a Critical item in its `PREPUBLISH-CHECKLIST.md`) |
| Tracking the economy after launch | `live-ops-analytics` |

Load `economy-design` first, then `economy-monetization`. Prices only make sense once you know what players earn for free.

## The process
1. **Read** `GAME-DESIGN.md` for the game (category, core loop, return engine) and `studio-profile.md` if it exists.
2. **Design the free economy** with `economy-design`: currencies, sources, sinks, pacing, the day 1, 7 and 28 wallet curve for a player who never pays.
3. **Design the paid layer** with `economy-monetization`: pick the model, list every SKU, class it, price it, run the fairness gate on each.
4. **Write `ECONOMY.md`** from `ECONOMY-TEMPLATE.md` into the game's folder (the profile's default path, or `design/<game>/ECONOMY.md`).
5. **Present the overview in chat** (format below) and **wait for the user's approval of the price list.**
6. After approval, and only for the items approved: create the products (with OK for that action), record the real IDs in `ECONOMY.md`, build the shop, then test with `testing`.
7. Any later price change or new SKU goes back through steps 3 to 5.

## Who does what
- **The build thread** designs, writes `ECONOMY.md`, implements the shop and receipts, and tests them.
- **A fresh reviewer agent** (for a first economy or any change to prices) reads `ECONOMY.md` cold and runs the fairness gate in `economy-monetization` on every SKU. It reports any item it would classify differently.
- **The user** approves the price list and every outward action.

## What a great economy looks like
- **A free player can finish everything that matters.** Every story beat, every mode, every ending. Payment speeds up or decorates; it never unlocks the game.
- **Rewards arrive faster than players expect, early.** The first reward lands in the first minute; the first meaningful choice of what to spend on comes within 10 minutes.
- **Every currency has somewhere to go.** Wallets don't pile up into meaningless numbers, and no sink feels like a tax.
- **Prices are honest and legible.** Sold in Robux, named for what you get, with nothing hidden behind an exchange rate.
- **Buyers are proud, not embarrassed.** What they bought shows off taste, supports the game, or saves them friction. It never makes them the reason someone else lost.
- **The shop is quiet.** Players find it when they want it. It doesn't find them mid-fight.

## Common mistakes
- Pricing before designing the free economy, so prices are guesses and the free path gets starved to make them look good.
- Selling power ("2× damage", "best sword") and calling it convenience.
- A premium currency with an odd exchange rate, or packs that never divide evenly into item prices.
- A revive offer that only appears on the death screen, with no free option beside it.
- Hard-coding prices in UI text.
- Creating products before the user approved the list, or changing a private-server price without warning that it cancels subscriptions.
- Granting a purchase in `PromptProductPurchaseFinished` instead of an idempotent `ProcessReceipt`.
- Designing around Premium Payouts or cross-game sales, both gone.

## Output
Every economy pass ends with two things:
1. **`ECONOMY.md`** in the game's folder, from `ECONOMY-TEMPLATE.md`.
2. **A clear overview in chat.** The file holds the detail; the chat overview is what the user reads. Give, in this order:
   - **The model in one sentence** (for example: "free story, cosmetic passes, capped paid revives, a paid private server").
   - **Currencies:** each one, with its main source and main sink, in one line each.
   - **The price table:** every pass and product with class, type and Robux price, in a table.
   - **The fairness verdict:** PASS, or each item that failed and why. Flag every convenience or second-chance item and say why it is still fair.
   - **Expected earnings range,** with the assumptions stated (see the revenue math in `economy-monetization`).
   - **The ask:** "Approve this price list so I can create these products?" Then wait.
