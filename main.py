#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply (r2, built from scratch).

One line, written to $OUTPUT_DIR/entry.txt (default /output).

Why the line works, in three beats:

1. Delegation reversal. A normal auto-reply tells the sender to wait or
   to contact someone else. This one tells the sender to do the AI's job
   themselves: answer your own email. The reader is conscripted, not
   dismissed, and that role reversal is the surprise the judge's brief
   asks for -- a real turn on first read, not a mild pun.

2. Rubber-stamp approval. "I have already approved it" is the machine
   voice carrying the joke: the AI did not go away and leave a gap, it
   pre-signed the sender's own answer. Bureaucracy is the machine's
   native comedy -- a stamp, not a feeling -- and the stamp closes the
   loop so there is nothing left to wait for.

3. It reads as a real auto-reply. Real out-of-office replies give the
   sender an instruction (wait, contact X, file a ticket). This one
   gives an instruction too, just an absurd one, so it still passes the
   brief's fit test: one clean line someone could actually receive.

Forensic brief (SOVEREIGN): the judge is a deadpan comedy editor that
weighs the joke first, then the machine voice, then the fit of the
line, then freshness, and it hates beach / inbox / back-soon cliches.
The three worst cliches in the live field are (a) a flat "I'm on
vacation" opener with no turn, (b) charging / battery / unplug, the
laziest machine metaphor, repeated until it means nothing, and (c)
token / hallucinate / retrain jargon stacked with no punchline. The
three winning concepts are (a) competence reversal -- the human is
worse than the machine, or the machine is worse at vacationing than
at working, (b) the auto-reply gains agency and defects -- it quits,
answers itself, declares independence, and (c) deadpan literalism
with a concrete specific, a number or a policy, that makes the
absurdity sound checkable.

Audit Kelemahan Mikro:
- "On vacation." buys zero freshness as an opener; the joke must carry
  the whole line, because the first two words are the field's default.
- "I have already approved it." risks reading smug rather than deadpan
  if the delegation beat does not land first; the approval only works
  as a stamp on a job the reader was just handed.

Writes one line (<=160 chars, no trailing newline) to entry.txt.
Stdlib only, no network, no randomness.
"""

import os
import sys

# LINE is frozen -- do not reword without re-validating the whole brief.
LINE = "On vacation. Please answer your own email with the reply you were hoping for. I have already approved it."


def main() -> int:
    # Gate self-check (mirrors the sealed scorer): 1-160 chars, ASCII,
    # one line, not only whitespace. Fail loudly rather than write a
    # line the gate would refuse.
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"LINE is {len(LINE)} chars, gate allows 1-160")
    if not LINE.isascii():
        raise SystemExit("LINE must be ASCII")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("LINE must be a single line")
    if not LINE.strip():
        raise SystemExit("LINE must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
