# Huzaifa’s Print Journal

A small, photo-first journal of real 3D prints, their quality, lessons learned, and the next experiment. Static HTML/CSS/JavaScript; no database, analytics, remote fonts, dependencies or printer connection.

## Update the journal

1. Add an entry to `prints.json`, newest first. Use an ISO date and stable unique ID. Keep exactly three notes: Quality, Learned, Next time. Credit the model designer; distinguish original designs from downloaded models.
2. Add reviewed, web-sized photo copies to `docs/images/`. Orient correctly and remove all embedded metadata before publishing. Keep originals outside this repository. Do not retouch defects away: the journal records real results.
3. Label mass/time as measured, slicer estimates, or owner estimates. Never invent unknown settings or treat planned prints as completed.
4. Run `python3 build.py` and preview the `docs` directory with a local HTTP server. Check phone and desktop layouts, photo selection, zoom, keyboard navigation and image descriptions.
5. Review the exact staged files before committing and pushing. GitHub Pages publishes only `/docs` from `main`.

The initial photo copies were produced with ImageMagick auto-orientation, a maximum size of 1280 pixels, metadata stripping and JPEG quality 86. Original photos were left untouched.

## Privacy boundary

This is a **separate public repository**, not a public copy of the local printing workspace. Never add parent folders, printer configuration, credentials, serial numbers, IP addresses, logs, videos, cloud backup links or private notes. Only reviewed journal text and photographs belong here. Check photo backgrounds as well as metadata. Future gift details or recipient photos need a privacy review before publication.

## Photo and model credits

Photos document Huzaifa’s own prints. No permission to reuse these photos is granted by publishing them here. Model authors retain their own rights. The journal does not redistribute the model files. Initial entries credit Creative Tools (3DBenchy) and JernejP. (bed scraper).
