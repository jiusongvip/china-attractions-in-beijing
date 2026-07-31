## Schema & Structured Data Findings

### What Works
- Attraction detail pages implement `TouristAttraction` schema via JSON-LD
- Schema includes `name`, `description`, `address` (PostalAddress), and `touristType`
- JSON-LD is valid and well-formed on all 10 attraction pages

### Findings

#### [High] Minimal TouristAttraction schema properties
Each attraction schema only includes 4-5 properties. Critical properties are missing:
- `image` — no photo reference (critical for rich results)
- `url` — no canonical page URL
- `geo` (GeoCoordinates) — no lat/long data
- `openingHours` — no operating hours
- `offers` — no ticket price structured data (despite having ticket prices in the page content)
- `publicAccess` — not specified

**Recommendation:** Expand the `TouristAttraction` schema to include all available data points. For the 10 attractions, add `image`, `url`, `geo`, and `offers` at minimum.

#### [Critical] No WebSite or Organization schema on homepage
The homepage lacks `WebSite` (with SearchAction) and `Organization` schema. These are the most basic schema types that every site should implement.
**Recommendation:** Add to `BaseLayout.astro`:
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "China Attractions in Beijing",
  "url": "https://china-attractions-in-beijing.com"
}
```

#### [High] No BreadcrumbList schema
Attraction pages have visual breadcrumbs in the HTML but no `BreadcrumbList` structured data.
**Recommendation:** Generate `BreadcrumbList` schema on each page that has breadcrumb navigation. This enables breadcrumb rich results in SERPs.

#### [Medium] No FAQPage schema on FAQ page
The FAQ page uses `<details>` elements for 8 FAQ items but lacks `FAQPage` structured data with `Question`/`Answer` items. The homepage also has 6 FAQ items with no schema.
**Recommendation:** Add `FAQPage` schema to the FAQ page and the homepage FAQ section. Each `<details>` should map to a `Question`/`Answer` pair.

#### [Medium] No CollectionPage or ItemList schema
The `/collections/` page and type pages (`/type/historical`, etc.) are list pages with no `ItemList` or `CollectionPage` schema.
**Recommendation:** Add `ItemList` schema to any page listing multiple attractions.

#### [Low] No Article schema on comparison pages
The `/compare/badaling-vs-mutianyu` page is essentially an article comparing two attractions but lacks `Article` or `Review` schema.
**Recommendation:** Add `Article` schema to the comparison page with `about` referencing both attractions.
