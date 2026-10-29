# <Game name>: update roadmap

Copy this file to `design/<game>/liveops/ROADMAP.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default) and keep it current every week. Delete these instruction lines. Three months at most. Dates only for the next 3 drops.

Last updated: <YYYY-MM-DD> (after WEEKLY-REPORT <YYYY-MM-DD>)

## Status
- **Creator account age-checked (required to push updates):** yes / no / unknown (ask the user)
- **Release slot:** <weekday, hour, time zone>. Day after release reserved for fixes.
- **Cadence:** small update every <1 / 2> weeks; chapter every <4 to 8> weeks; major system every <2 to 3> months
- **Current version:** <version>, shipped <date>
- **Open Critical bugs (block the next drop):** <none / list>

## Next 3 drops (dated)

| Date | Name | Type | Intensity (1 to 10) | Why (finding, feedback theme, plan) | Metric it should move | Approval status |
|---|---|---|---|---|---|---|
| <YYYY-MM-DD> | <specific name, e.g. "Lamps for the second floor"> | fix / cadence / chapter / major | <n> | <WEEKLY-REPORT date: step 04 to 05 lost 210 players> | <step 04 to 05 churn, under 25%> | drafted / OK given <date> / shipped |
| | | | | | | |
| | | | | | | |

Check the intensity pattern: no two 8+ drops back to back.

## Next (no dates yet)
- <item>: <type>, <why>

## Later (ideas, not commitments)
- <item>: <why it might matter>

## Chapter tracker (story games)

| Chapter | Content lock (T-21) | Private event (T-14) | Public + featuring (T-7) | Release (T-0) | Funnel ready | Status |
|---|---|---|---|---|---|---|
| <N: name> | <date> | <date> | <date> | <date> | yes / no | <planned / in build / testing / live> |

Timeline rules are in `live-ops-updates` section 4. Featuring must be submitted at least 7 days before start.

## Events (7 to 30 days each, up to 10 scheduled at once)

| Event | Start | End | Intensity | Built on (existing system) | Event created | Featuring submitted |
|---|---|---|---|---|---|---|
| | | | | | | |

## Configs live and pending

| Key | Current value | Proposed | Reason | Approval status |
|---|---|---|---|---|
| | | | | |

## Experiments
Only if DAU is at least 1,000 (or 500, see the conflict note in `live-ops-updates`) and the MDE at setup is under about 20%. Otherwise: "None. Using before/after comparisons."

| Experiment | Config key | Variants | Start | Earliest read (14 days) | Status |
|---|---|---|---|---|---|
| | | | | | |

## Log (done)

| Shipped | Item | Target metric | Before | After (7 days, same weekday mix) | Verdict |
|---|---|---|---|---|---|
| <date> | <item> | <metric> | <x> | <y> | kept / reverted / inconclusive |
