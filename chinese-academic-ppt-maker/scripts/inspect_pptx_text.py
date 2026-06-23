#!/usr/bin/env python
"""Extract visible text from a PPTX using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def slide_key(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 10**9


def extract_text_from_xml(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    texts: list[str] = []
    for node in root.findall(".//a:t", NS):
        if node.text:
            texts.append(node.text)
    return texts


def extract_pptx(pptx: Path) -> list[dict]:
    rows: list[dict] = []
    with zipfile.ZipFile(pptx) as zf:
        slide_names = sorted(
            [n for n in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=slide_key,
        )
        for idx, name in enumerate(slide_names, start=1):
            texts = extract_text_from_xml(zf.read(name))
            rows.append(
                {
                    "slide": idx,
                    "file": name,
                    "text": "\n".join(texts).strip(),
                    "items": texts,
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    rows = extract_pptx(args.pptx)
    if args.json_out:
        args.json_out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        for row in rows:
            print(f"\n=== Slide {row['slide']} ===")
            print(row["text"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
