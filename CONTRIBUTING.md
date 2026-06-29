# Contributing to Timber·Framer

Thanks for your interest! Timber·Framer is one self-contained `index.html` — no build tooling, no dependencies to install.

## Getting started

1. Clone the repo and open `index.html` in a browser. That's it — edit the file, refresh, done.
2. For local hosting (so reloads are clean), serve the folder with any static server, e.g. `python -m http.server` and open `http://localhost:8000/`.

## Where things live

It's a single file, organized top-to-bottom: constants & lumber tables → wall/corner/opening builders → roof (gable + shed) builders → the Three.js scene and render pipeline → the UI panel and event handlers → the cut-list / buy-list → the changelog. The whole frame is one `members[]` array; if you add a member type, give it a role, a color, and a legend label.

## Reporting bugs

Open an issue with:

- What you built (the **Export presets** JSON is the most reliable repro — attach it).
- What you expected vs. what happened, ideally with a screenshot.
- Browser and OS.

## Pull requests

- Keep changes focused and match the surrounding code style (it's terse and comment-dense on purpose).
- Bump the in-app `CHANGELOG` entry at the bottom of `index.html` with a short note.
- Remember the project's framing is **heuristic** — if you touch span/header/connection logic, keep the "not engineered, verify with a pro" guardrails intact.

## A note on accuracy

This tool helps people visualize and buy lumber; it does not replace engineering. Contributions that improve correctness (corner techniques, span tables, code rules) are especially welcome, but must preserve the disclaimers.
