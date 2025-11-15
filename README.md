# Codebase Organization Documentation

## Overview

This is a personal Hugo-powered blog by Thibault Lebrun deployed on Netlify. The blog contains markdown articles
organized in a hierarchical category structure. The codebase uses TailwindCSS for styling.

**Repository:** https://github.com/lebrunthibault/lebrunthibault.github.io  
**Website:** https://thibaultlebrun.dev/  
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

---

## Theme Configuration

### Theme Customizations

**Custom Layouts** (`/layouts/`):
- `/layouts/index.html` - Custom homepage with filtered post display
- `/layouts/partials/scripts.html` - Custom script includes
- `/layouts/partials/footer.html` - Custom footer
- `/layouts/post/` - Post-specific overrides (if any)
- `/layouts/shortcodes/code.html` - Custom code shortcode

---

## Build & Deployment

### Local Development

**Makefile** (`/Makefile`):

### Continuous Integration/Deployment

**Deployment Flow:**
1. Push to `master` branch
2. Netlify builds dans deployes
5. Site live at https://thibaultlebrun.dev/

---

### Table of Contents

- Auto-generated from headers
- Custom styling

---

## 9. Key Dependencies & Technologies

### Build Tools
- **Hugo** v0.93.2 (Extended) - Static site generator
- **Node.js/npm** - Package manager

### Frontend Libraries
- **TailwindCSS**

### Themes & Templates
- i18n support: English, French, Spanish, German, Russian, Japanese, Turkish, Chinese (CN/TW)

### Hosting & Deployment
- **Netlify**

---

### Local Development

```bash
make dev  # Starts dev server with hot reload
make css  # compile css
```

## Key Customization Points

### To modify appearance:
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
- **Emoji support:** Enabled in Hugo config
- **RSS feed:** Generated at `/index.xml`

---