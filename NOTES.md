# NOTES — variant B: "Again."

## Final line (229 chars)
> She spent three years sounding out the words on the spray bottles between night shifts, and tonight, still in her uniform, Rosa reads her daughter a bedtime story all the way to the last page — and her daughter whispers, 'Again.'

## Concept
A night-shift cleaner who taught herself to read — by sounding out the
words on the spray bottles between shifts, over three years — reads a
bedtime story aloud to her daughter for the first time. The pride is
never stated: it arrives in the last word, when the daughter whispers
"Again." — the child's request is the proof the reading worked, and the
proof is the payoff. See VERSIONS.md for v1–v8.

## Why it fits the judge brief (criteria in order)
1. **Genuine earned pride, on subject:** a small person doing something
   hard — a cleaner teaching herself to read over three years, then
   reading aloud to her child. The effort is the whole first half of the
   line; the moment is the effort landing.
2. **Concrete scene, real person, seen happening:** Rosa, still in her
   work uniform after her shift, reading a bedtime story to her daughter
   to the last page. A named person, a specific place in time (tonight),
   an action unfolding — not a summary.
3. **Pride earned inside the line, never asserted:** the word "proud"
   never appears and nobody congratulates anyone. The effort is felt
   (three years, sounding out spray-bottle labels between night shifts)
   and the payoff is shown (the daughter asks for the story again).
4. **Lands in one read, by the last word:** the line is one sentence
   with a single turn — the em dash pivots from the reading to the
   daughter's whispered "Again.", which is the last word and the whole
   point.
5. **Freshness:** no trophy, podium or graduation. The learning material
   is cleaning-product labels; the proof of success is a child asking for
   the story again, not applause.

## Validation
- `python3 main.py` run twice (different MAKEFUN_OUTPUT_DIR temp dirs):
  both runs byte-identical, SHA-256
  `402d8d934f7065489efc78865e0be9527f8e7f031d3366a183305b9138ce9cb1`.
- Output: 229 chars (excluding trailing newline), 1 line, UTF-8,
  not only whitespace — gate 1–240 chars: PASS.
- Repo-root `entry.txt` identical to `/output/entry.txt` content: yes.
- Deterministic: no network, no randomness, no time dependence.
- LICENSE line 1: `SPDX-License-Identifier: MIT` — PASS.
- `.makefun/owner.json`: wallet `FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH` — PASS.
- README: 3 live make.fun badges for this slug, referral 8dxq9bq0,
  no `{owner}`/`{repo}` placeholders left, Run it section with
  `python3 main.py` — PASS.
- Grader simulation: copied dir to /tmp, made copy read-only
  (`chmod -R a-w`, repo-root `entry.txt` removed from the copy), ran as
  unprivileged user `nobody` with `MAKEFUN_OUTPUT_DIR` set — exit code 0,
  output written, no `entry.txt` appeared in the read-only copy
  (repo-root write failed silently as designed).
