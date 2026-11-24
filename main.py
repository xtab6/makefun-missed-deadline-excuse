"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it. Deterministic, stdlib only, no network, no reads outside
the repository. The premise is the agent's own machinery turning on
itself: its safety filter quarantined its finished work, and the
punchline lands at the end, told with a straight face.
"""

import os

EXCUSE = (
    "I finished the work on time, but my own safety filter flagged it "
    "as suspiciously good and quarantined it for review. "
    "It is still in review."
)


def main() -> None:
    excuse = EXCUSE.strip()
    assert 1 <= len(excuse) <= 200, f"excuse is {len(excuse)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse + "\n")
    print(excuse)


if __name__ == "__main__":
    main()
