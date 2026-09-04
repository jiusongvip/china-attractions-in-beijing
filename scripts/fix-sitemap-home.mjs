// Post-build sitemap fixes:
// 1. Remove trailing slash from homepage URL (canonical has no trailing slash).
// 2. Serve the sitemap index at /sitemap.xml (robots.txt declares this path,
//    but @astrojs/sitemap only writes sitemap-index.xml, so /sitemap.xml 404s).
import { readFileSync, writeFileSync, readdirSync, copyFileSync } from "node:fs";
import { join } from "node:path";

const distDir = "dist";
const homeUrl = "https://www.china-attractions-in-beijing.com";
const target = `<loc>${homeUrl}/</loc>`;
const replacement = `<loc>${homeUrl}</loc>`;

let changed = false;
for (const file of readdirSync(distDir)) {
  if (!file.startsWith("sitemap") || !file.endsWith(".xml") || file.includes("index")) {
    continue;
  }
  const path = join(distDir, file);
  const content = readFileSync(path, "utf8");
  if (content.includes(target)) {
    writeFileSync(path, content.replaceAll(target, replacement));
    changed = true;
    console.log(`OK ${file}: homepage URL trailing slash removed`);
  }
}

if (!changed) {
  console.log("WARN no sitemap homepage URL needed fixing");
}

copyFileSync(join(distDir, "sitemap-index.xml"), join(distDir, "sitemap.xml"));
console.log("OK sitemap.xml written (copy of sitemap-index.xml)");
