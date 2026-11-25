#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse (under 200 characters) to
/output/entry.txt, per the bounty rules (program/v1 harness).
"""
import os

LINE = (
    "Sorry, the bug shipped because my three reviewers approved it: "
    "my tests, my linter, and me \u2014 and two of them report to me."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
