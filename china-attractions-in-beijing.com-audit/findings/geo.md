## AI Search Readiness (GEO) Findings

### What Works
- Content is structured in clear sections with descriptive headings that LLMs can parse
- JSON-LD schema on attraction pages provides structured data that AI crawlers can ingest
- No JavaScript-dependent content — all information is in the static HTML
- Content is factual, specific, and demonstrates first-hand knowledge (subway exit numbers, ticket booking procedures)

### Findings

#### [High] No llms.txt file
The site lacks an `llms.txt` file — the emerging standard for providing LLM-friendly site summaries. Major AI platforms (ChatGPT, Claude, Perplexity) are increasingly consuming llms.txt for context.
**Recommendation:** Create `public/llms.txt` with a concise site overview and links to key pages:
```
# China Attractions in Beijing
> Complete guide to Beijing's top attractions for international travelers.
## Key Pages
- [Home](https://china-attractions-in-beijing.com/): Full guide with checklist and FAQs
- [Forbidden City](https://china-attractions-in-beijing.com/attractions/forbidden-city): ...
...
```

#### [High] No E-E-A-T authority signals
The site lacks all key authority signals that AI crawlers use to evaluate trustworthiness:
- No author names or credentials
- No organizational transparency (who runs this site?)
- No external citations or references
- No date-of-last-update indicators on most pages (only the homepage shows "Updated July 2026")
- No "reviewed by" or editorial process statements

**Recommendation:** Add at minimum: an author/editor name on each page (even if site-wide), a "last updated" date on every page, and 1-2 external citations per attraction page linking to official sources.

#### [Medium] Thin entity coverage
Each attraction page names the attraction but provides only basic stats (rating, duration, ticket price, subway stop). Key entity attributes missing: opening hours, peak/off-peak periods, accessibility info, nearby dining, photography rules, audio guide availability.
**Recommendation:** Expand each attraction page with richer entity data. AI models extract entities and their attributes; the more complete the entity profile, the more likely the site is cited in AI-generated answers.

#### [Medium] No FAQ structured data
The FAQ sections (homepage + /faq page) use `<details>` elements which are semantically correct but not machine-readable in a way AI crawlers prefer. Adding FAQPage schema would make the Q&A pairs extractable.
**Recommendation:** Implement FAQPage schema alongside the existing `<details>` markup. This is a quick win for AI citability of the practical travel Q&A content.

#### [Low] No multilingual content
The site is English-only. Beijing attracts visitors from many non-English-speaking countries (Korea, Japan, Russia, Europe). AI models serving non-English queries may not surface the site.
**Recommendation:** Consider adding Chinese and/or other language versions. Astro's i18n routing supports this natively. Even a single translated key page (e.g., Chinese homepage) would dramatically expand the addressable audience.

#### [Low] No brand mention monitoring
There is no way to track whether AI platforms are citing or referencing the site's content.
**Recommendation:** Set up brand monitoring via Google Alerts, mention tracking, or specialized AI visibility tools to track citation growth over time.
