# Generate three blog articles for the Beijing travel blog.
import pathlib

OUT = pathlib.Path("src/pages/blog")
OUT.mkdir(parents=True, exist_ok=True)

def write(path, slug, title, desc, body):
    front = '---\nimport BaseLayout from "../../layouts/BaseLayout.astro";\nimport Icons from "../../components/Icons.astro";\nimport { siteConfig } from "../../data/site";\n\nconst title = "' + title + '";\nconst description = "' + desc + '";\nconst slug = "/blog/' + slug + '/";\nconst date = "2026-07-31";\n---\n\n'
    template = '<BaseLayout title={title} description={description}>\n  <article class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16">\n    <header class="mb-10">\n      <p class="text-sm text-base-400 mb-2">Published {date}</p>\n      <h1 class="text-3xl md:text-4xl font-bold tracking-tight text-base-900 mb-3">' + title + '</h1>\n      <p class="text-lg text-base-500 leading-relaxed">' + desc + '</p>\n    </header>\n'
    full = (front + template + body + '\n  </article>\n</BaseLayout>\n').replace('\u2014', '&mdash;').replace('\u2013', '&ndash;').replace('\u2019', '&rsquo;').replace('\u201c', '&ldquo;').replace('\u201d', '&rdquo;')
    OUT.joinpath(path).write_text(full, encoding="utf-8")
    print(f"  created {path}")

# ============================================================
# Article 1: Where to Stay in Beijing
# ============================================================
body_stay = """\
    <script type="application/ld+json" set:html={`{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "${title}",
      "description": "${description}",
      "datePublished": "${date}",
      "author": { "@type": "Organization", "name": "${siteConfig.name}" },
      "publisher": { "@type": "Organization", "name": "${siteConfig.name}", "url": "${siteConfig.url}" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "${siteConfig.url}${slug}" }
    }`}></script>
    <script type="application/ld+json" set:html={`{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "What\u2019s the best area to stay in Beijing for first-time visitors?", "acceptedAnswer": { "@type": "Answer", "text": "Dongcheng District, especially the Wangfujing-Dengshikou area. You\u2019ll be within walking distance of the Forbidden City, Tiananmen Square, and Jingshan Park, with easy subway access to everywhere else." } },
        { "@type": "Question", "name": "What\u2019s the cheapest area to stay in Beijing that\u2019s still convenient?", "acceptedAnswer": { "@type": "Answer", "text": "The Dongzhimen-Dongsishitiao corridor in Dongcheng. You get Dongzhimen Station (Lines 2 and 13, plus the Airport Express) for a fraction of Wangfujing prices. Hostels and budget hotels here are 30\u201350% cheaper while keeping you 15 minutes by subway from major attractions." } },
        { "@type": "Question", "name": "Should I stay near the Great Wall?", "acceptedAnswer": { "@type": "Answer", "text": "For most travelers, staying in central Beijing and day-tripping to the Wall is the better choice. But if you\u2019re a photographer chasing sunrise on the Wall or visiting in peak autumn foliage, one night near Mutianyu or Gubei Water Town is worth the splurge." } },
        { "@type": "Question", "name": "Is it safe to stay in a hutong courtyard hotel?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Beijing is one of the safest major cities in the world, and hutong courtyard hotels are generally well-maintained and secure. The main consideration is that some are down narrow alleys where taxis can\u2019t reach \u2014 you may need to walk the last 100\u2013200 meters with your luggage." } }
      ]
    }`}></script>
    <div class="table-responsive mb-10">
      <table class="table-attractions">
        <thead><tr><th>District</th><th>Best For</th><th>Vibe</th><th>Budget Range</th></tr></thead>
        <tbody>
          <tr><td>Dongcheng</td><td>First-timers, sightseeing</td><td>Historic, central, walkable</td><td>\u00a5150\u20131,500/night</td></tr>
          <tr><td>Xicheng</td><td>Hutong lovers, culture seekers</td><td>Traditional, quieter</td><td>\u00a5120\u20131,200/night</td></tr>
          <tr><td>Chaoyang</td><td>Nightlife, shopping, business</td><td>Modern, expat-friendly</td><td>\u00a5300\u20132,500/night</td></tr>
          <tr><td>Haidian</td><td>Budget travelers, students</td><td>University area, tech hub</td><td>\u00a5100\u2013800/night</td></tr>
          <tr><td>Dongzhimen</td><td>Airport access, value</td><td>Transit hub, practical</td><td>\u00a5100\u2013900/night</td></tr>
          <tr><td>Gulou</td><td>Boutique stays, photography</td><td>Hip, lake-and-hutong setting</td><td>\u00a5200\u20131,800/night</td></tr>
        </tbody>
      </table>
    </div>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Dongcheng \u2014 Best for First-Time Visitors</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Dongcheng is the geographic and cultural heart of tourist Beijing. The Forbidden City, Tiananmen Square, Jingshan Park, Wangfujing shopping street, and the National Museum are all in this district. If you only have 2\u20133 days and want to maximize sightseeing time, this is where you stay.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Wangfujing\u2013Dengshikou</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Walking distance to the Forbidden City and Tiananmen. The pedestrian-only Wangfujing street has everything from high-end malls to the famous night market snack street. Hotels here range from the five-star Peninsula Beijing to mid-range chains like Holiday Inn Express. Downside: it\u2019s the most tourist-dense neighborhood, so restaurants cater heavily to visitors and prices reflect it.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Nanluoguxiang area</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Further north in Dongcheng, nestled among historic hutongs. Boutique courtyard hotels (siheyuan conversions) dominate here. Staying in a restored Qing Dynasty courtyard with modern amenities is a uniquely Beijing experience. The trade-off: alleys are narrow, taxis can\u2019t always reach your door, and you\u2019ll need to be comfortable navigating on foot. Perfect for travelers who want atmosphere over convenience.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You\u2019re visiting Beijing for the first time, your itinerary is built around imperial landmarks, and you want to walk to the Forbidden City.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Hostels from \u00a580/night, mid-range hotels \u00a5350\u2013700/night, luxury \u00a51,000+/night. <strong>Subway:</strong> Lines 1, 2, 5, 6, and 8 crisscross Dongcheng.</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Xicheng \u2014 Best for Hutong Atmosphere</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Xicheng sits directly west of the Forbidden City and contains some of Beijing\u2019s best-preserved hutong neighborhoods. The Shichahai lakes area, the Bell and Drum Towers, and Beihai Park are all here. It\u2019s slightly less tourist-dense than Dongcheng but equally historic \u2014 the difference is you\u2019ll hear more Chinese spoken on the streets.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Shichahai lakes area</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Three connected lakes \u2014 Qianhai, Houhai, and Xihai \u2014 surrounded by hutong alleys, courtyard restaurants, and lakeside bars. This is where Beijingers go on weekend afternoons. Staying here puts you within a 15-minute walk of the Bell and Drum Towers, <a href="/attractions/nanluoguxiang/">Nanluoguxiang</a>, and the northern edge of the imperial axis. The lake views at dusk are a genuine highlight.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Xisi\u2013Fuchengmen area</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Further south in Xicheng, this is a working Beijing neighborhood with excellent food at local prices. The White Dagoba Temple (Baitasi), one of Beijing\u2019s oldest Buddhist landmarks, anchors the area. Few tourists stay here, so you get a more authentic experience \u2014 and hotel prices drop 30\u201340% compared to Dongcheng equivalents.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You want a traditional Beijing experience with lakeside strolls, morning tai chi in the parks, and hutong alleys right outside your door.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Hostels from \u00a570/night, courtyard hotels \u00a5300\u2013800/night, lakeside boutique \u00a51,200+/night. <strong>Subway:</strong> Lines 2, 4, 6, and 8 serve Xicheng.</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Chaoyang \u2014 Best for Nightlife, Dining, and Modern Comfort</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Chaoyang is Beijing\u2019s modern face: the CBD skyline, Sanlitun\u2019s bar streets, 798 Art District, and the city\u2019s best international dining. It\u2019s where most expats live and where Beijing feels most like a global capital. The trade-off: you\u2019re further from the imperial sights \u2014 expect 20\u201340 minutes by subway to reach the Forbidden City or Temple of Heaven.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Sanlitun</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s nightlife and dining epicenter. Taikoo Li is an open-air luxury mall worth visiting even if you\u2019re not shopping. The surrounding streets are dense with cocktail bars, craft beer pubs, Korean BBQ joints, and some of the city\u2019s best ramen. Hotels range from the ultra-luxe Opposite House to the mid-range InterContinental. The nearest imperial attraction is a 25-minute subway ride.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Guomao-CBD</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s financial district, home to the China World Trade Center. All the major international hotel brands have flagships here: China World Hotel, Park Hyatt, Ritz-Carlton. If you\u2019re combining business with tourism, this is the obvious choice. Guomao Station (Lines 1 and 10) connects you to the Forbidden City in 15 minutes.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">798 Art District area</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">A former East German-designed electronics factory complex turned contemporary art hub. Staying near 798 puts you among galleries, artist studios, and industrial-chic cafes. The nearest subway (Wangjing South, Line 14) is a 15-minute walk, so you\u2019ll rely on taxis or ride-hailing more than in other neighborhoods.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You care as much about restaurants, bars, and shopping as you do about sightseeing, or you\u2019re a repeat visitor who\u2019s already done the imperial circuit.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Mid-range \u00a5400\u2013900/night, luxury \u00a51,200\u20133,000+/night. <strong>Subway:</strong> Lines 1, 6, 10, and 14 serve Chaoyang.</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Haidian \u2014 Best for Budget Travelers</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Haidian is Beijing\u2019s university district, home to Peking University, Tsinghua University, and the <a href="/attractions/summer-palace/">Summer Palace</a>. It\u2019s northwest of the city center and significantly cheaper than Dongcheng or Chaoyang. If you\u2019re traveling on a tight budget or you\u2019re a student, Haidian delivers solid value.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Wudaokou</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s student town. Cheap Korean restaurants, bubble tea shops, and \u00a5100/night budget hotels cluster around the Wudaokou subway station (Line 13). It\u2019s youthful and energetic, and you\u2019ll stretch your yuan further here than anywhere else in Beijing. The Summer Palace is a 20-minute walk or one subway stop away. The Forbidden City is about 40 minutes by subway.</p>
      <h3 class="text-lg font-medium text-base-800 mb-2">Zhongguancun</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s tech hub, sometimes called \u201cChina\u2019s Silicon Valley.\u201d Home to the headquarters of Baidu, ByteDance, and hundreds of startups. Hotels here cater to business travelers, so mid-range chains like Holiday Inn and Atour are plentiful and often run promotions. Good access to the Summer Palace (15 minutes by taxi) and Fragrant Hills Park.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You\u2019re on a student or backpacker budget, the Summer Palace is high on your list, or you\u2019re visiting Peking/Tsinghua University.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Budget hotels \u00a580\u2013200/night, mid-range \u00a5250\u2013500/night. <strong>Subway:</strong> Lines 4, 10, 13, and 16 serve Haidian.</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Dongzhimen\u2013Dongsishitiao \u2014 Best Value Near the Airport Express</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The Dongzhimen area sits at the eastern edge of Dongcheng, anchored by a major transit hub where Lines 2, 13, and the Capital Airport Express converge. It\u2019s one of Beijing\u2019s best value-for-location pockets: you\u2019re one subway stop from the <a href="/attractions/lama-temple/">Lama Temple</a>, three stops from the Forbidden City, and directly connected to PEK airport in 25 minutes.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The area around Dongzhimen Station has a high concentration of mid-range business hotels that are 30\u201340% cheaper than equivalent properties in Wangfujing. Guijie Street (Ghost Street), Beijing\u2019s famous all-night dining strip, is a 5-minute walk south. If you have an early morning flight, the direct Airport Express link from Dongzhimen is worth the neighborhood choice alone \u2014 taxi to the airport takes 45\u201370 minutes; the Express takes 25.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You want a central location without central prices, easy airport access, proximity to the Lama Temple, or late-night dining options within stumbling distance.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Budget \u00a5100\u2013250/night, mid-range \u00a5300\u2013600/night. <strong>Subway:</strong> Lines 2, 5, 13, and Airport Express.</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Gulou\u2013Houhai \u2014 Best for Boutique Stays and Photography</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The area around the Drum Tower (Gulou) and Bell Tower (Zhonglou) is one of Beijing\u2019s most photogenic neighborhoods. Narrow hutong alleys, grey-brick courtyard walls, and the towers themselves silhouetted against the sky create the Beijing of postcards. This is where you stay if atmosphere is your priority.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The Gulou area has the highest concentration of boutique courtyard hotels in Beijing. Many are restored Qing Dynasty residences with 5\u201315 rooms, garden courtyards, and rooftop terraces with views of the Drum Tower. The <a href="/attractions/nanluoguxiang/">Nanluoguxiang hutong</a> is a 10-minute walk south. Houhai Lake\u2019s evening bar scene is a 5-minute walk west. The Forbidden City is three subway stops away on Line 8.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The trade-off: these boutique hotels are small and book up weeks in advance during peak seasons (April\u2013May, September\u2013October). Room sizes are typically modest \u2014 you\u2019re paying for the courtyard and atmosphere, not square footage. If the rustle of hutong life (bicycle bells at 7am, neighbors chatting in the alley) would bother you, a modern hotel in Chaoyang might suit you better.</p>
      <div class="border-l-4 border-accent pl-4 py-2 bg-accent-bg/30 rounded-r mb-4">
        <p class="text-sm text-base-700 leading-relaxed"><strong>Pick this area if:</strong> You\u2019re a photographer, a couple on a romantic trip, or a solo traveler who wants to wake up in the Beijing of your imagination rather than a generic hotel room.</p>
      </div>
      <p class="text-sm text-base-600 leading-relaxed"><strong>Price range:</strong> Courtyard boutique \u00a5300\u20131,800/night. Budget hostels \u00a580\u2013150/night. <strong>Subway:</strong> Line 8 (Shichahai Station) and Line 2 (Gulou Dajie Station).</p>
    </section>
    <section class="mb-12">
      <h2 class="text-2xl font-semibold tracking-tight mb-4">Practical Booking Tips</h2>
      <ol class="space-y-4 text-sm text-base-600">
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">1.</span><span><strong>Book through Chinese platforms for the best rates.</strong> Trip.com (English interface) has the best coverage for foreign travelers and typically beats Booking.com and Agoda on price for China hotels. For budget hotels under \u00a5300/night, Ctrip\u2019s Chinese app often has rates that aren\u2019t visible on international platforms.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">2.</span><span><strong>Check for foreigner registration.</strong> Not all hotels in China are licensed to accept foreign guests. In practice, most mid-range and above hotels in Beijing\u2019s central districts are \u2014 but ultra-budget guesthouses (under \u00a5100/night) in residential neighborhoods sometimes aren\u2019t. If booking a very cheap property, message the hotel first to confirm.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">3.</span><span><strong>Proximity to subway is more important than proximity to attractions.</strong> Beijing\u2019s subway is excellent and covers every major attraction. A hotel 5 minutes from a Line 2 or Line 1 station will serve you better than a hotel 15 minutes\u2019 walk from the Forbidden City but 25 minutes from any subway. Prioritize subway access.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">4.</span><span><strong>Peak season book ahead.</strong> During Chinese holidays \u2014 especially the first week of October (National Day) and the first week of May (Labor Day) \u2014 decent hotels across all price tiers sell out. Book at least a month ahead. Spring (April) and autumn (October\u2013November) weekends also see high demand.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">5.</span><span><strong>Hutong hotels: ask about luggage access.</strong> Some courtyard hotels sit down alleys too narrow for cars. If you\u2019re arriving with large suitcases, ask the hotel whether a taxi or ride-hail can reach their door. Good courtyard hotels will send someone to meet you at the nearest road with a cart.</span></li>
      </ol>
    </section>
    <section class="border-t border-base-200 pt-8">
      <h3 class="text-lg font-semibold mb-3">Related Guides</h3>
      <ul class="space-y-1 text-sm">
        <li><a href="/subway-guide/" class="text-accent hover:text-accent-light">Beijing Subway Guide: How to Reach Every Major Attraction</a></li>
        <li><a href="/collections/beijing-3-day-itinerary/" class="text-accent hover:text-accent-light">3 Days in Beijing: The Perfect Itinerary</a></li>
        <li><a href="/best-time/" class="text-accent hover:text-accent-light">Best Time to Visit Beijing: Month-by-Month Guide</a></li>
      </ul>
    </section>
"""

# ============================================================
# Article 2: What to Eat in Beijing
# ============================================================
body_eat = """\
    <script type="application/ld+json" set:html={`{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "${title}",
      "description": "${description}",
      "datePublished": "${date}",
      "author": { "@type": "Organization", "name": "${siteConfig.name}" },
      "publisher": { "@type": "Organization", "name": "${siteConfig.name}", "url": "${siteConfig.url}" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "${siteConfig.url}${slug}" }
    }`}></script>
    <section class="mb-10">
      <p class="text-base text-base-600 leading-relaxed mb-4">Beijing\u2019s food scene is one of the richest in the world \u2014 shaped by imperial banquets, Silk Road trade, and centuries of street-food tradition. This guide covers 15 essential dishes and snacks, from the obvious (Peking duck) to the deeply local (fermented bean juice), with specific restaurants where you can find each one done right.</p>
      <p class="text-base text-base-600 leading-relaxed mb-4">Most first-time visitors underestimate how much Beijing has to offer beyond roast duck. The city is a breakfast capital (dozens of savory crepe and pancake variations), the birthplace of Mongolian hotpot as we know it, and home to a rich Islamic Chinese culinary tradition in the Niujie (Ox Street) neighborhood. Here\u2019s where to start.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">1. Peking Duck (\u5317\u4eac\u70e4\u9e2d B\u011bij\u012bng K\u01ceoy\u0101)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The undisputed icon of Beijing cuisine. A whole duck is air-dried, glazed with maltose, and roasted in a wood-fired oven until the skin is paper-thin and crackling-crisp. It\u2019s carved tableside and served with thin pancakes, sweet bean sauce, cucumber, and scallions. The skin is the star \u2014 dip it in sugar for the traditional first bite.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Siji Minfu</em> (multiple locations, Dengshikou flagship is closest to the Forbidden City) is the locals\u2019 pick \u2014 half the price of touristy Quanjude, twice the quality. <em>Dadong</em> (Tiantan Road location near the Temple of Heaven) does a refined, less fatty version with artistic presentation. Budget: <em>Li Qun Roast Duck</em> in a hutong courtyard near Qianmen, where ducks are roasted in a traditional brick oven.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">2. Zhajiangmian (\u70b8\u9171\u9762 Zh\u00e1ji\u00e0ngmi\u00e0n)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s quintessential comfort food: thick wheat noodles topped with a rich, salty fermented soybean paste stir-fried with diced pork belly and served with a rainbow of fresh shredded vegetables (cucumber, radish, soybean sprouts). You mix everything at the table and eat it with raw garlic on the side. It\u2019s a \u00a515\u201325 meal that fills you for hours.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Haiwanju</em> on Zengguang Road in Haidian is the definitive version \u2014 the noodle-pulling happens in the front window. In Dongcheng, the zhajiangmian at <em>Old Beijing Zhajiangmian King</em> near the Lama Temple is a reliable introduction.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">3. Mongolian Hotpot (\u6dae\u7f8a\u8089 Shu\u00e0n Y\u00e1ngr\u00f2u)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Paper-thin slices of lamb swished in a bubbling copper pot of broth until just cooked, then dipped in sesame sauce. This originated in Beijing during the Yuan Dynasty when Mongol soldiers would cook mutton in their helmets over campfires. The copper pot with a central chimney is a Beijing invention. Never order hotpot for one \u2014 it\u2019s a communal meal.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Donglaishun</em> (multiple locations) is the century-old classic, founded in 1903. For a more local experience, <em>Nanmen Hotpot</em> near the Temple of Heaven gets consistently high marks. The sesame dipping sauce is non-negotiable \u2014 mix in cilantro, scallion, and a splash of the hot broth to thin it.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">4. Jianbing (\u714e\u997c Ji\u0101nb\u01d0ng)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The king of Beijing street breakfasts. A thin mung bean and grain crepe is spread on a hot griddle, cracked with an egg, sprinkled with scallions and cilantro, painted with chili and sweet bean sauce, folded around a crispy sheet of fried dough (baocui), and handed to you in a paper wrapper. Total cost: \u00a56\u201310. Total time: 90 seconds. Best eaten immediately while the baocui is still crunchy.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> Street carts near residential neighborhoods in the morning (7\u20139am). The cart outside Dongsi subway station (Line 5/6, Exit B) is legendary. Look for a line of office workers \u2014 that\u2019s your signal. Heizhima Hutong near Nanluoguxiang has a well-known stall that adds a second egg for \u00a52 extra.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">5. Dumplings (\u997a\u5b50 Ji\u01ceozi)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Northern China is dumpling country, and Beijing has its own distinct tradition. Unlike Shanghai\u2019s soup dumplings (xiaolongbao), Beijing jiaozi are larger, sturdier, and meant to be eaten in quantities of 15\u201320 per person. The classic filling is pork and Chinese cabbage, but lamb and coriander, egg and chive, and pork and fennel are equally traditional.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Xian Lao Man</em> near the Temple of Heaven is a Beijing institution \u2014 the dumplings are the size of a child\u2019s fist, boiled to order. <em>Mr. Shi\u2019s Dumplings</em> near the Drum Tower is more foreigner-friendly with an English menu and photos. For the full experience, visit a jiaozi guan (dumpling house) in any residential neighborhood and order by weight (liang) rather than piece count.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">6. Donkey Burger (\u9a74\u8089\u706b\u70e7 L\u01da r\u00f2u Hu\u01d2sh\u0101o)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Shredded braised donkey meat stuffed into a crisp, flaky flatbread \u2014 think of it as Beijing\u2019s answer to a pulled pork sandwich. The meat is lean, slightly gamey, and surprisingly tender. There\u2019s a local saying: \u201cIn heaven there is dragon meat, on earth there is donkey meat.\u201d</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Wang Pangzi</em> (Fatty Wang) has multiple locations and is the most famous chain. The original shop near Gulou Dajie is a tiny takeout window \u2014 order the \u201cchun l\u00fcrou\u201d (pure donkey meat) version for \u00a512\u201315. Eat it standing on the sidewalk like a local.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">7. Candied Hawthorn (\u51b0\u7cd6\u846b\u82a6 B\u012bngt\u00e1ng H\u00falu)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The iconic Beijing street snack: skewered hawthorn berries dipped in hardened sugar that cracks when you bite. The tartness of the hawthorn against the glassy sugar shell creates an addictive sweet-sour contrast. In winter, you\u2019ll see vendors carrying tall foam cylinders bristling with these skewers on every major street. Modern variations use strawberries or grapes, but the classic hawthorn is the one to try.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> Any street vendor in winter (November\u2013February). The best are near temple fairs during Chinese New Year and along Wangfujing Snack Street. \u00a55\u201310 per skewer. Avoid any that look melted or sticky \u2014 that means they\u2019ve been sitting too long.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">8. Mung Bean Milk (\u8c46\u6c41 D\u00f2uzh\u012b)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">A gray-green fermented drink made from mung beans, with an aroma that visiting foreigners often compare to stinky cheese or sour beer. Beijingers have been drinking it for over 300 years. The flavor is sour, slightly funky, and surprisingly refreshing once you get past the smell. It\u2019s typically served with pickled vegetables and jiaoquan (crispy fried dough rings). Honest verdict: most first-timers won\u2019t finish a bowl, but it\u2019s the most authentically Beijing thing you can consume.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Huguosi Snacks</em> on Huguosi Street in Xicheng is the historic go-to, serving douzhi since the Qing Dynasty. The classic pairing is douzhi + jiaoquan + salted pickles (\u00a58\u201312 total). Go in the morning when it\u2019s freshly made.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">9. Lamb Skewers (\u7f8a\u8089\u4e32 Y\u00e1ngr\u00f2u Chu\u00e0n)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Cumin-dusted, chili-flecked lamb grilled over charcoal on metal skewers. This is Uyghur-style street food from Xinjiang that Beijing has adopted as its own. The best versions alternate lean meat with small chunks of fat that render and baste the skewer as it cooks. Served by the handful, best eaten standing around a smoky grill with a cold Yanjing beer.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> Guijie Street after 8pm \u2014 the entire strip turns into an open-air grill festival. Any restaurant with a charcoal grill on the sidewalk and smoke billowing into the street is a good bet. For indoor dining, <em>Huajia Yiyuan</em> on Guijie serves excellent skewers. Budget \u00a53\u20135 per skewer, 10\u201315 skewers per person for a meal.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">10. Luzhu Huoshao (\u5364\u716e\u706b\u70e7 L\u01d4zh\u01d4 Hu\u01d2sh\u0101o)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">A deeply traditional Beijing breakfast: a dark, savory stew of pork offal (lung, intestine, stomach) simmered with tofu, wheat gluten, and a hard flatbread that soaks up the broth. It\u2019s topped with mashed garlic, fermented tofu, cilantro, and chili oil. Describing it makes it sound challenging; tasting it makes you understand why it has a cult following.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Beixinqiao Luzhu</em> near Beixinqiao subway station is the most famous purveyor, often with a line out the door by 8am. \u00a515\u201320 for a bowl. Go early; they often sell out by 10am.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">11. Beijing Yogurt (\u5317\u4eac\u9178\u5976 B\u011bij\u012bng Su\u0101nn\u01cei)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Served in small ceramic pots sealed with wax paper and a rubber band, Beijing yogurt is thicker and tangier than Western supermarket yogurt. It\u2019s a refreshing street snack in summer, sold from coolers outside convenience stores and from vendors in hutong alleys. Drink it straight from the pot with a straw, then return the pot.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> Any convenience store or street vendor in the hutongs. The most famous brand is <em>Sanyuan</em>. \u00a53\u20135 per pot. Look for a cooler marked \u201csu\u0101nn\u01cei\u201d (\u9178\u5976).</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">12. Mala Tang (\u9ebb\u8fa3\u70eb M\u00e1l\u00e0 T\u00e0ng)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Choose-your-own-adventure soup: grab a basket and tongs, pick from dozens of skewers of vegetables, tofu, noodles, meat, and mushrooms, then hand your basket to the cook who boils everything in a numbing-spicy Sichuan pepper broth. Your selections are slid off the skewers into a bowl of broth, topped with sesame paste and crushed peanuts. It\u2019s fast, cheap, and customizable.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Zhang Liang Mala Tang</em> (multiple locations) is the dominant chain with clean stores and visible hygiene. <em>Yang Guofu</em> is another reliable chain. Expect \u00a515\u201330 per person depending on how much meat you add.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">13. Baozi (\u5305\u5b50 B\u0101ozi)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Fluffy steamed buns filled with seasoned pork, vegetables, or sweet red bean paste. Beijing baozi are larger and breadier than the delicate xiaolongbao of Shanghai. They\u2019re the working person\u2019s breakfast \u2014 grab four or five from a steamer, dunk them in black vinegar with chili, and eat standing at the counter. Total cost: \u00a55\u201310 for a filling breakfast.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Qingfeng Baozi</em> (multiple locations) is the state-owned chain famous partly because Xi Jinping visited one branch in 2013. Pork and scallion baozi are \u00a52 each. For something more artisanal, small independent baozi shops in hutong neighborhoods are everywhere \u2014 look for the steaming bamboo baskets in the window.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">14. Imperial Court Cuisine (\u5bab\u5ef7\u83dc G\u014dngt\u00edng C\u00e0i)</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">For a splurge meal, Beijing\u2019s imperial court cuisine recreates dishes once served to the Qing emperor and his court. These restaurants operate in restored courtyard mansions and serve meticulous multi-course banquets featuring dishes like Buddha Jumps Over the Wall (a complex soup with abalone, sea cucumber, and shark fin) and elaborate pastries shaped like flowers and animals.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> <em>Bai Jia Da Yuan</em> (White Family Grand Courtyard) on Suzhou Street near the Summer Palace is set in a Qing Dynasty prince\u2019s mansion with garden pavilions for private dining. Expect \u00a5300\u2013600 per person. <em>Li Jia Cai</em> near the Forbidden City is more intimate \u2014 a family-run courtyard restaurant where the menu changes daily based on what the chef finds at market. Reservations essential for both.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">15. Niujie Muslim Cuisine</h2>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s Niujie (Ox Street) neighborhood is the historic center of the city\u2019s Hui Muslim community, with food traditions separate from mainstream Beijing cuisine. Lamb and beef dominate, pork is absent, and the spice palette (cumin, Sichuan peppercorn, star anise) is bolder. Niujie has been a food destination since the Tang Dynasty.</p>
      <p class="text-sm text-base-600 mb-4 leading-relaxed"><strong>Where to go:</strong> Start at Niujie Qingzhen Supermarket area and eat your way south. <em>Hongbin Lou</em> is the historic restaurant (founded 1853) for formal halal dining. For street food: sesame cakes stuffed with spiced beef at <em>Niujie Minzu Xiaochi</em>, and lamb chuan\u2019r grilled fresh at any stand with smoke coming from it. The neighborhood is ~20 minutes by taxi from the Forbidden City area.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-4">Quick Guide to Beijing Food Streets</h2>
      <div class="table-responsive mb-4">
      <table class="table-attractions">
        <thead><tr><th>Street</th><th>Best For</th><th>When to Go</th></tr></thead>
        <tbody>
          <tr><td>Guijie (\u7c05\u8857)</td><td>Crayfish, lamb skewers, late-night</td><td>After 8pm, any night</td></tr>
          <tr><td>Wangfujing Snack Street</td><td>Novelty snacks (scorpion on stick)</td><td>Late afternoon\u2013evening</td></tr>
          <tr><td>Niujie (\u725b\u8857)</td><td>Halal Muslim cuisine</td><td>Lunch, Friday prayers</td></tr>
          <tr><td>Huguosi Street</td><td>Traditional Beijing snacks</td><td>Breakfast\u2013lunch</td></tr>
          <tr><td>Qianmen Street</td><td>Classic restaurants, tourist-friendly</td><td>Lunch, dinner</td></tr>
          <tr><td>Sanlitun</td><td>International dining, cocktails</td><td>Dinner, weekend brunch</td></tr>
        </tbody>
      </table>
      </div>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-4">Dining Tips for First-Time Visitors</h2>
      <ol class="space-y-4 text-sm text-base-600">
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">1.</span><span><strong>Meal times are earlier than in the West.</strong> Lunch starts at 11:30am and winds down by 1:30pm. Dinner starts around 6pm and the kitchen often closes by 9pm, especially in residential neighborhoods. Guijie Street restaurants are the exception \u2014 many stay open past 2am.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">2.</span><span><strong>Cashless is the norm.</strong> WeChat Pay and Alipay dominate. Foreign cards are increasingly accepted at mid-range and above restaurants, but street food stalls and small family-run spots may be cash-only or QR-payment only. Carry some cash as backup.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">3.</span><span><strong>Sharing is the default.</strong> Chinese meals are communal. Dishes are ordered for the table and placed in the center for everyone to share. Don\u2019t order one dish per person the way you might in the West \u2014 aim for roughly the number of diners plus one dish, shared.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">4.</span><span><strong>Street food safety is generally good.</strong> Beijing\u2019s street food scene is vibrant and mostly safe. Follow the crowd \u2014 busy stalls with high turnover are the freshest. Avoid pre-cooked skewers sitting at room temperature. If a stall has a line of office workers at lunch, it\u2019s good.</span></li>
        <li class="flex items-start gap-2"><span class="text-accent font-bold mt-0.5 shrink-0">5.</span><span><strong>Don\u2019t skip the condiments.</strong> Chinese restaurant tables are covered with condiment caddies: black vinegar, soy sauce, chili oil, minced garlic. Beijingers customize every bite. Pour a small dish of black vinegar for your dumplings; add a spoon of chili oil to your noodles.</span></li>
      </ol>
    </section>
    <section class="border-t border-base-200 pt-8">
      <h3 class="text-lg font-semibold mb-3">Related Guides</h3>
      <ul class="space-y-1 text-sm">
        <li><a href="/attractions/nanluoguxiang/" class="text-accent hover:text-accent-light">Nanluoguxiang Hutong: Street Food and Shopping Guide</a></li>
        <li><a href="/collections/beijing-3-day-itinerary/" class="text-accent hover:text-accent-light">3 Days in Beijing: The Perfect Itinerary</a></li>
        <li><a href="/collections/free-beijing-attractions/" class="text-accent hover:text-accent-light">Free Beijing Attractions: Explore on a Budget</a></li>
      </ul>
    </section>
"""

# ============================================================
# Article 3: Beijing Travel Tips
# ============================================================
body_tips = """\
    <script type="application/ld+json" set:html={`{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "${title}",
      "description": "${description}",
      "datePublished": "${date}",
      "author": { "@type": "Organization", "name": "${siteConfig.name}" },
      "publisher": { "@type": "Organization", "name": "${siteConfig.name}", "url": "${siteConfig.url}" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "${siteConfig.url}${slug}" }
    }`}></script>
    <section class="mb-10">
      <p class="text-base text-base-600 leading-relaxed mb-4">Beijing rewards travelers who come prepared. It\u2019s a huge city (22 million people across 16,800 square kilometers), and the gap between a good trip and a frustrating one often comes down to knowing what to expect. These 20 tips cover the practical stuff guidebooks skip \u2014 from how the subway really works to which apps you actually need on your phone.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Before You Go</h2>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">1. Get a VPN before you leave home</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Google, Gmail, Instagram, WhatsApp, Facebook, and most Western social media are blocked in China. You need a VPN to access them. Download and test it <em>before</em> you arrive \u2014 VPN provider websites are also blocked inside China, so you can\u2019t install one after landing. ExpressVPN and Astrill have the best track records for reliability on Chinese networks. NordVPN and ProtonVPN often struggle. Pay for at least one month of service and confirm it\u2019s working before your flight.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">2. Install Alipay or WeChat for payments</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">China is nearly cashless. From street food carts to major museums, QR-code payments are the default. Alipay now supports international credit cards (Visa, Mastercard) and has an English interface. Download it before arriving, link your card, and verify your identity. WeChat Pay also works but requires more setup. Carry \u00a5200\u2013300 in cash as backup, but you\u2019ll use it less than you expect.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">3. Book attraction tickets in advance</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The Forbidden City, National Museum, and several other major attractions no longer sell tickets at the gate. You must reserve online, sometimes days in advance, with your passport number. For the <a href="/attractions/forbidden-city/">Forbidden City</a>, reservations open 7 days ahead and sell out within hours during peak seasons. Book as early as possible through the official WeChat mini-programs or your hotel concierge.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">4. Carry your passport everywhere</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Chinese law requires foreigners to carry their passport at all times. You\u2019ll need it to enter attractions (even those you\u2019ve pre-booked), check into hotels, and occasionally for random security checks in subway stations. A photo on your phone is not sufficient. Keep the physical passport with you. A photocopy in your luggage is a good backup.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">5. Learn five Mandarin phrases</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">English is not widely spoken outside hotels and major attractions. Learning a handful of phrases goes far: <em>n\u01d0 h\u01ceo</em> (hello), <em>xi\u00e8 xie</em> (thank you), <em>du\u00ec bu q\u01d0</em> (sorry/excuse me), <em>zh\u00e8 ge</em> (this one, while pointing at a menu), and <em>du\u014d sh\u01ceo qi\u00e1n?</em> (how much?). Download Pleco, the best Chinese-English dictionary app \u2014 it works offline and has optical character recognition that translates menus through your phone camera.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Getting Around</h2>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">6. The subway is your best friend</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijing\u2019s subway is clean, safe, air-conditioned, and covers virtually every attraction. It\u2019s also extremely cheap \u2014 \u00a53\u20139 per ride depending on distance. All signs and announcements are bilingual (Chinese/English). Rush hour (7:30\u20139am, 5:30\u20137pm) on Lines 1, 10, and 13 can be crushingly crowded \u2014 plan sightseeing outside these windows or accept the squeeze as part of the experience. For detailed routes to every attraction, see our <a href="/subway-guide/">Beijing Subway Guide</a>.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">7. Get a transportation card or use Alipay for transit</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The Yikatong card (\u00a520 deposit, refundable) works on all subways and buses. Buy it at any subway station service window. Alternatively, Alipay\u2019s Transport function now supports Beijing subway and bus QR payments with international cards \u2014 this is simpler if you already have Alipay set up.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">8. Ride-hailing: Didi is your only real option</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Uber doesn\u2019t operate in China. Didi is the dominant ride-hailing app and now has an English interface accessible through the Alipay app (look for the Didi Ride Hailing mini-program). Taxis are abundant but drivers rarely speak English \u2014 have your destination written in Chinese characters. Fares are reasonable: expect \u00a530\u201360 for most trips within the central districts.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">9. Bikeshare: the best way to explore hutongs</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Blue (Hello), yellow (Meituan), and green (Didi) bikeshare bikes are everywhere. Scan the QR code with Alipay or WeChat to unlock. Rides cost \u00a51.50 for 30 minutes. Biking through the hutong alleys of Dongcheng and Xicheng on a weekday morning, before the crowds arrive, is one of the best Beijing experiences. Stick to the narrow lanes; avoid major roads where cars and electric scooters can be chaotic.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">At the Attractions</h2>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">10. Arrive early \u2014 really early</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Tour buses start unloading at major attractions around 9:30am. If you arrive when gates open (usually 8am or 8:30am), you get 60\u201390 minutes of relative peace. This is especially critical for the <a href="/attractions/great-wall-badaling/">Great Wall at Badaling</a>, which becomes a human river by 10am, and the <a href="/attractions/great-wall-mutianyu/">Mutianyu section</a>, where the cable car line can hit 45 minutes by late morning. At the Forbidden City, early entry means you can photograph the empty courtyards before the tour-group flags appear.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">11. Monday is museum closure day</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Nearly all Beijing museums, including the Forbidden City (Palace Museum) and National Museum of China, are closed on Mondays. Plan your itinerary around this. Parks, temples, and the Great Wall remain open. Monday is a good day for outdoor attractions: the <a href="/attractions/summer-palace/">Summer Palace</a>, <a href="/attractions/jingshan-park/">Jingshan Park</a>, or a Great Wall trip.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">12. Bring your own toilet paper</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Public restrooms at tourist sites are generally clean but rarely stocked with toilet paper or soap. Carry a small pack of tissues and hand sanitizer. Western-style toilets are available at major international hotels and high-end malls; most public restrooms are squat toilets. At the Great Wall, restrooms are available at the entrance but not on the Wall itself.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">13. Expect security checks everywhere</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Bag X-ray and metal detectors are standard at subway stations, museums, Tiananmen Square, and major parks. They\u2019re quick (usually under 2 minutes) but constant. Travel light. Pocket knives, large scissors, and aerosol sprays will be confiscated at subway security. Tiananmen Square has the strictest checks \u2014 expect to show your passport.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Weather and Seasons</h2>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">14. Spring and autumn are the sweet spots</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">April\u2013May and September\u2013October offer the best weather: comfortable temperatures (15\u201325\u00b0C), clear skies, and manageable crowds outside of Chinese holidays. Late October is the peak autumn foliage window, especially at the Great Wall and Fragrant Hills Park. For a full seasonal breakdown, see our <a href="/best-time/">Best Time to Visit Beijing</a> guide.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">15. Avoid national holidays if you can</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The first week of October (National Day Golden Week) and the first week of May (Labor Day) bring domestic tourism to a standstill. Attractions are packed beyond capacity, hotels triple in price, and train tickets sell out. Chinese New Year (late January/early February) is quieter \u2014 Beijing empties out as residents return to their hometowns \u2014 but many small restaurants close and some attractions run reduced hours. Check the lunar calendar before booking.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">16. Winter has a silver lining</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">December\u2013February temperatures drop to -10\u00b0C (14\u00b0F), but crowds disappear and hotel prices drop 40\u201360%. The Forbidden City under snow is breathtaking, and you might have the Great Wall nearly to yourself. Frozen lakes in Shichahai become ice-skating rinks. Dress in layers, bring thermal underwear, and pack a warm hat \u2014 Beijing winter wind is biting. The payoff is a Beijing without crowds.</p>
    </section>
    <section class="mb-10">
      <h2 class="text-2xl font-semibold tracking-tight mb-2">Culture and Etiquette</h2>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">17. Queueing is... different</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">The Western concept of orderly lines doesn\u2019t always apply, especially at busy subway stations and food stalls. People push forward. Don\u2019t take it personally. Assert yourself politely but firmly \u2014 standing passively at the back of a loose crowd will mean you never get served. At the same time, aggressive shoving back is considered worse than the initial push. Find the balance between passive and aggressive.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">18. Tipping is not expected</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">There is no tipping culture in China. Restaurants, taxis, hotel staff, and tour guides do not expect tips. In high-end international hotels and very touristy restaurants, a service charge may be added to the bill \u2014 this replaces tipping. Leaving cash on the table will likely be chased after you by a confused waiter trying to return your change.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">19. Photographing people: ask first</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Beijingers are generally tolerant of photography, but pointing a camera at someone\u2019s face without permission is rude, same as anywhere. At temple fairs and in the hutongs, older residents in traditional dress are used to being photographed \u2014 a smile and a gesture toward your camera usually gets a nod or a wave. At temples, avoid photographing worshippers mid-prayer. Military installations and police stations: do not photograph them at all.</p>
      <h3 class="text-lg font-medium text-base-800 mt-6 mb-2">20. Drinking water: don\u2019t drink from the tap</h3>
      <p class="text-sm text-base-600 mb-4 leading-relaxed">Tap water is not potable in Beijing. Hotels provide bottled water or electric kettles for boiling. Convenience stores sell 1.5L bottles for \u00a52\u20133. Most restaurants serve boiled water or tea. Many Beijingers carry a thermos of hot water \u2014 it\u2019s a cultural habit, not just a safety precaution. If your hotel room has a kettle, boil water for 3 minutes and let it cool for drinking.</p>
    </section>
    <section class="border-t border-base-200 pt-8">
      <h3 class="text-lg font-semibold mb-3">Related Guides</h3>
      <ul class="space-y-1 text-sm">
        <li><a href="/subway-guide/" class="text-accent hover:text-accent-light">Beijing Subway Guide: How to Reach Every Major Attraction</a></li>
        <li><a href="/best-time/" class="text-accent hover:text-accent-light">Best Time to Visit Beijing: Month-by-Month Guide</a></li>
        <li><a href="/faq/" class="text-accent hover:text-accent-light">Beijing Travel FAQ: Answers to Common Questions</a></li>
        <li><a href="/collections/beijing-3-day-itinerary/" class="text-accent hover:text-accent-light">3 Days in Beijing: The Perfect Itinerary</a></li>
        <li><a href="/blog/where-to-stay-in-beijing/" class="text-accent hover:text-accent-light">Where to Stay in Beijing: Best Areas for Tourists</a></li>
      </ul>
    </section>
"""

# ============================================================
# Generate all files
# ============================================================
print("Generating blog articles...")

write("where-to-stay-in-beijing.astro", "where-to-stay-in-beijing",
      "Where to Stay in Beijing: Best Areas for Tourists [2026]",
      "Choose the best neighborhood in Beijing for your trip. Compare Dongcheng, Xicheng, Chaoyang, Haidian, and more \u2014 with recommendations keyed to attractions, budget, and travel style.",
      body_stay)

write("what-to-eat-in-beijing.astro", "what-to-eat-in-beijing",
      "What to Eat in Beijing: 15 Must-Try Dishes and Where to Find Them [2026]",
      "From Peking duck to street-side jianbing: discover 15 essential Beijing dishes with specific restaurant recommendations, price ranges, and neighborhood guides for every budget.",
      body_eat)

write("beijing-travel-tips.astro", "beijing-travel-tips",
      "Beijing Travel Tips: 20 Things to Know Before You Go [2026]",
      "Essential Beijing travel tips for first-time visitors: VPN setup, subway navigation, attraction booking, cultural etiquette, and practical advice that guidebooks skip.",
      body_tips)

print("\nDone! 3 blog articles created.")
