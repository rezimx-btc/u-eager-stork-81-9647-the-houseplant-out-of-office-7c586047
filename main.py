"""The Houseplant Out-of-Office -- make.fun one-liner entry.

Writes the chosen one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

LINE = (
    "My houseplant went on leave, force-pushed the watering schedule to "
    "never, and now the cactus is the only one still clocking in."
)


def main():
    # One sentence, one beat: the line must stay inside 90-153 bytes.
    size = len(LINE.encode("utf-8"))
    assert 90 <= size <= 153, f"line is {size} bytes, outside 90-153"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
