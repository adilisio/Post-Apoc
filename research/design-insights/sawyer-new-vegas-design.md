# Josh Sawyer and Obsidian on Fallout: New Vegas Design (Primary-Source Study)

Purpose: ground the Sawyer positions that `designer-lessons.md` left as `[UNVERIFIED - from memory of public talks]`, using the developers' own words, for use on an ORIGINAL post-apocalyptic RPG (we study, we do not copy Fallout names, text or art).

How this file was built: the best material came from three places that could be read in full. (1) Sawyer's own GDC 2012 slide deck (PDF he linked himself), (2) the Formspring Q&A archive 2010-2013 (about 2 MB of text), which I downloaded and searched locally so quotes could be checked word for word, and (3) the JSawyer mod readme that he distributed. Interviews and press write-ups were read through a fetch tool that summarises pages; where an outlet returned only a headline, that is flagged. Quotes are kept under 25 words. Anything not confirmed is tagged `[UNVERIFIED]`. Dates are as given by the source; Formspring entries are cited by the date the answer is stamped with in the archive.

## Quick Reference

- Karma is nearly cosmetic in New Vegas; reputation per faction does the real work. Sawyer, Formspring 11 Jan 2011: Karma has "very little effect" and is "mostly just there for player feedback". He agreed (5 Oct 2012) that reputation beats a simple morality meter.
- Sawyer calls himself a "moral relativist" and declined to name the good guys (Formspring, 16 Nov 2010). The design intent for NCR vs Legion was that players first read NCR as good and Legion as bad, then see NCR's dark side and Legion's positives (7 May 2012).
- Admitted flaw: the Legion's positives "did not happen" because the Legion areas east of the Colorado were cut (7 May 2012). Legion is "by far the least frequently selected ending" (4 May 2012). Three extra Legion locations were planned (28 Oct 2011).
- Kill policy: any visible non-child NPC can be killed without blocking the critical path (Sawyer, 27 Nov 2010 and 9 Dec 2012). Exceptions (Oliver, Lanius) were cutscene cases. Failed-quest messages are shown on purpose so players know what they locked out (18 Oct 2012). The main quest falls through to Yes Man (18 Jun 2011).
- Dialogue skill checks are flat thresholds because random checks "just lead to save-scumming" (27 Jul 2011). "Randomized resolution of stand-alone tasks is pointless" with unlimited save/reload (26 Feb 2012). A failed check never leaves the player worse off than before.
- Sawyer's later self-critique: a visible unlocked skill option implies "you should pick it", which weakens role-playing (Sawyer, GDS Prague, May 2024; GDC 2012 slides "Choice Conflict"; Formspring 9 Jul 2012).
- Skill checks should be spread over every skill and front-loaded in the opening; Goodsprings was built so every tagged skill pays off (Sawyer YouTube video on distributing skill checks, Aug 2024; Human Can Opener podcast, 2026).
- Armor: Sawyer brought back Damage Threshold so light and medium armor stay viable; shipped DT floors damage at 20% (Formspring 2 Oct 2011). He zeroed armor DR to reduce balancing variables (29 Aug 2011) and later said DR should have had a larger role (2022 armor talk, via RPG Codex).
- Weapon tier = skill requirement: 0, 25, 50, 75, 100 give Tiers 1-5 (Formspring 31 May 2011). Mods and ammo subtypes are store-only on purpose, as a money sink (26 Sep 2011).
- Skills in real-time gunplay: he blames "terrible weapons plus low skill" for random-feeling shots in shooty RPGs (Formspring 24 Aug 2011). He removed Big Guns and folded those weapons into other skills (GDC Europe 2011).
- Hardcore Mode: design intent was a combat and inventory challenge "without simply scaling hit points and damage" (411mania/Planet Fallout 2010), with needs borrowed from S.T.A.L.K.E.R.: Call of Pripyat. His verdicts: "I don't think Hardcore Mode is 'really' hard" (30 May 2012); would retune rates and food/drink availability (17 Jul 2012).
- JSawyer mod (readme 9.29.12): base carry weight 150 to 50, base HP quartered then set to 50, level cap 30 to 15 (35 with all DLC), hunger/thirst/sleep rates doubled, food and water drops "dramatically lower", plain stimpaks uncommon.
- Level design: deathclaws at Quarry Junction and a "monster badlands" north of Goodsprings were deliberate. Sawyer: players who "attempted to bulldoze their way through" mostly failed; the game did not block them (Formspring 19 Aug 2011).
- Invisible walls: used for four reasons; Sawyer says in retrospect most should have been dropped and the player shown ugly terrain (5 Dec 2012). Strip and Freeside were split into load zones because of console memory crashes (3 Apr and 19 Oct 2011).
- Schedule: "about 18 months" (27 Dec 2011), the hardest task was fixing world scope 18 months before release; it "became marathon-like" (2 Feb 2011). Not enough time to polish: he regrets shipped content with bugs ("less content, fewer bugs would have been better", 9 Apr 2011).
- His clearest named design failure: Charisma had no clear benefit, so players treated it as a dump stat (13 Dec 2011). His rule: if players call a stat a dump stat, "you probably screwed up".
- Cut content: post-ending play (decision by Sawyer, 1 May 2012), Legion camps east of the river, romances ("not enough time"), Ulysses as companion (cut "very late").
- Estimated cost of the wish list (more Legion, post-Hoover play, more side dungeons, more testing): 5-8 months (7 May 2012).
- General principle he repeats: clarity of mechanics over hidden depth ("RPG mathematics should [not] be overly fiddly", 7 Apr 2010; "mechanical clarity is more important than immersion", GDC blog follow-up 2012).

## Source key

IDs are used in the tables below. "Read" says how the text was accessed. Full URLs are in `## Sources`.

| ID | What | Read |
|---|---|---|
| S1 | Sawyer, GDC 2012 slides "Do (Say) The Right Thing" (PDF, 5 Mar 2012) | Full text extracted and read |
| S2 | GDC Vault page for the same talk (abstract only; video paywalled) | Abstract only |
| S3 | fallout.wiki page for the talk with Sawyer's blog follow-up and slide link | Via summarising fetch tool |
| S4 | Christian Nutt, Game Developer, "GDC Europe: Obsidian's Five Hard Lessons Of RPG Design", 17 Aug 2011 | Via fetch tool |
| S5-S8 | Sawyer's Formspring Q&A, archive pages for 2010, 2011, 2012, 2013 on fallout.wiki | Downloaded, searched locally, quotes verified verbatim |
| S9 | JSawyer mod release notes (Sawyer, version 9.29.12), file `JSawyer_READ_ME.txt` | Downloaded and read |
| S10 | fallout.wiki Mod:JSawyer and Mod:JSawyer/Documentation | Via fetch tool |
| S11 | fallout.wiki Hardcore mode | Via fetch tool |
| S12 | Kevin Kelly, Engadget, interview with Sawyer, 5 May 2010 | Via fetch tool |
| S13 | Chris Faylor, Shacknews, dev Q&A (Sawyer, Urquhart), 5 May 2010 | Via fetch tool |
| S14 | GameBanshee, 13 Oct 2010, summarising Planet Fallout interview | Via fetch tool |
| S15 | GameBanshee, 5 Jun 2010, quoting Xbox360Achievements interview | Via fetch tool |
| S16 | RPG Codex posts: OXM preview (16 Apr 2010), 411mania interview (16 Sep 2010), Planet Fallout skills (14 Oct 2010), DT confirmation (2 May 2010) | Via fetch tool |
| S17 | The Guardian interview with Sawyer, 10 Nov 2010 (via fallout.wiki) | Via fetch tool |
| S18 | Kat Bailey, US Gamer, "The Making of Fallout: New Vegas" (Sawyer, Urquhart, Avellone), 13 Sep 2017 (via fallout.wiki) | Via fetch tool, secondhand |
| S19 | John Gonzalez, GDC Online talk write-up by Kris Graft, Game Developer, 6 Oct 2010 | Via fetch tool |
| S20 | Sawyer YouTube video on distributing skill checks (Aug 2024) as reported by 80.lv (6 Aug 2024), David Wu mirror (5 Aug 2024), GamesRadar mirror (6 Aug 2024) | Secondhand reports |
| S21 | Gameranx, 18 Nov 2022, Sawyer on Kinda Funny Games | Secondhand report |
| S22 | Feed4Gamers, 29 May 2024, Sawyer at GDS Prague | Secondhand report |
| S23 | PC Gamer (via Yahoo), 23 Apr 2024, Sawyer in Rock Paper Shotgun interview | Secondhand report |
| S24 | In Game News, 28 Jun 2026, Sawyer on Human Can Opener podcast | Secondhand report |
| S25 | RPG Codex: Sawyer's 2020 reputation talk (6 Apr 2020) and 2022 armor talk (23 May 2022) | Secondhand reports |
| S26 | 80.lv, 16 Aug 2024: Goodsprings/deathclaws/cazadores remarks | Secondhand report |
| S27 | Engadget, 30 Dec 2011, on the JSawyer mod | Via fetch tool |
| S28 | GameBanshee, 17 Jul 2017 (Steemit interview) and 5 Jan 2011 (social interview) | Via fetch tool |
| S29 | The Outer Haven, 2 Jul 2025, Sawyer on granular difficulty (cites PC Gamer) | Secondhand report |

## 1. Choice and consequence over binary morality

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Karma "has very little effect"; mostly player feedback; only Cass reacts to it; it shows in the end slides | Sawyer | Formspring, 11 Jan 2011 | S6 |
| Karma matters to Cass and Mortimer and appears in the slides | Sawyer | Formspring, 29 Dec 2011 | S6 |
| Karma was a tuning mess: killing "Evil" actors gave about 50x more good Karma than "Very Evil" (values 100 vs 2); "no one on the team remembers changing" them | Sawyer | Formspring, 28 Dec 2011 | S6 |
| He agrees a reputation system beats a simple morality meter | Sawyer | Formspring, 5 Oct 2012 | S7 |
| Earlier reputation and morality systems (Ultima, Darklands) were often "inherently punitive" to bad players | Sawyer | Formspring, 13 May 2010 | S5 |
| "Each community and organization ... has its own reputation tracker for the player"; mixed standing carries its own consequences | Sawyer | Xbox360Achievements interview, summarised by GameBanshee, 5 Jun 2010 | S15 |
| Reputation score is easier and more flexible than quest variables for NPCs the player meets often | Sawyer | Formspring, 23 May 2010 | S5 |
| In slides: Alpha Protocol and New Vegas reputation are "Indirect Reaction Systems"; small or non-scripted responses feed a larger system | Sawyer | GDC 2012 slides | S1 |
| He was "not championing karma systems"; he supports visible GUI feedback for indirect reaction systems because "mechanical clarity is more important than immersion" | Sawyer | Blog follow-up to GDC 2012 | S3 (tool-extracted; wording not verified word for word) |
| "I am a product of my LIEberal arts education and consequently, a moral relativist"; will not name the good guys | Sawyer | Formspring, 16 Nov 2010 | S5 |
| Intent: most players first see NCR as "good guys" and Legion as "bad guys", then see NCR's dark side and Legion's positives | Sawyer | Formspring, 7 May 2012 | S7 |
| Legion's positives "did not happen, in large part because the Legion areas east of the Colorado were cut" (admitted flaw) | Sawyer | Formspring, 7 May 2012 | S7 |
| Legion is "by far the least frequently selected ending": rank-and-file misogyny, no Legion companion, few Legion locations | Sawyer | Formspring, 4 May 2012 | S7 |
| Wishes the Legion had "more locations, characters, and quests of their own" | Sawyer | Formspring, 28 Feb 2011 | S6 |
| Three more Legion locations were planned east of the Colorado; cut for time because areas near the map edge were built last | Sawyer | Formspring, 28 Oct, 29 Oct 2011 and 2 Jul 2011 | S6 |
| Ulysses was meant as a Legion-oriented companion in the core game; cut "very late" | Sawyer | Formspring, 4 May 2012 and 29 Jan 2012 | S7 |
| He would rather have "strong opinions about a well-defined enemy" than a generic bad faction | Sawyer | Formspring, 15 Dec 2010 | S5 |
| Legion is "highly ethical, efficient, and disciplined" yet misogynistic in practice; NCR is "fraught with bureaucratic inefficiency, corruption, and imperialist tendencies" (as reported) | Sawyer | The Guardian, 10 Nov 2010 | S17 |
| Legion is "really nasty and bad" but not an evil faceless organisation; NCR is not always good | Sawyer | Shacknews, 5 May 2010 | S13 |
| Avellone wanted players to "at least consider an alternate perspective" on the NCR | Avellone | US Gamer, 13 Sep 2017 | S18 |
| Faction pacing goal: avoid a faction choice early that limits exposure to the others, and avoid a late choice that makes earlier play irrelevant; a "slow path to forming an allegiance" | Sawyer | Formspring, 6 Jan 2011 | S6 |
| Rule: any character in line of sight can be killed (not children). Oliver and Lanius violate it; cutscene control was "preferable" to bulletproof glass | Sawyer | Formspring, 27 Nov 2010 | S5 |
| He personally required that any non-child NPC could die and the critical path still be completable | Sawyer | Formspring, 9 Dec 2012 | S7 |
| The game tells you when you have locked out content; hiding it would not help decisions | Sawyer | Formspring, 18 Oct 2012 | S7 |
| If every faction leader dies, the main quest "should always fall through to Yes Man/Independent" | Sawyer | Formspring, 18 Jun 2011 | S6 |
| Yes Man was a failsafe for the player; Gonzalez, in hindsight, thinks the questline may let players avoid "getting your hands dirty" | Gonzalez | PC Gamer headline only (body not readable); date not confirmed | [UNVERIFIED] detail |
| Ending slides are not tidy on purpose: players should be satisfied "but ... not completely satisfied"; there should be "something to wrestle with" | Sawyer | Formspring, 28 Nov 2011 | S6 |
| He will not name a canonical ending; the player's chosen ending is the right one | Sawyer | Formspring, 31 Dec 2011 and 24 Apr 2012 | S6, S7 |
| GDC 2012 slides: "Anything Goes, at any Scale (Kill Everyone)"; "Reverse-Triple-Cross Capable"; lots of scripted reactivity | Sawyer | GDC 2012 slides | S1 |
| GDC 2012 slides: forecast consequences ("Intrigue the player, but inform them"; "Surprise the player, but don't anger them"; "Lace consequences with sacrifices") | Sawyer | GDC 2012 slides | S1 |
| GDC 2012 slides: validate all options to avoid "Win" / "Loss"; a clear response and reactivity spectrum must be reinforced so "player benefits and character roles align" | Sawyer | GDC 2012 slides | S1 |
| Blog: validating every option does not make them equal; in a Greek dilemma both options "contain virtue and sacrifice" | Sawyer | Blog follow-up | S3 (tool-extracted) |
| Gonzalez: "frame the choices ... so that the player is directly participating"; themes found were greed and a rigged "machine" | Gonzalez | GDC Online, Oct 2010 (Game Developer, 6 Oct 2010) | S19 |
| Reputation systems as a design form have reached a dead end for Obsidian; wants mechanics nearer "standard scripted choice & consequence" (2020 view) | Sawyer | Reputation talk, Apr 2020 (RPG Codex report) | S25 |

Notes
- The "kill anyone" rule is a systems commitment: it forced Obsidian to write fallbacks (Yes Man, item boxes so players need not murder NPCs for loot, Formspring 5 Jun 2011).
- Karma is therefore a clear case of a feature kept for continuity, then admitted to be weak. Our game should not carry a morality meter out of habit.

## 2. Speech and skill checks: thresholds versus percentage rolls

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Asked threshold or dice: "In a computer/console environment with reloading, direct comparisons always." | Sawyer | Formspring, 19 Jun 2010 | S5 |
| A stand-alone randomised check "effectively leads to save-scumming and isn't a viable solution" | Sawyer | Formspring, 7 Dec 2010 | S5 |
| Visible [skill xx/yy] check was "an improvement from the randomized checks"; random dialogue checks lead to save-scumming | Sawyer | Formspring, 27 Jul 2011 | S6 |
| Fail options "never result in the player being worse off"; they show a check exists and how far you are from it; there is alternate (ideally entertaining) fail dialogue | Sawyer | Formspring, 27 Jul 2011 | S6 |
| Removing the Speech percentage roll: "Randomized resolution of stand-alone tasks is pointless" with unlimited save/reload | Sawyer | Formspring, 26 Feb 2012 | S7 |
| People only save-scum on stand-alone checks such as dialogue comparisons or forcing locks; combat randomness "normalizes" | Sawyer | Formspring, 27 Jul 2011 | S6 |
| FO3 had randomised skill checks; FO3 and NV both still had randomised Force Lock | Sawyer | Formspring, 18 Aug 2011 | S6 |
| Disliked FO3's "randomization and the save scumming that resulted" | Sawyer | Kinda Funny Games, reported by Gameranx 18 Nov 2022 | S21 |
| Anti-save-scum was planned before the gambling minigames existed; random roulette and slots would be "kind of pointless" without a disincentive | Sawyer | Formspring, 15 Nov 2010 | S5 |
| Lockpick and hacking alternatives: flat check from invested points (no minigame), or a skill-influenced minigame; he prefers either to a randomised check in a save-anywhere game | Sawyer | Formspring, 8 Sep 2011 | S6 |
| Skill-based dialogue options need more detail and specificity than general options (style guide rule) | Sawyer | Formspring, 25 Nov 2011 | S6 |
| Writers were told not to "shove words into the player's mouth"; the exception is stat, skill or perk unlocks | Sawyer | Formspring, 17 Nov 2010 | S5 |
| Many perks, skills and traits unlock dialogue; coverage was inconsistent for some | Sawyer | Formspring, 16 Dec 2010 | S5 |
| "Using skills in conversations is an emphasis for us"; every skill, including Explosives and Barter, can appear in dialogue | Sawyer | OXM preview, via RPG Codex 16 Apr 2010 | S16 (summarised) |
| Barter was underused in FO3; in NV it applies to negotiations involving numbers or rewards | Sawyer (as reported) | 1UP preview, reported in search results, 2010 | `[UNVERIFIED]` page not opened |
| Spread checks across skills: no earlier Fallout supported every path in every quest; paths are "tools that can be used regularly", not separate courses | Sawyer | Formspring, 31 Mar 2011 | S6 |
| Goodsprings was designed so each skill a player might tag had a use in the opening; goal "we're paying attention to the character that you made" | Sawyer (area built by Eric Fenstermaker) | YouTube video, reported 5-6 Aug 2024 | S20 |
| Checks should be "frontloaded"; they can thin out later, but rewards must continue "over time" | Sawyer | Same video, Aug 2024 | S20 |
| Tuning is "all about feelings ... But you use numbers to arrive at that feeling"; Obsidian tracks check counts with a script-tracking tool; overused skills get split, underused ones merged | Sawyer | Same video, 6 Aug 2024 | S20 |
| "Karma Police" internal audit makes sure each skill has enough to do; Big Guns removal spread weapons over Guns, Energy Weapons, Explosives | Sawyer | Human Can Opener podcast, as reported 28 Jun 2026 (In Game News) | S24 |
| He wants every skill "useful in a really meaningful and unique way" | Sawyer | Same podcast | S24 |
| Speech-as-skill-unlock (NV) and dialogue puzzles (Deus Ex: Human Revolution) both create an "optimal/correct answer" that conflicts with role-playing; "the main subject of my GDC talk" | Sawyer | Formspring, 9 Jul 2012 | S7 |
| NV's flat checks implied "if you ever saw your option come up, you should pick it" and removed role-play | Sawyer | GDS Prague, reported 29 May 2024 | S22 |
| GDC slides, "Choice Conflict": doing the "Right Thing" conflicts with being the "Right Character" (Deus Ex "social boss battles" vs NV "skill, SPECIAL and perk checks") | Sawyer | GDC 2012 slides | S1 |
| Speech checks are "not consistently low, but yes, it's an easy game" | Sawyer | Formspring, 18 Jul 2011 | S6 |
| Skill magazines as temporary boosts; skill formula forces specialisation ("New Vegas forces players to specialize their characters more") | Sawyer | Planet Fallout interview via RPG Codex, 14 Oct 2010 (specialisation only) | S16. Magazines: `[UNVERIFIED]` as a Sawyer statement; only fan-wiki descriptions found |
| Exact "[Speech 45]" style display and the specific threshold values in the shipped game | n/a | n/a | `[UNVERIFIED]` here as a Sawyer statement; the display format is confirmed only by his 27 Jul 2011 answer ("Skill[xx/yy]") |

Notes
- Two layers: (1) fixed thresholds shown to the player, chosen to kill save-scumming; (2) in 2024 Sawyer says this created "pick the unlocked option" play. The newer Obsidian view (Pentiment) is that an available option may be a bad idea, signalled through in-world reaction.
- The "no worse off for trying" tenet is the part that makes visible thresholds acceptable; it is cheap to copy.

## 3. Systems design

### 3a. Damage Threshold and armor

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Confirmed "damage threshold is returning to the Fallout series" | Sawyer | Reported by RPG Codex, 2 May 2010 | S16 |
| Against weak attacks, light and heavy armor can reduce damage equally; DT benefit "maxes out at 80% reduction", so it stops mattering whether the shot hits T-45d or combat armor | Sawyer | Formspring, 1 Jan 2011 | S6 |
| Wanted Light and Medium armor viable as well as Heavy; shipped min-damage 20%; in F1/F2 Power Armor was "always" the optimal choice, which "limits player choice too much" | Sawyer | Formspring, 2 Oct 2011 | S6 |
| Weight classes (Light, Medium, Heavy) set movement in "distinct increments"; FO3 used a fine sliding scale | Sawyer | Formspring, 2 Oct 2011 | S6 |
| DR "has limited scalability" and odd effects (blocks ten bullets of explosion damage, none of a small bullet); he zeroed armor DR "because we were switching systems entirely" and to limit variables | Sawyer | Formspring, 29 Aug 2011 | S6 |
| If DR is combined with DT, keep DR low (about 25% max) to help against explosions | Sawyer | Formspring, 29 Aug 2011 | S6 |
| Favoured model: DT or DR, ideally a combination as in F1/F2; with more time NV would have given DR a bigger role | Sawyer | 2022 armor talk, RPG Codex 23 May 2022 | S25 |
| Light armors are rarely worth wearing ("bad DT and low CND") so he added skill bonuses to make them a choice | Sawyer | Formspring, 22 Jun 2012 | S7 (tool-extracted; not locally re-verified) |
| Weak guns can hurt power armor deliberately so late game is not trivial | Sawyer | Forum remark quoted by search summary | `[UNVERIFIED]` wording and date |

### 3b. Weapons, ammo, tiers, skills

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Tier follows skill requirement: 0 / 25 / 50 / 75 / 100 = Tier 1 / 2 / 3 / 4 / 5; placement by efficacy relative to similar weapons and distinct role | Sawyer | Formspring, 31 May 2011 | S6 |
| Same-ammo weapons are kept within about 25% of base damage (as reported) | Sawyer | Formspring, 5 Jun 2011 | S6 (tool-extracted) |
| Every ammo type is used by at least two weapons (few exceptions); subtypes do not drop; 5.56mm is the only caliber used at all power levels | Sawyer | Formspring, 16 Jan 2011 | S6 |
| "I wanted mods to be a money-sink"; mods and most ammo subtypes are vendor-only | Sawyer | Formspring, 26 Sep 2011 | S6 |
| Wanted players to buy some ammo types and craft others | Sawyer | Formspring, 13 Dec 2011 | S6 |
| Crafting: more useful to let players craft consumables than standard weapons and armor | Sawyer | Formspring, 5 Mar 2011 | S6 (tool-extracted) |
| Players found the ammo crafting too detailed | Sawyer | Formspring, 7 Dec 2011 | S6 (tool-extracted) |
| Cowboy and Grunt damage bonuses were too high ("a bit high"); mod lowered them to 20% | Sawyer | Formspring, 30 Sep and 28 Dec 2011; readme | S6, S9 |
| Weapons are "tuned" by feel and numbers; "mostly vibes based" per later headline (body unread) | Sawyer | GamesRadar headline | `[UNVERIFIED]` body |
| Wanted "the weapon to feel good to use" while giving each a role; "I don't really view RPG and FPS as separate genres" | Sawyer | Engadget, 5 May 2010 | S12 |
| FO3 and NV model no recoil, only fixed spread that rises with limb condition and movement | Sawyer | Formspring, 21 Feb 2011 | S6 |
| Shooty RPGs feel random because "the bad condition stat of the weapon and the character's low skill" combine with spread; CoD uses progressive recoil | Sawyer | Formspring, 24 Aug 2011 | S6 |
| Removed Big Guns: "we got rid of the big guns skill and pushed those guns into other gun categories" (those weapons were rare and late) | Sawyer | GDC Europe 2011, Game Developer 17 Aug 2011 | S4 |
| In hindsight he would fold skills further (Guns and Energy; Melee and Unarmed; Explosives alone) and shrink point pools | Sawyer | Blog "Fallout weapon skills", 2012 | fallout.wiki page, tool-extracted |
| Melee and Unarmed are "feast or famine"; zero DPS between punches, high exposure | Sawyer | Formspring, 9 Jan 2011 and 10 Sep 2011 | S6 |
| Looping reload weapons were harder to implement than expected; with hindsight he would have cut or simplified them | Sawyer | Formspring, 11 Apr 2011 | S6 (tool-extracted) |

### 3c. Perks, traits, level cap, companions, disguise

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Perk every two levels "to make those perk slots more valuable and to make character builds more distinctive" | Sawyer | Formspring, 31 Dec 2011 | S6 |
| Skill points make maxing harder; fewer permanent skill boosts; "New Vegas forces players to specialize" | Sawyer | Planet Fallout, via RPG Codex 14 Oct 2010 | S16 |
| Level cap: he sees little value in raising it, but many players do; 50 levels "takes a relatively long time" | Sawyer | Formspring, 27 Mar and 4 May 2011 | S6 (tool-extracted) |
| He did not design the level increments, traits or perks beyond the core game and Honest Hearts | Sawyer | Formspring, 16 Jul 2011 | S6 |
| Trait respec was possible only as a one-off DLC exception; supporting respec needs planning from the start | Sawyer | Formspring, 19 Aug 2011 | S6 |
| Wanted respec available at a "significant cost" | Sawyer | Formspring, 19 Aug 2011 | S6 |
| GDC Europe 2011: no strong reason to deny respecs; strategic mistakes found 20-30 hours in "feel very bad" | Sawyer | Game Developer, 17 Aug 2011 | S4 |
| Companion Wheel is "much quicker" than FO3; he kept it simple (stimpaks only for items) | Sawyer | Planet Fallout via GameBanshee 13 Oct 2010; Formspring 4 May 2011 | S14, S6 |
| He designed all companions at concept level; others wrote the dialogue | Sawyer | Formspring, 21 Dec 2011 | S6 |
| Companions are strong and hard to compare, which hid Charisma's value | Sawyer | Formspring, 13 Dec 2011 | S6 |
| Companions in Dungeon Siege III dealt and took 25% damage so they need no babysitting (contrast with NV) | Sawyer | GDC Europe 2011 | S4 |
| Faction disguise system (design rationale) | n/a | n/a | `[UNVERIFIED]`: the GDC talk reportedly covers it (third-party summary), but the slides read do not mention disguises and no Sawyer statement was found |
| Trait reintroduction (design rationale) | n/a | n/a | `[UNVERIFIED]` as a Sawyer statement; he disclaims trait authorship outside core and Honest Hearts |

## 4. Hardcore Mode: intent, rules, later verdict

### 4a. Design intent (Sawyer)

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Born from wanting "increased level of challenge ... without simply scaling hit points and damage"; enjoyment depends on "general gaming tastes" more than Fallout experience | Sawyer | 411mania, via RPG Codex 16 Sep 2010 | S16 |
| "Hardcore is separate to difficulty"; a mechanical shift, compared to Ninja Gaiden | Sawyer | Xbox Live interview, reported 16 Feb 2010 | GameBanshee 16 Feb 2010 (secondhand via forum summary) |
| "It really does make a pretty big change in how you play"; think more about what gear to take | Sawyer | Engadget, 5 May 2010 | S12 |
| Healing always happens over time; meters for dehydration, starvation, sleep deprivation; optional, with an achievement for finishing | Sawyer | Planet Fallout, GameBanshee 13 Oct 2010 | S14 |
| The "needs" came from S.T.A.L.K.E.R.: Call of Pripyat because maintaining them "seemed to be a regular concern without being annoying" | Sawyer | Formspring, 26 Mar 2011 | S6 |
| "The point of Hardcore Mode was to introduce a game mode that changed the combat and inventory mechanics" for another layer of challenge; mechanics were exposed in the GECK for modders | Sawyer | Formspring, 19 Mar 2011 | S6 |
| Wanted Hardcore because a "significant chunk" of the audience wanted something tougher than the base game | Sawyer | Formspring, 30 May 2012 | S7 |
| Hardcore is optional, so players who skip it are unaffected | Sawyer | US Gamer, 13 Sep 2017 | S18 (secondhand) |
| Why not a higher difficulty setting for his mod tweaks? Different from an optional mode, little testing, small audience; an extra mode needed programming time that was "in desperately short supply" | Sawyer | Formspring, 20 Oct 2011 and 14 Jun 2012 | S6, S7 |

### 4b. Rules as implemented

Numbers below come from fallout.wiki (S11), not a developer statement, and were read through a summarising tool; treat the exact rates as `[UNVERIFIED]` until checked in game data. The mod readme (S9) confirms the structure (a first threshold at 200, later statuses every 150 in the mod).

| System | Rule |
|---|---|
| Dehydration | Meter 0-1000, penalties from 200 up (END, PER, INT, AGL), death at 1000; wiki rate about 12 per game hour |
| Hunger | Same scale; penalties to STR, PER, CHR; wiki rate about 4.75 per game hour |
| Sleep deprivation | Same scale; penalties to AGL, INT, END; wiki rate about 2.4 per game hour |
| Stimpaks, RadAway | Heal and remove radiation over time (rates not given) |
| Limbs | Crippled limbs need a doctor, Doctor's Bag (partial in Hardcore), certain beds, poultice, Auto-Doc or Hydra |
| Ammo | Has weight (value not confirmed) |
| Companions | Not essential in Hardcore; can die permanently |
| Raw meat | Carries debuffs unless cooked (wiki) |

### 4c. Later verdict and JSawyer changes

| Statement | Who | Where / date | Source |
|---|---|---|---|
| "I don't think Hardcore Mode is 'really' hard" | Sawyer | Formspring, 30 May 2012 (tool-extracted; not locally re-verified) | S7 |
| Asked if NV is still too easy even in Hardcore: "it's an easy game" | Sawyer | Formspring, 18 Jul 2011 | S6 |
| Aim was to "increment the difficulty above Fallout 3" without losing FO3 fans | Sawyer | Formspring, 23 Jul 2011 | S6 |
| If redoing needs: "re-tune the rates as well as the availability of food and drink" (as in his mod) | Sawyer | Formspring, 17 Jul 2012 | S7 |
| Mod's purpose: "make the game more challenging and to fix a bunch of the more obvious balance ... issues"; not an official patch; tested about 20 hours | Sawyer | JSawyer readme 9.29.12 | S9 |
| Why not a patch: "some of the mechanics changes make the game significantly more difficult"; he preferred opt-in | Sawyer | Engadget, 30 Dec 2011 | S27 |
| Mod list: max level 35 with all DLC (level cap 15 plus DLC), XP rate up (iXPBase 275 / bump 200), base carry weight 150 to 50, Strong Back 50 to 25, HP formula from 100 + END x 20 to 50 + END x 10 (+5 per level), Stimpak weight 0.25, default stimpaks uncommon with an "Expired" variant, food and water drops "dramatically lower", H2O/FOD/SLP rates doubled with first threshold moved 200 to 400 | Sawyer | JSawyer readme (Oct 2011 to Sep 2012 entries) and Formspring 28 Dec 2011 | S9, S6 |
| Endurance should not dominate health at level 20+ | Sawyer | Formspring, 5 Feb 2012 | S7 (tool-extracted) |
| Armor DR restored to Medium and Heavy armor in the mod (for example Metal Armor 10, T-51b 30, Remnants 35) because heavy gear was penalised by weight and speed | Sawyer | Readme, 8 Oct 2011 entries; Formspring 27 Jul 2012 | S9, S7 |
| Karma tuning in the mod: fKarmaModKillingEvilActor 100 to 5, VeryEvil 2 to 30; several NPC alignments changed | Sawyer | Readme, 9 Oct 2011 | S9 |
| Perk level requirements lowered for the shorter cap (level-50 perks need level 34) | Sawyer | Readme and Formspring 11 Aug 2012 | S9, S7 |
| Mod released Dec 29, 2011 (first version) | n/a | fallout.wiki | S10 |

Read together: the shipped Hardcore was a "nuisance and awareness" layer. His mod turns it into real resource pressure by cutting carry capacity and health, doubling needs rates, and starving the player of free water and healing.

## 5. World and level design

| Statement | Who | Where / date | Source |
|---|---|---|---|
| Deliberate danger near the start: "a quarry full of deathclaws next to Goodsprings" and "a monster badlands" north; many players "attempted to bulldoze" and mostly failed; the game did not block them, since Quarry Junction is optional | Sawyer | Formspring, 19 Aug 2011 | S6 |
| Rationale: if you pass an obstacle first try, "the obstacle wasn't that difficult and you didn't really accomplish anything" (cites F1 deathclaw lair, F2 Sierra Army Depot) | Sawyer | Formspring, 10 Dec 2010 | S5 |
| Deathclaws, cazadores and super mutants north of Goodsprings are there to warn FO3 players; "you can't just slide all over the map and not feel the heat" | Sawyer | YouTube video, reported 80.lv 16 Aug 2024 | S26 |
| FO3 "was not a hard game"; its scaling lets you feel "extremely strong" quickly | Sawyer | Same | S26 |
| He admired F1's open critical path; goes from Goodsprings straight to Benny; no FO3-style level scaling | Sawyer | In Game News report, undated; body not fully readable | `[UNVERIFIED]` date |
| Bethesda guideline: players should see at least three landmarks from any point in the world | Sawyer (relaying Bethesda) | US Gamer, 13 Sep 2017 | S18 (secondhand) |
| Invisible barriers had four reasons: map edge, a vantage where the world looked "extra bad", getting stuck in geometry (Zion), unassailable AI positions | Sawyer | Formspring, 5 Dec 2012 | S7 |
| "In retrospect, we should have allowed the bad sightlines and removed the invisible barriers" | Sawyer | Formspring, 4 Sep 2011 | S6 |
| Start was very close to the map edge (Goodsprings), and the Pip-Boy marked the whole square as boundary, so players thought half the map was unused; Honest Hearts fixed this | Sawyer | Formspring, 4 Sep 2011 | S6 |
| Map looked small because a square frame forced an irregular real shape inside it | Sawyer | Formspring, 3 Jan 2013 | S8 (tool-extracted) |
| Strip split into load zones: "consoles would have run out of memory" | Sawyer | Formspring, 3 Apr 2011 | S6 |
| "Memory problems caused crashing in both The Strip and Freeside, so they had to be split up" | Sawyer | Formspring, 19 Oct 2011 | S6 |
| Save bloat and later patches removing core content come from stored changes and persistent references (companions) held in memory | Sawyer | Formspring, 22 Nov 2011 | S6 |
| Strip fast travel failed due to trigger placement: "poor planning on our part"; fixing it late would risk the critical path | Sawyer | Formspring, 10 Jul 2011 | S6 |
| World was built outward from the map centre; edge areas came last, so the Colorado became the cut line | Sawyer | Formspring, 2 Jul 2011 | S6 |
| He builds mid-game areas first and the opening last, because you make most errors in the first area you build | Sawyer | Formspring, 31 Oct 2011 | S6 (tool-extracted) |
| Gomorrah's extra floor "detracted from the experience" | Sawyer | Formspring, 2 Nov 2012 | S7 (tool-extracted) |
| High-level design of companions and areas outside the Strip was his; others did hands-on area work; Gonzalez wrote the central plot; Scott Everts did most Westside world-building | Sawyer | Formspring, 9 Dec 2012 and 11 Sep 2011 | S7, S6 |
| He prefers larger levels that support exploration; smaller ones usually come from engine limits | Sawyer | Formspring, 24 Aug 2010 | S5 (tool-extracted) |
| "Faction gating": high-end NCR and Legion troops do not spawn until a story state is reached, limiting early-game gear | Sawyer | Formspring, 5 Jun 2011 | S6 (tool-extracted) |

## 6. Production constraints and regrets

| Statement | Who | Where / date | Source |
|---|---|---|---|
| "No, it was about 18 months." Used Van Buren only for faction ideas, characters, plot hooks; no documentation or assets | Sawyer | Formspring, 27 Dec 2011 | S6 |
| Development was the "longest development cycle of any game I've shipped"; best-selling | Sawyer | Formspring, 3 Jan 2013 (wording: "the longest development cycle of any game I've shipped") | S8 |
| Hardest part: "Projecting the scope of the world eighteen months ahead of release"; the scope set a pace that "became marathon-like" | Sawyer | Formspring, 2 Feb 2011 | S6 |
| Crunch: "During crunch I work between 10 and 13 hours a day" | Sawyer | Formspring, 7 Jun 2010 | S5 |
| About six months before release only a few areas remained in core development; team went to cleanup mid-period | Sawyer | Formspring, 1 Oct 2012 | S7 (tool-extracted) |
| Team had no engine experience ("We had no experience working with that engine"); Bethesda tools "incredibly good" | Sawyer | US Gamer, 13 Sep 2017 | S18 (secondhand) |
| "Absolutely no way" the game could be made without Bethesda's engine and tools | Sawyer | Steemit interview via GameBanshee, 17 Jul 2017 | S28 |
| Reusing FO3 technology freed the team to focus on quests and dialogue; the "plays too much like FO3" criticism was fair | Sawyer | Rock Paper Shotgun, reported 23 Apr 2024 | S23 |
| "Making it in 18 months, that was a big challenge" | Sawyer | GDS Prague, 29 May 2024 | S22 |
| Obsidian's earlier buggy games: "Poor planning, poorly phased implementation of content, poor scope management" | Sawyer | Formspring, 28 May 2010 | S5 |
| "Less content, fewer bugs would have been better"; regrets things that stayed in more than things left out; a quest that breaks midway wastes the idea | Sawyer | Formspring, 9 Apr 2011 | S6 |
| "New Vegas wasn't even hugely ambitious and it was pretty darn buggy despite our best efforts" | Sawyer | Formspring, 24 May 2011 | S6 |
| Programming was in "desperately short supply"; a new difficulty mode would have needed more | Sawyer | Formspring, 14 Jun 2012 | S7 |
| Designed post-ending play from the start; a few milestones before content complete he judged it could not be done with robust reactivity, so "I made the decision to cut it" | Sawyer | Formspring, 1 May 2012 | S7 |
| Extra content wish list (Legion camps, post-Hoover play, dungeons) plus testing: "I'd guess 5-8 months" | Sawyer | Formspring, 7 May 2012 | S5/S7 |
| Dungeons and secondary locations: "We didn't have time to make enough of them at a high enough level of detail" | Sawyer | Formspring, 14 May 2012 | S7 (tool-extracted) |
| Romances cut: "Not enough time to do them well" | Sawyer | Formspring, 6 Sep 2011 | S6 |
| Late cuts: Ulysses; iron sights on laser weapons ("The timing was just really bad" with artists and QA overloaded); the first-person intro scene "we couldn't get it to work reliably" | Sawyer | Formspring, 29 Jan 2012; 22 Jun 2011; 30 Jun 2012 | S7, S6 |
| Chose not to define more faction content: "I don't think I'd want to add any more faction content" | Sawyer | Formspring, 1 May 2012 | S7 |
| He was director only of the core game; he started preparing the next project while Avellone led DLC | Sawyer | Formspring, 9 Oct 2011 | S6 (tool-extracted) |
| Console certification is a platform-holder requirement, and the release date is set by the publisher and platform holder, not the developer | Sawyer | Formspring, 16 Apr 2010 and 26 Jul 2011 | S5, S6 (tool-extracted) |
| "Despite extensive playtesting ... we still made a few mistakes early on" (opening area) | Sawyer | Formspring, 15 Dec 2010 | S5 (tool-extracted) |
| Gonzalez's writing process: research first, story brief, more than 60,000 lines of dialogue, style guide "will save your ass" | Gonzalez | GDC Online, Game Developer 6 Oct 2010 | S19 |
| Fault line with Bethesda: large testing could not catch every problem; Urquhart avoids criticising Bethesda | Urquhart | US Gamer 13 Sep 2017 | S18 (secondhand) |
| Urquhart: game made on "a very fast timeframe" with many bugs (20th anniversary documentary) | Urquhart | Reported in search summary; documentary not viewed | `[UNVERIFIED]` |
| Launch reception: "not particularly well-received ... quite buggy"; about five years for the community to come around | Sawyer | Game Informer interview, reported by GamesRadar (headline only readable) | `[UNVERIFIED]` body |
| PS3's split memory pool as the worst case | forum posts | RPGHQ thread, 2025, unsourced | `[UNVERIFIED]`: Sawyer's own wording not found. The designer-lessons file cited it; I could only confirm console memory crashes generally |
| Scott Everts and other developers: little first-hand material found | n/a | n/a | gap |

## 7. General RPG design principles Sawyer has articulated

| Principle | Who | Where / date | Source |
|---|---|---|---|
| Mechanical chaos frustrates; random failure is reloaded away. "No actual human being likes this!" (on Alpha Protocol spread) | Sawyer | GDC Europe, Game Developer 17 Aug 2011 | S4 |
| What the player perceives matters; tiny stat increments they cannot feel are worthless | Sawyer | Same | S4 |
| Strategic failures (bad builds found 20-30 hours in) feel very bad and should be correctable | Sawyer | Same; Formspring 18 Aug 2011 | S4, S6 |
| Do not keep mechanics "because that's just the way RPGs are"; good gameplay first | Sawyer | Same | S4 |
| Granularity: very fine scales (1 point of 100) cannot be perceived; coarse steps are noticed | Sawyer | Formspring, 15 May 2010 | S5 |
| "I don't believe that RPG mathematics should be overly 'fiddly' or complex"; math should be exposed or deducible | Sawyer | Formspring, 7 Apr 2010 | S5 |
| The fix for complex choices is "not to remove options, but to carefully engineer how those options are presented" | Sawyer | Formspring, 9 Apr 2010 | S5 (tool-extracted) |
| Designers must give each stat, skill or perk a clear, worthwhile role and show its value; if players call a stat a dump stat "you probably screwed up" | Sawyer | Formspring, 13 Dec 2011 | S6 |
| Neglecting a stat should cause "a sting"; focusing on it should reward regularly | Sawyer | Same | S6 |
| Pillars of Eternity attribute tuning: no stat overwhelmingly better or worse (talk "Gods and Dumps", GDC 2016) | Sawyer | Search summary only | `[UNVERIFIED]` here; talk not read |
| Reputation systems are abstractions and should not grow more complicated than what they model | Sawyer | Reputation talk, RPG Codex 6 Apr 2020 | S25 |
| Build the core gameplay features before the character advancement systems | Sawyer | Formspring, 10 May 2010 | S5 (tool-extracted) |
| "I try to push our game play in directions that allow players to create their own stories" | Sawyer | Formspring, 4 May 2010 | S5 (tool-extracted) |
| An RPG is defined by expressing "the personality of your character in meaningful/influential ways" | Sawyer | Formspring, 9 Apr 2010 | S5 |
| Support odd builds: "I want people to build characters and have a good time with them"; hates telling players they built a "fundamentally bad character" | Sawyer | Human Can Opener, reported 28 Jun 2026 | S24 |
| Let players tune difficulty; do not aim at "everyone" (2025 report) | Sawyer | Outer Haven 2 Jul 2025 (citing PC Gamer) | S29 |
| Frustration is "a fundamental element of 'real' games"; the job is to find the right balance point per audience segment | Sawyer | Formspring, 30 May 2012 | S6/S7 |
| "Instant gratification" is not a good design goal: "it provides immediate satisfaction but can lead to long-term boredom" | Sawyer | Formspring, 19 Aug 2011 | S6 |
| Being "unstoppable gets boring pretty quickly"; acceptable late if challenge remains for others | Sawyer | Formspring, 5 Dec 2010 | S5 |
| Branching dialogue: "More branching is better than bigger branches"; guarantee critical information, isolate reactivity | Sawyer | GDC 2012 slides | S1 |
| GDC 2012: designers are "choice architects"; designer and player goals may conflict and must be resolved or accepted consciously | Sawyer | GDC 2012 slides | S1 |
| Dialogue choices should not carry emotional "intent loading" from the author | Sawyer | Formspring, 17 Nov 2010 | S5 |
| Turn-based combat declined in the 2000s for lack of "tactical variation" (headline only) | Sawyer | PC Gamer headline | `[UNVERIFIED]` body |
| Respecting player time: give players a way to correct errors instead of "lol make a new character" | Sawyer | Formspring, 18 Aug 2011 | S6 |

## Status of previously unverified claims

These are the six rows from the Sawyer `[UNVERIFIED]` table in `designer-lessons.md`.

| # | Topic | Earlier claim | Status | Evidence |
|---|---|---|---|---|
| 1 | Choice and consequence | Reactivity should be visible and proportionate; build choices around who the player is | PARTIALLY VERIFIED | GDC 2012 slides (S1): "forecast consequences", "differentiate consequences", "choices should have impact", character prototypes and expression range. "Proportionate" is our paraphrase; he stresses narrative and emotional impact as the scale. Blog (S3) says clarity beats immersion. |
| 2 | Skill thresholds | Fixed thresholds so players can plan; avoid hidden random failures on dialogue | VERIFIED | Formspring 19 Jun 2010, 27 Jul 2011, 26 Feb 2012 (S5-S7). Caveat: in 2012 and 2024 he also criticises the "unlocked option = optimal pick" effect. |
| 3 | Faction design | Coherent logic, real flaws; no good faction; player may support any | VERIFIED (with one admitted failure) | "Moral relativist", 16 Nov 2010 (S5); intent statement 7 May 2012 (S7). Failure: Legion's positive side did not materialise because content was cut. |
| 4 | Hardcore mode | Optional survival rules (food, water, sleep, ammo weight, limb damage) layered on a normal game | VERIFIED for intent; rule details PARTIALLY | Intent and optionality: S5-S7, S12, S14, S18. Needs (water, food, sleep), healing over time, companions: S14, S11. Ammo weight and limb rules rely on fallout.wiki (S11). Exact decay rates `[UNVERIFIED]`. |
| 5 | Level design | Guide by landmarks and sight lines, not invisible walls or hand-holding | PARTIALLY VERIFIED, and the "no invisible walls" part is WRONG | Landmarks: Bethesda's three-landmark rule (S18, secondhand). Soft gates from dangerous creatures: S6 (19 Aug 2011), S5 (10 Dec 2010). But NV used many invisible walls; Sawyer says most should have been removed (S6 4 Sep 2011, S7 5 Dec 2012). |
| 6 | Regrets | Cut Legion lands, post-ending content, engine instability, launch bugs | VERIFIED except "engine instability" PARTIALLY | Legion: S6/S7 (28 Oct 2011, 1-7 May 2012). Post-ending: 1 May 2012. Bugs: 9 Apr 2011, 24 May 2011. Engine: console memory crashes and save bloat (S6 3 Apr, 19 Oct, 22 Nov 2011); PS3 split-memory claim NOT FOUND in his words. |

Additional items from the earlier file:

- "Hand-tuned every weapon" - supported: Sawyer, Formspring 22 Sep 2011 ("I've spend a lot of time tuning [weapons]") and Planet Fallout/Engadget on weapon feel.
- "Heavy overtime" - supported: "During crunch I work between 10 and 13 hours a day" (7 Jun 2010).
- "18 months" - VERIFIED, Formspring 27 Dec 2011 and 25 Jan 2013.
- "Legion territory east of the Colorado dropped" - VERIFIED, 2 Jul and 28 Oct 2011.
- "Post-game cut for time" - VERIFIED, 1 May 2012.

## Not found / could not reach

- GDC Vault video (paywalled) and any transcript of "Do (Say) The Right Thing"; I used his slides instead, so spoken examples and asides are missing.
- Sawyer's Tumblr (jesawyer.tumblr.com, HTTP 403) and web.archive.org (blocked). Obsidian forum threads on the GDC talks (HTTP 403).
- Kinda Funny Games, Human Can Opener and Designer Notes #63 transcripts: only secondhand reports (S21, S24) and a summary page.
- PC Gamer, GamesRadar and Windows Central articles returned headlines only; their bodies were not read, so only the headline text is cited and tagged.
- No Eurogamer, Polygon or Kotaku New Vegas oral history from 2020-2024 was located.
- Reboot Develop / Digital Dragons talks by Sawyer: not found. His GDC 2016 "Gods and Dumps" talk appears only in a search summary.
- Little first-hand material from Eric Fenstermaker, Scott Everts or Feargus Urquhart beyond the points above. Avellone's NV design statements in these sources are limited to the NCR remark and DLC authorship.
- Several Formspring items were extracted by a summarising tool (marked "tool-extracted") and not re-verified against the archive text; entries marked simply with a date and S5-S8 were checked word for word.

## Sources

Consulted (URLs actually fetched or downloaded):

- S1: http://diogenes-lamp.info/GDC12_Do_Say_The_Right_Thing.pdf (slide deck; link given by Sawyer in Formspring, 9 Jul 2012)
- S2: https://gdcvault.com/play/1015758/ (abstract; GDC 2012)
- S3: https://fallout.wiki/wiki/Fallout:_New_Vegas_Developer_Statements/Interviews/Choice_Architecture,_Player_Expression,_and_Narrative_Design_in_Fallout:_New_Vegas
- S4: https://gamedeveloper.com/design/gdc-europe-obsidian-s-five-hard-lessons-of-rpg-design
- Game Developer video page for the GDC 2012 talk (6 Apr 2017): https://gamedeveloper.com/design/video-i-new-vegas-i-and-the-art-of-designing-better-conversations-in-games
- S5: https://fallout.wiki/wiki/Fallout:_New_Vegas_developer_statements/Joshua_Sawyer_Formspring_posts/2010
- S6: https://fallout.wiki/wiki/Fallout:_New_Vegas_developer_statements/Joshua_Sawyer_Formspring_posts/2011
- S7: https://fallout.wiki/wiki/Fallout:_New_Vegas_developer_statements/Joshua_Sawyer_Formspring_posts/2012
- S8: https://fallout.wiki/wiki/Fallout:_New_Vegas_developer_statements/Joshua_Sawyer_Formspring_posts/2013
- S9: http://diogenes-lamp.info/jsawyer_fnv_mod.zip (contains `JSawyer_READ_ME.txt`; link given by Sawyer, Formspring 26 Feb 2012)
- S10: https://fallout.wiki/wiki/Mod:JSawyer and https://fallout.wiki/wiki/Mod:JSawyer/Documentation
- S11: https://fallout.wiki/wiki/Hardcore_mode
- S12: https://www.engadget.com/2010-05-05-interview-josh-sawyer-on-fallout-new-vegas.html
- S13: https://www.shacknews.com/article/63656/fallout-new-vegas-makers-talk
- S14: http://www.gamebanshee.com/kwwdw (Planet Fallout summary, 13 Oct 2010)
- S15: http://www.gamebanshee.com/kwwc8 (5 Jun 2010) and http://www.gamebanshee.com/kwu3w (16 Feb 2010)
- S16: https://rpgcodex.net/article.php?id=6641 ; https://rpgcodex.net/article.php?id=7106 ; https://rpgcodex.net/article.php?id=7187 ; https://rpgcodex.net/article.php?id=6694
- S17: https://fallout.wiki/wiki/Fallout:_New_Vegas_Developer_Statements/Interviews/Joshua_Sawyer/Josh_Sawyer_on_post-apocalyptic_games
- S18: https://fallout.wiki/wiki/Fallout:_New_Vegas_Developer_Statements/The_Making_of_Fallout_New_Vegas
- S19: https://gamedeveloper.com/game-platforms/gdc-online-i-fallout-new-vegas-i-gonzalez-talks-inspiration-writing-process
- S20: https://80.lv/articles/fallout-new-vegas-lead-on-how-game-developers-distribute-skill-checks ; https://gjos.pages.dev/posts/fallout-new-vegas-director-on-the-art-of-making-sure-all-your-points-in-persuasion-arent-wasted-its-all-about-feelings-but-you-use-numbers-to-arrive-at-that-feeling ; https://vlctoria.pages.dev/post/fallout-new-vegas-director-josh-sawyer-explains-why-the-rpgs-opening-is-a-perfect-example-of-respecting-the-players-skill-choices-4cgre
- S21: https://gameranx.com/updates/id/402854/article/fallout-new-vegas-director-didnt-like-save-scumming-in-fallout-3/
- S22: https://www.feed4gamers.com/game-news/297795/josh-sawyer-reflects-on-design-evolution-from-icewind-dale-to-pentiment.htm
- S23: https://www.yahoo.com/entertainment/josh-sawyer-understands-why-fans-222409810.html
- S24: https://ingamenews.com/2026/06/josh-sawyer-explains-how-obsidian.html
- S25: https://rpgcodex.net/article.php?id=11399 (2020 reputation talk) ; https://rpgcodex.net/article.php?id=12021 (2022 armor talk)
- S26: https://80.lv/articles/new-vegas-start-hits-hard-to-show-fallout-3-fans-it-s-not-as-easy
- S27: https://www.engadget.com/2011-12-30-fallout-new-vegas-designer-makes-his-own-unofficial-mod.html
- S28: http://www.gamebanshee.com/kd6c3 (17 Jul 2017) ; https://www.gamebanshee.com/kw4a (5 Jan 2011)
- S29: https://www.theouterhaven.net/fallout-new-vegas-director-says-rpgs-should-let-players-choose-difficulty
- Also consulted: https://fallout.wiki/wiki/Joshua_Sawyer ; https://fallout.wiki/wiki/Joshua_Sawyer/Fallout_weapon_skills ; https://fallout.wiki/wiki/Joshua_Sawyer/Inside_the_Vault ; https://www.designer-notes.com/?p=1785 (summary page only) ; https://www.gamebanshee.com/36qhk (announcement of the 2020 talk) ; https://www.gamebanshee.com/kww96 (summary only) ; https://www.gamebanshee.com/k9kac (Tumblr save-scumming remark, 12 Jul 2016)

Reached but headline-only (body not readable): PC Gamer "Karma Police", "5 years", "turn-based", "Yes Man" and "Cazador" articles; GamesRadar "vibes based", "not particularly well received" and "opening" pieces; Windows Central "crunch" article.

Failed or blocked: forums.obsidian.net (403), jesawyer.tumblr.com (403), web.archive.org (blocked), fallout.fandom.com (402/403), Sawyer interviews on YouTube.

## Design Takeaways

Rules to adopt on our own game, derived from the verified material above.

1. **No global morality meter.** Track standing per faction or community and show effects through who talks to you, what they offer and what they refuse. If you keep any good/bad tally, do not let it silently gate content; Sawyer's own verdict is that it was feedback only.
2. **Design factions around a choice the player can defend, then fund all of them.** Sawyer's stated plan (first impression, then hidden dark side or hidden virtue) failed only for the faction whose content was cut. Budget so each faction has its own locations, a companion and some quests before alpha; cut a whole faction rather than starve one.
3. **Let the player kill anyone, and write the fallback.** Adopt the rule "anyone in line of sight can be killed (except children)", keep a failsafe route that completes the critical path, tell players when they lock out content, and put unique loot where players do not have to murder for it.
4. **Use fixed dialogue thresholds, shown in the text, and never punish an attempt.** A failed check must leave the player no worse off, and should have its own line. Never use stand-alone random rolls for things the player can reload.
5. **Counter the "unlocked means correct" trap.** Make some unlocked options carry in-world cost or a character-flavoured reaction, so the visible option is not always the best one. This is Sawyer's own later correction.
6. **Spread checks over every skill and front-load them.** Make the opening area pay off every tagged skill, track check counts per skill with a script tracker, and review that table each milestone. Hold an explicit "no dump stat" audit: if players call any stat a dump stat, fix its communication or its payoff.
7. **Give armor two layers but keep one dominant.** Flat damage subtraction with a minimum damage floor (NV used 20%) keeps light and medium armor viable; if you add a percentage layer, keep it small (about 25% max). Decide up front and balance one protection number, not two.
8. **Tie weapon tier to the skill requirement** (0/25/50/75/100) and give each weapon a role relative to its neighbours. Keep ammo types few, make every type serve at least two weapons, keep special ammo and mods in shops only as a money sink.
9. **If the game is a shooter in hand, tell the player what skill does.** Blame random-feeling shots on low skill plus bad gear and spread, not on a hidden dice roll; offer a way to feel competent early.
10. **Survival is a resource-pressure layer, not a difficulty slider.** Ship it optional, but tune it for real scarcity from day one: low carry weight, scarce free water and healing, meaningful healing time. NV's shipped Hardcore was admittedly "not really hard"; the JSawyer numbers (carry 50, HP 50 base, doubled needs, scarce drops) are a better starting point.
11. **Use dangerous creatures as soft gates.** A deadly optional area near the start, flagged by visible warnings, teaches players to read the world and gives return-later payoffs. Do not scale enemies to the player so strongly that the world feels safe.
12. **Skip invisible walls where you can.** Mark the map edge honestly on the map, start the player away from the border, and accept ugly distant terrain rather than blocking sightlines. Plan landmarks (aim for at least three visible from any point).
13. **Do not rely on one contiguous large city on weak hardware.** Decide the memory budget before layout; split cities by design, not by emergency, and place triggers/fast-travel points early.
14. **Plan scope against the real schedule.** Sawyer's repeated lesson: fix world scope early, build from the middle of the map outward so cuts happen at the edge, and protect polish. Prefer "less content, fewer bugs". Treat the schedule for a faction's content and a companion as one unit.
15. **Phase content so cuts are cheap.** Build mid-game areas first and the opening last; stage quest implementation (baseline first, then experiments); avoid heavy scripting in quests ("use less complex scripting", 18 Dec 2010).
16. **Plan post-ending state early or cut it early.** The post-game was cut a few milestones before content complete because reactivity could not be supported "to the extent that it deserved"; either build it into the quest state model from the start or decide against it in pre-production.
17. **Avoid fine-grained numbers players cannot perceive.** Use coarse steps (perk every two levels, tiers at 25-point intervals) and expose the math; a skill scale of 100 points works only if thresholds carry the meaning.
18. **Respect player time:** allow costly respecs, make mistakes recoverable, tell players what they locked out, and give optional challenge areas a way to be returned to.
19. **Verify before reusing a quote.** Items tagged `[UNVERIFIED]` or "tool-extracted" above should be rechecked against the archive text before they go into any public document.
