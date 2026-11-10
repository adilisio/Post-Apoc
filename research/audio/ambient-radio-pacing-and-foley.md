# Ambient Craft, Vintage Licensing, Radio Pacing and Foley

Scope: fills the gaps left by `score-analysis.md`, `licensed-music-and-radio.md` and `sound-design-and-voice.md` (same folder). It does not repeat their track tables, intro-song history (the Ink Spots "Maybe" story), station tracklists or voice casting; refer to them. New material here: composer method in the composers' own words, how the music engine behaves (New Vegas is documented in detail, the Bethesda games are not), who curated the licensed songs, the legal calendar for public-domain music, counted radio-dialogue structure with a derived pacing model, and the documented foley and creature work.

Source discipline: `[VERIFIED-PAGE]` means I fetched and read the page. `[SNIPPET]` means only a search-result snippet was seen. `[UNVERIFIED]` means not confirmed. A tool summarised each fetched page, so counts taken from the fandom-style wiki dialogue dumps are approximate and flagged as such.

## Quick Reference

- **Premise corrected:** found-object percussion is documented for *Fallout Tactics* and *Fallout 4*, not *Fallout 3*. Zur's own words for FO3 are "ominous orchestral, even scary" and "mood driven". For FO4 he describes banging garden furniture and bowing a garden chair with a cello bow (Bethesda "Behind the Score" piece).
- **Premise not confirmed:** I found no source naming mandolin, fiddle or dulcimer in the FO76 score. Zur's own FO76 statements say a "more classical approach" with "more traditional instruments" (Wastelanders), plus real-world sounds (birds, cars, wind). Folk instrumentation stays `[UNVERIFIED]`.
- **Morgan's brief (partly secondary):** Morgan says Fallout was "a very dark ambient game" and the team wanted to avoid a conventional orchestral score (PC Gamer 2014, as relayed). A summary of Tim Cain's own video says Cain listed ambient artists he loved (Eno, Aphex Twin, Future Sound of London) and asked audio director Charles Deenen to find someone who could write music that "belonged on CDs with this music". That summary is on a mirror site, so treat it as `[SNIPPET]`. This is the only link I found between Eno and the project, and it is Cain's taste, not Morgan's statement.
- **Vault Archives:** Morgan's free remaster, released 10 May 2010, 24 tracks, FLAC and 320 kbps MP3 `[SNIPPET]` (GameBanshee, GameRanx).
- **New Vegas music engine is documented** (Scott Lawlor, Gamasutra/Game Developer article and GDC 2012): five cue types (scripted, incidental, location, battle, hostile); incidentals are 5-15 second chunks at timed intervals; location tracks have three layers plus day and night versions and low/medium/high mixes.
- **Silence is a designed state.** In NV, when a scripted cue ends "the system will go silent until a new command is given", and the open wasteland uses incidentals that "quietly wisp away... Almost like silence" (Lawlor).
- **Curator:** the licensed songs for FO3, FO4 and FO76 were supervised by Brandracket, LLC (co-founders Christopher S. Parker and Tim Scanlin; Ian M. Anderson coordinator on FO4), not by Bethesda staff. Parker worked with audio director Mark Lampert and Todd Howard. APM Music supplied additional FO76 cues (100+ licensed; a 39-cue APM compilation was released 6 Dec 2018).
- **FO4 curation recipe (Lampert):** roughly thirds of well-known songs, lesser-known songs by famous artists, and obscure bands; "We almost had too much Bing early on." The timeline was left "a little blurry".
- **Dion suit:** filed 2 July 2017, N.D. California, over 1.0 million USD claimed. The song licence came through UMG and Dion alleged he never consented to these ads and called them "repugnant" for violence. Outcome unconfirmed (Wikipedia: arbitration compelled 2018). "The Wanderer" was later removed from the FO4 Anniversary Edition `[SNIPPET]`, cause speculative.
- **Public-domain calendar (US):** pre-1923 recordings entered PD on 1 Jan 2022; recordings from 1923-1946 enter on 1 Jan after turning 100 (1925 recordings entered 1 Jan 2026; 1926 recordings enter 1 Jan 2027). Compositions published before 1931 are PD as of 2026. Not legal advice.
- **Radio counts that are documented:** Radio New Vegas has 13 songs + 6 instrumentals and 50 news stories, of which 42 depend on quest progress; GNR 20 songs total 55:27 (computed); Enclave Radio has 11 intros, 11 outros, 28 transitions, 9 speeches; Diamond City Radio has 37 songs; Appalachia Radio has 50.
- **Radio New Vegas is the shortest rotation with a DJ:** about 19 tracks, roughly 52 minutes if the instrumentals average GNR's song length (estimate). Mojave Music Radio is 15 tracks with no host.
- **Pacing model (derived, section 3.5):** about 19 songs per hour, one DJ link every 2.5 songs, one news block every 5 songs; the song-count rule of thumb is about 1.25 songs per planned game hour.
- **Pip-Boy sound recipe (Lampert, 20k episode of 3 Dec 2025):** everyday clicks, pops and chirps plus recordings of an old 7200 RPM hard drive; page flips trigger drive-style ticks.
- **FO3 footsteps:** about 250 footstep sounds; Lampert removed squeaks that would make an accidental rhythm. FO3 gunfire was partly recorded from real firearms (GameSpy interview, 2008).
- **Gun criticism, evidence level:** FO3 designer Bruce Nesmith calls FO3's real-time gunplay "not good" `[SNIPPET]`. Evidence specific to gun *sound* is mostly fan mods. FO4: Todd Howard says id Software was called early for gunplay tips (Sept 2015 video, via KitGuru); a specific id role in weapon *audio* is `[UNVERIFIED]`.
- **Named people:** Mark Lampert (audio director FO3, FO4, FO76; Oblivion lead sound designer), Scott Lawlor (NV audio director, Obsidian), Andrew Dearing (every NV weapon sound), Ian Nickus (FO76 mixing engineer, per Soundiron), Inon Zur, Mark Morgan, Charles Deenen (Interplay audio director who hired Morgan).
- **Gaps that stayed open:** exact Bethesda music state machine (FO3/FO4/76), Geiger click-rate design, lockpick/terminal audio, deathclaw and radscorpion vocal sources, radstorm audio, how many Daring Dashwood episodes exist, per-song runtimes for NV/FO4/FO76.

## 1. Ambient soundscape craft: Morgan vs. Zur

### 1.1 Mark Morgan (FO1, FO2)

What he said (all `[VERIFIED-PAGE]` unless noted):

| Topic | Statement or fact | Source |
|---|---|---|
| Brief | Fallout was "simply a very dark ambient game"; the developers "knew they liked the ambient vibe" and avoided a conventional orchestral score; he worked with Charles Deenen | PC Gamer 2014, relayed by a tool summary (the article body would not load directly) |
| Goal | To "blend a kind of odd ethnic and industrial sound design into something not only musical, but emotional" | GameBanshee Morgan interview (excerpt) |
| Palette | Early synths: Jupiter, PPG, Moog, Oberheim, Yamaha; first modular synth "blew me away"; a NED Synclavier later became the centre of his sequencing workflow, praised for timing that is "so accurate" yet has "this amazing feel" | Game Informer 2014 |
| Method | "I just think of it as a story in my head"; style is "more of a feel" than a fixed genre; palette also includes tribal, ethnic and sound design | Game Informer 2014 |
| Character of the music | Fallout music "seemed to be very location specific"; FO1/FO2 music "quite tame and almost calming at times" | The Sound Architect `[SNIPPET]` |
| Reference material | Cain gave him a reference CD of Aphex Twin with names omitted (Wikipedia). One fandom wiki says Morgan was given an unlabelled CD and "sampled those tracks directly" `[SNIPPET]`. I could not confirm that on the pages I read | Wikipedia; fandom `[SNIPPET]` |
| Specific similarity claim | A fandom page says "Desert Wind" appears to be a retooled version of Aphex Twin's "Grey Stripe" (Selected Ambient Works Vol. II) `[SNIPPET]`. The fallout.wiki "Desert Wind" page I fetched makes no such claim | `[UNVERIFIED]` |
| Eno | No Morgan statement. Eno appears only in a secondary summary of Cain's video as part of Cain's own listening list `[SNIPPET]` | `[UNVERIFIED]` |
| Time and constraints | Another composer was first assigned; Deenen asked Morgan to deliver in a short window; Interplay set track lengths; no time for rewrites | fallout.wiki "Fallout soundtrack" (Game-OST interview) |

Vault Archives: Morgan remastered selected FO1/FO2 pieces and released them free on 10 May 2010 (Wikipedia; GameBanshee reports 24 tracks in FLAC and 320 kbps MP3 `[SNIPPET]`). The remaster is what New Vegas later licensed: Lawlor "contacted Bethesda and Morgan" and "all parties were fully on board", framing the reuse as an homage to the lineage of the series. In NV Morgan's music is mainly heard in vaults, and some FO3 tracks return at military-technology and Brotherhood areas (Lawlor).

How the Morgan tracks function (analysis, consistent with section 1 of `score-analysis.md`): long, beatless or lightly pulsed beds with industrial hits and tribal percussion, mapped to places rather than to events. The player never hears "combat music" in the sense the later games use it.

### 1.2 Inon Zur (FO3, NV, FO4, FO76)

| Game | Zur's own statements (verified) | Other documented design |
|---|---|---|
| FO3 | Brought in about four months before the game shipped, so the score was written fast (Gamepressure interview). "Take it a little back to the center"; the score is "mood driven"; battle music is new and "rhythmical energetic" while exploration stays mood-driven; a central theme gives "a musical signature" the first game lacked (Bethesda interview via GameBanshee). Level and Gain 2019: "Fallout 3 is a very dark story... essentially about the war for survival"; score is "ominous orchestral, even scary" | He contrasts it with *Tactics*, where he used shouting and banging on chairs and the floor, "not so friendly for listening to it by itself" but effective in game. No FO3 found-object claim |
| NV | Lawlor (not Zur): Southwestern and rural influences with a sci-fi edge; Zur is credited with most of the score | Music system built by Lawlor, section 1.3 |
| FO4 | Main theme recorded on his own grand piano that "will stay with us throughout the whole score"; Howard and Lampert found the first piano too bright, wanted warmer; result "really round and not bright at all but very lush", a real piano blended with electric piano. Main theme uses a minor chord moving to a major to show despair against hope: "You start from the bleak and you go to the hopeful". Percussion from garden furniture and a garden chair bowed with a cello bow, "shrill as hell". Lampert suggested a low accordion as lead; Zur sampled himself on an improvised ocarina. Distinct soundscapes per environment so players know where they are; prioritises "feel" over strongly thematic music (all Bethesda "Behind the Score with Inon Zur" piece) | Level and Gain 2019: score shows "glimpses of hope and beauty, of achievements that can be made". WOSU podcast summary: more melodious and warmer than FO3; accordion; a leitmotif at major moments. An "oil jack in the back yard" percussion story is in a search snippet only `[SNIPPET]` |
| FO76 | Budapest Film Orchestra and Lyris String Quartet; "sophisticated and emotional"; calls it one of his "most unique" scores (Gaming Audio News 2018). Wastelanders: "a more classical approach", "more traditional instruments", some original cues re-harmonised to "fit not only the Appalachian surroundings, but also to enhance the new story"; draws on real-world sounds such as birds, cars and wind (Push Square 2020). Level and Gain: "it's all about rebuilding for the future" | WSHU summary: traditional instruments such as piano and violin used in non-traditional ways; hope/despair duality carried across games. Lampert (same GAN article) talks about rebuilding and the West Virginia landscape. Mandolin/fiddle/dulcimer: no source `[UNVERIFIED]` |

### 1.3 Layer structure: exploration, combat, dungeon, location, and silence

Only New Vegas has a published specification. For FO3/FO4/FO76 the music state machine is undocumented `[GAP]`, so statements about their exact timers would be guesses.

New Vegas (Scott Lawlor, "The Music of the Mojave Wasteland"; GDC 2012 talk "The Music of the Wasteland: Interactive Music in an Open World"; Designing Sound interview, 14 Dec 2010):

| Layer | Behaviour | Role |
|---|---|---|
| Scripted | Highest priority, overrides everything; when it ends the system "will go silent until a new command is given" | Story beats; silence afterwards by design |
| Incidental | 5-15 second random chunks at timed intervals in the open wasteland | Keeps the desert sparse; blends with ambience |
| Location | Three layers: first layer starts on approach, second joins closer, full track at the town centre; reverses on leaving. Day and night versions; low/medium/high mixes to reduce repetition over 100+ hours | Wayfinding by ear; hub identity |
| Battle | Intro, loop, outro for small skirmishes | Combat |
| Hostile | Three layers (explore, tension, battle) switching on the player's threat level | Dungeon-like threat gradient |
| Reactive tone | Goodsprings plays "dark, foreboding" if the player is aggressive and "much lighter, rural" if helpful; controllers key music to faction reputation; template controllers (scary, hostile, mysterious, peaceful, rural, vault) cover the world first, then NCR and Legion paths were refined | Music as reputation meter |

Lawlor on the interaction of music and ambience: they "never wanted them to be fighting each other"; in the open desert music is minimal, short bursts that build near points of interest. He also states the aim that the systems "should go completely unnoticed".

FO3/FO4 design intent from the composers: FO3 alternates mood-driven exploration with new rhythmical battle cues; FO4 uses instrument families to mark area types (see `score-analysis.md` section 4). Observed from play and therefore `[UNVERIFIED]`: long silent stretches between cues in both games, with wind and room tone carrying the gap.

### 1.4 Table: Morgan vs. Zur

| Dimension | Mark Morgan (FO1/FO2) | Inon Zur (FO3 to FO76) |
|---|---|---|
| Instrumentation | Synths (Jupiter, PPG, Moog, Oberheim, Synclavier), samples from libraries and own recordings, drones, industrial hits, tribal/ethnic percussion, sparse guitar | Hybrid orchestra: strings, brass, piano (FO4), accordion and ocarina samples (FO4), Budapest Film Orchestra and string quartet (FO76), electronics, found-object percussion in *Tactics* and FO4 |
| Harmony | Mostly static: drones, modal beds, little functional harmony `[analysis]` | Tonal and cinematic; FO4 theme uses a minor-to-major pivot; FO76 cues re-harmonised for Wastelanders |
| Density | Thin to medium, long slow evolution; music is texture | Varies: sparse ambient in exploration, dense and rhythmic in combat, melodic hubs |
| Emotional target | Desolation, unease, ritual, "calming" detachment | FO3: dread and survival; FO4: bleak to hopeful, personal; FO76: rebuilding and adventure |
| Interaction with gameplay | Location-based tracks in an isometric game; no combat music (Cain's design; combat cues arrive in FO3, per Zur) | Layered location music, battle states, scripted stingers; NV reacts to reputation (Lawlor's system) |
| Production risk | Reference-track imitation controversy; fixed track lengths; no rewrites | Short schedules (FO3 about four months); critics find FO3 score unobtrusive, FO4 sometimes bombastic (GameBanshee reviewer) |

## 2. Vintage licensing strategy

### 2.1 Why 1930s-50s: three reasons

| Reason | Evidence | Confidence |
|---|---|---|
| Tonal irony | Lampert: the atomic novelty songs show "a naive optimism" about atomic technology; he wanted "more of the early rock-n-roll sound" for FO4 (Bethesda "Facing the Music") | Verified |
| Period fit | Fallout's retro-futurist 1950s fiction; Lampert let the timeline be "a little blurry" to admit songs slightly outside it, e.g. Skeeter Davis, 1962 | Verified |
| Cost | Cheng: main reason for the era is "reduced licensing costs"; Bethesda sought Elvis but one song's cost outweighed the variety of the rest (Wikipedia, citing Cheng and Lopez). Cut GNR side quest to let players add their own tracks was rejected by Howard over music rights and tone (fallout.wiki Three Dog) | Verified, secondary |

### 2.2 Who curated

| Person or firm | Role | Evidence |
|---|---|---|
| Brandracket, LLC (Christopher S. Parker, Tim Scanlin) | Music supervision and licensing/clearance: credited on FO76 (fallout.wiki); Parker cited with Scanlin for FO3 and FO76, Parker on FO4 `[SNIPPET]` | fallout.wiki FO76 soundtrack; Bethesda "Facing the Music" ("Chris Parker of Brandracket"); IMDb listing `[SNIPPET]`. Scanlin's surname is spelled "Scalin" on some pages |
| Ian M. Anderson | Music coordinator, FO4 | fallout.wiki / search result |
| Mark Lampert | Audio director; helped license music for FO3 and FO4; wrote and directed RedEye's music (Andrew W.K.); worked with Spank on the "Country Roads" cover | fallout.wiki Mark Lampert |
| Todd Howard | Co-set the vision with Lampert | Bethesda "Facing the Music" |
| APM Music | Production-library catalogue; supplied additional FO76 cues; 100+ licensed; 39-cue compilation released 6 Dec 2018 | fallout.wiki FO76 soundtrack |

So "Christopher S. Parker at Bethesda" is wrong: he is an outside music supervisor (Brandracket). Lampert's quote on the FO4 process: "Chris found a pocket of music that I hadn't heard before." Licensing volume by game is in the sibling file.

### 2.3 Genre mix per game (what each library emphasises)

| Game | Dominant genres (from the sibling file's lists) | Note |
|---|---|---|
| FO3 | Swing and big-band, jump blues, vocal groups (Ink Spots, Andrews Sisters), library/stock cues (Shaindlin, Trede, Brull) | 20-song GNR; stock tracks visible |
| NV | Rat-Pack crooners and torch songs on Radio New Vegas; Western swing and cowboy songs on Mojave Music Radio; some 1979-2009 re-recordings | Lawlor: Radio New Vegas "Rat Pack-era", Mojave "rural and country" |
| FO4 | Pop, vocal groups, rhythm and blues, atomic novelties, plus classical station | Thirds recipe (well-known, lesser-known by famous artists, obscure) |
| FO76 | Swing, Western swing, country, folk and gospel-adjacent (Blind Willie Johnson), Ink Spots, atomic songs, modern covers | 50 songs plus library/pirate/vault stations |

### 2.4 Original recordings in period style

| Item | Detail | Source |
|---|---|---|
| Lynda Carter / Magnolia (FO4) | Original period-style songs; Lampert: "The songs all came together much faster than I expected" | Bethesda "Facing the Music" |
| RedEye (FO4 Nuka-World) | Music by Lampert, performed by Andrew W.K. | fallout.wiki Lampert |
| "Take Me Home, Country Roads" (FO76) | Cover by Spank, worked on by Lampert; charity details in the sibling file | fallout.wiki Lampert |
| NV re-recordings | 1979-2009 recordings of older songs on station lists | Sibling file; whether commissioned is `[UNVERIFIED]` |

### 2.5 The Dion DiMucci case (what the record shows)

- Filed 2 July 2017 in federal court in California against ZeniMax Media; claim over 1,000,000 USD (TheWrap, Game Informer, others, `[SNIPPET]`).
- Theory: the song was licensed through UMG, but Dion's contract let him negotiate payment terms and withhold consent for advertising uses; he says ZeniMax skipped that step and the ads were "repugnant" (violence in a dystopian setting). One outlet claimed the song was in the soundtrack; other reports say trailers and commercials, so I treat that as an error.
- Outcome: Wikipedia says arbitration was compelled in 2018 and gives no final result. A fandom page says dismissed in 2018 and a Steam thread says it was dismissed after forced arbitration, both `[UNVERIFIED]`. A PlainSite docket listing (DiMucci v. ZeniMax Media Inc., N.D. Cal.) is the primary place to check.
- Lampert had said of the song, "We gotta do that song" (GameBanshee relay of an interview). The lesson for contracts: gameplay licence is not advertising licence, and artists can hold approval rights over marketing use.

### 2.6 US public-domain status: compositions vs. sound recordings

Two separate copyrights exist in every song: the composition (words and music) and the sound recording (the specific recorded performance). Timelines as of this writing (Nov 2026), from the Cornell chart and Wikipedia's Music Modernization Act article:

| Item | Public-domain rule | Entering PD examples |
|---|---|---|
| Compositions published in the US | Before 1931 are PD (as of 2026). 1931 works enter 1 Jan 2027 | 1930 compositions entered 1 Jan 2026 |
| Recordings published before 1923 | PD since 1 Jan 2022 (Music Modernization Act, Title II) | |
| Recordings 1923-1946 | PD on 1 Jan after turning 100 (rolling, until 1 Jan 2047). The act added a one-year offset: nothing entered on 1 Jan 2023 | 1925 recordings: 1 Jan 2026. 1926: 1 Jan 2027 |
| Recordings 1947-1956 | 110 years from publication (Cornell chart) | Latest entries run toward 2067 |
| Recordings 1957 to 14 Feb 1972 | Federal protection until 15 Feb 2067 | |
| Derived example | The 1940 recording of "Maybe" is PD in 2041 under the 100-year rule, while its composition is a separate matter | My calculation from the chart; check publication date |

Foreign sources, foreign recordings and local laws differ `[UNVERIFIED]`. Not legal advice.

### 2.7 What an indie team can legally and affordably do

| Option | Legal basis | Cost shape | Risks |
|---|---|---|---|
| Re-record public-domain compositions | You pay performers and engineer; no composition licence if truly PD | One-time recording cost; you own the master | Verify the specific arrangement and lyrics are PD, not just the melody (later arrangements, translations and new lyrics carry fresh copyright) |
| Use PD recordings (pre-1923 now, 1925 and earlier from 2026) | Recording and composition both PD | Almost free; cost is restoration | Digitised copies on archive sites may carry their own terms; check each item; recording quality is lo-fi (a feature for the genre) |
| Production-library licences (APM-style) | Blanket licence for catalogue cues | Subscription or per-cue; FO76 licensed 100+ cues this way | Non-exclusive: others use the same cues; check sync, broadcast and trailer rights separately |
| Commission period pastiche | Work-for-hire or exclusive licence with composer | Fixed fee; lyrics can comment on your world | Needs clear originality brief (see Morgan reference-track lesson) |
| Hero licences | Master + sync from label and publisher | Per-track price unpublished `[UNVERIFIED]` | Marketing uses need separate clearance (Dion) |

Enclave Radio is a worked precedent: its eight tracks are patriotic marches and anthems that are old enough to be PD or historical (fallout.wiki), which made a whole station cheap.

## 3. Radio station pacing

### 3.1 Counts per station

Counts from fallout.wiki station and dialogue pages. Dialogue dumps are line-level and include male/female and Karma variants, so they overstate distinct content; the tool that read them noted truncation.

| Station / host | Rotation | Documented DJ and news structure | Reaction to the player | Reach and gating |
|---|---|---|---|---|
| Galaxy News Radio (FO3), Three Dog (Erik Todd Dellums) | 20 songs, total 55:27, average 2:46 (summed from the sibling file's lengths) | Music intros 14 (2 generic, 12 song-specific), music extros 12, news links 10; PSAs: 21 info lines plus 4 intros; hellos 13; news: 35 generic story lines across 10 topic tags, 6 DLC-tagged | Post-quest news 13 lines; Dad-quest news 8; "Karma titles" about 118 variants; Karma sets: Hope 6, Paradigm 7, Scourge 5; a "player exploit reports" group the tool counted at about 239 `[approximate, unclear grouping]`. Three Dog uses "101" or Karma title. Margaret takes over if he dies and ignores the player | Signal fades with distance from Megaton until the player brings a replacement dish (Virgo II lander, Museum of Technology) to the Washington Monument; then GNR can be heard everywhere. Quest reward 400 XP; +200 Karma on install |
| Herbert "Daring" Dashwood (GNR radio play) | Four episode titles are visible in references: "Escape from Paradise Falls!", "Super Mutant Mayhem!", "In the Black Widow's Web!", "Between Rockopolis and a Hard Place!" | "Jazzy Interlude" frames broadcasts at start and end | Trigger unknown | Total episode count `[UNVERIFIED]` |
| Radio New Vegas (NV), Mr. New Vegas (Wayne Newton) | 13 songs + 6 Gerhard Trede instrumentals = 19 tracks. Runtime: 13 songs about 36 min at the 2:46 average; with instrumentals about 52 min `[estimate]` | Intros 15; news links 8; sponsors 7 (Primm, Vikki and Vance, Ultra-Luxe, Gomorrah, The Tops, Vault 21, Silver Rush); song announcements 12 (3 generic, 9 specific; 4 songs lack one); **news stories 50** | 42 of 50 tied to quest progress: 11 "before completion", 30 "after completion", 1 Boone conditional; 1 at game start; 7 unconditional. Choice-dependent outcomes (e.g. who is sheriff of Primm, NCR annexing Primm, Kings' Gambit). Written by Eric Fenstermaker per Joshua Sawyer | Coverage of the Mojave is implied (the sibling file and Mojave Music Radio page say that station covers the whole Mojave); Lawlor: radio is "heard all over the wasteland" |
| Mojave Music Radio (NV) | 12 songs + 3 Bert Weedon instrumentals = 15; no host | None | Four songs shared with other stations | "Its signal covers the entire Mojave" |
| Black Mountain Radio (NV) | Same music, Tabitha propaganda between songs (sibling file) | | Silenced permanently by a quest | |
| Enclave Radio (FO3), Eden (Malcolm McDowell) | 8 patriotic tracks, 9 speeches | 11 intros, 11 outros, 28 transitions (two without audio); transition quotes attributed to real presidents | Offline if Eden is persuaded to self-destruct; Broken Steel bug takes it offline too | Raven Rock source; Eyebots rebroadcast; first station heard after leaving Vault 101 |
| Diamond City Radio (FO4), Travis Miles (Brendan Hunt) | 37 songs per the page (not counting Magnolia's) | Introductions; main-quest news; faction-specific news (Brotherhood, Institute, Minutemen, Railroad); side-quest news; sponsors; song announcements; song interims. In the portion read: 42 openers, 39 song announcements and 39 interims, all in the confident register | Institute's destruction has versions crediting the Brotherhood, the Minutemen or the Railroad; side-quest stories have alternate endings (Billy reunited or sold to raiders). Confidence arc: before the "Confidence Man" quest Travis mumbles and sometimes shouts; after it and at least one in-game day he speaks with a Transatlantic accent, sometimes calls himself "Lonely" Miles. A news item reports the Sole Survivor leaving Vault 111 as if they had not met, a continuity slip. If killed, Sheng Kawolski replaces him | Frequency 98.0, unlimited range |
| Appalachia Radio (FO76), Julie (Grace Rolek) | 50 songs in the main list (6 more were cut in beta) | Before Wastelanders: automated, no DJ, no commentary. Julie's lines in the first 109 entries: 20 general (12 opening monologue, 4 station IDs, 3 Collectron banter, 1 slogan), 89 song-related across 31 song segments, about 2.9 lines per song | No visible quest-reactive lines; at most about 3 lines refer to people returning to Appalachia | "All of Appalachia and its surroundings" |

### 3.2 Loop structure (what the counts imply)

- **NV (best documented):** an interleave of song, announcement, sponsor, news-link and news story. Announcement pools (15 + 12 + 8) are small, so the *news* pool carries the sense of change; the 50 stories are the main reactivity. The page does not give the exact rotation order, so the loop sequence is `[UNVERIFIED]`.
- **GNR:** many micro-categories (intros, extros, links, PSAs, Karma, deed reports) rather than one big pool. The most reactive material (deed reports, Karma titles) is the largest group.
- **Appalachia:** speech is attached to individual songs (about 3 lines each), a "commentary-per-song" model with little reactivity.
- **Diamond City:** structure mirrors GNR but with separate faction branches for the main quest, so one event spawns up to four variants.

### 3.3 The repetition complaint, counted

| Station | Tracks | Estimated runtime | Notes |
|---|---|---|---|
| Radio New Vegas | 19 (13 songs + 6 instrumentals) | about 52 min `[est.]` | Smallest rotation with a host |
| Mojave Music Radio | 15 | about 41 min `[est.]` | No host, so no variety layer at all |
| GNR | 20 | 55:27 | Computed |
| Diamond City Radio | 37 | about 102 min `[est.]` | |
| Appalachia Radio | 50 | about 138 min `[est.]` | |

Player evidence is anecdotal and search-snippet only: one Steam poster says Radio New Vegas stays enjoyable about 20 minutes before the same few songs cycle; a modder claims the original script only checks whether a song played in the last three or four selections, and fan mods ("No Repeat Day", "Radio Free Wastelands") exist to enforce non-repeat rotation `[SNIPPET]`. With a random pick over N tracks, the expected number of songs before the first audible repeat is about sqrt(pi N / 2): 5.5 songs for N = 19, so roughly 17 minutes at 192 seconds per song-slot. That matches the Steam anecdote without proving it.

### 3.4 Gating

| Method | Example | Reason it works |
|---|---|---|
| Quest repairs signal | GNR dish quest | Player earns the benefit (reach) and Three Dog's gratitude; the world's one voice becomes global |
| Faction-owned broadcast | Enclave Radio, Black Mountain Radio | Silencing it is a quest outcome; cost of silence is felt |
| Host replacement | Margaret, Sheng Kawolski | Failure state changes tone but station survives |
| Host arc | Travis's confidence quest | Delivery itself is progress |
| Late addition | Julie in Wastelanders | Station changes character between content updates |

### 3.5 Derived pacing model (my model, assumptions stated)

Assumptions: average song 166 s (GNR measured). A DJ link of 20 s occurs every 2.5 songs; a news block of 90 s occurs every 5 songs; listeners tolerate R plays per song (R = 4 strict, 6 relaxed, loved songs can pass 8). Players listen to radio for fraction f of play time (assume 0.3 to 0.5). Speech tolerance is lower: about 2 plays per DJ line, 1.5 per news item.

Per song slot: 166 + 8 + 18 = 192 s. Therefore:

| Quantity | Value | Reasoning |
|---|---|---|
| Songs per hour of continuous listening | about 19 | 3600 / 192 |
| DJ links per hour | about 7.5 | 19 / 2.5 |
| News blocks per hour | about 3.75 | 19 / 5 (2 stories per block gives about 7.5 stories/hr) |
| Speech share | about 14% | 26 s of 192 s |
| Minimum songs for H game hours | N = 19 x f x H / R | each song is heard 19 f H / N times |

Worked table (f = 0.4, R = 6):

| Game length H | Listening hours (f x H) | Total plays | Minimum songs N | DJ link lines (R = 2) | News items (R = 1.5) |
|---|---|---|---|---|---|
| 10 h | 4 | 75 | 13 | 15 | 20 |
| 25 h | 10 | 188 | 31 | 38 | 50 |
| 50 h | 20 | 375 | 63 | 75 | 100 |
| 100 h | 40 | 750 | 125 | 150 | 200 |

Rule of thumb: about 1.25 songs per planned game hour at f = 0.4, R = 6. Sanity check against the shipped games: Radio New Vegas's 19 tracks reach an average of four plays after about 4 hours of listening (10 game hours at f = 0.4); FO4's 37 reach four plays after about 8 hours; FO76's 50 after about 11. The sibling file's 40-plus recommendation fits a 30-50 hour game. For longer games the model gives numbers no studio can license, which is why mitigation matters:

- Multiple stations multiply the pool because players pick by taste, not by rotation.
- Tiered unlocks (new songs after milestones) reset perceived repetition.
- Time-of-day blocks and a no-repeat window of at least N/2.
- Make DJ speech count: NV's 50 news stories at R = 1.5 cover about 75 news items at roughly 7.5/hr, about 10 listening hours, which is about right for its 42 quest-linked stories being released over a playthrough.
- All shipped rates in this section are assumptions; I found no developer document giving actual DJ timing or pick logic `[UNVERIFIED]`.

## 4. Environmental foley and world audio

### 4.1 Who and where documented

| Source | Content | Status |
|---|---|---|
| Twenty Thousand Hertz, "The Sound of Fallout: From Iconic Games to Prestige TV", 3 Dec 2025 (https://www.20k.org/episodes/fallout) | Mark Lampert on game design; TV crew Sue Cahill, Daniel Colman, Steve Bucino, Keith Rogers | Verified, best single source |
| Noclip, "The Music & Sound of Bethesda Game Studios" (2018), summarised by Game Developer | Fallout 3 opened "a whole new palette" of electronic sound; electronics that "get hot when they've been on a while" | Video not watched; article read |
| GameSpy Fallout 3 sound interview with Lampert (2008), relayed by GameBanshee | Weapons recorded from real firearms | Verified via GameBanshee |
| Designing Sound interview with Scott Lawlor (14 Dec 2010); Inside the Vault Q&A (fallout.wiki) | NV audio in detail | Verified |
| GDC 2012, Lawlor, "The Music of the Wasteland: Interactive Music in an Open World" (gdcvault 1015602) | NV music system | Description read, video not seen |
| QuakeCon 2010 panel "Let There Be Sound" with Lampert, id Software and Splash Damage designers | Mentioned in GameSpot headline `[SNIPPET]` | Contents not read |
| Soundiron "In the Studio with Fallout 76 composer Inon Zur" | Part three features mixing engineer Ian Nickus on "Dynamic Mixing" (Cubase and Pro Tools) | Verified summary; no instrument list |
| A Sound Effect, "Designing the Fantastic Sound of the Fallout Series" | TV only. Show reused game Pip-Boy and HUD sounds (about 90% of Pip-Boy sounds per 20k) | Verified |

Lampert's employment status conflicts across sources: fallout.wiki lists him as a Bethesda audio director "present", one search snippet says he left in 2023 and 20k calls him a principal sound designer. Treat `[UNVERIFIED]`.

No GDC talk by Lampert on the Fallout games was found.

### 4.2 Device-by-device

| Element | What is documented | Evidence level |
|---|---|---|
| Pip-Boy UI | Built from everyday clicks, pops and chirps plus old PC hard-drive ticks and boot sounds; each page flip triggers drive-style ticks; "mechanical, analog feel"; Lampert's reference point was an old computer or television (20k; Game Developer) | Verified |
| Geiger counter | Built into the Pip-Boy (fallout.wiki). The "clicks get noisier near a source" description is one author's observation, not a developer statement (Krotos blog). Click-rate design | `[UNVERIFIED]` |
| Level-up, death, vault-exit stingers | Named music cues (sibling file) | Verified |
| VATS | NV: sound is "iconic", kept close to the series' original while aiming to "kick it up a notch" (Lawlor). Krotos blog describes an electronic hiss and rhythmic blip (non-developer). Crit sounds | `[UNVERIFIED]` |
| Lockpick and terminals | No documented source found | `[GAP]` |
| Vault doors | Lampert avoided sci-fi sounds: "two big pieces of metal" with hydraulic assist and a pressure release; layered library sounds (20k) | Verified |
| Vault interiors | Lampert aimed for a "sterile" feel "similar to an office" (fallout.wiki Lampert page) | Verified, secondary |
| Footsteps | FO3 has about 250 footstep sounds across wood, grass, gravel, metal; Lampert removed any squeak that would create an unwanted rhythm: "The player does not need to fall in love with the sound of each and every footstep" (20k). NV wood footsteps were layered from a movie set, a ghost town and decaying cabins; Lawlor wanted them "solid and strong, yet gritty and decayed" (Inside the Vault). Panamint City and Paramount Ranch recordings (Designing Sound) | Verified |
| Power armor | FO3: donning is instant; later games made it vehicle-like with hydraulic release, closing sounds and fusion-core insertion, with a different sound inside versus outside the suit (20k). Footstep design details | `[UNVERIFIED]` |
| Weapons, FO3 | Small arms partly recorded from real firearms (a colleague's pistols and rifles; bolts and magazines); built from field-recording libraries with Foley for bass; the starting BB gun is a mix of two pellet guns; exotic weapons reuse small-arms mechanical clanks (GameSpy via GameBanshee, 2008) | Verified |
| Weapons, NV | Aim of "a strong sense of space and distance"; FO3's guns reworked with new distant layers; Andrew Dearing handled every weapon sound; Josh Sawyer checked caliber and power; shell-drop sounds per caliber; the loose-file system sometimes made fire sound less random than intended (Designing Sound) | Verified |
| Weapons, FO4 | Howard: id Software was phoned early to get gunplay tips (KitGuru, Sept 2015, citing a Bethesda video); Game Informer reported Destiny as a reference and a senior systems designer, Josh Hamrick, tuning firearms `[SNIPPET]`. A reworked weapon *audio* pass guided by id | `[UNVERIFIED]` |
| Gun-sound criticism | FO3 designer Bruce Nesmith: FO3's real-time gunplay was "not good" and VATS was a workaround `[SNIPPET]`. Sound-specific criticism appears mainly in fan mod descriptions ("all weapons use the same generic pistol and rifle sounds" for FO4 `[SNIPPET]`), so I cannot confirm a critic consensus on audio alone | `[SNIPPET]` |
| Creatures | Yao guai built from bear recordings and library sounds with Lampert's voice filling gaps; gulper from wet, sticky textures including a mac-and-cheese recording and Lampert's voice; Dogmeat from a real German Shepherd named River (20k). Lampert reportedly voiced feral ghouls across FO3, FO4 and FO76 `[SNIPPET]` | Partly verified. Deathclaw, radscorpion, mole rat: `[GAP]` |
| Ambient beds, NV | Engine feature attached sounds to art objects (one creak on a Goodsprings telephone pole propagates to every pole); fences, billboards, water towers, signs, broken cars got subtle sounds; dawn and dusk loops; one-shots (birds, wind gusts) scheduled by time of day; danger from distant screams, glass breaks and muffled explosions; recordings at Anza-Borrego State Park, a Piru shoot for distant gunfire, a tumbleweed on a highway; Sound Devices 702 recorder and Sanken CS5 mic; Altiverb for perspective; casino walla recorded in Newport Beach bars and a lobby of about 15 developers (Designing Sound) | Verified |
| Ambient beds, FO3 | IGN praised "minimalist" wind-and-dust sound (sibling file). Lampert's palette quote: electronics that "get hot when they've been on a while" | Verified |
| Ambient beds, FO4/FO76 | Krotos blog claims field recordings of factory drones and creaking buildings (not sourced to developers `[SNIPPET]`); Zur uses real-world sounds such as birds, cars and wind as score material (Push Square) | Weak |
| Radstorm and weather audio | No source found | `[GAP]` |
| Interior room tone, vaults | Only the "sterile office" intent and the door recipe. The TV show used metal drones, rattling vents, water in pipes and broken fans for vaults, but that is a show design, not the game | Partly verified |
| Mixing | NV: "The guns should be loud and satisfying and you always need to hear the dialogue" (Lawlor); little bus or snapshot control in the engine, so one solid mix | Verified |

## 5. Audio device to gameplay information to emotional effect

| Audio device | Gameplay information it carries | Emotional effect |
|---|---|---|
| Diegetic radio with DJ | World events, your deeds, where stations are, time of play | Witnessed progress; irony; companionship while alone |
| Ironic licensed song | Era and mood of the lost world; sometimes a plot hint (title as joke) | Bittersweet comedy; dread through contrast |
| Dark-ambient bed (Morgan) | Region type and danger band | Slow unease; a sense of vast emptiness |
| Layered location music (NV) | How close a town or site is; faction mood toward you | Anticipation; reputation made audible |
| Hostile three-layer cue | Threat level inside a location | Tension that rises before the first shot |
| Silence after a scripted cue | A beat is over; you are alone again | Relief, loneliness |
| Geiger clicks | Radiation intensity without a UI element | Anxiety and urgency; physical sense of environment |
| Pip-Boy ticks and clicks | Menu navigation, mode | Tactile ownership of a worn device |
| Level-up stinger | Progress | Reward |
| Footsteps by surface | What you stand on; stealth cost | Groundedness; they must not annoy over thousands of repeats |
| Heavy vault door recipe | Safe/unsafe, breach, entry | Industrial weight; sterile safety |
| Creature call before contact | Type of enemy nearby | Learned dread (`[analysis]`) |
| Distant gunfire, screams, explosions (NV ambience) | Danger exists offscreen | World continues without you |
| Power-armor servo and hydraulics | Armour state, vehicle-like status | Empowerment and bulk |

## Design Takeaways

- **Write the DJ as a three-layer system, not as dialogue.** NV's split (15 intros, 8 links, 7 sponsors, 12 song announcements, 50 news stories with 42 quest-conditional) shows where authored effort pays: the news, not the banter. Spend the budget on reactive news and reuse a thin layer of link lines.
- **Give every major quest a "before", "after" and "failed" news line.** NV's 11 before-completion, 30 after-completion and "For Auld Lang Syne failed" story is a cheap template for making the world feel as if it is watching.
- **Budget songs by the formula, not by gut.** About 1.25 songs per planned game hour at f = 0.4, R = 6 (section 3.5). For a 40-hour game, plan 50 songs, a second station of contrasting taste, and an unlock tier. Shipping 19 tracks and expecting 40 hours of play invites the NV complaint.
- **Do not copy the 1950s.** Keep the function (lost-world cheer over ruins) and pick a different identity: PD-composition re-records in a period we choose, library cues, and 15-25 commissioned in-world songs whose lyrics can name our own catastrophe. Use the Enclave precedent of anthems and marches for a cheap faction station.
- **Use the public-domain calendar.** Recordings before 1926 are PD now; from 1 Jan 2027 the 1926 vintage opens; compositions to 1930 are PD. A Roaring-Twenties/early-jazz identity is legal, cheap and clearly different from Fallout's 1940s-50s. Always clear the specific arrangement and lyrics, and consult a lawyer.
- **Separate game, marketing and soundtrack-album rights in every contract** (Dion; FO3's vinyl needing a different "Easy Living" in the sibling file). Reserve approval-right language for any hero licence.
- **Make the DJ's voice itself the progress meter.** Travis's accent and confidence arc is an audio-only character arc; pair it with a failure state (replacement host). Avoid the continuity slip where the news reports someone the DJ already met.
- **Gate radio reach with a quest.** The GNR dish quest turns reach into a reward and a story; an equally cheap beat is a jammer or hijack that changes content.
- **Specify the music engine up front, in the NV style.** Five cue types, three-layer location tracks, day/night and low/medium/high mixes, battle intro/loop/outro, and an explicit silent state. Write silence as a state with timers (e.g. a no-music window after scripted cues).
- **Let ambience and music share one budget.** Lawlor's rule that music and ambience should never "fight" is the guardrail; lower music ducks under wind and distant events rather than the reverse.
- **Make UI sounds from the fiction.** Pip-Boy came from hard-drive ticks and clicks; Geiger clicks carry radiation. Pick two or three diegetic devices, record real equivalents, and avoid generic UI beeps. Document the recipe as you go (public record on Fallout's sound design is thin).
- **Avoid squeaks and rhythm in repeated sounds.** Lampert deleted footstep squeaks that formed accidental rhythms; budget around 250 footstep samples for a game with several surfaces.
- **Craft a creature library with vocal layers** (animal recordings + the designer's own voice + food textures). Cheap, memorable, and makes early-warning cues possible.
- **Gunfire needs distance layers.** NV's lesson: near/far layers, per-caliber shell drops and a mix that keeps guns loud and dialogue clear. Fix gun audio at the same time as gunplay (FO3 vs FO4), not afterwards.
- **Tell composers what may be borrowed.** The Aphex Twin controversy came from a reference CD with names omitted; write the do and do-not list (mood, tempo, palette yes; melody, samples, signature timbres no).
- **Choose a signature sound for the original score.** Zur's FO4 piano and Morgan's industrial-tribal bed both give instant identity; ours should be a single recognisable timbre carried across hubs and trailers.
- **Hope needs a harmonic plan.** FO4's minor-to-major pivot "bleak to hopeful" is a simple device: pre-agree whether the world's tone arc ends in rebuilding, as FO76 does, and write the main motif to move that way.

## Sources

Fetched and read (summaries only):

- https://fallout.wiki/wiki/Radio_New_Vegas
- https://fallout.wiki/wiki/Mojave_Music_Radio
- https://fallout.wiki/wiki/Galaxy_News_Radio
- https://fallout.wiki/wiki/Galaxy_News_Radio_(quest)
- https://fallout.wiki/wiki/Three_Dog
- https://fallout.wiki/wiki/Three_Dog/Dialogue
- https://fallout.wiki/wiki/Diamond_City_Radio
- https://fallout.wiki/wiki/Travis_Miles
- https://fallout.wiki/wiki/Travis_Miles/Dialogue
- https://fallout.wiki/wiki/Appalachia_Radio
- https://fallout.wiki/wiki/Julie_(Wastelanders)/Dialogue
- https://fallout.wiki/wiki/Mr._New_Vegas
- https://fallout.wiki/wiki/Enclave_Radio
- https://fallout.wiki/wiki/Herbert_%22Daring%22_Dashwood
- https://fallout.wiki/wiki/Mark_Lampert
- https://fallout.wiki/wiki/Geiger_counter
- https://fallout.wiki/wiki/Fallout_soundtrack
- https://fallout.wiki/wiki/Fallout_76_soundtrack
- https://fallout.wiki/wiki/Vats_of_Goo
- https://fallout.wiki/wiki/Desert_Wind
- https://fallout.wiki/wiki/Fallout_Tactics_developer_statements/Interviews/Inon_Zur/Level_and_Gain_Interview_(October_2019)
- https://fallout.wiki/wiki/Fallout:_New_Vegas_Developer_Statements/Interviews/Scott_Lawlor/Inside_the_Vault
- https://www.gamedeveloper.com/audio/the-music-of-the-mojave-wasteland
- https://gamedeveloper.com/audio/obsidian-s-lawlor-original-i-fallout-1-2-i-tracks-in-i-new-vegas-i-as-homage-
- https://gamedeveloper.com/audio/the-sound-design-behind-bethesda-s-i-oblivion-i-and-i-fallout-3-i-
- https://gdcvault.com/play/1015602/The-Music-of-the-Wasteland
- https://designingsound.org/2010/12/14/fallout-new-vegas-exclusive-interview-with-audio-director-scott-lawlor/
- https://www.20k.org/episodes/fallout
- https://www.asoundeffect.com/fallout-series-sound-design/
- https://krotos.studio/blog/fallout-4-sound-effects (author observations, not developer statements)
- https://bethesda.net/en-US/news/facing-the-music-in-fallout-4
- https://fallout.bethesda.net/en-EU/news/fallout-25-behind-fallout-4-score-with-inon-zur
- https://fallout.bethesda.net/en-US/news/fallout-25-celebrating-fallouts-songs
- http://www.gamebanshee.com/kwcw4 and http://www.gamebanshee.com/kx8w3 and http://www.gamebanshee.com/kxa66 and http://www.gamebanshee.com/k6r8a and https://www.gamebanshee.com/kuk9f and https://www.gamebanshee.com/4wr6 (Zur, Lampert, Morgan interviews)
- https://gamingaudionews.com/2018/08/14/inon-zur-continues-to-score-the-fallout-series-with-upcoming-fallout-76/
- https://www.pushsquare.com/news/2020/06/interview_bringing_some_humanity_to_fallout_76_with_composer_inon_zur
- https://www.wshu.org/podcast/music-respawn/2022-11-10/celebrating-fallouts-25th-anniversary-with-inonzur
- https://www.gamepressure.com/newsroom/ive-been-working-on-starfield-for-7-years-music-for-fallout-3-i-h/z357dc
- https://soundiron.com/blogs/news/in-the-studio-with-fallout-76-composer-inon-zur
- https://gameinformer.com/b/features/archive/2014/01/24/music-spotlight-wasteland-2-fallout-new-vegas-composer-mark-morgan
- https://www.pcgamer.com/interview-mark-morgan-composer-on-wasteland-2-fallout-and-fallout-new-vegas (only partial text retrieved)
- https://www.kitguru.net/gaming/matthew-wilson/id-software-helped-build-the-shooting-mechanics-for-fallout-4
- https://en.wikipedia.org/wiki/Music_of_the_Fallout_series
- https://en.wikipedia.org/wiki/Mark_Morgan_(composer)
- https://en.wikipedia.org/wiki/Music_Modernization_Act
- https://guides.library.cornell.edu/copyright/publicdomain

Search-snippet only (page not read):

- Dion lawsuit coverage: https://www.thewrap.com/?p=1668437 , https://gameinformer.com/b/news/archive/2017/07/08/report-39-the-wanderer-39-singer-files-suit-against-zenimax-for-fallout-4-live-action-ads , https://www.gamepressure.com/newsroom/fallout-4s-most-iconic-song-was-removed-from-the-anniversary-edit/z88934 , https://steamcommunity.com/app/377160/discussions/0/1760230437365449045
- Morgan: https://thesoundarchitect.co.uk/?p=2130 , https://gamebanshee.com/kww3q (Vault Archives), https://gameranx.com/updates/id/4345/article/fallout-composer-releases-remastered-soundtracks-for-fallout-1-and-2/ , https://turbo-wiki.pages.dev/tim-cain/interplay/the-music-of-fallout (mirror of a Tim Cain video summary; login-gated), https://medium.com/northwest-jammin/plunderphonics-or-plagiarism-a694de7443d6 (403)
- Gun audio and gunplay: https://pcgamer.com/games/fallout/fallout-3-developer-says-a-remaster-would-have-to-improve-the-not-good-gunplay , https://www.gamespot.com/articles/fallout-4-gun-gameplay-built-with-doom-devs-help/1100-6430602/ (403) , https://www.nexusmods.com/fallout4/mods/10189
- Radio repetition: https://games.softpedia.com/blog/Fallout-New-Vegas-Diary-Radio-Stations-and-Boredom-165799.shtml (403), Steam and Nexus threads surfaced in search
- Brandracket credits: IMDb listing, https://dev.fallout.wiki/wiki/Tim_Scanline
- Lampert panels: https://gamespot.com/articles/designers-from-id-software-splash-damage-and-bethesda-talk-game-audio/1100-6273499/ (403)
