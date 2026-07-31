## Images Findings

### What Works
- All images have descriptive `alt` text matching the attraction name
- Images use `loading="lazy"` for below-fold content
- Images use `decoding="async"` for non-blocking decode
- Aspect ratio containers (`aspect-[16/9]`) prevent layout shift (CLS)
- Image paths are consistent and predictable (`/images/attractions/{slug}.jpg`)

### Findings

#### [Critical] All images are SVG placeholders, not real photos
Every attraction image file (both `.jpg` and `.svg` versions) contains identical SVG placeholder content: a dark rectangle with the attraction name in white text. The `.jpg` files have a `.jpg` extension but contain SVG markup — browsers will render them, but this is technically invalid and misleading.

The content of each "image" is:
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450">
  <rect width="800" height="450" fill="#1e293b"/>
  <text x="400" y="225" text-anchor="middle" fill="#cbd5e1">ATTRACTION NAME</text>
</svg>
```

This is the single most damaging issue for the site's visual credibility. Users clicking from search results will see blank dark rectangles instead of photos of the Forbidden City, Great Wall, etc.

**Recommendation:** Replace all 10 attraction images with real photographs. Minimum: 800x450px, compressed WebP or optimized JPEG under 100KB each. If real photos are unavailable, use high-quality stock photos with proper licensing.

#### [High] File extension mismatch
Files named `.jpg` contain SVG content. This can cause issues with CDNs, image optimization services, and some crawlers.
**Recommendation:** Rename `.jpg` to `.svg` if keeping SVGs, or replace with actual JPEG/WebP images.

#### [Medium] No responsive image markup
Images use a single `src` with no `srcset` or `<picture>` element for responsive delivery. All viewports receive the same 800x450 image.
**Recommendation:** Use Astro's built-in `<Image />` component or add `srcset` for responsive image delivery.

#### [Medium] No width/height attributes
Images lack explicit `width` and `height` attributes. While the `aspect-[16/9]` CSS container handles layout, explicit dimensions improve LCP and prevent cumulative layout shift during load.
**Recommendation:** Add `width="800"` and `height="450"` to all `<img>` tags.

#### [Low] OG image also missing
In addition to the missing attraction photos, the shared OG image (`/images/og-default.jpg`) does not exist either, doubling the image problem for social sharing.
**Recommendation:** Create a branded OG image (1200x630px) with the site name and a Beijing-themed visual.
