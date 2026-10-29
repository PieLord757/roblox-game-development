---
name: marketing-creative
description: "The creative craft of marketing a Roblox game: what short clips spread and why, how to script and cut them, trailer craft with a two-cut shot list (on-platform video thumbnail and off-platform trailer), thumbnail and icon craft from a marketing angle, every asset spec, Roblox thumbnail personalization and how to test thumbnails, and how to build clip-worthy moments into the game. Use when making any trailer, clip, thumbnail, icon or ad creative. Loaded from the marketing router."
---

# Marketing: creative

Load `marketing` first if you haven't; it holds the approval rule, the spend gate and the policy facts. This skill is about making the assets. **Uploading or posting any of them needs the user's OK.** For the visual language of every image (palette, type, lighting, what reads as AI-made), load `de-ai-ui`. For every line of copy and caption, load `de-ai-story`.

Labels: **Policy (official)** is from Roblox docs; re-check the linked source before relying on it. **[3RD-PARTY]**, **[UNVERIFIED]** and **[SYNTHESIS]** as in the `marketing` router.

## 1. What clips spread

**The evidence [3RD-PARTY unless marked]:**
- **An official account amplifying a clip.** Dead Rails broke out after Roblox's own TikTok posted "Discover the dangers of the Dead Rails desert" (499K+ likes). Then big creators covered it.
- **A reveal that reads in about 15 seconds.** Grow a Garden's rare-mutation and rare-seed reveals were native to TikTok [UNVERIFIED analysis]; one count found 1.3M #growagarden videos.
- **Reactions to horror, and monsters people can name.** Doors spread through creator reactions and memes and theories about its entities. 99 Nights built its Deer as a mascot-face monster on purpose: scary, but readable at a glance.
- **Rivalry and live events.** The Grow a Garden vs Steal a Brainrot "Admin War" became its own wave of content.
- **Short-video consensus** [UNVERIFIED strategy blogs]: hook in the first second, no intro or greeting; volume beats polish (3 to 5 a week); #roblox plus the game's tag; clip real moments, don't stage "funny" ones.

**The clip types that work for story, horror and older audiences [SYNTHESIS]:**
1. **The scare.** A diegetic jumpscare or a monster appearing where the player didn't expect. Cut a beat before it, so the viewer is looking where the player was.
2. **The near-miss chase.** The door closes with the monster a step behind. Speed, sound and a clear escape.
3. **The "wait, WHAT" twist.** A spoiler-light story reveal: show the reaction and the first half-second of the reveal, not the answer.
4. **The monster reveal.** The signature creature's silhouette, sound and one behavior. Builds a name people repeat.
5. **The failure compilation.** Five deaths in 12 seconds, each to a different thing. Funny and a skill challenge.
6. **"This doesn't look like Roblox."** An atmosphere shot that sells the art direction. Works on older viewers; dies instantly if anything looks generic or AI-made.

### Writing a clip script (the craft)
Every clip has five parts, timed to the second:

| Part | Time | Rule |
|---|---|---|
| **Hook** | 0 to 1 s | Motion or a face in the first frame. The scare, the monster, the falling floor. Never a logo, a title card, a greeting or a slow pan |
| **Setup** | 1 to 4 s | One line of on-screen text that makes the viewer care: "Don't look at it when the lights go out." |
| **Payoff** | 4 to 12 s | The moment itself, uncut or in two or three cuts. Let the game's sound carry it |
| **Button** | last 1 to 2 s | A reaction, a freeze frame, or the line that makes people comment |
| **End card** | final 1 to 2 s | Game name and "Free on Roblox". Nothing else |

- **Length 9 to 20 s, vertical 9:16.** Shorter loops better. Make one horizontal 16:9 version for X or Reddit when that platform's rules allow.
- **Captions on,** in the game's type style, big enough to read on a phone at arm's length, kept out of the platform's UI zones (the bottom fifth and the right edge).
- **Sound on matters,** but the clip must still work muted: the text carries the setup.
- **Spoiler discipline.** Never show a chapter's ending or a twist's answer. Show the question.
- **Real gameplay only.** Capture from real playtests (`capture_screenshot`, recorded sessions). No staged animation that isn't in the game.
- **Write the caption and the first comment too.** A question ("what would you have done?") drives comments; comments drive reach.

### Build clip-worthy moments into the game [SYNTHESIS]
If the kit can't find five great moments, the game needs them. Hand these to the build as design notes:
- one **signature monster or mascot** per chapter, with a distinctive silhouette and sound;
- one **spectacle moment** per chapter (a collapse, a reveal, a chase set piece);
- one **"screenshot room"** per chapter, lit to be photographed;
- a **Moments capture prompt** (the Captures API) at that moment (Policy, official: Moments clips are 30 s, 13+, and viewers can jump straight into the game);
- an optional **photo mode or streamer camera** that hides the HUD.

## 2. Trailer craft

Make **two cuts** from one shot list [SYNTHESIS]. They have different rules.

### Cut A: on-platform video thumbnail (Policy, official rules)
- **15 to 30 s of real gameplay.**
- **No voice-over or narration, no music with lyrics,** no real-life footage, no enhanced graphics, no unreleased features, no ads, no subjective claims ("best game ever").
- Logos and sparse descriptive text are fine.
- **3 uploads a month, and rejections count.** Check every rule before uploading.
- Not shown on Xbox, PlayStation or VR, so the still thumbnails must stand on their own.
- Lead with the monster or set piece **in the first 2 seconds**; end on the logo.

### Cut B: off-platform trailer (YouTube, TikTok, X, Reddit)
- Voice-over and music are allowed, from the legal sources in SG1 (`sound`) and SR10 (`sound-roblox`) only; no copyrighted music. Roblox's licensed library is licensed for use on Roblox only, so it can't go in an off-platform trailer: use audio you own or a source whose license covers video use.
- **Structure:** cold open with a scare or twist (0 to 5 s), 3 or 4 beats of how it plays (chase, puzzle, atmosphere, the monster), the hook line, then the release date or "Play free on Roblox".
- 45 to 75 s for YouTube. **Vertical 9:16 cutdowns of 9 to 20 s** for short-video platforms, each one built around a single beat.

### Writing the shot list (the craft)
Each shot gets a row: number, cut (A, B or both), duration, what is on screen, camera, the in-game setup to capture it, sound, and on-screen text.
- **Start from the hook and work backwards.** Pick the single best moment first. Everything else exists to set it up or pay it off.
- **One idea per shot.** If a shot needs explaining, cut it.
- **Vary the rhythm:** slow dread, then a fast burst. Three fast shots in a row stop feeling fast.
- **Show the player's agency:** hands on the controls, a choice, a hiding spot. Viewers want to know what they would do.
- **Capture plan:** the place, the dev hook or config setting to stage it, the camera (the game's own camera or a capture camera), and the device. Capture at the highest settings that are still honest about what players see.
- **End-card frame** held for at least 1.5 s.

**What great looks like:** a stranger watching on mute with no context knows within 3 seconds what kind of game this is and what the threat is, and wants to try it.

## 3. Thumbnails and icon (marketing angle)

`de-ai-ui` owns how these look, and `publish-store-page` owns the store page as a whole (title, hook, description, localization). This section owns what the images must do to win clicks, and reuses the same specs; if the two ever disagree, re-check the Roblox docs linked below and fix the stale one.

### Asset specs (Policy, official)

| Asset | Spec |
|---|---|
| **Icon** | Square, **512 x 512 or larger**. Judged at **150 x 150**. One per locale. Mood colors (high contrast and dark suit horror) |
| **Thumbnails** | Up to **10** images or videos. **16:9, ideally 1920 x 1080**, under 3 MB for personalization uploads. jpg, png, gif, tga or bmp. **Keep text and key art out of the bottom strip,** where the player-count overlay sits |
| **Personalization** | Activate **2 to 5** thumbnails. Roblox serves each player segment its winner and keeps exploring |
| **Video thumbnail** | Rules in Cut A above. 3 uploads a month |
| **Ads creative** | Up to 10 thumbnails per campaign, 16:9 |
| **Event thumbnail** | One per event, unique |

A **custom thumbnail is required** for Home recommendation impressions (Policy, official).

### What makes a thumbnail get clicked (the craft)
- **One subject, one action, one question.** The monster in a doorway, a player half-hidden, a light about to go out. Not a collage.
- **Readable at phone size.** Check it at about 400 px wide. If the subject isn't clear, it fails.
- **A face or a silhouette** is the fastest read. The signature monster belongs on at least one thumbnail.
- **Real game art, real lighting.** Staged in the game, captured from the game. Official rules require real gameplay; it is also a promise you keep the moment the player joins.
- **Text: 0 to 4 words, or none.** Never "FREE", "UPDATE!!", Robux symbols or giveaway language (reward bait is not prioritized).
- **Contrast against the Roblox Home page,** which is mostly bright, saturated tiles. A dark, controlled image stands out there.
- **Each thumbnail tests a different idea,** not a different crop of the same idea: the monster, the place, the mystery, the player's fear.

### The icon
- It sits beside hundreds of others at 150 x 150. **One shape, one or two colors, readable in a glance.**
- The signature monster's face or silhouette, or one object that is the game's symbol.
- No text unless it is a single bold letterform. No tiny details.
- Test it by placing it in a screenshot of the real Home page among other icons, at real size.

### Testing thumbnails (Policy, official, and the craft)
- **Personalization is the A/B test.** Activate 2 to 5 thumbnails. Roblox reports an average **+8.5% qualified play-through rate**, with some games at **+50%**.
- Read the **Thumbnails** dashboard (or the Analytics Query API: `ThumbnailQualifiedPTR`, `ThumbnailImpressions`, `ThumbnailWinningSegments`) weekly in `live-ops-analytics`.
- **Add new thumbnails with each major update or chapter,** and keep old winners active. **Don't churn them between updates;** the system needs time to learn.
- Retire a thumbnail only after it has had real impressions and lost in every segment.
- A new thumbnail idea that wins is a clue for the next trailer and clips: it shows what the audience is clicking for.
- Uploading or activating thumbnails is a store-page change. **It needs the user's OK.**

## What great looks like
- Five clips that each hook in the first frame, each a different type, all from real play.
- A trailer whose first 2 seconds could be a clip by themselves.
- A thumbnail set where each image tests a different reason to click, and a winner emerges.
- An icon you can recognise at 150 px from across a room.
- Nothing that looks generic, glossy or AI-made.

**Common mistakes:**
- opening on a logo, a studio card or a slow establishing pan
- a video thumbnail with voice-over or lyrics (rejected, and it uses one of 3 monthly uploads)
- enhanced or rendered shots that the game can't match
- text in the bottom strip, under the player-count overlay
- five clips of the same type
- spoiling the twist in a clip
- an icon with fine detail that turns to mush at 150 px
- swapping thumbnails every few days, so no winner ever emerges
- copyrighted music in the off-platform trailer

## Output
1. The trailer shot list, the 5 clip scripts and the thumbnail and icon briefs, written into `LAUNCH-KIT.md` (template in `marketing-launch`).
2. Captured stills and clips in `design/<game>/marketing/<launch-or-chapter>/assets/` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default), named by kit item.
3. **A chat overview:** a table of the 5 clips (type, hook line, length, platform), the two trailer cuts with length, the thumbnail set (one line each on the idea it tests), and the icon idea. Send a contact sheet of stills and thumbnails (SendUserFile or the equivalent). List every upload or post waiting for the user's OK.

## Tools
- `solo_playtest`, `capture_screenshot`, `capture_device_matrix` (robloxstudio MCP): real footage and stills; check thumbnails and icons at phone size.
- `eval_client_runtime`: stage a moment (camera, lighting, monster position) through dev hooks for capture. Dev hooks must stay inert outside Studio (see `testing`).
- `de-ai-ui` for the look, `de-ai-story` for captions and lines, `de-ai-audit` before anything goes to the user.

## Sources
- Thumbnails: https://create.roblox.com/docs/production/publishing/thumbnails
- Experience icons: https://create.roblox.com/docs/production/publishing/experience-icons
- Discovery (custom thumbnail required, reward metadata): https://create.roblox.com/docs/discovery
- Moments: https://about.roblox.com/newsroom/2025/09/roblox-moments-user-generated-discovery
- Dead Rails analysis [3RD-PARTY]: https://www.gameanalytics.com/blog/dead-rails-and-the-hit-makers-formula
- Doors [3RD-PARTY]: https://www.pcgamesn.com/roblox/doors-horror-game
- 99 Nights creator spotlight: https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940
- Short-video strategy [UNVERIFIED]: https://blog.eklipse.gg/beginner-guide-2/roblox-youtube-shorts-strategy.html
