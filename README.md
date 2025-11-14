# Codebase Organization Documentation

## Overview

This is a personal Hugo-powered blog by Thibault Lebrun, deployed on GitHub Pages. The blog contains markdown articles
organized in a hierarchical category structure. The codebase uses the "Even" Hugo theme with custom layouts, SASS styling.

**Repository:** https://github.com/lebrunthibault/lebrunthibault.github.io  
**Website:** https://lebrunthibault.github.io/  
**Hugo Version:** 0.93.2 (Extended)

---

## Content Organization

### Content Structure

All blog content resides in `/content/post/` organized by category and subcategory.

Articles are organized in a hierarchical directory structure where each category can contain subcategories and markdown files.

### Frontmatter Structure

Posts use YAML frontmatter (delimited by `---`). Example:

```yaml
---
title: "Article Title"
draft: true
---
```

Supported Frontmatter Fields:
- `title` (string, required) - Post title
- `draft` (boolean, optional) - Hide draft posts in production builds
- `description` (string, optional) - Short description
- `keywords` (array, optional) - Keywords for search tagging
- `prod` (boolean, optional) - Custom flag for production status (used in homepage)

The archetypes/default.md template provides a minimal blueprint for new posts:
```yaml
---
title: "{{ replace .Name "-" " " | title }}"
draft: true
---
```

---

## Theme Configuration

### Theme: Even

The blog uses the **Even** theme, a clean and minimalist Hugo theme.

- **Source:** https://github.com/olOwOlo/hugo-theme-even
- **Installation:** Git submodule at `/themes/even/`
- **Theme Version:** Latest from git submodule

The theme provides:
- Base layouts and styling
- Default post/page templates
- i18n support (10+ languages)
- Archive, tag, and category pages
- RSS feed generation

### Theme Customizations

**Custom Layouts** (`/layouts/`):
- `/layouts/index.html` - Custom homepage with filtered post display
- `/layouts/partials/scripts.html` - Custom script includes
- `/layouts/partials/footer.html` - Custom footer
- `/layouts/post/` - Post-specific overrides (if any)
- `/layouts/shortcodes/code.html` - Custom code shortcode

**Custom SASS** (`/assets/sass/_custom/`):
- `_custom.scss` - Main custom styles (search widget positioning, post layout)
- `_accordion.scss` - Dropdown menu styles for nested content
- `_code.scss` - Code block styling
- `_dev_mode.scss` - Development mode styling

---

## Configuration Files

### config.toml

Main Hugo configuration with key settings:

**Key Features:**
- Git info enabled for last modification dates
- Chroma-based syntax highlighting with class output
- CDN-hosted jQuery and FancyBox for image galleries
- RSS feed generation enabled
- Safe HTML rendering in markdown allowed

---

## Build & Deployment

### Local Development

**Makefile** (`/Makefile`):

### Continuous Integration/Deployment

**GitHub Actions** (`.github/workflows/gh-pages.yml`):

**Deployment Flow:**
1. Push to `master` branch
2. GitHub Actions triggers build
3. Hugo builds static site to `/public`
4. Artifacts deployed to `build` branch (GitHub Pages source)
5. Site live at https://thibaultlebrun.dev/

---

## Static Assets Organization

### CSS

**`/static/css/prism.css`**
- Prism.js syntax highlighting theme
- Used for code block styling

**Custom SASS** (compiled to CSS):
- `/assets/sass/_custom/_custom.scss` - Main styles

### JavaScript

**`/static/js/prism.js`**
- Prism.js syntax highlighting library
- Client-side code highlighting for `<pre><code>` blocks

**Included via CDN** (in `/layouts/partials/scripts.html`):
- jQuery 3.2.1
- Slideout (mobile menu)
- FancyBox 3.1.20 (image lightbox)

## Special Features & Customizations

### Dev Mode

**Enabled by URL parameter or localStorage:**
- Query params: `?dev` or `?d`
- localStorage: `dev-mode` key
- When enabled:
  - Draft posts are shown
  - Homepage shows "dev" class on posts container
  - Search includes drafts

### Homepage Filtering

**Custom `/layouts/index.html`:**
- Filters posts by `hOiddenfromhomepage` param
- Only shows posts with `prod: true` frontmatter in default view
- Shows hidden posts in dev mode

### Table of Contents

- Auto-generated from headers
- Auto-collapse feature enabled
- Custom styling in SASS

### Code Highlighting

Dual system:
- **Server-side:** Chroma (Hugo) with class output
- **Client-side:** Prism.js as fallback
- FancyBox for image galleries
- Accordion dropdowns for nested code

### Syntax Highlighting Dependencies

- Uses Prism.js for client-side highlighting
- Prism CSS/JS loaded from `/static/`
- Line numbers enabled in Hugo config: `pygmentsOptions = "linenos=table"`

---

## 9. Key Dependencies & Technologies

### Build Tools
- **Hugo** v0.93.2 (Extended) - Static site generator
- **Node.js/npm** - Package manager

### Frontend Libraries (CDN)
- **jQuery** 3.2.1 - DOM manipulation
- **Slideout** 1.0.1 - Mobile menu
- **FancyBox** 3.1.20 - Image gallery/lightbox
- **Prism.js** - Syntax highlighting

### Themes & Templates
- **Even Theme** (git submodule) - Hugo theme base
- i18n support: English, French, Spanish, German, Russian, Japanese, Turkish, Chinese (CN/TW)

### Hosting & Deployment
- **GitHub Pages** - Static site hosting
- **GitHub Actions** - CI/CD automation

---

### Local Development

```bash
make dev  # Starts dev server with hot reload
```

## Key Customization Points

### To modify appearance:
- `/assets/sass/_custom/*.scss` - Custom styles
- `/layouts/partials/footer.html` - Footer content
- `config.toml` - Site metadata and theme parameters

### To add new functionality:
- `/layouts/shortcodes/` - Add custom shortcodes
- `/layouts/partials/` - Add template partials
- `config.toml` - Configure new parameters

### To change content structure:
- Create new directories in `/content/post/`
- Hugo automatically creates taxonomy pages

---

## SEO & Accessibility

- **Sitemap:** Auto-generated at `/sitemap.xml` with weekly change frequency
- **Robots.txt:** Auto-generated
- **Git commit history:** Used for accurate last-modified dates
- **Open Graph/Twitter Cards:** Support from Even theme
- **Emoji support:** Enabled in Hugo config
- **RSS feed:** Generated at `/index.xml`

---