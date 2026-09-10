"""Pull the paper's real evaluation dataset (100 Question/Answer pairs, confirmed to match
the paper's Table 2 / supplementary examples verbatim) from the authors' own GitHub repo and
convert it into `data/eval_dataset.json`.

The authors publish Question/Answer pairs but no granular/global label per question -- only
four example questions are named in the supplementary material (two granular, two global).
This script tags only those four with a confirmed type; every other question is left
"unlabeled" rather than guessing, since a keyword heuristic tested against the real data
came back 97/3 against the paper's stated 70/30 split -- the split isn't recoverable from
question text alone. If you want the full granular/global breakdown from Fig. 2, you'll
need to label the remaining questions yourself -- edit the "type" field in the output file.

Usage:
    python -m scripts.fetch_eval_dataset
"""
import json
from pathlib import Path
from urllib.request import urlopen

SOURCE_URL = "https://raw.githubusercontent.com/FHL1998/MetalMind/main/evaluation_ground_truth.json"
OUTPUT_PATH = Path("data/eval_dataset.json")

# Confirmed by exact string match against the paper's supplementary information examples.
KNOWN_TYPES = {
    "What is the minimum argon cylinder pressure required before starting a build?": "granular",
    "What is the weight of an empty silo and what precautions should be taken during its removal?": "granular",
    "What is the complete process for setting up and starting a build?": "global",
    "How does the gas circuit and oxygen monitoring system work in the AM400?": "global",
}


def main():
    with urlopen(SOURCE_URL) as response:
        raw = json.loads(response.read())

    converted = [
        {
            "query": item["Question"],
            "ground_truth": item["Answer"],
            "type": KNOWN_TYPES.get(item["Question"], "unlabeled"),
        }
        for item in raw
    ]

    OUTPUT_PATH.write_text(json.dumps(converted, indent=2))
    labeled = sum(1 for c in converted if c["type"] != "unlabeled")
    print(f"Wrote {len(converted)} questions to {OUTPUT_PATH} ({labeled} with a confirmed type, "
          f"{len(converted) - labeled} unlabeled)")


if __name__ == "__main__":
    main()
