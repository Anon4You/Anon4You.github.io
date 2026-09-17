# Alienkrishn — personal portfolio

A lightweight, responsive portfolio for **Alienkrishn / Anon4You**. Built with HTML, CSS, and a small progressive-enhancement script. No build step, framework, or API keys.

## Preview locally

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Core content and navigation work without JavaScript.

## Run static checks

```sh
python test_site.py --deep
```

These dependency-free checks cover HTML nesting, local assets, internal links, CSS references, and basic project hygiene. They do not replace visual browser testing or JavaScript runtime testing.

## Publish with GitHub Pages

Push to the default branch, then select **Settings → Pages → Deploy from a branch**, choose that branch and **/ (root)**, and save. The intended URL is https://anon4you.github.io/. No deployment has been triggered by creating these files locally.

## Edit content

- `index.html`: biography, selected projects, verified public contact links, and page metadata.
- `style.css`: colors, layout, typography, and mobile/reduced-motion styles.
- `script.js`: opt-in GIF playback and static fallback; no tracking or analytics.
- `assets/`: favicon, a local still frame for the Tenor illustration, and a social-share cover image.

## References & media

Research references: [Brittany Chiang](https://brittanychiang.com/) (clear project descriptions), [Lee Robinson](https://leerob.io/) (content-first structure), and [Josh W. Comeau](https://www.joshwcomeau.com/) (restrained playfulness). Layout, styling, and implementation here are original.

The astronaut illustration is **“Izzeh Lost” by Blastonid on [Tenor](https://tenor.com/view/izzeh-lost-space-lost-in-space-pixel-gif-23225625)**. A first-frame preview is stored locally; clicking **Play GIF** requests the animated preview from Tenor’s CDN. Attribution is included on the page. Third-party media remains subject to its owner's rights and applicable Tenor terms; remove or replace it if necessary. Google Fonts supplies DM Sans and Space Grotesk with local system-font fallbacks.

Projects and contact links were checked against the public GitHub profile and repositories during development. Follower/star counts are intentionally omitted to avoid stale statistics. No personal email address or unverified employment claims are published.
