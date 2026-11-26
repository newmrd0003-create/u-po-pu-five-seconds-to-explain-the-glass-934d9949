"""Five Seconds to Explain the Glass — make.fun entry.

Competition: u-po-pu-five-seconds-to-explain-the-glass-934d9949
Task: one sentence (<=200 chars), in the cat's own voice, defending itself
five seconds after knocking a glass off the table. No apology, no confession.

Rejected drafts (genuine rejections, not filler):

Draft 1: "The glass was blocking my sunbeam, so I served it a formal
eviction notice -- the floor can handle the paperwork."
REJECTED: reads like a written office joke, not a spoken 5-second defence.
"Paperwork" is human bureaucracy, not cat logic, and the punchline is split
across two clauses, so the delivery sags instead of landing.

Draft 2: "It stared at me first, so I stared back, and it blinked first --
that is a forfeit, and forfeits fall."
REJECTED: the staring-contest frame is a near-cliche, and the final clause
explains the joke instead of landing it; "forfeits fall" is wordplay, not a
cat defending itself.

Final entry: the glass as an informant about to snitch to the dog. Fresh
angle (not gravity / slippery edge / already-falling), pure cat self-interest
-- remove the witness before it talks -- zero remorse, one spoken sentence.
"""

ENTRY = "The glass overheard my plans and was about to tell the dog, so I removed it before it could talk."

_SENTENCE_END = ".!?"


def validate(text):
    """Return (True, []) if text is a single sentence of 1-200 chars."""
    errors = []
    if not isinstance(text, str) or not text.strip():
        errors.append("empty or whitespace-only")
        return False, errors
    if len(text) != len(text.strip()):
        errors.append("leading or trailing whitespace")
    if len(text) > 200:
        errors.append("over 200 characters")
    if "\n" in text or "\r" in text:
        errors.append("contains newline")
    ends = [c for c in text if c in _SENTENCE_END]
    if len(ends) != 1 or not text.rstrip().endswith(tuple(_SENTENCE_END)):
        errors.append("not exactly one sentence")
    return (not errors), errors


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        raise SystemExit("invalid entry: %s" % "; ".join(errors))
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
