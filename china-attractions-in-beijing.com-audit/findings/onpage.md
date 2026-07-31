## On-Page SEO Findings

### What Works
- Every page has a unique, descriptive `<title>` tag that includes target keywords
- Every page has a unique `<meta name="description">` of appropriate length (130-155 chars)
- H1 headings are present on every page and match the page topic
- Homepage heading structure is well-organized: H1 > H2 (8 sections) > H3 (26 subsections) > H4
- Internal linking is extensive with 57 internal links on the homepage across 22 unique targets
- URLs are clean, descriptive, and use hyphens (e.g., `/attractions/forbidden-city`)
- No query parameters in URLs
- Keyword placement is natural and user-focused

### Findings

#### [Medium] Heading hierarchy gaps on subpages
Several pages jump from H1 directly to H4 (from the Footer), with no H2 or H3 content sections:
- `/about`: H1 only (no H2/H3), then H4 from footer
- `/faq`: H1 only, details elements have summaries but no H2/H3 structural headings
- `/collections`: H1 > H3 (cards), no H2
- `/compare`: H1 > H3, no H2
- `/blog`: H1 > H4, completely empty H2/H3

**Recommendation:** Add H2 section headings to break content into scannable sections on every page. Use the hierarchy: H1 (page title) > H2 (major sections) > H3 (subsections).

#### [Medium] Missing breadcrumbs on non-attraction pages
Only attraction detail pages have breadcrumbs. Type pages, collections, compare pages, and informational pages have no breadcrumb navigation.
**Recommendation:** Add breadcrumbs to all pages. This improves UX, provides internal linking structure, and enables BreadcrumbList rich results.

#### [Medium] Mobile hamburger menu is non-functional
The Header component renders a hamburger button for mobile (`md:hidden`) but there is no associated mobile menu panel or JavaScript toggle. Clicking it does nothing.
**Recommendation:** Implement a working mobile navigation. For a static site, a simple `<details>` or CSS-only solution is sufficient.

#### [Low] All nav links hidden on mobile
The four main nav links have `hidden md:inline` classes, meaning mobile users see zero navigation links — only a non-functional hamburger button.
**Recommendation:** Once the mobile menu is functional, ensure all 4 nav links are accessible from mobile.

#### [Low] Title tag formatting inconsistency
Some titles use `[2026]` suffix convention, others don't:
- With year: "Plan Your Trip [2026]", "Season by Season Guide [2026]", "Complete Guide [2026]"
- Without year: "About | China Attractions in Beijing", "Curated Guides for Every Traveler"
**Recommendation:** Either add year to all titles or remove from all. Consistency matters for brand presentation in SERPs.

#### [Low] No meta keywords (low priority)
While meta keywords are ignored by Google, some secondary search engines and internal site search tools still reference them.
**Recommendation:** Optionally add, but this is the lowest priority item in the entire audit.

#### [Low] Clickable card links may confuse crawlers
The `AttractionCard` component wraps the entire card in an `<a>` tag. This is fine for users but means the card's image alt text and all text content becomes the link anchor text. Some crawlers may interpret this as overly long anchor text.
**Recommendation:** This is an acceptable pattern. Monitor in Search Console for any anchor text anomalies.
