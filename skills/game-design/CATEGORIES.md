# Game categories (one taxonomy for Steam and Roblox)

This is the core of the game-design skill set. Every game, new or existing, gets **one main category and at most one secondary** from this list. The brief, pitch and audit skills all read their must-haves, targets and fit labels from here.

Categories are defined by **core loop and player motivation**, not by setting or broad genre. "Horror" is not a category; "escalating room-by-room horror run" is. A zombie game could sit in five different categories depending on what the player actually does every 30 seconds.

There are 40 categories in 8 families. Most games on Steam or Roblox fit one cleanly. Hybrids get a secondary.

---

## How to read an entry

Each entry has the same fields:

- **Is:** a one-line definition.
- **Loop:** the core loop at the moment-to-moment scale, with the session loop where it matters.
- **Motivations:** from the Quantic Foundry set of 12 (below), strongest first.
- **Must-haves:** 3-6 pillars that every hit in the category has. Each one is written so a reviewer can **see it in a playtest** and score it 0-2. If your game is missing one, it is missing a reason the category works.
- **Fails when:** the recurring failure modes, with the cautionary game where one exists.
- **Exemplars:** 3+ real games with numbers and source tags. If the research could not reach 3 sourced exemplars, the entry says **Evidence gap** and the unsourced names carry `[UNV]`.
- **Targets:** session length, D1 and D7 return, and time to first fun. All are `[analysis]` (see "Where the targets come from").
- **Fit:** the solo, real-time, non-menu label (see below).
- **Flags:** traits a studio's hard rules might ban.
- **Guide:** the deep-guidance file, for every category not labeled No.

### Motivation vocabulary (Quantic Foundry's 12, in 6 pairs)
| Pair | Motivations |
|---|---|
| Action | **Destruction** (chaos, explosions), **Excitement** (pace, thrills, surprise) |
| Social | **Competition** (duels, rankings), **Community** (being on a team, belonging) |
| Mastery | **Challenge** (practice, hard content), **Strategy** (planning, careful decisions) |
| Achievement | **Completion** (collect everything, finish everything), **Power** (stronger gear and characters) |
| Immersion | **Fantasy** (being someone else), **Story** (plot and characters) |
| Creativity | **Design** (expression, customizing, building), **Discovery** (exploring, tinkering, figuring out) |

Competition and Community correlate; they are not opposites. Strategy is the one motivation that fell sharply from 2015 to 2024, so readable reactive decisions reach more players than long-range planning.

### The fit label
The label judges each category on three generic axes:
1. **Solo-complete:** the full loop is fun and finishable with nobody else online. Bot fill counts if bots can play the role well.
2. **Real-time:** the core verb happens in real time under the player's direct control, not in turns.
3. **Non-menu:** the main decisions are made with the body in the world, not in inventories, cards or panels.

Values:
- **Yes:** the category's normal form passes all three.
- **Variant:** passes only in a named variant. Pitch and brief must use that variant.
- **No (axis):** the normal form breaks the named axis. Use these to classify existing games. Pitch mode never proposes them.

**Flags** are separate from the label. A studio's `studio-profile.md` may ban some of them outright:
`open-world` · `vehicles` · `air-combat` · `needs-population` (needs many concurrent humans) · `needs-friends` (needs a pre-made group or voice) · `content-hungry` (needs authored content faster than a small team can make it) · `young-skew` (audience evidence skews under 13) · `ip-risk` (the category leans on licensed or imitated IP).

### Source tags
| Tag | Meaning |
|---|---|
| `[SC]` | SteamCharts all-time peak concurrent players, fetched 2026-10-29. Under-reads short spikes. `avg30` is the 30-day average in late Oct 2026; "ret" is avg30 ÷ peak. |
| `[SDB-press]` | A SteamDB figure quoted by a news article. |
| `[3P]` | Another third-party tracker. Less reliable. |
| `[RBX]` | Roblox live API, pulled 2026-10-29 08:09 UTC (off-peak), shown as `off-peak CCU / Sunday 2026-10-25 chart CCU`, plus visits and like %. |
| `[Rolimons]` | Rolimons 7-day-average peak, pulled 2026-10-25. |
| `[press]` | An instantaneous record reported by press. |
| `[GA]` | GameAnalytics "Key Roblox Game Metrics 2026" (500+ games with 1M+ MAU, Aug 2025 to Jul 2026). |
| `[UNV]` | Not verified. Named for orientation only; do not cite it as evidence. |
| `[analysis]` | A design reading, not a measurement. |

Raw peak CCU is not success. Compare retention (avg30 ÷ peak), and treat CCU on idle and clicker games as possibly inflated by AFK or bots.

### Where the targets come from
No source publishes trustworthy per-genre retention. Every target below is `[analysis]`, anchored on these measured numbers:
- **D1:** median 10.3%, top 1% 22.2% `[GA]`.
- **D7:** median 1.6%, top 1% 9.1% `[GA]`.
- **Session length:** median 9.8 min, top 5% 16.6 min, top 1% 21.1 min `[GA]`.
- **Bounce windows:** Roblox scores first-play bounce at under 60 s and at 61-180 s, and counts playtime only up to 60 min per user per day. So a hook must land inside 60 s, and the reason to return tomorrow matters more than a long session.

The targets are "what a good game in this category should aim for", set between the median and the top 1%. A game that misses them is not doomed; it is a signal to look at that part of the design.

---

## How to classify a game

1. **Watch or play 3 minutes and write the verb.** What does the player physically do most often? ("aims and shoots", "parries a ball", "opens doors and hides", "walks a corridor and judges it".) Ignore the setting.
2. **Write the session loop.** What ends a session-sized unit: a round, a run, a floor, a day, a chapter, nothing?
3. **Name the top 2 motivations** from the table above.
4. **Find the family** by the session loop:
   - other players are the content → A or B
   - a pre-made friend group is the content → C
   - a run that ends in death or extraction → D
   - an authored course to clear → E
   - a persistent character or world that grows → F
   - knowledge, observation or a story is the progress → G
   - accumulation, routine or building → H
5. **Pick the main category** whose loop and must-haves match best. If two match, the main one is whichever one **the first 3 minutes** belong to.
6. **Add at most one secondary**, and only if a whole layer of the game runs on that category's loop (a story game whose chapters are stealth heists; an extraction game with an offline-income base). A borrowed feature, such as daily quests or a leaderboard, is not a secondary.
7. **Check the label and flags.** If the main category is labeled No, or a flag hits a hard rule in `studio-profile.md`, say so plainly. That is a verdict input, not a footnote.
8. **If nothing fits**, pick the closest, write "closest fit" and name what is different. Do not invent a category inside a brief. If the same gap shows up twice, propose an addition to this file.

---

## Index

| # | Family | Category | Slug | Fit |
|---|---|---|---|---|
| 1 | A. Competitive skill | Team tactical and objective PvP | `team-tactical-pvp` | No (solo) |
| 2 | A | Duel arena shooter | `duel-arena-shooter` | Yes |
| 3 | A | Parry-tempo duel | `parry-tempo-duel` | Yes |
| 4 | A | Melee skill duel | `melee-skill-duel` | Yes |
| 5 | A | Ability battleground | `ability-battleground` | Yes |
| 6 | A | Platform fighter | `platform-fighter` | Yes |
| 7 | A | Physics sport | `physics-sport` | Variant |
| 8 | A | Battle royale | `battle-royale` | No (solo) |
| 9 | B. Asymmetric, social, party | Asymmetric hunt | `asymmetric-hunt` | Variant |
| 10 | B | Social deduction and bluff | `social-deduction-bluff` | No (solo) |
| 11 | B | Party elimination | `party-elimination` | Variant |
| 12 | B | Social roleplay and avatar | `social-roleplay-avatar` | No (solo) |
| 13 | C. Co-op first | Friend-group co-op comedy | `friend-coop-comedy` | No (solo) |
| 14 | C | Co-op horde mission | `coop-horde-mission` | Variant |
| 15 | D. Run-based PvE | Horde survivor | `horde-survivor` | Yes |
| 16 | D | Action roguelite | `action-roguelite` | Yes |
| 17 | D | Extraction raid | `extraction-raid` | Variant |
| 18 | D | Room-depth horror run | `room-depth-horror-run` | Yes |
| 19 | D | Chase-round survival | `chase-round-survival` | Yes |
| 20 | D | Survival nights | `survival-nights` | Yes |
| 21 | D | Stealth heist | `stealth-heist` | Yes |
| 22 | D | Menu strategy and card runs | `menu-strategy` | No (real-time, non-menu) |
| 23 | E. Mastery course | Precision course | `precision-course` | Yes |
| 24 | E | Rage climb | `rage-climb` | Yes |
| 25 | E | Lane runner | `lane-runner` | Yes |
| 26 | E | Time-trial racing | `time-trial-racing` | Yes |
| 27 | E | Physics and spatial puzzle | `physics-spatial-puzzle` | Yes |
| 28 | F. Worlds and builds | Metroidvania boss mastery | `metroidvania-boss-mastery` | Yes |
| 29 | F | Boss-gated survival sandbox | `boss-gated-sandbox` | Yes |
| 30 | F | Base-raid survival with wipes | `base-raid-wipe` | No (solo) |
| 31 | F | Hardcore build RPG | `hardcore-build-rpg` | Yes |
| 32 | F | Grind ARPG | `grind-arpg` | Yes |
| 33 | G. Knowledge, observation, story | Knowledge-loop mystery | `knowledge-loop-mystery` | Yes |
| 34 | G | Anomaly and rules check | `anomaly-rules-check` | Yes |
| 35 | G | Evidence investigation | `evidence-investigation` | Variant |
| 36 | G | Mechanic-led story chapters | `mechanic-story-chapters` | Yes |
| 37 | H. Accumulate, routine, build | Job-sim empire | `job-sim-empire` | Yes |
| 38 | H | Routine collection sim | `routine-collection-sim` | Variant |
| 39 | H | Incremental accumulate | `incremental-accumulate` | No (real-time skill, non-menu) |
| 40 | H | Build and optimize | `build-and-optimize` | Variant |

---

## A. Competitive skill (other players are the content)

### 1. Team tactical and objective PvP · `team-tactical-pvp`
- **Is:** teams of 3-6 fight over objectives in rounds or long matches where team coordination, economy or drafting decides the result.
- **Loop:** buy or draft → play the round or lane → win or lose the round → adjust economy and plan → next round. Session: one match, 20-50 min.
- **Motivations:** Competition, Strategy, Challenge, Community.
- **Must-haves:**
  1. Fights are decided by aim, positioning and teamwork, never by paid stats.
  2. A between-round economy or draft, so losing a round still shapes the next one.
  3. Maps that rarely change, so knowledge compounds.
  4. A ranked ladder with visible rank.
  5. Cosmetic-only monetization.
- **Fails when:** pay-to-win; bad hit registration; too few players to matchmake (fatal for a new game); a hero roster nobody connects with. Concord shut down 14 days after launch.
- **Exemplars:** Counter-Strike 2 1,818,368 `[SC]`, 43.6% ret. Dota 2 1,291,328 `[SC]`, 50.4% ret. Rainbow Six Siege 200,476 `[SC]`. Marvel Rivals 642,333 `[SC]`. Concord ~697 `[SDB-press]`, cautionary. BedWars 14K / 37K, 11.8B visits `[RBX]`.
- **Targets:** session 25-45 min; D1 20%+; D7 8%+; first fun under 2 min.
- **Fit:** **No (solo).** Bots do not substitute for a human team. Borrow its fairness and ladder ideas only.
- **Flags:** needs-population.

### 2. Duel arena shooter · `duel-arena-shooter`
- **Is:** matchmade 1v1 to 5v5 duels in small arenas, first to N short rounds, loadout chosen before the round.
- **Loop:** queue → spawn with loadout → 30-90 s round → round won or lost → next round until first to N → rewards → requeue.
- **Motivations:** Competition, Challenge, Excitement.
- **Must-haves:**
  1. In a match within 10 s of joining, with no tutorial wall.
  2. Rounds of 1-3 min, first to N rounds; a round loss resets fast.
  3. Power is near-flat: loadout choice is a side-grade, and aim and movement decide fights.
  4. Clear hit feedback on every shot (sound, marker, number or flinch) within 100 ms.
  5. A visible return hook: ranked rank, win streak, or weapon-attached cosmetics with stat trackers.
  6. Bot fill when the queue is empty, and mobile aim assist.
- **Fails when:** pay-to-win weapons; new players matched against veterans; long queues at low CCU; unreadable hits; too few maps. Arsenal fell to 1.5K after RIVALS took its slot.
- **Exemplars:** RIVALS 119K / 266K, 19.0B visits, 93.7% liked, #1 top-earning game, 345K `[Rolimons]` peak about 20 months in and holding 51% `[RBX]`. Hypershot 17K / 36.6K, holds 50% of peak `[RBX]`. Sniper Arena 15K, launched 2026, over-earner `[RBX]`. Murderers VS Sheriffs Duels 6.4K `[RBX]`. Arsenal 1.5K, 6.3B visits, cautionary `[RBX]`.
- **Targets:** session 15-25 min; D1 18%+; D7 6%+; first fun under 15 s.
- **Fit:** **Yes**, with bot fill and a bot-tuned skill curve.
- **Flags:** needs-population (bots cover it at low CCU).
- **Guide:** `categories/duel-arena-shooter.md`

### 3. Parry-tempo duel · `parry-tempo-duel`
- **Is:** a single timed input (parry or deflect) against a threat that speeds up each exchange, until one player misses.
- **Loop:** threat targets you → tap at the right moment → it speeds up and targets someone else → last one standing wins → quick rematch.
- **Motivations:** Challenge, Competition, Excitement.
- **Must-haves:**
  1. One input, legible to a viewer in a single exchange.
  2. Tempo visibly rises each exchange until someone fails.
  3. A clear tell of who is targeted and when the window opens (sound plus visual).
  4. Rematch in under 10 s.
  5. Abilities are side-grades that change how you play, not how strong you are.
  6. The final 1v1 is shown to everyone (spectate or big-screen), because it is the clip.
- **Fails when:** abilities become pay-to-win; latency makes parries feel unfair; it goes shallow after an hour with no new reads.
- **Exemplars:** Blade Ball 11K / 22K, 6.5B visits, 93.5% liked `[RBX]`. Death Ball 3.3K `[RBX]`. Ball VS Ball 14K `[RBX]`, format inferred from title `[UNV]`. Buckshot Roulette 20,135 `[SC]` is a turn-based cousin of the "who breaks first" tension.
- **Targets:** session 12-20 min; D1 16%+; D7 5%+; first fun under 20 s.
- **Fit:** **Yes**, with bot opponents.
- **Flags:** needs-population (bots cover it).
- **Guide:** `categories/parry-tempo-duel.md`

### 4. Melee skill duel · `melee-skill-duel`
- **Is:** close-range fights decided by reading wind-ups and choosing parry, dodge, attack or feint under a stamina limit.
- **Loop:** close distance → read the opponent's wind-up → parry, dodge or punish → manage stamina → win the exchange → win the round.
- **Motivations:** Challenge, Competition, Power.
- **Must-haves:**
  1. A readable wind-up on every attack, long enough to react to on a phone.
  2. A parry, dodge and stamina triangle where each option beats one and loses to another.
  3. A punish window after a successful read that feels earned (hit-stop, stagger).
  4. 1v1 or small arena play with skill-based matchmaking or a protected new-player pool.
  5. Style or weapon variety that changes timing and range, not raw stats.
- **Fails when:** mobile timing feels bad; the skill gap calcifies and new players get stomped (Combat Warriors went from a 1.46B-visit game to 1.2K CCU); style gacha frustrates.
- **Exemplars:** Untitled Boxing Game 8.5K, 1.49B visits, 87.1% `[RBX]`. Combat Warriors 1.2K, 1.46B visits, cautionary `[RBX]`. Deepwoken's PvP layer, 1.1K `[RBX]`. Volleyball Legends and Blue Lock Rivals use the same style-plus-skill structure in sports `[RBX]`.
- **Targets:** session 15-25 min; D1 15%+; D7 5%+; first fun under 30 s.
- **Fit:** **Yes**, with a bot sparring partner that reads like a person.
- **Flags:** needs-population (bots cover it).
- **Guide:** `categories/melee-skill-duel.md`

### 5. Ability battleground · `ability-battleground`
- **Is:** a large open free-for-all where each player picks a character kit of about 4 moves plus an ultimate and brawls with whoever is near.
- **Loop:** spawn → find a fight → combo, dash, block → fill the meter → ultimate → kill streak or respawn → repeat.
- **Motivations:** Power, Excitement, Challenge, Fantasy.
- **Must-haves:**
  1. Spawn straight into a fight with no menu between death and action.
  2. Each kit has 4 moves, an awakening or ultimate, and one combo a new player can find in 2 minutes.
  3. Tech depth beyond the basics (cancels, ragdoll extensions, tech chases) that veterans show off.
  4. Big, readable hit effects scaled to importance, so a 15-player brawl still reads.
  5. A new character or kit on a visible cadence.
- **Fails when:** IP or licensing exposure; balance whiplash; new players stomped; like ratio drifts down (The Strongest Battlegrounds sits at 83.7%).
- **Exemplars:** The Strongest Battlegrounds 47K / 95K, 19.5B visits `[RBX]`. Jujutsu Shenanigans 64K / 250K, peaked about 2 years in and holds 60% `[RBX]`. Heroes Battlegrounds 2.5K `[RBX]`. Fruit Battlegrounds 1.5K `[RBX]`.
- **Targets:** session 15-30 min; D1 16%+; D7 5%+; first fun under 15 s.
- **Fit:** **Yes**; strangers fill large servers, and an empty server needs dummy or bot opponents.
- **Flags:** ip-risk, needs-population (bots cover it).
- **Guide:** `categories/ability-battleground.md`

### 6. Platform fighter · `platform-fighter`
- **Is:** side-view brawls where damage raises knockback and you win by launching opponents off the stage.
- **Loop:** approach → land hits to build damage → launch → edge-guard or recover → take a stock → last fighter standing.
- **Motivations:** Challenge, Competition, Excitement, Destruction.
- **Must-haves:**
  1. Knockback that visibly scales with damage, so the kill threat is readable from the HUD.
  2. Recovery and edge play: ledge grabs, a double jump or up-special, and a real chance to come back.
  3. Hit-stop and camera response on every hit, scaled up for kill hits.
  4. Distinct fighters whose weight, speed and range change the matchup.
  5. A full solo mode: bots at several levels plus a ladder, tower or boss.
- **Fails when:** floaty or laggy input; a grind-heavy relaunch with a thin roster (MultiVersus fell from 153,044 to 29 avg30); bots too dumb to teach anything.
- **Exemplars:** MultiVersus 153,044 `[SC]`, now 29 avg30, cautionary. Gang Beasts `[SC]` figure suspect, a wobbly ring-out brawler. Super Smash Bros. and Brawlhalla `[UNV]`. **Evidence gap:** no sourced Roblox platform fighter in the research.
- **Targets:** session 15-25 min; D1 15%+; D7 5%+; first fun under 30 s.
- **Fit:** **Yes**, solo against bots; online is a layer.
- **Flags:** needs-population for online (bots cover solo).
- **Guide:** `categories/platform-fighter.md`

### 7. Physics sport · `physics-sport`
- **Is:** a one-sentence sport goal ("hit the ball in") played through deterministic physics with a skill ceiling that keeps rising.
- **Loop:** kickoff → position → touch the ball → shoot or pass → goal → reset; matches of 2-5 min.
- **Motivations:** Competition, Challenge, Community.
- **Must-haves:**
  1. A goal explainable in one sentence.
  2. Deterministic physics: the same touch gives the same result, so skill transfers.
  3. Matches of 2-5 minutes, 1v1 to 3v3.
  4. A visible skill ceiling that viewers recognize (aerials, spikes, curves).
  5. A solo training mode or free play that is fun on its own.
- **Fails when:** random physics; a low ceiling (Fall Guys); full teams required with no bots; style gacha read as pay-to-win.
- **Exemplars:** Rocket League 146,902 `[SC]` Steam only. Volleyball Legends 29K / 72K, 95.2% `[RBX]`. Blue Lock Rivals 6.5K, 96.6% `[RBX]`. Basketball Legends 2.6K `[RBX]`.
- **Targets:** session 15-25 min; D1 16%+; D7 5%+; first fun under 30 s.
- **Fit:** **Variant:** solo-viable only with competent bot teammates and opponents plus a training mode that is fun alone.
- **Flags:** needs-population.
- **Guide:** `categories/physics-sport.md`

### 8. Battle royale · `battle-royale`
- **Is:** many players drop onto a map, loot, and fight inside a shrinking zone until one player or squad is left.
- **Loop:** drop → loot → rotate with the zone → fight → place → requeue.
- **Motivations:** Excitement, Competition, Power.
- **Must-haves:** many players and one winner; random loot that makes each match a different story; a shrinking zone that forces fights; near-misses that pull you back.
- **Fails when:** late entry into a crowded field (The Culling 12,622 `[SC]` then about 0); too few players; long downtime between fights.
- **Exemplars:** PUBG 3,236,027 `[SC]`. Apex Legends 624,473 `[SC]`. The Culling 12,622 `[SC]`, cautionary.
- **Targets:** session 20-40 min; D1 18%+; D7 6%+; first fun under 2 min.
- **Fit:** **No (solo).** It needs a full lobby; bots break the "last of many humans" fantasy.
- **Flags:** needs-population, open-world.

---

## B. Asymmetric, social and party (strangers matter)

### 9. Asymmetric hunt · `asymmetric-hunt`
- **Is:** one hunter against several survivors or hiders, who win by completing objectives, hiding or escaping.
- **Loop:** roles assigned → survivors work objectives or hide while the hunter tracks → chase → escape or caught → swap roles.
- **Motivations:** Excitement, Competition, Fantasy.
- **Must-haves:**
  1. The hunter role is aspirational: powerful, readable and fun to play.
  2. Survivors have objectives that pull them into danger (generators, keys), or a disguise verb that is fun on its own.
  3. Chases with counterplay: loops, pallets, hiding spots, stuns.
  4. Small servers (5-9) where every player matters.
  5. Bots good enough to fill either side, so a solo player gets a full round.
- **Fails when:** sides are unbalanced; the queue tilts (nobody or everybody wants to hunt); bots are too weak to make solo play worth it; disguise-only versions need humans hiding.
- **Exemplars:** Dead by Daylight 168,845 `[SC]`, 27.6% ret. Violence District 55K / 105K, 93.0% `[RBX]`. Forsaken 25K / 59.5K `[RBX]`. Flee the Facility 9.7K / 54K `[RBX]`. MECCHA CHAMELEON 340,534 `[SDB-press]` (hide-and-seek variant); its Roblox clones reached about 50K and 37K CCU `[press]`.
- **Targets:** session 15-30 min; D1 16%+; D7 5%+; first fun under 60 s.
- **Fit:** **Variant:** solo-viable only as a solo hunter against bot survivors, or a solo survivor against a bot hunter with authored behavior. Pure hide-and-seek is No.
- **Flags:** needs-population.
- **Guide:** `categories/asymmetric-hunt.md`

### 10. Social deduction and bluff · `social-deduction-bluff`
- **Is:** hidden roles or hidden information, where lying, reading people and voting decide the round.
- **Loop:** secret role → act or bluff → accuse or vote → reveal → next round.
- **Motivations:** Community, Competition, Excitement.
- **Must-haves:** hidden roles revealed at round start; short rounds of 3-10 min; accusation with stakes; the group itself is the content; often a trading or cosmetic economy as the long tail.
- **Fails when:** no progression (Liar's Bar 0.5% ret); not enough humans; toxic play; bots cannot deduce.
- **Exemplars:** Among Us 438,524 `[SC]` Steam only. Murder Mystery 2 367K / 2.16M, #1 on 2026-10-25, record 1.02M `[Rolimons]` in Aug 2026, 12 years in `[RBX]`. Liar's Bar 109,419 `[SC]`. Buckshot Roulette 20,135 `[SC]` (solo against an AI dealer, turn-based).
- **Targets:** session 15-30 min; D1 15%+; D7 5%+; first fun under 60 s.
- **Fit:** **No (solo).** Buckshot's solo form is also turn-based.
- **Flags:** needs-population.

### 11. Party elimination · `party-elimination`
- **Is:** a crowd plays short obstacle or minigame rounds, and each round cuts the field until one winner is left.
- **Loop:** round announced → chaotic course or minigame → qualify or eliminated → next round → crown.
- **Motivations:** Excitement, Competition, Community.
- **Must-haves:**
  1. Each round is explained in its first 3 seconds by what you see.
  2. Rounds of 30-120 s with fast transitions.
  3. Physical comedy that makes losing funny.
  4. Enough round variety, or player-made rounds, to stay fresh.
  5. A skill edge (routes, grabs, timing) that a regular can feel.
- **Fails when:** a thin skill ceiling and few rounds (Fall Guys fell to about 13% of peak in 4 months); cheating; a licensed trend that runs out (Ink Game is at 3% of its peak, 79.2% liked).
- **Exemplars:** Fall Guys 172,026 `[SC]`, now 390 avg30, cautionary. Ink Game 9.5K now, 315K `[Rolimons]` peak `[RBX]`. Ultimate Chicken Horse 15,850 `[SC]`.
- **Targets:** session 10-20 min; D1 14%+; D7 4%+; first fun under 30 s.
- **Fit:** **Variant:** solo-viable only with bot racers that look and fail like people, plus a solo progression.
- **Flags:** needs-population, content-hungry.
- **Guide:** `categories/party-elimination.md`

### 12. Social roleplay and avatar · `social-roleplay-avatar`
- **Is:** an unstructured space (a town, a dressing room, a pet home) where the activity is improvised roleplay, dress-up or pet care with others.
- **Loop:** claim a house, outfit or pet → improvise with others → show off or vote → come back with friends.
- **Motivations:** Community, Design, Fantasy.
- **Must-haves:** instant identity (house, car, outfit); a large wardrobe or prop set; others as audience; premium property or item passes.
- **Fails when:** no goals, so retention depends on friends; moderation load; low spend per hour (Brookhaven is #3 most played but #62 earning).
- **Exemplars:** Brookhaven RP 260K / 657K, 89.0B visits `[RBX]`. Adopt Me! 183K / 287K `[RBX]`. Dress To Impress 43K / 177K `[RBX]`.
- **Targets:** session 20-40 min; D1 15%+; D7 5%+; first fun under 60 s.
- **Fit:** **No (solo, real-time skill).**
- **Flags:** needs-population, young-skew.

---

## C. Co-op first (a friend group is the content)

### 13. Friend-group co-op comedy · `friend-coop-comedy`
- **Is:** 2-4 friends with voice chat take on a job or a climb where clumsy physics, limited information and danger make the group funny ("friendslop").
- **Loop:** drop in together → scavenge, carry or climb → panic, laugh, fail → meet the quota or reach the top → next shift.
- **Motivations:** Community, Excitement, Discovery.
- **Must-haves:** proximity voice or friends in a call; a pressure loop (quota, stamina); clumsy physics or limited information that makes failure funny; cheap and short shifts.
- **Fails when:** played solo; without voice; a clone without the quota pressure (Content Warning 63,320 `[SC]`, 1.2% ret); no content after launch. Decay is fast: Lethal Company 1.1% ret, R.E.P.O. 5.7%, PEAK 8.2%. These sold well as paid games; on a free platform the same curve earns little.
- **Exemplars:** Lethal Company 239,369 `[SC]`. R.E.P.O. 266,908 `[SC]`. PEAK 169,910 `[SC]`. How to Fish 373,887 `[SC]`. Content Warning 63,320 `[SC]`, cautionary.
- **Targets:** session 20-40 min; D1 10%+; D7 2%+; first fun under 2 min.
- **Fit:** **No (solo).** Borrow its moments (quota pressure, rule-based monsters, fragile carries) for solo designs.
- **Flags:** needs-friends.

### 14. Co-op horde mission · `coop-horde-mission`
- **Is:** a small squad drops into a mission area, completes objectives against waves of enemies, and extracts, with class roles and loadouts.
- **Loop:** pick loadout → drop → objectives under swarms → call in tools → extract → upgrade → harder tier.
- **Motivations:** Community, Power, Excitement, Destruction.
- **Must-haves:**
  1. A signature verb nobody else has (stratagem codes, drilling through walls).
  2. Objectives that move the squad through the map, not a static defense.
  3. Swarms that read as a single threat, with a few named special enemies.
  4. Extraction under pressure as the climax.
  5. A solo mode with a helper (drone, bot squadmate) tuned so solo is fun, not just possible.
  6. Difficulty tiers and loadout unlocks.
- **Fails when:** no destructible or unique verb (samey Left 4 Dead-likes); solo is a lonely afterthought; friendly fire without comedy.
- **Exemplars:** Helldivers 2 458,208 `[SC]`. Deep Rock Galactic 53,558 `[SC]` (solo with the Bosco drone). Risk of Rain 2 74,945 `[SC]`, 22% ret (co-op layer). Left 4 Dead `[UNV]`. **Evidence gap:** no sourced Roblox exemplar.
- **Targets:** session 20-35 min; D1 14%+; D7 4%+; first fun under 60 s.
- **Fit:** **Variant:** solo with a helper drone or bot squad designed in from day one.
- **Flags:** needs-friends (unless the solo variant is built), content-hungry.
- **Guide:** `categories/coop-horde-mission.md`

---

## D. Run-based PvE (a run is the session)

### 15. Horde survivor · `horde-survivor`
- **Is:** you move, attacks fire automatically, and you pick upgrades every 20-40 s while the screen fills with enemies, for a 15-30 min run.
- **Loop:** move → collect XP → pick 1 of 3 upgrades → survive the next wave → discover a combination → die or win → meta-unlock → run again.
- **Motivations:** Power, Discovery, Excitement, Completion.
- **Must-haves:**
  1. One main verb (move), so the game is playable with one thumb.
  2. A pick-1-of-3 upgrade every 20-40 s.
  3. Discoverable combinations (evolutions, stacking) that are not shown up front.
  4. Visible absurd power by minute 10-15.
  5. A long unlock list between runs.
  6. Enemies and pickups readable on a phone even at peak density.
- **Fails when:** clones with no secrets or evolutions; 3D readability; visual noise on mobile; fast decay without new content (Megabonk 2.6% ret). Reskins of the 2D formula changed only the art.
- **Exemplars:** Vampire Survivors 77,061 `[SC]`. Megabonk 116,969 `[SC]`. Brotato 38,761 `[SC]`, 18.8% ret. Risk of Rain 2 74,945 `[SC]`, 22% ret.
- **Targets:** session 15-30 min; D1 16%+; D7 5%+; first fun under 60 s.
- **Fit:** **Yes.**
- **Flags:** none by default. The 2D top-down form is widely cloned; it needs a distinctive verb or space.
- **Guide:** `categories/horde-survivor.md`

### 16. Action roguelite · `action-roguelite`
- **Is:** responsive real-time combat through rooms, choosing a reward each room, dying, and returning to a hub that grows and talks back.
- **Loop:** clear a room → pick a boon → next room → boss → die → hub → story beat and meta-upgrade → run again.
- **Motivations:** Challenge, Power, Story, Discovery.
- **Must-haves:**
  1. Combat that is fun in a grey-box room: dash, attack and special with tight feel.
  2. A visible reward choice before each room or after each fight.
  3. Build synergies that change how you play within one run.
  4. Death advances something: story, hub, or a permanent unlock.
  5. A difficulty ladder (Heat-style modifiers) for veterans.
  6. Runs of 20-40 min with a mid-run checkpoint or boss.
- **Fails when:** repetition with no reason to go again; long runs; weak combat feel; roguelites with no story reason feel like grind.
- **Exemplars:** Hades 54,015 `[SC]`. Hades II 112,300 `[SC]`. Dead Cells 14,880 `[SC]`, 17% ret. Cult of the Lamb 56,262 `[SC]`.
- **Targets:** session 20-40 min; D1 16%+; D7 5%+; first fun under 60 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry if story is the reason to continue.
- **Guide:** `categories/action-roguelite.md`

### 17. Extraction raid · `extraction-raid`
- **Is:** bring gear into a dangerous area, grab loot, and get out alive; die and you lose what you carried.
- **Loop:** prepare loadout → enter → loot under threat → decide to push or leave → extract or lose it all → upgrade the stash or base.
- **Motivations:** Excitement, Power, Strategy, Completion.
- **Must-haves:**
  1. What you carry is at risk, and the player can see what they stand to lose.
  2. A push-or-leave decision every minute, with greed rewarded and punished.
  3. Tension that peaks at extraction (a timer, a noise meter, a final gauntlet).
  4. A persistent stash, hideout or base that the loot visibly improves.
  5. A PvE threat good enough that no other humans are needed.
- **Fails when:** pure PvP scares casual players; live-service bloat; late entry (Marathon fell under 4% by month five); a generic setting (The Day Before). Fantasy-dungeon extraction is crowded on Roblox `[UNV]`.
- **Exemplars:** Escape from Duckov 301,322 `[SC]` (solo PvE, top-down). ARC Raiders 481,966 `[SDB-press]`. Marathon 88,337 `[SDB-press]`, cautionary. Escape from Tarkov `[UNV]`.
- **Targets:** session 15-30 min; D1 15%+; D7 5%+; first fun under 60 s.
- **Fit:** **Variant:** the solo PvE form. PvP extraction is No (solo).
- **Flags:** needs-population for the PvP form.
- **Guide:** `categories/extraction-raid.md`

### 18. Room-depth horror run · `room-depth-horror-run`
- **Is:** push through procedurally ordered rooms toward a depth number, surviving entities that each have one tell and one counter-rule.
- **Loop:** open the next room → hear or see a tell → apply that entity's rule (hide, look away, stand still) → solve a light puzzle → reach the floor's end.
- **Motivations:** Excitement, Challenge, Discovery.
- **Must-haves:**
  1. A visible depth counter (door or room number) that is the progress bar.
  2. Each entity has a distinct audio tell and exactly one counter-rule, so fear turns into mastery.
  3. Procedural room order, so runs differ.
  4. The first entity encounter in about 2 minutes.
  5. Checkpoints or floors so a run fits in 20-40 min.
  6. Modifiers or a hard mode for veterans.
- **Fails when:** content burns out between floor drops (Pressure is at 529 off-peak, Grace at 452); jump scares with no counterplay; runs too long for mobile.
- **Exemplars:** DOORS 31K / 100K, 8.0B visits, 93.0% `[RBX]`. Pressure 529 off-peak, 0.49B visits `[RBX]`. The Mimic 8.4K `[RBX]`. Dandy's World 54K / 151K (hybrid with a character roster) `[RBX]`.
- **Targets:** session 20-40 min; D1 15%+; D7 4%+; first fun under 60 s (first tell under 2 min).
- **Fit:** **Yes** (DOORS is fully playable solo).
- **Flags:** content-hungry.
- **Guide:** `categories/room-depth-horror-run.md`

### 19. Chase-round survival · `chase-round-survival`
- **Is:** short rounds where something hunts or hits the whole server (nextbots, disasters), and you survive by movement.
- **Loop:** round starts → chased within seconds → move, juke, revive → survive or go down → currency → next round on a new map.
- **Motivations:** Excitement, Challenge, Community.
- **Must-haves:**
  1. A chase or threat within 10 s of the round starting.
  2. Rounds of 2-4 min on varied maps.
  3. A movement skill ceiling (bunny-hop, slide, emote-dash) that veterans show off.
  4. A low-cost way to help others (revive) that works with strangers.
  5. Cosmetics only; nothing bought makes you faster.
- **Fails when:** movement tech is too obscure for new players; map fatigue.
- **Exemplars:** Evade 45K / 82K, 9.4B visits, 93.9% `[RBX]`. Natural Disaster Survival 4.4K, 4.5B visits, created 2008 `[RBX]`. Tower of Hell 30K / 49K, a timed-course neighbor `[RBX]`.
- **Targets:** session 15-25 min; D1 16%+; D7 5%+; first fun under 15 s.
- **Fit:** **Yes**; strangers are a bonus, and the threat is AI.
- **Flags:** none.
- **Guide:** `categories/chase-round-survival.md`

### 20. Survival nights · `survival-nights`
- **Is:** gather and build by day, defend by night, and push a night counter or distance toward a long goal.
- **Loop:** day: gather, craft, feed the base → night: survive the threat → morning: count the night → stronger tools → next night.
- **Motivations:** Excitement, Power, Completion, Community.
- **Must-haves:**
  1. A day and night cycle with a clear switch from preparing to surviving.
  2. A base or safe radius that visibly grows (campfire level, train).
  3. A counter as the long goal (night 99, 80 km).
  4. Night threats that scale and have readable rules.
  5. Solo tuning: the solo night is beatable without a group.
- **Fails when:** the meta-loop runs out (Dead Rails is at 2% of peak); grind padding; solo too punishing.
- **Exemplars:** 99 Nights in the Forest 151K / 442K, 2.09M `[Rolimons]` peak `[RBX]`. Dead Rails 16.8K / 62K, 863K `[Rolimons]` peak, now 2% `[RBX]`. A Dusty Trip 9.7K `[RBX]`. Don't Starve Together 121,538 `[SC]`, 21.5% ret.
- **Targets:** session 20-40 min; D1 15%+; D7 4%+; first fun under 90 s (first night under 5 min).
- **Fit:** **Yes**, when solo tuning is designed in.
- **Flags:** open-world (often), vehicles (convoy variants).
- **Guide:** `categories/survival-nights.md`

### 21. Stealth heist · `stealth-heist`
- **Is:** infiltrate a hand-made space, reach an objective without being seen or with a planned loud fallback, and get out.
- **Loop:** scout → plan a route → move between cover, distract, disable → grab the objective → escape → score by stealth and time.
- **Motivations:** Strategy, Challenge, Fantasy, Discovery.
- **Must-haves:**
  1. Guards with readable vision and patrols, shown in the world, not on a minimap only.
  2. More than one way through each space.
  3. Tools or verbs that create openings (distract, disguise, hack a camera, throw a noise maker), each with a cost.
  4. Getting spotted escalates instead of instantly failing, so recovery is possible.
  5. An end-of-level rating that rewards clean play and invites a replay.
- **Fails when:** AI too dumb for stealth to matter; high content cost per map; tactical controls that fail on phones; trial-and-error with no way to read guards.
- **Exemplars:** Notoriety 1.7K `[RBX]`. ROB IT 1.8K `[RBX]`. Entry Point 61, Moderate label `[RBX]`. Payday 3 69,112 `[SC]`, now 867 avg30, cautionary. Hitman `[UNV]`.
- **Targets:** session 15-30 min; D1 14%+; D7 4%+; first fun under 90 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry.
- **Guide:** `categories/stealth-heist.md`

### 22. Menu strategy and card runs · `menu-strategy`
- **Is:** decisions made in menus, cards, grids or placement screens: deckbuilders, score-engine roguelites, tactics, auto battlers, tower defense, 4X and choice-driven narrative.
- **Loop:** read the state → choose a card, unit or option → watch it resolve → reward pick → next encounter.
- **Motivations:** Strategy, Discovery, Completion, Power.
- **Must-haves:** readable enemy intent or score target; pick 1 of 3 after each fight; synergies that can break the game; a difficulty ladder; daily seeded runs.
- **Fails when:** RNG with no counterplay; no telegraphing; flat synergies; on Roblox, menu play bounces action-seeking players `[analysis]`.
- **Exemplars:** Slay the Spire 2 574,638 `[SC]`. Balatro 43,825 `[SC]`, 16% ret. Mewgenics 115,063 `[SC]`. Tower Defense Simulator 10.7K, over-earner `[RBX]`. Anime Vanguards 13.6K, 96.7% `[RBX]`.
- **Targets:** session 20-40 min; D1 15%+; D7 5%+; first fun under 2 min.
- **Fit:** **No (real-time, non-menu).** Borrow pick-1-of-3, daily seeds and ascension for action games.
- **Flags:** none.

---

## E. Mastery course (the level is the opponent)

### 23. Precision course · `precision-course`
- **Is:** an authored course of jumps, timing and rhythm, where you die, respawn instantly and try again (platformers, obbies, rhythm platformers).
- **Loop:** attempt → fail → instant retry → clear the section → next stage.
- **Motivations:** Challenge, Completion, Competition.
- **Must-haves:**
  1. Respawn in under 1 s at a nearby checkpoint (or a deliberate no-checkpoint mode).
  2. Tight controls with invisible forgiveness (coyote time, input buffer).
  3. A visible stage number or progress bar.
  4. Each section teaches one idea, then twists it.
  5. Optional harder routes, collectibles or time trials for the skilled.
  6. A long tail: player-made levels, daily courses or leaderboards.
- **Fails when:** floaty controls; checkpoints in the wrong places; no new content; frustration that costs likes (Tower of Hell sits at 73.6%). Obby is the most crowded genre on Roblox.
- **Exemplars:** Celeste 7,720 `[SC]`, 24% ret. Geometry Dash 108,707 `[SC]`, 40.3% ret through player-made levels. Tower of Hell 30K / 49K, 29.3B visits, 73.6% `[RBX]`. Obby But You're On a Bike 597, 76.3% `[RBX]`.
- **Targets:** session 10-20 min; D1 18%+; D7 5%+; first fun under 10 s.
- **Fit:** **Yes.**
- **Flags:** young-skew (classic obby).
- **Guide:** `categories/precision-course.md`

### 24. Rage climb · `rage-climb`
- **Is:** a vertical climb with an awkward but precise control scheme, where one mistake can drop you far below.
- **Loop:** climb → misjudge → fall → feel it → climb again, better.
- **Motivations:** Challenge, Excitement, Competition.
- **Must-haves:**
  1. A single unusual movement verb (a hammer, a grapple, a chain) that is precise once learned.
  2. Loss of progress that is visible and dramatic, never random.
  3. Height shown at all times, plus personal best.
  4. Falls that are funny or spectacular to watch.
  5. Every fall is the player's fault on replay.
- **Fails when:** randomness causes falls; there is no depth after the summit; legal or asset disputes (Only Up! was delisted `[UNV]`).
- **Exemplars:** Getting Over It 4,959 `[SC]`. Chained Together 92,186 `[SC]` (co-op variant). Only Up! `[UNV]`, fetch failed. **Evidence gap:** no sourced Roblox exemplar.
- **Targets:** session 15-30 min; D1 14%+; D7 4%+; first fun under 30 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry once the one climb is solved.
- **Guide:** `categories/rage-climb.md`

### 25. Lane runner · `lane-runner`
- **Is:** auto-forward runs where you steer between lanes or gates, growing, shrinking or dodging, in 30-120 s levels.
- **Loop:** steer → pick a gate or dodge → watch the count or score change → end-of-run clash or finish line → upgrade → next level.
- **Motivations:** Power, Excitement, Completion.
- **Must-haves:**
  1. One-thumb steering, understood with no instructions.
  2. A choice every 2-4 s (which gate, which lane).
  3. A payoff moment at the end of each run (a clash, a multiplier, a big number).
  4. Levels of 30-120 s, so "one more" is easy.
  5. Upgrades that change the next run's opening choices.
- **Fails when:** the choices have an obvious best answer; numbers without spectacle; no reason to replay a level.
- **Exemplars:** DONT SPLASH 61K, launched Oct 2026, a runner-obby `[RBX]`. Count Masters and Mob Control `[UNV]` (mobile). Make an Army on Roblox, no sourced number. **Evidence gap:** thin sourced data.
- **Targets:** session 8-15 min; D1 14%+; D7 3%+; first fun under 10 s.
- **Fit:** **Yes.**
- **Flags:** young-skew.
- **Guide:** `categories/lane-runner.md`

### 26. Time-trial racing · `time-trial-racing`
- **Is:** race a vehicle or a fast body along a track against the clock, ghosts or other racers.
- **Loop:** start → drive the line → nail or miss corners → finish → compare to ghost → retry.
- **Motivations:** Challenge, Competition, Excitement.
- **Must-haves:**
  1. Handling that feels good on a straight and better in a corner (drift, boost, slipstream).
  2. A visible split time against your best or a ghost.
  3. Instant restart.
  4. Tracks short enough to learn (30-90 s laps).
  5. Async competition: ghosts and leaderboards, so solo is the main mode.
- **Fails when:** physics jitter under latency; handling that feels the same everywhere; too few tracks.
- **Exemplars:** Trackmania `[UNV]`. Mario Kart `[UNV]`. Roblox lists Racing as an official subgenre, with no sourced numbers. **Evidence gap:** no sourced exemplar in the research.
- **Targets:** session 10-20 min; D1 15%+; D7 4%+; first fun under 15 s.
- **Fit:** **Yes.**
- **Flags:** vehicles.
- **Guide:** `categories/time-trial-racing.md`

### 27. Physics and spatial puzzle · `physics-spatial-puzzle`
- **Is:** short levels solved by manipulating physics or space (drawing a shape, placing an object, bending a rule) in real time.
- **Loop:** see the problem → act on the world → watch physics resolve → succeed or tweak → next level.
- **Motivations:** Discovery, Challenge, Design.
- **Must-haves:**
  1. The problem is readable at a glance with no text.
  2. Multiple valid solutions, so the player's own idea works.
  3. Physics that is consistent, so failure teaches.
  4. Each level introduces or twists one idea.
  5. A replay reason: stars, efficiency scores, an endless or daily mode.
- **Fails when:** physics jitter makes a correct idea fail; one intended solution; level count runs out.
- **Exemplars:** Human Fall Flat 127,516 `[SC]` (physics puzzle levels, long sales tail via video creators). Brain It On and Save the Doge `[UNV]` (mobile draw-to-solve). Portal 2 `[UNV]`. **Evidence gap:** no sourced Roblox exemplar.
- **Targets:** session 10-20 min; D1 14%+; D7 3%+; first fun under 20 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry.
- **Guide:** `categories/physics-spatial-puzzle.md`

---

## F. Worlds, power and builds (a character or world that grows)

### 28. Metroidvania boss mastery · `metroidvania-boss-mastery`
- **Is:** explore an interconnected hand-made world where new movement abilities open old areas, punctuated by hard, readable bosses.
- **Loop:** explore → hit a locked path → find an ability → backtrack → boss → new region.
- **Motivations:** Discovery, Challenge, Fantasy.
- **Must-haves:**
  1. Movement and combat that feel good before any upgrade.
  2. Visible locks seen early and opened later ("I remember that ledge").
  3. Bosses with readable patterns and a fair punish window.
  4. A map and landmarks that prevent getting lost.
  5. Atmosphere and lore delivered through places, not text dumps.
- **Fails when:** getting lost; padding; backtracking that feels like chores; expensive to hand-author.
- **Exemplars:** Hollow Knight 95,428 `[SC]`. Hollow Knight: Silksong 587,150 `[SDB-press]`. Ori and the Will of the Wisps 31,224 `[SC]`. Nine Sols 6,493 `[SC]`.
- **Targets:** session 25-45 min; D1 18%+; D7 6%+; first fun under 60 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry; a large map can drift toward open-world.
- **Guide:** `categories/metroidvania-boss-mastery.md`

### 29. Boss-gated survival sandbox · `boss-gated-sandbox`
- **Is:** gather, build and craft in a large world, with each biome's boss unlocking the next tier.
- **Loop:** explore a biome → gather → craft better gear → summon the boss → new biome and materials.
- **Motivations:** Discovery, Design, Power, Completion.
- **Must-haves:**
  1. A clear next goal at all times ("what does the next boss drop?").
  2. Building as self-expression that persists.
  3. Each tier changes how you play (new tools, travel, threats), not just numbers.
  4. Atmosphere and lighting that make exploring worth it.
  5. Friends optional, and solo complete.
- **Fails when:** the late game runs out of content; grind with no boss to aim for; crowded on Roblox `[UNV]`.
- **Exemplars:** Valheim 498,478 `[SC]`, 18.2% ret. Terraria 486,918 `[SC]`. Enshrouded 160,361 `[SC]`, 19.0% ret. Subnautica 50,876 `[SC]` (solo, story-led). Palworld 2,101,535 `[SC]`, 2.0% ret, cautionary for a meme hook without depth. Project Zomboid 124,506 `[SC]`, 38.8% ret (permadeath simulation variant).
- **Targets:** session 30-60 min; D1 18%+; D7 6%+; first fun under 2 min.
- **Fit:** **Yes.**
- **Flags:** open-world, content-hungry.
- **Guide:** `categories/boss-gated-sandbox.md`

### 30. Base-raid survival with wipes · `base-raid-wipe`
- **Is:** start with nothing on a persistent server, build a base, raid others or be raided, and reset everything on a wipe schedule.
- **Loop:** gather → build → craft → raid or defend → wipe → start again.
- **Motivations:** Power, Competition, Community, Excitement.
- **Must-haves:** start from nothing; persistent loss through raids; social politics with strangers; scheduled wipes that reset the ladder.
- **Fails when:** no wipes, so clans entrench; PvE-only removes the drama; an early grind wall.
- **Exemplars:** Rust 259,646 `[SC]`, 31.7% ret. DayZ 78,739 `[SC]`, 42.6% ret. ARK: Survival Evolved 247,292 `[SC]`.
- **Targets:** session 40-90 min; D1 20%+; D7 8%+; first fun under 3 min.
- **Fit:** **No (solo).** Raids need people. An async or AI-raid version would be a different design.
- **Flags:** needs-population, open-world.

### 31. Hardcore build RPG · `hardcore-build-rpg`
- **Is:** a punishing action RPG with deep stat and talent builds, skill-based combat and permanent stakes (permadeath or lives).
- **Loop:** build a character → fight with parry and dodge → descend or progress → risk the character → theorycraft the next build.
- **Motivations:** Challenge, Strategy, Power, Fantasy.
- **Must-haves:**
  1. Real stakes: permadeath, lives or heavy loss, shown before the player risks it.
  2. Builds that change how combat plays, discussed on wikis.
  3. Skill-based combat with readable enemies.
  4. An onboarding path that keeps the brutality but teaches it.
  5. Layers or regions that gate progress.
- **Fails when:** brutal onboarding causes bounce; PvP griefing; a very small audience.
- **Exemplars:** Deepwoken 1.1K, 1.65B visits, over 60% of fans 17+ in 2021 `[RBX]`. Bloodlines about 9K Sunday, #5 top earner, paid access `[RBX]`. Rogue Lineage 285 `[RBX]`. Arcane Odyssey 315 `[RBX]`. Souls-likes on Steam `[UNV]`.
- **Targets:** session 30-60 min; D1 15%+; D7 6%+; first fun under 2 min.
- **Fit:** **Yes.**
- **Flags:** open-world (often), content-hungry.
- **Guide:** `categories/hardcore-build-rpg.md`

### 32. Grind ARPG · `grind-arpg`
- **Is:** level and grind toward power spikes (fruits, techniques, gear), fight bosses for drops, and roam a large world with PvP bounties.
- **Loop:** take a quest → grind enemies → level up → unlock a power → fight a boss → new region.
- **Motivations:** Power, Completion, Fantasy, Competition.
- **Must-haves:**
  1. A power spike that is visible and fun to use within the first session.
  2. Bosses with drops worth chasing.
  3. A large set of powers or builds to collect.
  4. A clear next goal on screen at all times.
  5. Optional PvP that does not punish players who avoid it.
- **Fails when:** grind fatigue; huge content cost; powers balanced so badly that PvP is one build.
- **Exemplars:** Blox Fruits 122K / 230K, 65.1B visits, 40%+ of users 17+ in 2021 `[RBX]`. Grand Piece Online 10.7K, over-earner `[RBX]`. Jujutsu Infinite 2.2K `[RBX]`. Shindo Life 1.6K `[RBX]`.
- **Targets:** session 30-60 min; D1 16%+; D7 5%+; first fun under 2 min.
- **Fit:** **Yes.**
- **Flags:** open-world, ip-risk, content-hungry.
- **Guide:** `categories/grind-arpg.md`

---

## G. Knowledge, observation and story (what you know is the progress)

### 33. Knowledge-loop mystery · `knowledge-loop-mystery`
- **Is:** a reset (a time loop, a death, a new day) that keeps only what the player has learned, in a hand-made world where every clue fits.
- **Loop:** explore → learn a fact or a schedule → reset → use the knowledge to get further → assemble the truth.
- **Motivations:** Discovery, Story, Challenge.
- **Must-haves:**
  1. Knowledge is the only progression, and the player can feel it (in Outer Wilds, "I know that tower drains its sand by minute 11").
  2. Resets are fast and cheap, so trying things costs nothing.
  3. A world on a fixed schedule that the player can learn and exploit.
  4. Clues that point to each other, so the player can reason, not guess.
  5. A reveal the player assembles themselves.
  6. A repeatable layer for after the solve: speed, fewest loops, a draft or variety generator.
- **Fails when:** no replay after the solve; spoilers spread; obscure puzzles; low concurrent players by nature (Outer Wilds peaked at 7,936).
- **Exemplars:** Outer Wilds 7,936 `[SC]`, 14.5% ret. Blue Prince 19,243 `[SC]` (adds a draft roguelite layer). Inscryption 17,044 `[SC]`. **Evidence gap:** time-loop games on Roblox are small `[UNV]`.
- **Targets:** session 25-45 min; D1 15%+ (driven by "I need to know"); D7 3%+ between chapters; first fun under 90 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry.
- **Guide:** `categories/knowledge-loop-mystery.md`

### 34. Anomaly and rules check · `anomaly-rules-check`
- **Is:** learn a baseline, then judge each new corridor, passenger or document against it: something is wrong, or nothing is.
- **Loop:** observe → judge (go on, turn back, approve, deny) → right moves you forward, wrong sends you back → new subtle variation.
- **Motivations:** Discovery, Challenge, Excitement.
- **Must-haves:**
  1. A baseline the player can learn in under a minute.
  2. Judgments made with the body (walk back, stamp, open the door), not a menu.
  3. Right and wrong outcomes that are fair on replay: the anomaly was really there.
  4. Escalating subtlety and new rules over time.
  5. A generator for the long tail (daily anomaly sets, player-made anomalies, leaderboards).
- **Fails when:** too short; anomalies run out; ambiguity reads as unfair; clone saturation and fast decay (the Roblox anomaly wave of 2026).
- **Exemplars:** The Exit 8 2,785 `[SC]` (sold far more than CCU suggests `[UNV]`). Papers, Please 6,038 `[SC]`. Animal Hospital (Anomaly) 31.5K live, 556K `[Rolimons]` peak `[RBX]`. Sell Fries! [Anomaly] 30.8K `[RBX]`. Airport Security (Anomaly) 3.7K `[RBX]`.
- **Targets:** session 10-25 min; D1 12%+; D7 3%+; first fun under 30 s.
- **Fit:** **Yes**, in the walk-through or hands-on form. A pure document-panel form is No (non-menu).
- **Flags:** content-hungry.
- **Guide:** `categories/anomaly-rules-check.md`

### 35. Evidence investigation · `evidence-investigation`
- **Is:** gather evidence with tools or by looking, then identify the culprit, ghost or cause, under pressure.
- **Loop:** enter the scene → use tools or examine → collect evidence → narrow the possibilities → commit to an answer → consequence.
- **Motivations:** Discovery, Challenge, Story, Excitement.
- **Must-haves:**
  1. Evidence is found by moving and looking in the world, not by reading a list.
  2. The answer can be reasoned from evidence the player saw, with no guess required.
  3. A pressure source while investigating (a hunt, a clock, a suspect leaving).
  4. Committing to an answer is a physical act with stakes.
  5. Variety per case (randomized culprit, ghost type or clue placement) so mastery is reading behavior, not memorizing.
- **Fails when:** a slow first few minutes; solved once the evidence table is memorized; needs friends; deduction moved into a notebook menu.
- **Exemplars:** Phasmophobia 112,241 `[SC]`, 9.2% ret (works solo). Demonology 3.5K `[RBX]`. Blair 436, Moderate `[RBX]`. Specter 99 `[RBX]`. Return of the Obra Dinn `[UNV]`.
- **Targets:** session 15-35 min; D1 14%+; D7 4%+; first fun under 90 s.
- **Fit:** **Variant:** solo, with deduction done in the world (pointing, walking up to, arranging) instead of a notebook screen.
- **Flags:** needs-friends in the co-op ghost-hunt form.
- **Guide:** `categories/evidence-investigation.md`

### 36. Mechanic-led story chapters · `mechanic-story-chapters`
- **Is:** a story game released in chapters, where one unusual verb drives every puzzle and the plot is discovered by using that verb.
- **Loop:** use the verb to get past a room → learn something about the world → the verb's rules deepen → chapter climax → wait for or play the next chapter.
- **Motivations:** Story, Discovery, Fantasy, Challenge.
- **Must-haves:**
  1. A verb that is fun as a toy in an empty room before any story exists.
  2. The first use of the verb within 10-30 s.
  3. Every puzzle has more than one solution through the verb.
  4. Story beats delivered by what the verb reveals (an enemy who remembers you spared them, a card that should not exist), not cutscenes.
  5. A twist the player discovers through the mechanic, planted in chapter 1.
  6. A replay or return layer: ratings, secrets, a chapter cadence the player can see.
- **Fails when:** the verb is a gimmick that stops changing after chapter 1; cutscenes carry the plot; the game is dead between chapters; the twist only works once and the mechanic is not enough on its own.
- **Exemplars:** Undertale 11,071 `[SC]` (spare mechanic carries the story). The Mimic 8.4K `[RBX]`. Piggy 4.5K now, 14.4B visits, chapter releases `[RBX]`. Inscryption 17,044 `[SC]` (a card game whose rules become the plot).
- **Targets:** session 25-45 min; D1 12%+; D7 3%+ between chapters, with spikes on chapter drops; first fun under 30 s.
- **Fit:** **Yes.**
- **Flags:** content-hungry.
- **Guide:** `categories/mechanic-story-chapters.md`

---

## H. Accumulate, routine and build (growth is the reward)

### 37. Job-sim empire · `job-sim-empire`
- **Is:** do a mundane job by hand, satisfyingly, then grow it into an empire with hiring and automation.
- **Loop:** do the job (stock, clean, mix, deliver) → get paid → expand or hire → automate the old job → take on a bigger one.
- **Motivations:** Completion, Power, Design, Fantasy.
- **Must-haves:**
  1. The hands-on job is satisfying as a toy (the beep of a scanner, the squeak of a clean surface).
  2. A first upgrade affordable inside 3 minutes that visibly changes the job.
  3. Pressure or stakes in the job (a quota, police heat, spreading mess), not just a meter.
  4. Automation that frees the player for a new, harder job.
  5. A themed fantasy with a moment people retell.
- **Fails when:** a grimmer, fiddlier execution (Drug Dealer Simulator next to Schedule I); a theme with no moment; a static mess with no pressure; Roblox tycoons already cover the plain version `[analysis]`.
- **Exemplars:** Schedule I 455,652 `[SC]`, the biggest solo-developer launch on Steam. Supermarket Simulator 51,353 `[SC]`. Clean the Library on Roblox peaked at 83,591 CCU `[press]`, beating the Steam original.
- **Targets:** session 15-30 min; D1 15%+; D7 4%+; first fun under 30 s.
- **Fit:** **Yes.**
- **Flags:** none.
- **Guide:** `categories/job-sim-empire.md`

### 38. Routine collection sim · `routine-collection-sim`
- **Is:** a daily routine (fish, farm, keep bees) that fills a collection, where things change while you are away and a small skill game sits inside the routine.
- **Loop:** do the routine → skill minigame → catch or harvest → log or sell → better tools → new area; come back tomorrow to a changed world.
- **Motivations:** Completion, Discovery, Power.
- **Must-haves:**
  1. A real-time skill moment inside the core action (the reel, the timing), not just a click.
  2. A collection log with visible gaps and rarity.
  3. Something that changes while the player is away.
  4. Timed events (weather, restocks) that create a reason to be online now.
  5. Tool upgrades that open new places, not just bigger numbers.
- **Fails when:** the core action has no skill; trends die in weeks (Grow a Garden is at about 1% of peak); very young audience; FOMO pressure older players resent.
- **Exemplars:** Fisch 46K / 103K, 431K `[Rolimons]` peak `[RBX]`. Bee Swarm Simulator 30K / 37.6K, 95.6% liked `[RBX]`. Grow a Garden 15K / 26.9K, 2.87M `[Rolimons]` peak `[RBX]`. Stardew Valley 236,614 `[SC]`, 21.5% ret.
- **Targets:** session 15-30 min; D1 18%+; D7 6%+; first fun under 20 s.
- **Fit:** **Variant:** only with a real-time skill game inside the routine (the Fisch form). Pure timer growth is No (real-time).
- **Flags:** young-skew.
- **Guide:** `categories/routine-collection-sim.md`

### 39. Incremental accumulate · `incremental-accumulate`
- **Is:** numbers grow (clicks, hatches, rolls, income, stolen units), with prestige resets, rarity reveals and offline income.
- **Loop:** earn → buy generators or rolls → earn faster → rebirth → earn faster again.
- **Motivations:** Completion, Power.
- **Must-haves:** exponential growth; prestige resets; rarity reveal animation; offline income; trading or stealing for social glue.
- **Fails when:** no decisions; power creep; paid-luck backlash; bot-inflated CCU (Banana 890,713 `[SC]` was widely reported as bot-inflated); trends that die in weeks.
- **Exemplars:** Pet Simulator 99 55K / 97K `[RBX]`. Sol's RNG 32K `[RBX]`. Steal a Brainrot 219K / 307K, 25.2-25.8M instantaneous record `[press]` `[RBX]`. Cookie Clicker 67,806 `[SC]`, 14% ret.
- **Targets:** session 10-60 min (often AFK); D1 15%+; D7 4%+; first fun under 10 s.
- **Fit:** **No (real-time skill, non-menu).** Use prestige or offline income as a layer only.
- **Flags:** young-skew, needs-population (steal variants).

### 40. Build and optimize · `build-and-optimize`
- **Is:** place and connect buildings or machines to grow output: tycoons, theme parks, factories, cities.
- **Loop:** place → connect → watch it run → find the bottleneck → expand.
- **Motivations:** Design, Strategy, Completion.
- **Must-haves:**
  1. Hand-work gives way to automation early.
  2. A bottleneck the player can see in the world (a pile-up, an idle machine).
  3. Each tier unlocks a bigger problem, not just bigger numbers.
  4. Watching your machine run is satisfying in itself.
  5. Building done in first or third person with the body, not only from a placement menu.
- **Fails when:** grind before automation; unreadable UI; poor performance at scale; a content wall once everything is built; precise layouts are hard on phones.
- **Exemplars:** Factorio 118,166 `[SC]`. Satisfactory 185,957 `[SC]` (first-person). Theme Park Tycoon 2 1.9K `[RBX]`. Lumber Tycoon 2 1.7K `[RBX]`. Restaurant Tycoon 3 5.7K `[RBX]`.
- **Targets:** session 25-60 min; D1 15%+; D7 5%+; first fun under 60 s.
- **Fit:** **Variant:** first- or third-person building in real time (the Satisfactory form). Top-down placement menus are No (non-menu).
- **Flags:** content-hungry.
- **Guide:** `categories/build-and-optimize.md`
