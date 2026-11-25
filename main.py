"""One-line roast for the make.fun bounty
u-suzy-one-line-one-laugh-roast-your-fridge-f1063521."""

import sys

MAX_CHARS = 200

ENTRY = "My fridge hums all night like it's plotting something, yet the only thing it ever chills is my hope of finding anything edible inside."


def validate_entry(text):
    """Check the entry against the bounty rules before printing it."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if "fridge" not in text.lower():
        raise ValueError("entry must be about the fridge")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return text


def main():
    """Validate the entry, print exactly it (no trailing newline), exit 0."""
    try:
        text = validate_entry(ENTRY)
    except ValueError as exc:
        sys.stderr.write("invalid entry: %s\n" % exc)
        return 1
    written = sys.stdout.write(text)
    sys.stdout.flush()
    if written != len(text):
        sys.stderr.write("output verification failed: wrote %d of %d chars\n"
                         % (written, len(text)))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
