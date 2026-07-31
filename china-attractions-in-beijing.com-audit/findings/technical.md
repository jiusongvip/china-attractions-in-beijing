## Technical SEO Findings

### What Works
- All pages have valid canonical URLs pointing to correct HTTPS paths
- All pages return proper HTTP status codes (200 for valid pages, 404 for missing)
- SSL/TLS configured (HTTPS enforced)
- Valid `<html lang="en">` on all pages
- `charset=utf-8` declared on all pages
- Responsive viewport meta tag present
- No mixed-content issues (all resources use HTTPS paths)

### Findings

#### [Critical] No robots.txt file
The site returns 404 for `/robots.txt`. Without a robots.txt, search engines have no crawl guidance. At minimum, you need to allow crawling and point to the sitemap.
**Recommendation:** Create a `robots.txt` in `public/`:
```
User-agent: *
Allow: /
Sitemap: https://china-attractions-in-beijing.com/sitemap.xml
```

#### [Critical] No XML sitemap
The site returns 404 for `/sitemap.xml`. A sitemap is essential for search engines to discover all pages, especially dynamic routes like `/attractions/[slug]` and `/type/[type]`.
**Recommendation:** Install `@astrojs/sitemap` and configure it in `astro.config.mjs`. The static site already has all pages pre-rendered; the integration will automatically generate a comprehensive sitemap.

#### [High] Empty page at /type/culture
The route `/type/culture` exists because `culture` is in `typeLabels`, but no attraction has `type: "culture"`. The page returns a 302 redirect, but the route is still discoverable and creates a soft-404 situation.
**Recommendation:** Either add content of type "culture" or filter `getStaticPaths` to only generate pages for types that have attractions.

#### [High] OG image reference does not exist
Every page references `https://china-attractions-in-beijing.com/images/og-default.jpg`, but this file does not exist in `public/images/`. This means social shares will have no preview image.
**Recommendation:** Create a proper OG image (1200x630 px) and place it at `public/images/og-default.jpg`. Alternatively, generate one per attraction page.

#### [Medium] HTML entities in title tags
Title tags containing ampersands render as `&amp;` in the raw HTML (e.g., "Tickets, Hours, Subway &amp; Tips"). While browsers handle this correctly, it appears in raw source and some crawlers may parse it oddly.
**Recommendation:** Use the `&amp;` or `&#38;` entity only when the title is being embedded in an HTML attribute context; Astro's `{ }` expression handles escaping automatically so using a bare `&` in the template literal is fine.

#### [Medium] No custom 404 page
The 404 response returns a basic Astro dev error page. In production, there is no branded 404 page.
**Recommendation:** Add a `src/pages/404.astro` with helpful navigation links and a search suggestion.

#### [Low] No security headers
The dev server does not set HSTS, X-Content-Type-Options, X-Frame-Options, or CSP headers. The production deployment platform may add these, but they should be verified.

#### [Low] Inline CSS in dev mode
In development, all CSS (~71KB) is inlined in every page's `<head>`. In production (static build), the CSS is extracted to a separate file. This is fine for production but note that the CSS bundle is larger than ideal.
**Recommendation:** Review Tailwind purge settings and remove unused utility classes. The current `global.css` appears to include the full Tailwind v4 defaults.
