# <Game name>: audio credits and licenses

Copy this file to `design/<game>/CREDITS.md` (`design/<game>/` here means the game folder: the path set in `studio-profile.md`, or `design/<game>/` by default). Add a row **at the moment** an asset goes into the game (SR11), not at the end. Delete these instruction lines when the file is in use.

Rules (from `sound` and `sound-roblox`):
- Allowed sources, in order: Roblox Creator Store (Roblox and partner library), audio we own, CC0, royalty-free game licenses, CC BY (with credit), royalty-free no-attribution sites (with proof).
- Never: NC licenses, share-alike, YouTube Audio Library, BBC Sound Effects, personal-use packs, popular or ripped music, community uploads of unknown origin.
- Third-party files we upload stay private to our experiences and are never put on the Creator Store.
- License proof for every third-party source is saved in `design/<game>/licenses/`.
- Do not record account names, group IDs or universe IDs here if this file is shared publicly; keep them in `studio-profile.md`.

## 1. Asset log
| Asset ID | Name | Used for (event or area) | Source | Source URL | License | Attribution required? | Attribution text | License proof file | Uploaded by (owner) | Private? | Date added |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | Creator Store (Roblox / partner) | | Roblox library, on Roblox only | no | | n/a | n/a | n/a | |
| | | | Owned (made by / commissioned from) | | Owned / contract | per contract | | contract note | | yes | |
| | | | Freesound | | CC BY 4.0 | yes | "<Title>" by <author>, <URL>, CC BY 4.0 | licenses/<file> | | yes | |

## 2. In-game credits text
Every CC BY asset, and any asset whose license asks for credit, appears here and in `ReplicatedStorage/Credits` (SR12). Format: Title by Author, Source, License.

```
Music
  <Title> by <Author>, <Source>, <License>

Sound effects
  <Title> by <Author>, <Source>, <License>
```

## 3. Experience description credit line
A short line or link in the experience description, for example:
"Audio: <titles or 'see in-game Credits'> by <authors> (CC BY 4.0)."

## 4. Removed assets
| Asset ID | Name | Removed on | Why (license problem, replaced, cut) |
|---|---|---|---|
| | | | |
