## Performance Findings

### What Works
- Static site generation (SSG) — all pages are pre-rendered as HTML, no client-side JS required
- CSS containment with `aspect-[16/9]` prevents layout shift from images
- Font files use modern `woff2` format with subsetting (Latin + Cyrillic + Vietnamese)
- No render-blocking third-party scripts
- No tracking scripts, analytics, or ad networks
- Images use `loading="lazy"` and `decoding="async"`
- Geist font family is optimized and self-hosted (no Google Fonts external request)

### Findings

#### [Medium] CSS bundle size
The production CSS bundle in `dist/_astro/BaseLayout.*.css` is 71,645 bytes (uncompressed). This includes the full Tailwind v4 utility set. For a site with 25 pages and relatively simple layouts, this is larger than necessary.
**Recommendation:** Run Tailwind CSS purging. If using Tailwind v4, ensure the content paths are correctly configured so unused utility classes are eliminated. Estimate: could reduce to 20-30KB.

#### [Medium] Font file payload
Six font files totaling ~150KB are loaded for the Latin subfamily alone (Geist Sans + Geist Mono, 400/500/600/700 weights). This is a one-time cost that caches well but inflates first-visit page weight.
**Recommendation:** Consider using `font-display: swap` to prevent FOIT and evaluate whether all font weights are needed. The Geist Mono weights (400/500) are particularly heavy for limited use.

#### [Low] No asset preloading
Critical above-fold resources (fonts, hero image if added) are not preloaded via `<link rel="preload">`.
**Recommendation:** Add preload hints for the primary font files and any hero image.

#### [Low] No service worker or offline support
As an informational travel guide, offline access would be valuable for travelers with limited connectivity in China.
**Recommendation:** Consider adding a simple service worker for caching static assets, but this is optional and should be weighed against maintenance cost.

#### [Info] Dev vs Production differences
In development mode (as tested), CSS is inlined into every page (~71KB per page). In production, the CSS is extracted to a single shared file (~71KB, cached). The production build is the correct reference for performance scoring.
**Recommendation:** Always test performance against the production build (`npm run build && npx serve dist`).
