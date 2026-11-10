# Fallout: New Vegas (2010) — Gameplay, Systems and Balance

Scope: mechanics, numbers and balance of Obsidian's *Fallout: New Vegas* (FNV), what it changed from
*Fallout 3* (FO3) and why, how it was received, and what its own director later said he would change.
Story and lore are covered elsewhere; they appear here only where they drive systems.

**Confidence note.** Numbers in this file were checked against fallout.wiki pages and press coverage where
marked as such in the Sources section. The session's web-search budget ran out part-way through, and Nukapedia
(fandom.com) refused automated fetches, so some figures come from a single wiki or from the author's recall and
are tagged `[UNVERIFIED]`. Treat anything so tagged as a lead, not a fact.

## Quick Reference

- **Built in about 18 months** on Bethesda's Gamebryo/FO3 codebase by a team that had never used the engine;
  shipped 19 Oct 2010 with crashes, save corruption and scripting bugs; a day-one patch fixed "200+" quest issues.
- **Metacritic 84 (PC, 360) / 82 (PS3).** Obsidian's only bonus required 85+; contract was a flat fee, no royalties.
- **Armor is subtractive, not just percentage.** `Final = max(Base × (1 − DR) − DT, Base × 0.20)`. A hit can never
  do less than 20% of its base damage. A red shield icon tells the player when their hits are being absorbed.
- **Ammo is a tactical layer.** Armor-piercing = ×0.95 damage, −15 target DT. Hollow point = ×1.75 damage,
  target DT ×3. Surplus = ×1.15 damage, ×3 weapon wear. Hand-loads (perk-gated) are the best of both.
- **Perk every 2 levels** (FO3: every level); **traits return** (pick 0-2, each an upside with a downside).
- **Level cap 30, +5 per story DLC to 50.** The DLC raises are widely seen, including by Sawyer, as breaking
  late-game balance; his own mod cuts the base cap to 15 (35 with all DLC).
- **Dialogue skill checks are hard thresholds**, displayed as e.g. `[Barter 55]`; fail options are shown and
  auto-fail. No percentage rolls, so no save-scumming. All 13 skills get dialogue uses, not just Speech.
- **Skill magazines give +10 (+20 with Comprehension)** temporarily, so thresholds become a resource puzzle.
- **Reputation replaces karma as the system that matters:** separate Fame and Infamy tracks per faction/town,
  combined into a 4×4 grid of 16 titles. Karma still exists but does almost nothing.
- **Hardcore mode** adds thirst, hunger, sleep, weighted ammo, healing over time and permadeath for companions.
  Loved as an idea, widely judged too lenient; Sawyer's mod doubles the need rates.
- **Any NPC can be killed** and the game stays completable; an unkillable-in-practice robot (Yes Man) is the
  failsafe route to an ending.
- **Four endgame branches** (House, NCR, Legion, Independent), roughly 25 main-arc quests between them, converging
  on one final battle with different sides.
- **World is authored, not level-scaled.** A safe road loops south and east from the start town; the direct route
  north is lined with deathclaws and cazadores. Sawyer says these teach caution; they are not hard walls.
- **Criticised for** invisible walls, a sparser map than FO3, a Strip chopped into gated cells for console
  memory, and thin Legion content.
- **Economy has real sinks:** 4,000-cap stat implants (count capped by Endurance), 8,000-12,000 special implants,
  weapon mods, casino bans on big winners. It still collapses late through repair-and-sell loops and DLC loot.
- **Dominant builds:** sneak-crit sniper (anti-materiel or Gauss rifle), crit-stacked light/medium armor,
  and melee/unarmed with armor-bypass perks. **Weak:** Charisma, Barter, low-damage automatics versus DT.
- **JSawyer mod** (first released 29 Dec 2011, v5.1 on 29 Sep 2012): halves base HP, cuts carry weight from 150 to 50, makes
  stimpaks weigh something, and adds DR back onto heavy armor.

## 1. Context: schedule, engine, launch state

| Item | Detail | Source confidence |
|---|---|---|
| Developer / publisher | Obsidian Entertainment / Bethesda Softworks | Verified |
| Development time | About 18 months | Verified (wiki, Wikipedia, PCGamesN) |
| Announced / released | 20 Apr 2009 / 19 Oct 2010 (NA), 21 Oct (AU), 22 Oct (EU) | Verified |
| Engine | Gamebryo, FO3 codebase. No Obsidian staff had used it; a modder with Oblivion experience was hired | Verified (Wikipedia) |
| Project director / lead designer | Josh Sawyer | Verified |
| Other leads | John Gonzalez (creative lead / writer), Chris Avellone (senior designer, DLC lead), Joe Sanabria (art), Scott Everts (world building) | Verified |
| Script size | 65,000+ recorded lines | Verified |
| Team size, budget | Not found | Gap |
| Metacritic | 84 PC, 84 Xbox 360, 82 PS3 | Verified |
| Sales | 5 million shipped and ~$300M revenue by Nov 2010; EEDAR estimate 11.6M by 2015; wiki cites 12M+ by 2020 | Verified |

**Why the schedule matters for systems.** Almost every structural weakness listed later traces to the schedule
or to console memory: the split Strip, cut post-game play, thin Legion territory, buggy disguises, and bugs that
could not be patched because of base-game/DLC interactions. Sawyer's summary of feature management was
"It's triage" (PCGamesN). He also said cutting disguises would have been the smart call, because they were
expensive and buggy.

**Launch bugs and patches.**

| Patch (PC) | Date | Notes |
|---|---|---|
| 1.1.0.268 | 20 Oct 2010 | Day-one; "200+" quest and scripting fixes (360 notes say 300+) |
| 1.1.1.271 | 21 Oct 2010 | Fixed auto/quick-save bugs introduced by Steam Cloud |
| 1.2.0.285 | 10 Nov 2010 | Crash and companion fixes |
| 1.2.0.314 | 14 Dec 2010 | Large general fix pass |
| 1.2.0.352 | 21 Feb 2011 | Engine update |
| 1.3.0.452 | 25 Apr 2011 | Large fix pass; console equivalent "includes various weapon adjustments" (balance patch) |
| 1.4.0.525 | 7 Jul 2011 | Final; Old World Blues compatibility |

The 360 balance patch of 28 Apr 2011 had to be re-issued two days later because it stopped some users loading
saves. Critics docked the game for crashes, corrupted saves, frame rate and pathfinding. Edge's verdict is the
most quoted: creatively it "gets almost everything right. Mechanically and technically, it's a tragedy."

**The Metacritic bonus.** In March 2012 Chris Avellone tweeted, in reply to a fan assuming the game had made
Obsidian rich, that it "was a straight payment, no royalties, only a bonus if we got an 85+ on Metacritic,
which we didn't." The tweet was later deleted. The game sat at 84. The amount was never disclosed and Bethesda
declined comment. Avellone later described the bonus as something Bethesda offered above and beyond the contract and
said it would not have prevented the roughly 30 layoffs Obsidian made that month after an unrelated project was
cancelled. CEO Feargus Urquhart said the terms were contractual and he was not upset. The lesson usually drawn:
the one-point gap is plausibly the bugs, which were a function of the schedule the publisher set.

## 2. Combat changes from Fallout 3

### 2.1 Damage Threshold

FO3 used percentage Damage Resistance only (capped at 85%). FNV restores Damage Threshold (DT) from Fallout 1/2
as the primary armor stat and keeps DR as a minor, rarely used secondary stat.

```
after_DR = Base × (100 − min(DR, 85)) / 100
Final    = max(after_DR − DT, Base × 0.20)
```

- Critical bonus damage is added to Base before armor.
- DR applies first, then DT, then the 20% floor, then the difficulty multiplier.
- Shotgun pellets are each checked against DT separately, which is why buckshot collapses against armor.
- Because of the floor, DR of 80 or more makes DT irrelevant.
- Player DT maximum in the base game: 46 (Remnants power armor 28 + helmet 8 + Sub-Dermal implant 4 +
  Toughness ×2 for 6). With Old World Blues: 53.

**Why Obsidian did it.** Sawyer's stated reasons (RPG Codex report of 2 May 2010, and his wiki-quoted remarks):

1. Subtractive armor makes weapon choice matter. High rate-of-fire, low per-shot weapons are for soft targets;
   slow, heavy-hitting weapons are for armor. DT can "effectively neutralize a lot of small arms."
2. Feedback. FO1/2 printed damage numbers; FO3 showed only a health bar, so a player could not tell "armored"
   from "lots of HP". FNV adds a red shield icon by the target's bar when a hit is at or below DT, and a shield
   by the player's own bar when the same happens to them.
3. The Pip-Boy shows DAM and DPS side by side so the trade-off is legible.

**Worked example (target DT 20, no DR).**

| Weapon | Base dmg | After DT | Floor (20%) | Actual | % of base delivered |
|---|---|---|---|---|---|
| 9mm pistol | 16 | −4 | 3.2 | 3.2 | 20% |
| Service rifle | 18 | −2 | 3.6 | 3.6 | 20% |
| Marksman carbine | 24 | 4 | 4.8 | 4.8 | 20% |
| Hunting rifle | 52 | 32 | 10.4 | 32 | 62% |
| Brush gun | 75 | 55 | 15 | 55 | 73% |
| Anti-materiel rifle | 110 | 90 | 22 | 90 | 82% |
| Service rifle + AP (DT −15) | 17.1 | 12.1 | 3.4 | 12.1 | 67% of standard base |

The table shows both the strength of the system (ammo and weapon choice become real decisions) and its balance
problem: against late-game armor, big single-shot weapons win outright and automatics need AP ammo to function.

### 2.2 Ammunition types

Every calibre has variants bought, found, or crafted. Modifiers below are from fallout.wiki.

| Variant | Damage | Target DT | Weapon wear | Other | Role |
|---|---|---|---|---|---|
| Standard | ×1.0 | — | ×1 | | Baseline |
| Armor Piercing (AP) | ×0.95 | −15 (5mm AP: −25) | ×1 | | Armored targets |
| Hollow Point (HP) | ×1.75 | ×3 (5mm HP: ×2) | ×1 | | Unarmored animals, ghouls |
| Surplus (5.56mm, 5mm) | ×1.15 | — | ×3 | 5mm spread ×1.2 | Cheap bulk, eats the gun |
| +P (9mm, .45) | ×1.1 | −2 | ×1.2 | | Mild all-rounder |
| .38 Special / .44 Special | ×0.75 | — | ×0.75 | | Cheap practice rounds in magnum guns |
| JHP hand-load (9mm, 10mm, 12.7mm) | ×1.65 | ×2 | ×1 | | Better HP |
| JSP hand-load (.308, 5mm) | ×1.3 | — (5mm −10) | ×1.5 | | Big flat damage |
| SWC hand-load (.44, .45-70) | ×1.2 | −6 | ×1 (.45-70: ×3) | | Damage and penetration |
| Match hand-load (5.56mm, .50 MG) | ×1.15 | — | ×1 | Spread ×0.65 | Accuracy |
| .50 MG explosive (GRA) | standard +40 explosive | — | | | Top-end, expensive |
| 12 ga slug | — | — | | 1 projectile, spread ×0.35 | Range, beats DT |
| 12 ga magnum / 4/0 buck magnum | ×1.3 | −2 | ×1.15 | | Heavier buck |
| 12 ga bean bag | ×0.05 | — | | +250 fatigue | Non-lethal knockout |
| 12 ga pulse slug | ×0.7 | — | | +50 vs robots, +25 vs power armor | Anti-robot |
| Energy: standard | ×1.0 | −2 | ×1 | | All energy ammo has small built-in DT bypass |
| Energy: bulk | ×0.85 | | ×0.85 | | Cheap |
| Energy: over charge | ×1.25 | −5 | ×1.5 | | |
| Energy: max charge | ×1.5 | −10 | ×2.5 | | |
| Energy: optimized (GRA, perk) | ×1.3 | −5 | ×1.1 | Weight ×0.6 | Best in practice |

Notes:
- 5mm standard rounds have −10 DT built in, which is the only thing keeping the minigun usable.
- **Reloading benches** let the player break ammo into primers, powder, lead and cases and reassemble other
  variants; Repair skill gates recipes. **Hand Loader** (level 6, Repair 70) unlocks the hand-load recipes and
  doubles case recovery. **Vigilant Recycler** (level 6, Science 70) does the same for energy cells and unlocks
  optimized ammo. Workbenches convert energy ammo types into each other.
- Design consequence: a player who ignores ammo types has a noticeably harder game; one who engages gets a
  real power increase without a level-up. This is knowledge-as-progression.

### 2.3 Weapon mods

- Each base weapon has up to three defined mods; one of each type; applied through the Pip-Boy; **permanent**.
- Mod value is added to the weapon's value.
- Unique weapons generally cannot be modded (exceptions: Weathered 10mm, Mercenary's Grenade Rifle, Holorifle).
  This is the main balance lever between uniques and commons: a fully modded common weapon can beat or match
  its unique (classic example: modded laser rifle with focus optics +3 damage and beam splitter +30% versus AER14).
- Sold by roughly ten vendors whose stock rotates every 72 game hours, so finding a specific mod is a caps and
  time sink. Typical prices run from a few hundred to several thousand caps `[UNVERIFIED exact range]`.
- Gun Runners' Arsenal (GRA) added mods for weapons that had none, including a suppressor and carbon-fibre
  parts (−7 weight) for the anti-materiel rifle.

### 2.4 Other combat changes

| Change | Detail | Why |
|---|---|---|
| Iron sights | True aim-down-sights on all guns | Make real-time shooting viable beside VATS; Sawyer: switching between the two is "much more viable" |
| Small Guns + Big Guns → Guns | Explosives takes launchers; Energy Weapons takes heavy energy | FO3's Big Guns was a late-blooming trap skill |
| Strength and skill requirements on weapons | Below requirement: more sway (guns) or slower swings (melee); still usable | Soft gating instead of hard locks |
| VATS damage reduction cut | Player takes far more damage in VATS than in FO3 `[UNVERIFIED: commonly cited 25% reduction vs 90%]` | VATS was an invulnerability button in FO3 |
| Melee/unarmed VATS special moves | Skill 50+ unlocks named moves | Give melee depth |
| Throwing weapons | Spears, knives, hatchets under Melee Weapons | Variety |
| Fixed, hand-placed enemies | Little level scaling; areas have set difficulty | Geography as difficulty curve |
| Weapon condition | Still degrades; repair by like items, vendors, repair kits; Jury Rigging perk (Repair 90) allows cross-type repair | Caps sink and Repair value |

## 3. Character system

### 3.1 Numbers

| Rule | FO3 | FNV |
|---|---|---|
| Perk rate | Every level | Every 2 levels |
| Level cap | 20 (30 with Broken Steel) | 30; +5 per story DLC, 50 with all four |
| Traits | None | 0-2 at creation (10 base, 6 more in Old World Blues) |
| Skills | 13 (Small Guns, Big Guns) | 13 (Guns, Survival) |
| Skill start | — | 2 + 2×stat + ceil(Luck/2) |
| Tag bonus | +15 | +15, three tags |
| Skill points/level | 10 + INT | 10 + INT/2 (odd INT alternates) |
| Skill books | +1 (+2 with perk) | +3 (+4 with Comprehension) `[UNVERIFIED on fetched pages; widely documented]` |
| Skill magazines | None | +10 temporary (+20 with Comprehension) |
| Regular perks | — | 88 base game, 117 with DLC; plus 8 companion, 16 challenge, 18 special |
| HP | — | 100 + END×20 + (Level−1)×5 |
| Carry weight | 150 + STR×10 | 150 + STR×10 |

At the level-30 cap the player gets 15 perk picks; at 50, 25. With INT 5 a character earns about 12.5 points a
level, so roughly 360 points by 30 against 13 skills × ~85 points of headroom. A level-30 character maxes four
or five skills; a level-50 character maxes nearly all of them, which is the core of the DLC balance complaint.

### 3.2 Skills and attributes

| Skill | Stat | Notes on value |
|---|---|---|
| Barter | CHA | Prices plus many dialogue checks; still considered weak |
| Energy Weapons | PER | Weak early (ammo scarcity, low DT bypass), strong late |
| Explosives | PER | Covers launchers, mines, grenades; many dialogue checks |
| Guns | AGI | Broadest weapon list in the game; default best |
| Lockpick | PER | Thresholds at 25/50/75/100 |
| Medicine | INT | Scales healing items; many dialogue checks |
| Melee Weapons | STR | Strong with perks; includes thrown |
| Repair | INT | Arguably best utility skill: Jury Rigging, Hand Loader, repair kits |
| Science | INT | Hacking at 25/50/75/100; frequent dialogue checks |
| Sneak | AGI | Sneak-attack criticals multiply the best weapons |
| Speech | CHA | Still the most common check, but no longer the only one |
| Survival | END | New. Campfire crafting; scales food/drink healing |
| Unarmed | END | Strong with perks and ballistic fist |

### 3.3 Traits (restored from Fallout 1/2)

| Trait | Upside | Downside |
|---|---|---|
| Built to Destroy | +3% crit chance | Weapons decay 15% faster |
| Fast Shot | +20% fire rate | −20% accuracy |
| Four Eyes | +1 PER with glasses | −1 PER without |
| Good Natured | +5 to five non-combat skills | −5 to five combat skills |
| Heavy Handed | More melee/unarmed damage | Less crit damage |
| Kamikaze | +10 AP | −2 DT |
| Loose Cannon | Throw faster | Less throw range |
| Small Frame | +1 AGI | Limbs cripple more easily |
| Trigger Discipline | +20% accuracy | −20% fire rate |
| Wild Wasteland | Swaps in joke encounters | Replaces some serious ones |
| Skilled (OWB) | +5 all skills | −10% XP |
| Logan's Loophole (OWB) | No addiction, chems last twice as long | Level cap locked at 30 |
| Claustrophobia, Early Bird, Hoarder, Hot Blooded (OWB) | Situational bonuses | Matching situational penalties |

Trait numbers above are from recall and standard documentation `[UNVERIFIED individually]`. Good Natured and
Skilled are near-free picks for most builds, which shows the difficulty of balancing a downside system: a
downside the player never encounters is not a downside. Skilled was also exploitable (re-pick traits in the Old
World Blues auto-doc to stack the bonus).

### 3.4 Skill checks: thresholds, not rolls

- FO3 Speech checks showed a percentage and rolled. Players quick-saved and retried, so the skill mostly
  measured patience.
- FNV shows the requirement in brackets and resolves deterministically. If the character falls short, the
  option is still visible (with the shortfall shown) and can be picked for an auto-fail line, often a joke.
- Checks draw on all skills, plus SPECIAL stats and perks. *Beyond the Beef* alone uses Speech (35, 38, 45, 55,
  62), Barter 55, Medicine (25, 45, 55), Repair 35, Guns 45, Unarmed 45, Strength 7, Survival 75, and the
  Cannibal and Black Widow perks.
- **Magazines** convert this into a resource puzzle: a +10 (or +20) temporary boost lets a character with
  Speech 45 pass a 55 check, at the cost of a consumable. Players carry a small library and pop one before key
  conversations. This softens the cliff of hard thresholds without bringing back the dice.
- Sawyer's GDC 2012 talk, *Do (Say) The Right Thing: Choice Architecture, Player Expression, and Narrative
  Design in Fallout: New Vegas*, argues that conversation structure in RPGs had barely changed in a decade and
  that designers steer players toward a "correct" choice while advertising freedom. The FNV approach is to make
  options legible and to make competing choices each carry both virtue and cost. (Abstract and attendee notes
  consulted; the full talk video was not watched for this document.)

Criticism: thresholds are binary and can be gamed with magazines and gear, and with a level-50 cap nearly every
check is passable by one character, erasing build identity.

### 3.5 Survival skill and crafting

| Station | Governing skill | Makes |
|---|---|---|
| Campfire | Survival | Food, healing powder, poisons, antivenom, gecko-backed armor, water purification |
| Workbench | Repair, Science | Weapon repair kits, stimpaks/doctor's bags (Medicine), mines, energy ammo conversion |
| Reloading bench | Repair | Ballistic ammo, hand-loads |

- Survival also multiplies the benefit of food and drink, which matters in Hardcore where food heals over time.
- Ingredients are harvested from plants at fixed locations that regrow, giving the map a foraging layer.
- Assessment: crafting was praised for ammo and criticised for clutter; most recipes are not worth the
  ingredient hunting on normal difficulty. Survival is a weak skill outside Hardcore and strong inside it.

## 4. Hardcore mode

Optional toggle offered at the start; can be switched off any time (which forfeits the achievement).

| Rule | Normal | Hardcore |
|---|---|---|
| Stimpaks, food | Instant heal | Heal over time |
| Crippled limbs | Stimpak or any sleep | Doctor, doctor's bag, Hydra, healing poultice, auto-doc, or an owned bed |
| Sleep | Heals fully anywhere | Heals only in owned beds (or with Roughin' It perk) |
| Ammo | Weightless | Has weight (per-round values not retrieved; gap) |
| Companions | Knocked out | Die permanently |
| Radiation, needs | Radiation only | Adds H2O, FOD, SLP meters |

| Need | Rate (game time) | 200 | 400 | 600 | 800 | 1000 |
|---|---|---|---|---|---|---|
| Dehydration | ~12/hour | −1 END | −1 PER, −2 END | −2 PER, −1 INT, −3 END | −2 PER, −3 END, −2 AGI, −1 INT | Death |
| Starvation | ~4.75/hour | −1 STR | −2 STR, −1 CHA | −3 STR, −1 PER, −2 CHA | −3 STR, −2 PER, −2 CHA | Death |
| Sleep deprivation | ~2.4/hour | −1 AGI | −1 INT, −2 AGI | −2 INT, −1 END, −3 AGI | −2 INT, −2 END, −3 AGI | Death |

At those rates the first thirst penalty arrives after about 17 game hours, first hunger penalty after about 42,
first sleep penalty after about 83.

**Reception.** Reviewers and players liked that it existed and that it tied Survival, food, water sources and
beds into the loop. The consensus criticism is that it is bookkeeping rather than danger: water and food are
abundant, the rates are slow, and the only reward for finishing the game in it is an achievement (the intro
text promises a "special reward"; nothing else exists). The parts that actually change play are healing over
time, limb rules and ammo weight. Sawyer said it "really does make a pretty big change in how you play", but his
own mod doubles all three need rates, moves the first penalty threshold, and gives stimpaks weight, which is a
fair measure of how far he thought the shipped version fell short. Bethesda's later Survival mode in Fallout 4
adopted and hardened most of these ideas.

## 5. Reputation versus karma

**Structure.** Each faction and town tracks two independent totals, Fame and Infamy. Points are almost never
removed; good deeds do not erase bad ones.

| Action size | Very minor | Minor | Average | Major | Very major |
|---|---|---|---|---|---|
| Points | 1 | 2 | 4 | 7 | 12 |

Each track has four bands whose thresholds scale with the size of the faction:

| Faction | Band 2 | Band 3 | Band 4 |
|---|---|---|---|
| White Glove Society | 2 | 5 | 10 |
| Goodsprings | 3 | 8 | 15 |
| Brotherhood of Steel | 3 | 10 | 20 |
| Freeside | 11 | 35 | 70 |
| NCR | 12 | 40 | 80 |
| Caesar's Legion | 15 | 50 | 100 |

Title matrix (Fame across, Infamy down):

| | Fame 1 | Fame 2 | Fame 3 | Fame 4 |
|---|---|---|---|---|
| **Infamy 1** | Neutral | Accepted | Liked | Idolized |
| **Infamy 2** | Shunned | Mixed | Smiling Troublemaker | Good-Natured Rascal |
| **Infamy 3** | Hated | Sneering Punk | Unpredictable | Dark Hero |
| **Infamy 4** | Vilified | Merciful Thug | Soft-Hearted Devil | Wild Child |

- Tracked factions: NCR, Legion, Brotherhood, Boomers, Great Khans, Followers, Powder Gangers, White Glove
  Society. Tracked towns: Goodsprings, Novac, Freeside, the Strip (Primm exists but is unused).
- Effects: vendor access and discounts, safehouse keys (Liked), gifts, companion availability (Veronica refuses
  to travel with someone the Brotherhood dislikes), quest availability, and hit squads from NCR or Legion at
  high Infamy.
- Being seen killing a faction member is a large Infamy hit; unseen sneak kills add none. Theft when caught
  is a small hit.
- **Amnesty resets:** both major factions wipe the player's Infamy once at a scripted main-quest point (NCR
  after first meeting House; Legion after dealing with Benny), so an early rampage does not lock out a branch.
- **Disguises:** wearing a faction's armor sets displayed reputation with that faction to neutral and makes
  its enemies hostile. Certain NPCs (officers, dogs) see through it. Towns ignore disguises. Sawyer called the
  feature costly and buggy.

**Karma** survives from FO3 but drives almost nothing: a few ending-slide variants, one companion (Cass) leaving
at very low karma, and theft penalties. It also behaves oddly (stealing from villains costs karma; killing them
restores huge amounts). The JSawyer mod patches the values rather than removing it, changing the reward for
killing evil characters and re-tagging many NPC alignments. The design lesson most writers draw is that the two-axis,
per-faction model made a global morality meter redundant.

**Critique of reputation.** Fame is easy to farm and Infamy rarely bites until the main quest forces it;
mixed titles are flavourful but mostly cosmetic; and the "killing in secret doesn't count" rule plus the
amnesties mean consequences are softer than the matrix implies.

## 6. Companions

- **One humanoid plus one non-humanoid** at a time.
- **Companion wheel** replaces FO3's dialogue-menu commands: open inventory, stay/follow, ranged/melee,
  aggressive/passive, distance, use stimpak, talk, dismiss. Praised as a pure usability win.
- **Nerve:** companions gain +5% damage and DT per point of the player's Charisma (+50% at CHA 10). This was the
  attempt to make Charisma matter in combat; it was not enough to rescue the stat.
- Companions are unkillable (knocked out) in normal mode and mortal in Hardcore. They need no food or water.
- Each grants a **perk while hired** (even when told to wait), and each has a **personal quest** triggered by
  visiting places or hearing topics with them, which upgrades the perk or their gear.

| Companion | Type | Base perk | Quest | Upgrade (choice) |
|---|---|---|---|---|
| Arcade Gannon | Human | Better Healing: +20% from healing items | For Auld Lang Syne | Tesla armor / Remnants join final battle |
| Craig Boone | Human | Spotter: highlights hostiles when aiming | I Forgot to Remember to Forget | Assault armor or Survival armor |
| Cass | Human | Whiskey Rose: no alcohol downsides, DT when drinking | Heartache by the Number | Hand of Vengeance (+15% guns damage) or Calm Heart (+50 HP) |
| Veronica | Human | Scribe Assistant: portable workbench | I Could Make You Care | Causeless Rebel (attack speed) or Bonds of Steel (+4 DT) |
| Raul Tejada | Ghoul | Regular Maintenance: gear decays 50% slower | Old School Ghoul | Full Maintenance (75%) or Old Vaquero (+33% fire rate, revolvers/lever guns) |
| Lily | Nightkin | Stealth Girl: Stealth Boys last 2×, +10% sneak crit damage | Guess Who I Saw Today | Medication choice changes combat behaviour |
| ED-E | Eyebot | Enhanced Sensors: long detection range, target cloaked enemies | ED-E My Love | Weapon upgrade (Followers) or +8 DT (Brotherhood) |
| Rex | Cyberdog | Search and Mark: highlights loot when zoomed | Nothin' But a Hound Dog | Brain choice: +25 damage, +10 DT, or +50% speed |

Boone, Veronica and Rex base perks are from recall `[UNVERIFIED on fetched pages]`.

**Balance.** Two companions with good weapons trivialise much of the base game on normal difficulty; Boone and
ED-E together spot and kill enemies before the player sees them. Reviewers also complained that companion AI
ignored orders and pathfinding broke. Companion quest triggers were opaque enough that many players never
completed them.

## 7. Main quest structure and the "kill anyone" rule

**Shape.** Linear first act (track down the man who shot you, roughly Goodsprings → Primm → Nipton → Novac →
Boulder City → the Strip), then a wide second act where four parties court the player, then a single final
battle at Hoover Dam fought from whichever side was chosen.

| Branch | Arc quests | Final quest | Key demands |
|---|---|---|---|
| Mr. House | The House Always Wins I-VIII (9 quests) | All or Nothing | Destroy the Brotherhood; side with Boomers etc. |
| NCR | 4 unique + 1 shared | Eureka! | Deal with House; Brotherhood may be destroyed or allied via truce; protect the president |
| Caesar's Legion | 4 | Veni, Vidi, Vici | Destroy Brotherhood; kill House; assassinate the president |
| Independent (Yes Man) | Wild Card series (7) | No Gods, No Masters | Player decides fate of every minor faction |

About 25 distinct arc quests in total. Progress down one branch fails the others at marked points; the game
warns the player before a commitment becomes irreversible.

**Minor-faction layer.** Every branch asks the player to settle the same set of smaller groups (Boomers, Great
Khans, Brotherhood, Followers, Kings, Omertas, White Gloves, Remnants), but each patron wants a different
outcome, and the result appears both in the final battle (who shows up to help) and in the ending slides. One
set of content therefore serves four storylines. This is the game's most reusable structural idea.

**Killable NPCs.** A stated design rule was that the player can kill anyone, including quest givers and faction
leaders, without making the game unwinnable (children excepted, plus a handful of technical exceptions). The
mechanisms:

1. Critical information is duplicated on notes, holotapes, terminals and bodies.
2. Quests fail cleanly with a notification instead of hanging.
3. **Yes Man** is the backstop. He will work for anyone regardless of reputation, his branch needs no faction's
   goodwill, and if destroyed he respawns in another robot body once the player leaves the area. However
   many people the player has killed, an ending remains reachable.

Writer John Gonzalez later said he regretted how the Independent route turned out, because it lets the player
avoid committing to a flawed faction; he suggested a version where control slips away from the player would
have been stronger. That is worth noting: the failsafe doubles as the "have it all" ending, and many players
treat it as the default.

**Cut for time:** post-ending play and its reactivity. The game ends at the slides.

## 8. World design

**The loop.** The start town sits southwest of the goal. The road north is the short route and is guarded by
giant wasps (cazadores), a deathclaw-infested quarry, and super mutants on a mountain. The road south and then
northeast is long, signposted by the main quest, and passes a sequence of towns that each introduce a faction
and a mechanic. Most first-time players are funnelled around a clockwise loop of the map and arrive at the city
around level 10-15 having met every major faction.

- Enemies are placed by hand at fixed strength rather than scaled to the player.
- Sawyer says the dangerous creatures near the start were a signal to FO3 players that roaming anywhere was no
  longer safe: "You can't just slide all over the map and not feel the heat." In October 2023 he rejected the
  fan theory that those areas existed to block the route to the Strip, saying they were there for players to
  "Git Gud or Die". Both routes are legitimate; speedrunners and experienced players sneak or sprint north.
- The quarry concept is credited to Sawyer; implementation to Jeff Husges.

**Criticisms.**

| Criticism | Substance |
|---|---|
| Invisible walls | Many climbable-looking ridges are blocked, largely to protect the routing and prevent sequence breaks. Deeply unpopular; Sawyer later said he would insist on as few as possible |
| Sparser map | Fewer dungeon-like points of interest and less "wander and find" than FO3; many map markers are shacks. Supporters reply that locations are connected to quests and factions instead |
| The divided Strip | The city centre is split into several gated cells with load screens and few NPCs. Sawyer recalled seeing it on a console devkit and concluding it would not run; splitting it cost content. Freeside and the suburbs were also sectioned off for console performance. The PS3's split memory pool was the worst constraint |
| Thin Legion territory | Almost everything east of the river was cut; the Legion has one main camp and far fewer quests than the NCR `[widely reported; Sawyer statements not re-verified here]` |
| Scale | Map compressed to roughly 1/60 real scale; the river had to be widened so players could not jump it |
| Cut simulation | Water, farming and governance systems for settlements were simplified |

## 9. Quest design

- Volume: 60+ marked side quests visible in the wiki's base-game list (page truncated; total not confirmed),
  plus many unmarked quests and four DLC campaigns. IGN estimated about 100 hours to do everything.
- Reviewers repeatedly rated side quests above the main story and praised the number of solutions per quest.

| Quest | What it demonstrates |
|---|---|
| **Beyond the Beef** | Four broad routes (expose the conspirator, join him, frame the client, massacre) with sub-variants: sacrifice a companion, lock a member in a freezer, or cook a fake substitute (Survival 75 without the recipe). About 16 distinct skill, stat and perk checks. Entry requires Strip reputation of Accepted |
| **Return to Sender** | A fetch-and-upgrade errand across six ranger stations that turns into discovering a respected officer is falsifying intelligence. Player can expose, excuse or kill him; affects NCR morale and ending slides. Shows a "boring" quest shape used as misdirection |
| **Volare!** (Boomers) | A hostile, isolated tribe reached by running an artillery barrage; winning them needs Idolized reputation earned through many small jobs, then a multi-location salvage job. Every main branch needs them dealt with, and they provide air support at the end |
| **Oh My Papa** (Great Khans) | Outcomes include keeping them with the Legion, turning them to the NCR, making them leave the region, a suicidal last stand, or a leadership coup. Each requires different legwork and skill checks |
| **Still in the Dark** (Brotherhood) | Long bunker chain; can end in alliance, a leadership change, or destruction. House and the Legion demand destruction; the NCR accepts a truce; Independent players choose. A companion's quest interlocks with it |

Common pattern: every quest offers combat, stealth and conversational routes; outcomes write to reputation and
to ending slides; and several quests reference each other's state. The cost was scripting complexity, which is
where a large share of the launch bugs lived.

## 10. Economy

**Sinks.**

| Sink | Cost |
|---|---|
| SPECIAL implants (7) | 4,000 caps each; total implants limited to base Endurance score |
| Sub-Dermal Armor (+4 DT) | 8,000 |
| Monocyte Breeder (1 HP per 10 s) | 12,000 |
| Old World Blues implants (4) | 8,000-20,000 each, 50,000 for all; not Endurance-limited |
| Weapon mods | Hundreds to thousands each, on rotating stock |
| Top-tier weapons | 5,000-20,000 list price (anti-materiel rifle 5,600; Medicine Stick 20,000) |
| Repairs, ammo, GRA uniques | Ongoing |
| Strip entry | 2,000-cap credit check (bypassable by Science, Speech, forged passport, or a monorail) |

The Endurance cap on implants is a neat cross-system hook: it makes Endurance a build-planning stat.

**Sources.**

- Loot and quest rewards, repair-and-sell (two damaged guns become one valuable one), and with Jury Rigging
  the whole world becomes sellable stock.
- **Casinos.** Blackjack, roulette and slots, with outcomes weighted by Luck (at high Luck the player wins most
  hands). Each casino comps the player at thresholds and then bans them from gambling at a winnings cap. The
  Tops: comps at 2,500 / 5,000 / 7,500, ban at 10,000 (verified). Other caps from recall: Atomic Wrangler 5,000,
  Gomorrah 9,000, Ultra-Luxe 15,000, Vikki and Vance 2,500 `[UNVERIFIED]`. Total base-game casino winnings are
  therefore bounded at roughly 40,000 caps. This is a rare example of a gambling minigame with a designed
  ceiling instead of an infinite money exploit.
- **Caravan,** an original card game played against NPCs, has no such cap but is slow.
- **Three currencies** (caps, NCR dollars, Legion coin) exist with fixed exchange rates. Mostly flavour.

**Where it breaks.** The Dead Money DLC ends in a vault holding 37 gold bars worth about 10,500 caps each, with
weight meant to force a choice about how many to carry; players found ways to take all of them, and the DLC
also grants a renewable chip voucher. Sawyer's mod cuts the bar's value from 10,547 to 3,500 and replaces the
recurring voucher. By level 30 most players have nothing left to buy.

## 11. Weapons

Roughly 315 weapon entries in the base game and about 127 more from DLC by one wiki section count (may include
duplicates and non-player variants). FO3 had far fewer. Each common weapon typically has a unique variant.

Stats from fallout.wiki. "Rate" is attacks per second as listed; DPS is damage × rate and overstates
single-shot weapons that reload every round (Gauss rifle, anti-materiel rifle, launchers).

### Guns

| Weapon | Dmg | Rate | Crit × | Ammo | Wt | Value | Skill / STR | Unique variant (dmg, notes) |
|---|---|---|---|---|---|---|---|---|
| 9mm pistol | 16 | 3.1 | 1 | 9mm | 1.5 | 100 | 0 / 2 | Maria: 20, crit ×2 |
| .357 revolver | 26 | 1.75 | 1 | .357 | 2 | 110 | 0 / 3 | Lucky: 30, crit ×2.5, faster |
| Cowboy repeater | 32 | 1.7 | 1.25 | .357 | 5 | 800 | 25 / 4 | La Longue Carabine |
| Service rifle | 18 | 4.2 | 1 | 5.56 | 8.5 | 540 | 25 / 2 | Survivalist's rifle (DLC) |
| Hunting rifle | 52 | 0.95 | 2 | .308 | 6 | 2,200 | 50 / 6 | Paciencia (GRA) |
| Marksman carbine | 24 | 5.7 | 1 | 5.56 | 6 | 5,200 | 100 / 4 | All-American: 26, rate 6 |
| Sniper rifle | 45 | 1.9 | 2 | .308 | 8 | 4,100 | 75 / 6 | Gobi: 48, faster, 4.5 wt; Christine's (silenced) |
| Brush gun | 75 | 1.2 | 1 | .45-70 | 5 | 4,900 | 100 / 6 | Medicine Stick: 78, 20,000 caps |
| Anti-materiel rifle | 110 | 0.45 | 1 | .50 MG | 20 | 5,600 | 100 / 8 | Moddable in GRA |
| Hunting shotgun | 70 | 1.7 | 1 | 12 ga | 7.5 | 3,800 | 75 / 5 | Dinner Bell |
| Riot shotgun | 67 | 4 | 1 | 12 ga | 5 | 5,500 | 100 / 7 | — |
| Minigun | 12 | 20 | 0.5 | 5mm | 25 | 5,500 | 100 / 10 | CZ57 Avenger: 13, rate 30, 18 wt |

Skill requirements for some rows are from recall `[UNVERIFIED]`; STR values are from the wiki.

### Energy weapons

| Weapon | Dmg | Rate | Crit × | Ammo | Wt | Value | Skill / STR | Notes |
|---|---|---|---|---|---|---|---|---|
| Laser rifle | 22 | 3.1 | 1.5 | MFC | 8 | 800 | 25 / 3 | Three good mods; AER14 unique: 35, crit ×2 |
| Laser RCW | 15 | 9 | 0.5 | ECP | 4 | 2,150 | 50 / 4 | Automatic; poor vs DT |
| Plasma rifle | 47 | 1.4 | 2 | MFC | 8 | 1,300 | 25 / 3 | Slow projectile; Q-35 unique: 40, rate 2.4, faster bolt |
| Multiplas rifle | 105 | 1 | 1 | MFC | 7 | 2,500 | 50 / 4 | Energy shotgun |
| Tesla cannon | 80 | 1.3 | 2 | ECP | 8 | 8,700 | 100 / 8 | |
| Gauss rifle | 120 | single | 2 | MFC | 7 | 3,000 | 75 / 5 | YCS/186 unique: 140. Top sniper |
| Plasma caster | 65 | 3 | 1 | MFC | 20 | 7,000 | 100 / 8 | Very high sustained damage |
| Gatling laser | 10 | 30 | 1 | ECP | 18 | 6,800 | 100 / 8 | Crippled by DT; Sprtel-Wood 9700 (GRA): 16 |
| LAER (OWB) | 65 | 2.5 | 1.5 | MFC | 4 | 8,000 | 75 / 4 | Powerful, breaks fast (JSawyer raises durability 75→125) |
| Pew Pew | 75 | 2 | 2.5 | EC | 3 | 2,500 | 0 / 1 | Unique pistol; reward for a long collection quest |
| Alien blaster | 75 | 1.75 | always crits | Alien cells | 2 | 4,000 | 75 / 1 | Finite ammo; only with Wild Wasteland |

### Explosives, melee, unarmed

| Weapon | Class | Dmg | Rate | Crit × | Wt | Value | STR | Notes |
|---|---|---|---|---|---|---|---|---|
| Grenade launcher | Explosives | 30 + round | 0.56 | 1 | 12 | 4,200 | 5 | |
| Thump-Thump | Explosives | unique grenade rifle | 2.8 | 1 | 5.5 | 800 | 3 | Cheap, early, strong |
| Grenade machinegun | Explosives | round | 3 | 1 | 15 | 5,200 | 8 | Mercy unique uses 40mm |
| Missile launcher | Explosives | 125 + blast | — | 0 | 20 | 3,900 | 6 | Annabelle unique |
| Fat Man | Explosives | not retrieved | | | | | | Stats gap |
| Machete | Melee | 11 | 3 | 1.5 | 2 | 50 | 3 | |
| Chance's knife | Melee | 22 | 4.2 | 2 | 1 | 900 | 3 | Early unique, excellent |
| Bowie knife / Blood-Nap | Melee | 23 / 30 | 3.5 / 3.7 | 1.5 | 1 | 1,000 / 1,999 | 3 / 4 | DLC |
| Shishkebab / Gehenna | Melee | 40 / 42 | 2.3 / 2.8 | 2 | 3 | 2,500 / 12,000 | 6 | Fire damage |
| Knock-Knock | Melee | 66 | 1.8 | 1 | 8 | 3,200 | 5 | Unique fire axe |
| Super sledge / Oh, Baby! | Melee | 70 / 80 | 1.6 / 1.7 | 1 | 20 | 5,800 / 6,200 | 8 | |
| Chainsaw | Melee | 80/s | cont. | 1 | 20 | 2,800 | 7 | Ignores DT `[UNVERIFIED]` |
| Thermic lance | Melee | 100/s | cont. | 1 | 20 | 5,500 | 7 | Ignores DT `[UNVERIFIED]` |
| Blade of the West | Melee | 60 | 2.1 | 1.5 | 12 | 5,700 | 9 | DLC |
| Power fist | Unarmed | 40 | 1.1 | 1 | 6 | 800 | 5 | |
| Pushy | Unarmed | 60 | 1.5 | 1 | 6 | 4,200 | 2 | Unique displacer glove |
| Ballistic fist | Unarmed | 80 | 1.1 | 1 | 6 | 7,800 | 9 | Two-Step Goodbye unique: 70, crit ×4 |
| Greased Lightning | Unarmed | 32 | 3 | 1 | 6 | 15,000 | 5 | GRA; highest attack speed |

Observations:
- **Guns** have the most weapons, the most ammo variety, the most mods and the best early availability. A Guns
  character is never short of options. This was a known imbalance.
- **Energy weapons** start weak and expensive to feed, then end with some of the best items. The April 2011
  patch and GRA both tried to lift the middle of the list.
- **Explosives** are strong but self-endangering, heavy in Hardcore, and expensive.
- **Melee and unarmed** scale with perks that ignore armor (Piercing Strike −15 DT; Slayer +30% attack speed),
  special VATS moves, and Super Slam knockdowns; on higher difficulties they out-damage guns.
- **Uniques versus modded commons** is mostly a real trade-off, which is good design. The exceptions are
  uniques with crit multipliers (Lucky, Maria, AER14, YCS/186) that feed the crit build.

### Armor reference

| Armor | Class | DT | Wt | Value | Extras |
|---|---|---|---|---|---|
| Leather / reinforced | Light | 6 / 10 | 15 | 160 / 1,200 | |
| Joshua Graham's armor (DLC) | Light | 15 | 8 | 2,000 | Crit chance bonus `[UNVERIFIED]` |
| Sierra Madre armor, reinforced (DLC) | Light | 18 | 17 | 1,000 | |
| Combat armor / reinforced Mk 2 | Medium | 15 / 20 | 25 | 6,500 / 8,000 | |
| NCR Ranger combat armor | Medium | 20 | 30 | 7,500 | |
| Riot gear / advanced / elite (DLC) | Medium | 20 / 21 / 22 | 30 / 25 / 23 | 7,994 / 8,494 / 12,500 | Elite: +5 crit chance, +10 Guns, +1 CHA |
| Gannon family Tesla armor | Medium | 26 | 35 | 8,194 | +10 Energy Weapons |
| Metal armor | Heavy | 12 | 30 | 1,100 | −1 AGI |
| T-45d power armor | Heavy | 22 | 45 | 4,500 | +2 STR, −2 AGI |
| T-51b power armor | Heavy | 25 | 40 | 5,200 | +1 STR, +25 rad resist |
| Remnants power armor | Heavy | 28 | — | — | Best DT in base game |

Heavy armor slows movement by 15% and medium by 7.5% (JSawyer documentation gives these as the stock values).
The table makes the power-armor problem plain: elite riot gear gives DT 22 at 23 weight in the medium class with
offensive bonuses, against T-51b's DT 25 at 40 weight in the heavy class requiring a training perk. Power armor in FNV is not worth it.

## 12. DLC as mechanical experiments

Each story DLC raises the level cap by 5 and deliberately changes one rule of the base game.

| DLC | Date | Metacritic (PC/360/PS3) | Rule changed | Result |
|---|---|---|---|---|
| **Dead Money** | 21 Dec 2010 | 70 / 70 / 68 | All gear removed on entry. Survival-horror pacing: toxic cloud drains health, bomb collar detonates near radios, enemies revive unless dismembered, invincible holograms on patrol routes, vending machines fed by scavenged chips, no fast travel, no leaving until done | Most divisive. Avellone wanted "miracle items like Stimpaks to feel amazing again". Praised for tension and theme; criticised for frustration, difficulty spike and bugs. Reputation has grown over time |
| **Honest Hearts** | 17 May 2011 | 66 / 64 / 66 | Carry-weight limit on entry (about 75 lb, more with certain skills/perks `[UNVERIFIED]`). Open wilderness map, foraging, food replaces stimpaks | Liked for exploration and a hidden environmental story told through terminals; criticised for fetch quests and a short main line |
| **Old World Blues** | 19 Jul 2011 | 82 / 83 / 81 | Open sandbox hub; talking home base with upgradable appliances that convert junk into supplies; new traits and a free respec of traits; high-HP enemies | Best reviewed. Writing praised; combat criticised as bullet-sponge |
| **Lonesome Road** | 20 Sep 2011 | 62 / 63 / 57 | Linear corridor, no companions except a robot, detonating warheads to open paths, very strong enemies and very strong loot | Criticised for linearity; supplies the game's most overpowered gear |
| **Gun Runners' Arsenal** | 27 Sep 2011 | n/a | Weapons, mods, ammo types and a challenge list | A balance patch sold as content; adds late-game caps sinks |
| **Courier's Stash** | 27 Sep 2011 | n/a | Pre-order item packs given at start | Unbalances the opening; JSawyer scatters them around the map instead |

Takeaway: the DLCs show how far the base systems could be pushed by subtracting player resources (Dead Money,
Honest Hearts) and how cap raises plus ever-better loot (Lonesome Road) hollow out the core game.

## 13. Balance assessment

### Dominant builds

| Build | Why it wins |
|---|---|
| **Sneak-crit sniper** | Sneak attacks always crit and multiply damage; a 110-140 base hit ignores most DT; Better Criticals (+50% crit damage), suppressed GRA anti-materiel rifle, Boone or ED-E spotting. Kills nearly anything in one shot from outside aggro range |
| **Crit stacker** | Luck 10 + Finesse (+5%) + Built to Destroy (+3%) + Light Touch (+5%) + elite riot gear or light armor bonuses + high-multiplier uniques. Approaches guaranteed crits on fast weapons |
| **Melee / unarmed** | Piercing Strike, Slayer, Super Slam, cheap ammo (none), strong chems; ballistic fist or thermic lance class weapons |
| **Shotgun** | Shotgun Surgeon (−10 DT), And Stay Back (knockdown chance per pellet), riot shotgun: stun-locks everything |
| **High-INT generalist** | With cap 50, maxes almost every skill and passes almost every check; no real downside |

### Overpowered items and perks

| Item | Problem |
|---|---|
| Anti-materiel rifle (esp. GRA version with suppressor) | Highest per-shot damage among guns; AP, match and explosive rounds; silenced in GRA |
| Gauss rifle / YCS/186 | Energy equivalent with crit ×2 |
| Riot gear family | Medium weight class, top-tier DT, offensive bonuses; obsoletes power armor |
| Riot shotgun + And Stay Back | Perma-knockdown |
| Holorifle, LAER, DLC uniques | Outscale base-game enemies |
| Jury Rigging | Repair anything with anything; breaks condition economy and caps economy |
| Turbo, Psycho, Med-X, Slasher stacks | Chem stacking has no real cost outside Hardcore |
| Stimpaks | Weightless and plentiful; healing is never a constraint on normal |
| Dead Money gold and vouchers | Ends the economy |
| Companions (two at once) | Carry the player through normal difficulty |

### Weak options

| Option | Why |
|---|---|
| **Charisma** | Only feeds Speech/Barter starting values and companion nerve. Skill points compensate cheaply. The standard dump stat |
| **Barter** | Money stops mattering; dialogue checks are its only real use |
| **Survival** (non-Hardcore) | Crafting is optional and food is unnecessary |
| **Automatic weapons** | DT floor punishes low per-shot damage; need AP ammo and eat condition |
| **Energy weapons early** | Scarce, costly ammo; low damage |
| **Power armor** | Needs training perk from specific quests, heavy, slow, and out-performed by DLC medium armor |
| **Karma** | Does nothing |
| **Many perks** | A long tail of flavour perks that no optimiser takes, though perk-every-2-levels makes that more painful |

### What Sawyer said he would change: the JSawyer mod

Released 29 Dec 2011, after patch support ended; final version 5.1 on 29 Sep 2012. Sawyer framed it as changes
he personally preferred but was not sure the FO3 audience would accept, and that the team had no time to
experiment with. It is the most direct record of his view of the shipped balance.

| Area | Shipped | JSawyer | What it says about the original |
|---|---|---|---|
| Level cap | 30 (50 with DLC) | 15 (35 with DLC); XP curve steeper; DLC main-quest XP −66% | Characters become good at everything |
| Player HP | 100 + END×20 + 5/level | 50 + END×10 + 5/level | Player is too tanky |
| Carry weight base | 150 | 50 | Inventory limits never bind |
| Strong Back | +50 | +25 | Same |
| Stimpak weight | 0 | 0.25 (super: 0.5) | Healing is unlimited |
| Stimpak supply | Common | Mostly replaced by weaker expired stimpaks, 4:1 | Same |
| Hardcore need rates | See section 4 | Doubled; thresholds retuned | Hardcore is too gentle |
| Heavy / medium armor speed penalty | 15% / 7.5% | 10% / 5% | Heavy armor over-penalised |
| Armor DR | None on most armor | Added DR on top of DT: T-51b 30, T-45d 25, Remnants 35, combat 8, riot gear 12-14 | Pure DT made heavy armor weak against big hits and power armor underwhelming |
| Weak sidearms | 9mm 16, laser pistol 12 | 18, 16 | Low-tier weapons fall off too fast |
| Plasma projectile speed | Slow | Doubled | Plasma missed moving targets |
| Fragile energy weapons | LAER 75 HP, Tesla cannon 80 | 125, 160 | Condition punished energy builds |
| Grunt / Cowboy perks | +25% | +20% | Too strong |
| Rushing Water (unarmed speed) | +50% | +20% | Too strong |
| Demolition Expert | 3 ranks | 2 ranks, +10% each with blast radius | Too strong |
| Gold bar | 10,547 caps | 3,500 | Economy breaker |
| Pre-order packs | Given at start | Placed in the world and in a shop, weakened | Free power at level 1 |
| Karma | Odd values | Rebalanced, NPC alignments corrected | Acknowledged as broken |

Other positions attributed to Sawyer in interviews and Q&A, not re-verified in this session
`[UNVERIFIED]`: that the DLC level-cap raises were a mistake for balance; that the Strip and Legion lands were
the content cuts he most regretted; that he would drop karma entirely; and that he prefers every skill to have
comparable value, which he later pursued in Pillars of Eternity. His line on balance work in general:
"Tuning is a never-ending process."

## 14. Gaps

- Hardcore per-round ammo weights and exact stimpak heal durations were not retrieved.
- Fat Man stats, complete side-quest count, and most casino caps are not verified.
- The GDC 2012 talk was consulted via abstract and secondary notes only.
- Sawyer's Tumblr/Formspring archive could not be searched (search budget exhausted); statements tagged above.
- Nukapedia was not reachable, so several numbers rest on fallout.wiki alone.
- Team size and budget not found.

## Design Takeaways

**Learn from**

- **Subtractive armor plus a damage floor.** It turns weapon and ammo choice into decisions with one extra
  number. Keep the floor (20% feels right) so nothing is ever fully immune, and show a clear "your hit was
  absorbed" indicator. Fix what FNV got wrong: give rapid-fire weapons a native role (built-in penetration,
  stagger, suppression) so they do not depend on special ammo, and give heavy armor a second defensive property
  so it is not strictly worse than good medium armor.
- **Ammo variants as cheap depth.** Three or four variants per calibre with one clean trade-off each
  (penetration versus damage versus wear versus cost) is enough. Do not ship fifteen shotgun shells.
- **Deterministic, visible skill checks using every skill.** Show the requirement, show the near-miss, make
  failure a line of dialogue instead of a locked door. Pair with scarce temporary boosters so thresholds bend.
  Then protect it: keep the level and skill budget tight enough that one character cannot pass everything.
- **Two-track reputation per faction.** Fame and infamy that do not cancel produce memorable mixed standings.
  Go further than FNV did: make the mixed states mechanically distinct, and make secret actions discoverable later.
- **Minor factions as shared content.** Build one set of mid-sized faction quests and let each main branch want
  a different outcome from them. Enormous replay value for the content cost.
- **Kill-anyone with a failsafe.** Duplicate critical information, fail quests cleanly, and keep one route that
  cannot be closed. But make the failsafe route cost something, so it is not simply the best ending.
- **Authored difficulty geography.** Fixed-strength enemies make the map itself a progression system and let
  skilled players sequence-break. Signpost danger diegetically (warnings from locals, corpses, signs).
- **Traits with real downsides, and slower perk cadence.** Fewer, weightier choices.
- **Bounded minigame economy.** Casinos that ban winners are funny, in-fiction, and stop infinite money.
- **Cross-system hooks** like implant count limited by Endurance: one line of rules that makes a stat matter.
- **Optional survival mode whose meaningful rules are about healing and weight,** not meters.

**Avoid**

- **Raising the level cap with every expansion.** It dissolves build identity and all later balance. Add
  horizontal options instead, or plan the final cap from day one.
- **Weightless, instant, abundant healing.** It removes attrition, which is the heart of post-apocalyptic play.
- **Survival meters that are only chores.** If thirst never threatens the player, it is a tax. Tie needs to
  route planning and scarcity, or leave them out. Give the hard mode a real reward.
- **A vestigial morality meter** alongside reputation. One system, done properly.
- **Dump stats.** If a stat can be bought back with skill points or gear, it will be dumped. Give every
  attribute at least one thing nothing else provides.
- **One weapon skill with twice the content of the others.** Audit weapon counts, ammo, mods and early
  availability per skill.
- **Invisible walls.** If terrain must block, make it look impassable.
- **Designing the capital city last and beyond the memory budget.** Prototype the densest space first on the
  weakest target hardware.
- **Features that cost more than they return under a fixed schedule** (disguises). Cut early.
- **Day-one bonus items and DLC loot that outclass the base progression.** Place them in the world at an
  appropriate tier.
- **Shipping on a borrowed engine in 18 months without a stabilisation phase.** Reactivity multiplies script
  state; budget QA time in proportion to branching, and never accept a contract where the bonus hinges on a
  review aggregate the schedule makes hard to hit.

## Sources

Pages fetched and read for this document:

- https://fallout.wiki/wiki/Damage_Threshold_(Fallout:_New_Vegas)
- https://fallout.wiki/wiki/Damage_Threshold
- https://fallout.wiki/wiki/Fallout:_New_Vegas_ammunition
- https://fallout.wiki/wiki/Fallout:_New_Vegas_weapons
- https://fallout.wiki/wiki/Fallout:_New_Vegas_weapon_mods
- https://fallout.wiki/wiki/Fallout:_New_Vegas_armor_and_clothing
- https://fallout.wiki/wiki/Fallout:_New_Vegas_skills
- https://fallout.wiki/wiki/Fallout:_New_Vegas_perks
- https://fallout.wiki/wiki/Fallout:_New_Vegas_implants
- https://fallout.wiki/wiki/Fallout:_New_Vegas_companions
- https://fallout.wiki/wiki/Fallout:_New_Vegas_reputations
- https://fallout.wiki/wiki/Fallout:_New_Vegas_quests
- https://fallout.wiki/wiki/Fallout:_New_Vegas_patches
- https://fallout.wiki/wiki/Fallout:_New_Vegas
- https://fallout.wiki/wiki/Hardcore_mode
- https://fallout.wiki/wiki/Yes_Man
- https://fallout.wiki/wiki/Beyond_the_Beef
- https://fallout.wiki/wiki/Dead_Money
- https://fallout.wiki/wiki/The_Tops
- https://fallout.wiki/wiki/JSawyer
- https://fallout.wiki/wiki/Mod:JSawyer/Documentation
- https://en.wikipedia.org/wiki/Fallout:_New_Vegas
- https://en.wikipedia.org/wiki/Fallout:_New_Vegas_downloadable_content
- https://rpgcodex.net/article.php?id=6694 (Sawyer on DT and weapon design, 2 May 2010)
- https://www.engadget.com/2010/05/05/interview-josh-sawyer-on-fallout-new-vegas/
- https://www.pcgamesn.com/fallout-new-vegas/making-of-fallout-new-vegas-josh-sawyer
- https://gdcvault.com/play/1015758/Do-(Say)-The-Right-Thing (abstract only)
- https://gazdalman.github.io/synthesis_product-project/Sources/Source-3 (secondary notes on the GDC talk)

Read as search-result summaries or headlines only (article body not retrieved):

- https://pcgamer.com/games/rpg/josh-sawyer-says-fallout-new-vegas-has-deathclaws-in-cazador-as-a-warning-to-fallout-3-players-expecting-another-easy-ride-you-cant-just-slide-all-over-the-map-and-not-feel-the-heat
- https://gamesradar.com/fallout-new-vegas-director-debunks-13-year-old-theory-about-the-rpgs-most-infamous-areas-they-were-there-for-players-to-git-gud-or-die
- https://gamesradar.com/games/rpg/fallout-new-vegas-director-took-one-look-at-the-strip-on-a-console-devkit-and-thought-oh-my-god-this-isnt-going-to-run
- https://www.techradar.com/gaming/consoles-pc/fallout-new-vegas-director-debunks-popular-fan-theory-over-a-decade-later
- https://80.lv/articles/fallout-new-vegas-strip-content-was-cut-to-run-on-console
- https://www.gameinformer.com/b/news/archive/2012/03/15/obsidian-missed-new-vegas-bonus-payment-by-a-single-metacritic-point.aspx
- https://www.engadget.com/2012/03/15/obsidian-missed-fallout-new-vegas-metacritic-bonus-by-one-point
- https://kotaku.com/why-are-game-developer-bonuses-based-on-review-scores-5893595
- https://www.gamespot.com/articles/obsidian-denied-bonus-over-new-vegas-metacritic-score-studio-head/1100-6366337/
- https://forums.obsidian.net/topic/59386-obsidian-at-gdc-2012/
- https://en.wikipedia.org/wiki/Deathclaw

Attempted but unavailable: fallout.fandom.com (Nukapedia) pages returned HTTP 402 to automated fetches.
