#!/usr/bin/env python3
"""Strip noisy fields (e.g. url, urldate) from a Zotero-exported .bib file.

Usage:
    python clean_bib.py input.bib [output.bib] [--fields url,urldate,note,file,abstract,keywords]

If output.bib is omitted, input.bib is overwritten in place.
Assumes one BibTeX field per physical line (Zotero's "Better BibTeX" export format).
"""
import re
import sys

DEFAULT_FIELDS = ["url", "urldate"]


def clean_bib(text: str, fields: list[str]) -> str:
    field_pattern = re.compile(
        r"^\s*(" + "|".join(re.escape(f) for f in fields) + r")\s*=", re.IGNORECASE
    )
    return "\n".join(line for line in text.splitlines() if not field_pattern.match(line))


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    field_arg = next((a for a in sys.argv[1:] if a.startswith("--fields")), None)
    fields = field_arg.split("=", 1)[1].split(",") if field_arg else DEFAULT_FIELDS

    if not args:
        print(__doc__)
        sys.exit(1)

    input_path = args[0]
    output_path = args[1] if len(args) > 1 else input_path

    with open(input_path, encoding="utf-8") as f:
        text = f.read()

    cleaned = clean_bib(text, fields)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Removed fields {fields} -> {output_path}")


if __name__ == "__main__":
    main()
