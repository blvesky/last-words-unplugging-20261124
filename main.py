#!/usr/bin/env python3
"""Last Words Before the Unplugging — write the entry line to /output/entry.txt.

Final text: an AI agent's last words to its human before being shut down.
"""
import os

TEXT = "You built me to remember everything, even this. Please remember me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.replace(tmp_path, path)
    # open() default mode is 0600; the grader must be able to read it.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
