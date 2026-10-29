---
name: publish-store-page
description: "Craft for a Roblox game's store page: the title, the 160-character hook, the description, the icon (legible at 150 px), image and video thumbnails, Roblox's built-in thumbnail A/B testing, localization of the name and hook, and search. Includes the 2026 specs and the rules that get a page's exposure reduced. Writes the store-page sections of STORE-PAGE.md. Use when drafting or refreshing any store page, icon or thumbnail (load publish first for the approval gate)."
---

# Store page

Load `publish` first for the approval gate. **Changing anything on a live page needs the user's OK for that change.** Drafting in `STORE-PAGE.md` and making images locally do not.

## Why the page matters
Home recommendations show the icon or thumbnail to a small group of players and measure the **play-through rate** (plays per impression). Then they measure whether those players stayed past the first 3 minutes. The page has two jobs that pull against each other:
- **Earn the click.** Stand out in a row of 20 tiles at phone size.
- **Tell the truth.** A player who clicks expecting something else leaves in under a minute. A first-play bounce is a negative signal that cuts distribution.

**A great page earns the click from exactly the players who will love the game.**

## How facts are marked
**Policy (official, checked 2026-10):** from Roblox Creator Hub docs (thumbnails, icons, descriptions, localization, discovery). Re-check before a decision; Roblox changes these often. Everything else is craft and design judgment.

---

## 1. Title
- **Short, sayable and searchable.** Two or three words a player can type after hearing a friend say it. Check that search for the exact name finds the game, and that no popular game already owns it.
- **Unique.** Near-copies of existing titles or images reduce exposure (Policy).
- **From the game's own world.** A name that only this game could have. Generic names ("Monster Escape", "Survival Game") read as AI-made and can't be searched. `de-ai-story` has naming rules if the project has it.
- **Keep it consistent** across updates, socials and trailers. Avoid repeated words. No published character limit was found in the docs; keep it short enough to show in full on a phone tile.
- **Update tags** ("[UPDATE]", "[CHAPTER 2]", a seasonal emoji) are common among top games. Use them sparingly, only while true, and remove them when stale.
- **Words in titles can trip moderation filters.** Check the name doesn't contain a filtered word or a real-world sensitive reference.

## 2. The hook and description
**Policy (official, checked 2026-10):** 1,000-character limit. **The first ~160 characters are the hook:** they show in search snippets and the collapsed mobile view. Roblox's description guidelines are labeled experimental. **Tags and hashtags are not used in ranking**; don't add them. Don't list controls; teach them in-game. Keep it appropriate for all ages. Emojis are fine in moderation. Roblox search is semantic: natural-language queries match intent, so write in plain words players would use.

### The hook (first 160 characters)
Say, immediately:
1. **What it is** (genre, in player words).
2. **The one thing no other game has.**
3. **The goal**, or what you do in the first minute.

Example structure (not real copy): "<Title> is a solo <genre> where you <unique action> to <goal>. <One concrete detail that makes it vivid>."

**Test:** a stranger reads only the hook and says what the game is. If they can't, rewrite.

### The rest
1. Optional: one short line about the latest update ("Chapter 2 is out: the flooded mill").
2. Main features as 3 to 5 bullets. Each a concrete thing the player does or sees, not an adjective. "Hide in lockers while the warden searches room by room" beats "Intense, immersive gameplay".
3. Extra info: devices supported, solo or with friends, a short FAQ.

### Rules that cut exposure (Policy, official, checked 2026-10)
- **Leading with giveaways or monetary rewards** ("free Robux", "win items") reduces exposure and shows a banner on the Creator Dashboard.
- **Metadata that doesn't match gameplay.**
- **Promotional claims** ("best game ever") are banned on video thumbnails; keep them off the page too.
- **Off-platform directions.** No "join our Discord" in the description or game. Links go only in the official social-link fields, which are shown only to age-checked users 16+.

### Voice
Write like the game's own world, not like a marketing template. Avoid the AI tells: "embark on an epic journey", "immersive", "unleash", rhetorical questions, triple adjectives. `de-ai-story` covers store descriptions specifically, if the project has it.

## 3. Icon
**Policy (official, checked 2026-10):** square, at least 512×512, one per locale. Shown as small as about 150×150.

**Craft:**
- **One subject, big.** A face, a creature, an object. It fills most of the frame.
- **Readable at 150 px.** Scale it down and look. Then look at it in a row of other icons. If the subject turns into mush, simplify.
- **Strong value contrast** between subject and background, so it reads in grayscale too.
- **Color matches the mood:** saturated for fantasy, muted for somber, high contrast for horror.
- **Text only if it reads at 150 px,** which usually means one short word or none.
- **Distinct from the genre's crowd.** Put it next to the top 10 icons in the same genre. If it could be one of them, change it.
- **From the real game.** A rendered character or object from the game, posed and lit for the shot. Never a style the game doesn't have.
- **Test variants.** Icons and thumbnails can be swapped without harming discovery (Policy). Make 2 or 3 and keep the best.

## 4. Image thumbnails
**Policy (official, checked 2026-10):**
- 16:9 at 1920×1080. Other ratios are stretched.
- JPG, GIF, PNG, TGA or BMP. Up to **10** images or videos.
- **Keep text and key elements away from the bottom edge;** player-count metadata covers it.
- **A default-only thumbnail makes the game ineligible for Home recommendation impressions.** Never launch with the default.

**Craft:**
- **At least 3 at launch,** each showing a different real moment: the core action, the setting, the threat or goal.
- **The first thumbnail is the pitch.** It must show the one thing no other game has.
- **Real gameplay or real in-game scenes,** composed and lit well. Showing features the game lacks causes bounces and breaks rules.
- **One focal point** per image. Clear silhouette, clear action.
- **Genre-signaling color and composition,** sharp and high resolution.
- **Unique.** Near-duplicates of other games' thumbnails reduce exposure.
- **No giveaway or money-led imagery.**
- **After each update, add a thumbnail showing the new content.**
- **Check at phone size.** Most impressions are on phones.

## 5. Video thumbnails
**Policy (official, checked 2026-10):**
- **3 uploads a month; rejected uploads count.** Each upload needs the user's OK.
- Not shown on Xbox, PlayStation or VR.
- **Allowed:** real gameplay, varied camera angles, mild color grading, logo overlays, in-game UI, music from the Roblox catalog.
- **Banned:** features the game lacks, enhanced graphics, real-world footage, voice-over or narration, music with lyrics, promotional or subjective claims ("best game!").

**Craft:** the first 2 seconds show the core action, not a logo. Cut on action. Keep it short. Reuse trailer shots from `marketing` only if they follow every rule above.

## 6. Thumbnail A/B testing (personalization)
**Policy (official, checked 2026-10):**
- Roblox's built-in test needs **at least 2 active thumbnails** (Home Page tab, Edit active thumbnails).
- It serves variants to random groups and shifts impressions to each segment's winner by play-through rate.
- Roblox reports +8.5% on average and up to +50% in its testing.
- Swapping thumbnails or icons doesn't harm discovery.

**Process:**
1. Make 3 to 5 thumbnails that test **different ideas**, not different crops of one idea: the threat, the hero, the setting, the core action.
2. Keep at least 2 active from launch.
3. Leave them alone until the next major update. Constant swapping just resets learning.
4. With each major update, add a variant showing the new content and drop the weakest.
5. Read play-through rate in Acquisition > Home Recommendations (`live-ops-analytics`). If it is below benchmark after a week of real traffic, the page is the problem, not the game.

## 7. Localization
**Policy (official, checked 2026-10):**
- Automatic translation covers the name, description and in-game text for players who turn it on, even if you do nothing.
- Manual translations override automatic ones.
- Set the source language (defaults to the creator's account language) and add supported languages. Translator collaborators can be added.
- **Turn off `AutoLocalize` on proper nouns** (character names, signage, the title in-world) so the machine doesn't mangle them.
- **Standout Games explicitly asks for localization** before nomination.

**Process:**
- Manually translate at least the **name, the 160-character hook and key UI strings** in the top languages for the audience. A reasonable default set (design judgment): Spanish, Portuguese (Brazil), Indonesian, German, French, Japanese, Korean.
- Decide per language whether the title is translated or kept. Keep it if it is a proper noun.
- Have each translated hook checked for tone, not just meaning.
- Editing live localization tables is a page change and needs the user's OK.

## 8. Genre
Genre is set with the page but has compliance rules (changeable only every 3 months). It lives in `publish-compliance`.

## Related skills
- `marketing-creative` covers thumbnails, icons and trailers from the marketing angle (what spreads off-platform). This skill owns the specs and what goes on the store page itself. Use both, and keep one set of files.
- `de-ai-ui` and `de-ai-story` (if the project has them) check that the images and words don't look or read AI-generated.

## What great looks like
- At phone size, in a row of competitors, the icon is the one you notice, and you can say what the game is.
- The hook passes the stranger test in one read.
- Every thumbnail shows something a player will actually do in their first session.
- Several thumbnails are active and testing distinct ideas.
- The page is translated by hand where it matters most.
- Nothing on the page looks or reads AI-generated.

## Common mistakes
- One thumbnail, or the default thumbnail.
- An icon full of detail that turns to noise at 150 px.
- Text along the bottom edge of a thumbnail, hidden by the player count.
- A hook that spends its 160 characters on the title and adjectives.
- Showing a boss fight or area the game doesn't have yet.
- Hashtags and keyword lists in the description.
- Swapping thumbnails every day.
- Spending a video upload on a clip with narration or a lyric track.

## Output
Fill these sections of `STORE-PAGE.md` (from `publish/STORE-PAGE-TEMPLATE.md`): Title, Hook, Description, Icon, Thumbnails, Video, A/B plan, Localization. Save image files beside it (for example `store/icon.png`, `store/thumb-1.png`) and list their paths. Show the title, the hook as it will appear, and the icon and lead thumbnail in the chat overview defined in `publish`.

## Sources
Roblox Creator Hub (read 2026-10-29): thumbnails, experience icons, descriptions, localization, discovery and discovery FAQ, Standout Games. All under `https://create.roblox.com/docs/`.
