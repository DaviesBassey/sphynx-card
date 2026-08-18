# Sphynx Motion — Digital Card

Davies Bassey A.'s digital business card. Dark cinematic design matched to sphynxmotion.com. The card is a shareable "linktree": its main QR opens the whole card on anyone's phone, with a tap-to-reveal contact QR, Save Contact, and all the links.

**Live card (installable):** https://daviesbassey.github.io/sphynx-card/
**Also on claude.ai:** https://claude.ai/code/artifact/bb5d0929-07be-4455-a618-a42ce4dbd7e7

## Two built files (run `build.py` to regenerate both)
- **`index.html`** — the installable PWA served by GitHub Pages. Add it to a phone's home screen and it opens full-screen like an app. Any push to `main` auto-republishes it. A service worker (`sw.js`) keeps the installed app current: it fetches the latest card whenever the phone is online (network-first) and falls back to the cached copy offline, so edits appear on next open with no re-adding.
- **`sphynx-card.html`** — the same card as one self-contained file (fonts, logo, photo, both QRs embedded). Works offline; this is the copy used for the claude.ai artifact.
- **`Davies-Bassey.vcf`** — contact file, with photo. AirDrop it or email it and the recipient's phone adds you in one tap.

## How the QRs work
- **Hero QR ("Scan to open my card")** → the live card URL above. Anyone who scans it gets this whole card on their own phone.
- **Contact QR** (inside Save Contact) → a vCard with name, phone, email, studio, website (no photo, so it scans easily). The `.vcf` file is the one that carries the photo.

## Folders
- **`assets/`** — pieces the build reads: `logo.png`, `headshot-original.jpg`, `avatar-cropped.jpg` (the circle), `qr-card.svg` (hero QR → the card URL), `qr-contact.svg` (vCard QR), `fonts-embedded.css` (Fraunces + Plus Jakarta Sans as data URIs).
- **`icons/`** — home-screen app icons generated from the logo (192, 512, maskable, apple-touch).
- **`reference/`** — copies of the site's own `home.html` / `site.css` + Google Fonts CSS, kept for re-matching the brand later.
- **`working/`** — render checks from the build. Safe to delete.

## Notes
- The line under the name reads **"Cinematic Motion · Brand Film"** — a placeholder from the studio's description, not a confirmed title. Change it in `build.py` (the `.role` line), re-run `python3 build.py`, then commit + push. Update `Davies-Bassey.vcf` (`TITLE:`) to match.
- The card page is public (needed so phones can open it without a login); `noindex` keeps it out of search results.
- Brand colours: ground `#08080A`, accent red `#E8181E`, text `#F0EDE8`.
