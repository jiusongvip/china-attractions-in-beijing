export interface AttractionExtras {
  whyVisit: string[];
  whatToExpect: string[];
  visitPlan: string[];
  goodToKnow: string[];
  faq: { q: string; a: string }[];
}

export const attractionExtras: Record<string, AttractionExtras> = {
  "forbidden-city": {
    whyVisit: [
      "The Forbidden City is the single most important architectural complex in China and the world's largest palace: 180 acres, nearly a thousand buildings, and home to 24 emperors across the Ming and Qing dynasties. No other site in Beijing connects you so directly to imperial China's power, art, and ritual — the same stones that emperors walked for 500 years are the ones beneath your feet.",
      "It also anchors the city. Everything else in Beijing — the central axis, the museums, the gate, the surrounding hutongs — makes more sense once you have walked the palace's courtyards. For most visitors it is the reason the trip exists."
    ],
    whatToExpect: [
      "Entering the Forbidden City is the closest thing Beijing has to walking into a time machine. The Meridian Gate, the southern entrance you will almost certainly use, towers 35 meters high with the double-eaved roof that became the visual shorthand for China. Once through the gate, the first courtyard alone is bigger than most European town squares — expect a brief 'wait, this is all palace?' moment before the sheer scale settles in.",
      "The palace is laid out on a strict north-south axis: grand ceremonial halls up front, imperial residence and gardens at the rear. Most visitors follow the central spine — three great halls, then the inner court — but that central line is also where the tour groups concentrate. The eastern and western wings, which hold the treasure galleries, ceramics collections, and quiet courtyards, are where the experience shifts from a crowd shuffle to something closer to contemplation.",
      "Give yourself permission to wander off the main line. The Hall of Clocks, tucked in the eastern section, holds an extraordinary collection of mechanical timepieces gifted by European courts; the Nine Dragon Wall at the far eastern edge is a ceramic masterpiece most visitors never see because they exit straight through the back gate. These peripheral halls also tend to be dramatically quieter — on a busy holiday you can still find ten-minute stretches alone in front of a Ming bronze.",
      "The architecture rewards attention to detail. Notice the threshold stones carved with clouds and dragons under each gate, the bronze incense burners in front of the main halls, and the roof decorations — each extra mythical beast on a ridge signals a more important building. The Hall of Supreme Harmony, the tallest hall of all, sits on a three-tiered marble platform ringed by 18 bronze vessels, and its 72 golden columns were once the tallest building in Beijing by decree — no one was allowed to build higher.",
      "Expect a half-day rather than a quick stop. A focused walk of the central axis plus one or two side galleries takes three to four hours at a comfortable pace. Add the Treasure Gallery, the eastern section, or the rooftop-facing Jingshan climb after you exit the north gate, and the palace becomes a full day anchored around one of the world's great buildings."
    ],
    visitPlan: [
      "Arrive through the east gate (Donghuamen) at opening to skip the Meridian Gate bottleneck.",
      "Walk the central axis north from the Gate of Supreme Harmony through the three great halls.",
      "Detour east to the Treasure Gallery and Hall of Clocks before the tour groups reach them.",
      "Wander the western wing's quiet courtyards and ceramics halls if time allows.",
      "End at the Imperial Garden, then exit north into Jingshan Park for the rooftop panorama."
    ],
    goodToKnow: [
      "Tickets must be booked online 7 days ahead with your passport number — there is no on-site ticket counter.",
      "Wear shoes you can walk 4+ hours in; the palace is roughly 180 acres of courtyards and stone paths.",
      "Wheelchairs and stroller rental are free at the Meridian Gate security area.",
      "Weekday afternoons are dramatically quieter than weekend mornings — the 2pm sweet spot rewards patient visitors.",
      "Audio guides and English signage cover the main halls; the side galleries have lighter labeling."
    ],
    faq: [
      { q: "How far in advance should I book Forbidden City tickets?", a: "Book 7 days ahead when slots open at 8am Beijing time. Peak season (May, Oct, holidays) sells out in minutes, so set a reminder. You will need your passport number and a China mobile number." },
      { q: "How long does it take to see the Forbidden City?", a: "A central-axis walk with one side gallery takes 3-4 hours. Seeing the Treasure Gallery, ceramics, and quiet courtyards comfortably fills a full morning." },
      { q: "Which entrance is least crowded?", a: "The east gate (Donghuamen) sees far fewer visitors than the main Meridian Gate. Entering there drops you straight into the quieter eastern halls, and you can work south or north at your own pace." },
      { q: "Is the Forbidden City worth visiting with kids?", a: "Yes — children under 18 enter free (book a zero-price ticket), strollers are allowed, and the wide courtyards give kids room to run. Bring snacks; the palace has limited food options inside." }
    ]
  },

  "great-wall-badaling": {
    whyVisit: [
      "Badaling is the Great Wall as it exists in the world's collective imagination — the wide, battle-tested ramparts and receding watchtowers you have seen in films and photographs. It is also the section every foreign head of state visits, which tells you it delivers the defining Chinese experience reliably.",
      "The combination of iconic scenery, straightforward transport, and the free museum at the base makes it the most complete Great Wall day trip for first-time visitors — even with the crowds, the 'I'm on the Great Wall' moment is unmistakable here."
    ],
    whatToExpect: [
      "Badaling is the Great Wall in its most theatrical form. The wall here rises over steep, bare mountainsides with watchtowers receding into the distance — the image you have seen in a thousand travel posters is this exact stretch. The Wall is also at its most commercial here, which is the price you pay for that perfect postcard.",
      "The experience splits cleanly into two. South of the entrance, the wall climbs to a single restored tower with pleasant views — the easy route. North is where the real Badaling lives: tower after tower connected by broad ramps and occasional steep steps, wide enough in places for five people abreast. The climb to Tower 8, the highest point open to tourists, is genuinely rewarding, and the crowds thin noticeably the further you push.",
      "The cable car saves the steepest 700 meters and is worth it for anyone with mobility concerns or limited time. Purists prefer the walk from the entrance, but both routes end at the same ridgeline — how you get there matters less than being there early. Arrive at the 8am gate opening and you will walk nearly empty ramps; by 10am the first tour buses disgorge.",
      "The Wall here is also a piece of living engineering history. Built and reinforced across the Ming Dynasty (1368-1644), Badaling guarded the Juyongguan Pass, the most direct approach to Beijing from the northern steppe. The watchtowers you can climb were once garrison posts; the beacon platforms along the ridge were part of a smoke-signal relay network that could raise the alarm to the capital in a single day.",
      "Round out the visit with the Great Wall Museum at the base — free, well-curated, and the best 30 minutes you will spend explaining how this colossal structure was built, garrisoned, and maintained. A morning on the wall plus the museum makes a satisfying, complete half-day."
    ],
    visitPlan: [
      "Take the S2 train from Beijing North at 6:12am for the scenic ride and an 8am arrival.",
      "Skip the south side entirely; head north and climb past Tower 4 where most visitors turn back.",
      "Pause at Tower 8 for the classic panorama and the Wall museum at the base.",
      "Be at the shuttle bus by 1pm if you want to avoid the return crowd peak."
    ],
    goodToKnow: [
      "The entrance fee is CNY 40 with the cable car as an optional extra.",
      "The official Great Wall Museum at the base is free and a smart use of 30 minutes.",
      "In winter the bare mountains are dramatic and almost empty — bring spikes for icy steps.",
      "Restrooms are at the base and at Tower 8 only; plan accordingly on the wall.",
      "The S2 train runs a limited schedule — check the timetable the night before and queue early."
    ],
    faq: [
      { q: "How do I get to Badaling from Beijing?", a: "The scenic S2 train from Beijing North Station (about 1 hour, CNY 6) or Bus 877 from Deshengmen (90 minutes, CNY 12) are the cheap, direct options. Private drivers cost roughly CNY 500-700 round trip." },
      { q: "Is Badaling the Great Wall section in photos?", a: "Yes — the wide, heavily restored ramps and receding watchtowers in most Great Wall travel photos are Badaling. It is the classic 'postcard wall'." },
      { q: "Is Badaling too crowded to enjoy?", a: "Crowds peak 10am-2pm with tour groups. Arriving for the 8am opening or visiting on a weekday gives you the postcard views without the shoulder-to-shoulder shuffle. The northern towers past Tower 4 stay relatively clear even at peak." },
      { q: "Can I do Badaling with the cable car and how long does it take?", a: "Yes — the cable car runs from the base to near Tower 4 and costs about CNY 100 one-way or 140 round trip. With the cable car both ways, budget 3-4 hours total; walking both ways adds 1-2 hours." }
    ]
  },

  "great-wall-mutianyu": {
    whyVisit: [
      "Mutianyu is the Great Wall experience most people imagine but rarely find: the Wall winding through forest, watchtowers close enough to make the walk a series of satisfying mini-destinations, and genuine quiet stretches even at peak season.",
      "Add the toboggan slide — a 1,580-meter ride down through the treeline that has no equivalent on any other section — and Mutianyu turns a once-in-a-lifetime monument into an afternoon people still talk about years later. For families especially, it is the friendliest Great Wall there is."
    ],
    whatToExpect: [
      "Mutianyu is the Great Wall for people who want the grandeur without the theme-park atmosphere. The Wall here runs through dense forest that erupts into gold and crimson every October, and the 23 closely-spaced watchtowers create a rhythm of climb, rest, view — far more forgiving than Badaling's long, unbroken ascents.",
      "The standard route is the loop: cable car or chairlift up to Tower 14, walk west toward Tower 1 (or east from Tower 19 if you ride the other lift), then the toboggan or chairlift down. Tower 14 to Tower 19 is the gentlest, best-viewed section, and even on a busy Saturday you will find stretches where it is just you and the wall disappearing into the treeline.",
      "The toboggan slide is the experience that separates Mutianyu from every other section. A 1,580-meter steel chute through the forest, it is faster than you expect and grins you all the way down. Kids ride tandem with parents; adults of all ages queue for a second go.",
      "History buffs get a bonus here: Mutianyu predates Badaling. The original wall was built in the Northern Qi Dynasty (550-577 CE) and reinforced by Ming general Xu Da in 1368. Because it guarded the imperial Ming tombs to the south, the watchtowers were built unusually dense — 23 towers over just 2.25 kilometers — and several retain original battlements and the arrow-slit windows that later restorations elsewhere smoothed away.",
      "Getting to Mutianyu is slightly more effort than Badaling — it is why the crowds stay moderate. The reward is a wall that feels more like a hike and less like a sightseeing ride: quieter ramps, forest-framed views, and that toboggan finish that makes the trip memorable for every age."
    ],
    visitPlan: [
      "Bus 916 Express to Huairou, then a local taxi to the entrance gate (90-120 minutes total).",
      "Cable car up to Tower 14 and walk east toward Tower 19 for the gentlest ridge line.",
      "Turn back at Tower 19 and descend by toboggan from Tower 6 if you walk the full length.",
      "Finish with lunch at a farmhouse restaurant before the 2pm bus departure."
    ],
    goodToKnow: [
      "Combined entrance + cable car + toboggan runs about CNY 180 per adult.",
      "The wall here is 2.25km with 23 towers — a full exploration takes 4-5 hours.",
      "Autumn (late Oct to early Nov) is peak foliage; book the day's entry online.",
      "There are no restaurants on the wall — the farmhouse village at the base is the spot to eat.",
      "Chairlift up + toboggan down is the most popular combo; the cable car is better in rain or wind."
    ],
    faq: [
      { q: "Mutianyu or Badaling — which should I pick?", a: "Mutianyu for families, photographers, and anyone who dislikes crowds — it has gentler slopes, forest views, and the toboggan. Badaling for the classic postcard scene, easiest transport, and the S2 train. See our full Badaling vs Mutianyu comparison." },
      { q: "How do I get to Mutianyu by public transport?", a: "Take Bus 916 Express from Dongzhimen to Huairou (about 1 hour), then a local taxi the last 20 minutes to the gate. Private cars and hotel shuttles run about CNY 600-800 round trip." },
      { q: "How long should I allow for Mutianyu?", a: "A full day, door to door. On the wall itself, the loop (cable car up, walk, toboggan down) takes 3-4 hours; lingering on the towers and adding a farmhouse lunch easily extends it." },
      { q: "Is the toboggan slide safe for kids?", a: "Yes — children ride tandem with a parent, and the sled has simple brake levers. Minimum solo-rider age is around 12; younger kids pair with an adult. It is one of the most family-friendly things on the Great Wall." }
    ]
  },

  "temple-of-heaven": {
    whyVisit: [
      "The Temple of Heaven is Beijing's architectural icon — the circular Hall of Prayer for Good Harvests on its marble terrace is the symbol that appears on everything from postcards to the national badge. No other structure in the city so purely distills the ancient Chinese worldview of a round heaven over a square earth.",
      "It is also the one major monument where locals genuinely outnumber tourists — the dawn ritual of tai chi, opera, and kite-flying makes it the most alive, most human site in Beijing, and the only place you can see imperial architecture and daily Beijing life in the same frame."
    ],
    whatToExpect: [
      "The Temple of Heaven is two experiences in one park, and the one you remember will likely be the one you did not plan for. By day it is a UNESCO monument: the circular Hall of Prayer for Good Harvests rising from a three-tiered marble terrace, blue tiles glowing against the sky — the architectural symbol of Beijing itself.",
      "But arrive before 8am and the park transforms. This is the Temple of Heaven the locals know: hundreds of residents practicing tai chi in slow-motion clusters, couples dancing to waltzes under the cypresses, women in red scarves singing opera arias, badminton shuttlecocks arcing over the gravel paths. The monuments become a backdrop to a living city ritual that has played out here every morning for generations.",
      "The site is laid out in a perfect square-within-circle geometry — square wall, circular altar, representing the ancient Chinese belief that earth is square and heaven round. The Echo Wall encircling the Circular Mound Altar is a genuine acoustic marvel; whisper against the wall and someone 60 meters away hears you clearly. Stand on the central stone of the Circular Mound Altar and your voice noticeably amplifies — the emperors' prayers were literally designed to carry.",
      "The architecture is numerology made visible. The Hall of Prayer is 36 meters high and built without a single nail, its three roof rings and blue tiles symbolizing heaven; the four inner columns represent the four seasons, the twelve outer columns the months, and the outer ring the twelve double-hours of the day. It is one of the most mathematically deliberate buildings in China.",
      "The park itself is Beijing's largest open green space in the old city, a 273-hectare cypress forest where locals come year-round — to practice calligraphy with water on the paving stones in summer, to fly kites and play chess on mild weekends, and to celebrate the January ice festival when it arrives."
    ],
    visitPlan: [
      "Enter at Tiantan Dongmen for the shortest walk to the Hall of Prayer.",
      "Walk the northern axis through the Hall of Prayer before the 10am tour wave.",
      "Descend south through the Echo Wall and Circular Mound Altar.",
      "Finish by walking the park's west side, where the morning locals gather."
    ],
    goodToKnow: [
      "Buy the combined through ticket (CNY 15) — the park-only ticket excludes the Hall of Prayer and Echo Wall.",
      "The park opens at 6am; monuments open at 8am. Morning tai chi happens regardless.",
      "The Danbi Bridge walkway is the 360-meter sacred road emperors once used — walk the center path.",
      "June to August is lush and hot; winter is stark and cold but nearly empty.",
      "Hongqiao Market and its pearl stalls are a 10-minute walk south for a combined outing."
    ],
    faq: [
      { q: "What time should I visit the Temple of Heaven?", a: "Arrive before 8am to see the monuments open with the locals' tai chi and opera practice. If you want the Hall of Prayer without crowds, be at the ticket gate by opening — the tour wave starts around 10am." },
      { q: "Which ticket do I need to see the Hall of Prayer?", a: "The combined through ticket (CNY 15 in peak season) covers the Hall of Prayer, Echo Wall, and Circular Mound Altar. The park-only ticket (CNY 10) admits you to the grounds but not the monuments." },
      { q: "How does the Echo Wall work?", a: "The round wall's smooth surface carries whispers along its curve — speak quietly against the wall on one side and a friend at the far point hears you clearly. It is a practical demonstration of the circular geometry that makes the site famous." },
      { q: "Is the Temple of Heaven good with kids?", a: "Very — the park is vast and open for running, the acoustics of the Echo Wall and Circular Mound delight children, and early-morning kite-flying and tai chi are fascinating to watch. Allow 2-3 hours and bring water in summer." }
    ]
  },

  "summer-palace": {
    whyVisit: [
      "The Summer Palace is China's greatest imperial garden and the most beautiful open space in Beijing — 290 hectares of lake, hill, and painted corridor assembled on a scale that makes you feel the Qing court's wealth with every step.",
      "Where the Forbidden City impresses with power, the Summer Palace seduces with pleasure: boat rides on Kunming Lake, the world's longest painted corridor, and the marble boat of Empress Dowager Cixi's rebuilding. It is the most romantic, most relaxing of Beijing's World Heritage sites — and the best escape when the city heat builds."
    ],
    whatToExpect: [
      "The Summer Palace is the largest imperial garden in China, and the first view of Kunming Lake explains why the Qing emperors chose this spot to escape Beijing's summer heat. The lake — a third of the park's 290 hectares — sits in a natural basin with Longevity Hill rising from its northern shore, crowned by the Tower of Buddhist Incense.",
      "The classic walk hugs the lake's north shore. The Long Corridor, 728 meters of painted wooden galleries running from the East Palace Gate toward the Marble Boat, contains over 14,000 individual paintings — scenes from classical novels, flowers, birds, and landscapes — and is the world's longest painted corridor. Each beam is a small artwork; budget time to actually look up.",
      "The defining Summer Palace moment, though, is the boat ride. Rent a dragon-painted pedal boat or join a lake cruise, and the whole composition reassembles itself from the water: the hill, the temple, the Seventeen-Arch Bridge arcing toward South Lake Island. The park rewards slow movement and lake-light.",
      "Behind the beauty is a dramatic rebuilding story. The Summer Palace was destroyed and rebuilt twice — first by Anglo-French forces in 1860, then again during the Boxer Rebellion of 1900. Empress Dowager Cixi oversaw the second reconstruction in the 1880s, and her decisions shaped what you see: the Marble Boat, a stone 'warship' pavilion built (critics joked) with funds diverted from the navy, and the 17-meter Tower of Buddhist Incense, the park's sacred heart.",
      "Climb Longevity Hill from the rear to reach the Tower of Buddhist Incense's courtyard, then descend the other side for a panorama over the lake and the Seventeen-Arch Bridge. The hill's back slope is far quieter than the lakeside and offers some of the best photo angles in the park."
    ],
    visitPlan: [
      "Enter via the South Gate to arrive directly at Kunming Lake, away from the tour-bus East Gate.",
      "Follow the lakeshore clockwise: Seventeen-Arch Bridge, then the Long Corridor.",
      "Climb Longevity Hill from the rear to the Tower of Buddhist Incense.",
      "End at the Marble Boat and take a lake cruise back toward the East Gate."
    ],
    goodToKnow: [
      "The combined ticket (CNY 30) covers the Long Corridor, Tower of Buddhist Incense, and the big temple.",
      "The park is enormous — a full loop on foot takes 4+ hours; the lake cruise is the shortcut.",
      "Spring magnolias (late March-April) are a highlight; the lakeside willows green up first.",
      "Suzhou Street, a replica Qing shopping street inside the park, is free with the combined ticket.",
      "Lake cruises between piers run every 20-30 minutes and cost about CNY 30 per leg."
    ],
    faq: [
      { q: "How long do I need at the Summer Palace?", a: "Three to four hours covers the Long Corridor, Longevity Hill, and a lake cruise. A full loop on foot with stops is closer to five. It is a half-day attraction — pair it with a relaxed lunch or the nearby Old Summer Palace ruins." },
      { q: "Which entrance should I use?", a: "The South Gate lands you directly at Kunming Lake and avoids the tour-bus crowds at the East Palace Gate. The East Gate is the classic entrance but the busiest." },
      { q: "Is the Marble Boat worth seeing?", a: "Yes, briefly — it is the park's most famous surviving symbol of Empress Dowager Cixi's rebuilding and makes a great photo. The real highlights are the Long Corridor and the Tower of Buddhist Incense." },
      { q: "Can I take a boat on Kunming Lake?", a: "Yes — pedal boats and electric boats rent by the lakeshore in summer, and scheduled lake cruises connect the main piers year-round (weather permitting). Winter freezes the lake into a skating rink." }
    ]
  },

  "tiananmen-square": {
    whyVisit: [
      "Tiananmen Square is the symbolic heart of modern China — the vast, flag-flying stage around which the country's most important institutions and ceremonies are arranged. Standing in the middle of the world's largest public square is a genuinely humbling experience of scale and national identity.",
      "The dawn flag-raising ceremony, when the square goes silent to a 46-second anthem, is one of Beijing's most moving free experiences — a daily ritual that connects the modern nation to its imperial axis. No other site in the city explains contemporary China's relationship to its past as directly."
    ],
    whatToExpect: [
      "Tiananmen Square is less a monument than a stage for modern China, and its 440,000 square meters feel even larger in person than the numbers suggest. You stand in the middle and every direction holds a structure of national weight: the red-walled Gate of Heavenly Peace to the north, the Great Hall of the People to the west, the National Museum to the east, the Monument to the People's Heroes at the center.",
      "The single experience that elevates a visit is the flag ceremony. At dawn, the national flag is raised to a 46-second anthem precisely timed to sunrise; crowds gather an hour early at the security gates, and the moment the guard marches out with the flag, the square goes silent. Sunset's flag-lowering is nearly identical with a fraction of the crowd.",
      "Be prepared for the process, not just the place. Every entrance funnels through security with a passport check, bags are X-rayed, and the square is cleared for the October 1 National Day parade rehearsals each September. The square is best treated as a deliberate, ceremonial stop — not a casual stroll.",
      "The square's scale is its message. Laid out in its current form in 1958 and expanded to hold over a million people, it sits at the northern end of Beijing's central axis, the world's longest urban spine, running 7.8 kilometers from the Bell Tower in the north to Yongding Gate in the south. The Forbidden City and its 600-year-old gate form the square's backdrop, bridging imperial and modern China in a single view.",
      "Plan the square as the anchor of a morning: the flag ceremony at dawn, the square itself, then the National Museum on its eastern edge, followed by lunch in Dashilan to the south. It is a tight, walkable cluster of Beijing's most significant public sites."
    ],
    visitPlan: [
      "Arrive by 4:30am in summer (later in winter) for the 6am flag-raising.",
      "Walk the center line toward the Monument to the People's Heroes.",
      "Circle west past the Great Hall of the People to Qianmen Gate on the south side.",
      "Exit south into Dashilan for the old commercial street and lunch."
    ],
    goodToKnow: [
      "Entry is free but passport is mandatory at security — no exceptions.",
      "The square closes for several days around National Day (Oct 1) for parade rehearsals.",
      "Bring minimal baggage — the X-ray lines move faster without a suitcase-sized bag.",
      "The nearest subway is Tiananmen East (Line 1); the square is a 2-minute walk.",
      "Combine with the National Museum (east edge) or the Forbidden City (north gate) in the same day."
    ],
    faq: [
      { q: "Do I need a ticket to enter Tiananmen Square?", a: "No — the square is free. You only need your passport for the security screening at each entrance. Certain state functions and holiday rehearsals close it without notice, so check before you go." },
      { q: "What time is the flag ceremony?", a: "The flag is raised at sunrise, between about 5am in June and 7:30am in January, to a precise schedule published each month. Arrive 45-60 minutes early in summer to pass security and get a viewing spot." },
      { q: "How long should I spend at the square?", a: "Forty-five minutes to an hour covers the walk and photos. A full morning pairs the flag ceremony, the square, and the National Museum (allow 2+ hours there)." },
      { q: "Is there a subway stop right at the square?", a: "Yes — Tiananmen East and Tiananmen West on Line 1 both open directly onto the square's edges. The stations close without warning during events, so have a backup plan on Line 2 (Qianmen)." }
    ]
  },

  "lama-temple": {
    whyVisit: [
      "The Lama Temple is Beijing's most atmospheric religious site — a working Tibetan Buddhist lamasery where incense smoke, chanting, and maroon-robed monks create an experience no museum-style temple can replicate. The 18-meter sandalwood Maitreya Buddha, carved from a single tree, is among the most extraordinary objects in China.",
      "Compact, reverent, and unlike anything else on this list, it is the place visitors consistently describe as 'the surprise of the trip' — a 90-minute immersion in living faith that feels a world away from the crowds of the palace and the square."
    ],
    whatToExpect: [
      "The Lama Temple is the most active, most atmospheric temple complex in Beijing — and the least museum-like. Smoke from stick incense curls through five courtyards in succession, each hall denser with devotion than the last, and the ritual has not stopped since the Yongzheng Emperor's former residence was converted to a lamasery in 1744.",
      "The finale is the Pavilion of Ten Thousand Happinesses, which houses the 18-meter-tall Maitreya Buddha carved from a single sandalwood tree — the largest such statue in the world. The tree was brought from Nepal in the 18th century; standing beneath the statue's serene face, looking up 18 meters of single wood, is the kind of encounter no photograph prepares you for.",
      "Come with eyes open to the rituals. You will see visitors light three incense sticks, hold them above their heads, and bow three times toward each direction of the compass. Lamas in maroon robes walk the courtyards between prayers. This is not a performance for tourists — it is a working temple, and that authenticity is precisely the draw.",
      "The temple is a lesson in Tibetan Buddhist art. From the ornate, multi-layered Hall of the Wheel of Law with its giant prayer wheel to the gilt-roofed halls roofed with friezes of Sanskrit mantras, the details reward slow looking. The centerpiece buildings follow a strict north-south sequence, each courtyard a step deeper into the Tibetan-Buddhist tradition the Qing emperors patronized as a diplomatic bridge to their Tibetan and Mongolian territories.",
      "A visit threads the whole experience into one flowing walk — five halls, one main axis, about 90 minutes — then spills you out into the Guijie (Ghost Street) restaurant district for a well-earned meal. It is compact, reverent, and unlike any other site in Beijing."
    ],
    visitPlan: [
      "Enter through the front gate and work north through all five halls in sequence.",
      "Pause in the Hall of the Wheel of Law for the giant sandalwood prayer wheel.",
      "Reach the Pavilion of Ten Thousand Happinesses for the Maitreya Buddha.",
      "Return via the western courtyard, where the incense and light make the best photographs."
    ],
    goodToKnow: [
      "Entry is CNY 25 and includes a free bundle of incense at the ticket window.",
      "Visit on a weekday afternoon — mornings bring tour groups, weekends bring families.",
      "The temple is at Yonghegong station (Lines 2 and 5), Exit C.",
      "Guijie (Ghost Street) is a 10-minute walk south for the city's best late-night food.",
      "Photography is allowed in courtyards but is restricted inside several of the halls — watch the signs."
    ],
    faq: [
      { q: "Is the Lama Temple a functioning temple?", a: "Yes — it is one of Beijing's most active monasteries, with resident lamas, daily services, and a steady stream of worshippers. That living atmosphere is a large part of why it feels so different from other sites." },
      { q: "How long does a visit take?", a: "About 90 minutes. The five halls follow one north-south axis, so the route is linear — walk in, progress hall by hall, and exit near where you started." },
      { q: "Can I burn incense at the temple?", a: "Yes — the temple provides incense with your ticket. The common practice is three sticks held above the head and three bows to each direction. Observe locals to pick up the rhythm." },
      { q: "What is the 18-meter Buddha made of?", a: "The Maitreya Buddha is carved from a single white sandalwood tree imported from Nepal in 1750. It stands 18 meters tall — 8 meters above ground and an estimated 10 meters below, in the statue's foundation." }
    ]
  },

  "national-museum": {
    whyVisit: [
      "The National Museum of China is one of the world's great museums — and it is free. Its Ancient China gallery is the finest single introduction to 5,000 years of Chinese civilization anywhere, walking you from Neolithic pottery to Ming porcelain in one chronological, beautifully labelled hall.",
      "Where the Forbidden City shows you imperial art in situ, the National Museum shows you the civilization behind it — the bronze, jade, silk, and ceramics that shaped everything you will see elsewhere in Beijing. For context, it is the smartest hour-and-a-half you can spend in the city."
    ],
    whatToExpect: [
      "The National Museum of China is one of the world's great museums, and it is free. Its collections trace 5,000 years of Chinese civilization across a floor plan larger than the Vatican Museums — which means the fatal mistake is trying to see all of it. The museum rewards strategy, not stamina.",
      "The essential gallery is Ancient China on the B1 floor: a chronological walk from Neolithic pottery through Shang bronzes, Han jade, Tang ceramics, and Ming porcelain. This single hall is the best introduction to Chinese civilization anywhere — rivalling the British Museum's China galleries in depth, with the advantage of near-universal English labels. The Simuwu Ding, an 832kg Shang bronze ritual vessel, is the heaviest ancient bronze known and sits here in the center of the hall.",
      "Above ground level, the museum runs rotating special exhibitions on themes from Dunhuang frescoes to revolutionary history. The rooftop is free to access and offers a quiet, overlooked view straight down Beijing's central axis toward the Forbidden City — a photographer's secret most visitors miss.",
      "The building itself is part of the story. Completed in 1959 as one of Beijing's 'Ten Great Buildings' and thoroughly renovated before the 2011 reopening, its stone-clad bulk sits on the eastern edge of Tiananmen Square. The central hall — a vast, sky-lit atrium with a sweeping staircase — is among the most imposing modern interiors in Beijing and worth a pause before you descend to the galleries.",
      "A focused visit of two hours covers the Ancient China gallery properly; adding a special exhibition extends it to a half-day. Pair it with the square and Dashilan lunch for a complete central-Beijing morning."
    ],
    visitPlan: [
      "Reserve your free ticket online at least 3 days ahead — walk-ins are not admitted.",
      "Spend 60-90 minutes on the Ancient China exhibition on B1 first.",
      "Pick one special exhibition upstairs; two is pushing it for a single visit.",
      "End on the rooftop for the central-axis view, then exit toward Qianmen for lunch."
    ],
    goodToKnow: [
      "Free but reservation is mandatory; passport required at entry.",
      "The museum closes Mondays (and some state holidays) — plan for Tue-Sun.",
      "Bags larger than cabin size must be checked; dress for air conditioning that runs cold.",
      "The Ancient China hall is busiest 10am-1pm; late afternoon is quieter.",
      "English audio guides and labels are excellent in the main galleries."
    ],
    faq: [
      { q: "How do I book the National Museum?", a: "Reserve free tickets online through the museum's official app or the WeChat mini-program up to 7 days ahead. Walk-ins without a reservation are not admitted. Bring your passport to match the booking." },
      { q: "Which exhibition should I not miss?", a: "Ancient China on B1. It is the museum's crown jewel — 5,000 years of Chinese history in one chronological hall, including the Simuwu Ding bronze and the Han jade burial suit." },
      { q: "Is the National Museum really free?", a: "Yes — general admission is free. Special ticketed exhibitions are occasional and clearly labeled. Because capacity is capped, reserving ahead matters more than any entrance fee." },
      { q: "How long is enough?", a: "Two hours for Ancient China alone; three to four with a special exhibition. The museum closes at 5pm, and last entry is usually around 3:30-4pm, so start by early afternoon." }
    ]
  },

  "jingshan-park": {
    whyVisit: [
      "Jingshan Park holds the definitive view of Beijing: from the summit's Wanchun Pavilion, the entire Forbidden City spreads south like a red-and-gold map, the old city's drum towers stand to the north, and the Central Axis runs between them. It is the cheapest great view in China — CNY 2 for the panorama that anchors every Beijing itinerary.",
      "Because it sits directly behind the Forbidden City's north gate, it is also the perfect capstone to a palace morning — ten minutes of climbing that turns the day's visit into a memory you can actually see."
    ],
    whatToExpect: [
      "Jingshan Park is a 45-minute detour with a payout disproportionate to its size. The artificial hill directly north of the Forbidden City was built from the earth excavated to create the palace moat in the 15th century — and its summit, Wanchun Pavilion, is the highest point in Beijing's old city. From there, the entire Forbidden City unrolls southward like a red-and-gold map.",
      "The view at sunset is the single most photographed urban panorama in China, and it earns the cliché. The palace's golden roofs catch the low light and glow like molten metal against the haze; on clear autumn evenings the Western Hills float on the horizon. Arrive 45 minutes before sunset to claim a rail spot at the pavilion, and expect to share the platform with a wall of phone-wielding tourists — the view is worth the company.",
      "Beyond the summit, the park is a proper Beijing neighborhood green space: peony gardens that explode in April, families flying kites on weekends, and a small corner where residents still practice opera singing. It is a rare spot where the two Beijings — tourist and local — coexist in one small hill.",
      "The hill is steeped in imperial history. Created in 1421 as a feng shui shield for the palace, Jingshan's five pavilions each hold a bronze Buddha, and its eastern slope is where the last Ming emperor, Chongzhen, is said to have taken his own life in 1644 as the capital fell to rebel forces. The park packs five centuries of story into a 15-minute climb.",
      "The logistics could not be simpler: the south gate sits directly opposite the Forbidden City's north exit, the entry costs CNY 2, and the whole ascent takes under twenty minutes at a slow pace. It is the cheapest great view in Beijing and the perfect capstone to a palace morning."
    ],
    visitPlan: [
      "Enter via the south gate directly opposite the Forbidden City's north exit.",
      "Climb the 15-minute path to Wanchun Pavilion at the summit.",
      "Time the climb for 45 minutes before sunset for the golden-roof panorama.",
      "Descend and exit the west gate into Jingshan Houjie for dumplings or noodles."
    ],
    goodToKnow: [
      "Entry is CNY 2 — the cheapest great view in Beijing.",
      "The peak is 48.7 meters; the climb is gentle switchbacks, not stairs.",
      "April's peony garden in the southwest corner is a seasonal highlight.",
      "Pair with the Forbidden City: exit the palace north gate and walk 2 minutes to the south entrance.",
      "Sunset is the busiest time — weekday afternoons offer the best compromise of light and crowd."
    ],
    faq: [
      { q: "How long do I need at Jingshan Park?", a: "Forty-five minutes to an hour covers the climb, the panorama, and a slow descent. It is deliberately short — a stopping point rather than a destination." },
      { q: "Is the view from Jingshan worth the climb?", a: "Unquestionably. From Wanchun Pavilion you see the entire Forbidden City spread south, the Bell and Drum Towers north, and the Central Axis running between them. It is the definitive Beijing panorama." },
      { q: "What is the best time of day to visit?", a: "Late afternoon, timed so you reach the summit about 45 minutes before sunset for golden light over the palace roofs. Morning also works and is quieter, with the palace in soft light." },
      { q: "Can I combine Jingshan with the Forbidden City?", a: "Yes — they are inseparable. The Forbidden City's north gate (Shenwu Men) exits directly across the road from Jingshan's south gate. Do the palace first, then climb Jingshan for the reverse view." }
    ]
  },

  "nanluoguxiang": {
    whyVisit: [
      "Nanluoguxiang is the most walkable window into Beijing's hutong life — the courtyard lanes where the old city's daily rhythm still plays out, minutes from the modern chaos. The main lane's boutiques and snacks are the draw, but the quiet side alleys — Mao'er, Yu'er — are the real discovery.",
      "Dating to the Yuan Dynasty's original street grid, it is one of the best-preserved hutong neighborhoods in the city, and the free stroll from here to the Drum and Bell Towers stitches together the old city's most photogenic mile."
    ],
    whatToExpect: [
      "Nanluoguxiang is Beijing's most famous hutong, and it wears that fame with mixed results. The main lane is a 780-meter spine of boutiques, snack stalls, craft shops, and neon signs — a lively, occasionally frantic commercial strip that draws crowds from mid-morning onward. The real Nanluoguxiang experience is what branches off it.",
      "Duck into Mao'er Hutong or Yu'er Hutong — perpendicular alleys barely two meters wide — and within thirty seconds the crowd evaporates. Courtyard homes (siheyuan) with peeling red gates line the lanes, old men play chess on folding tables, and the only soundtrack is the clatter of bicycle bells. This is the hutong Beijing tourists imagine before they arrive and usually miss on the main drag.",
      "The neighborhood rewards aimless walking. The lanes connect eventually to the Drum and Bell Towers at the north end — climb the Bell Tower's steep stairs for a panoramic hutong-rooftop view — and the whole district fills with red-lantern restaurants after dark.",
      "The hutong grid is one of Beijing's oldest. Nanluoguxiang dates to the Yuan Dynasty (1271-1368) and follows the same chessboard pattern as the original city; the surrounding lanes were laid out when the Mongol capital's streets were organized into blocks of courtyard compounds. It is the best-preserved hutong-and-siheyuan neighborhood in the old city, and many courtyards still house families who have lived there for generations.",
      "The best rhythm is a morning-to-late-afternoon wander: shop the main lane while it is quiet, lose yourself in the side alleys, then end at the Drum and Bell Towers before the neighborhood's restaurant and bar scene wakes up. It is free, walkable, and endlessly photogenic."
    ],
    visitPlan: [
      "Walk the main lane south-to-north in the morning, when shops open and crowds are thin.",
      "Detour into Mao'er and Yu'er hutongs on the west side for the quiet courtyards.",
      "End at the Drum and Bell Towers and climb the Bell Tower for the rooftop view.",
      "Return at night for the lantern-lit street food scene."
    ],
    goodToKnow: [
      "Free to enter; budget for snacks and small purchases.",
      "The lane is pedestrian-only in the middle; the closest subway is Nanluoguxiang (Lines 6/8).",
      "Weekday mornings are the golden window — weekends after 2pm are shoulder-to-shoulder.",
      "Guijie (Ghost Street), the late-night crayfish strip, is a 15-minute walk north.",
      "Respect resident privacy in the side hutongs — courtyards are homes, not attractions."
    ],
    faq: [
      { q: "How long should I spend in Nanluoguxiang?", a: "One to two hours covers the main lane and a side-alley detour. Add the Drum and Bell Towers climb and a meal, and it comfortably fills a half-day." },
      { q: "What are the best side alleys off Nanluoguxiang?", a: "Mao'er Hutong and Yu'er Hutong on the west side are the classic quiet lanes, with courtyard homes, chess players, and tiny family-run shops. They are the antedote to the main lane's crowds." },
      { q: "Is Nanluoguxiang free?", a: "Yes — walking the lanes is free. You pay only for snacks, shops, and the Drum/Bell Tower climb (about CNY 30 for both towers)." },
      { q: "When is the best time to visit?", a: "Weekday mornings before 11am are quiet and photographable. The lane is busiest from mid-afternoon to evening on weekends, when the restaurants and bars take over." }
    ]
  },

  "beihai-park": {
    whyVisit: [
      "Beihai Park is the oldest, most complete imperial garden in Beijing — the White Dagoba perched on Jade Mountain above the lake is one of the city's most photographed and beloved silhouettes, and the park's lakeside calm is a genuine antidote to the palace crowds nearby.",
      "It is also gloriously versatile: a two-hour scenic loop, a rowboat on the lake in summer, a skating rink in winter, and a front-row seat to Beijingers' daily life — fishing, kite-flying, tai chi. Few sites reward an unhurried visit so well, and it chains perfectly with Jingshan and the Drum Towers for a full old-city day."
    ],
    whatToExpect: [
      "Beihai Park is Beijing's oldest and most complete imperial garden, and its centerpiece — the white Tibetan-style dagoba perched on Jade Mountain above the lake — is one of the city's most photographed silhouettes. The park works on two scales at once: a grand imperial composition of lake, hill, and pagoda, and an intimate neighborhood green space full of daily life.",
      "The lake dominates. In summer, pedal boats and dragon boats crisscross the water while locals fish from the willow-shaded banks; in winter the frozen lake becomes one of Beijing's great outdoor skating rinks. The Five-Dragon Pavilions, five connected pavilions jutting into the water on the north shore, are the classic viewing spot for the dagoba reflected across the lake.",
      "The north gate entrance leads to the causeway crossing to Jade Mountain — climb the 17 winding steps to the White Dagoba's base for the elevated view over the entire lake and, beyond it, the drum towers of the old city. The park rewards slow loops: the full perimeter walk takes two hours with a rowboat break thrown in.",
      "The dagoba has a storied past. Built in 1356 as a Tibetan-style pagoda, it was destroyed by lightning and rebuilt repeatedly — the current structure dates to the Qing Dynasty, and its niche housed a Buddhist relic until the 1960s. The surrounding hill, an artificial mound of earth and rock, carries the same feng shui logic as Jingshan, screening the imperial residence from cold northern winds.",
      "Beihai slots neatly into a day of central-Beijing sightseeing: it sits a short walk from both Jingshan Park and the Drum and Bell Towers, and its lakeside atmosphere makes it the most relaxing of the imperial sites — part garden, part public square, entirely worth two unhurried hours."
    ],
    visitPlan: [
      "Enter at Beihai North (Line 6, Exit B) for the shortest walk to the lakeshore.",
      "Cross the causeway to Jade Mountain and climb to the White Dagoba.",
      "Walk the north shore to the Five-Dragon Pavilions for the classic dagoba reflection shot.",
      "End with a 30-minute rowboat rental before the late-afternoon light fades."
    ],
    goodToKnow: [
      "Entry is CNY 10; the dagoba interior adds a small surcharge.",
      "Beihai connects to Jingshan and the Forbidden City by short walks — chain all three in one day.",
      "Mornings are for locals (tai chi, kite-flying); weekday afternoons are the quietest for tourists.",
      "Winter skating on the lake is a Beijing institution — check the ice depth notices first.",
      "The south gate exits near the Forbidden City's north area and the Shichahai lake district."
    ],
    faq: [
      { q: "How much time should I allow for Beihai Park?", a: "Two hours covers the dagoba climb, the Five-Dragon Pavilions, and a lake loop. Adding a rowboat or the winter skating rink extends it by 30-60 minutes." },
      { q: "Is Beihai Park free or ticketed?", a: "Ticketed — CNY 10 in peak season. The White Dagoba interior carries a small separate surcharge. Entry is free on a handful of state holidays." },
      { q: "What is the White Dagoba?", a: "A Tibetan-style white pagoda built in 1356 atop Jade Mountain. It is the park's defining landmark and offers the best elevated view over Beihai Lake and the old city from its base." },
      { q: "Can I combine Beihai with other sights?", a: "Yes — it chains naturally with Jingshan Park (10-minute walk), the Drum and Bell Towers (15 minutes), and the Forbidden City (25 minutes). They form one of the best walking loops in central Beijing." }
    ]
  },

  "798-art-zone": {
    whyVisit: [
      "798 Art Zone is where contemporary China actually happens — a vast former factory complex turned into Beijing's contemporary art heart, with murals, sculpture, and world-class institutions like UCCA all free to wander. It is the essential counterweight to the imperial sights.",
      "After days of palaces and temples, 798 shows you the China of today: its artists, designers, and cafe culture, in one of the most photographed creative districts in Asia. It is free, easy, and the best half-day introduction to where Chinese art is going."
    ],
    whatToExpect: [
      "798 Art Zone is Beijing's contemporary art heart — a former military electronics factory complex from the 1950s repurposed into a sprawling district of galleries, studios, design shops, and cafes. The Bauhaus-style concrete architecture (high ceilings, huge factory windows, exposed beams) is itself the first exhibit; the district's scale — over 500,000 square meters — takes a full afternoon to even sample.",
      "The galleries range from established institutions like UCCA Center for Contemporary Art, which mounts some of China's most important exhibitions, to tiny single-room spaces that change their shows every few weeks. Between the galleries, the streets are an open-air museum: political pop-art murals, monumental sculptures, and rusted factory machinery preserved as installation. This is where Beijing's art scene visibly lives, not just hangs.",
      "Beyond the art, 798 has matured into a lifestyle district — design bookstores, vinyl shops, studios where you can watch ceramicists and printmakers at work, and cafes where gallery-hopping crowds refuel. It is genuinely free to wander; only the special exhibitions charge entry.",
      "The setting is historically layered. The factory complex was built in 1957 by East German architects for the state electronics industry; its Bauhaus-influenced halls were among the largest such structures in Asia. When the factories closed in the 1990s, artists moved in from around 2000, and the district became China's first state-endorsed contemporary art zone — the template for creative districts from Shanghai's M50 to Beijing's own 751.",
      "Come without a rigid itinerary. The pleasure of 798 is in the drift: follow a mural, duck into a gallery that catches your eye, and let the district reveal itself. Two to three hours is the minimum; four if you add a special exhibition and a long lunch."
    ],
    visitPlan: [
      "Take Line 10 to Wangjingnan, then a 10-minute walk or taxi to the south gate.",
      "Start at the 798 Main Street for the street-art murals before the galleries fill up.",
      "Visit UCCA or 798 Space for a major exhibition — book special shows online in advance.",
      "Finish in the sculpture-garden cafe strip as the light turns to golden hour."
    ],
    goodToKnow: [
      "Free to enter; most galleries are free, with special exhibitions typically CNY 50-100.",
      "Most galleries open 10am-6pm and close Mondays — check individual schedules.",
      "Weekdays are quiet; weekends draw families and street performers.",
      "Combine with the nearby 751 D-Park design district for a full creative-zone day.",
      "Wear comfortable shoes — the district is huge and laid out along long factory roads."
    ],
    faq: [
      { q: "Is 798 Art Zone free?", a: "Yes — wandering the district and most galleries is free. Only special exhibitions (UCCA, 798 Space, and others) charge, typically CNY 50-100. Check each show's page before you go." },
      { q: "How do I get to 798?", a: "The simplest route is Line 10 to Wangjingnan station, then a 10-minute walk or short taxi. Several bus lines also stop near the main gates. Expect 40-60 minutes from central Beijing." },
      { q: "How long should I spend at 798?", a: "Two to three hours covers the murals and a handful of galleries. Add a special exhibition and a meal, and it becomes a full afternoon." },
      { q: "Is 798 family-friendly?", a: "Yes \u2014 it is an easy, stroller-friendly district with wide roads, outdoor sculpture, and plenty of cafes. The street art and factory machinery fascinate older kids, though some exhibition content is adult-themed." }
    ]
  },

  "beijing-zoo": {
    whyVisit: [
      "Beijing Zoo is the easiest place in the capital to see giant pandas up close, and for many visitors that is the whole reason to come. The Panda House is the zoo's centrepiece, and a chance to watch these iconic bears munch bamboo, nap in the sun, and roll around their enclosure is a genuinely heart-warming half-day.",
      "It is also excellent value for families \u2014 entry is around CNY 15-20, and beyond the pandas you get golden snub-nosed monkeys, Siberian tigers, and a lovely lakeside park setting right in the city, 110 years old and still one of Beijing's most-loved outings."
    ],
    whatToExpect: [
      "Beijing Zoo is a proper 19th-century-style zoological park wrapped around a lake, not a cramped attraction. The pandas are the headline, but the park rewards wandering: golden snub-nosed monkeys in a hillside enclosure, big cats along one avenue, and waterfowl on the lake that cuts through the grounds.",
      "The Panda House is the star. There are usually several giant pandas on display across an indoor hall and outdoor yards, and they are at their liveliest first thing in the morning during feeding. Watching a panda methodically strip bamboo shoots while a crowd three-deep looks on is a quintessential Beijing moment.",
      "Beyond the pandas, the zoo has an aquarium area, reptile house, and a growing set of modern enclosures. The atmosphere is casual and local \u2014 you will see as many Beijing grandparents with grandchildren as tourists, which is part of the charm.",
      "Allow two to three hours, and pace it around the pandas: arrive at opening, do the Panda House first, then take a relaxed loop around the lake before the school groups build through the morning."
    ],
    visitPlan: [
      "Arrive at the 7:30am gate opening and head straight for the Panda House.",
      "Watch the pandas' morning feeding (8:30-10am) while the crowd is thin.",
      "Loop the lake past the golden monkeys and big-cat enclosures.",
      "Finish with a snack at the lakeside stand before the mid-morning rush."
    ],
    goodToKnow: [
      "Entry is CNY 15-20; the Panda House is included.",
      "Nearest subway is Beijing Zoo station, Line 4, Exit A \u2014 the north gate is 2 minutes away.",
      "Pandas are liveliest 8:30-10am; by afternoon they are usually napping.",
      "Weekday mornings are far quieter than weekends.",
      "The zoo is closed on some national holidays for maintenance \u2014 check before visiting."
    ],
    faq: [
      { q: "How much does Beijing Zoo cost?", a: "Around CNY 15-20 for general entry, which includes the Panda House. It is one of the best-value attractions in Beijing." },
      { q: "What time are the pandas active?", a: "Feeding happens between roughly 8:30 and 10am, when the pandas are most active. By mid-afternoon they are typically asleep, so go in the morning." },
      { q: "How long should I spend at the zoo?", a: "Two to three hours covers the pandas and a relaxed loop of the park. It makes a good half-day with a nearby lunch." },
      { q: "Is Beijing Zoo worth it for adults without kids?", a: "Yes \u2014 the giant pandas are a must-see for many visitors regardless of age, and the park itself is pleasant and cheap. Morning is the time to go." }
    ]
  },

  "beijing-bell-tower": {
    whyVisit: [
      "The Bell & Drum Towers are Beijing's best-kept secret viewpoint. From the top of the 45-meter Bell Tower you get the definitive panorama of the old city's grey-tiled hutong rooftops stretching to Jingshan and the Forbidden City \u2014 the same view you have seen in a thousand Beijing photographs, but from the middle of it.",
      "For nearly 700 years these towers announced the hours across the capital \u2014 the drum by night, the bell at dawn. Climbing them is a short, steep, utterly rewarding step into Beijing's medieval timekeeping, with the Drum Tower's drum performances adding a live soundtrack."
    ],
    whatToExpect: [
      "The two towers stand 100 meters apart at the northern edge of the old city. The Bell Tower is the taller (45 meters) with the better panorama; the Drum Tower, lower and squarer, houses the huge drums and a 25-ton bronze bell.",
      "The climb is the thing \u2014 steep wooden staircases with no elevator, but the reward at the top is the single best hutong-rooftop view in Beijing. Below you, the grey-tiled roofs of the drum-and-bell neighborhood stretch to Jingshan and the Forbidden City beyond.",
      "The Drum Tower hosts short percussion performances through the day \u2014 a dramatic burst of drumming that echoes through the hall and is over in a few minutes. It is included in the entry and worth timing for.",
      "The neighborhood around the towers is itself the attraction: Nanluoguxiang's hutong lanes to the south, the Houhai lake district to the west, and street food everywhere. The towers are the anchor of one of Beijing's best walking areas."
    ],
    visitPlan: [
      "Climb the Bell Tower first for the panorama, then the Drum Tower.",
      "Time the Drum Tower drum performance (last show around 4:45pm).",
      "Wander the hutong rooftops view from the Bell Tower's top.",
      "Finish with jianbing and street snacks in the surrounding lanes."
    ],
    goodToKnow: [
      "Entry is CNY 30 for both towers.",
      "Nearest subway is Shichahai, Line 8, Exit A \u2014 a 5-minute walk.",
      "There is no elevator \u2014 the Bell Tower climb is steep, so it suits active visitors.",
      "Late afternoon (4-5pm) is the golden window for light and smaller crowds.",
      "Combine with Nanluoguxiang and Houhai for a full old-city walking day."
    ],
    faq: [
      { q: "Which tower has the better view?", a: "The Bell Tower, at 45 meters, offers the higher and more famous panorama over the hutong rooftops toward Jingshan and the Forbidden City. The Drum Tower's view is still excellent and closer to the action." },
      { q: "Are the drum performances worth it?", a: "Yes \u2014 the Drum Tower runs short percussion shows several times daily, and the sound in the wooden hall is striking. The last performance is usually around 4:45pm, so plan to be there by 4:30pm." },
      { q: "How long does a visit take?", a: "About an hour for both towers including the drum show. Add another hour to wander the surrounding hutongs and Houhai lake." },
      { q: "Is the climb hard?", a: "The Bell Tower has steep wooden stairs with no lift \u2014 a challenge but short (a few minutes). If mobility is a concern, the Drum Tower's climb is gentler." }
    ]
  },

  "ming-tombs": {
    whyVisit: [
      "The Ming Tombs are where imperial China's burial grandeur is laid out at full scale \u2014 13 of the 16 Ming emperors buried in a vast complex against the forested mountains 50km north of Beijing. The Sacred Way's avenue of stone animals alone is worth the trip, and it pairs perfectly with a Great Wall visit since the tombs sit on the same northern route.",
      "It is the quieter, more atmospheric half of the classic 'Great Wall + Ming Tombs' day trip \u2014 less crowded than the Wall, and a chance to see the excavated underground palace at Dingling, where you walk down into an actual imperial tomb."
    ],
    whatToExpect: [
      "The Ming Tombs site has two must-see parts. The Sacred Way is the ceremonial approach \u2014 a 7-kilometer avenue lined with 36 enormous stone animals and officials in pairs, built to guard the spirits of the emperors. It is eerie, beautiful, and nearly crowd-free late in the day.",
      "Changling, the tomb of the Yongle Emperor (who built the Forbidden City), is the largest and most impressive above-ground tomb \u2014 its great hall is held up by 60 huge nanmu cedar pillars that smell faintly of wood and feel like standing inside a forest.",
      "Dingling is the only tomb actually excavated \u2014 the underground palace was opened in the 1950s, and you descend a long staircase into the stone burial chambers to see where the emperor's coffin and treasures lay.",
      "The tombs are spread over a large site with shuttle buses between the main sights. Allow three to four hours, and pace it: Dingling first (it fills up), then Changling, then the Sacred Way in late afternoon."
    ],
    visitPlan: [
      "Visit Dingling first, before the tour groups arrive (from 10am).",
      "Walk through Changling's great hall with its nanmu pillars.",
      "Take the shuttle to the Sacred Way and walk the avenue of stone animals.",
      "Time the Sacred Way for late afternoon light and smaller crowds."
    ],
    goodToKnow: [
      "Entry is CNY 40-60 depending on which tombs you visit.",
      "There is no direct subway \u2014 go by taxi, tour bus, or as part of a Great Wall tour.",
      "The tombs pair naturally with Badaling or Simatai on the same northern route.",
      "The site is spread out \u2014 wear walking shoes and use the shuttle buses between sights.",
      "Bring water and snacks; the on-site canteens are basic."
    ],
    faq: [
      { q: "How do I get to the Ming Tombs?", a: "There is no direct subway. The easiest options are a taxi (about 1 hour, CNY 150-200), a guided Great Wall + Ming Tombs tour, or a bus to Changping then a local taxi. The tombs sit on the same route as Badaling, so they pair naturally." },
      { q: "Is the Dingling underground palace worth it?", a: "Yes \u2014 it is the only excavated Ming imperial tomb, and walking down into the actual stone burial chambers is the most atmospheric part of the site. Go first, before the crowds." },
      { q: "How long should I spend at the Ming Tombs?", a: "Three to four hours covers Dingling, Changling, and the Sacred Way. Combined with a Great Wall morning, it makes a full but classic day trip." },
      { q: "Which tomb should I see if I'm short on time?", a: "Dingling for the underground palace, plus the Sacred Way for the iconic stone-animal avenue. Skip Changling if you must cut something." }
    ]
  },
};
