## Prioritized Action Plan

### Phase 1: Critical Fixes (Week 1)

These items block crawlability or cause immediate damage to user trust.

| # | Action | Effort | Category |
|---|--------|--------|----------|
| 1 | Create `public/robots.txt` with sitemap reference | 5 min | Technical |
| 2 | Install `@astrojs/sitemap` and configure in `astro.config.mjs` | 10 min | Technical |
| 3 | Fix `/type/culture` empty page — filter getStaticPaths | 10 min | Technical |
| 4 | Replace all 10 SVG placeholder images with real photos | 2-4 hrs | Images |
| 5 | Fix `.jpg` files that contain SVG — rename or replace | 15 min | Images |
| 6 | Create `public/images/og-default.jpg` (1200x630) | 30 min | Images/On-Page |
| 7 | Add WebSite + Organization JSON-LD to BaseLayout.astro | 15 min | Schema |

### Phase 2: High-Impact Improvements (Weeks 2-3)

These items significantly improve rankings, CTR, and user experience.

| # | Action | Effort | Category |
|---|--------|--------|----------|
| 8 | Expand About page: add author credentials, editorial process, update policy | 2 hrs | Content |
| 9 | Either publish 3-5 blog posts or remove blog from navigation | 1-4 hrs | Content |
| 10 | Add external citations (2-3 per attraction page) linking to official sources | 1 hr | Content |
| 11 | Add FAQPage schema to FAQ page and homepage FAQ section | 30 min | Schema |
| 12 | Expand TouristAttraction schema: add image, url, geo, offers, openingHours | 1 hr | Schema |
| 13 | Add BreadcrumbList schema to all pages with breadcrumbs | 30 min | Schema |
| 14 | Add breadcrumb navigation to type, collection, and compare pages | 1 hr | On-Page |
| 15 | Fix heading hierarchy on subpages (add H2 section headings) | 2 hrs | On-Page |
| 16 | Implement functional mobile navigation menu | 1-2 hrs | On-Page |
| 17 | Standardize title tag format (year suffix or no year suffix) | 15 min | On-Page |

### Phase 3: Content & Authority (Month 2)

These items build long-term authority and expand the site's reach.

| # | Action | Effort | Category |
|---|--------|--------|----------|
| 18 | Create `public/llms.txt` with site overview and key page links | 15 min | GEO |
| 19 | Add last-updated date to every page (not just homepage) | 1 hr | Content |
| 20 | Add author/editor attribution to all pages | 30 min | Content |
| 21 | Expand attraction pages with richer entity data (hours, geo, accessibility) | 3-5 hrs | GEO/Content |
| 22 | Make attraction-specific tips unique (replace boilerplate tips) | 1 hr | Content |
| 23 | Add more attractions to reach the "50+" claim or adjust homepage copy | 5-20 hrs | Content |
| 24 | Add ItemList schema to type pages and collections page | 30 min | Schema |
| 25 | Add Article schema to comparison page | 15 min | Schema |
| 26 | Add responsive image markup (srcset, picture) for attraction photos | 1 hr | Images/Perf |

### Phase 4: Monitoring & Iteration (Ongoing)

These items provide ongoing improvement and should be revisited monthly.

| # | Action | Effort | Category |
|---|--------|--------|----------|
| 27 | Set up Google Search Console and submit sitemap | 30 min | Technical |
| 28 | Set up Google Analytics (GA4) for traffic monitoring | 30 min | Technical |
| 29 | Monitor Core Web Vitals in Search Console / PageSpeed Insights | Ongoing | Performance |
| 30 | Track AI citation growth over time | Ongoing | GEO |
| 31 | Regularly update ticket prices and subway info (monthly) | 1 hr/month | Content |
| 32 | Review and optimize CSS bundle size after Tailwind purge config | 30 min | Performance |
| 33 | Consider adding Chinese-language pages (i18n routing) | 5-10 hrs | GEO |
| 34 | Add branded custom 404 page | 30 min | Technical |
| 35 | Set up brand mention monitoring for AI platform citations | 30 min | GEO |

---

## Effort Summary

| Phase | Items | Estimated Hours |
|-------|-------|-----------------|
| Phase 1: Critical Fixes | 7 | 3-6 hrs |
| Phase 2: High-Impact | 10 | 8-14 hrs |
| Phase 3: Content & Authority | 9 | 11-29 hrs |
| Phase 4: Monitoring | 9 | 2-12 hrs + ongoing |
| **Total** | **35** | **24-61 hrs** |

---

*Focus on Phase 1 first. Completing just the first 7 items will raise the SEO Health Score from ~48 to ~65 and make the site functional for search engines and social sharing.*
