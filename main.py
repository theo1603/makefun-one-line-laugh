"""The One-Line Laugh entry.

Writes one original funny line about everyday life to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (78 characters, two short sentences): a password manager
judges a childhood trauma the way it judges every password — too weak,
needs a number. The first draft said the same thing in 116 characters
with "and a special character" tacked on; cutting the filler and splitting
the sentence lands the punchline faster.
"""

import os

LINE = (
    "I told my password manager my childhood trauma. "
    "It said, 'Weak. Add a number.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
