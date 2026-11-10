# Fallout 3 (2008) — Gameplay, Systems and Balance

Scope: how Fallout 3 plays, how its rules work numerically, where the balance holds and where it collapses, and
what it fixed in place as the template for every later 3D Fallout. Story, lore and art are covered elsewhere.

Confidence key: figures with no tag were confirmed against at least one source fetched for this document
(mostly fallout.wiki pages built from game data). `[UNVERIFIED]` means the figure is recalled from general
knowledge of the game and could not be re-checked in this session (Nukapedia/Fandom and the UESP GECK wiki
refused automated fetches, and the web-search budget ran out before the last few checks). `[DISPUTED]` means
sources disagree.

## Quick Reference

- **Format shift:** isometric turn-based CRPG became a first/third-person real-time open world on Bethesda's
  Oblivion-era Gamebryo engine. Released 28 Oct 2008 (NA) on PC, Xbox 360, PS3. Metacritic 91 / 93 / 90.
  4.7 million shipped in week one; ~12.4 million lifetime (EEDAR estimate, 2015).
- **Core loop:** pick a compass blip, walk to it, clear it with guns + V.A.T.S., strip it of loot, repair/sell,
  level up, repeat. The world, not the main quest, is the content.
- **V.A.T.S.:** pauses combat, spends Action Points (AP = 65 + 2 x Agility) on queued, body-part-targeted shots
  at a displayed hit percentage (max 95%). While it plays out the player takes **10% of normal damage** and
  gets **+15 critical chance**, at the price of roughly 4-5x weapon wear.
- **V.A.T.S. was designed as a "panic button"** (Emil Pagliarulo) and the combat was balanced assuming its use.
  It is also a crutch for weak real-time shooting.
- **Character system:** 7 SPECIAL stats (40 points at creation), 13 skills (0-100), 3 tag skills (+15 each),
  10 + Intelligence skill points per level, **one perk every level**.
- **Level cap 20, raised to 30 by Broken Steel.** XP to next level = 50 + 150n; 29,450 XP total to 20, 66,700
  to 30.
- **Convergence:** with skill books (about 25 per skill, +1 each, +2 with Comprehension), 13 skill bobbleheads
  (+10) and 7 SPECIAL bobbleheads (+1), a level-30 character can have 100 in every skill and 9-10 in every
  stat. Builds stop mattering around level 15-20.
- **Broken perks:** Grim Reaper's Sprint (level 20: any V.A.T.S. kill refills all AP) and Almost Perfect
  (level 30: all SPECIAL set to 9).
- **Damage Resistance** is a flat percentage reduction, hard-capped at **85%**. Power armor + two perks gets
  close to the cap permanently.
- **Weapon skill affects both damage and spread; weapon condition affects damage** (down to 66% / 54% / 50% of
  base at 0% condition for single-shot / automatic / melee). Repair needs a duplicate item, and maximum
  repairable condition = 40% + 0.6% x Repair.
- **Level scaling** is softer than Oblivion's: leveled lists with few tiers, and each encounter zone locks to
  the player's level on first entry.
- **Broken Steel bullet sponges:** Albino Radscorpion 1,500 HP, Super Mutant Overlord 1,250 HP, Feral Ghoul
  Reaver 1,100 HP, versus 100-500 HP for most base-game enemies.
- **Speech checks are percentage rolls** (Charisma multiplier x Speech / check difficulty), one attempt per
  conversation, which trains players to quicksave and reload.
- **Lockpicking and hacking are hard-gated minigames** at skill 0/25/50/75/100; player dexterity does not
  substitute for skill.
- **Karma** runs -1000 to +1000 in five bands. It gates companions, sends hit squads (Talon Company if good,
  Regulators if evil) and changes radio commentary, but it is a single global number with easy resets.
- **World:** a compact map (a few square miles of real terrain) packed with hand-built locations, most of
  which tell a small story through props, terminals and corpses. This is the game's most praised feature.
- **Downtown D.C.** is a set of disconnected surface pockets linked by metro tunnels; widely disliked for
  navigation, and Bethesda itself cut back a more realistic network because miles of tunnel were dull.
- **Quests:** about 15 main quests and 17 named side quests (plus roughly 23 unmarked and 16 repeatable). Few,
  but most side quests have several distinct solutions.
- **Economy:** caps, ammo and stimpaks pile up; by mid-game nothing is scarce on Normal. Merchants' limited
  cash is the only real limit on wealth.
- **Stability:** frequent crashes and quest-breaking bugs at launch on all platforms; PS3 and the PS3 Game of
  the Year edition were notably worse; the PC version needs community fixes on modern Windows.

## 1. From isometric turn-based to first-person open world

| Item | Detail |
|---|---|
| Developer / publisher | Bethesda Game Studios / Bethesda Softworks |
| Licence | Acquired from Interplay in 2004 ($1.175 million minimum guaranteed advance) |
| Development | Started late 2004 with ~10 people while Oblivion was in production; grew to ~75 after 2006 |
| Engine | Gamebryo (the Oblivion codebase, extended) |
| Release | 28 Oct 2008 NA; 30/31 Oct 2008 PAL; 4 Dec 2008 Japan |
| Key leads | Todd Howard (game director), Emil Pagliarulo (lead designer / writer), Istvan Pely (lead artist) |
| Metacritic | PC 91, Xbox 360 93, PS3 90 |
| Sales | 4.7M shipped in week one (~$300M); ~12.4M lifetime by 2015 (EEDAR estimate) |
| Awards | GDC Game of the Year and Best Writing; multiple outlet GOTYs; Golden Joystick Ultimate GOTY 2009 |

What the engine choice brought with it, for good and ill:

- **Inherited from Oblivion:** a seamless exterior worldspace streamed in cells with separately loaded
  interiors; a compass that shows nearby undiscovered locations; fast travel to discovered markers; "Radiant"
  NPC schedules; containers and physics-enabled clutter everywhere; leveled lists; quicksave anywhere; the
  dialogue camera that zooms to a stiffly animated face.
- **Added for Fallout:** V.A.T.S., a locational damage and limb-crippling model, weapon/armor condition and
  repair, radiation, the wrist-computer menu (inventory, stats, map, quests and radio in one diegetic device),
  karma, perks, and radio stations.
- **Lost from Fallout 1/2:** turn-based combat, traits, the overworld travel map with discrete towns, most
  skill-gated dialogue breadth, and hard time limits.
- The camera can be first or third person, but animations, weapon handling and interface are built for first
  person; third person is widely considered a novelty.

The significance is less technical than structural: Fallout became a game about **walking across a continuous
ruined landscape and stumbling into things**, not about travelling between hubs and talking.

## 2. Moment-to-moment loop

1. **Spot** something: a compass tick, a silhouette on the skyline, a radio signal, a quest marker.
2. **Travel** on foot across open terrain; random and placed encounters interrupt.
3. **Fight** through an exterior camp or a loaded interior "dungeon" (office, vault, factory, metro, cave).
4. **Loot** everything: every desk, locker, ammo box and corpse is a container. Carry weight is
   150 + 10 x Strength lb, and it fills fast.
5. **Maintain:** repair gear by consuming duplicates, use stimpaks, clear radiation.
6. **Fast travel** to a hub, sell junk, buy ammo, hand in quests.
7. **Level up:** distribute skill points, choose a perk.

Design observations:

- XP comes from kills, quests, lockpicking/hacking (20-60 XP each), speech successes and location discovery,
  so nearly any activity advances the character. That is why exploration feels rewarding even without quests.
- The loop is strongest in the first 10-12 levels, when ammunition, armor condition and health are all
  genuinely limited. It weakens badly once the player is rich and over-skilled (see sections 12 and 20).
- There is no hunger, thirst or sleep requirement. Radiation is the only survival pressure and it is mild:
  resistance from Endurance is only (Endurance - 1) x 2%, but RadAway and doctors are cheap and plentiful.

## 3. V.A.T.S.

### 3.1 How it works

Pressing the V.A.T.S. button freezes time, zooms on the nearest target and overlays each body part with a hit
percentage and condition bar. The player queues attacks until AP run out, then watches them resolve in slow
motion from cinematic cameras. Afterwards AP regenerate in real time and the player fights conventionally (or
hides) until enough return.

| Parameter | Value | Notes |
|---|---|---|
| Action Points | 65 + 2 x Agility | 67 at AGI 1, 85 at AGI 10; Action Boy/Girl perk +25 |
| Max hit chance | 95% | `fVATSMaxChance` |
| Hit chance inputs | weapon skill, distance, weapon spread, target part size, visibility, weapon condition | Exact formula not published in the sources reached |
| Damage taken by player during playback | x0.1 (90% reduction) | `fVATSPlayerDamageMult = 0.1` |
| Critical chance bonus | +15 (percentage points) | `fVATSCriticalChanceBonus = 15` |
| Weapon wear | 4x normal per the wiki prose; the game setting is 5 | `fVATSDamageToWeaponMult`; `[DISPUTED]` between the two figures on the same page |
| Spread multiplier in V.A.T.S. | x0.5 | `fVATSSpreadMult` |
| Melee in V.A.T.S. | reach x2 (max 300 units); automatic-melee damage x2 | Player lunges to the target |
| Max engage distance | 5,000 units (~71 m) | |
| Concentrated Fire perk | +5% per queued shot on the same part | Level 18 |
| Sniper perk | +25% head hit chance | Level 12 |
| Commando / Gunslinger | +25% accuracy with two-handed / one-handed guns | Levels 8 / 6 |
| Mysterious Stranger | 10% chance to finish a target under 150 HP | Luck 6 perk |

AP cost per attack (per shot or burst):

| Weapon | AP | Shots per full bar at AGI 5 (75 AP) | Confidence |
|---|---|---|---|
| Hunting rifle | 25 | 3 | Verified |
| Metal Blaster (unique laser rifle) | 17 | 4 | Verified |
| Firelance (unique alien pistol) | 20 | 3 | Verified |
| Gauss rifle (DLC) | 38 | 1 | Verified |
| Mesmetron, Auto Axe | 65 | 1 | Verified |
| 10mm pistol, laser rifle | ~17 | 4 | `[UNVERIFIED]` |
| Assault rifles, combat shotgun | ~23-27 | 2-3 | `[UNVERIFIED]` |
| Sniper rifle | ~38 | 1 | `[UNVERIFIED]` |
| Missile launcher / Fat Man | ~55 / ~65 | 1 | `[UNVERIFIED]` |

So a typical V.A.T.S. activation is **3-4 pistol or rifle shots, 2-3 automatic bursts, or 1 heavy shot**, after
which AP take several seconds to return.

Targeting specific parts has mechanical payoffs: headshots deal double damage; crippled legs slow the target;
crippled arms wreck its accuracy; a crippled head cuts Perception by 4; shooting a weapon can knock it out of
the target's hands or destroy it; insect antennae cause frenzy; some robots have a combat-inhibitor weak
point. Limbs on the player work the same way and need a bed, a doctor or a stimpak applied to the limb.

### 3.2 Why it exists

- Pagliarulo described V.A.T.S. as his initial design, drawing on the aimed shots of Fallout 1 and 2, with the
  cinematic replays suggested by Todd Howard after both had played a lot of Burnout's crash mode. Howard's
  pitch, as widely reported, was to imagine the flying car parts as eyeballs and guts.
- Pagliarulo's summary of the core was "pause game; queue up actions; watch actions play out cinematically."
  He resisted a pure slow-motion version because he wanted a **"panic button"**: a moment to stop and assess.
- He also stated: "We designed the combat balance with V.A.T.S. use in mind."
- A later developer retrospective (reported by GamesRadar) framed it as cover for a studio with little shooter
  experience: "We were never going to create gun combat that was on par with Call of Duty or Battlefield."
  (Speaker not confirmed here; the article body could not be retrieved.)

V.A.T.S. is therefore a bridge in three senses: it preserves **stat-driven to-hit rolls and called shots** from
the turn-based games; it lets players without shooter reflexes play; and it gives an action game a
recognisable Fallout signature.

### 3.3 Balance problems

- **Near-invulnerability.** A 90% damage reduction during playback means V.A.T.S. is defensively better than
  cover. Chaining it (helped by AP chems and perks) turns the player into a tank.
- **Grim Reaper's Sprint** removes the AP economy altogether: one kill refills the bar, so any fight against
  several weak enemies is one continuous V.A.T.S. sequence at 10% incoming damage.
- **Two-speed combat.** The optimal rhythm is: empty the AP bar, then retreat or circle until it refills. The
  real-time gap is the weakest part of the game, so the system highlights rather than hides the gunplay.
- **Repetition.** Kill cameras are spectacular for ten hours and slow for the next fifty; they cannot be
  skipped, only shortened.
- **Crit stacking.** +15 flat critical chance on top of Luck x 1% (+5 from Finesse), multiplied by the weapon's
  critical multiplier, makes high-multiplier weapons crit most of the time. Better Criticals adds +50% crit
  damage. Sneak attacks double total damage and headshots double it again; the wiki's own worked example takes
  a 440-damage shotgun blast to 2,480.
- **The wear penalty is not a real cost**, because repair fodder is abundant (section 7).
- **Melee/unarmed** benefit most: V.A.T.S. teleports the character into range and Paralyzing Palm (30% chance
  per strike, 30-second paralysis) trivialises single tough enemies.

## 4. Character system

### 4.1 SPECIAL

40 points at creation (5 in each of 7 stats, 5 free to move; range 1-10).

| Stat | Derived effects | Skills governed |
|---|---|---|
| Strength | Carry weight 150 + 10 x ST; melee damage +0.5 x ST | Melee Weapons |
| Perception | Compass detection range | Energy Weapons, Explosives, Lockpick |
| Endurance | HP = 90 + 20 x EN + 10 x Level; rad resist (EN-1) x 2%; poison resist (EN-1) x 5% | Big Guns, Unarmed |
| Charisma | Speech-check multiplier (100% at CH 1 to 206% at CH 10) | Barter, Speech |
| Intelligence | Skill points per level = 10 + IN | Medicine, Repair, Science |
| Agility | AP = 65 + 2 x AG | Small Guns, Sneak |
| Luck | Critical chance = LK x 1%; +ceil(LK/2) to every starting skill | (all, slightly) |

Observations:

- **Intelligence dominates.** IN 9 or 10 gives roughly twice the skill points of IN 1 over a full game. Since
  skills are what gate content, IN is close to mandatory for a first-time optimiser.
- **Charisma is the dump stat.** Its only effects are small skill bonuses and the speech multiplier, and speech
  failure is reversible by reloading.
- The stat-derived differences are small. HP at level 20 is 310 for EN 1 versus 490 for EN 10; AP is 67 versus
  85. Compared with Fallout 1/2, SPECIAL was demoted from character identity to modest tuning.
- Raising stats later: 7 SPECIAL bobbleheads (+1 each), the Intense Training perk (+1, 10 ranks), No
  Weaknesses (Broken Steel, level 24: every stat below 5 becomes 5), Almost Perfect (level 30: every stat
  becomes 9). Taking Almost Perfect *before* collecting bobbleheads yields 10 in everything, a widely known
  ordering trick `[UNVERIFIED in this session, but consistent with the perk's "set to 9" wording]`.

### 4.2 Skills

Thirteen skills, cut down from the eighteen of Fallout 1/2 (First Aid and Doctor merged into Medicine; Steal
folded into Sneak; Traps into Explosives/Repair; Gambling and Outdoorsman removed; Throwing folded away).

| Skill | Stat | What it does |
|---|---|---|
| Barter | CH | Sell at 45-90% of value, buy at 155-110% |
| Big Guns | EN | Damage/accuracy with miniguns, flamers, launchers |
| Energy Weapons | PE | Damage/accuracy with lasers and plasma |
| Explosives | PE | Grenade/mine damage; disarming mines |
| Lockpick | PE | Gates lock tiers at 0/25/50/75/100 |
| Medicine | IN | Scales stimpak and RadAway effectiveness |
| Melee Weapons | ST | Melee damage |
| Repair | IN | Max repairable condition 40% + 0.6% x skill; crafting quality |
| Science | IN | Gates terminal tiers at 25/50/75/100 |
| Small Guns | AG | Damage/accuracy with conventional firearms |
| Sneak | AG | Detection chance; pickpocket success |
| Speech | CH | Speech-check probability |
| Unarmed | EN | Unarmed damage (skill/20 + 0.5) |

- Starting value: 2 + 2 x stat + ceil(Luck / 2). A stat of 5 with Luck 5 gives 15.
- Tag skills: 3, each +15 once. (In Fallout 1/2 tags doubled the rate of skill gain; here they are a flat,
  one-time bonus, which makes them much less defining.)
- Points per level: 10 + Intelligence; +3 with the Educated perk (available at level 4). So 11-23 per level.
- Skills cap at 100.
- Raising a skill has **no escalating cost**: point 99 costs the same as point 20. Fallout 1/2 charged more
  per point at high values. This flat cost is a major cause of the convergence below.

### 4.3 Perks

- **One perk at every level-up** (19 picks to level 20, 29 to level 30). Fallout 1/2 gave one every three
  levels (four with a particular trait) and had traits; Fallout 3 has no traits.
- 58 regular perks in the base game plus 14 from Broken Steel, alongside quest and special perks.
- Many early perks are just "+5 to two skills" (and similar), which become worthless once skills cap. This
  filler dilutes the choice.

| Perk | Level | Requirement | Effect | Assessment |
|---|---|---|---|---|
| Intense Training | 2 | - | +1 to a SPECIAL stat (10 ranks) | Fine; rare way to fix stats |
| Educated | 4 | IN 4 | +3 skill points per level | Mandatory early pick; accelerates convergence |
| Comprehension | 4 | IN 4 | Skill books give +2 instead of +1 | Up to +25 per skill; mandatory for completists |
| Toughness | 6 | EN 5 | +10% DR | Strong, stacks toward the 85% cap |
| Gunslinger / Commando | 6 / 8 | - | +25% V.A.T.S. accuracy by weapon class | Solid |
| Finesse | 10 | - | Crit chance as if +5 Luck | Strong |
| Sniper | 12 | PE 6, AG 6 | +25% V.A.T.S. head hit chance | Strong |
| Cyborg | 14 | Medicine 60, Science 60 | +10% DR, poison and rad resist, +10 Energy Weapons | Strong |
| Action Boy/Girl | 16 | AG 6 | +25 AP | Roughly one more shot per activation |
| Better Criticals | 16 | PE 6, LK 6 | +50% critical damage | Very strong with V.A.T.S. crit bonus |
| Concentrated Fire | 18 | Small Guns 60, Energy Weapons 60 | +5% hit chance per repeat shot | Good |
| Paralyzing Palm | 18 | Unarmed 70 | 30% chance of 30 s paralysis per V.A.T.S. strike | Trivialises single targets |
| Explorer | 20 | - | Reveals every map marker | Removes the discovery loop |
| **Grim Reaper's Sprint** | 20 | - | A V.A.T.S. kill restores all AP | **Breaks the AP economy** |
| Quantum Chemist | 22 | Science 70 | 10 Nuka-Colas become 1 Quantum | Novelty |
| No Weaknesses | 24 | - | Stats below 5 raised to 5 | Erases stat trade-offs |
| Karma reset perks (three) | 24 | Karma condition | Set karma to Very Good / Neutral / Very Evil | Makes karma meaningless |
| Nerves of Steel | 26 | AG 7 | Faster AP regeneration | Good |
| Warmonger | 26 | IN 7 | All craftable weapons without schematics | Skips a collection loop |
| **Almost Perfect** | 30 | - | All SPECIAL set to 9 | **Erases the stat system** |
| Nuclear Anomaly | 30 | - | Explode at 20 HP or less | Dangerous to self and allies |

Grim Reaper's Sprint was toned down in New Vegas (to a partial AP refund) and Fallout 4 made it a chance-based
effect, which is a fair indication that later designers agreed it was overtuned.

### 4.4 Levelling and the level cap

- XP from level n to n+1 = 50 + 150n: 200 XP for level 2; 3,050 XP for level 21.
- Cumulative: 29,450 XP for level 20; 66,700 XP for level 30.
- HP +10 per level. No stat gain per level.
- Base-game cap of 20 was reached by thorough players well before finishing the map (often with a third to a
  half of locations unvisited), after which kills and quests gave no progression reward. This and the
  hard-stop ending were the two loudest post-launch complaints. Broken Steel (5 May 2009) addressed both: cap
  30, and play continues after the finale. Todd Howard has since said the studio did not expect players to
  hate the ending's full stop.

### 4.5 Why every character converges on master-of-all

Skill budget, worked through (my arithmetic from the verified formulas above):

| Source | Points (IN 9-10 build) |
|---|---|
| Starting values, 13 skills at ~15-17 each | ~210 |
| 3 tags x 15 | 45 |
| Level-ups 2-20: 19 x 20 (IN 10) | 380 |
| Educated from level 4 (16 further levels x 3) | 48 |
| 13 skill bobbleheads x 10 | 130 |
| Skill books, ~25 per skill x 13 x 1 | ~325 (or ~650 with Comprehension) |
| **Total at level 20** | **~1,140 without Comprehension, ~1,460 with** |
| Levels 21-30 (Broken Steel): 10 x 23 | +230 |
| **Needed for 100 in all 13 skills** | **1,300** |

- In the base game a diligent book-collector with Comprehension can already max everything by level 20. A
  casual player who finds a third of the books still ends with 9-10 skills at or near 100.
- With Broken Steel, maxing all 13 is comfortable even without full book collection. The wiki notes that
  merely training each skill to about 40 is enough to reach 100 once books, bobbleheads and bonuses are added.
- Add Almost Perfect and the seven SPECIAL bobbleheads, and stats converge too.
- Two skills (Big Guns and Science) even have repeatable book sources, removing the last limit.

Consequences: no build identity, no replay motivation from the character sheet, no reason to bring a
companion for a missing skill, and skill-gated content stops being a choice and becomes a schedule.
New Vegas responded by granting a perk every *two* levels, lowering books to a smaller count with bigger
bonuses and adding traits back; Fallout 4 removed skills entirely.

## 5. Gunplay without V.A.T.S.

Real-time shooting uses a physical projectile/hitscan model modified by character stats.

**Spread** (cone of fire), from the game's settings:

Spread = Perks( IronSights x Crouch x (ConditionTerm + SkillTerm) x Movement + ArmPenalty ), never below the
weapon's own minimum spread.

| Term | Value |
|---|---|
| Aiming (zoom) | x0.35 |
| Crouching | x0.6 (x0.21 combined with aiming) |
| Skill term | 0.5 - 0.005 x skill (0.5 at skill 0, 0.25 at 50, 0 at 100) |
| Condition term | 0 by default (condition does not affect spread in the shipped settings) |
| Crippled arm | +0.5 (one-handed, right arm), +0.25 per arm for two-handed |
| Per-weapon base | e.g. hunting rifle 0.3 |

**Damage vs. weapon skill:** the engine's skill bonus is base + mult x skill/100 with both settings at 0.5,
i.e. **50% of listed damage at skill 0, 100% at skill 100** `[UNVERIFIED for ranged weapons specifically: the
GECK wiki documents these values for the melee formula and marks the gun formula incomplete]`.

**Damage vs. condition** (at skill 100): Damage = Base x (Min + Condition x (1 - Min)), with Min = 0.66 for
single-shot guns, 0.54 for automatics, 0.5 for melee.

What this feels like:

- There are **no true iron sights**: "aiming" is a zoom that tightens the cone. Shots still deviate randomly
  inside it, so a centred crosshair can miss at low skill. Players read this as the gun lying to them.
- Low skill is punished twice (wide cone *and* half damage), so early real-time combat is weak and V.A.T.S.
  feels compulsory. High skill makes the gun both accurate and twice as strong, so late combat is trivial.
  The skill curve widens the gap instead of smoothing it.
- No cover system, minimal hit reactions outside crippling, enemies that mostly charge or strafe in place,
  floaty movement and limited recoil. Reviewers at the time singled out AI and animation; Bethesda's own
  staff later called the shooting one of the game's weaker elements.
- Weapons can jam on reload at low condition, a characterful touch that players mostly experience as noise.

Weapon class identity is thin: Small Guns ammunition and weapons are everywhere, Energy Weapons arrive
mid-game, and Big Guns are heavy, ammo-hungry and wear out fastest. Small Guns is therefore the default
choice for almost everyone.

## 6. Damage model, Damage Resistance and the 85% cap

- **Model:** Final damage = (weapon damage after skill and condition + critical damage if a crit) x sneak
  multiplier x headshot multiplier x difficulty multiplier, then reduced by the target's DR percentage.
- **DR is purely proportional.** There is no damage threshold: every bullet does something to every target.
  Armor never makes a weapon useless, only less efficient. (New Vegas reintroduced a threshold to restore
  weapon/armor matchups.)
- **Cap: 85%** from all sources combined.
- Armor DR falls as the armor's condition falls `[UNVERIFIED: exact curve]`.

| DR source | Value |
|---|---|
| Best power armor with helmet (T-51b or Hellfire) | 60 |
| Toughness | +10 |
| Cyborg | +10 |
| Superior Defender (Point Lookout) | +10 standing still |
| Barkskin (Oasis quest reward) | +5 |
| Survival Expert (quest reward) | up to +6 |
| Med-X (chem) | +25 temporary |
| Nerd Rage! | +50 below 20% health |

Permanent totals of 80-94% are reachable, so the cap is hit by endgame characters with no chems at all, and
Med-X alone lifts mid-game armor to the cap.

Why the cap matters for balance: at 85% DR the player takes 15% damage; inside V.A.T.S. that becomes 1.5%.
Against that, designers have only two levers: enemies with enormous health pools or attacks that ignore DR.
Broken Steel and Point Lookout used both. An overlord's tri-beam laser and Point Lookout's swamp-dwellers are
commonly reported to carry hidden bonus damage that bypasses DR `[UNVERIFIED]`, which players experienced as
arbitrary because nothing in the interface explains it.

## 7. Weapon condition and repair

| Rule | Value |
|---|---|
| Wear per shot | A percentage of base damage: Small Guns 3%, Energy 4%, Melee/Unarmed 5%, Big Guns 6% |
| Example | Plasma rifle (45 dmg, 900 item HP) loses 1.8 per shot: 500 shots from new to broken |
| Example | Hunting rifle (500 item HP): ~667 shots |
| Field repair | Requires a second item of the same type (or a listed compatible one), which is consumed |
| Result | 5% + better item's condition + 5% of the worse item's + 0.15% x Repair, capped by skill |
| Max condition by skill | 40% + 0.6% x Repair (46% at 10; 70% at 50; 100% at 100) |
| Merchant repair | Costs caps; capped by that merchant's own Repair skill (most well under 100) |
| Unique weapons | Repaired with the common variant; a few (e.g. the best power armor) need NPC repair |

Assessment:

- **Good:** it creates a use for duplicate loot, gives Repair a real job, and makes the first ten hours tense.
  Looted gear arrives in poor condition, which is an elegant brake on early power.
- **Bad:** it is a hidden tax that most players pay by hoarding. Every looted rifle is either food for your
  rifle or dead weight. Rare weapons with no common twin become too precious to use.
- **Convergence again:** Repair is so valuable (it raises damage, DR and sale value at once) that almost
  everyone maxes it, at which point the system stops generating decisions and becomes a menu chore.
- Fallout 4 removed condition entirely; New Vegas kept it but added repair kits and weapon-family repair
  perks. Neither kept Fallout 3's version unchanged.

## 8. Enemy scaling and the Broken Steel bullet sponges

How scaling works:

- Spawn points draw from **leveled lists**: at each player-level band a tougher variant becomes eligible
  (raider to better-armed raider; super mutant to brute to master).
- Lists have **few tiers** compared with Oblivion, and equipment is mostly not leveled, so the world does not
  re-gear around the player the way Oblivion's bandits did.
- **Encounter zones** have a minimum level and **lock at the player's level on first entry**. A place visited
  at level 3 stays easy forever; some areas (deathclaw territory, certain late-game buildings) have high
  minimums and are dangerous early. This gives a mild sense of geography of danger, more than Oblivion had and
  much less than New Vegas.
- A handful of fixed encounters (the five Behemoths, named enemies) are hand-placed.

Reference health values:

| Enemy | HP | Notes | Confidence |
|---|---|---|---|
| Super mutant / brute / master | ~100 / ~250 / ~360 | Base-game tiers | `[UNVERIFIED]` |
| Glowing one | ~240 | Toughest base-game feral ghoul | `[UNVERIFIED]` |
| Deathclaw | ~500 | Toughest common base-game creature | `[UNVERIFIED]` |
| Super mutant behemoth | ~2,000 | Five in the world, set-piece bosses | `[UNVERIFIED]` |
| **Feral ghoul reaver** | **1,100** | Level 12 creature, 100 melee damage, heals from radiation, 0% DR | Verified |
| **Super mutant overlord** | **1,250** | Gatling laser, tri-beam laser, missile launcher or sledge variants | Verified |
| **Albino radscorpion** | **1,500** | 100 melee + 25 poison/s for 4 s; regenerates in sunlight; never flees | Verified |
| Player at level 30, EN 9 | 570 | For comparison | Computed |

The Broken Steel problem:

- Raising the cap to 30 required new top tiers, and they were made by **multiplying health by 3-5x** rather
  than by adding behaviours. A reaver has more than four times the health of the glowing one it replaces and
  appears in packs in the same metro tunnels.
- These variants enter ordinary leveled lists at high player levels `[UNVERIFIED: exact threshold; commonly
  reported as the low-to-mid 20s]`, so installing the add-on changes the whole base-game map: random
  scorpion encounters become multi-minute ammunition sinks.
- They have 0% DR and no new weaknesses, so there is no smart answer, only more bullets. The optimal responses
  are degenerate: a specific dart gun that instantly cripples legs, sneak-critical stacking, or V.A.T.S. with
  Grim Reaper's Sprint.
- They are a direct result of the 85% DR cap and V.A.T.S. damage reduction: with the player almost immune,
  the only remaining knob was enemy time-to-kill.

Lesson: Fallout 3's scaling is acceptable through level ~15 and breaks beyond it, because player power grows
multiplicatively (skill x condition x crits x perks) while enemy design only had one additive dial.

## 9. Karma

| Band | Range | Consequences |
|---|---|---|
| Very Good | +750 to +1000 | Talon Company hit squads; Fawkes and Star Paladin Cross will join; gifts from Megaton residents |
| Good | +250 to +749 | As above |
| Neutral | -249 to +249 | No hit squads; Butch and Sergeant RL-3 will join |
| Evil | -250 to -749 | Regulator hit squads; Jericho and Clover will join |
| Very Evil | -750 to -1000 | As above |

| Action | Karma |
|---|---|
| Steal from a non-evil owner | -5 per item |
| Kill a non-evil character | -100 |
| Disarm the Megaton bomb for free | +200 |
| Detonate the Megaton bomb | -1000 |
| Final quest: self-sacrifice / poison the water | +600 / -1000 |
| Give purified water to beggars; donate to a church | Small repeatable gains |

Other effects: a karma-and-level title (30 levels x 3 alignments), Three Dog's opening description of the
player, some dialogue reactions, certain ending slides, and access to the slaver town versus the good hubs.

Strengths: immediate feedback, a clear moral identity, and hit squads that make alignment felt in the open
world.

Weaknesses:

- **One global number.** Nobody remembers *what* you did, only your running total. There are no faction
  reputations. A character can annihilate a town and buy back sainthood with bottled water.
- **Omniscient.** Stealing unobserved still costs karma, so karma is a cosmic ledger rather than reputation.
- **Binary writing.** Most quest choices are saint versus cartoon villain, with a paid neutral option.
  The Megaton bomb is the emblem: memorable spectacle, but the evil choice has little motive beyond caps and
  a penthouse.
- **Trivially resettable**, even before Broken Steel's three karma-reset perks.
- Evil play is under-served: fewer quests, fewer rewards, weaker companions.
- Praised exceptions exist where neither side is clean (the Tenpenny Tower ghoul dispute, the android in
  Rivet City, the tree-man at Oasis), and these are the quests critics still cite.

## 10. Dialogue and speech checks

- Dialogue is a list of full-sentence options with a silent protagonist. Compared with Fallout 1/2, fewer
  options are gated by Intelligence or skills; there is no low-Intelligence dialogue path.
- Options tagged with a stat, skill or perk exist, but most are flavour. Some perks (Lady Killer / Black
  Widow, Child at Heart, Toughness) add unique lines.
- **Speech checks show a percentage** and roll once:

  Chance = Charisma multiplier x Speech / check difficulty

  | Input | Value |
  |---|---|
  | Charisma multiplier | 100% at CH 1 rising non-linearly to 206% at CH 10 (133% at CH 5) |
  | Typical check difficulty | ~111-215 early; few exceed ~170; hardest ~457 |
  | Example: CH 5, Speech 50 | ~60%, ~45%, ~31% against difficulty 111, 147, 215 |
  | Weapon drawn | ~10% harder |
  | Retry | Not in the same conversation |

- **Save-scumming.** A visible percentage, a single attempt and a quicksave key make reloading the dominant
  strategy; fallout.wiki's own page recommends it. A 31% check is not a risk, it is roughly three reloads.
  That converts the Speech skill from a build choice into a patience tax and erodes the value of Charisma.
- New Vegas replaced this with **deterministic thresholds** (the option shows the required skill and either
  succeeds or fails), and extended checks to many other skills. This is close to universal consensus as the
  better design.

## 11. Lockpicking and hacking

| Tier | Lockpick required | Science required | XP |
|---|---|---|---|
| Very Easy | 0 | 0 `[DISPUTED: one fallout.wiki table lists 15]` | 20 |
| Easy | 25 | 25 | 30 |
| Average | 50 | 50 | 40 |
| Hard | 75 | 75 | 50 |
| Very Hard | 100 | 100 | 60 |

**Lockpicking:** rotate a bobby pin to find a hidden sweet spot, then turn the lock with a screwdriver; the pin
shakes and breaks if held under tension in the wrong position. Harder locks have narrower sweet spots and
break pins faster. A "force lock" option skips the game on a skill-based chance; failure jams the lock
permanently (unless the Infiltrator perk is held). Backing out and re-entering re-randomises the position but
saves the pin.

**Hacking:** a screen of memory-dump characters hides candidate passwords of equal length (4-5 letters at Very
Easy up to 13-15 at Very Hard). Four guesses; each wrong guess reports how many letters are in the correct
position (a word-based code-breaking game). Selecting matched bracket pairs removes a dud word or restores
guesses. Failing all four locks the terminal permanently. Higher Science changes the candidate pool. The
well-known exploit is to quit after three guesses and re-enter with a fresh puzzle `[UNVERIFIED in this
session; near-universal community practice]`, which removes the fail state.

Assessment:

- **Hard gating by skill tier** is the important decision: unlike Oblivion, a dextrous player cannot open a
  Very Hard lock with skill 20. This protects the RPG layer.
- But the tiers are coarse: skill values of 26-49 are functionally identical to 25. Together with flat point
  costs this encourages moving skills in 25-point jumps.
- Both minigames are good the first twenty times and tedious by the two-hundredth; there are hundreds of locks
  and terminals. Bobby pins are so common they are not a resource.
- Hacking is the better design (deduction, fictional flavour, terminals that pay off in story text). The
  lockpick game survived unchanged through Skyrim and Fallout 4.
- Because both give XP and gate loot and lore, both skills end up maxed on almost every character.

## 12. Economy and abundance

Price formulas:

- Sell price = value x (0.45 + 0.45 x Barter/100): 45% at Barter 0, 90% at 100.
- Buy price = value x (1.55 - 0.45 x Barter/100): 155% at Barter 0, 110% at 100.
- So the buy/sell spread shrinks from 3.4:1 to 1.2:1. Master Trader (Barter 60, CH 6) takes a further 25% off
  purchases; several quests give standing discounts of 10-30%.
- Item value scales with condition, so Repair is also the best money skill.

Why it breaks:

- **Sources vastly exceed sinks.** Every enemy drops a sellable weapon and armor; every building holds ammo
  boxes, first-aid kits and chems. Meaningful sinks are few: a player home and its themes (a few thousand
  caps), two companion purchases (1,000-2,000 caps), schematics, and repairs.
- **Stimpaks** restore 30 HP at base, more with Medicine `[UNVERIFIED: exact scaling]`, weigh nothing, apply
  instantly from a paused menu and are found constantly. Players commonly finish with 100+. Because healing
  happens while paused, health is effectively *current HP + (stimpaks x heal)*, and death mostly comes from
  burst damage.
- **Ammunition is weightless**, so there is no reason not to carry thousands of rounds of everything.
- **Food and water are irrelevant** except as minor heals that add radiation; with stimpaks abundant, the
  radiation-for-health trade is never worth making after the first few hours.
- **Merchant cash** (a few hundred caps each, restocking every few days `[UNVERIFIED: exact figures]`) is the
  one real limiter, and it limits *convenience*, not wealth: the player ends up with more valuables than the
  world can buy.
- Unique weapons are found, not bought; shops rarely sell anything you want. Caps therefore have nothing to
  aspire to.

Net effect: the scavenging fantasy holds for roughly the first 8-10 hours. After that the post-apocalypse is a
place of plenty, and the survival tone exists only in the art.

## 13. World design: the Capital Wasteland

| Measure | Figure | Confidence |
|---|---|---|
| Playable exterior | roughly 50 x 50 cells, a little over 1.8 miles (~2.9 km) across, so ~3.3 sq mi | UESP GECK wiki, via search summary |
| Popularly quoted size | "16 square miles" | `[DISPUTED]` (Giant Bomb and many articles; inconsistent with the cell count) |
| Map-marker locations (base game) | usually quoted as ~160; one user-quoted figure gives 225 including add-ons | `[DISPUTED]` |
| fallout.wiki location index | 461 "marked" and 359 "unmarked" entries (counts sub-locations and interiors) | Verified as that page's count |
| Settlements listed | 22 | fallout.wiki |

Whatever the exact counts, the important ratio is clear: **well over a hundred named places in about three
square miles**, i.e. something new roughly every one to two minutes of walking in any direction.

How the map is organised:

- **Start in the south-centre** (the vault exit and the first town are a two-minute walk apart). The exit
  from the vault is staged as a blinding reveal over the whole landscape with landmarks visible to the
  horizon; it is the series' most imitated moment.
- **Regions by difficulty:** gentle south-west; raider and mutant belts in the middle; the dense ruined city
  in the south-east; deathclaws and high-level zones to the far north and west.
- **Landmark navigation:** a tall monument, a tower block, a beached carrier-city and a giant satellite array
  are visible from far away and pull the player across the map without quest markers.
- **Compass ticks** show undiscovered locations nearby, which converts walking into a breadcrumb chain.
- **Settlements are small.** The largest hubs have a few dozen named NPCs. Critics argue they do not form a
  believable society (no visible food production, 200 years on and nobody has swept the floor). As a *game*
  space, though, each is distinctive: a town around an unexploded bomb, a city in a ship, a tower of rich
  recluses, a cave town of children, a slaver camp, a two-house "republic".
- **Unmarked locations** are numerous: collapsed overpasses with sniper nests, wrecked convoys, drainage
  chambers, shacks with a skeleton and a note. They never appear on the map and reward off-road walking.
- **Random encounters** occupy fixed trigger points with a pool of events, so repeat trips differ.

### Environmental storytelling — the biggest strength

Almost every location answers "what happened here?" with staged props rather than dialogue: skeleton
tableaux, terminal logs, holotapes, traps, graffiti, and above all the **vaults**, each a self-contained
horror short story about a social experiment (a vault of clones, a hallucinogen vault, a vault of white
noise, a simulated suburb run by a sadist). Players reconstruct the story themselves, at their own pace, with
no fail state.

Why it works so well here:

- It suits first-person real-time play in a way dialogue trees do not: the story is *in the space you are
  already searching for loot*, so narrative and looting reinforce each other.
- It is cheap relative to voiced, branching quests, so there can be a hundred instances of it.
- Post-apocalypse is inherently about backstory; ruins are literal evidence.
- It is compatible with any character build and any play order.

Even harsh critics of the writing (Shamus Young's long plot critique, NMA-style reviewers) generally concede
the exploration. Reviewers describe the world as feeling vast despite a limited asset palette, and as having
a haunting quality the other entries lack.

Limits: the storytelling is almost entirely *retrospective*. It tells what happened before the bombs or a
decade ago, rarely what the living are doing now, and it sits beside a main plot that many find incoherent.
The world is a superb museum and a weak society.

### Downtown D.C. and the metro maze

- The city centre is not continuous. Collapsed buildings form impassable rubble walls that divide it into
  separate surface districts, each a different loaded worldspace, joined by **metro stations and tunnels**.
- The practical reason is technical (console memory and performance in dense geometry). The cost is
  navigational: the world map shows a destination 200 metres away that requires three tunnel interiors and
  four loading screens to reach, tunnel entrances are not labelled with where they lead, the local map is
  nearly useless underground, and the tunnels share one tile set, so they blur together.
- Tunnels are also the game's most repetitive combat: feral ghouls and raiders in corridors.
- Pagliarulo has said the team first planned a metro that tracked the real surface network and cut it back on
  finding that miles of tunnel were dull: realism "sometimes isn't fun". The shipped version is thus already
  the compromise. Similarly, the presidential mansion is a crater because no quest needed it built.
- Dissent: some players and at least one retrospective (PCGamesN) defend the metro as Bethesda's most
  ambitious connected dungeon, navigable via in-world signage, and point out that emerging from a tunnel into
  the monument-lined central park is the game's second great reveal.
- The complaint is nonetheless one of the most consistent in Fallout 3 criticism, and Fallout 4's Boston was
  built as a continuous walkable city, which reads as Bethesda's own verdict.

## 14. Quests

| Category | Count | Notes |
|---|---|---|
| Main quests | 15 | 4 tutorial, 4 act one, 7 act two; main line is short (roughly 10-15 hours) |
| Named side quests | 17 | Long, multi-stage, multi-solution |
| Unmarked quests | ~23 | No journal entry |
| Repeatable quests | ~16 | Mostly turn-in loops (scrap metal, tech, fingers/ears, pre-war books) |
| Add-on quests | 35 across five add-ons | |

(fallout.wiki states "59 base-game quests" in one place while its own lists sum differently; treat totals as
`[DISPUTED]`.)

Design character:

- **Few but elaborate.** With only 17 full side quests, each got substantial bespoke content: unique
  locations, several endings, often a skill/speech bypass. Typical structure offers a good, an evil and a
  mercenary resolution.
- The standout structural design is the **survival-guide quest**: nine research tasks in three chapters, each
  with a basic and a bonus objective, each answerable truthfully, sarcastically or with skill-based input. The
  reward perk and the quality of the in-fiction book scale with how thoroughly it was done. It is also a
  disguised extended tutorial covering mines, radiation, crippling, stealth and the major enemy types.
- Other frequently praised quests are praised for *consequence and ambiguity* (a ghoul/human housing dispute
  whose "peaceful" solution ends badly; an escaped android whose owner and protectors both have a case) or for
  *tone* (two costumed lunatics fighting over a town; a fire-ant infestation).
- **Weaknesses:** the main quest is linear, hands key decisions to NPCs, hard-ended the game at release, and
  its final choice ignored radiation-immune companions (patched narratively by Broken Steel, clumsily by most
  accounts). Tim Cain remarked that the endings were not built enough around player choices. Many map
  locations have no quest at all, which critics call "raider dungeons" and fans call freedom.
- The **main quest can be sequence-broken**: walking into the right locations early skips several steps and
  the game copes. This robustness is under-appreciated.
- Quest density is the starkest contrast with New Vegas, which has several times as many marked side quests
  tied to faction reputation, and a much sparser, less surprising landscape.

## 15. Companions

| Companion | Karma needed | Type | HP (level-scaled) | Notes |
|---|---|---|---|---|
| Dogmeat | Any | Dog | 500, later far higher after patches/add-ons | Found in a scrapyard; can fetch items; does not count against the limit |
| Charon | Any | Ghoul, shotgun | 240-365 | Buy his contract (2,000 caps; 1,000 with Barter 50) or do a murder for his owner |
| Jericho | Evil | Ex-raider, assault rifle | 235-360 | 1,000 caps |
| Clover | Evil | Slave bodyguard | 240-385 | Bought |
| Butch | Neutral | Vault bully, pistol | 190-335 | Requires a specific late side quest; has limited ammo |
| Sergeant RL-3 | Neutral | Robot, plasma + flamer | 350 scaling up | 1,000 caps (500 with Barter 70); self-repairs |
| Star Paladin Cross | Good | Power-armored soldier | 445-570 | Free |
| Fawkes | Good | Super mutant, gatling laser | 500 scaling very high | Only after a late main-quest step |

- Limit: **one humanoid/robot companion plus the dog**.
- Companions can die permanently (no "essential" flag). In the base game they are fragile at high level;
  later patches/add-ons inflated the health of the dog, the robot and the mutant enormously (values up to
  10,000-15,000 are listed), which swung them from liabilities to immortal tanks.
- Controls are a short dialogue menu: follow/wait, distance, melee/ranged, trade inventory. No companion
  quests, no approval system, very little banter, no perks granted.
- They break stealth, block doorways and wander into the player's fire. Many players leave them at home.
- Recruitment is gated almost solely by karma band, so there is no relationship arc.
- This is the least developed system in the game and the one that changed most afterwards: New Vegas added a
  command wheel, companion perks and personal quests; Fallout 4 added approval and unkillable companions.

## 16. Radio

- **Diegetic radio** plays through the wrist device during normal play: one DJ-led station with ~20 licensed
  1940s-50s songs, one propaganda station of marches and presidential monologues, and local or quest signals
  (distress beacons that lead to unmarked locations).
- **Reactivity:** the DJ introduces news items by describing the player according to current karma, then
  reports on completed quests with variants depending on how they were resolved (for instance different
  reports on the fate of the bomb town or the slaver camp). He credits or condemns "that kid from the vault".
- **Mechanical hook:** the station's signal is poor outside the city until an early quest replaces its relay
  dish, after which it covers the whole map. This gives the player a mechanical reason to help the station
  and makes the radio feel like infrastructure. The DJ can be killed, replaced by a flat-voiced technician.
- **Why it matters:** it is the cheapest, widest-reaching reactivity in the game. A handful of recorded
  variants make the entire world seem to notice the player, while the music does most of the work of
  establishing the series' ironic retro tone during otherwise silent walking.
- **Weaknesses:** 20 songs loop within an hour or two; news lines repeat heavily; a known bug stops
  player-specific commentary at level 20 until karma changes.

## 17. The childhood tutorial

The opening runs the player through one character's first 19 years in a sealed shelter, with each scene
teaching one system while performing one character-creation step:

| Age | Fiction | System taught / choice made |
|---|---|---|
| Birth | Delivery room | Name, sex, appearance (framed as a projection of the adult face) |
| 1 | Playpen and a picture book | Movement, interaction; **SPECIAL allocation** via the book |
| 10 | Birthday party | Dialogue, the wrist computer, first weapon (an air rifle), V.A.T.S. on a pest |
| 16 | Aptitude exam | **Tag skills** via a joke multiple-choice test (results can be overridden) |
| 19 | Escape | Combat, sneaking, lockpicking, hacking, first speech checks and karma choices |
| Exit door | - | Prompt to **revise name, appearance, SPECIAL and tags** before leaving |

Strengths: character creation is integrated with fiction; it establishes the father whose disappearance drives
the plot; the claustrophobic interior makes the exit reveal land; the final "revise everything" prompt is an
excellent mercy; a save at the exit door lets repeat players skip it.

Weaknesses: it is 30-60 minutes long and unskippable; it asks for build decisions before the player has seen
the systems they affect (rescued only by the revise prompt); and it imposes a fixed age, upbringing and
father, which cuts against the "be anyone" freedom of the earlier games. It is charming once and a chore on
every replay, the standard complaint about Bethesda openings.

## 18. Difficulty

| Setting | Damage dealt by player | Damage taken | XP |
|---|---|---|---|
| Very Easy | 200% | 50% | 50% |
| Easy | 150% | 75% | 75% |
| Normal | 100% | 100% | 100% |
| Hard | 75% | 150% | 125% |
| Very Hard | 50% | 200% | 150% |

- Difficulty is purely two multipliers plus an XP modifier. No AI, spawn, loot or economy changes.
- Changeable at any time from the menu, including mid-fight.
- **Higher difficulty gives more XP**, so Very Hard levels the character 50% faster, which accelerates the
  over-levelling that makes the game easy. It also hits the cap sooner.
- Very Hard quarters the player's effective damage-to-health ratio and turns every enemy into a sponge,
  compounding the Broken Steel problem. It makes fights longer, not smarter.
- Difficulty curve on Normal: **front-loaded**. The first hours (poor guns, no caps, low skills) are the
  hardest; from about level 10 the game eases steadily, and by level 20 only DR-ignoring or 1,000+ HP enemies
  threaten. There is no hardcore/survival mode; New Vegas added one in direct response.

## 19. Bugs and stability

- Launch reviews on all platforms noted crashes, freezes, physics glitches and bugs that could block quest
  progression.
- **PS3** was the weakest version: lower frame rate, longer freezes, add-ons delivered months late (all five
  arrived by late 2009), and the Game of the Year edition drew many reports of worse stability with add-ons
  installed, plus a save-compatibility problem between regional editions.
- **Broken Steel on PC** initially shipped broken and had to be re-released; several add-ons launched with
  corrupted files or crash bugs `[UNVERIFIED in this session]`.
- **PC long-term:** the game was never officially supported on Windows 7 or later. Crashes on new game start
  on multi-core processors (fixed by an .ini thread-limit edit), the bundled Games for Windows Live client
  (removed in a 2021 update `[UNVERIFIED date]`), autosave-related save corruption, and reliance on
  community unofficial patches are the standard experience.
- Engine-typical oddities: NPCs falling through floors or dying off-screen, companions vanishing, broken
  scripted scenes, physics objects launching, stuck quest stages. The PC console lets players self-repair
  quests; console players had no such recourse.
- Regional content edits for classification (a real-world drug name replaced in all versions after the
  Australian board objected; the bomb-detonation option removed in Japan; gore reduced in Germany) are not
  bugs but did fragment versions.
- Reception absorbed all this: scores stayed above 90. The lesson the industry drew, unfortunately, was that
  open-world scope buys forgiveness for instability.

## 20. Balance assessment

| Area | Verdict | Why |
|---|---|---|
| Early game (levels 1-8) | Good | Scarce ammo, poor-condition gear, real danger; every system generates decisions |
| Mid game (9-15) | Fair | Economy overflows, key skills reach thresholds, perks stack |
| Late base game (16-20) | Poor | Skills converge, DR near cap, Grim Reaper's Sprint arrives, XP stops at 20 |
| Broken Steel (21-30) | Poor | Player becomes all-10s/all-100s; enemies answered with 3-5x health |
| V.A.T.S. | Fun but overpowered | 90% damage reduction + crit bonus + AP-refund perk |
| Real-time shooting | Weak | Stat-driven cone, half damage at low skill, thin AI and feedback |
| Skill system | Front-loaded | Flat costs, generous points, books and bobbleheads remove scarcity |
| Perks | Too many, too filler | One per level; a few build-defining, a few game-breaking, many +skill fillers |
| DR model | Too simple | Percentage only, 85% cap easy to reach, no threshold |
| Condition/repair | Good early, chore late | Elegant brake on early power; becomes inventory busywork |
| Level scaling | Tolerable | Softer than Oblivion; zone locking helps; top tiers are sponges |
| Speech | Flawed | Visible percentage + single roll = reload |
| Lock/hack gating | Sound idea, coarse | 25-point tiers; minigames overused |
| Karma | Shallow | Single global ledger, resettable |
| Economy | Broken after ~10 hours | Sources greatly exceed sinks; weightless ammo and instant healing |
| World / exploration | Excellent | Density, landmarks, environmental stories, vaults |
| Downtown navigation | Poor | Fragmented surface, look-alike tunnels |
| Side quests | Good, too few | Multi-solution, memorable; only 17 |
| Main quest | Weak | Linear, railroaded ending |
| Companions | Underdeveloped | Karma-gated followers with no depth |
| Stability | Poor | Crashes and quest-breakers on every platform |

The through-line: **Fallout 3 is generous everywhere at once.** Generous skill points, a perk every level,
generous loot, generous healing, generous damage reduction. Each is pleasant in isolation; together they
eliminate scarcity and therefore choice, and the only response left to the designers was to inflate enemy
health. The systems are a ladder the player finishes climbing with a third of the game still to go. What
keeps people playing after that is not the systems at all but the world.

## 21. What Fallout 3 established as the 3D-Fallout formula

Every later first-person Fallout (New Vegas, 4, 76) keeps the following, even where it revises the numbers:

1. **A continuous first-person open world** entered through a staged "step out of the shelter" reveal, with
   landmark-led navigation, compass ticks for nearby locations and fast travel to discovered markers.
2. **Exploration as the primary content**, delivered through dense hand-built locations and environmental
   storytelling (skeleton scenes, terminals, audio logs), with experimental shelters as the signature dungeon
   type.
3. **Real-time gunplay with V.A.T.S. on top**: AP-funded, body-part-targeted, percentage-displayed attacks
   with cinematic kill cameras and a damage-reduction bonus.
4. **The wrist-computer interface** unifying stats, inventory, map, quests and radio in one diegetic menu,
   with instant paused healing from it.
5. **Loot everything**: every container searchable, every enemy droppable, junk with weight, ammo without.
6. **Diegetic radio** with period music and a DJ who reports the player's deeds.
7. **Lockpicking and terminal-hacking minigames** gated by tiers, with terminals doubling as lore delivery.
8. **A perk-centred progression** with frequent picks, plus collectible permanent stat boosts (bobbleheads,
   skill books/magazines) hidden in the world as exploration rewards.
9. **Level-banded enemy variants** drawn from leveled lists, with zone minimums for a rough danger geography.
10. **A voiced, zoom-in dialogue system** with tagged skill/stat options, and a small roster of recruitable
    followers.
11. **Weapon variety through found unique variants** of common guns rather than through shops.
12. **Tone by juxtaposition**: cheerful mid-century optimism (music, mascots, advertising) laid over ruin and
    gore, delivered mostly by art, audio and props rather than by dialogue.
13. **A personal-search main plot** (find a family member) that the player is free to ignore for dozens of
    hours.
14. **Post-launch add-ons** as self-contained new worldspaces with their own gear and a raised cap.

What later entries *changed* is equally instructive, since each change points at a Fallout 3 flaw: thresholds
instead of percentage speech rolls and faction reputation beside karma (New Vegas); damage thresholds and
ammo types (New Vegas); a perk every two levels and the return of traits (New Vegas); a survival mode (New
Vegas, Fallout 4); iron sights and rebuilt shooting (New Vegas, then Fallout 4); slow-motion rather than paused
V.A.T.S. with weaker damage reduction (Fallout 4); removal of weapon condition and skills (Fallout 4); a
walkable city without tunnel mazes (Fallout 4); companions with quests, perks and approval (New Vegas,
Fallout 4); and no level cap but slower growth (Fallout 4).

## Design Takeaways

**Learn from**

- **Density over area.** About three square miles with a discovery every one to two minutes beats a large
  empty map. Budget content per minute of walking, not per square kilometre.
- **Stage the first vista.** A confined, low-ceilinged opening followed by one wide reveal with three or four
  visible landmarks sets up the whole exploration loop in five seconds.
- **Put the story where the loot is.** Environmental vignettes are the best cost-to-value narrative in the
  genre: build-agnostic, order-agnostic, unfailable. Give every location a one-line answer to "what happened
  here?" before building it.
- **Self-contained "experiment" dungeons** with a twist are endlessly reusable as a format. We need our own
  equivalent premise, not shelters-with-experiments.
- **A cheap global reactivity channel** (a broadcaster, a newspaper, town criers, graffiti that updates) makes
  the world appear to notice the player for the price of a few variant lines. Tie it to a mechanical unlock.
- **A tactical pause as an accessibility bridge.** A resource-limited targeting mode lets non-shooter players
  enjoy real-time combat and gives stats a visible job. Keep the idea; rebalance the numbers.
- **Hard skill gates on minigames**, so character build matters more than thumb skill.
- **Poor-condition loot as an early-game brake**, and duplicates as repair fuel, make junk meaningful.
- **Few, deep, multi-solution side quests** are remembered longer than many shallow ones. A long multi-chapter
  "research" quest can secretly be the extended tutorial.
- **Let players revise build choices at the end of the tutorial**, and offer a skip for replays.
- **A robust main quest** that tolerates out-of-order discovery.

**Avoid**

- **Do not hand out a perk every level plus enough skill points to max everything.** Decide the end-state
  first: a finished character should master perhaps a third of the skill list. Use escalating costs or a hard
  point budget, and make collectible boosts scarce or exclusive.
- **No "erase the build" capstones** (all stats to near-max; full resource refund on kill; alignment reset).
  Capstones should deepen a specialisation, not delete trade-offs.
- **Do not make the tactical mode a 90% damage shield.** If pausing is safe, real-time play becomes the
  penalty phase. Prefer slow-motion or a modest defensive bonus, and give the resource a real refill cost.
- **Never answer player power with health multipliers alone.** High-tier enemies need new behaviours, weak
  points and counters. If our armor model can reach near-immunity, fix the model (thresholds, armor
  penetration, damage types) rather than adding hidden unblockable damage.
- **Do not show a percentage on a one-shot dialogue roll** in a game with free saving. Use thresholds, partial
  successes, or let failure open a different path rather than a dead end.
- **Do not track morality as one omniscient global number.** Use witnessed actions and per-community
  reputation so consequences are local, legible and not purchasable.
- **Balance sources against sinks for the whole game length.** Give ammunition and healing weight, cost or
  time; make healing non-instant; provide late-game money sinks worth wanting. Decide deliberately whether
  scarcity is a 10-hour phase or the whole game.
- **Do not make higher difficulty award more XP**, and do not let difficulty be only two multipliers. Change
  scarcity, AI and healing rules instead.
- **Do not fragment a city into loading-screen pockets joined by identical tunnels.** If technology forces
  partitioning, make connectors short, visually distinct, signposted with destinations, and shown on the map.
- **Do not let the level cap arrive before the content ends.** Either pace XP to the content or keep
  post-cap rewards flowing.
- **Do not ship followers as karma-gated gun turrets.** Either invest in them (commands, quests, reactions,
  mechanical benefits) or leave them out.
- **Do not hard-end the game after the finale**, and do not write a final choice that ignores the abilities of
  characters standing in the room.
- **An unskippable hour-long opening** is a replay tax. Keep the integrated character creation; make it brief
  or bypassable.
- **Budget for stability.** Quest-blocking bugs with no in-game recovery are a design failure, not just a QA
  one: build fail-safes (alternate triggers, non-essential NPC redundancy) into quest logic.

## Sources

Wikis and data references

- https://fallout.wiki/wiki/Fallout_3_V.A.T.S. — V.A.T.S. game settings (damage multiplier, crit bonus, max chance, wear, spread)
- https://fallout.wiki/wiki/Action_Points — AP formula
- https://fallout.wiki/wiki/Fallout_3_combat — damage/critical formulas, per-weapon AP examples
- https://fallout.wiki/wiki/Fallout_3_skills — skill list, formulas, books, bobbleheads
- https://fallout.wiki/wiki/Fallout_3_SPECIAL — SPECIAL and derived statistics
- https://fallout.wiki/wiki/Fallout_3_perks — perk levels, requirements, effects, counts
- https://fallout.wiki/wiki/Level_(Fallout_3) — XP formula and totals
- https://fallout.wiki/wiki/Hit_Points_(Fallout_3) — HP formula
- https://fallout.wiki/wiki/Damage_Resistance_(Fallout_3) — 85% cap and DR sources
- https://fallout.wiki/wiki/Weapon_Spread_(Fallout_3) — spread formula
- https://fallout.wiki/wiki/Weapon_condition — condition-to-damage formula, wear rates
- https://fallout.wiki/wiki/Repair_(Fallout_3) — repair formulas
- https://fallout.wiki/wiki/Hunting_Rifle_(Fallout_3) — sample weapon statistics
- https://fallout.wiki/wiki/Difficulty/Fallout_3 — difficulty multipliers
- https://fallout.wiki/wiki/Karma_(Fallout_3) — karma bands, values, consequences
- https://fallout.wiki/wiki/Speech_(Fallout_3) — speech-check formula and examples
- https://fallout.wiki/wiki/Barter_(Fallout_3) — price formulas
- https://fallout.wiki/wiki/Hacking_(Fallout_3) — hacking rules
- https://fallout.wiki/wiki/Lock_(Fallout_3) — lockpicking rules
- https://fallout.wiki/wiki/Albino_radscorpion — creature statistics
- https://fallout.wiki/wiki/Super_mutant_overlord — creature statistics
- https://fallout.wiki/wiki/Feral_Ghoul_Reaver_(Fallout_3) — creature statistics
- https://fallout.wiki/wiki/Fallout_3_quests — quest lists
- https://fallout.wiki/wiki/Fallout_3_locations — location counts
- https://fallout.wiki/wiki/Fallout_3_companions — companion table
- https://fallout.wiki/wiki/Galaxy_News_Radio_(radio) — radio behaviour
- https://geck.uesp.net/wiki/Encounter_Zone and https://geck.uesp.net/wiki/Bethsoft_Tutorial_NPCpopulation — encounter-zone locking, leveled lists (via search summaries; direct fetch refused)
- https://geck.uesp.net/wiki/Gun_Spread_Formula and https://geck.uesp.net/wiki/FDamageSkillBase — spread and skill-damage settings (via search summaries)
- https://geck.uesp.net/wiki/Units — cell-based map size (via search summary)
- https://en.wikipedia.org/wiki/Fallout_3 — development, release, scores, sales, awards, criticisms, regional edits
- https://giantbomb.com/wiki/Locations/The_Capital_Wasteland — "16 square miles" figure (via search summary)

Developer statements

- http://www.gamebanshee.com/k6r8r — GameBanshee, 15 Oct 2008, relaying Emil Pagliarulo's forum comments on V.A.T.S.
- https://www.pcgamer.com/games/fallout/the-fallout-vats-system-was-inspired-by-burnouts-crash-mode-of-all-things-or-as-todd-howard-puts-it-imagine-the-car-parts-are-like-eyeballs-and-guts — Todd Howard on the Burnout inspiration (headline only retrievable)
- https://www.gamesradar.com/games/fallout/fallout-3s-vats-system-helped-compensate-for-bethesdas-lack-of-shooting-chops-we-were-never-going-to-create-gun-combat-that-was-on-par-with-call-of-duty-or-battlefield — V.A.T.S. as compensation for gunplay (headline only retrievable)
- https://www.pcgamer.com/games/fallout/bethesda-originally-thought-fallout-3s-metro-system-should-track-to-the-surface-world-then-realised-running-through-miles-of-tunnels-was-dull-as-hell-being-realistic-sometimes-isnt-fun — metro cut-back (headline only retrievable)
- https://www.pcgamer.com/games/fallout/the-white-house-is-a-radioactive-crater-in-fallout-3-because-there-were-no-quests-there-so-why-build-it-it-is-our-version-of-indiana-jones-shooting-the-guy-rather-than-pulling-out-his-whip-and-going-into-a-fight — scope-cutting anecdote (title via search)
- https://www.pcgamer.com/games/fallout/todd-howard-says-bethesda-really-didnt-expect-people-to-hate-the-way-fallout-3-ended-with-a-full-stop-and-they-scrambled-together-a-solution-but-ill-give-us-an-average-grade-on-that — Howard on the ending (title via search)

Critiques, retrospectives and community

- https://www.shamusyoung.com/twentysidedtale/?p=27085 — Shamus Young, "The Blistering Stupidity of Fallout 3" (2015)
- https://thewertzone.blogspot.com/2018/12/revisiting-wasteland-fallout-3-and-art.html — retrospective (via search summary)
- https://www.rpgfan.com/review/fallout-3-3/ — review (via search summary)
- https://gamebanshee.com/kdch8 — relay of PCGamesN on Fallout 3 level design and the metro (via search summary)
- https://nma-fallout.com/threads/dungeon-crawler.185660 — community criticism of tunnels and dungeon-heavy design (via search summary)
- https://forums.nexusmods.com/topic/85310-enemy-scaling and https://www.gamesas.com/post524874.html — community explanations of scaling versus Oblivion (via search summaries)
- https://www.gamebanshee.com/988 — "Are Bethesda Games Too Buggy?", PS3 Game of the Year edition save issue (via search summary)
- https://forums.nexusmods.com/topic/749106-fallout-3-crashing-on-windows-7 and https://forums.nexusmods.com/topic/201495-fallout-3-crash-fix-guide/page/2 — PC stability reports and fixes (via search summaries)
- https://www.gamesas.com/post243094.html — PS3 stability reports (via search summary)

Not reachable in this session: Nukapedia / fallout.fandom.com (HTTP 402), geck.uesp.net and dev.fallout.wiki
direct fetches (HTTP 403), full text of the PC Gamer, GamesRadar and TechRadar developer-interview articles
(truncated), and any GDC talk transcripts. Figures that depended on those are tagged `[UNVERIFIED]` above.
