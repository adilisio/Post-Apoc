# Fallout Production Metrics: Team, Time, Money, Scale, Result

Scope: a sourced table of production metrics for each mainline Fallout game (plus Van Buren), with a confidence grade on every number, followed by derived comparisons and scope lessons for a small original team. Companion to `development-history.md` (narrative); this file does not repeat that narrative and reuses its verified facts only where noted. Research date: November 2026.

## Quick Reference

- **Grade key.** [A] = stated by a named participant or the publisher (seen through at least one write-up; originals such as the GDC 2012 video, Fortune, and Bethesda posts were not opened). [B] = reputable press or a Wikipedia line whose cited reference is named. [C] = analyst, third-party, or my own derived estimate. [UNVERIFIED] = single weak source or not confirmed. [DISPUTED] = sources disagree. "No credible public figure" means I searched and found nothing citable.
- **Fallout 1:** about US$3M [A: Cain / Fargo] over about 3.5 years. Cain alone for 6 months, 15 people in year two, 30 in year three [A: Cain GDC 2012 notes]. Metacritic 89 [B]. Roughly 750 person-months [C, derived].
- **Fallout 2:** under about 9 months of real production [A: Urquhart], released Oct 30, 1998 [B]. Interplay PR said 15 people were working on it in Jan 1998 [B]. Budget: no credible public figure. Metacritic 86 [B].
- **Van Buren:** about 6 months of work before cancellation, Dec 8, 2003 [B]. Cain estimated 12 to 18 more months, Sawyer at least 24 [A]. No headcount (Sawyer: "skeleton crew") and no budget figure.
- **Fallout 3:** about 10 people at start in late 2004, about 75 at the end [B: GameSpot 2007 / TechRadar 2018], about 80 in Todd Howard's own estimate [A via Game Developer]. 40,000+ recorded lines [A: Guinness 2011]. Marketing budget US$13M [B: Video Business, Aug 2008, seen via Wikipedia]. Development budget: no credible public figure. Metacritic 90 to 93 [B]. Shipped 4.7M in the first week [B: GameSpot].
- **New Vegas:** 18 months [A: Gonzalez, Sawyer]. About 70 to 73 developers at Obsidian, counted by Chris Avellone [A, retrospective]. 65,000 lines [A: Guinness]. Flat fee with no royalties and a bonus at Metacritic 85+; it scored 84 (PC and 360) and 82 (PS3) [A: Avellone, Urquhart]. 5M shipped and US$300M revenue by Nov 8, 2010 [A: Bethesda]. Fee amount: no credible public figure.
- **Fallout 4:** "just over 100 people," only about 8 more than at Skyrim [A: Gardiner / Howard, Game Informer 2015]. First asset in 2009, full production from April 2013, ship Nov 10, 2015: about 7 years elapsed, about 31 months in full production [A]. 111,000+ voiced lines [A: Bethesda]. 12M shipped and US$750M in 24 hours [A: Bethesda]. Budget: no credible public figure.
- **Fallout 76:** greenlit after Fallout 4 shipped (Nov 2015), announced May 30, 2018, released Nov 14, 2018 [B]. Multi-studio (Rockville, BattleCry/BGS Austin, plus Arkane, id, ZeniMax Online, Iron Galaxy, Double Eleven for additional work) [B]. Headcount: no credible public figure. Launch Metacritic 49 to 53 [B]. 1.4M digital copies by end of 2018 [C: SuperData]. Bethesda later claimed 21M+ "Vault-dwellers" by Nov 2024 [A, not unique buyers].
- **Reported FO76 conditions:** Kotaku, June 2022, by Sisi Jiang, drawing on interviews with about 10 former employees [B]. QA reportedly worked about 10-hour days, six days a week before launch; staff were moved over from Starfield and Redfall; multiplayer expertise in Austin and ZeniMax Online was reportedly sidelined.
- **Only the pre-Bethesda games have a stated budget** (FO1 about US$3M). For every Bethesda-era game the development budget is not public; only FO3's marketing figure and sales figures are.
- **Derived (labelled C):** FO1 about 750 person-months; FO2 about 300; FO3 about 1,850; NV about 1,000; FO4 about 3,500. Voiced lines per person-month: FO3 about 22, NV about 65, FO4 about 32.
- **What the normalisation says:** the tightest, most reactive writing per unit of labour came from the team that reused a toolset (NV). The biggest labour spend went into voice, systems and the protagonist (FO4), which scored similarly to NV but sold at a different order of magnitude. Metacritic per unit of labour falls sharply as teams grow, but this is a weak signal (see caveats).
- **Cheapest high-value features** (from the evidence): text-driven reactivity and skill checks, faction reputation, ending slides, reused assets with new writing, and a documented tone. **Expensive with weak payoff:** a fully voiced protagonist, a custom-engine rewrite for multiplayer, a hand-built dense map without human NPCs, and unbeta'd live-service launches.
- **Biggest data gaps:** Fallout 2 headcount and budget; any Bethesda or Obsidian development budget; FO76 headcount; word counts for all games; quest counts and voiced-NPC counts from developers (fan wikis count them, but not citably here).

## Method and Limits

- Wikipedia figures were cross-checked against the references Wikipedia itself names (for example, FO3's team size traces to GameSpot 2007 and TechRadar 2018; FO3's marketing budget traces to Video Business 2008; FO3's line count traces to Guinness World Records 2011 Gamer's Edition, p. 147).
- Press sites that returned 403 or truncated pages (MobyGames, GamePro, Kotaku original, PC Gamer, GameSpot, TweakTown) were not read in full. Where a figure came from a search-result summary rather than a fetched page, it is flagged.
- Person-month figures are crude. They multiply a stated or assumed average headcount by calendar months. They exclude outsourced QA, voice recording, publisher marketing, middleware, and shared-studio support. The arithmetic is shown in the derived section so it can be rechecked or replaced.
- Several 2026-dated claims in Wikipedia (FO4 at "35 million", native PS5/Series versions on Sept 15, 2026, a new Obsidian Fallout) are each single-source and not independently confirmed here.

## 1. Team Size

Developers are separated from total credits. "Core" means design, art, programming, production.

| Game | Start | Peak / typical | Credited (total) | Notes | Grade |
|---|---|---|---|---|---|
| Fallout (1997) | Tim Cain alone for the first 6 months; then a scripter and an artist | 15 in year two; 30 in year three ("roughly 30" at the peak) | Not counted here (MobyGames blocked). fallout.wiki claims near 100 credited at peak | Cain's own count excludes Interplay-wide QA (see conditions). Wikipedia: 15 in 1995, 30 in 1996 | Start and peak [A: Cain GDC 2012 notes; Game Developer]. Credit count [UNVERIFIED] |
| Fallout 2 (1998) | 15 people working on it in late Jan 1998 (Interplay PR rep Kurt Green) | No stated peak. Staff were moved over from Planescape: Torment; Cain, Boyarsky and Anderson left within months | 187 credited people, 225 credits on Windows (178 professional roles, 9 thanks), from a MobyGames summary seen only in search results | 187 is a credits count, not a team size | 15 [B: fallout.wiki citing Interplay PR]. 187 [UNVERIFIED] |
| Van Buren (2003, cancelled) | Black Isle's team, moved from the cancelled Baldur's Gate III | Cut to a "skeleton crew" before cancellation, losing at least one character artist | n/a | Chris Avellone led design; Josh Sawyer lead system designer; producer Tom French | "Skeleton crew" [A: Sawyer via VGC]. Headcount: no credible public figure |
| Fallout 3 (2008) | About 10 in late 2004 (most staff on Oblivion) | About 75 at completion (programmer Jean Simonet); about 80 (Todd Howard's estimate to Game Developer) | Not retrieved | The team grew sharply after Oblivion shipped in 2006 | Start [B: GameSpot, May 2007]. End 75 [B: TechRadar, Nov 2018]. 80 [A via Game Developer] |
| New Vegas (2010) | Small at the start; grew as Alpha Protocol finished (Sawyer, via a secondary summary) | About 70 developers (Avellone, Apr 2022); a later report says 73. Game Developer's Cain piece implies 60 to 80 (three to four times Icewind Dale's roughly 20) | Not retrieved | Five cross-discipline teams plus a small producer group (Larry Liberty). Avellone excluded administrative staff and Bethesda personnel | 70 [A, retrospective count; reported by Game World Observer]. 73 [UNVERIFIED, one Russian-language report] |
| Fallout 4 (2015) | Concept art from 2009; 1 to a few dozen people during Skyrim (exact size not public) | "Just over 100 people," up about 8 since Skyrim (Gardiner; Howard) | Not retrieved | Sister studios (for example Montreal, Dallas) and outsourcers are not in the 100 | 100+ [A: Gardiner / Howard via Gamerant and Game Informer 2015] |
| Fallout 76 (2018) | BattleCry Studios (Austin) paused its own F2P game to take the prototype | Headcount: no credible public figure | Not retrieved | Rockville, Austin, plus Arkane, id, ZeniMax Online, Iron Galaxy, Double Eleven for extra work; Starfield and Redfall staff reassigned | Studios list [B: Wikipedia]. Reassignments [B: Kotaku via NME, Wikipedia] |

Context data points: Skyrim "more than 90" developers (Game Developer, FO article); Bethesda in 2024 said hundreds of people were working across at least three Fallout projects (TweakTown headline only; page blocked) [UNVERIFIED]; Interplay as a whole went from about 42 staff when Cain joined to over 600 when he left [A: Cain, Shacknews oral history].

## 2. Timeline

| Game | Pre-production | Full production | Announce | Ship | Total | Grade |
|---|---|---|---|---|---|---|
| Fallout | Early 1994 (Cain's spare-time engine) | About 1995 onward (team grew to 15, then 30) | Demo April 26, 1997 | Gold Oct 1, 1997; release Oct 10, 1997 (a Shacknews narration says Oct 9) | About 3.5 years (about 42 months) | [B: Wikipedia, Game Developer] |
| Fallout 2 | Pitch discussed before FO1 shipped | Mid-1997 per Game Developer, Oct 1997 per fallout.wiki [DISPUTED]; Urquhart: "most of the game" in about 8 to 9 months | Cain posted "11 months" in Dec 1997; official Feb 13, 1998 | Gold Oct 22; shipped Oct 26; released Oct 30, 1998 | About 12 to 16 months calendar; about 8 to 9 months of real production | [A: Urquhart quotes; B: fallout.wiki] |
| Van Buren | FO3 work began early 2003 (Sawyer) | About 6 months before cancellation | Never announced | Cancelled Dec 8, 2003 | About 6 months | [A: Sawyer; B: Wikipedia] |
| Fallout 3 | Licence signed 2004 (Bethesda announced July 2004) | Late 2004; the Oblivion team joined from 2006 | Game Informer cover reveal, 2007 (month not verified) | Oct 28, 2008 (NA); Oct 30/31 (EU/AU); Dec 4 (Japan) | About 46 months from late 2004 | [B: Wikipedia]. Pagliarulo told Game Developer in Sept 2008 that pre-production started roughly four years earlier [A] |
| New Vegas | A three-page pitch; source-code access delayed by Bethesda clearance | 18 months | Announcement date not verified in this research | Oct 19, 2010 (NA); Oct 21 (AU); Oct 22 (EU) | 18 months | [A: Gonzalez "a mere 18 months"; Wikipedia] |
| Fallout 4 | First asset in 2009 ("a week after Fallout 3's DLC"); sound library 2010; renderer rewrite from 2012 | Team moved off Skyrim's last DLC in April 2013 | June 2015 (E3 reveal, alpha state); Kotaku leaked casting docs Dec 2013 | Nov 10, 2015 | About 7 years elapsed; about 31 months in full production | [A: Howard / Burgess in Game Informer, Nov 2015] |
| Fallout 76 | Multiplayer ideas shelved during FO4; project greenlit after FO4's Nov 2015 release | Roughly Nov 2015 to Nov 2018 (about 36 months) | May 30, 2018; E3 June 10, 2018 | Open beta Oct 23 (Xbox) / Oct 30 (PS4, PC), 2018; release Nov 14, 2018 | About 36 months, announce-to-ship about 5.5 months | [B: Wikipedia]; Howard: "76 is the multiplayer design from Fallout 4" [A: Noclip via Game Developer] |

### Post-ship content cadence

| Game | Post-ship content | Grade |
|---|---|---|
| Fallout 1 | None (patches only) | [B] |
| Fallout 2 | None; last official patch 1.02, Feb 11, 1999 | [B: earlier research] |
| Fallout 3 | Five add-ons in about 6 months: Operation: Anchorage (Jan 27, 2009), The Pitt (Mar 24), Broken Steel (May 5), Point Lookout (Jun 23), Mothership Zeta (Aug 3). Development of the packs began about two months before the base game shipped; only three were planned at first. Howard: two dev teams were dedicated to two episodes | [B: fallout.wiki; Wikipedia; Howard via Game Informer] |
| New Vegas | Four story DLC over 9 months: Dead Money (Dec 21, 2010), Honest Hearts (May 17, 2011), Old World Blues (Jul 19, 2011), Lonesome Road (Sept 20, 2011); two item packs listed Sept 27, 2011 | [B: fallout.wiki]. Item-pack dates [DISPUTED / UNVERIFIED] |
| Fallout 4 | Six add-ons in 5 months, starting 4 months after launch: Automatron (Mar 22, 2016), Wasteland Workshop (Apr 12), Far Harbor (May 19), Contraptions (Jun 21), Vault-Tec Workshop (Jul 26), Nuka-World (Aug 29 or 30). Season pass announced Feb 16, 2016. Creation Club Aug 2017 | [B: Wikipedia, fallout.wiki] |
| Fallout 76 | Live service: patches from launch (first about 50 GB); Fallout 1st subscription Oct 23, 2019; Wastelanders (human NPCs) April 2020; modes added and removed | [B: Wikipedia] |

## 3. Budget

Label: STATED BY DEVELOPER / REPORTED BY PRESS / ANALYST ESTIMATE / FAN ESTIMATE / UNKNOWN.

| Game | Figure | Label | Notes and grade |
|---|---|---|---|
| Fallout | About US$3M (about US$4.5M in 2015 dollars) | STATED BY DEVELOPER | Cain, Game Developer 2015; Fargo's "three years and three million dollars" (Shacknews oral history). Wikipedia converts to about US$5.58M in 2025 money. [A] |
| Fallout (modern equivalent) | US$5.5 to 9.1M to rebuild in 2022 | FAN ESTIMATE | A Reddit user's calculation (30 to 50 people, 27 months, US$205 to 340K per month), reported by wnhub. [C] |
| Fallout 2 | No credible public figure | UNKNOWN | A Urquhart line in the Shacknews oral history gives Interplay budgets rising from about US$250K to about US$2M, but the context is Interplay's general growth and I could not confirm it refers to Fallout 2. Do not use. [UNVERIFIED] |
| Van Buren | No credible public figure | UNKNOWN | Cain: Interplay could not fund more than about six months. |
| Fallout 3: IP | US$1.175M minimum guaranteed advance (2004 licence); US$5.75M for the IP (April 2007) | REPORTED BY PRESS | Wikipedia; the earlier research file. [B] |
| Fallout 3: marketing | US$13M | REPORTED BY PRESS | Video Business, Aug 18, 2008, via Wikipedia footnote 33; I did not open the original. [B] |
| Fallout 3: development | No credible public figure | UNKNOWN | RPG Codex and a Cyberpost FAQ suggest US$20 to 30M including marketing, but both are loose; I do not recommend citing them. [UNVERIFIED] |
| New Vegas | Flat fee, no royalties, bonus if any platform reached 85 on Metacritic. "A straight payment, no royalties, only a bonus if we got an 85+" (Avellone). Urquhart: Bethesda added the bonus; Obsidian "just pretty much ignored it" | STATED BY DEVELOPER | [A] |
| New Vegas: fee amount | No credible public figure | UNKNOWN | |
| New Vegas: bonus amount | Reported at US$1M | REPORTED BY PRESS | Kotaku, one anonymous source. [UNVERIFIED] |
| Fallout 4 | No credible public figure (development or marketing) | UNKNOWN | Forum guesses only. Bethesda's own number is US$750M of product shipped in 24 hours, which is retail value, not profit. |
| Fallout Shelter (context) | About US$100M lifetime mobile revenue (about 4 years) | ANALYST ESTIMATE | Sensor Tower, reported by PocketGamer.biz, June 2019; Game Developer's Kotaku summary says Shelter's takings prompted the multiplayer project. [C] |
| Fallout 76 | No credible public figure | UNKNOWN | |

## 4. Engine, Tech and Content Scale

| Game | Engine: inherited vs. built | Content scale (as stated) | Grade |
|---|---|---|---|
| Fallout | Built: custom 2D engine, cavalier oblique projection, 640x480, 256 colours (about 230 usable) | 3 main acts (Cain: the earlier time-travel concept had "thirty or forty"); each quest solvable at least two ways (fight, talk, sneak); talking heads took 8 weeks each, 4 months including voice matching. Lines or word count: no credible public figure | [A: Cain GDC 2012 notes; Shacknews] |
| Fallout 2 | Inherited FO1 engine; 16-bit upgrade rejected because all art would be redone | Mandate from management to be 50% bigger (Scott Everts); world size roughly doubled (earlier research). Words or lines: no credible public figure | [A: Everts; B] |
| Van Buren | Built: in-house "Jefferson", then NDL 3D; Black Isle's inexperience slowed work | A design document of about 700 pages and a playable tutorial demo leaked (2005 to 2007). Counts of words, lines or quests: no credible public figure | [B: Wikipedia] |
| Fallout 3 | Inherited: Gamebryo (Oblivion). Rebuilt design from scratch; no Van Buren assets | 40,000+ recorded lines (Guinness record); Howard: 100+ hours of content (from a search summary only); D.C. downtown cut from 26 enclosed areas to 12; about 30% of dialogue cut late for disc space; wasteland doubled in alpha | Lines [A: Guinness 2011]. Hours [UNVERIFIED]. Cuts [A: Zeleny, Pagliarulo in earlier research] |
| New Vegas | Inherited: Gamebryo and a modified Fallout 3 G.E.C.K. (Gonzalez); no prior Gamebryo experience, so a modder was hired; PS3 memory forced cuts | 65,000+ recorded lines (Guinness record); 8 companions in the base game; five cross-discipline teams. Word count and quest count: no credible public figure | Lines [A: Guinness, Bethesda PR via Prima]. Companions [C: guide] |
| Fallout 4 | Inherited and modified: Creation Engine (Skyrim); renderer rewrite from 2012; 30 fps target; new gun-mod system | 111,000+ voiced lines (more than FO3 and Skyrim combined); two protagonist actors each recorded 13,000+ lines (Howard); 150 to 200 locations planned (Burgess); map about 3.8 square miles (press estimate) | Lines and actors [A: Bethesda, Howard]. Locations [A: Burgess]. Map [C] |
| Fallout 76 | Inherited and stretched: Creation Engine (single-player); "the game doesn't load except around one player" (Mayer); Quake-derived netcode ideas | Bethesda claimed a map four times Fallout 4's (E3 2018); outlets estimated about 16 square miles, with walking tests suggesting a smaller real difference. Lines or quest count: no credible public figure | Claim [A]. Square miles [C]; walking tests [C] |

Counts that had **no credible public figure for any game in this research:** words of text, total quest count, voiced-NPC count (fan wikis publish counts, but I could not verify any of them against a developer statement). The "lines" figures for FO3, NV and FO4 come from three different counters (Guinness, Guinness, Bethesda's own post) and may not count barks the same way [UNVERIFIED].

## 5. Commercial and Critical Result

| Game | Launch / early sales | Lifetime / later | Metacritic | Grade |
|---|---|---|---|---|
| Fallout | 53,777 US copies by end of 1997; 100,000+ shipped by Dec 1997 | 600,000 total (Fargo, 2017); 144,000 US by March 2000 (PC Data) | 89 | Sales [B: Wikipedia, citing Bethke, PC Data, Fargo]. Score [B] |
| Fallout 2 | Third on PC Data's chart, first week of Nov 1998; fell off the top ten the next week | 123,000 US by March 2000 (PC Data). UK: 50,000 combined with FO1 by 2008 (Eurogamer). Lifetime: no credible public figure | 86 (GameRankings 87%) | [B: Wikipedia] |
| Van Buren | n/a | n/a | n/a | |
| Fallout 3 | 4.7M copies and US$300M in the first week (GameSpot, Nov 2008); outsold every previous Fallout combined; 57% above Oblivion's first week | 12.4M by 2015 (EEDAR estimate) | PC 91; PS3 90; X360 93 | Launch [B: GameSpot via Wikipedia]. Lifetime [C] |
| New Vegas | 5M shipped and US$300M revenue by Nov 8, 2010 | 11.6M by 2015 (EEDAR estimate) | PC 84; X360 84; PS3 82 (85 was the bonus threshold; missed by one point) | Launch [A: Bethesda]. Lifetime [C]. Scores [B] |
| Fallout 4 | 12M shipped and US$750M in 24 hours (sell-in, not sell-through); 1.2M Steam units in 24 hours; about 470,000 concurrent Steam players | Bethesda reported more than 35M copies in July 2026 (single source: Wikipedia) | PC 84; PS4 87; X1 88 | Launch [A: Bethesda]. Lifetime [UNVERIFIED]. Scores [B] |
| Fallout 76 | NPD: lower launch sales than FO4 or NV; physical sales about 82% below FO4 in the opening months; UK charts third, fifth in Switzerland; PS4 sold 73,489 in Japan in week one; 1.4M digital copies by end of 2018 (SuperData) | 11M players (Howard, Nov 2021); 13.5M (Dec 2022); 17M (Mar 2024); "over 21 million Vault-dwellers" (Bethesda, Nov 2024). "Players" includes Game Pass trials, not just buyers. Third-party sales estimates (3M to 7.2M on Steam) conflict | Launch: PC 52, PS4 53, X1 49. Wastelanders: PC 68, PS4 63. User scores about 2.4 to 2.9 at launch | Sales [B/C]. Player counts [A, definition vague]. Scores [B] |

Awards for context: FO3 won Game Developers Choice Game of the Year and Best Writing 2008 [B]; FO4 won D.I.C.E. Game of the Year, BAFTA Best Game, and Game Critics Awards Best of Show 2015 [B].

## 6. Working Conditions as Reported

| Game | Reported conditions | Grade |
|---|---|---|
| Fallout | Cain: "fourteen-hour days Monday through Saturday, and an eight-hour day on Sunday" in the last stretch. QA: the project's own QA group plus "thirty or forty other QA people" at Interplay; QA staff reportedly worked weekends unpaid. Cain nearly lost the project several times to internal competition | [A: Cain via Shacknews oral history; GDC 2012 notes] |
| Fallout 2 | Nine-ish months, with staff pulled from Planescape: Torment; "a whole lot of crunch" (Spitzley); Urquhart said he pushed everyone too hard and later recommended slipping dates rather than crunching. Cain left for burnout and bonus-related reasons; patch 1.02 four months after launch | [A: Spitzley, Urquhart; B] |
| Van Buren | Cancelled when Interplay's money ran out; one account says the team was laid off, Cain says most were moved to other projects [DISPUTED]; Black Isle closed about two weeks after Sawyer left | [B] |
| Fallout 3 | Late-development burnout and mistakes (Pagliarulo to Edge, via secondary summary); about 30% of dialogue cut late; release-day bugs. No specific overtime figures found | [B: secondary] |
| New Vegas | Sawyer: "forty to fifty hours" a week (Wikipedia); fallout.wiki's note claims "mandatory crunch weekends" [DISPUTED]. QA: Sawyer thanked Bethesda QA contacts (Ashley Cheng, Andrew Scharf), and Bethesda Softworks QA testers are credited, but I found **no source stating how QA labour was split** between Obsidian and Bethesda, so "Bethesda handled QA" is [UNVERIFIED]. Launch was buggy; Obsidian blamed size and the 18-month window; PS3 memory limits forced cuts. Gonzalez scripted dialogue directly in the tools | [A: Sawyer, Gonzalez; B] |
| Fallout 4 | Team "just over 100" and stable (+8 since Skyrim). A designer spent 3 years on loot. Workshop was a late-schedule risk Gardiner expected to be cut. Crunch reports: I found none in the sources consulted (absence of evidence only) | [A: Game Informer 2015] |
| Fallout 76 | Kotaku, June 2022 (Sisi Jiang), about 10 former employees: "brutal culture of crunch"; QA about 10-hour days, six days a week in the months before launch, weekend pushes paid about US$200 plus pizza; weekend work called voluntary but the whole team came in if too few volunteered; timed breaks; QA told to verify a fix in a build that lacked it; QA exposed to death threats while triaging forum reports; QA reportedly got three days with a good build in a good week; senior developers left under pressure or for health reasons; Fallout 4 veterans resented live-service work; staff moved from Starfield and Redfall (which reportedly hurt those games); multiplayer experience in Austin and ZeniMax Online reportedly sidelined; release date not moved after the E3 announcement even as scope grew. Howard publicly regretted no beta. Bethesda did not comment at publication | [B: Game Developer (Bryant Francis, June 8, 2022), NME, MeinMMO, PC Gamer snippets, all summarising Kotaku; anonymous sources] |
| Layoffs after ship | Interplay and Black Isle 2003 (see above). Microsoft-era cuts hit Bethesda studios, and reports named Fallout 76 quest designers among those cut; I could not retrieve dates or headcounts | [UNVERIFIED details] |

## 7. Derived Comparison (rough estimates, [C])

### 7a. Person-months

Formula: person-months (pm) = sum over periods of (average headcount x months). Headcounts are the stated figures with the assumptions listed. These are order-of-magnitude numbers (plus or minus 25% at best).

| Game | Arithmetic | pm | Range | Assumptions |
|---|---|---|---|---|
| Fallout | Months 0-6: 6 x 1 = 6. Months 6-12: 6 x 3 = 18. Year 2: 12 x 15 = 180. Year 3: 12 x 30 = 360. Last 6 months: 6 x 30 = 180. Total 744 | about 750 | 600 to 900 | Cain's yearly figures; "3" for the scripter and artist is assumed. Excludes Interplay-wide QA, voice, music |
| Fallout 2 | About 12 months x average 25 = 300 | about 300 | 200 to 400 | Only anchor is 15 in Jan 1998; assumes growth with Planescape staff. Real production was shorter, so this is generous |
| Fallout 3 | Late 2004 to Mar 2006: 17 months x 17 average = about 290. Mar 2006 to Oct 2008: 31 months x 50 average = 1,550. Total about 1,840 | about 1,850 | 1,400 to 2,400 | Start 10, ramp to about 25 at Oblivion's ship, then to 75 to 80 |
| New Vegas | 18 months x average 55 = 990. Upper bound: 73 x 18 = 1,314 | about 1,000 | 800 to 1,300 | Team ramped up as Alpha Protocol wound down; excludes Bethesda QA and publishing |
| Fallout 4 | Full production: 31 months x 100 = 3,100. Pre-production 2009 to Apr 2013: about 40 months x 10 = 400. Total 3,500 | about 3,500 | 3,000 to 4,000 | Pre-production headcount is a guess; excludes sister studios, outsourcers, VO studios |
| Fallout 76 | Not computable | n/a | n/a | No credible public headcount |
| Van Buren | About 6 months x unknown skeleton crew | n/a | n/a | No headcount |

Sanity check on money: Fallout 1 at US$3M and about 750 pm implies about US$4,000 per person-month fully loaded. That is plausible for 1990s Southern California and suggests the US$3M figure is a real all-in total rather than a marketing number. It cannot be checked for any later game because no later budgets exist.

### 7b. Output per unit of effort

| Metric | FO1 | FO2 | FO3 | NV | FO4 |
|---|---|---|---|---|---|
| Person-months (7a) | 750 | 300 | 1,850 | 1,000 | 3,500 |
| Peak team | 30 | about 25 to 40 (assumed) | 75 to 80 | 70 to 73 | 100+ |
| Months | 42 | 9 to 12 | 46 | 18 | 31 production / 84 elapsed |
| Voiced lines | no credible figure | no credible figure | 40,000 | 65,000 | 111,000 |
| Lines per pm | n/a | n/a | 40,000 / 1,850 = 22 | 65,000 / 1,000 = 65 (range 50 to 81) | 111,000 / 3,500 = 32 (player-heard: 98,000 / 3,500 = 28) |
| Metacritic (PC) | 89 | 86 | 91 | 84 | 84 |
| Points per 1,000 pm | 89 / 0.75 = 119 | 86 / 0.3 = 287 | 91 / 1.85 = 49 | 84 / 1.0 = 84 | 84 / 3.5 = 24 |
| Launch units shipped per pm | about 100,000 / 750 = about 130 | n/a | 4.7M / 1,850 = about 2,500 | 5M / 1,000 = 5,000 | 12M / 3,500 = about 3,400 |

For FO4's player-heard line count I subtracted one protagonist's 13,000 lines because a player hears only one of the two voice actors.

### 7c. What this tells us and what it does not

What it tells us:
- Voice is the single largest labour sink in the Bethesda games, so line count is a defensible proxy for content cost. NV produced roughly three times FO3's lines per person-month, consistent with a reused toolset, a writing-first process, and a shorter schedule with less polish.
- The score gap between NV (84) and FO4 (84 on PC) cost about 3.5x the labour; the commercial gap (launch shipments) was far larger. Quality per head fell as headcount rose, but reach rose more. For a small team the lesson is on the quality-per-head side, not the reach side.
- Era matters more than team: FO1's score-per-labour is high because the product was text-heavy, 2D, unvoiced (apart from talking heads), and built on a custom engine without third-party overhead.

What it does not tell us:
- Metacritic is a bounded, saturating scale; a point at 89 is not comparable to a point at 60, and aggregates differ by era and platform mix.
- Launch shipments are sell-in, depend heavily on brand, marketing and platform base, and are not creative output.
- Headcounts are inconsistent in definition (Cain's core team, Avellone's developer count, Bethesda's "just over 100"); person-months ignore outsourcing and shared-engine labour that Bethesda games rely on.
- FO2's number is only illustrative; there is no credible headcount.
- Lines of dialogue are not quality, and are counted differently by Guinness and Bethesda.
- Three different studios, tool states and publishers sit behind the five games, so the table shows patterns, not causes.

## 8. What Each Team Spent On vs. What Reviewers and Fans Valued

Spend entries come from the sourced facts above. "Valued" entries combine award and score data with developer statements; where I found no source, the entry is tagged as opinion or consensus and not verified here.

| Game | Where the budget (labour and time) visibly went | What reviewers and the audience rewarded | What the spend missed or wasted |
|---|---|---|---|
| Fallout | A custom engine (6 solo months), a rule system rewritten in about 2 weeks, 8-week talking heads, multiple-solution quest design | 89 Metacritic; reactive dialogue and multiple solutions; strong tone; the tone document survived the licence loss [B] | Late companions (bugs the scripts could not fix); a rating surprise; no tail content |
| Fallout 2 | Doubling the world on about 9 months; reusing the engine; Planescape designers bolted on | 86 Metacritic; breadth and humour [B] | Bugs (the car trunk fix arrived 4 months after launch); uneven story after the founders left; weaker UK sales [B] |
| Van Buren | A new 3D engine (NDL) that Black Isle did not know; a 700-page design document | Nothing shipped. The setting and factions survived and were reused by NV | Time on engine learning, not content; money ran out before a vertical slice convinced executives (Sawyer: execs never visited) |
| Fallout 3 | A first-person open world on Gamebryo; V.A.T.S.; D.C. rebuilt in zones; 40,000 voiced lines; 4 years; two DLC teams started before launch | Game Developers Choice GOTY and Best Writing; 90 to 93 Metacritic; the exploration loop and V.A.T.S. [B] | Cut downtown D.C. (26 to 12 areas); about 30% of dialogue cut late; end-of-cycle burnout and launch bugs; the broken ending triggered a DLC fix (Howard via Windows Central, headline only) |
| New Vegas | Writing, reputation, and faction systems on inherited tech; 65,000 lines in 18 months | 82 to 84 Metacritic at launch; the community needed about 5 years to warm to it (Sawyer); strong long-term reputation [A] | Bugs and console memory problems; the one-point bonus miss; no time to polish or rebalance |
| Fallout 4 | A voiced protagonist (111,000 lines), a new renderer, gun modding, settlement building, 7 years of lead time | GOTY awards; 84 to 88 Metacritic; workshop popularity ("very few people were finishing the game"); shooting feel [B] | Consensus criticism of the simplified dialogue wheel and thin RPG choices (widely held opinion, not sourced here); settlements arguably took scope from quest depth (opinion) |
| Fallout 76 | A new multiplayer netcode on a single-player engine; a 4x map claim; roughly 3 years; multi-studio help; no human NPCs | Mostly nothing at launch (49 to 53). After Wastelanders added human NPCs (April 2020), reviews rose to 63 to 68; sustained play grew | Launch without a proper beta; space without people; heavy QA crunch; staff pulled from other games; a rebuild of the key missing feature after ship |

## 9. Scope Lessons for a Small Original Team

### Cheap and high value

| Feature | Evidence | Why it is cheap |
|---|---|---|
| Text-driven reactivity and skill-checked dialogue | FO1's three solutions per quest; NV's writing on reused tech (about 65 lines per pm in this study's rough arithmetic) | Text and script flags cost writer time, not art, animation or voice. Cain: at least two solutions per quest |
| Ending slides | Used across the classic games and NV (practice widely known; I did not source a cost figure) | A few images and text blocks summarise hundreds of player decisions |
| Faction reputation | NV (Sawyer, Gonzalez) reused the Van Buren factions on a 18-month schedule | A handful of variables drives dialogue, prices and access across the whole world |
| Reused assets and new writing | NV on Fallout 3's tools and engine; FO2 on FO1's engine | The 16-bit upgrade for FO2 was rejected because redoing the art would not fit the schedule |
| A tone document written early | FO1 survived the loss of GURPS and the SPECIAL rewrite in about 2 to 3 weeks | The design vision is cheap to write and expensive to lose |
| Perks and character build variety | Perks were added in one day (Cain) | Content-light, replay-heavy |
| Mod and tool access | FO3's G.E.C.K. reused by NV; long-tail community fixes | Tooling is amortised across games and fans |

### Expensive with weak or uncertain payoff

| Feature | Evidence | Why it cost more than it returned |
|---|---|---|
| A fully voiced protagonist | FO4: 111,000 lines; two actors recorded 13,000+ lines each; about 22 to 32 lines per pm vs. NV's 65 | Each added voiced line locks the script, doubles for two genders, and constrains choice design (opinion on payoff) |
| Voiced everything | FO3 cut about 30% of dialogue to fit the disc; NV's 65,000 lines were done in 18 months, and bugs were the visible price | Voice amplifies late cuts and rework |
| A custom or rewritten engine in a short window | Van Buren's NDL; FO4's renderer rewrite from 2012; FO76's single-player engine pushed into a shared world | Learning cost and unfamiliar bugs take time from content |
| Multiplayer retrofitted onto a single-player engine | FO76: three years, a crunch-heavy QA stage, and a Metacritic of 49 to 53 | The engine "doesn't load except around one player" (Mayer) |
| A large map without populated places | FO76's launch map was empty of human NPCs | Space is cheap to generate and expensive to make meaningful; the rebuild shipped 17 months later |
| Skipping public beta for a live-service launch | Howard's own regret; beta only began Oct 23/30, 2018 | The cost of discovery moves to launch day |
| Schedule compression after scope expansion | FO2's doubling, NV's 18 months, and FO76's fixed date after E3 | Each produced a patch-heavy launch; Urquhart later preferred slipping dates over crunching |
| Contract bonuses on aggregate scores | NV's 85 threshold, missed by one point | Incentives drive resentment, not quality (opinion; Urquhart called the withholding "petty") |

### Rules of thumb (opinion, derived from the data above)

- Budget voice at a fraction of the writing. If a team cannot afford 65,000 voiced lines, record fewer and use text for the long tail.
- Pick one expensive pillar (open world, voice, systemic building, or multiplayer) per game, not three.
- Ship a small vertical slice that an executive or publisher can actually play. Van Buren's demo existed, but nobody with the money looked at it.
- Count the whole team honestly. If your own definition of "team" excludes QA and outsourced work, your schedule will be wrong.
- Put a public test (alpha, beta) in the plan from month one for anything networked.

## Sources

Fetched pages that supplied figures:

- https://en.wikipedia.org/wiki/Fallout_(video_game)
- https://en.wikipedia.org/wiki/Fallout_2
- https://en.wikipedia.org/wiki/Fallout_3
- https://en.wikipedia.org/wiki/Fallout:_New_Vegas
- https://en.wikipedia.org/wiki/Fallout_4
- https://en.wikipedia.org/wiki/Fallout_76
- https://en.wikipedia.org/wiki/Van_Buren_(video_game)
- https://fallout.wiki/wiki/Fallout_2
- https://fallout.wiki/wiki/Fallout_3_add-ons
- https://fallout.wiki/wiki/Fallout:_New_Vegas_add-ons
- https://www.gamedeveloper.com/design/20-years-of-i-fallout-i-lessons-learned-shipping-games-in-the-wasteland (Cain, Urquhart, Howard; team sizes; US$3M)
- https://thiscageisworms.com/2012/04/09/tim-cains-gdc-2012-talk-fallout/ (notes on Cain's GDC 2012 talk)
- https://shacknews.com/article/114982/world-on-fire-the-oral-history-of-fallout-and-fallout-2 (Cain, Boyarsky, Urquhart, Everts, DeMilt, Spitzley)
- https://gameinformer.com/FalloutOralHistory-PartII (Gonzalez, Sawyer, Howard, Pagliarulo)
- https://gameinformer.com/b/features/archive/2015/11/06/the-making-of-fallout-4 (Howard, Burgess, Gardiner; "just over 100"; timeline)
- https://gamerant.com/fallout-4-development-team/ (Gardiner: "just over 100 people")
- https://www.gamedeveloper.com/design/revitalizing-a-heritage-the-writing-of-fallout-3 (Pagliarulo, Sept 2008)
- https://www.gamedeveloper.com/game-platforms/-i-fallout-76-i-devs-say-mismanagement-and-crunch-led-to-buggy-launch (Bryant Francis, June 8, 2022; summarises Sisi Jiang's Kotaku piece)
- https://gamedeveloper.com/production/noclip-shares-a-look-inside-the-making-of-multiplayer-i-fallout-76- (Noclip; Howard, Mayer)
- https://www.nme.com/news/gaming-news/report-alleges-fallout-76-suffered-from-a-disastrous-development-cycle-3243529
- https://mein-mmo.de/en/report-casts-a-grim-light-on-the-development-of-fallout-76-speaks-of-crunch-and-layoffs,835768
- https://gameworldobserver.com/2022/04/11/20-out-of-70-people-from-fallout-new-vegas-team-still-work-at-obsidian-chris-avellone-says
- https://rpgcodex.net/article.php?id=6638 (Larry Liberty interview; five teams)
- https://www.guinnessworldrecords.com/world-records/95609-most-lines-of-dialogue-in-a-single-player-role-playing-game
- https://www.videogameschronicle.com/news/the-original-isometric-fallout-3-wouldnt-have-been-cancelled-if-execs-had-bothered-to-see-it-new-vegas-lead-says/
- https://wnhub.io/news/engines/item-19906 (fan estimate of FO1 cost in 2022)
- https://www.vgchartz.com/article/463207/fallout-76-tops-21-million-players/ (Bethesda 21M, Nov 27, 2024)

Search results consulted (summaries only; page bodies not read in full):

- https://www.pcgamer.com/report-says-fallout-76-development-was-plagued-by-crunch-and-poor-leadership
- https://www.gamesradar.com/report-calls-fallout-76-a-crunch-nightmare-that-drained-staff-and-pulled-devs-from-starfield-and-redfall
- https://www.pcgamesn.com/fallout-4/fallout-4-is-going-to-talk-your-ear-off-with-over-111000-lines-of-spoken-dialogue
- https://twinfinite.net/pc/fallout-4s-two-main-voice-actors-have-recorded-over-13000-lines-of-dialogue/
- https://kotaku.com.au/?p=1360906 and https://www.gamesradar.com/games/fallout/fallouts-co-creator-was-convinced-the-cancelled-og-fallout-3-couldve-shipped-and-been-a-really-good-game-in-18-months-but-money-troubles-got-in-interplays-way (Cain on Van Buren)
- https://www.engadget.com/2012/03/15/obsidian-missed-fallout-new-vegas-metacritic-bonus-by-one-point and https://www.gamespot.com/articles/obsidian-denied-bonus-over-new-vegas-metacritic-score-studio-head/1100-6366337/ (bonus terms; both returned errors on fetch, so facts come from the search summary)
- https://www.pocketgamer.biz/fallout-shelter-accumulates-100-million-in-player-spending-on-mobile
- https://gamersyde.com/news_josh_sawyer_interview-9293_en.html (no figures found)
- https://www.gamespot.com/articles/fallout-76-was-never-expected-to-get-great-reviews/1100-6467300/ (403; search summary only)
- https://mobygames.com/game/239/fallout-2/credits/ (403; the 187-credit figure comes from a search summary only)
- Attempts that failed or returned nothing usable: MobyGames FO1, GamePro DE, PC Gamer FO76 pieces, TweakTown, Windows Central layoffs article, TechRadar FO3 article, web.archive.org (not fetchable from this tool).

Also used from the earlier file: `C:\Projects\post-apoc\research\design-insights\development-history.md` (IP purchase prices, FO2 dates, Troika, leaks, Sawyer and Cain statements).

## Design Takeaways

- **Budget in person-months, not dollars.** The only trustworthy public cost is FO1's (about US$3M for about 750 person-months, roughly US$4,000 per person-month). Plan our own scope as a person-month ceiling per feature before pricing anything.
- **Copy New Vegas's economics, not FO4's.** NV's roughly 65 voiced lines per person-month, reused toolset, five small cross-discipline teams, and faction and reputation systems gave a score within four points of FO4 at about 30% of the labour (rough, derived). Choose inherited or off-the-shelf technology and spend the budget on writing and reactivity.
- **Make text the default and voice the exception.** Voice is the largest visible labour sink in the Bethesda games, forces late cuts (FO3 lost about 30% of its dialogue), and fixes the script. For a small team, voice only key characters and set pieces, and let everything else carry its weight in text.
- **Keep the cheap, high-value features at the core:** multiple solutions per quest, skill-gated dialogue, faction reputation, ending slides, and a written tone document. All were low-cost in the evidence and are the features fans still cite.
- **One expensive pillar per game.** FO4 combined a voiced protagonist, a renderer rewrite, gun modding and settlements; FO76 combined a multiplayer retrofit, a large map and a fixed date. A small team should pick one pillar and cut the rest.
- **Prove a playable slice early and show it to whoever funds you.** Van Buren had a demo that executives never saw; Cain's 12-to-18-month estimate cancelled it. A short, playable, honest vertical slice is both a design tool and a funding tool.
- **Never retrofit multiplayer onto a single-player engine, and never launch networked content without a public beta.** FO76 is the clearest case: about three years, an engine that "doesn't load except around one player," a 49 to 53 launch score, and a rebuild of human NPCs 17 months later.
- **Do not let schedule shrink while scope grows.** FO2 (about 9 months for a doubled world), NV (18 months, bug-heavy), and FO76 (date held after E3) each shipped with visible damage. Urquhart's own conclusion: slip the date rather than crunch.
- **Do not hide QA.** FO1's QA worked unpaid weekends; FO76's QA worked 10-hour, six-day weeks and was told to test builds without the fix. Budget QA as a named line, not as leftover time.
- **Avoid score-linked bonuses and score-driven pay.** The one-point NV miss damaged trust more than any bug. Tie incentives to ship dates, retention and post-launch support instead.
- **Record the missing numbers ourselves.** Public data on word counts, quests, voiced NPCs, budgets and headcount is poor for every Fallout game. Track person-months, lines, quests and cuts from day one so our own postmortem has real data.
