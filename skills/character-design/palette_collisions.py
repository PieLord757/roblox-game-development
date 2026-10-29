#!/usr/bin/env python3
"""Find colours that a studio's games share, or nearly share, and show house-style drift.

Each game is a folder under GAMES_DIR. The script reads every #RRGGBB in that folder's
ART-DIRECTION.md and CHARACTERS.md (when present). Lines containing the placeholder
#RRGGBB are ignored, so an unfilled template never pollutes the scan.

Usage:
  python3 -I palette_collisions.py GAMES_DIR                 # every pair of games
  python3 -I palette_collisions.py GAMES_DIR --target mygame # one game against the rest
Options:
  --threshold 10   CIE76 deltaE under which two colours count as a near match
                   (about 2.3 is barely visible; under 10 is clearly the same family)
  --min-chroma 12  skip colours with chroma below this (greys, near-black, cream) on
                   EITHER side, since every game needs a dark and a light. Use 0 to include them.
  --no-families    skip the colour-family summary

Output:
  1. Near-match pairs, sorted closest first: deltaE, game A, hex A, game B, hex B.
  2. A colour-family table: for each family (red, orange, brass/gold, oxblood, cream,
     near-black, ...), which games use it. A family used by most games is house-style drift.
The output is evidence for NOTES. Nothing here fails a character on its own.
Standard library only.
"""
import argparse
import glob
import itertools
import math
import os
import re
import sys

HEX = re.compile(r'#[0-9A-Fa-f]{6}\b')
FILES = ('ART-DIRECTION.md', 'CHARACTERS.md')


def lab(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: ((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92
    r, g, b = f(r), f(g), f(b)
    X = (r * .4124 + g * .3576 + b * .1805) / .95047
    Y = r * .2126 + g * .7152 + b * .0722
    Z = (r * .0193 + g * .1192 + b * .9505) / 1.08883
    t = lambda v: v ** (1 / 3) if v > 0.008856 else 7.787 * v + 16 / 116
    return 116 * t(Y) - 16, 500 * (t(X) - t(Y)), 200 * (t(Y) - t(Z))


def lch(h):
    L, a, b = lab(h)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def family(h):
    """Rough, readable colour family. Tuned for spotting house styles, not for colour science."""
    L, C, H = lch(h)
    if C < 12:
        if L < 25:
            return 'near-black'
        if L > 80:
            return 'cream/paper' if C >= 4 and 40 <= H < 110 else 'off-white'
        return 'grey'
    if C < 30 and L > 75 and 40 <= H < 110:
        return 'cream/paper'
    if H < 20 or H >= 345:
        return 'oxblood/maroon' if L < 35 else ('pink/magenta' if H >= 345 else 'red (hue 345-20)')
    if H < 45:
        return 'oxblood/maroon' if L < 35 else 'red (hue 20-45)'
    if H < 70:
        return 'brown' if L < 45 else 'orange/amber'
    if H < 100:
        return 'brown/olive' if L < 45 else 'brass/gold/yellow'
    if H < 160:
        return 'green'
    if H < 215:
        return 'teal/cyan'
    if H < 290:
        return 'blue'
    return 'purple/violet'


def load(games_dir):
    palettes = {}
    for d in sorted(glob.glob(os.path.join(games_dir, '*', ''))):
        hexes = set()
        for name in FILES:
            p = os.path.join(d, name)
            if not os.path.isfile(p):
                continue
            with open(p, encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    if '#RRGGBB' in line:
                        continue
                    hexes.update(h.upper() for h in HEX.findall(line))
        if hexes:
            palettes[os.path.basename(os.path.normpath(d))] = sorted(hexes)
    return palettes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('games_dir')
    ap.add_argument('--target', help='compare only this game folder against the others')
    ap.add_argument('--threshold', type=float, default=10.0)
    ap.add_argument('--min-chroma', type=float, default=12.0)
    ap.add_argument('--no-families', action='store_true')
    a = ap.parse_args()

    P = load(a.games_dir)
    if not P:
        sys.exit(f'No ART-DIRECTION.md or CHARACTERS.md with hex colours found under {a.games_dir}')
    if a.target and a.target not in P:
        sys.exit(f'Target "{a.target}" not found or has no colours. Games found: {", ".join(P)}')

    pairs = [(x, y) for x, y in itertools.combinations(P, 2) if not a.target or a.target in (x, y)]
    hits = []
    for g1, g2 in pairs:
        if a.target and g2 == a.target:
            g1, g2 = g2, g1
        for x in P[g1]:
            lx, cx = lab(x), lch(x)[1]
            if cx < a.min_chroma:
                continue
            for y in P[g2]:
                if lch(y)[1] < a.min_chroma:
                    continue
                d = math.dist(lx, lab(y))
                if d < a.threshold:
                    hits.append((round(d, 1), g1, x, g2, y))

    scope = f'{a.target} vs {len(P) - 1} other games' if a.target else f'all pairs across {len(P)} games'
    print(f'## Near matches (deltaE < {a.threshold}, chroma >= {a.min_chroma}), {scope}')
    for h in sorted(hits):
        print(f'{h[0]:>5}  {h[1]} {h[2]}  ~  {h[3]} {h[4]}')
    print(f'{len(hits)} pairs')

    if not a.no_families:
        fam = {}
        for g, hexes in P.items():
            for h in hexes:
                fam.setdefault(family(h), set()).add(g)
        n = len(P)
        print(f'\n## Colour families ({n} games). Families used by more than half the games are house-style drift.')
        for f_, games in sorted(fam.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            mark = '  <-- house style' if len(games) > n / 2 and n > 2 else ''
            tgt = ''
            if a.target:
                tgt = '  [target uses it]' if a.target in games else ''
            print(f'{len(games):>3}/{n}  {f_:<20}{tgt}{mark}')


if __name__ == '__main__':
    main()
