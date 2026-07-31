## Executive Summary

**Site:** china-attractions-in-beijing.com (tested locally on Astro dev server)
**Date:** 2026-07-31
**Business Type:** Travel/Tourism — Informational guide for international visitors to Beijing
**Pages Audited:** 28 (10 attraction detail, 6 type, 3 collection, 2 compare, 5 informational, homepage, blog)

### Overall SEO Health Score: 48/100

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Technical SEO | 45 | 22% | 9.9 |
| Content Quality | 55 | 23% | 12.7 |
| On-Page SEO | 65 | 20% | 13.0 |
| Schema / Structured Data | 30 | 10% | 3.0 |
| Performance (CWV) | 75 | 10% | 7.5 |
| AI Search Readiness (GEO) | 25 | 10% | 2.5 |
| Images | 15 | 5% | 0.8 |
| **Total** | | | **49.4** |

### Top 5 Critical Issues

1. **No robots.txt or XML sitemap** — Search engines have zero crawl guidance. Pages are discoverable only through internal links.
2. **All images are SVG placeholders** — Dark rectangles with text instead of real photos. This destroys visual credibility and prevents image search traffic.
3. **No WebSite/Organization schema** — Missing the most fundamental structured data types.
4. **Empty blog page** — A dead-end page linked from the main navigation with zero content.
5. **No E-E-A-T authority signals** — No author info, no citations, no last-updated dates on subpages.

### Top 5 Quick Wins (under 1 hour each)

1. Create `robots.txt` in `public/` — 5 minutes
2. Install `@astrojs/sitemap` and rebuild — 10 minutes
3. Create `public/images/og-default.jpg` (branded 1200x630 image) — 30 minutes
4. Add WebSite + Organization JSON-LD to BaseLayout — 15 minutes
5. Add FAQPage schema to the FAQ page — 15 minutes

---

## Technical SEO

**Score: 45/100**

The site's static generation architecture is solid — all pages are pre-rendered HTML with clean URLs, proper canonicals, and no JavaScript dependency. However, the crawl infrastructure layer is entirely missing.

### Critical Gaps
- No `/robots.txt` — search engines have no crawl instructions
- No `/sitemap.xml` — no machine-readable page inventory
- Empty route at `/type/culture` exists because the type label is defined but has zero attractions

### Recommendations
1. Create `public/robots.txt` pointing to the sitemap
2. Install `@astrojs/sitemap` for automatic sitemap generation
3. Filter `getStaticPaths()` in `[type].astro` to skip types with no attractions
4. Add a branded `404.astro` page
5. Verify security headers are set by the production hosting platform

---

## Content Quality

**Score: 55/100**

The attraction content is genuinely useful — subway exit numbers, ticket booking procedures, and seasonal advice show real domain knowledge. The homepage FAQ and pre-trip checklist are thoughtfully structured. The weakness is in supporting content: the About page is 150 words, the blog is empty, and there are no external citations to reinforce authority.

### Priority Fixes
1. Expand the About page with author credentials, editorial process, and update policy
2. Either publish 3-5 blog posts or remove the blog from navigation
3. Add 2-3 external citations per attraction page linking to official sources
4. Make at least 1 tip per attraction page unique to that specific attraction
5. Adjust the "50+ attractions" claim on the homepage to match the actual 10 listed

---

## On-Page SEO

**Score: 65/100**

This is the strongest category. Every page has unique title tags, meta descriptions, and H1 headings. URL structure is clean. Internal linking is strong with 57 links across 22 targets on the homepage alone.

### Areas to Improve
1. Fix heading hierarchy on subpages (several jump from H1 to H4 with no H2/H3)
2. Add breadcrumbs to all pages, not just attraction detail pages
3. Implement a working mobile navigation menu (the hamburger button currently does nothing)
4. Standardize title tag convention (year suffix present on some, absent on others)

---

## Schema & Structured Data

**Score: 30/100**

Attraction detail pages have functional `TouristAttraction` JSON-LD, which is good. But the implementation is minimal (4-5 properties out of 20+ available) and no other page types have any schema at all.

### Missing Schema Types
- **WebSite** + **Organization** (homepage) — most basic, highest impact
- **BreadcrumbList** (all pages with breadcrumbs)
- **FAQPage** (FAQ page + homepage FAQ section)
- **ItemList** (type pages, collections page)
- **Article** (comparison page)

### Schema Expansion for TouristAttraction
Add: `image`, `url`, `geo` (lat/long), `openingHours`, `offers` (ticket price), `publicAccess`

---

## Performance

**Score: 75/100**

The static site architecture gives a strong performance baseline. No client-side JS, no third-party scripts, self-hosted fonts, and lazy-loaded images. Main optimization opportunities are in CSS bundle size and font payload.

### Recommendations
1. Review Tailwind v4 purge config — the 71KB CSS bundle likely contains many unused utilities
2. Add `font-display: swap` to prevent flash of invisible text
3. Preload critical font files with `<link rel="preload">`
4. Add explicit `width`/`height` attributes to all images for LCP optimization

---

## Images

**Score: 15/100**

This is the worst-performing category and the most visually damaging. Every attraction "photo" is a dark SVG rectangle with the attraction name in white text, served with a misleading `.jpg` extension. Until real photos are added, the site cannot credibly serve as a visual travel guide.

### Immediate Actions
1. Replace all 10 attraction images with real photographs (minimum 800x450px, WebP format)
2. Rename or replace the `.jpg` files that actually contain SVG content
3. Add responsive image markup (`srcset`, `<picture>`) for different viewport sizes
4. Create a branded OG image at `/images/og-default.jpg` (1200x630px)
5. Add explicit `width` and `height` attributes to all `<img>` tags

---

## AI Search Readiness (GEO)

**Score: 25/100**

The site's structured, section-based content is inherently AI-friendly. But without llms.txt, E-E-A-T signals, or rich entity data, the site is unlikely to be cited by AI platforms like ChatGPT, Perplexity, or Google AI Overviews.

### Priority Actions
1. Create `llms.txt` with site overview and key page links
2. Add author/editor attribution and last-updated dates to every page
3. Expand entity data on attraction pages (hours, geo, accessibility, nearby dining)
4. Add FAQPage schema to make Q&A content machine-extractable
5. Consider Chinese-language content for the largest target audience

---

## Crawl Summary

| Metric | Value |
|--------|-------|
| Total pages crawled | 28 |
| HTTP 200 pages | 26 |
| HTTP 302 redirect | 1 (/type/culture) |
| HTTP 404 pages | 1 (/nonexistent-page — correct behavior) |
| Pages with schema | 10 (attraction detail only) |
| Pages with images | 11 (but all images are SVG placeholders) |
| Average page size (dev) | ~57 KB (includes inlined CSS) |
| Average page size (prod est.) | ~8-12 KB (CSS externalized) |
| Internal links (homepage) | 57 across 22 unique targets |
| External links (entire site) | 0 |

---

*Audit generated 2026-07-31 by Codex. See [ACTION-PLAN.md](ACTION-PLAN.md) for the prioritized implementation roadmap.*
