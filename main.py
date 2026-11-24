"""One Line of Earned Pride — variant B: "Again."

Writes one line (a quiet, earned moment of pride: a night-shift
cleaner who taught herself to read, reading a bedtime story aloud to
her daughter for the first time) to /output/entry.txt and to entry.txt
in the repo root.

Deterministic: no network, no randomness, no time dependence.
Honours MAKEFUN_OUTPUT_DIR when set (a directory or a file path).
"""

import os

LINE = (
    "She spent three years sounding out the words on the spray bottles "
    "between night shifts, and tonight, still in her uniform, Rosa reads "
    "her daughter a bedtime story all the way to the last page — and her "
    "daughter whispers, 'Again.'"
)


def resolve_output_path() -> str:
    """Resolve the primary output file path.

    Honours MAKEFUN_OUTPUT_DIR when set (a directory or a file path);
    defaults to /output/entry.txt.
    """
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        if os.path.isdir(out) or out.endswith(os.sep):
            return os.path.join(out, "entry.txt")
        return out
    return "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    """Write text to path, creating parent directories as needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = LINE + "\n"

    # Primary output FIRST: /output/entry.txt, or MAKEFUN_OUTPUT_DIR
    # when set. This must succeed even when the repo dir is read-only.
    write_entry(resolve_output_path(), text)

    # Best-effort convenience copy next to this script (repo root).
    # The grader sandbox mounts /bot read-only, so this write may fail;
    # it must never crash the run.
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        write_entry(os.path.join(here, "entry.txt"), text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
