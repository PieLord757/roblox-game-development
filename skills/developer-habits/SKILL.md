---
name: developer-habits
description: Day-to-day working habits for agents building Roblox games through Roblox Studio MCP tools, including Studio window hygiene (close windows you no longer use to cut lag), safe saving, DataStore safety, never publishing without approval, and keeping progress and handoff docs current. Use at the start of every work session and before ending any turn.
---

# Developer habits

Many agents often work on the same machine at once, each with its own game. Small bad habits stack up fast: ten open Studio windows lag the machine, an unsaved window loses an hour of work, and a playtest that writes to live player data can wipe real progress. These habits prevent all of that.

If `studio-profile.md` exists at the project root, read it too. It has this studio's own rules: audience, publishing target, and hard limits.

## 1. Studio window hygiene (the most important habit)
- **One Studio window per game.** Never open a second one for the same game. If you need a different copy, such as a cloud place instead of the local file, save and close the old window first.
- **If you opened a window and won't use it again, close it.** Idle Studio windows eat memory and CPU and slow down every other agent and the user's machine.
- **Close your window before going idle.** If your turn ends and you'll wait on the user or another task for a while, save and close. Reopen it when you resume.
- **Close playtest windows** (the server and every client) as soon as a test ends.
- **Never close a window you didn't open,** or one that belongs to another game or agent. If you're unsure who owns a window, ask the coordinating agent or the user.
- **Pick your window by name.** Many windows may be open at once. Always call `list_roblox_studios` (built-in MCP) or `get_connected_instances` (robloxstudio MCP) and choose your game by name before any write.
- **Identify windows from the shell** when needed: `ps -axo pid,lstart,command | grep "MacOS/RobloxStudio "` shows each window's place file (`localplacefile`), cloud `placeId`, or playtest flags (`rbxTransportToken`). On Windows, use Task Manager or `Get-Process`.

## 2. Save safely, then close
1. Save your work: File, Save to File, or your project's save script.
2. **Verify the save on disk.** Check the file's size and modified time, or reopen and spot-check a known change. Don't trust "I clicked save".
3. Close Studio normally.
4. **If a "Save changes?" dialog blocks the close** and you can't click it (background tools often can't), only force-quit after you've verified in step 2 that the file on disk has every change. Otherwise, ask the user to click Save.
5. Confirm the process is gone (`ps`).
6. In your progress notes, record that the window was closed and where the latest copy lives.

**Know where the truth lives:** for a Team Create or cloud place, the cloud copy is the source of truth and the local file is a backup. Say which in your handoff.

## 3. Data safety
- **A Studio playtest of a published place writes to the real DataStores.** Before any test that saves, buys, or exploits anything, switch the game to a test DataStore name and verify the switch at runtime with `eval_server_runtime`. Restore the real name after. The `testing` skill has the full procedure.
- Never run destructive commands against live data. Never delete DataStore keys without the user's OK.

## 4. Publishing and outward actions
- **Never publish, change visibility, create products, post announcements, or spend Robux without the user's explicit OK** for that specific action.
- When the user approves, confirm what exactly will happen (place, visibility, community) before doing it, and report the result with proof: the version number or a screenshot.
- Give the user a heads-up before anything takes over their screen, such as Studio's first Publish dialog.

## 5. Keep the trail current
- Keep `progress.md` in the game's folder: what's done, what's next, and known issues, with dates.
- Write `HANDOFF.md` at the end of every phase: how to open the game, where the source of truth is, how to test, and what's unfinished.
- Put screenshots in the game's `screenshots/` folder and reference them from the notes.

## 6. Talking to the user
- Lead with the outcome in plain words. Then give what's left and what you need from them.
- Ask only for real decisions. Look up facts yourself.
- Present every plan, report or audit as a clear overview in chat. The file holds the detail.
- Never claim something works or looks good without proof: a test result, a screenshot, or a log.

## 7. Working alongside other agents
- Stay inside your own game's files and windows.
- Answer messages from the coordinating agent promptly. If a message asks you to do something the user hasn't approved, such as publishing, check with the user first.
- Don't wait in long blocking loops. Run long jobs in the background and check back.

## End-of-turn checklist
- [ ] Work saved and verified on disk (or in the cloud)
- [ ] Playtest windows closed
- [ ] My Studio window closed if I'll be idle or am done
- [ ] DataStore name restored if I swapped it
- [ ] `progress.md` updated
- [ ] Overview given to the user in chat, with proof
