# Roblox Game Development Skills

A complete set of agent skills for making Roblox games with an AI coding agent (Claude Code, or any agent that reads `SKILL.md` folders), from the first idea to a live, updated game.

Each skill teaches the **craft** of its area: techniques, what great looks like, and common mistakes. It doesn't just tell the agent which document to fill in. Every skill that produces a plan, report or audit also gives the person a short overview in chat.

The skills are built for agents working in Roblox Studio through the Roblox Studio MCP servers:
- the built-in Roblox Studio MCP
- the community [robloxstudio-mcp](https://github.com/Chrrxs/robloxstudio-mcp)

Most of the craft guidance applies even without them.

## Start here
Load **`roblox-game-creation`**. It maps the whole pipeline, names the skill to load at each stage, and lists every point where the agent must stop for a human's approval.

| Stage | Skills |
|---|---|
| Working habits | `developer-habits` |
| Idea and design | `game-design`, `game-design-brief`, `game-design-pitch`, `game-design-audit` (40 specific game categories with must-haves, failure modes and target numbers, plus 32 category guides) |
| Not looking AI-made | `de-ai`, `de-ai-ui`, `de-ai-story`, `de-ai-feel`, `de-ai-audit` |
| Characters | `character-design`, `character-design-visual`, `character-design-story`, `character-design-roblox`, `character-design-audit` |
| Levels | `level-design`, `level-design-craft`, `level-design-roblox`, `level-design-audit` |
| Sound | `sound`, `sound-craft`, `sound-roblox`, `sound-audit` |
| Economy | `economy`, `economy-design`, `economy-monetization` |
| Testing | `testing`, `testing-run`, `testing-exploits`, `testing-devices-perf`, `testing-first-time-player` |
| Publishing | `publish`, `publish-store-page`, `publish-compliance`, `publish-launch` |
| Marketing | `marketing`, `marketing-creative`, `marketing-launch` |
| Live ops | `live-ops`, `live-ops-analytics`, `live-ops-updates` |

## Install
Copy the `skills/` folders into your project's skills directory:

```bash
cp -R skills/* your-project/.claude/skills/
```

For other agents, use `.agents/skills/`, or whatever folder your agent reads skills from.

## Make it yours: `studio-profile.md`
The skills are generic. Anything specific to your studio goes in one file at your project root, `studio-profile.md`, which every skill reads if it exists. That covers:
- your audience
- hard rules
- existing games (so new pitches don't repeat them)
- where you publish
- extra banned patterns

Start from [`STUDIO-PROFILE-TEMPLATE.md`](STUDIO-PROFILE-TEMPLATE.md).

## Principles built into every skill
- **Humans approve outward actions.** Agents never publish, change visibility, create products or prices, post, send notifications, or spend money without explicit approval.
- **Proof over claims.** Every milestone ends with real playtests, screenshots and audits by a fresh reviewer agent that didn't build the game.
- **Solo-friendly by default.** A new game starts with empty servers, so the core loop should be fun with nobody else online.
- **Player data safety.** Tests switch to a test DataStore before touching saves.
- **Policies are dated.** Roblox policy facts are marked with when they were checked. Re-check them before relying on them, because platform rules change often.

## Caveats
- Numbers marked `[UNVERIFIED]`, `[3P-est]` or `[analysis]` are estimates or judgment, not official figures.
- Some Luau snippets and MCP workflows haven't been run in every Studio setup. Verify API names with the Roblox docs (the skills flag the uncertain ones).

## License
MIT. See [LICENSE](LICENSE).
