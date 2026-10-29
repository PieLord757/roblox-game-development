---
name: economy-design
description: "Craft for designing a Roblox game's free economy: how many currencies, mapping every source and sink, controlling inflation, pacing progression across day 1, 7 and 28, making rewards feel generous, and instrumenting it with LogEconomyEvent. Writes the currency, source/sink and wallet-curve sections of ECONOMY.md. Use before designing any currency, reward, upgrade or shop, and before pricing anything (load economy first for the approval rule)."
---

# Economy design

Load `economy` first if you haven't. It holds the approval rule and the output format. This skill covers the free economy: what players earn and spend without paying. Prices come after, in `economy-monetization`.

## Why the free economy comes first
The paid layer sits on top of the free one. If you price first, you end up starving the free path to make purchases look attractive, which is the most common way a fair-looking shop turns pay-to-win. Design the game as if nobody ever buys. Then sell things that sit beside that path, never in the way of it.

## Step 1: Decide the currencies

**Rule: one earnable soft currency, and at most one premium cosmetic currency.** Every extra currency is another number the player has to understand and another exchange rate that can feel like a trick.

- **Soft currency.** Earned by playing, spent on progress or cosmetics. Examples: coins, scrap, knobs, salvage.
- **Premium cosmetic currency (optional).** Bought with Robux and sometimes earned slowly, spent only on cosmetics.
- **For story and solo games, prefer no premium currency at all.** Sell cosmetics directly for Robux. It is more honest, it avoids the currency-disclosure and paid-random-item traps, and players can see the real price of every item.
- **Event currencies** are fine if they expire into something (convert to soft currency or a cosmetic at the end), never into nothing.
- **Name currencies from the setting.** "Coins" and "Gems" read as generic; a currency that belongs to the world (lamp oil, tithes, scrap) makes the economy part of the fiction. The `de-ai-story` skill has naming rules if the project has it.

Roblox's Economy dashboard tracks at most **5 currencies** per game. Treat that as a hard design ceiling.

## Step 2: Map every source and sink, before building
Write the full table in `ECONOMY.md`. Each row gets: the currency, the action, the amount, how often it happens, and whether it is capped.

**Typical sources:**
- quest or objective rewards
- enemy, boss or chest drops
- chapter or level completion
- first-time achievements
- daily login or daily objective
- rewarded ad (small, see `economy-monetization`)
- purchase (Robux)

**Typical sinks:**
- upgrades and unlocks
- consumables (ammo, healing, repair kits, torches)
- cosmetic shop
- fees (repair, fast travel, re-spec)
- crafting
- rerolls of free, earned rewards (never paid random items without disclosure)

**Every source needs a matching sink that scales with it.** If a late-game player earns 10× what an early player earns, late-game sinks must cost roughly 10× too, or the wallet runs away.

## Step 3: Draw the wallet curve
For a player who never pays, estimate the soft-currency balance at:
- end of session 1
- day 7
- day 28

Do it for a typical player and a heavy player. Then check:
- **Session 1:** the player can afford at least one meaningful thing they chose. If not, the first purchase is too far away.
- **Day 7:** the player has spent most of what they earned, on things they wanted. A large unspent balance means the sinks are weak or unappealing.
- **Day 28:** there is still something to save toward. If a heavy player has bought everything, add depth (prestige cosmetics, a long-term goal) or the economy ends before the game does.

Write the curve as a small table in `ECONOMY.md`. After launch, compare it with the real numbers from the Economy dashboard.

## Step 4: Control inflation
- **Sinks scale with income:** costs rise with level, consumables burn, cosmetics are priced as prestige items.
- **Cap or decay anything that runs without the player.** Idle and AFK income must have a ceiling per session or per day. Uncapped AFK income attracts farming bots and makes every price meaningless. It also risks Creator Rewards fraud flags.
- **Rewarded-ad rewards must not inflate currency or unbalance the economy.** This is a Roblox rule, not just a design preference.
- **No trading in story and solo games.** Trading economies (pet and item trading games are the classic case) inflate, attract scams, and pull in extra policy: trading paid items must respect `PolicyService.IsPaidItemTradingAllowed`, and regional prices create arbitrage.
- **No buy-then-sell loop may make a profit.** The `testing` pre-publish checklist checks this; design it out first.

**How to read the wallet after launch:**
- The median balance rising for payers **and** non-payers means sinks are too weak.
- The balance falling while quit rates rise means sinks are too harsh.
- Roblox's Economy dashboard shows sources and sinks, the average wallet for all users, payers and non-payers, and the top sources and sinks.

## Step 5: Pace progression
Pacing is how often something new arrives. Good pacing feels like the game keeps giving.

- **First minute:** a reward that needs no explanation (currency pickup, a chest, a first unlock). The player learns "doing things earns things".
- **First 10 minutes:** the first real choice of what to spend on. Two or three options, each clearly useful.
- **Each session:** at least one thing to look forward to that a typical session can reach.
- **Each week:** one bigger goal (a cosmetic set, a major upgrade, the next chapter).
- **Use a sawtooth, not a ramp.** A cheap win right after a costly one. Long flat stretches of saving with nothing to buy are where players quit.
- **Time-to-next-unlock grows gently.** If unlock 10 takes 5× as long as unlock 1, that is already a steep curve. Show progress toward it (a bar, a count) so long goals feel reachable.
- **Every chapter or update resets the curve:** new sinks and new rewards so returning players have something to spend on.

These numbers are design judgment, not measured benchmarks. Tune them from the Economy dashboard and the funnels in `live-ops-analytics`.

## How to make an economy feel generous
Generosity is a feeling, and it comes more from timing and presentation than from raw amounts.

- **Over-deliver early.** A slightly larger first reward than the player expected builds trust that lasts.
- **Make every reward visible.** A number that ticks up, a sound, the item appearing in the world. A silent `+50` in a corner feels like nothing.
- **Give free cosmetics.** At least one desirable cosmetic must be earnable by play alone, ideally in the first session. It tells players the shop is not the only way to look good.
- **Free versions of most paid conveniences.** Free revives earned through play, a free daily retry, free checkpoints. The paid version saves time; it doesn't replace something missing.
- **Round, readable numbers.** 100, 250, 500 read as gifts. 137 reads as a calculation.
- **No "almost enough" traps.** Never tune so players end up 10 short of the item they want so they'll buy currency.
- **Respect time away.** Returning after a week should feel like a welcome (a small bonus, new things to buy), not a punishment (lost streaks, decayed items).
- **Retroactive claim** on any season or chapter reward track: late joiners can claim tiers they already reached.

## Instrument it
Log every source and sink with `AnalyticsService:LogEconomyEvent`:
- arguments: the player, `Enum.AnalyticsEconomyFlowType.Source` or `Sink`, the currency name, the amount, the balance after, the transaction type, and an optional item SKU
- transaction types: `IAP`, `TimedReward`, `Onboarding`, `Shop`, `Gameplay`, `ContextualPurchase`, or a custom one
- **server-only, and only recorded in a published game.** Studio calls do nothing.
- up to 5 currencies

List each logging point in the source and sink table in `ECONOMY.md`, so the build thread knows exactly what to wire. The full analytics plan (funnels, custom events, limits) lives in `live-ops-analytics`; the Luau lives in the built-in `rbx-instrument-analytics` skill if your session has it.

## What great looks like
- A non-payer at day 7 has spent most of what they earned, on things they chose, and has a goal for next week.
- Every currency has a one-line reason to exist.
- The source and sink table balances on paper, and the Economy dashboard confirms it within two weeks of launch.
- Nobody needs a calculator to understand a price.

## Common mistakes
- Three or four currencies because "big games have them".
- Sinks that only exist at the start, so wallets explode by week 2.
- Uncapped idle income.
- Earn rates tuned so the free path is miserable and a booster looks necessary.
- Rewards that are logged but not felt (no sound, no visual).
- A free path with no free cosmetic, which tells players the shop is mandatory for self-expression.
- Forgetting to plan new sinks for each update, so returning players have nothing to do with their savings.

## Output
Write these sections of `ECONOMY.md` (from `economy/ECONOMY-TEMPLATE.md`): Currencies, Sources and sinks, Wallet curve, Pacing, Instrumentation. Then hand off to `economy-monetization` for the paid layer. Include the currency list and the day 1, 7 and 28 wallet curve in the chat overview described in `economy`.
