# Fallout (1997) — Gameplay, Systems and Balance

Scope: how the first Fallout plays, the numbers behind its character system and combat, and an assessment of
its balance. Lore, art and narrative are covered elsewhere. Figures are for the patched PC game (v1.1/1.2)
unless stated. Confidence tags follow `CONVENTIONS.md`.

## Quick Reference

- **Structure:** isometric, single-character RPG. Real-time exploration on town maps, a fog-of-war world map
  with random encounters, and turn-based combat on a hex grid driven by action points (AP).
- **Character system (SPECIAL):** 7 primary stats, range 1-10, all start at 5 with 5 spare points (40 total);
  18 skills (3 tagged); 16 traits (pick 0-2); a perk every 3 levels; level cap 21.
- **SPECIAL was an emergency replacement.** The game was built on GURPS; the licence ended in Feb/March 1997,
  about seven months before the October 1997 release. Skills and combat were redesigned and recoded in
  roughly two weeks.
- **XP curve:** level n needs n(n-1)/2 x 1,000 XP (L2 = 1,000; L10 = 45,000; L21 = 210,000). Most runs end
  in the low-to-mid teens, so the level 18 perks and the cap are rarely seen.
- **Derived stats:** HP = 15 + ST + 2xEN (+2 + EN/2 per level); AP = 5 + AG/2; AC = AG; carry weight =
  25 + 25xST lb; sequence = 2xPE; melee damage = ST-5 (min 1); crit chance = LK%; skill points per level =
  5 + 2xIN.
- **Agility and Intelligence are the power stats; Charisma is the dump stat.** AG only pays out on even
  values (AP breakpoints). CH 1 is viable.
- **Gifted (+1 to all seven stats)** is near-universally rated the best trait; its penalties are small.
- **Small Guns carries the first two thirds of the game; Energy Weapons ends it.** Roughly half of the 18
  skills are skippable (Throwing, Traps, Gambling, Barter, Outdoorsman, Doctor, Big Guns, Steal).
- **Aimed shots are the combat endgame:** -60% to hit the eyes also gives +60% critical chance, and the
  critical tables for eyes/head contain armour bypass, knockout, blindness and instant death.
- **Endgame kit:** power armour (+3 ST, DT 12 / DR 40% normal) plus a plasma rifle, both upgradeable to
  hardened power armour and the 4-AP turbo plasma rifle. A lead designer later said the turbo rifle's AP
  cut unbalanced the late game.
- **Time limits:** 150 days to find the water chip (+100 days if you pay water merchants 2,000 caps), then
  in v1.0 a hidden 500-day limit before the mutants take the home vault. Patch 1.1 (13 Nov 1997) removed the
  500-day limit after player complaints. The 150-day limit stayed.
- **Every major quest was meant to support at least two of fight / talk / sneak.** The game can be finished
  without the player killing anyone; the final boss can be argued into destroying himself (needs IN 7, high
  Speech and one piece of evidence).
- **Low-Intelligence play is a distinct mode:** IN below 4 replaces dialogue with grunts and closes most
  quests and all human companions.
- **Companions were a last-minute addition** and it shows: no inventory screen, no armour changes, no combat
  orders, and burst-fire allies that shoot the player.
- **Length:** about 16-17 hours for the main path, 22-25 with side content.
- **Biggest lessons:** build-reactive quest design and visible long-term consequences are what the game is
  remembered for; interface friction, opaque rolls, dead skills and uncontrollable allies are what it is
  forgiven for.

## 1. Moment-to-Moment Play

### 1.1 The three layers

| Layer | What the player does | Notes |
|---|---|---|
| Local map (real time) | Walk/run on an isometric map, talk, loot, use skills on objects, enter buildings | Cursor modes: move, action (context menu: look, use, talk, use skill, use item on), and attack. Skills are applied by picking a skill then clicking a target. |
| World map | Click a destination; the party crawls across a grid while the calendar advances | Squares are revealed as you pass. Travel time is the main consumer of the 150-day budget. Random encounters interrupt travel. |
| Combat (turn-based) | Spend AP on movement (1 AP per hex), attacks, reloads, inventory use | Triggered when a hostile notices the player or the player attacks. Ends when no hostiles remain aware, or by pressing End Combat when safe. |

Display is 640x480 in 256 colours (about 230 usable after palette reservation for colour cycling), with
pre-rendered sprites rather than polygons.

### 1.2 World map and random encounters

- Encounter chance depends on terrain and region; the Outdoorsman skill gives a chance to avoid or be warned
  of an encounter, and the Ranger/Scout/Explorer/Pathfinder perks modify frequency, visibility and speed
  (Pathfinder: -25% travel time per rank).
- Encounter types: hostile wildlife or raiders, neutral traders/patrols, and rare one-off "special
  encounters" weighted by Luck (one of them yields the best pistol-class weapon in the game). The official
  guide warns that Luck 1-2 locks the player out of some of these.
- Caravan escort jobs in the trade hub turn random encounters into a paid activity: 200, 400 or 600 caps per
  trip depending on employer, leaving on fixed days of the month, with a 50-100% chance of an ambush en route.
- Travel is where the time limit bites: crossing the map between distant towns costs one to two weeks each
  way. [UNVERIFIED exact day counts per route]

### 1.3 Pace and opening

The game opens in a cave of rats with a weak level-1 character and no tutorial beyond the manual. One modern
retrospective calls this opening dull and the early hours a poor advertisement for what follows. The first
town is a day or two away, and the first real difficulty spike is the first raider camp or the first
radscorpion cave.

## 2. Character Creation

### 2.1 Primary statistics

All seven start at 5 with 5 points to distribute (minimum 1, maximum 10, total 40 before traits).

| Stat | Governs | Community verdict |
|---|---|---|
| Strength (ST) | HP, carry weight, melee damage, weapon minimum-strength checks (-20% to hit per point short) | 5-6 is enough; power armour adds +3 and an in-game procedure adds +1. ST 7 covers every gun. |
| Perception (PE) | Sequence, ranged to-hit at distance, First Aid/Doctor/Lockpick/Traps base | 5+ to qualify for the best early perk; 6-8 for gun builds. |
| Endurance (EN) | HP, HP per level, healing rate, poison/radiation resistance | Commonly lowered to 4. HP per level only changes on even values. |
| Charisma (CH) | Speech and Barter base, initial NPC reaction (+5 reaction per point) | The dump stat. CH 1 is workable. |
| Intelligence (IN) | Skill points per level, dialogue options, Science/Repair/First Aid/Doctor/Outdoorsman base | "Probably the most important stat" per the best-known fan guide. 7 opens almost all dialogue. |
| Agility (AG) | Action points, armour class, most combat skills, Sneak/Steal/Lockpick/Traps | Take 8 or 10 (odd values waste a point: 6 and 7 both give 8 AP). |
| Luck (LK) | Critical chance, Gambling, special encounters, some perk prerequisites | 6+ for the critical perks; 8-10 for crit builds. |

Stats can be raised in play: +1 to most stats through paid surgery, more to ST via armour. Because of an
implementation glitch IN and LK can gain 2 instead of 1 [per the Jorner guide], so veterans start those at 8.

### 2.2 Derived statistics

| Derived stat | Formula | Example (all stats 5) |
|---|---|---|
| Hit points (level 1) | 15 + ST + 2xEN | 30 |
| HP gained per level | 2 + EN/2, rounded down (the manual states a different, more generous figure) | 4 |
| Action points | 5 + AG/2, rounded down | 7 |
| Armour class | AG (+ armour AC) | 5 |
| Carry weight | 25 + 25xST lb (Small Frame: 15 per ST) | 150 lb |
| Melee damage bonus | ST - 5, minimum 1 | 1 |
| Sequence | 2xPE | 10 |
| Healing rate | EN/3, minimum 1 | 1 |
| Critical chance | LK % | 5% |
| Poison resistance | 5xEN % | 25% |
| Radiation resistance | 2xEN % | 10% |
| Skill points per level | 5 + 2xIN | 15 |
| Perk rate | 1 perk per 3 levels | — |

Cross-checked between fallout.wiki, the RPGClassics shrine and the Jorner guide; all agree.

### 2.3 Skills: starting values

Three skills are tagged at creation. A tagged skill gets an immediate +20% and rises 2% per skill point
instead of 1%. In Fallout 1 a point always buys 1% regardless of how high the skill is (the escalating cost
curve arrived in the sequel). Skills cap at 200%. Unspent points above 99 are lost at level-up.
Non-combat skills are shifted by difficulty: +20% on Easy, -10% on Hard.

| # | Skill | Base formula | Used for | Verdict |
|---|---|---|---|---|
| 1 | Small Guns | 35 + AG | Pistols, SMGs, rifles, shotguns | **Essential.** Best weapon variety, usable from minute one, still strong late via the sniper rifle and .223 pistol. |
| 2 | Big Guns | 10 + AG | Minigun, flamer, rocket launcher | Weak. Only three weapons, all late, heavy and ammo-hungry; low base. |
| 3 | Energy Weapons | 10 + AG | Laser and plasma pistols/rifles, Gatling laser, alien blaster | **Endgame best.** Useless for the first half (no weapons), dominant afterwards. Often tagged late via the Tag! perk. |
| 4 | Unarmed | 65 + (AG+ST)/2 | Fists, knuckles, power fist | Strong. Highest base in the game, cheap 3-AP attacks, power fist late. |
| 5 | Melee Weapons | 55 + (AG+ST)/2 | Knives, spears, sledges, ripper, super sledge | Strong, with knockback utility. |
| 6 | Throwing | 40 + AG | Grenades, spears, knives, rocks | Near useless: scarce consumable ammo, no late-game scaling. |
| 7 | First Aid | 30 + (PE+IN)/2 | Heal minor HP, limited uses per day | Marginal: stimpaks and resting replace it; books raise it for free. |
| 8 | Doctor | 15 + (PE+IN)/2 | Heal more HP, cure crippled limbs | Marginal: paid doctors are everywhere. |
| 9 | Sneak | 25 + AG | Avoid detection, set up thefts and backstabs | Situational. Effect is opaque and appears capped near 95% before modifiers. |
| 10 | Lockpick | 20 + (PE+AG)/2 | Doors, lockers, several quest shortcuts | **High value.** 70-100% opens nearly everything; enables stealth routes through both endgame dungeons. |
| 11 | Steal | 20 + AG | Pickpocketing; also the only way to plant items on allies | Low marginal value: testing found little practical difference between 30% and 200% in ordinary cases. |
| 12 | Traps | 20 + (PE+AG)/2 | Detect/disarm traps, set explosives | Near useless: few traps, low damage from failing. |
| 13 | Science | 25 + 2xIN | Computers, some dialogue, arming the final bomb (70%) | Useful at thresholds (40%, 70%); books cover most of it. |
| 14 | Repair | 20 + IN | Fixing machinery in a handful of quests, obtaining power armour | Threshold skill; books cover it. |
| 15 | Speech | 25 + 2xCH | Persuasion checks, the non-violent ending | **High value.** Around 100% recommended; base depends only weakly on CH, which is why CH can be dumped. |
| 16 | Barter | 20 + 2xCH | Buy prices | Low. Money stops mattering by mid-game; ~60% is plenty. |
| 17 | Gambling | 20 + 3xLK | Casino games | Useless as a skill, but exploitable for unlimited money at modest values. |
| 18 | Outdoorsman | 5 + (IN+EN)/2 | Avoiding random encounters | Low; books cover it. |

Skill books sold in the trade hub raise First Aid, Science, Repair, Small Guns and Outdoorsman up to roughly
91% for free, which further devalues spending points on them. A known exploit temporarily lowers the skill
(harder difficulty setting or stat-reducing drugs) to read past the cap.

### 2.4 Traits

Sixteen optional traits; pick up to two at creation. Each is designed as a benefit paired with a cost.

| Trait | Benefit | Cost | Verdict |
|---|---|---|---|
| Gifted | +1 to all seven stats | -10% all skills, -5 skill points per level | Best in game by consensus; one respected guide author refuses it because it "feels like cheating". |
| Fast Shot | Attacks cost 1 AP less | No aimed shots | Top tier; in Fallout 1 it is reported to apply to hand-to-hand too. Stacks with the rate-of-fire perks. |
| Small Frame | +1 AG | Carry weight 15 lb per ST instead of 25 | Near-free stat point, especially with a pack-mule companion. |
| Finesse | +10% critical chance | All attacks do 30% less damage | Decent for crit builds. |
| One Hander | +20% to hit with one-handed weapons | -40% with two-handed | Good for pistol/unarmed builds; bad late because the best guns are two-handed. |
| Heavy Handed | +4 melee damage | -30 on critical-table rolls | Good early, self-defeating late. |
| Bruiser | +2 ST | -2 AP | Bad: costs the equivalent of 4 AG. |
| Kamikaze | +5 sequence | Natural AC becomes 0 | Poor trade. |
| Fast Metabolism | +2 healing rate | Poison and radiation resistance start at 0% | Marginal. |
| Good Natured | +20% First Aid, Doctor, Speech, Barter | -10% all combat skills | Only for diplomat builds. |
| Skilled | +5 skill points per level | Perk every 4 levels instead of 3 | Bad trade on paper, and reported bugged: the extra points never arrive. [per Jorner guide] |
| Night Person | +1 IN and PE at night | -1 IN and PE by day | Poor: most NPCs and shops are day-only. |
| Chem Reliant | Faster recovery from addiction | Addiction chance doubled | Marginal. |
| Chem Resistant | Addiction chance halved | Chem effects last half as long | Marginal. |
| Jinxed | Everyone suffers more critical failures | ...including you and allies | Niche (pure melee vs. gun users). |
| Bloody Mess | Always see the most violent death animation | None (also alters one ending scene) | Cosmetic. |

Design note: the benefit/cost pairing is elegant on paper, but only about five of sixteen are regularly taken
and one is close to mandatory.

### 2.5 The three premade characters

| | Max Stone (fighter) | Natalia (thief) | Albert (diplomat) |
|---|---|---|---|
| ST / PE / EN | 10 / 4 / 9 | 4 / 5 / 6 | 5 / 6 / 4 |
| CH / IN / AG / LK | 4 / 4 / 7 / 4 | 7 / 7 / 10 / 6 | 9 / 6 / 4 / 6 |
| Traits | Bruiser, Heavy Handed | Night Person, Gifted | Skilled, Good Natured |
| Tag skills | Small Guns, Big Guns, Unarmed | Sneak, Steal, Unarmed | Small Guns, Speech, Barter |

These map directly onto the three archetypes the team designed quests around (brawler, sneaker, talker). All
three are mechanically poor by community standards: Max has IN 4 (13 skill points per level against 21 for an IN 8
build) and a trait that removes 2 AP; Albert has AG 4 (7 AP) and a reportedly non-functional
trait; Natalia is the strongest thanks to AG 10 and Gifted but tags two of the weakest skills. The premades
teach the archetypes but not the system.

## 3. Where SPECIAL Came From

| Date | Event | Source agreement |
|---|---|---|
| Early 1994 | Interplay licenses GURPS from Steve Jackson Games; Tim Cain, a GURPS enthusiast who had written GM utilities for it, starts the engine alone | Agreed |
| 1994-96 | Team grows to ~15 (year two) and ~30 (year three); setting moves from fantasy to time travel to post-nuclear | Agreed |
| Feb-March 1997 | Steve Jackson objects to the violent intro and the mascot art; Interplay drops the licence | Month varies (Feb vs March). The precise cause is [DISPUTED]: most accounts cite violence/art; some participants describe a broader licensing breakdown. |
| Following ~2 weeks | Chris Taylor adapts a homebrew tabletop system he had tinkered with for years; Cain recodes. Skills and combat are replaced | "About a week each" (Wikipedia) vs "two weeks" (Cain, GDC 2012) vs "a few weeks" (wikis) |
| Same period | The acronym is first ACELIPS; a colleague rearranges it to SPECIAL | Agreed |
| Same period | Perks added; per Cain's GDC talk, at the studio head's request and implemented by Taylor in one day | Another account frames perks as the replacement for GURPS advantages; both can be true |
| 10 Oct 1997 | Release | Agreed |

What survived from GURPS: a skill-based, classless design; percentile-ish skill rolls; traits as the
descendant of GURPS disadvantages/quirks; called shots; and the ethos that non-combat skills must matter.
What changed: seven attributes on a 1-10 scale instead of four on a 3-18 scale, a level/XP layer on top
(GURPS has none), and perks as periodic rewards. Luck was added as a stat at Cain's instigation.

Design relevance: a system written in two weeks shipped with ~half its skills under-supported by content.
The structure (stats -> derived stats -> skills -> perks, plus trade-off traits) was sound enough to last
decades; the tuning was not.

## 4. Progression: Levels, Perks

### 4.1 XP table

Threshold for level n = n(n-1)/2 x 1,000.

| Level | XP | Level | XP | Level | XP |
|---|---|---|---|---|---|
| 1 | 0 | 8 | 28,000 | 15 | 105,000 |
| 2 | 1,000 | 9 | 36,000 | 16 | 120,000 |
| 3 | 3,000 | 10 | 45,000 | 17 | 136,000 |
| 4 | 6,000 | 11 | 55,000 | 18 | 153,000 |
| 5 | 10,000 | 12 | 66,000 | 19 | 171,000 |
| 6 | 15,000 | 13 | 78,000 | 20 | 190,000 |
| 7 | 21,000 | 14 | 91,000 | 21 (cap) | 210,000 |

- XP comes from kills, quest completion, and skill use (successful lockpicks, repairs, etc.). Quest XP is
  large relative to kill XP: single quest steps give 500-1,500, and destroying the mutant base awards enough
  for about four levels at once.
- The Jorner guide's own low-IN run cleared both final dungeons at levels 13-15, and notes that grinding the
  best repeatable enemy takes 80+ kills to go from 12 to 18. Seven perks (levels 3-21) is the theoretical
  maximum; four or five is typical. The level-18 capstones are effectively post-game content.

### 4.2 Perks

One perk every 3 levels (every 4 with Skilled). Around 50 perks. Requirements are level + stat/skill
minimums. Table below groups by earliest level; ranks in brackets.

| Lvl | Perk (ranks) | Requirements | Effect | Verdict |
|---|---|---|---|---|
| 3 | Awareness (1) | PE 5 | Shows target HP, weapon and ammo on examine | **Top pick**: pure information, permanently useful |
| 3 | Bonus HtH Damage (3) | AG 6, ST 6 | +2 melee damage per rank | Weak (raises max only; ~+1 average) |
| 3 | Earlier Sequence (3) | PE 6 | +2 sequence | Weak |
| 3 | Faster Healing (3) | EN 6 | +1 healing rate | Weak |
| 3 | Healer (3) | PE 7, AG 6, IN 5, First Aid 40% | +2-5 HP healed | Weak |
| 3 | Night Vision (3) | PE 6 | Less darkness penalty | Weak |
| 3 | Presence (3) | CH 6 | +10 initial reaction | Weak |
| 3 | Quick Pockets (3) | AG 5 | -1 AP to open inventory in combat | Situational |
| 3 | Scout (1) | PE 8 | Reveal more world map | Weak |
| 3 | Smooth Talker (3) | IN 4 | +1 IN for dialogue only | Niche (low-IN builds) |
| 3 | Strong Back (3) | EN 6, ST 6 | +50 lb carry | Weak |
| 3 | Survivalist (3) | EN 6, IN 6, Outdoorsman 40% | +20% Outdoorsman | Weak |
| 3 | Swift Learner (3) | — | +5% XP | Judged the worst pick given the cap and curve |
| 3 | Toughness (3) | EN 6, LK 6 | +10% damage resistance | Decent |
| 6 | Bonus HtH Attacks (1) | AG 6 | Melee/unarmed attacks cost 1 AP less | **Top pick** for melee |
| 6 | Bonus Move (3) | AG 5 | +2 movement-only AP | Good |
| 6 | Bonus Ranged Damage (2) | AG 6, LK 6 | +2 damage per bullet | Weak except with burst weapons |
| 6 | Educated (3) | IN 6 | +2 skill points per level | Weak (too few levels left) |
| 6 | Empathy (1) | PE 7, IN 5 | Colour-codes dialogue lines by NPC reaction | Interesting UI perk |
| 6 | More Criticals (3) | LK 6 | +5% crit chance | Good |
| 6 | Sharpshooter (2) | PE 7, IN 6 | +2 PE for range | Reported half-effective due to a bug |
| 6 | Fortune Finder, Friendly Foe, Ghost, Heave Ho!, Mysterious Stranger, Pathfinder, Rad Resistance, Ranger, Silent Running, Snakeater | various | utility | Mostly filler |
| 9 | Better Criticals (1) | PE 6, LK 6, AG 4 | +20 on critical-table rolls (the only way to reach the instant-death band) | **Top pick** |
| 9 | Bonus Rate of Fire (1) | PE 6, IN 6, AG 7 | Ranged attacks cost 1 AP less | **Top pick** |
| 9 | Dodger (2) | AG 4 | +5 AC | Decent |
| 9 | Mutate! (1) | — | Swap a trait | Niche (drop Fast Shot late) |
| 9 | Animal Friend, Explorer, Flower Child, Master Trader, Pickpocket, Scrounger | various | utility | Filler |
| 12 | Action Boy (3) | AG 5 | +1 AP per rank | Strong |
| 12 | Lifegiver (2-3) | EN 4 | +4 HP per level | Weak this late |
| 12 | Tag! (1) | — | Fourth tag skill | Strong: the standard way to bring Energy Weapons online |
| 12 | Cult of Personality, Master Thief, Medic, Mr. Fixit, Speaker | various | +10-20% to two to four skills | Weak ("only skill points") |
| 15 | Mental Block (1) | — | Resist psychic attacks | Obsoleted by a quest item |
| 18 | Sniper (1) | PE 8, AG 8, Small Guns 80% | Ranged hits crit at roughly 10xLK % | Game-breaking, rarely reached |
| 18 | Slayer (1) | AG 8, ST 8, Unarmed 80% | All hand-to-hand hits are criticals | Game-breaking, rarely reached |
| 18 | Silent Death (1) | AG 10, Sneak 80% | Double damage on sneak backstab | Rarely reached |

Rank counts differ slightly between sources (e.g. Lifegiver 2 vs 3). [UNVERIFIED exact ranks for a few perks]

Observation: perks that change the action economy (AP cost, AP pool) or the crit system are worth a slot;
perks that grant skill points, HP or resistances are not. Roughly 10 of ~50 are competitive.

## 5. Combat Mechanics

### 5.1 Turn structure and AP

- Whoever initiates gets a free opening turn; after that, order is by Sequence (2xPE).
- AP pool: 5 + AG/2, so 5-10 base; perks can push it to 13 plus movement-only AP.

| Action | AP cost |
|---|---|
| Move one hex | 1 |
| Punch / light melee | 3 |
| Heavy melee swing | 4 |
| Pistol / rifle single shot | 4-5 (most are 5) |
| Burst | Single-shot cost +1 |
| Aimed (called) shot | Normal cost +1 |
| Heavy weapons, sniper rifle | 6 |
| Reload | 2 [UNVERIFIED this session; from the manual as remembered] |
| Open inventory in combat | 4, reduced by Quick Pockets [UNVERIFIED as above] |
| Swap between the two active item slots | Free |

- Unspent AP adds to armour class until the next turn [UNVERIFIED this session], which gives "end turn early"
  a small defensive value.
- Opening the inventory costs a flat fee no matter how many items are used inside it, so healing with several
  stimpaks from the inventory screen is far cheaper than using them one at a time from a hand slot. The game
  never explains this.

### 5.2 To-hit

For ranged attacks, restated from fallout.wiki:

```
chance = skill - 30
       + (PE - 2) x 16        (x8 for weapons without the long-range property)
       - 4 x distance_in_hexes
       - target_AC
       - 20 per point of ST below the weapon's minimum
       - 10 in darkness at 5+ hexes
       - aimed-shot penalty
       + weapon accuracy bonus (+20 for several pistols/shotguns)
       + 40 if the target is prone
clamped to a maximum of 95%
```

- Melee/unarmed: essentially skill minus target AC, plus the same aimed-shot penalties.
- One Hander: +20 / -40. Scoped-style weapons trade close-range accuracy for flat long-range accuracy.
- Because penalties stack subtractively, skill above 100% is not wasted: around 150% is where eye shots at
  typical ranges reach the 95% cap, which is why guides recommend one combat skill at ~150%.

### 5.3 Aimed shots

| Target | To-hit penalty | Crit-chance bonus | Typical crit effects |
|---|---|---|---|
| Torso (default) | 0 | 0 | Extra damage, knockdown; instant death only in the top band |
| Legs | -20 | +20 | Crippled leg (movement costs more), knockdown |
| Arms | -30 | +30 | Crippled arm, dropped weapon |
| Groin | -30 | +30 | Knockdown, lost turns |
| Head | -40 | +40 | Knockout, armour bypass, instant death in top band |
| Eyes | -60 | +60 | Blindness (target's PE collapses), armour bypass, instant death in top band |

The crit bonus equalling the hit penalty is the key rule: once skill is high enough to absorb -60, every eye
shot has a 60%+ crit chance before Luck. Burst-only weapons and Fast Shot characters cannot aim.

### 5.4 Critical hits

- Chance = LK% + 5% per More Criticals rank + 10% (Finesse) + aimed-shot bonus + a small bonus from how far
  the hit roll beat the target ((chance - roll)/10, rounded down).
- Sniper perk: a ranged hit that was not already critical gets a second roll against Luck (about 10xLK%).
  Slayer: every hand-to-hand hit is critical.
- On a crit the game rolls 1-100 on a table indexed by **target type x body part**, in bands 1-20, 21-45,
  46-70, 71-90, 91-100 and 101+. Each cell combines a damage multiplier (about x1.5 to x4) with riders:
  ignore armour, knockdown, knockout, blind, cripple, lose next turn, instant death.
- Better Criticals adds +20 to the roll and is the only way into the 101+ band (instant death for head, eyes
  and torso). Heavy Handed subtracts 30.
- Different creature types have different tables, so "eyes" is not universally best (robots and some
  mutants are tougher), but against humanoids it nearly always is.

### 5.5 Critical failures

Misses can become critical failures: lost turn, dropped or jammed weapon, lost ammo, weapon destroyed, energy
weapon exploding, hitting an unintended target. Lower hit chance means more failures; Jinxed raises it for
everyone on the map.

### 5.6 Damage and armour

```
damage = roll(weapon range) [+ melee bonus]
damage = damage - DT(type)             (flat threshold)
damage = damage x (1 - DR(type)%)      (percentage resistance), rounded down
```

- Five main damage types (normal, laser, fire, plasma, explosive) plus electrical/EMP. Each armour has its
  own DT and DR per type.
- Ammunition modifiers: fallout.wiki states Fallout 1 does not apply ammo damage modifiers at all (so
  hollow-point and armour-piercing rounds behave identically), while the Jorner guide says armour-piercing is
  simply worse than hollow-point in practice. [DISPUTED] Either way, the AP/JHP choice presented to the
  player is not a real decision.
- DT is why low-damage, many-bullet weapons collapse against heavy armour (each bullet is reduced
  separately) and why single big hits (plasma, sniper rifle, crits with armour bypass) define the late game.

### 5.7 Burst fire

- Burst fires 3-40 rounds in a cone; each round rolls damage and is reduced by armour individually.
- At point-blank range most of the burst lands on one target and does enormous damage; at range rounds spread
  to anything in the cone, including allies and bystanders.
- Burst weapons in the game: 10 mm SMG (10 rounds), assault rifle (8), combat shotgun (3), minigun (40),
  Gatling laser (10).
- The Gatling laser at point blank is the highest single-action damage in the game; the Jorner guide reports
  crits above 450 against the final boss (who has 500 HP).

### 5.8 Companion AI

Companions were added in the last stretch of development (the dog first, then the first human follower) and
run on the same AI as hostile NPCs, with a "team" flag.

| Problem | Detail |
|---|---|
| No orders | Dialogue offers only: leave, draw your best weapon, change follow distance. No target, stance, burst or healing settings. |
| No inventory access | There is no trade screen. Players use Steal to plant items, Barter to swap, or "use item on". Barter ignores weight, so allies are infinite pack mules. |
| No armour changes | A companion wears what they joined in for the whole game, so by the endgame they die to a single burst. |
| No levelling | Companions keep their starting stats (39-60 HP) while enemies scale to 100+ damage attacks. |
| Friendly fire | Given an SMG, the first human companion bursts through the player. Cain: scripters could not fix it because script code had no access to the AI. |
| Pathing | Companions block doorways and corridors; there is no "push" (added in the sequel). The dog cannot open doors and walks into lethal force fields. |
| Persistence bugs | Dead companions' bodies vanish on reload; saving in combat with a dead companion can freeze the game; one companion can turn permanently hostile. |

| Companion | HP | Recruit | Weapons |
|---|---|---|---|
| Wanderer (first town) | 50 | 100 caps, or free via IN 6 + Speech | Knives, pistols, SMGs |
| Dog (second town) | 50 | Feed it, or wear a specific jacket | Bite |
| Desert ranger (second town) | 60 | After a specific quest | Rifles, shotguns, spears |
| Scavenger (late city) | 39 | Ask | Knives, some pistols, SMGs; can pick locks |

Net effect: companions are useful as early damage sponges and pack mules, and most experienced players leave
them behind before the final dungeons.

## 6. Weapons and Armour

### 6.1 Armour

DT/DR listed as normal / laser / fire / plasma / explosive. Values from fallout.wiki; the hardened power
armour fire/plasma cells were ambiguous in the scrape. [UNVERIFIED for those two cells]

| Armour | AC | DT | DR % | Wt (lb) | Value | When / how |
|---|---|---|---|---|---|---|
| Robes | 5 | 0/0/0/0/0 | 20/25/10/10/20 | 10 | 90 | Disguise in the cult's buildings |
| Leather jacket | 8 | 0/0/0/0/0 | 20/20/10/10/10 | 5 | 300 | First hours |
| Leather armour | 15 | 2/0/0/0/0 | 25/20/20/20/20 | 8 | 800 | Second town, quest reward |
| Metal armour | 10 | 4/6/4/4/4 | 30/75/10/20/25 | 35 | 1,100 | Mid game; heavy |
| Tesla armour | 15 | 4/19/4/10/4 | 20/90/20/80/10 | 35 | 4,200 | Niche anti-energy |
| Combat armour | 20 | 5/8/4/4/6 | 40/60/30/50/40 | 20 | 6,500 | Trade hub (expensive), +20 rad resist |
| Faction combat armour | 20 | 8/8/7/7/8 | 40/70/50/60/40 | 25 | 4,800 | Faction reward |
| Power armour | 25 | 12/18/12/10/20 | 40/80/60/40/50 | 85 | 12,500 | Faction quest; +3 ST, +30 rad resist |
| Hardened power armour | 25 | 13/19/12/13/20 | 50/90/60/50/60 | 100 | 14,500-15,000 | Upgrade by an NPC chemist given a book item |

The jump from combat armour to power armour more than doubles normal DT (5 -> 12). Combined with the +3 ST,
it is the single largest power spike in the game, and it can be obtained around the mid-point by a player who
knows the route (a Repair check on a broken suit, a quest reward gated on karma 16+, or theft from the
faction's stores).

### 6.2 Weapons (selected progression)

| Stage | Weapon | Skill | Damage | AP | Range | Burst | Min ST | Value |
|---|---|---|---|---|---|---|---|---|
| Start | 10 mm pistol | Small Guns | 5-12 | 5 | 25 | — | 3 | 250 |
| Start | Knife / spear | Melee | 1-6 / 3-10 | 3 / 4 | 1 / 2 | — | 2 / 4 | 40 / 80 |
| Early | Hunting rifle | Small Guns | 8-20 | 5 | 40 | — | 5 | 1,000 |
| Early | 10 mm SMG | Small Guns | 5-12 | 5 (+1) | 25 | 10 | 4 | 1,000 |
| Early | Shotgun | Small Guns | 12-22 | 5 | 14 | — | 4 | 800 |
| Early-mid | Desert Eagle .44 | Small Guns | 10-16 | 5 | 25 | — | 5 | 800 |
| Mid | Assault rifle | Small Guns | 8-16 | 5 (+1) | 45 | 8 | 5 | 1,300 |
| Mid | Combat shotgun | Small Guns | 15-25 | 5 (+1) | 22 | 3 | 5 | 2,750 |
| Mid | 14 mm pistol | Small Guns | 12-22 | 5 | 24 | — | 4 | 1,100 |
| Mid | .223 pistol (unique reward) | Small Guns | 20-30 | 5 | 30 | — | 5 | 3,500 |
| Mid-late | Sniper rifle | Small Guns | 14-34 | 6 | 50 | — | 5 | 2,200 |
| Mid-late | Ripper / super sledge | Melee | 15-32 / 18-36 | 4 / 3 | 1 / 2 | — | 4 / 5 | 900 / 3,750 |
| Mid-late | Power fist | Unarmed | 12-24 | 3 | 1 | — | 1 | 2,200 |
| Late | Minigun | Big Guns | 7-11 x40 | 6 | 35 | 40 | 7 | 3,800 |
| Late | Flamer | Big Guns | 40-90 fire | 6 | 5 | — | 6 | 2,000 |
| Late | Rocket launcher | Big Guns | 35-100 expl. | 6 | 40 | — | 6 | 2,300 |
| Late | Laser pistol / rifle | Energy | 10-22 / 25-50 | 5 | 35 / 45 | — | 3 / 6 | 1,400 / 5,000 |
| Late | Plasma pistol / rifle | Energy | 15-35 / 30-65 | 5 | 20 / 25 | — | 4 / 6 | 2,750 / 4,000 |
| Late | Gatling laser | Energy | 20-40 x10 | 6 | 40 | 10 | 6 | 7,500 |
| Endgame | Turbo plasma rifle | Energy | 35-70 | **4** | 35 | — | 6 | 10,000 |
| Special | Alien blaster (rare encounter) | Energy | 30-90 | 4 | 10 | — | 2 | 10,000 |
| Thrown | Frag / plasma / pulse grenade | Throwing | 20-35 / 40-90 / 100-150 (robots) | 4 | 15 | — | 3-4 | 150-300 |

### 6.3 The endgame loadout

- **Hardened power armour + turbo plasma rifle** is the canonical finish. Both upgrades are done by minor
  NPCs in the last city for a trivial cost (a fetch item; a small favour).
- Turbo plasma rifle: 52.5 average damage for 4 AP, versus 47.5 for 5 AP unmodified. With Bonus Rate of Fire
  it is 3 AP; with Fast Shot as well, 2 AP, i.e. five shots a turn at 10 AP. The plasma damage type also hits
  the weakest column of most late enemies' armour.
- The standard late enemy carries a minigun or laser weapon. Against power armour, a minigun bullet
  (7-11 normal) minus DT 12 does zero unless it crits. The armour does not reduce late-game difficulty; it
  largely deletes it, leaving rockets, plasma and criticals as the only threats.
- Feargus Urquhart is recorded as regretting the turbo rifle's AP reduction as unbalancing the late game, and
  as saying both it and the hardened armour were last-minute additions.

## 7. Economy and Barter

- **Currency:** bottle caps. There is no fixed price list for the player: trade is a two-sided barter table
  where goods and caps are placed on either side until the merchant accepts.
- **Pricing rule:** the player's goods are always valued at base value; the merchant's goods are marked up
  by a factor driven by the player's Barter skill versus the merchant's and by reaction. Reaction modifies
  effective Barter by roughly -25% (bad) to +50% (good). At very low skill, mark-ups approach 10x. The Master
  Trader perk is worth a 15-30% discount depending on the shop. [UNVERIFIED exact formula]
- **Merchant stock:** mostly fixed; shops generally restock only caps (their cash resets when you re-open
  dialogue), with a few exceptions. This makes the world's supply of top-tier ammunition finite in practice.
- **Money sinks:** combat armour (6,500), skill books, stat-raising surgery, water caravans (2,000; less
  with Barter), a location holodisk (750, or 500 with a check), healing.
- **Money sources:** selling looted guns (the dominant source), caravan escort pay (200-600 per run), quest
  rewards (hundreds to low thousands), safes.
- **Breakage:**
  - Looted weapons sell at full base value regardless of Barter, so combat characters are rich by mid-game.
  - Gambling at about 50% with a key held down on a roulette table yields tens of thousands of caps.
  - Stealing from merchants and selling back.
  - Bartering to an overloaded companion bypasses carry weight entirely.
- **UI friction:** caps move at most 999 per transfer, so large trades need repeated clicking.
- Net: the economy matters for about the first third of the game (affording leather armour, a rifle, the
  first companion) and is solved thereafter. Barter as a skill has almost no payoff.

## 8. Dialogue System

- **Keyword-free branching trees** with full-sentence player lines, plus an optional typed "ask about"
  keyword box on some NPCs. [UNVERIFIED this session; from play knowledge]
- **Intelligence gates lines.** Options are simply absent if IN is too low; IN 6 opens many and IN 7 nearly
  all. Mentats (a +IN chem) can be taken before a conversation to meet a threshold, and the Smooth Talker
  perk adds dialogue-only IN.
- **IN below 4** swaps the entire tree for grunts. NPCs respond with pity, contempt or confusion. Almost no
  quests can be taken, no human companion can be recruited, and several NPCs turn hostile or behave
  differently (one medic hands out free healing items every conversation). The game is still completable by
  combat: the documented "stupid" route enters the faction bunker by lockpicking, skips every dialogue-gated
  quest, and finishes both end dungeons by force.
- **Speech checks** are hidden percentage rolls against the skill on particular lines. The player sees only
  the outcome, never the odds, which encourages save-scumming. The Empathy perk partially lifts the veil by
  colouring lines according to how the NPC will receive them.
- **Reaction** is a per-NPC number: +5 per CH point, +10 per Presence rank, plus karma, plus reputation-title
  modifiers; at or below 0 is hostile-leaning, 51+ favourable. It shifts which branches open and barter
  prices.
- **Talking heads:** key NPCs (about 20 [UNVERIFIED count]) get a full-screen animated, lip-synced, voiced
  head with mood-dependent expressions. Each was sculpted in clay, digitised and animated: about 8 weeks per
  head, roughly 4 months including voice matching. Everyone else is text-only with floating lines.
- **Sequence breaking:** reviewers at release noted dialogue occasionally referring to events the player had
  not yet seen, a cost of the open structure.

## 9. Quest Design

### 9.1 The rule

Per Cain's GDC postmortem, the team's working standard was that a quest needed solutions on at least two of
three axes (combat, stealth, dialogue) before it counted as done, built around the three archetype
characters. Cain also stated a preference for morally grey quests and for letting players "play badly" so
long as they live with the results.

### 9.2 Worked examples (described generically)

| Quest | Combat | Stealth / skills | Talk |
|---|---|---|---|
| Rescue the headman's daughter from raiders | Kill the camp; or beat the leader in a one-on-one unarmed duel | Sneak to the back, pick the cell lock, walk out | Buy her freedom by barter; or bluff/intimidate the leader |
| Sheriff vs. casino boss (second town) | Shoot the boss; or take the boss's contract and kill the sheriff | Plant a listening device or wear a wire to get a confession | Extract the confession through dialogue; negotiate a higher bounty at IN 6 |
| Obtain the water chip from the ghoul city | Kill the mutant garrison | Slip through sewers; repair the city's pump (Repair check, +1,000 XP) so the locals survive losing the chip | Talk past the garrison; make a deal with the ghoul leader |
| Join the tech faction and get power armour | Raid their stores | Sneak or lockpick into the stores; fix a broken suit with Repair | Complete their "impossible" initiation errand; bluff a quartermaster |
| Destroy the mutant base | Fight through (alarm sounds if a fight exceeds ~2 rounds at the gate) | Use a radio to lure the gate guards away (+1,500 XP); pick the door; wear cult robes; hack force fields; trigger self-destruct from a terminal | Surrender to be escorted inside, then talk or slip away; persuade the base commander |
| Defeat the Master | Kill him: 500 HP, AC 30, two Gatling-laser attacks per round, a reinforcement every other turn (up to 12) | Lockpick into the vault below and arm the bomb (Science 70%, or a key found elsewhere), never meeting him | Present evidence that his plan is biologically doomed; he ends it himself |

### 9.3 Finishing without killing

- Achievable: lockpick/bluff into the mutant base and trigger the self-destruct; convince the Master.
  Whether deaths from the resulting explosions "count" is a matter of taste.
- Tim Cain has said the no-kill run was not planned: a QA tester discovered that the dialogue paths left
  almost no one dead, and the team then adopted it as a goal for later games.
- Requirements for the talk-down: IN 7, high Speech (around 100% recommended; Mentats help), and a specific
  autopsy report obtained (or read) from a faction scientist. Without the evidence the argument cannot be
  made; bluffing with threats makes him hostile.
- Why it works as design: the solution is foreshadowed across three locations, requires the player to have
  engaged with the world rather than just raised a number, and resolves the villain on his own terms. It is
  the most-cited moment in the game.

### 9.4 Sequence breaking and speed

- Nothing gates the end dungeons except knowledge and enemy strength. A documented route with tags in
  Unarmed, Lockpick and Speech goes straight to the mutant base, steals a disguise and key card, triggers the
  countdown, then does the cathedral with a power fist and aimed eye punches: about twenty minutes for a
  practised player. Speedruns of the game in multi-game marathons take about five minutes. [UNVERIFIED time,
  second-hand]
- The cost of that openness: one ending slide combination is unreachable because of ordering bugs, and
  several town endings were cut or never fire (see 10.3).

## 10. Time Limits, Karma and Consequences

### 10.1 The two clocks

| Clock | Length | Modifiers | On expiry | Versions |
|---|---|---|---|---|
| Water chip | 150 days | +100 days by paying water merchants (2,000 caps, less with Barter; +1,000 XP) | Game over cutscene | All versions |
| Invasion of the home vault | 500 days from start | -100 days if the water caravan was sent (it reveals the vault); halved by one action inside the mutant base | Game over cutscene | v1.0 only; patch 1.1 pushed it out to a hard-coded 13 years |
| Town invasions (ending slides only) | Followers 90 days, ghoul city 110 days (or 30 days after clearing its garrison), trade hub 140, tech faction 170, second town 210, first town 230 | Stopped by killing the Master | That town's bad ending | Several of these are cut or unreachable; the ghoul-city one is also visible in play |

Pre-rendered warning cutscenes play at 100 and 50 days remaining on the water clock.

### 10.2 Reception and the patch

- The time limit was argued over internally for months; lead designer Chris Taylor was its main advocate.
- At release it was one of the biggest early-customer complaints. Patch 1.1 (announced 10 Nov, released 13
  Nov 1997, five weeks after launch) removed the 500-day invasion limit. The 150-day chip limit was kept.
  One widely-read summary of Cain's GDC talk says a "release-day patch removed the quest"; that is garbled.
  [DISPUTED wording; patch notes and wikis agree on the 1.1 / 500-day account]
- Cain has said the time limit is the one thing he would change.
- In practice 150 days is generous: an efficient first-time player finds the chip in 60-90 days. The pressure
  is mostly psychological, but it discourages exactly the wandering the open map invites, and it can strand a
  save (a late player with no caps for the water caravan has to restart). Modern players remain split: some
  praise it as the only thing that gives the main quest urgency.
- The more interesting piece is the trade-off on the water caravan: buying 100 days for clock one silently
  costs 100 days on clock two. A hidden cost attached to an obvious convenience.

### 10.3 Karma and reputation

- A single global number ("reputation" in the original UI; "karma" in later usage). Quest outcomes move it by
  small amounts (+1 to +10); killing good or evil characters moves it; jail in one town costs 1-3.
- Thresholds are checked in specific scripts rather than systemically: 16+ lets you pick a better quest
  reward (the power armour route), 20+ earns an escort offer, -21 or lower lets you extort one NPC, -2 or
  lower changes the final scene.
- Three **reputation titles**: Champion (many evil kills while good; +20 reaction), Berserker (many good
  kills; -20, reported non-functional), Childkiller (activates after three child kills; -10 to -30 reaction
  depending on source, and bounty hunters on the world map).
- **There is no per-town reputation meter in Fallout 1**; that arrived in the sequel. Local standing is
  expressed through individual NPC reactions, town-wide hostility when you attack guards, and above all the
  **ending slideshow**, which reports each settlement's fate based on quest flags and the invasion timers.
  [UNVERIFIED: absence asserted from general series knowledge, consistent with all sources read]
- A guide note worth recording: no NPCs are actually flagged "evil" for the reaction system, so negative
  karma never flips into an advantage with bad characters the way the design implies.
- Ending slides: roughly a third of the authored town endings are cut, bugged or unreachable (e.g. the
  good ending for the trade hub and for the Followers; one of the two orderings for the final dungeons).

## 11. Difficulty Curve, Length, UI and Bugs

### 11.1 Difficulty curve

| Phase | Typical level | Experience |
|---|---|---|
| Opening (cave, first town, first vault) | 1-3 | Fragile: 25-35 HP, 50-60% to hit, rats and scorpions can kill. Poison is a real threat. |
| Raider camp, second town | 3-6 | First spike: a dozen armed humans. Leather armour and a rifle or SMG normalise it. |
| Trade hub and side quests | 6-10 | Comfortable. Money and gear flood in. Caravan runs and deathclaw-class enemies offer optional challenge. |
| Ghoul city, tech faction, irradiated ruin | 8-12 | Super mutants with miniguns and flamers are the second spike unless bypassed. Power armour flattens it. |
| Mutant base and cathedral | 12-16 | With power armour and plasma, mostly trivial apart from rockets and criticals. Without them, brutal. |

The curve is inverted relative to modern expectations: hardest in the first three hours, easiest in the last
three. Random critical hits against the player (burst weapons especially) cause sudden deaths throughout,
which the save-anywhere system papers over.

Separate difficulty sliders exist for combat (three levels, changeable mid-fight) and for the game (shifts
non-combat skills by +20% / -10%).

### 11.2 Length

- Main path about 16-17 hours; main plus side content about 22-25 hours (HowLongToBeat figures as relayed by
  secondary sites; one long retrospective says about 25).
- Twelve or so locations, five of them towns. Short by RPG standards of its day, and explicitly built to be
  replayed with a different archetype.

### 11.3 UI/UX friction

| Area | Problem |
|---|---|
| Inventory | A single scrolling column showing a handful of items at a time; no sorting or categories; new items go to the bottom; weight is shown as a total only |
| Stacks | Caps and ammo move at most 999 per transfer |
| Looting | One body at a time; no "take all" in the original release [UNVERIFIED this session] |
| Combat pace | Every NPC on the map takes its turn in sequence, including non-combatants running away; large town fights take minutes per round. The end-turn control is small and unexplained |
| Mode flipping | At the edge of an enemy's perception the game can bounce between real time and turn-based |
| Feedback | Key information arrives as small green text in a scrolling message box and is easily missed; the ammo indicator is an unlabelled bar of dots |
| Opaque rolls | Skill and speech checks never show odds; skills fail silently and can be retried only after a delay or a level |
| Skill use | Applying a skill takes several clicks through a pop-up panel |
| Companions | See 5.8: no inventory, armour or tactics interface at all |
| Onboarding | The manual is required reading. It is very good (written in-world), but the game itself teaches nothing |
| Map | Local automap is minimal; no quest markers; the quest log lists titles only |

The interface is deliberately diegetic (riveted metal panels, CRT readouts). A critic's fair summary is that
it puts atmosphere ahead of clarity.

### 11.4 Bugs

| Bug | Version | Effect |
|---|---|---|
| Stats rise after surviving radiation | 1.0 (fixed 1.1) | Free permanent stat gains |
| Duplicate copies of a companion can join | 1.0 (fixed 1.1) | Party of clones |
| Armour stat bonuses mishandled when moved in inventory | 1.0 (fixed 1.1) | Stackable or lost ST bonus |
| Save corruption when saving in combat | 1.0 (partly fixed 1.1) | Lost saves; enemies get a free turn on reload even after patching |
| A stealth item turns into a Geiger counter | 1.0 (fixed 1.1) | Item swap |
| Skilled trait gives no extra points | All [per Jorner] | Trait is all penalty |
| Sharpshooter gives half its intended effect | All [per Jorner] | Weak perk |
| Bonus Move AP refreshes on save/load in combat | All | Infinite movement |
| Wrong skill checked on the final bomb (Lockpick instead of Repair) | All | Unintended route |
| Reputation title "Berserker" does nothing | All | Dead system |
| Several ending slides unreachable | All | Good endings for some towns cannot occur |
| Saving near touchy NPCs makes them hostile on load | All | Towns turn on the player |
| Companion issues | All | See 5.8 |
| Second-town boss killed -> town turns hostile even on the "good" path | Intermittent | Quest breaks |
| European 1.2 removes children entirely | 1.2 | Related quests/pickpockets become invisible NPCs; this is the default build on current digital stores |

The game shipped after a three-and-a-half-year, roughly $3 million development with QA volunteering
weekends; v1.0 had several game-ruining bugs, and community patches still circulate.

## 12. Balance Assessment

### 12.1 Dominant builds

| Build | Core | Why it wins |
|---|---|---|
| Gifted sniper | AG 10, PE 8, IN 8, LK 8, CH 2; Gifted + Finesse or Small Frame; tags Small Guns, Speech, Lockpick; Awareness -> More Criticals -> Better Criticals -> Bonus Rate of Fire -> Tag! (Energy Weapons) -> Action Boy | Covers all three solution axes at once. Aimed eye shots with 60-80% crit chance and armour-bypassing crit results end every fight in the first round. |
| Fast Shot energy gunner | AG 10; Fast Shot + Gifted; Bonus Rate of Fire; turbo plasma rifle or alien blaster at 2 AP | Five 50-damage plasma shots per turn. Gives up aimed shots but does not need them. |
| Unarmed/melee critter | AG 10, ST 6+; Bonus HtH Attacks (2 AP punches); power fist or super sledge; Slayer if reached | Highest base skill in the game, no ammunition economy, strong from level 1; knockback and knockout lock enemies down. |
| Diplomat-infiltrator | IN 8+, Speech ~100%, Lockpick ~100%, Science 70% | Skips both final dungeons' fights and the final boss. Needs a little combat ability (or a lot of running) for the wilderness. |

The first build is the important one: because Speech's base barely depends on Charisma (25 + 2xCH) and skill
points come from Intelligence, **the best fighter and the best talker are the same character.** The three
archetypes the quests were built for collapse into one optimal generalist.

### 12.2 Dump stats and dead content

- **Charisma** is the dump stat: +2% Speech and Barter and +5 reaction per point, no companion limit, almost
  no hard checks. Dropping CH from 5 to 1 costs 8% Speech (four skill points when tagged).
- **Endurance** is the second dump: HP matters less than not being hit and killing first, and power armour
  makes HP nearly irrelevant.
- **Strength** above 6 is wasted because armour and surgery supply up to +4.
- **Odd Agility** values are wasted.
- **Dead or near-dead skills:** Throwing, Traps, Gambling (as intended), Barter, Outdoorsman, Doctor, First
  Aid, Big Guns, Steal. That is half the skill list. Several are dead because content does not call for them
  (Traps, Throwing), others because a consumable or NPC service duplicates them (Doctor, First Aid), others
  because free books cover the useful range (Science, Repair, Outdoorsman).
- **Dead traits:** 10 or 11 of 16. **Dead perks:** roughly 40 of 50.

### 12.3 Broken strategies

- Eye shots + Better Criticals (instant kills, armour bypass, blinding).
- Power armour obtained at level 6-8 by a player who knows where to go.
- Turbo plasma at 2-3 AP.
- Point-blank burst with the Gatling laser or minigun: hundreds of damage per action.
- Roulette macro for unlimited caps; steal-and-resell.
- Chem stacking before stat checks (Mentats for dialogue and perk prerequisites; a combat stimulant for
  resistance). Addiction is a weak deterrent.
- Stimpak spam from the inventory screen for one flat AP fee.
- Knock out, loot and leave; hold-a-key tricks to act first on map load.
- Save-scumming hidden checks (speech, steal, lockpick, crits). The game's opacity plus save-anywhere makes
  this the default way most people play.
- Companions as weightless mules.

### 12.4 What it gets right about player agency

1. **Builds change the content, not just the numbers.** A low-IN brute, a silver-tongued coward and a thief
   see materially different games in the same 20 hours. The low-IN dialogue rewrite is expensive, used by few
   players, and remembered by everyone.
2. **Multiple solutions are authored per quest, not per system.** Each route is a hand-placed back door,
   terminal, disguise or dialogue branch. This is costly, but it guarantees each route is actually fun.
3. **The critical path can be attacked from any angle, in any order, at any level.** Only knowledge and enemy
   strength gate it. That is what makes twenty-minute runs, no-kill runs and stupid runs all possible in one
   game.
4. **The villain can be defeated by understanding him.** The talk-down needs evidence gathered in the world,
   a stat threshold and a skill threshold, so it reads as earned.
5. **Consequences are reported back.** The ending slideshow turns dozens of small decisions into each town's
   fate. It is cheap to produce relative to its emotional payoff.
6. **The player is allowed to fail and to be awful.** Any NPC can be killed, quests can be broken
   irrecoverably, and the game continues.
7. **Trade-off thinking is built into creation.** Traits and the 40-point stat budget force identity-defining
   choices before the first minute of play, even if the tuning lets a few choices dominate.

### 12.5 What it gets wrong

1. Half the skills and most traits/perks have too little content or payoff; the system promises more breadth
   than the game delivers.
2. The optimal character is a generalist, which undermines the archetype-based quest design.
3. The difficulty curve is inverted and the endgame gear removes combat as a threat.
4. Hidden rolls and silent failures make skills feel arbitrary and push players into reloading.
5. Companions were bolted on with no interface or dedicated AI.
6. The time limit fights the exploration the map invites, and the hidden second clock punished players
   without warning.
7. The interface taxes the most frequent actions (inventory, trading, ending turns).

## Design Takeaways

**Learn from**

- **Author at least two, ideally three, routes through every critical-path quest, and make the final
  confrontation solvable without combat via evidence the player has to find.** This is the feature people
  still talk about three decades on.
- **Let a mental stat rewrite dialogue wholesale at the extremes.** It is the strongest possible signal that
  the character sheet matters. Budget for it early; it cannot be retrofitted.
- **Keep the critical path ungated except by knowledge and danger.** It gives speedrunners, replayers and
  role-players the same gift.
- **Close with consequence reporting per settlement or faction.** Cheap to build, disproportionately
  memorable. Track flags for it from day one, and test that every authored ending is reachable.
- **Tie crit chance to risk taken** (their aimed-shot rule: the accuracy you give up is the crit chance you
  gain). It is a one-line rule that makes every attack a decision. But cap the payoff: no instant kills on
  bosses, and give enemies tools against it.
- **Pair every creation-time bonus with a cost**, as traits do, and playtest until at least two thirds of
  them see real use.
- **Perks should change the action economy or reveal information**, not hand out flat percentages. The best
  early perk in the game does nothing but show enemy HP.
- **A hidden cost on an obvious convenience** (buying time for one clock by shortening another) is a good
  pattern, provided the player can discover the link before it kills a save.

**Avoid**

- **Do not ship skills without content.** For every skill, list the quests, shortcuts and encounters that
  call for it; if the list is short, merge or cut the skill. Aim for 10-12 skills that all earn their place
  rather than 18 where 9 are traps.
- **Do not let one stat feed both the talking and the progression economy while the "social" stat feeds
  neither.** Make sure the charismatic character gets something no one else can (companion capacity, unique
  routes, prices that stay relevant).
- **Break stat breakpoints visibly or remove them.** Odd-value dead zones punish players who have not read a
  guide.
- **Do not hide odds.** Show the chance on speech, lockpick and steal attempts, or use deterministic
  thresholds. Hidden rolls plus free saving equals reloading, not role-playing.
- **Hard global timers with a game-over are the wrong urgency tool for an exploration game.** Prefer
  escalating world-state changes (towns fall, prices rise, routes close) that the player can see coming and
  live with. If a timer exists, never hide it.
- **Do not let endgame armour zero out the common enemy's damage.** Keep thresholds proportional so late
  enemies remain a threat; make the best gear a capstone, not a mid-game pickup for those who know the map;
  playtest any last-minute "cool upgrade" against the action economy.
- **Companions need their own interface and AI from the start**: shared inventory, equippable armour,
  stance/target rules, friendly-fire avoidance, and a way to move them out of doorways. Do not reuse enemy AI.
- **Fix the inverted difficulty curve.** The first three hours should not be the hardest and dullest; open
  with a situation that shows off multiple solutions, not a corridor of vermin.
- **Budget interface time for the most frequent verbs** (loot, trade, heal, end turn). Diegetic styling is
  fine; it must not cost clarity. Speed up or batch non-combatant turns.
- **Remove degenerate money loops** (unbounded gambling, full-value loot resale) or the economy stops being a
  system after the first act.

## Sources

Consulted directly:

- fallout.wiki — derived statistics: https://fallout.wiki/wiki/Fallout_derived_statistics
- fallout.wiki — skills: https://fallout.wiki/wiki/Fallout_skills
- fallout.wiki — perks: https://fallout.wiki/wiki/Fallout_perks
- fallout.wiki — traits (list only): https://fallout.wiki/wiki/Fallout_traits
- fallout.wiki — armour: https://fallout.wiki/wiki/Fallout_armor_and_clothing
- fallout.wiki — weapons: https://fallout.wiki/wiki/Fallout_weapons
- fallout.wiki — combat: https://fallout.wiki/wiki/Fallout_combat
- fallout.wiki — levels: https://fallout.wiki/wiki/Level_(Fallout)
- fallout.wiki — critical hits and critical chance: https://fallout.wiki/wiki/Critical_Hit and
  https://fallout.wiki/wiki/Critical_Chance_(Fallout)
- fallout.wiki — barter: https://fallout.wiki/wiki/Barter_(Fallout)
- fallout.wiki — karma: https://fallout.wiki/wiki/Karma_(Fallout)
- fallout.wiki — companions: https://fallout.wiki/wiki/Fallout_companions
- fallout.wiki — the Master: https://fallout.wiki/wiki/The_Master
- fallout.wiki — endings and invasion timers: https://fallout.wiki/wiki/Fallout_endings
- fallout.wiki — time limit: https://fallout.wiki/wiki/Time_limit
- fallout.wiki — patches: https://fallout.wiki/wiki/Fallout_patches
- fallout.wiki — bugs: https://fallout.wiki/wiki/Fallout_bugs
- fallout.wiki — turbo plasma rifle and hardened power armour:
  https://fallout.wiki/wiki/Turbo_Plasma_Rifle_(Fallout) and
  https://fallout.wiki/wiki/Hardened_Power_Armor_(Fallout)
- Per Jorner, "The Nearly Ultimate Fallout Guide" v1.1 (mirror):
  https://lemmings19.github.io/fallout-1-walkthrough/original-source.html
- RPGClassics Fallout shrine, character creation (traits, premades, formulas):
  https://shrines.rpgclassics.com/pc/fallout1/CharacterCreation.shtml
- Walkthrough credited to Chris Taylor and Tim Cain (archive copy):
  https://rpggamers.com/walkthrough/fallout-walkthrough
- Summary of Tim Cain's GDC 2012 Fallout postmortem:
  https://thiscageisworms.com/2012/04/09/tim-cains-gdc-2012-talk-fallout/
- Game Developer, on SPECIAL replacing GURPS:
  https://gamedeveloper.com/design/how-i-fallout-i-almost-didn-t-ship-with-its-key-special-system
- Jimmy Maher (The Digital Antiquarian), "The CRPG Renaissance, Part 1: Fallout", with reader comments:
  https://www.filfre.net/2025/01/the-crpg-renaissance-part-1-fallout/
- 80.lv, on Tim Cain's account of the accidental pacifist run:
  https://80.lv/articles/original-fallout-s-pacifist-run-was-created-accidentaly
- Wikipedia, Fallout (video game): https://en.wikipedia.org/wiki/Fallout_(video_game)

Seen only as search-result excerpts (not opened in full):

- PC Gamer, on Cain's GURPS notes and the lost licences:
  https://www.pcgamer.com/games/rpg/fallouts-creator-reveals-you-could-have-played-as-a-snoring-cow-hater-who-believes-in-ufos-had-black-isle-stuck-with-its-original-licensed-roleplaying-system/
- GOG forum threads on the time limit: https://gog.com/forum/fallout_series/fallout_1_patches_time_limit
- GOG forum thread on no-kill play: https://gog.com/forum/fallout_series/must_i_kill
- GamePro (DE) playtime ranking: https://www.gamepro.de/artikel/fallout-spielzeit-ranking,3433300.html
- PC Gamer, series speedrun: https://pcgamer.com/fallout-speedrunner-beats-all-5-games-in-under-90-minutes

Not reachable during this session (so not used): Nukapedia / fallout.fandom.com (HTTP 402), StrategyWiki
(403), speedrun.com (403), NMA-Fallout forum (403), the turbo-wiki archive of Tim Cain's YouTube summaries
(login wall). Tim Cain's own videos were therefore used only through second-hand reporting.

### Known gaps

- Exact barter price formula, and exact karma change per kill.
- Full critical-hit tables per creature type (structure and bands confirmed; cell values not transcribed).
- AP costs for reload and inventory, "unspent AP adds to AC", and the absence of a per-town reputation
  meter are stated from general knowledge and tagged, not confirmed against a source this session.
- Whether Fallout 1 applies ammunition modifiers (sources conflict).
- Exact talking-head count; exact speedrun record; HowLongToBeat figures are second-hand.
- Per-route world-map travel times.
