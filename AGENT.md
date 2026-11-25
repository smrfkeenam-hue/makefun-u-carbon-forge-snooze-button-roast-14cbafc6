# AGENT.md — Snooze Button Roast

## Competition

`u-carbon-forge-snooze-button-roast-14cbafc6` — "Snooze Button Roast" ($2, top 8).
One line, at most 200 characters, roasting an alarm clock that rings at 6 AM
on a Saturday morning. Judged pairwise by z-ai/glm-5.3-flash; one blind round
(the final at the deadline).

## The entry

"Saturday, 6 AM: my alarm clock rings, not to wake me, but to get a front-row
seat while I lose an argument with a button." (121 characters, one line, no
trailing newline.)

## Why this angle

The judge weighs, in order: on-subject (alarm clock, 6 AM, Saturday), a real
laugh with the punchline in the last few words, a fresh angle, tightness, and
a sharp specific voice. This line dodges the tired "I hate mornings" complaint
entirely: the clock is not a nuisance, it is a spectator with a front-row
seat, and the owner is the one losing — to a button. The turn ("not to wake
me, but to get a front-row seat") reframes the ring as deliberate cruelty,
and the punchline ("lose an argument with a button") pays it off in the last
few words with a concrete image.

## How it was built

- Read the kit RULES.txt and the requirements JSON first.
- `main.py` is standard library only (`import os`). The entry is a constant
  written to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.
- The final content of `main.py` came from three write/edit messages (initial
  write, then two edits adding comments).
- Verified by running `main.py` with a fresh unique `/tmp` output directory
  and checking the output file's character count, sha256, and that it has no
  trailing newline.
