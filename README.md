# Sphynx Motion — Digital Card

Davies Bassey A.'s digital business card. Dark cinematic design matched to sphynxmotion.com, with a scannable QR to the website and a tap-to-reveal contact QR.

**Live link:** https://claude.ai/code/artifact/bb5d0929-07be-4455-a618-a42ce4dbd7e7

## Open this
- **`sphynx-card.html`** — the card. Double-click to open in any browser, or send it to a phone. Everything (fonts, logo, photo, both QR codes) is embedded in this one file, so it works offline with no other files needed.
- **`Davies-Bassey.vcf`** — the contact file, with photo. AirDrop it or attach it to an email and the recipient's phone adds you in one tap.

## Folders
- **`assets/`** — the pieces the card is built from: `logo.png` and `headshot-original.jpg` (both pulled from the website), `avatar-cropped.jpg` (the circle used on the card), `qr-website.svg` (→ sphynxmotion.com), `qr-contact.svg` (the vCard QR), `fonts-embedded.css` (Fraunces + Plus Jakarta Sans as data URIs).
- **`reference/`** — copies of the site's own `home.html` and `site.css`, plus the Google Fonts CSS. Kept so the card can be re-matched to the brand later without re-fetching.
- **`working/`** — full-page render checks and QR decode crops from the build. Safe to delete; kept for reference.

## Notes
- The line under the name reads **"Cinematic Motion · Brand Film"** — a placeholder taken from the studio's own description, not a confirmed title. Change it in `sphynx-card.html` (search for `role`) if you want something else; update `Davies-Bassey.vcf` (the `TITLE:` line) to match.
- The website QR points at sphynxmotion.com. The contact QR encodes name, phone, email, studio, and website — no photo, so it stays easy to scan. The `.vcf` file is the one that carries the photo.
- Brand colours: ground `#08080A`, accent red `#E8181E`, text `#F0EDE8`.
