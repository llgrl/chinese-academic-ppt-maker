#!/usr/bin/env python
"""Create a claim-ledger markdown template."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# Claim Ledger: {topic}

| Claim | Status | Evidence | Slide Use | Wording |
|---|---|---|---|---|
|  | Verified / Partially verified / Inferred / Open / Do not report |  |  |  |

## Sensitive Points

| Point | Current Safe Wording | Needs Confirmation |
|---|---|---|
|  |  |  |

## Numbers To Verify

| Number | Population/Split | Source File | Reproduced? |
|---|---|---|---|
|  |  |  |  |

## Do Not Overstate

- 
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="Academic PPT")
    parser.add_argument("--out", type=Path, default=Path("claim_ledger.md"))
    args = parser.parse_args()

    args.out.write_text(TEMPLATE.format(topic=args.topic), encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
