# BUILD_LOG — news-image-20261119

## 2026-11-19 ~07:14 WIB — brief

Parent task: build a make.fun entry for `news-image-20261119`, "Sum up
19 November's world news in one image". Facts supplied by the parent:
deadline 2026-11-21 07:00 WIB, free entry, $250 pot (1st $50, 2nd $30,
3rd $15, 4th-10th $5, 11th-50th $3). Gate: the entry is main.py (Python
3.13, stdlib only) in the repo root writing one image to
/output/entry.png; whole PNG, at most 1 MiB and 1024x1024; program runs
twice, both runs byte-identical; no network. New repo:
`~/workspace/makefun/entries/news-image-20261119/`, git init, branch
main, no commits yet. No files copied from any older entry; the 18
November entry was read only as a layout reference.

Six stories (facts supplied by the parent, my own headline and caption
wording): GTA VI global rollout and return to Vice City after a
13-year wait; US and Iran striking each other again (US hits Qeshm
launchers 17 Nov, Iran hits a US base in Kuwait and Bahrain again 18
Nov); Democrats nominating Hakeem Jeffries as Speaker, the first Black
Speaker; Cyclone Akvan due to make landfall on India's east coast
between Machilipatnam and Puri, Andhra Pradesh and Odisha on high
alert; Trump, Xi and Putin holding trilateral talks in Shenzhen at the
APEC summit; the EU proposing a 45 billion euro loan for Ukraine,
repaid once Russia pays reparations. No story was swapped during the
build. The two supplied alternates (Voyager 1 at one light-day, Jensen
Huang resigning) were not needed.

## 2026-11-19 ~07:15-07:20 WIB — six illustrations generated

Six flat editorial illustrations, one per story, generated with the
media image tools with "no text, no words, no letters" in every prompt
(4 in one round, 2 in the next, per the tool's 4-per-response limit).
Output: WEBP each, saved under assets/. Each was read back visually:
all six match their stories (neon Vice City boulevard at sunset;
missiles and explosions over a desert Gulf airbase with radar domes
and a warship; the US House chamber with rostrum, gavel and flags;
spiral cyclone off India's east coast; three leaders with US, China
and Russia flags before a Shenzhen skyline; EU round table with a
Europe map, Ukraine in gold, coins and a handshake) and none contains
any text, word, letter or number.

## 2026-11-19 ~07:20-07:22 WIB — compose, first pass

`compose.py` (build-time only, PIL) draws the front page on the proven
18 November pattern: masthead "THE WORLD TODAY" / "THURSDAY 19
NOVEMBER 2026", 3x2 grid, each panel a centre-cropped illustration
(321x250) above a red tag, bold headline and one-line sub-caption, all
text drawn with DejaVu so every letter is real and crisp. Font sizes
are adaptive from the start (headline tries 27 px down until it fits 2
lines, sub tries 16 px down until it fits 2 lines) and the script
asserts no overflow. First run succeeded outright: panel headlines
24-27 px, all subs 16 px, 1024x1024 PNG, 794,771 bytes, sha256
`503f2c193f78ad6cc0dc9106071fdb69e3e1a2aaaf477523191554a87fafbf32`.

## 2026-11-19 ~07:22 WIB — self-review of the final image

Read the composed image as an image. All six headlines and
sub-captions spelled exactly (GTA VI ROLLS OUT WORLDWIDE; US AND IRAN
TRADE NEW STRIKES; JEFFRIES NOMINATED AS SPEAKER; CYCLONE AKVAN HEADS
FOR INDIA; TRUMP, XI, PUTIN HOLD SUMMIT TALKS; EU PLANS 45BN LOAN FOR
UKRAINE), no garbled or cut-off text, no panel overflowing, every
illustration matching its caption. No defect found, so no recompose
was needed. This is the shipped image. Size margin is comfortable
(253,805 bytes under the 1 MiB cap).

## 2026-11-19 ~07:23-07:26 WIB — main.py and verification

Wrote `main.py` fresh (own wording, same proven behaviour as the 18
November entry): stdlib only, checks PNG magic / IHDR dims / size
before copying, copies entry.png to $MAKEFUN_OUTPUT_DIR (default
/output), asserts output sha256 and size equal the source's.
Second pass (a real improvement, not cosmetic): `_check_png` now
returns the image's (width, height), and `main()` re-checks the OUTPUT
file after copying: it re-reads the output's own PNG magic, IHDR
dimensions and size, and asserts the output's dimensions equal the
source's. Before, only the source was gate-checked and the output was
trusted on sha256 + size alone. A hash says the bytes match the source;
the re-read proves the file that actually lands in /output is itself a
whole, gate-passing PNG. Error messages name the file being checked.
Tests (after the second pass):
- `python3 -m py_compile main.py`: OK.
- Two runs to separate output dirs: `cmp` byte-identical; all three
  sha256 equal `503f2c19...` (source and both outputs). PASS.
- Output 1024x1024, 794,771 bytes, under 1 MiB. PASS.
- Negative test: a non-PNG file is rejected ("bad magic bytes"). PASS.
- Negative test: a 1200x1200 PNG is rejected ("over 1024x1024"). PASS.

## Cleanup

Build inputs removed from the repo after composing: assets/ (six WEBP
illustrations) and compose.py deleted; compose.py kept at
/tmp/news-image-20261119-compose.py for reference.

## Status

Entry built and tested in `~/workspace/makefun/entries/news-image-20261119/`:
`entry.png`, `main.py`, `README.md`, `LICENSE`, this `BUILD_LOG.md`.
NOT committed, NOT submitted, NOT bundled. Ready for the parent agent
to commit, bundle and submit before the 2026-11-21 07:00 WIB deadline.
