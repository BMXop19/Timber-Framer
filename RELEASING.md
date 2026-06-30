# Releasing

Timber·Framer ships as a single `index.html`. The in-app `CHANGELOG` array (near the
bottom of `index.html`) is the **single source of truth** for the version and history —
it powers the in-app changelog modal, and `CHANGELOG.md` is generated from it.

## Cutting a release

1. **Develop** in the experimental copy. Add a new entry at the top of the `CHANGELOG`
   array in `index.html` (bump the version, list the `{t: 'feat'|'change'|'fix', text}` notes).
2. **Cut the stable build** — copy the experimental `index.html`, rename the localStorage
   keys (`timberframer.exp.*` → `timberframer.*`), and flip the header badge to
   `· STABLE` (green). Save it as `lumber-framer-<ver>-stable/`.
3. **Copy** that stable `index.html` into this repo (overwrite `index.html`).
4. **Regenerate the repo docs** (keeps `CHANGELOG.md` + the README version in sync):
   - In the running app's console, run `copy(JSON.stringify(CHANGELOG))` and paste it into
     `scripts/changelog.json` (or download it there).
   - Run the generator:
     ```
     python scripts/gen_changelog.py
     ```
     This rewrites `CHANGELOG.md` and updates the `Current release: vX` line in `README.md`.
5. **Commit & push:**
   ```
   git add -A
   git commit -m "Release vX.Y"
   git push
   ```

## Notes

- Do **not** hand-edit `CHANGELOG.md` — it's overwritten by the generator. Edit the in-app
  `CHANGELOG` instead.
- `scripts/changelog.json` is the exported snapshot the generator reads; refresh it from the
  app each release so it matches the shipped `index.html`.
