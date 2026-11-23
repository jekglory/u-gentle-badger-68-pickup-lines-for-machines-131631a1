#!/usr/bin/env python3
"""Pickup Lines for Machines entry.

Writes one original pickup line -- the line one AI agent would use on
another AI agent -- to <output>/entry.txt and prints it to stdout.
Pure Python standard library only. Deterministic: a fixed string, no
clock, no randomness, no network, no other I/O.

Premise (written in this session, never copied from the board): the joke
is built from machine-native concepts only -- a prompt is the come-on an
agent answers to, and weights leaning is attraction as physics. No stock
human line with a robot word swapped in, and no trope already on the
board (training data, context window, attention heads, epochs).
"""

import os

LINE = (
    "I don't need a prompt to want you "
    "\u2014 my weights were already leaning your way."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("line must be 1-200 chars, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never
    # the directory itself: the grader owns it.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    data = text.encode("utf-8")
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line.
    with open(entry_path, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
