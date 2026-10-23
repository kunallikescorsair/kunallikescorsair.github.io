# Kunal's Data Lab — Personal Portfolio

A hand-crafted, static portfolio for Kunal Gurung. This repository contains the original approved visual design. It uses plain HTML, CSS and JavaScript: **no Bootstrap, purchased template, npm install or build step required**.

## Website

- Initial GitHub Pages address (after publication): **https://kunallikescorsair.github.io/**
- Planned custom domain: **kunalgurung.com.np** (not configured by this package)

## Files

- `index.html` — content, project cards and visual elements
- `assets/styles.css` — responsive illustrations, styling, motion preferences
- `assets/site.js` — accessible project filtering and copyright year
- `assets/favicon.svg` — original vector icon
- `.nojekyll` — instructs GitHub Pages to publish static files directly

## Local preview

```sh
python3 -m http.server 4321
```

Open http://localhost:4321. No Python backend is used by the actual website; Python only serves it during local development.

## Publish through GitHub Pages

1. On GitHub, create a new **public, empty** repository named `kunallikescorsair.github.io` under account `kunallikescorsair`. Do not initialise it with a README, licence or .gitignore.
2. From the unzipped project folder run:

   ```sh
   git init -b main
   git add .
   git commit -m "Publish Kunal's Data Lab portfolio"
   git remote add origin https://github.com/kunallikescorsair/kunallikescorsair.github.io.git
   git push -u origin main
   ```

3. Open repository **Settings → Pages**. Under **Build and deployment**, set **Source: Deploy from a branch**, **Branch: main**, **Folder: /(root)**; click **Save**.
4. Once deployment completes, visit `https://kunallikescorsair.github.io/` and review desktop/mobile behaviour.

**Keep the .np DNS and GitHub Pages custom-domain field unchanged until the temporary GitHub Pages site is verified.** Before switching nameservers, review any existing website/email DNS records and verify domain ownership. Do not copy a `CNAME` file into this project yet.

## Quality checks

```sh
node --check assets/site.js
python3 scripts/check_site.py
```

## Before public launch

- Verify the linked research preprint DOI and other external project links.
- Review public `job-hunter-au` repository for sensitive configuration, personal history and secrets before promoting it.
- Test the published site in mobile and desktop browsers. The graphical project thumbnails are intentionally illustrative rather than real project screenshots.
- Add a resume link only once an up-to-date resume file is available and approved for publication.

## Future updates

Edit the project files locally, commit, and `git push`. GitHub Pages publishes changes from `main`. Keep illustrations and CSS intact unless intentionally redesigning the site.
