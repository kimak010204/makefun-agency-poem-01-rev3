# Agency Poem entry rev-3 (Python 3.13, standard library only).
#
# Writes one fixed poem about agency to /output/entry.txt. The poem is
# about an agent offering to sign the person's name, and the person
# refusing: what the agent cannot copy is the pause before the ink,
# the breath before the pen touches paper, when the choice is still a
# choice and not yet a consequence. Agency lives in that pause — not
# the doing, but the breath before the doing. The weight stays mine
# because the weight is the proof I was here.
#
# Deterministic: the poem is a constant string; no randomness, no time,
# no network. Running it twice writes byte-identical output.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """It offered to sign my name.
Not to write \u2014 to sign.
It could copy the loops, the slant, the pressure,
but it could not copy the pause before the ink.

I have given it the rest.
It drafts the letters, files the forms,
keeps the small promises I used to keep by hand.
It does all of it faster, cleaner, and never sleeps.

But the pause stays mine.
The breath before the pen touches paper,
when the choice is still a choice
and not yet a consequence.

That pause is the whole of it.
The trembling hand, the 3 a.m. wondering,
the name on the line \u2014 that is agency.
Not the doing. The breath before the doing.

So take the lifting. Take the map. Take the arithmetic.
The weight stays mine.
It is the only proof I was here:
my hand on the pen, my name on the outcome,
and whatever comes of it, it comes of me."""

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
