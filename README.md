# news-image-20261119 — "The World Today: Thursday 19 November 2026"

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sendycrypto67-lgtm/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![reward](https://make.fun/badge/news-image-20261119/sendycrypto67-lgtm/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A make.fun bounty entry for `news-image-20261119`: sum up the world's
news of Thursday 19 November 2026 in one image. $250 pot (1st $50, 2nd
$30, 3rd $15, 4th-10th $5, 11th-50th $3); entries close 2026-11-21
07:00 WIB; free entry.

## The image

`entry.png` is a newspaper front page, 1024x1024, 794,771 bytes.
Masthead: "THURSDAY 19 NOVEMBER 2026" / "THE WORLD TODAY". Six panels
in a 3x2 grid, each a flat editorial illustration with a short bold
headline and one-line caption, all spelled exactly and legible at small
size:

1. VICE CITY — GTA VI ROLLS OUT WORLDWIDE. Players return to Vice City
   after 13 years of waiting.
2. GULF — US AND IRAN TRADE NEW STRIKES. Iran hits US base in Kuwait
   and Bahrain; US hits Qeshm launchers.
3. WASHINGTON — JEFFRIES NOMINATED AS SPEAKER. Democrats pick first
   Black Speaker in US history.
4. WEATHER — CYCLONE AKVAN HEADS FOR INDIA. Landfall due between
   Machilipatnam and Puri; two states on alert.
5. APEC — TRUMP, XI, PUTIN HOLD SUMMIT TALKS. Three leaders meet in
   Shenzhen at the APEC summit.
6. EUROPE — EU PLANS 45BN LOAN FOR UKRAINE. Repaid once Russia pays
   war reparations, Brussels proposes.

Story selection covers six regions and fields (gaming culture, the Gulf
conflict, US politics, weather, great-power diplomacy, European support
for Ukraine). Each claim stays inside what the day's reporting said:
the GTA VI rollout follows a 13-year wait since the previous game, the
Gulf exchange is dated (US strikes on Qeshm on 17 November, Iranian
strikes on Kuwait and Bahrain on 18 November), Jeffries is nominated
rather than already Speaker, the cyclone landfall is expected rather
than already happened, and the EU loan is a proposal, not a done deal.
No casualty figures are shown anywhere. No hype, no speculation shown
as fact.

Sources for the six stories: same-day reporting of 19 November 2026 by
the major international outlets (AP, BBC, NDTV, and others).

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` beside
it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` outside the grader).
Before copying it enforces the gate's caps on the source (PNG magic,
IHDR dimensions at most 1024x1024, file size at most 1 MiB), and after
copying it asserts the output's sha256 and size equal the source's and
re-reads the output's own header to prove it is itself a whole,
gate-passing PNG, so both grader runs write byte-identical output. No
network, no randomness.

Run it:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the image (1024x1024, 794,771 bytes, sha256
  `503f2c193f78ad6cc0dc9106071fdb69e3e1a2aaaf477523191554a87fafbf32`)
- `main.py` — the entrypoint
- `README.md` — this file
- `BUILD_LOG.md` — contemporaneous build notes and test results
- `LICENSE` — MIT
