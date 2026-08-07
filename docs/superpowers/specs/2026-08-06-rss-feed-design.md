# RSS Feed Feature Design

## Overview
Add an RSS feed to the ATBInsight website that outputs the 50 most recent articles, and expose a link to this feed in the site header.

## Architecture & Components

### 1. RSS Feed Generation
- **Plugin:** `mkdocs-rss-plugin`
- **Configuration (`zensical.toml`):**
  - Enable the `rss` plugin.
  - Set `length` to 50 to output only the 50 most recent articles.
  - Set `match_path` to target only the `blog/posts/.*` directory.
  - Define the output filename as `rss.xml`.

### 2. Header UI Integration
- **Theme Override:** Utilize MkDocs Material's theme override capability.
- **File:** `overrides/partials/header.html`
- **Implementation:** Extend the base Material `header.html` block. Inject an SVG RSS icon (e.g., `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M..."></svg>`) wrapped in an anchor tag linking to `/rss.xml`.
- **Placement:** The icon will be placed in the top-right header action area, next to the light/dark mode theme toggle.

## Data Flow
1. During the site build (`mkdocs build`), the `mkdocs-rss-plugin` scans `blog/posts/`, sorts the latest 50 markdown files by date, and generates `rss.xml` in the `site/` directory.
2. The user navigates to the site, clicks the RSS icon in the header, and is directed to `https://insight.aitobox.com/rss.xml`.

## Error Handling & Edge Cases
- **Empty Feed:** If there are no posts, the plugin handles creating an empty valid XML feed.
- **Missing Dates:** Articles must have valid date metadata in their Front Matter for the plugin to sort them correctly. Our ingestion pipeline already enforces this.
- **Icon Styling:** Ensure the injected RSS icon uses the existing Material header icon CSS classes (`md-header__button`, `md-icon`) so it inherits the correct color, size, and hover states.

## Testing
- Build the site locally and verify `site/rss.xml` is generated and contains the expected 50 items.
- Visually inspect the header in the local dev server to ensure the icon renders correctly in both desktop and mobile views, and in both light and dark modes.
- Verify the link successfully resolves to the generated XML feed.
