#!/usr/bin/env python3
"""Generate CHANGELOG.md (and refresh the README version) from the app's changelog.

The single source of truth is the in-app `CHANGELOG` array inside index.html (it powers
the in-app changelog modal). Export it from the running app and run this script:

    1. In the app, run:  copy(JSON.stringify(CHANGELOG))   (or download it)
    2. Save it as scripts/changelog.json
    3. python scripts/gen_changelog.py

This rewrites CHANGELOG.md and updates the "Current release: vX" line in README.md so the
repo always matches the shipped version. Do not hand-edit CHANGELOG.md.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "scripts" / "changelog.json"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"

# in-app note type -> Keep-a-Changelog style label
LABEL = {"feat": "Added", "change": "Changed", "fix": "Fixed"}


def main():
    entries = json.loads(DATA.read_text(encoding="utf-8"))
    if not entries:
        raise SystemExit("changelog.json is empty")
    latest = entries[0]["v"]

    out = [
        "# Changelog",
        "",
        "All notable changes to **Timber·Framer**, newest first.",
        "",
        "> Generated from the app's built-in changelog by "
        "[`scripts/gen_changelog.py`](scripts/gen_changelog.py) — do not edit by hand.",
        "",
    ]
    for e in entries:
        head = f"## [{e['v']}]"
        if e.get("date"):
            head += f" — {e['date']}"
        out.append(head)
        for n in e.get("notes", []):
            label = LABEL.get(n.get("t", ""), n.get("t", "").title() or "Note")
            out.append(f"- **{label}** — {n['text']}")
        out.append("")
    CHANGELOG.write_text("\n".join(out), encoding="utf-8")

    # keep the README's "Current release" marker in sync (if present)
    if README.exists():
        txt = README.read_text(encoding="utf-8")
        new = re.sub(r"Current release: v[0-9.]+", f"Current release: v{latest}", txt)
        if new != txt:
            README.write_text(new, encoding="utf-8")

    print(f"Generated CHANGELOG.md ({len(entries)} versions); latest v{latest}")


if __name__ == "__main__":
    main()
