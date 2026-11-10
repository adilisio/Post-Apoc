# Fallout 2 (1998) — Gameplay, Systems and Balance

Scope: how Fallout 2 plays, what its numbers are, where its balance breaks, and what its structure (a big
web of town hubs with heavy reactivity) teaches us. Story and lore are covered elsewhere.

Confidence notes used below: `[UNVERIFIED]` = stated from general community knowledge and not re-checked
against a source in this research pass; `[DISPUTED]` = sources disagree.

## Quick Reference

- Built in roughly 12 months (start October 1997, gold 22 October 1998, release 30 October 1998) on the
  Fallout 1 engine, with a target of about twice the world size. Tim Cain, Leonard Boyarsky and Jason
  Anderson left early in development; Feargus Urquhart and Matt Norton became lead designers and areas
  were handed out to many designers in parallel.
- The rules are Fallout 1's SPECIAL almost unchanged. The sequel's changes are mostly **content and
  convenience**: more towns, more quests, more perks, controllable companions, a car, push-NPC, no hard
  time limit, level cap 99.
- Level cap 99 (level 99 needs 4,851,000 XP by the n(n-1)/2 x 1000 curve); one perk every 3 levels
  (every 4 with Skilled). A normal playthrough ends in the mid-20s to low-30s `[UNVERIFIED]`, so the
  level-24 perks (Sniper, Slayer) are the practical capstones.
- Skill cap 300% (200% in Fallout 1). Cost per point rises in bands: 1 SP to 100%, 2 to 125%, 3 to 150%,
  4 to 175%, 5 to 200%, 6 to 300%. Tagged skills gain 2% per purchase.
- The damage formula applies the ammo multiplier **before** armor. Armor-piercing rounds halve damage
  before threshold is subtracted, so AP is worse than hollow-point against almost everything. This is the
  best-known balance bug in the game.
- Dominant build: high Agility, Gifted, Small Guns into Sniper at level 24 with Luck 10 (every hit is a
  critical), plus Bonus Rate of Fire and, optionally, Fast Shot. Melee equivalent: Slayer.
- The best armor tier (Advanced Power Armor: AC 30, normal DT 15 / DR 55%) can be taken from an unguarded
  locker at Navarro by a level-1 to level-3 character who walks down the coast and passes one dialogue
  check. Nothing gates it except knowing where it is.
- Useless or near-useless skills per the standard community guide: Throwing, Barter, Gambling, Sneak,
  Steal, and First Aid/Outdoorsman/Repair as point sinks (books and trainers cover them).
- Party size = Charisma / 2 rounded down (+1 with Magnetic Personality). Companions level up, wear armor
  (humans only), and have a combat-behaviour menu. This turned Charisma from a dump stat into a real choice.
- Reactivity runs on four layers: karma (a number), per-town reputation (a number per town), special
  titles (boolean flags such as Made Man, Slaver, Childkiller, Prizefighter, Porn Star), and stat checks
  in dialogue (notably Intelligence below 4 rewrites nearly all dialogue).
- The mid-game is a genuinely interlinked political web: Vault City, Gecko, NCR, New Reno and Redding
  each have endings determined by quests done in the *other* towns.
- The mandatory tutorial dungeon (Temple of Trials) was demanded by marketing, forces spear/unarmed
  combat on every build, and is the most disliked part of the game.
- The early game (Arroyo to the Den) is the hardest stretch for any non-combat character: no gun, almost
  no money, weak armor, lethal random encounters.
- Shipped very buggy. Official patch 1.02d (11 February 1999) invalidated v1.0 saves. Community patch by
  "killap" fixes 800+ further bugs; his Restoration Project re-adds cut locations.
- Metacritic 86. Critics praised scale and freedom; criticised bugs and "more of the same" technology.
  Its own designers later called it patchwork and tonally unsupervised.

## 1. Development context that explains the design

| Date | Event |
|---|---|
| October 1997 | Development begins right after Fallout 1 ships; most of the original team returns |
| Late November 1997 | Tim Cain tells Feargus Urquhart he is considering leaving |
| Late January 1998 | Interplay confirms Cain's departure; Boyarsky and Anderson follow (Troika Games) |
| 13 February 1998 | Game announced; Urquhart and Matt Norton lead design; four Planescape: Torment designers pulled over |
| 22 October 1998 | Gold master |
| 30 October 1998 | Release |
| 11 February 1999 | Patch 1.02d ("final US patch") |

Why Cain left, in his own later account (2023 video, reported by several outlets): "exhaustion,
interference, and lack of motivation." Specifics he gave: more crunch as the reward for the first game,
responsibilities he did not want, box art outsourced without consulting him, and a reduced bonus.
He has asked that Brian Fargo not be cast as a villain.

Consequences visible in the product:

- **Parallel area design with little oversight.** Chris Avellone (who did New Reno and Vault City while
  also working on Planescape: Torment) described an emergency meeting where Urquhart handed out areas
  quickly. He later called it "a slapdash project without a lot of oversight" and said there was no clear
  "spine" to the game. Each town is strong on its own terms; the towns do not share a tone.
- **Tone drift.** Cain's rule on the first game (no joke the player needs outside knowledge to get) was
  dropped. Special encounters and several towns lean on film and TV references.
- **Marketing mandates.** A tutorial level and other requests came from outside the team (see section 8).
- **Too big for the schedule.** Scott Everts later said the game was made "too big"; the bug count at
  launch and the amount of cut content (later restored by fans) are the evidence.

## 2. What changed from Fallout 1

| Area | Fallout 1 | Fallout 2 |
|---|---|---|
| World size | ~12 map locations `[UNVERIFIED]` | ~20+ named locations, several multi-map cities; design target of 2x |
| Time pressure | 150-day water chip deadline (plus a mutant-invasion timer in v1.0) | No fail timer. Only an engine limit: the game ends after 13 in-game years (25 July 2254). Dream messages urge haste but nothing happens |
| Level cap | 21 | 99 |
| Skill cap | 200% | 300% (per the 1.02d readme, raised to 300 in the patch) |
| Starting skills | Higher base values | Lower base values (e.g. Small Guns 5% + 4 x AG) |
| Perks | ~50 `[UNVERIFIED]` | 70 regular + 12 special (implants, training, quest-granted) |
| Companions | 4, uncontrollable, do not level, cannot change armor | 14 permanent; level in stages; equip armor/weapons; combat-settings menu; limit = CH / 2 |
| Blocking NPCs | Constant doorway blockage | "Push" command moves any friendly NPC one hex |
| Travel | On foot only | Buyable car with trunk storage, upgrades and fuel |
| Traits | Night Person | Replaced by Sex Appeal |
| Ammo | Ammo modifiers not functional | AC/DR/damage modifiers per ammo type work (and are mis-tuned, see section 5) |
| Unarmed | One punch, one kick | Tiered special punches/kicks unlocked by skill, level and stats `[UNVERIFIED]` |
| Reactivity | Karma + a few titles | Karma + per-town reputation + many titles + more stat/skill gated dialogue |
| UI | Loot one item at a time | "Take all", more skill-on-object uses (Repair, Science, Doctor on world objects and NPCs) |
| After the ending | Game over | Play continues after the final boss |

The key design fact: **almost no rules were rebalanced for the larger game.** XP curve, perk cadence,
weapon skills and damage maths were carried over, then stretched across two to three times as much content
and a much higher gear ceiling. Most balance problems follow from that.

## 3. Character system

### 3.1 Primary and derived stats

Seven stats, 1-10, 40 points total at start (5 in each plus 5 free), reducible to 1 to buy others.

| Derived stat | Formula |
|---|---|
| Hit points (start) | 15 + ST + 2 x EN |
| HP per level | 2 + EN / 2 (rounded down) `[UNVERIFIED]` |
| Action points | 5 + AG / 2 (rounded down) |
| Armor class | AG + armor |
| Carry weight | 25 + 25 x ST lbs (Small Frame: 25 + 15 x ST `[UNVERIFIED]`) |
| Melee damage bonus | ST - 5 (minimum 1) |
| Sequence | 2 x PE |
| Healing rate | EN / 2 (minimum 1) |
| Critical chance | LK % |
| Poison resistance | 5 x EN % |
| Radiation resistance | 2 x EN % |
| Skill points per level | 5 + 2 x IN (Skilled +5, Gifted -5) `[UNVERIFIED]` |
| Party limit | CH / 2 rounded down |

Design consequences noted by Per Jorner's guide (the standard community reference):

- Action points only change on even Agility, so odd AG values are "wasted"; the same half-step logic
  applies to several other stats.
- Endurance is weak: it "only affects HP" and two extra points are worth about 30 HP by the end. Advice:
  do not go above 4.
- Agility "never below 6"; 10 is fine. AP is the most valuable currency in the game.
- Intelligence 7 is "balanced"; it drives skill points *and* dialogue options.
- Luck is the weakest stat early, then becomes decisive once Sniper/Slayer and Better Criticals arrive.
- In-game permanent gains are plentiful: by the guide's count ST can rise by 6 (power armor +4 counted),
  PE by 2, EN by 1, CH by 3, IN by 3, AG by 1, LK by 3 through implants, surgery, items and events. This
  rewards players who know the game and under-buy those stats at creation.

### 3.2 Traits (pick up to two)

Effects below are the commonly documented ones; fallout.wiki's trait index did not list numbers on the
page fetched, so exact values are `[UNVERIFIED]` unless Jorner's guide is cited.

| Trait | Benefit | Penalty | Community verdict (Jorner) |
|---|---|---|---|
| Gifted | +1 to all seven stats | -10% to all skills, -5 skill points per level | "Regarded as the best"; seven stat points for a small skill tax |
| Small Frame | +1 Agility | Lower carry weight | Recommended; a free stat point, and companions/car carry the loot |
| Fast Shot | Ranged attacks cost 1 AP less | No aimed (targeted) shots | Author's favourite for gunfighters; stacks with Bonus Rate of Fire |
| Finesse | +10% critical chance | Targets get +30% damage resistance | Good early; made obsolete by Sniper/Slayer |
| One Hander | +20% to hit with one-handed weapons | -40% with two-handed | Good for melee/unarmed |
| Heavy Handed | +4 melee damage | -30 on the critical effect table | Good early, poor late |
| Jinxed | Everyone (you included) has more critical failures | — | Only for pure melee novelty builds |
| Good Natured | +15% First Aid, Doctor, Speech, Barter | -10% combat skills | Marginal |
| Sex Appeal | Better reactions from the opposite sex | Worse from the same sex | Marginal; helps low-CH barter |
| Skilled | +5 skill points per level | Perk every 4 levels instead of 3 | Avoid; perks are worth far more than skill points |
| Bruiser | +2 ST | -2 AP | Avoid; AP is king |
| Kamikaze | +5 sequence | Base armor class 0 | Avoid |
| Fast Metabolism | +2 healing rate | No starting rad/poison resistance | Avoid |
| Chem Reliant / Chem Resistant | Addiction tuning | Addiction tuning | Avoid |
| Bloody Mess | Always the goriest death animation | — | Cosmetic |

Pattern worth noting: of 16 traits, about 5 are ever recommended, and one (Gifted) is close to mandatory
for optimisers. The "benefit with a drawback" premise only works when drawbacks bite; Gifted's drawback is
paid in the game's cheapest currency (skill points), Skilled's is paid in its most expensive (perks).

### 3.3 Skills

18 skills. Three are tagged at creation: a tagged skill gets a one-time +20% `[UNVERIFIED]` and gains 2%
per skill point spent.

| Skill | Starting value | Skill book |
|---|---|---|
| Small Guns | 5 + 4 x AG | Guns and Bullets |
| Big Guns | 2 x AG | — |
| Energy Weapons | 2 x AG | Cat's Paw issue 5 (one copy) |
| Unarmed | 30 + 2 x (ST + AG) | — |
| Melee Weapons | 20 + 2 x (ST + AG) | — |
| Throwing | 4 x AG | — |
| First Aid | 2 x (PE + IN) | First Aid Book |
| Doctor | 5 + PE + IN | — |
| Sneak | 5 + 3 x AG | — |
| Lockpick | 10 + PE + AG | — |
| Steal | 3 x AG | — |
| Traps | 10 + PE + AG | — |
| Science | 4 x IN | Big Book of Science |
| Repair | 3 x IN | Dean's Electronics |
| Speech | 5 x CH | — |
| Barter | 4 x CH | — |
| Gambling | 5 x LK | — |
| Outdoorsman | 2 x (EN + IN) | Scout Handbook |

Cost to raise a skill by one purchase:

| Current skill | Skill points per purchase | Tagged: % gained per purchase |
|---|---|---|
| up to 100% | 1 | 2% |
| 101-125% | 2 | 2% |
| 126-150% | 3 | 2% |
| 151-175% | 4 | 2% |
| 176-200% | 5 | 2% |
| 201-300% | 6 | 2% |

So tagging halves the cost at every band. Raising an untagged skill from 100% to 200% costs
25 x 2 + 25 x 3 + 25 x 4 + 25 x 5 = 350 points; tagged, 175. Unspent points above 99 are lost at level-up.

Other skill rules:

- **Difficulty setting** shifts non-combat, non-tagged skills: -10% on hard, +20% on easy. Players abuse
  this by flipping difficulty for a single check, or to dip a skill under a cost threshold.
- **Skill books.** Commonly documented formula: gain = (100 - current skill) / 10, rounded down, so books
  stop working at 91%; Comprehension adds 50% `[UNVERIFIED — formula not re-confirmed this pass]`. Books
  are sold and restocked in several towns, so a patient player buys First Aid, Science, Repair, Outdoorsman
  and Small Guns up to ~91% with money instead of skill points. This is why the community guide says those
  skills should be raised "without points."
- **Trainers** also hand out free skill (e.g. a boxing coach: +10% Unarmed and +10% Melee Weapons; an
  Outdoorsman trainer: +2 x IN %).
- **Useful ceilings.** Jorner: most skills "aren't worth raising above 101%"; combat skills are worth
  raising until you reach the 95% hit-chance cap under the penalties you actually face (range, darkness,
  aimed shots, enemy AC). The 300% cap exists mainly so targeted eye shots at long range against
  AC 30-35 enemies can still reach 95%.

Skill evaluation (community consensus, mostly Jorner):

| Skill | Verdict | Why |
|---|---|---|
| Small Guns | Best combat skill | Covers the whole game from 10mm pistol to Gauss rifle; has a skill book; feeds Sniper |
| Speech | Best non-combat skill | Most quest branches and XP shortcuts key off it |
| Lockpick | Essential | Many doors/containers; no reliable substitute |
| Doctor | Useful to ~75% | Fixes crippled limbs; gates a Vault City perk chain and Living Anatomy (60%) |
| Science, Repair | Useful to ~80-100% | Quest gates; mostly reachable by books |
| Energy Weapons, Big Guns | Late-game alternatives | Weapons arrive late; companions can cover them |
| Melee / Unarmed | Viable | Strong end state (Slayer), weak middle |
| Traps | Minor | 60-70% is plenty |
| Outdoorsman, First Aid | Book-only | Never worth points |
| Sneak | Weak | Little content is built around it; killing is usually simpler |
| Steal | Weak/risky | Failure turns towns hostile; save-scumming makes it strong but degenerate |
| Barter | Useless | Money is never scarce past the early game; Charisma matters more than the skill |
| Gambling | Useless as designed | Either irrelevant or, at high values, an infinite money button |
| Throwing | Useless | Grenades are scarce and outclassed |

### 3.4 Perks

One perk every 3 levels (levels 3, 6, 9, ...). 70 regular perks. Highlights and traps:

| Perk | Level | Requirements | Effect | Verdict |
|---|---|---|---|---|
| Awareness | 3 | PE 5 | Shows target HP, weapon and ammo | Top-3 in Jorner's list; information is power |
| Quick Pockets | 3 | AG 5 | Inventory in combat costs 2 AP (normally 4) | Recommended |
| Toughness | 3 | EN 6, LK 6 | +10% DR, 3 ranks | Possibly useful |
| Swift Learner | 3 | — | +5% XP, 3 ranks | "Deceptively poor"; classic trap |
| Here and Now | 3 | — | One immediate level | Trap |
| Bonus Move | 6 | AG 5 | +2 movement-only AP, 2 ranks | Recommended for melee |
| More Criticals | 6 | LK 6 | +5% crit, 3 ranks | OK until Sniper |
| Educated | 6 | IN 6 | +2 skill points per level, 3 ranks | Trap (skill points are cheap) |
| Magnetic Personality | 6 | CH below 10 | +1 companion slot | Good for party builds |
| Better Criticals | 9 | PE 6, LK 6, AG 4 | +20 on the critical effect roll | Core |
| Sharpshooter | 9 | PE 7, IN 6 | +2 effective PE for range | Fine |
| Mutate! | 9 | — | Swap one trait | Lets you drop Finesse/Heavy Handed late |
| Action Boy | 12 | AG 5 | +1 AP, 2 ranks | Core |
| Living Anatomy | 12 | Doctor 60% | +10% Doctor, +5 damage per hit vs living targets | Core; +5 applies after armor, so it is large for burst weapons |
| Lifegiver | 12 | EN 4 | +4 HP per level, 2 ranks | Decent |
| Gain [stat] | 12 | Stat below 10 | +1 to a stat | Gain Agility on odd AG is +1 AP |
| Tag! | 12 | — | Fourth tag skill | Doubtful by level 12 |
| HtH Evade | 12 | Unarmed 75% | AC bonus from unused AP and Unarmed / 12 | Niche |
| Bonus Rate of Fire | 15 | PE 6, IN 6, AG 7 | Ranged attacks cost 1 AP less | Top-3; defines gun builds |
| Bonus HtH Attacks | 15 | AG 6 | Melee/unarmed attacks cost 1 AP less | Core for melee |
| Pickpocket | 15 | AG 8, Steal 80% | Ignore size/facing when stealing | Doubtful |
| Silent Death | 18 | AG 10, Sneak 80%, Unarmed 80% | Double HtH damage sneaking from behind | Flavour |
| Sniper | 24 | PE 8, AG 8, Small Guns 80% | Each ranged hit gets a second roll: Luck x 10% chance to become a critical | Top-3; with Luck 10 every hit is a critical |
| Slayer | 24 | ST 8, AG 8, Unarmed 80% | Every HtH hit is a critical | Melee capstone |

Notes:

- Jorner states Cult of Personality and Karma Beacon "have no effect in the game"; the wiki lists
  intended effects. `[DISPUTED]`
- Animal Friend, Flower Child, Mental Block and Scrounger are listed by the guide as not implemented.
- The official patch nerfed several skill perks (Speaker +40% to +20%, Negotiator +20% to +10%) and
  switched many to percentage bonuses.
- Perk requirements are checked against current stats, and the wiki notes that perks taken while chems
  (Mentats, Buffout) are raising stats are permanent. Drugging up before a level-up to qualify for Sniper
  or Slayer is a standard trick.
- 12 "special" perks come from quests and purchases: combat implants (Dermal +5%/+10% DR vs normal and
  explosive; Phoenix +5%/+10% vs fire/laser/plasma; each needs a Combat Armor and $5,000-$40,000, with the
  upgraded tier costing -1 CH), Vault City medical training, gecko skinning, and joke perks from drinking
  or a faulty auto-doc.

### 3.5 The notorious picks, and why they break things

| Pick | What it does to the maths |
|---|---|
| Gifted | 7 stat points (one-sixth of the entire starting budget) for -10% skills and -5 SP/level. With IN 7+ the skill loss is recovered within a few levels and by books |
| Fast Shot + Bonus Rate of Fire | A 5 AP single shot becomes 3 AP; a 6 AP burst becomes 4 AP. With 10 base AP + 2 Action Boy = 12 AP: four rifle shots or three bursts per turn |
| Sniper (Luck 10) | Every hit is a critical. Criticals roll on an effect table (see 4.3) that includes armor bypass and instant death, so late enemies' armor and HP stop mattering. Because the roll is on *any* ranged hit, losing aimed shots to Fast Shot costs little |
| Slayer | Same for melee/unarmed, at 2-3 AP per attack with Bonus HtH Attacks; often 4-6 guaranteed criticals a turn |
| Better Criticals | Shifts the effect roll +20, opening the top tier (instant-death results) on about 20% of criticals |
| Living Anatomy | Flat +5 after armor, per bullet that connects, which is disproportionate on burst weapons |

## 4. Combat mechanics

Turn-based on a hex grid, action-point budget per turn, same as Fallout 1.

### 4.1 Action point costs (typical)

| Action | AP |
|---|---|
| Move one hex | 1 |
| Punch/kick | 3 |
| Melee swing | 3-4 |
| Pistol / rifle single shot | 5 (4 for a few fast weapons) |
| Aimed shot | +1 |
| Burst | 5-6 |
| Reload | 2 |
| Open inventory | 4 (2 with Quick Pockets) |
| Unused AP | +1 AC each until next turn |

### 4.2 Hit chance

Ranged, per fallout.wiki (long-range rifle case):

`to-hit = (skill - 30) + (PE - 2) x 16 - 4 x distance_in_hexes - target AC` , -10% at night beyond 5 hexes,
-20% per missing point of minimum Strength, plus weapon-specific bonuses (e.g. accurate weapons +20%).
Shorter-ranged weapons use x 8 instead of x 16 for the Perception term. Melee: skill minus target AC.
Result is capped at 95%.

Aimed-shot penalties (and equal bonus to critical chance):

| Location | To-hit penalty / crit bonus |
|---|---|
| Eyes | 60 |
| Head | 40 |
| Groin | 30 |
| Arms | 30 `[UNVERIFIED]` |
| Legs | 20 `[UNVERIFIED]` |
| Torso | 0 |

So an aimed eye shot by a Luck 6 character has roughly a 66% critical chance before perks — aimed shots
are the non-Sniper way to play the critical game and why raw skill above 150% has value.

### 4.3 Criticals

1. A hit becomes a critical on a roll against critical chance (Luck + perks + aimed bonus), or via the
   Sniper/Slayer rule.
2. A second roll (1-100, +20 with Better Criticals, -30 with Heavy Handed) selects one of six effect
   tiers per body part and creature type: bands at 20 / 45 / 70 / 90 / 100 / over 100.
3. Each tier defines a damage multiplier (1.5x to 4x in practice) and flags: knockdown, knockout, crippled
   limb, blindness, **armor bypass** (target DT and DR cut to 20% of normal) and **instant death**.

Tier 6 is only reachable with Better Criticals. Because armor bypass appears in many head/eye results,
critical builds largely ignore the armor system that everyone else is fighting.

### 4.4 Damage, DT and DR

Per fallout.wiki:

`damage = (raw x DM - DT) - floor((DR + DRM) x (raw x DM - DT))`

- raw = weapon damage roll (+ bonuses); DM = ammo damage multiplier; DT = flat threshold of the armor for
  that damage type; DR = percentage resistance of the armor; DRM = ammo's resistance modifier.
- Each armor has separate DT/DR for normal, laser, fire, plasma, explosion, electrical and EMP.
- For bursts each bullet is resolved separately, so DT is subtracted from **every** bullet.

Ammo table (selected):

| Ammo | AC mod | DR mod | Damage mod |
|---|---|---|---|
| 10mm JHP | 0 | +25% | x2 |
| 10mm AP | 0 | -25% | x1/2 |
| 5mm JHP | 0 | +35% | x2 |
| 5mm AP | 0 | -35% | x1/2 |
| .44 Magnum JHP | 0 | +20% | x2 |
| .44 Magnum FMJ | 0 | -20% | x1 |
| .223 FMJ | -20 | -20% | x1 |
| 7.62mm | -5 | -10% | x1 |
| 14mm AP | 0 | -50% | x1/2 |
| 4.7mm caseless | -5 | -10% | x3/2 |
| 2mm EC (Gauss) | -30 | -20% | x3/2 |
| 12 ga. shells | -10 | 0 | x1 |
| Explosive rocket | 0 | -25% | x1 |
| Rocket AP | -15 | -50% | x1 |

### 4.5 The AP ammo problem (worked example)

The multiplier is applied before the threshold. Take a raw roll of 10 with 10mm ammo:

| Target armor (normal DT / DR) | JHP (x2, +25% DR) | AP (x1/2, -25% DR) |
|---|---|---|
| Leather Armor (2 / 25%) | 20 - 2 = 18; DR 50% -> **9** | 5 - 2 = 3; DR 0% -> **3** |
| Metal Armor (4 / 30%) | 16; DR 55% -> **8** | 1; DR 5% -> **1** |
| Combat Armor (5 / 40%) | 15; DR 65% -> **6** | 0 -> **0** |
| Power Armor (12 / 40%) | 8; DR 65% -> **3** | 0 -> **0** |

"Armor-piercing" rounds are worse against every armor in the game, and worst against heavy armor, which
is the opposite of the intent. An NMA thread gives the same result with a 16-damage SMG burst round: zero
with AP against power armor, 7 with JHP. The halving was clearly meant to trade damage for penetration,
but a x1/2 multiplier before a flat threshold can never win. Consequences:

- The correct play is "always JHP", and the only good rounds for hard targets are those with x1 or better
  multipliers *and* negative DR modifiers (.223 FMJ, 2mm EC, 4.7mm caseless).
- Miniguns (7-11 or 10-14 raw per bullet, 5mm ammo) are nearly useless against late-game armor because DT
  eats each bullet; the Bozar (25-35 per bullet, .223) and Gauss weapons do the real work.
- Enemies obey the same maths, so in power armor most ballistic enemies do zero to the player, while
  energy weapons and criticals still kill. Late difficulty becomes binary.
- Fan fixes (Glovz's damage formula, "Yet Another Ammo Mod", later "vanilla+" ammo mods, selectable via
  the sfall engine extender) all reorder the calculation or rebalance the modifiers.

## 5. Gear tiers

### 5.1 Armor

Values from fallout.wiki. "Where" is general knowledge and partly `[UNVERIFIED]`.

| Tier | Armor | AC | Normal DT/DR | Laser | Plasma | Explosion | Weight | Value | Typical first access |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Robes | 5 | 0 / 20% | 0 / 25% | 0 / 10% | 0 / 20% | 10 | 90 | Start region |
| 1 | Leather Jacket | 8 | 0 / 20% | 0 / 20% | 0 / 10% | 0 / 20% | 5 | 250 | Klamath |
| 1 | Leather Armor | 15 | 2 / 25% | 0 / 20% | 0 / 10% | 0 / 20% | 8 | 700 | Klamath / Den |
| 1 | Leather Armor Mk II | 20 | 3 / 25% | 1 / 20% | 1 / 10% | 1 / 25% | 10 | 1,000 | Mid towns |
| 2 | Metal Armor | 10 | 4 / 30% | 6 / 75% | 4 / 20% | 4 / 25% | 35 | 1,100 | Den / Modoc / Vault City |
| 2 | Metal Armor Mk II | 15 | 4 / 35% | 7 / 80% | 4 / 25% | 4 / 30% | 35 | 1,900 | Vault City / New Reno |
| 2 | Tesla Armor | 15 | 4 / 20% | 19 / 90% | 10 / 80% | 4 / 20% | 35 | 4,500 | Late shops |
| 3 | Combat Armor | 20 | 5 / 40% | 8 / 60% | 4 / 50% | 6 / 40% | 20 | 6,500 | NCR / San Francisco shops |
| 3 | Combat Armor Mk II | 25 | 6 / 40% | 9 / 65% | 5 / 50% | 9 / 45% | 25 | 8,000 | San Francisco |
| 3 | Brotherhood Armor | 20 | 8 / 40% | 8 / 70% | 7 / 60% | 8 / 40% | 25 | 4,800 | San Francisco |
| 4 | Power Armor | 25 | 12 / 40% | 18 / 80% | 10 / 40% | 20 / 50% | 42 | 12,500 | Late-game base / faction reward |
| 4 | Hardened Power Armor | 25 | 13 / 50% | 19 / 90% | 13 / 50% | 20 / 60% | 50 | 15,000 | Upgrade service, San Francisco |
| 5 | Advanced Power Armor | 30 | 15 / 55% | 19 / 90% | 15 / 60% | 20 / 65% | 45 | 20,000 | **Navarro locker** |
| 5 | Advanced Power Armor Mk II | 35 | 18 / 60% | 19 / 90% | 18 / 60% | 20 / 70% | 50 | 25,000 | Final area |

Power armors also grant hidden perks (+3 or +4 Strength and +30% to +75% radiation resistance).

The jump from tier 1 to tier 5 is the whole game's survivability curve: a 10mm pistol hit (5-12 raw, JHP)
does up to 11 to leather armor and at most 4 to Advanced Power Armor.

### 5.2 Weapons

| Tier | Weapon | Skill | Damage | AP | Range | Ammo | Min ST | Value |
|---|---|---|---|---|---|---|---|---|
| 0 | Spear | Melee | 3-10 | 4 | 2 | — | 4 | 80 |
| 0 | Sharpened Spear | Melee | 4-12 | 4 | 2 | — | 4 | 100 |
| 1 | 10mm Pistol | Small | 5-12 | 5 | 25 | 10mm | 3 | 250 |
| 1 | Hunting Rifle | Small | 8-20 | 5 | 40 | .223 | 5 | 1,000 |
| 2 | Desert Eagle .44 | Small | 10-16 | 5 | 25 | .44 | 5 | 800 |
| 2 | 10mm SMG | Small | 5-12 (burst) | 5 | 25 | 10mm | 4 | 1,000 |
| 2 | Assault Rifle | Small | 8-16 | 5 | 45 | 5mm | 5 | 1,300 |
| 2 | Scoped Hunting Rifle | Small | 8-20 | 5 | 40 | .223 | 5 | 1,500 |
| 3 | Combat Shotgun | Small | 15-25 | 5 | 22 | 12 ga | 5 | 2,750 |
| 3 | FN FAL | Small | 9-18 | 5 | 35 | 7.62mm | 5 | 1,500 |
| 3 | Sniper Rifle | Small | 14-34 | 6 | 50 | .223 | 5 | 2,200 |
| 3 | .223 Pistol | Small | 20-30 | 5 | 30 | .223 | 5 | 3,500 |
| 3 | H&K P90c | Small | 12-16 | 4 | 30 | 10mm | 4 | 2,500 |
| 3 | Pancor Jackhammer | Small | 18-29 | 5 | 35 | 12 ga | 5 | 5,500 |
| 3 | Plasma Rifle | Energy | 30-65 | 5 | 25 | MFC | 6 | 4,000 |
| 3 | Laser Rifle | Energy | 25-50 | 5 | 45 | MFC | 6 | 5,000 |
| 3 | Minigun / Avenger | Big | 7-11 / 10-14 per bullet | 6 | 35 / 40 | 5mm | 7 | 3,800 / 5,500 |
| 3 | Flamer | Big | 45-90 | 6 | 5 | Fuel | 6 | 2,000 |
| 3 | Rocket Launcher | Big | 35-100 | 6 | 40 | Rockets | 6 | 2,300 |
| 4 | Bozar | Big | 25-35 per bullet (burst only) | 6 | 35 | .223 | 6 | 5,250 |
| 4 | Turbo Plasma Rifle | Energy | 35-70 | 5 | 35 | MFC | 6 | 10,000 |
| 4 | Gatling Laser | Energy | 20-40 per beam | 6 | 40 | MFC | 6 | 7,500 |
| 4 | Solar Scorcher | Energy | 20-60 | 4 | 20 | Sunlight | 3 | 2,000 |
| 5 | PPK12 Gauss Pistol | Small | 22-32 | 4 | 50 | 2mm EC | 4 | 5,250 |
| 5 | M72 Gauss Rifle | Small | 32-43 | 5 | 50 | 2mm EC | 6 | 8,250 |
| 5 | YK32 Pulse Pistol | Energy | 32-46 (electrical) | 4 | 15 | SEC | 3 | 12,500 |
| 5 | YK42B Pulse Rifle | Energy | 54-78 (electrical) | 5 | 30 | MFC | 9 | 17,500 |
| 5 | Vindicator Minigun | Big | 14-19 per bullet | 6 | 30 | 4.7mm | 7 | 15,250 |
| M | Super Sledge | Melee | 18-36 | 3 | 2 | — | 5 | 3,750 |
| M | Ripper | Melee | 15-32 | 4 | 1 | SEC | 4 | 900 |
| M | Power Fist / Mega Power Fist | Unarmed | 12-24 / 20-40 | 3 | 1 | SEC | 1 | 2,200 |
| S | Alien Blaster | Energy | 30-90 | 4 | 10 | SEC | 2 | 10,000 |

Observations:

- **Small Guns has no ceiling.** The best single-shot weapon in the game (Gauss rifle: range 50, ammo
  with x1.5 damage and -20% DR) uses the same skill as the starting pistol. Energy Weapons and Big Guns
  are parallel tracks that start around the game's midpoint and do not end higher. There is no reason to
  switch skill families, so most optimal builds never do.
- **The Bozar is misfiled** as a Big Gun but is the best burst weapon; with Fast Shot + Bonus Rate of Fire
  it fires three bursts a turn.
- **Energy weapons pay for themselves through damage type**, not numbers: electrical (pulse) and plasma
  resistances on late enemies are lower than their laser resistance (19 DT / 90% DR on power armors makes
  lasers nearly useless against the final faction).

### 5.3 The Navarro rush

What it is: the top-tier Advanced Power Armor sits in an unlocked locker in an enemy base that treats the
player as a recruit if they say so.

Route as documented in community guides:

1. Leave the starting village and walk south along the coast to San Francisco (the far end of the map).
   Outdoorsman is low, so several random encounters are likely; saving every few squares and reloading
   past lethal ones (especially elite patrols near the destination, described as "instant death" at low
   level) is assumed.
2. In San Francisco, take the quest that marks Navarro on the map.
3. At Navarro's outpost, claim to be a new recruit (a modest Speech/Charisma check), or kill the unarmed
   gatekeeper (74 HP).
4. Walk into the base, open the locker, wear the armor, walk out. Optional quests inside can push a
   new character to level 7-8, and a plasma rifle and other gear are available.

Why it matters for design: the game is non-linear by intent (nothing on the world map is gated) but its
itemisation assumes a linear route. A single piece of foreknowledge collapses the difficulty curve of
roughly the first two-thirds of the game. The community treats this as a beloved sequence break; it is
also a textbook case of the **open world plus linear gear ladder** problem. Note the gates that *were*
there are all soft and knowledge-based: map knowledge, one dialogue check, and tolerance for save-reload.

## 6. Economy

- **Currency and prices.** Barter is item-for-item with money as one more item. Sale prices depend on
  Barter skill, Charisma-driven reaction and perks (Master Trader: 25% off). Jorner: Charisma matters more
  than the Barter skill unless the skill is pushed far past 100%.
- **Merchant cash is the real limiter.** Shops restock stock and money every 2-4 days (patched) or 1-2
  weeks (v1.0). Players therefore trade loot for goods directly (stimpaks, ammo, books) rather than
  for cash.
- **Money stops mattering by mid-game.** Every armed enemy drops a sellable gun. Once the player has a
  car trunk to haul loot, income outstrips every sink except implants ($5,000-$40,000) and a few
  bribes. This is the stated reason the community guide calls Barter pointless.
- **Money makers and sinks**

| Item | Amount |
|---|---|
| Free the first companion's debt | $350 |
| Free the second companion from slavers | $1,000 |
| Car | $2,000 plus a part (or pay extra for the part) `[UNVERIFIED]` |
| Fuel regulator upgrade | $750 |
| Skill book (e.g. Guns and Bullets) | ~$425 |
| Day pass bribe, Vault City | $500 |
| Combat implants | $5,000 / $30,000 tiers (up to $7,000 / $40,000 with poor reaction) |
| Cattle-guard job | $1,000 minus $100 per dead animal |
| Slave run | ~$100 per captive, ~$1,000 per run |
| Selling a companion into slavery | ~$800-$1,300 |
| Debt-collection job | up to $2,000 |

- **Exploits**
  - *Barter-screen item dupe/dodge:* dropping items before a trade lets you receive goods without giving
    yours up (documented in Jorner's guide).
  - *Infinite ore sale:* one mining-town transaction can be repeated for unlimited money or XP.
  - *Stealing:* XP for consecutive successful steals rises 10, 20, 30... per item, so stealing and
    replanting items farms XP. With save-reload, any NPC's inventory is free. In Fallout 2 most shop stock
    lives in a container rather than on the shopkeeper, which blunts the Fallout 1 trick of pickpocketing
    a store empty `[UNVERIFIED]`. Getting caught can turn a whole town hostile, which without reloading
    makes Steal too risky to rely on.
  - *Gambling:* with a high skill, table games become a positive-expectation loop that can be repeated
    indefinitely for cash `[UNVERIFIED]`. Jorner notes at least one dice script ignores the skill entirely,
    and v1.0 had a dice game that paid no winnings (fixed in 1.02d). Either way the skill produces nothing
    but money, in a game where money is already abundant.
  - *Difficulty toggling* for skill checks and skill-cost thresholds (section 3.3).
  - *Stat chems before level-up* to meet perk requirements permanently.
  - *Permanent stat gain from a quest item* (a drug antidote) through a script bug.
- **Drugs** (Jet, Buffout, Psycho, Mentats) are a second economy: cheap, strong temporary stats with
  addiction as the cost. Jet's +AP is the strongest and its addiction the harshest (curable only via a
  late quest). The town of Redding's whole storyline is this mechanic turned into politics.

## 7. Structure: tutorial, early game, hubs

### 7.1 Temple of Trials

- Four small maps: giant ants, radscorpions, floor traps, one locked door (Lockpick), one door opened with
  explosives (Traps), and a final unarmed duel that can be bypassed by Speech (IN 4 and tagged Speech per
  Jorner, 600 XP), by stealing a key (600 XP), or fought (300 XP). 300 XP for finishing.
- Critical hits are disabled on the first game day, critical failures for the first five (Jorner).

Why it is disliked:

1. **It is mandatory and unskippable** on every new character, in a game built for replays.
2. **It tests the wrong skills.** The player has a spear and no gun. A character built around Small Guns,
   Energy Weapons, Speech or Science starts with 30-50% in Melee/Unarmed and whiffs repeatedly at ants.
   The game's first 20-30 minutes punish most of the builds its character creator encourages.
3. **It teaches little.** Dialogue, barter, the world map and ranged combat — the things that are actually
   distinctive — are absent. It teaches "attack adjacent enemy" and "use skill on door."
4. **It does not fit the fiction.** A stone temple with mechanical doors and military explosives owned by
   a tribal village; the series' own design notes call it "pretty implausible."
5. **It was imposed.** Tim Cain has said marketing required a tutorial-style opening map and that it did
   not fit the setting.

It does do one thing right: three resolutions for the final duel (fight, talk, steal) signal the game's
multi-solution quest design within the first half hour.

### 7.2 Early-game difficulty for non-combat builds

The stretch from the starting village through the first three towns is the game's real difficulty spike:

- No firearm at start. The first guns are a single-shot pipe rifle and, if bought, a 10mm pistol (250).
  Starting cash is negligible; stimpaks are too expensive to buy (Jorner advises skipping them early and
  buying 10mm ammo and leather armor first).
- Early quests are pest control: rats, geckos (golden geckos irradiate on hit), a dog pack (ten dogs
  attacking a herd you must protect), wolves, mantises.
- World-map encounters near the start scale partly by player level but include groups that outnumber a
  solo level-2 character. Low Outdoorsman means few can be avoided.
- A talker has few talking targets yet: the first hub's quests mostly want things killed or fetched. The
  big dialogue-driven hubs (Vault City, NCR, New Reno) are 5-15 hours in.
- The fix the game offers is the first companion (a melee fighter, $350) and then a second. This is why
  Charisma 4-6 is close to mandatory for non-combat characters, and why "solo diplomat" is the hardest
  legitimate build.
- Net effect: nearly every build tags one combat skill. A true pacifist/diplomat run is a challenge run,
  not a supported playstyle, despite the breadth of non-combat skills on the sheet.

### 7.3 Town-hub structure

The game is a chain of hubs with rising scale. Quest counts from fallout.wiki's quest index (the page was
truncated, so later hubs are not counted here):

| Hub | Role | Listed quests | Notes |
|---|---|---|---|
| Arroyo | Tutorial village | 8 | Start |
| Klamath | First town | 8 | Pest quests, first companion, car parts lead |
| The Den | Vice town | 14 | Slavers (title: Slaver), second companion, car |
| Modoc | Farm town | 12 | Peace-or-war quest with a hidden community; shotgun wedding |
| Vault City | First major polity | not counted | Citizenship gating; xenophobic; four ways in |
| Gecko | Ghoul reactor town | 6 | Reactor repair/optimise/sabotage drives two towns' endings |
| Broken Hills | Mining town | 8 | Human/mutant tension; third-tier companion |
| New Reno | Crime city | 15+ (truncated) | Four families, most reactive hub |
| Redding | Gold-mining town | not counted | Its allegiance is the prize of the mid-game |
| NCR | Expanding republic | 15 | Assassination contracts cross-link to New Reno |
| Vault 15 / Vault 13 | Dungeon-towns | not counted | Main quest objective sits here |
| San Francisco | End-game hub | not counted | Three factions, best shops |
| Navarro, military base, Sierra depot | Dungeons | 3 (Navarro) | High-tier loot |
| Final area | Ending | — | Can be completed largely by Speech/Science |

The main quest is short and almost linear ("find the item, then stop the people behind the abductions");
perhaps 80% of the content is optional hub quests `[UNVERIFIED estimate]`.

### 7.4 The interlinked quest web (Vault City – Gecko – NCR – New Reno – Redding)

This is the game's best structural idea: the towns want things from each other, and the player is the
only free agent.

| Link | Mechanism |
|---|---|
| Vault City <-> Gecko | Gecko's leaking reactor poisons Vault City's groundwater. Player can repair it (4,000-4,500 XP depending on method), repair **and optimise** it, or sabotage it (meltdown). Repair = truce; optimise = Vault City decides the plant is worth seizing and enslaves the ghouls (the "better" engineering outcome gives the worse ethical ending); sabotage or neglect = one town destroys or outlasts the other |
| NCR -> Vault City | NCR wants to annex Vault City and is covertly paying raiders (via a New Reno family) to harass it. Player can wipe out the raiders and deliver two pieces of evidence. Evidence delivered + specific NPCs alive = Vault City stays independent; partial = joins or is occupied by NCR |
| New Reno -> NCR | One crime family is NCR's proxy; another offers contracts to assassinate NCR officials. The same NPCs are quest-givers in one hub and targets in another |
| New Reno -> Redding | A family floods the mining town with an addictive drug to control its gold. Player can find a cure (requires work in Vault City and New Reno) |
| Vault City / NCR / New Reno -> Redding | All three want the gold. Who the player sells a mining component to, and whether the cure is delivered, decides whether Redding is annexed by Vault City, joins NCR, allies with New Reno, or empties |
| New Reno internal | Each family has a power counter starting at 100; quests shift counters; highest at the end rules the city (tie order fixed). At least eight distinct city endings, including "all four bosses dead" |
| Den <-> New Reno | Slavers supply one family's drug labs; the Den's ending depends on whether the slaver boss and a New Reno boss are alive |
| New Reno -> final faction | One family trades with the end-game enemy for energy weapons; witnessing the deal is an early glimpse of the antagonists |
| Broken Hills -> Gecko/Vault City | Uranium ore refinement ties the mining town's economy to the reactor chain `[UNVERIFIED]` |

What makes this work:

- **State is simple.** Outcomes are driven by a handful of flags (reactor fixed? optimised? evidence
  delivered? NPC alive?) and a few counters. The apparent complexity is combinatorial, not systemic.
- **Ending slides pay it off.** Each town gets a narrated outcome; Vault City alone has six.
- **Quests are entered from several sides.** The raider quest can be found from Vault City, from the
  raiders' base on the map, or from New Reno documents.

Where it fails: some endings are bugged or unreachable in the shipped game (the Gecko "alliance" ending
and a Mordino ending are flagged as bugged on fallout.wiki), and nothing in-game tells the player the
consequences of optimising the reactor — a deliberate trap that many players only learn from a wiki.

## 8. Reactivity mechanisms

### 8.1 Karma

A single signed integer starting at 0. Titles at +/-250, 500, 750, 1000 (Defender / Shield of Hope /
Guardian of the Wastes / Savior of the Damned; Betrayer / Sword of Despair / Scourge of the Wastes /
Demon Spawn). Effects: NPC reaction modifier, some dialogue gates, companion recruitment (several refuse
below roughly -100 or at "evil"; one leaves), and wanted posters at very low karma. Declining a cash
reward usually converts it to karma. Grave robbing: -5 karma each.

### 8.2 Town reputation

A separate integer per town.

| Level | Threshold |
|---|---|
| Idolized | +30 |
| Liked | +15 |
| Accepted | +1 |
| Neutral | 0 |
| Antipathy | -1 |
| Hated | -15 |
| Vilified | -30 |

Used for: quest availability (some quest-givers will not talk at Neutral or below with negative karma),
companion recruitment (one needs "Accepted" in his town; another refuses if you are Hated in his), shop
access, and floating-text barks. Quests in a town move that town's number, so a villain elsewhere can
still be a local hero — a cheap way to make reputation feel regional.

### 8.3 Special titles

| Title | How earned | Effects |
|---|---|---|
| Made Man | Finish a New Reno family's quest chain and accept the reward (needs IN above 4; either sex) | Family-specific shop stock and discounts, special services; the **other three families attack on sight**; dealers and barmen charge more; power armor (face hidden) conceals the status until someone talks to you; turning on your family removes it; a sequence trick lets you be made by nearly every family |
| Slaver | Join the Den slavers' guild; forehead tattoo | -25% reaction (up to -50%) from anti-slavery NPCs; NCR rangers hostile; two quests locked; slave runs unlocked; several companions refuse to join |
| Childkiller | Kill two children in combat (certain named children count double); companion kills and indirect kills do not count | -30 initial reaction from good **and** evil NPCs; several companions refuse; bounty hunters appear as world-map encounters in four level-scaled grades, from leather jackets and hunting rifles up to power armor and miniguns |
| Berserker | 25+ kills with at least twice as many "good" as "bad" victims, at bad karma | Good NPCs react worse; some companions refuse |
| Champion | Many "bad" kills at good karma, not a Childkiller | Good NPCs react better |
| Prizefighter | Win the boxing ladder in New Reno | +5% Unarmed, +5% damage resistance, local fame; local price mark-ups |
| Porn Star | Make a film at the New Reno studio (CH 9, or already locally famous) | Local fame and unique barks; one family matriarch refuses to speak, locking a quest; dealer mark-ups |
| Gigolo / Sexpert | Pass a hidden "performance" score check (derived from CH, EN, AG, ST and a perk) | Dialogue acknowledgement only |
| Married / Separated | Shotgun wedding in Modoc after sleeping with a farmer's son or daughter (same-sex marriage possible) | A near-useless spouse companion occupying a party slot; can be divorced, widowed or sold |
| Grave Digger | Dig up any grave | -5 karma per grave; a mark on the sheet |

Why these work better than the karma number:

- They are **specific and legible**: a noun on the character sheet earned by a memorable act.
- They are **cheap to implement**: one flag, checked in a dozen scripts.
- They have **material trade-offs** (Made Man: one family's perks for three families' hostility), unlike
  karma, which mostly just accumulates.
- They produce **stories players retell** — the porn-star/boxer/mobster triple in one city, bounty hunters
  for child killing — far out of proportion to their cost.

Weak points: effects are concentrated in one or two towns (mostly New Reno), and several titles (Gigolo,
Champion, Grave Digger) do almost nothing.

### 8.4 Low-Intelligence dialogue

With Intelligence below 4 the player's dialogue options are replaced by grunts and malapropisms and NPCs
respond accordingly. Mechanical effects documented in Jorner's guide:

- Most quest-givers will not give quests; computers need IN 4; several companions will not join.
- Some content opens up instead: a gate guard waves you through with a free day pass; a fellow dim NPC
  converses with you fluently; some characters take pity; some swindle you (a 10% "service charge").
- Certain made-man/title perks interact (a New Reno dealer reacts differently to famous but dim players).
- The guide rates the "stupid" build as viable only as a gun character and advises against stupid melee.

Design reading: it is an alternate script for roughly every major NPC, i.e. a very expensive joke, but it
is one of the most cited proofs that "the game notices who you are." It is also toggleable mid-game with
Mentats (to pass a check) or by drugging yourself down, which players use deliberately.

## 9. Companions

Limit = CH / 2 rounded down; Magnetic Personality +1 (so 5 at CH 10). XP is not shared with or reduced by
companions. Each companion has fixed level-up stages that trigger by chance when the player levels.

| Companion | Where | Requirement | Weapons | Final HP | Assessment |
|---|---|---|---|---|---|
| Sulik | First town | Pay $350 debt or do a rescue; refuses Slaver/Childkiller/Berserker/karma < -100 | Melee 110%, SMGs (Small Guns 77%) | 146 | The early-game lifeline; better with a hammer than an SMG (bursts hit friends) |
| Vic | The Den (via main quest) | $1,000 or kill the slavers | Small Guns 98%, Energy 129%, Repair 106% | 132 | Mediocre early, good late with energy rifles; free Repair skill |
| Cassidy | Vault City | Not Slaver/Childkiller, IN 4+, karma >= -100 | Small Guns 127%, Energy 116%; rifles | 128 | Widely rated the best: accurate, single-shot weapons, wears power armor |
| Lenny | Gecko | "Accepted" in Gecko, positive karma | Small Guns 70%, Doctor 106% | 206 | Weak fighter; walking Doctor skill; cannot wear armor; barred from Vault City |
| Marcus | Broken Hills | Two local quests, positive karma | Big Guns 145%, Energy 100% | 205 | Huge damage, cannot wear armor, minigun bursts kill allies; barred from Vault City |
| Myron | New Reno outskirts | Ask | Energy 83%, Science 109% | 122 | Poor fighter; makes drugs and antidotes; Science on tap |
| Skynet | Sierra depot | Build it a body (Science) | Small Guns 122% (with the right brain) | 210 | Strong but late; quality depends on a skill check at creation |
| Goris | Vault 13 | Ask | Unarmed 100% | 187 | Strong melee; slow "cloak" animation every fight; can be lost to a plot event |
| K-9 / Robodog | Navarro / NCR | Repair / quest | Unarmed | 137 | Tanky melee pets |
| Dogmeat | Special encounter | Luck to find it | Unarmed 101% | 168 | Nostalgia pick; solid |
| Miria / Davin | Modoc | Marriage | Almost none | 35 | "Absolutely useless" (Jorner); never level |
| Pariah dog | Special encounter | Fail a Luck check | Never fights | 750 | A curse: sets Luck to 1 and adds Jinxed while it lives |

Combat control menu: disposition presets (berserk/aggressive/defensive/coward/custom), and under custom:
burst discipline, flee threshold, weapon preference, distance (stay close / charge / snipe / on your own /
hold), target priority (whoever attacks me / strongest / weakest / closest), chem use. Plus "use best
weapon/armor", trade, heal, wait.

What improved over Fallout 1: armor, levelling, orders, and the push command. What did not:

- Burst fire still ignores friendlies in the cone; "be absolutely sure you won't hit me" helps but does
  not solve it. Players strip burst weapons from companions.
- Companions follow the player into certain traps and force fields and die; pathing in doors is still poor.
- Non-humans cannot change armor, so they fall off against energy weapons.
- Late-game enemies in tier-5 armor are immune to most companion damage (same DT maths as the player).
- Party size trivialises early and mid-game ballistic fights, then becomes a liability in the final areas.

## 10. Random and special encounters

Per-tile encounter chance bands on the world map (from the game's data as documented on fallout.wiki):

| Band | Chance per check |
|---|---|
| Forced | 100% |
| Frequent | 38% |
| Common | 22% |
| Uncommon | 12% |
| Rare | 4% |
| None | 0% |

- Tables are regional and partly level-gated (e.g. some thug groups appear only above level 6).
- Avoidance: an Outdoorsman-based roll, capped at 95%, asks whether to engage. Successful avoidance grants
  100 XP + the zone's difficulty value (0-70) — a rare case of XP for *not* fighting.
- Travelling by car reduces the number of checks per trip because trips are shorter.
- Encounter types: wildlife; raiders, slavers, highwaymen; caravans (which can be joined for pay and
  guaranteed fights); three-way fights between groups (free loot and XP if you stand back); and, near the
  end-game coast, elite patrols that one-shot low-level characters — the only "gate" on the Navarro rush.

Special encounters (16 listed), found by chance (higher with Luck and the Explorer perk; exact formula
`[UNVERIFIED]`):

| Encounter | Min level | Content |
|---|---|---|
| Diner of nostalgia | 1 | Cameos from the first game; the dog companion |
| Peasants vs a rat | 1 | Comedy boss fight (a film parody) |
| Crashed shuttle | 6 | Three dead crewmen with unique healing items (TV parody) |
| Crashed whale and flowerpot | 6 | Novel parody |
| Exploding herd | 6 | Animals that detonate on contact |
| Rusted soldier | 6 | Oil him for 150 micro fusion cells (film parody) |
| Toxic dump | 6 | Radiation, no loot |
| Time portal | 8 | Travel back and cause the first game's inciting incident; reward: an item and, in effect, a perk-like bonus |
| Bridge-keeper | 10 | Riddle parody; unique robes equal to Combat Armor at 10 lbs |
| Knights seeking a holy grenade | 10 | Film parody |
| Giant stone head | 10 | Karma-gated reward |
| Mystery-weapon trader | 10 | Blind purchase gamble |
| Lone surviving dog | 10 | The cursed companion |
| Ambush of a farming family | 10 | Scripted look at the main villain |

Half of these are direct pop-culture parodies. They are the most-loved and the most-criticised content in
the game at once: memorable, optional, and tonally nothing like the first game's handful. Later entries in
the series made this content opt-in behind a trait, which is the right lesson.

## 11. Length and pacing

- Commonly cited play time: roughly 30-40 hours for a focused run and 60-80+ for most side content
  `[UNVERIFIED]`; the first game is commonly cited at 15-25 hours `[UNVERIFIED]`. A knowledgeable player
  can finish in well under an hour by sequence-breaking straight to the end-game.
- Pacing shape: slow, punishing start (tutorial + three small towns, 5-10 hours) -> broad, excellent
  middle (Vault City, Gecko, New Reno, NCR, Redding, Broken Hills; 20-40 hours, any order) -> thin, combat-
  heavy end (San Francisco is visibly less finished; two large dungeons; a final area that is mostly
  corridors).
- The car arrives at about the point the map opens up, cutting travel time and adding a trunk. It can be
  stolen in New Reno (a quest to get it back), runs on energy cells, and has three or four upgrades
  (fuel efficiency, speed, trunk size) scattered across towns as small rewards. It is "largely scripted"
  (fallout.wiki) rather than a system, and was a major source of launch bugs.
- With no time limit, nothing pushes the player along. The dream-message urgency is fiction only. This is
  the correct call for a game this size — the first game's timer was patched out for the same reason — but
  it makes the main plot feel inert for the middle 30 hours.
- Level curve vs content: because XP needed grows quadratically while quest XP rewards grow with town
  tier, a completionist reaches level 24 (Sniper/Slayer) around the last third `[UNVERIFIED]`, exactly when
  enemy armor makes non-critical damage stop working. The capstones are effectively *required* by the
  armor curve, which is why "Luck 8-10 critical build" is the default advice.

## 12. Bugs, patches and the community's role

Launch state (v1.0, October 1998):

- The car's trunk could detach and be lost, or the car could vanish, until patch 1.02d — almost four
  months after release.
- Companions could turn hostile unprovoked; several quests could lock up; one town's population could
  attack on entry; a gambling game paid nothing; a trainer gave unlimited free skill.
- Save games could bloat or corrupt on maps with too many items `[UNVERIFIED]`.
- Several ending slides and at least one perk pair did nothing.

| Patch | Date | Notes |
|---|---|---|
| 1.02d (official, US) | 11 Feb 1999 | Fixes car/trunk, hostile companions, quest lock-ups; nerfs skill perks; **invalidates v1.0 saves**; separate UK patch; none for the low-violence edition |
| killap's Unofficial Patch (final 1.02.31) | 2000s to July 2014 | Fixes 800+ bugs left after 1.02d; no new content |
| killap's Restoration Project (2.3.3) | July 2014 | Unofficial Patch plus cut content rebuilt from design notes and leftover files: new locations (an environmental research facility, an abbey, a tribal village tied to the first companion's missing sister, a village outside Vault City, more of the Den and San Francisco) and quests `[list partly UNVERIFIED]` |
| sfall (engine extender) | ongoing | Modern resolutions, bug fixes in the executable, optional damage-formula replacements, scripting hooks |
| "Unofficial Patch updated" / "Restoration Project updated" (BGforge) | ongoing | Community-maintained continuations of killap's work |

Takeaways from the patch history:

- A patch that breaks saves in a 60-hour RPG is itself a design failure; many players never applied it.
- The community has kept the game playable and has effectively finished it. That was possible because the
  game is data-driven (plain-text world-map tables, per-NPC scripts, item prototypes), and because the
  scale left a lot of half-built content worth restoring.
- The existence of 800+ post-patch fixes is the clearest quantitative statement of what the 12-month
  schedule cost.

## 13. Balance assessment

### 13.1 Dominant builds

| Build | Core | Why it wins |
|---|---|---|
| Sniper gunfighter (the default) | Gifted + Fast Shot or Small Frame/Finesse; AG 9-10, PE 7-8, LK 8-10, IN 7, EN 4, ST 5; tag Small Guns, Speech, Lockpick; Awareness, Quick Pockets, Better Criticals, Living Anatomy/Action Boy, Bonus Rate of Fire, Action Boy, Sniper | One weapon skill for the whole game, the best perk at 15 and the best at 24, criticals that bypass armor |
| Burst variant | Same, with Fast Shot and a Bozar or Gauss pistol | Three or four attacks per turn; no need for aimed shots once Sniper is in |
| Slayer brawler | ST 5 (+4 from armor to reach 8 with a stat boost), AG 9-10; tag Unarmed/Melee; Bonus Move, Bonus HtH Attacks, Slayer | 4-6 guaranteed criticals a turn at 2-3 AP each; weak until level 15-24 |
| Party leader | CH 6-8, Magnetic Personality, give followers the best rifles | Trivialises early and mid-game; fades in the end-game |

All of these put **Intelligence 6-7+ and Agility 8+** as non-negotiable and Endurance at 4. The "real"
character space is much smaller than the sheet suggests.

### 13.2 Broken strategies

| Strategy | Effect |
|---|---|
| Navarro rush | Tier-5 armor at level 1-3; most of the game cannot hurt you |
| Sniper with Luck 10 | 100% critical rate; armor system and HP bloat bypassed |
| Fast Shot + Bonus Rate of Fire + Action Boy x2 | Up to four shots or three bursts per turn |
| Always-JHP | AP ammo is a trap (formula bug) |
| Book-buying | Five skills to ~91% for money only |
| Chems before level-up | Permanent access to perks you do not qualify for |
| Difficulty toggling | +20% to non-combat skills for one check |
| Steal with save-reload | Free loot and scaling XP |
| Repeatable ore sale; barter drop trick; high-skill gambling | Unlimited money |
| Super-stimpak assassination | Deferred damage kills quest NPCs without combat, hostility or (for children) the title |
| Selling companions / spouses | Party members as currency |

### 13.3 Useless or trap options

- **Skills:** Throwing, Gambling, Barter (near-zero return); Sneak (too little content supports it);
  First Aid and Outdoorsman (books); Big Guns as a *primary* (arrives late, eats ammo, its best weapon is
  better used by the Sniper build's logic anyway).
- **Traits:** Skilled, Bruiser, Kamikaze, Fast Metabolism, both Chem traits, Bloody Mess (cosmetic).
- **Perks:** Swift Learner, Here and Now, Educated, Survivalist, Heave Ho!, Pack Rat/Strong Back once the
  car exists, the two possibly non-functional Charisma perks, and roughly 20 skill-bonus perks that give
  +10-20% in a system where skill points are cheap.
- **Stats:** Endurance above 4; Strength above 5-6 once power armor adds +3/+4; Charisma is either 1-2
  (solo) or 6+ (party), never in between.

Root causes worth naming:

1. **One currency is much cheaper than the others.** Skill points are abundant (5 + 2 x IN per level, plus
   books and trainers, across 25-35 levels), perks are scarce (8-11 in a normal run). Anything that trades
   perks for skill points is a trap; anything that trades skill points for stats (Gifted) is a steal.
2. **18 skills, but content for about 8.** Speech, Lockpick, one weapon skill, Doctor, Science and Repair
   carry nearly every check. The rest have a handful of uses each.
3. **Multiplicative end-state perks.** "Every hit is a critical" and "-1 AP per attack" are multipliers on
   an economy tuned around additive bonuses.
4. **Flat thresholds vs many small hits.** DT makes burst and low-damage weapons collapse against heavy
   armor; combined with the ammo bug, half the arsenal is obsolete in the last third.
5. **Open map, linear loot.** Tiers are placed geographically, not gated mechanically.

### 13.4 What the design gets right

- **Reactivity by flags and titles.** Cheap booleans plus ending slides create the feeling of a world that
  remembers. Per-town reputation makes consequences local and readable.
- **Hubs that want things from each other.** The Vault City–Gecko–NCR–New Reno–Redding web gives side
  quests stakes without a single cutscene, and gives the player real political leverage.
- **Multi-solution quests as the norm.** Fight / talk / sneak / steal / repair options on most significant
  quests, with XP differentiated by method (e.g. the reactor repair: 4,000 manual, 4,250 by persuasion,
  4,500 by robot).
- **Character sheet as dialogue input.** Stat, skill, sex, title and Intelligence checks in conversation;
  low-INT as a full alternate script.
- **Companions as characters with rules** — recruitment conditions tied to karma and titles, town-specific
  prejudice against them, banter — and a control menu that later squad RPGs copied.
- **Quality-of-life fixes that mattered** (push NPC, take-all, companion inventory, the car's trunk).
- **Freedom is real.** Sequence breaks, killing anyone, finishing the game by talking — the game rarely
  says no.
- **No timer** at this scale.

### 13.5 Where scale hurt quality

- **Bugs.** 800+ fixed by fans after the final official patch; a save-breaking official patch; broken
  endings; a flagship feature (the car) unreliable for four months.
- **Tone.** Parallel authorship without a "genre overseer" (Avellone's phrase) produced a game where a
  grim slaver town, a 1930s-gangster city, kung-fu San Francisco, talking deathclaws and a Monty Python
  bridge share a map. Individually liked; collectively the reason many fans of the first game consider
  the sequel's world less coherent.
- **Uneven hubs.** New Reno and Vault City are dense and reactive; San Francisco, the military base and
  the last dungeon are thin, combat-only and visibly rushed. The best content is in the middle; the game
  ends on its weakest material.
- **Unscaled rules.** A level-21, 20-hour ruleset stretched over 60 hours and level 30+ without re-tuning:
  skill-point glut, perk traps, capstones that break combat, an armor curve that invalidates companions
  and half the weapons.
- **Slow start.** A mandated tutorial plus three small low-level towns means the game's best feature (the
  political hub web) starts 8-10 hours in. Many players bounce off before then.
- **Cut content.** Enough was left half-built to fuel a decade-long fan restoration.
- **Thin main plot.** The mid-game has no forward pressure, and the antagonists barely appear until the
  end; the world is the star and the story is an afterthought.

## Design Takeaways

- **Build a web, not a list.** Give each settlement one thing it wants from two neighbours and let quests
  in town A set flags read by town B and by the ending. Five towns with ten shared flags beat fifteen
  isolated towns. Budget for it explicitly: it is the highest value-per-cost feature in this game.
- **Use named titles, not just meters.** A short list of earned, visible status flags with concrete
  trade-offs ("ally of X, enemy of Y and Z") gives more felt reactivity than a global morality number.
  Every title should change at least prices, access and combat hostility somewhere, in more than one town.
- **Keep per-settlement reputation** with a small number of thresholds (their seven bands at 0/±1/±15/±30
  are a fine template) and make it gate services, not just barks.
- **Do not ship a skill unless content needs it at least once per hub.** If we want 12+ skills, write a
  content matrix (skill x hub) before production; cut or merge any row with fewer than, say, five uses.
  Money-only skills (gambling, barter) should be perks or mini-systems, not skill lines.
- **Price the currencies honestly.** If perks are scarce and skill points are plentiful, never offer trades
  between them at face value. Audit every trait as "what does this cost in the scarce currency?" Aim for
  at least half of the traits being seriously chosen.
- **No "always" capstones.** Avoid perks that turn a probability into a certainty or cut the core action
  cost by a flat point with no ceiling. Prefer capstones that add options (a new move, a new reaction)
  over multipliers.
- **Do the armor maths on paper for every weapon class at every tier.** Flat threshold + percentage
  resistance + per-bullet resolution needs a spreadsheet, and ammo modifiers must be tested in the actual
  order of operations. If "armor-piercing" exists, it must beat standard ammo against armor, by design
  test, before content lock.
- **Decide deliberately how the open map meets the gear ladder.** Either gate top-tier gear behind
  capability (skill, quest state, a fight you cannot bluff), or embrace sequence breaking and make the
  world respond (the armor gets you recognised, hunted, or refused service). An unlocked locker is neither.
- **The tutorial must exercise the build the player just made.** Offer talk/sneak/shoot/fix routes from
  minute one, make it skippable on replays, and never let a mandate from outside the team dictate the
  first hour. The first hour should showcase what is distinctive (choices and reactions), not basic attacks.
- **Protect the early game for non-combat characters.** Give talkers and tinkerers something to talk to
  and fix in the first settlement, and an early ally. If a pacifist is not viable, do not present
  eighteen equal-looking skills at creation.
- **Companions: keep recruitment conditions and behaviour settings; fix friendly fire and scaling.**
  Tie party size to a social stat only if that stat has other strong uses; make sure companions remain
  relevant against end-game defences, or say clearly that the finale is solo.
- **Alternate-script reactivity (the low-INT idea) is worth one big, visible instance.** Pick one
  character-sheet extreme and rewrite the dialogue around it; players will cite it for decades. Do not
  try to do it for every stat.
- **Put jokes and references behind an opt-in, or keep them in-fiction.** Adopt the first game's rule:
  no joke that needs outside knowledge to make sense. One tone owner signs off on every area.
- **Scope to the schedule, and finish the ending first.** This game's middle is superb and its end is
  thin because areas were built in travel order. Build the finale and the first hour early; let the
  optional middle absorb cuts.
- **Never break saves in a patch; plan for moddable data.** Text-table world data and per-NPC scripts are
  why this game is still playable. Treat mod-friendliness as insurance.
- **Re-tune rules when the game doubles in length.** XP curve, perk cadence, skill-point income and level
  cap are a function of content volume; a sequel twice the size needs a new curve, not a higher cap.
- **No hard global timer; use local, visible clocks** (a town that deteriorates if a quest is ignored)
  to keep urgency without punishing exploration.

## Sources

Consulted directly in this research pass:

- https://fallout.wiki/wiki/Fallout_2 — development timeline, team changes, changes from Fallout 1, reception
- https://fallout.wiki/wiki/Fallout_2_perks — perk list, levels, requirements
- https://fallout.wiki/wiki/Fallout_2_skills — starting formulas, cost bands, tag rules, difficulty effects
- https://fallout.wiki/wiki/Fallout_2_traits — trait list
- https://fallout.wiki/wiki/Fallout_2_combat — hit and damage formulas
- https://fallout.wiki/wiki/Fallout_2_ammunition — ammo modifiers
- https://fallout.wiki/wiki/Fallout_2_armor_and_clothing — armor table
- https://fallout.wiki/wiki/Fallout_2_weapons — weapon table
- https://fallout.wiki/wiki/Fallout_2_companions — companions, party limit, combat control
- https://fallout.wiki/wiki/Fallout_2_reputations — town reputation thresholds
- https://fallout.wiki/wiki/Karma_(Fallout_2) — karma titles
- https://fallout.wiki/wiki/Made_Man , https://fallout.wiki/wiki/Slaver_(reputation) ,
  https://fallout.wiki/wiki/Childkiller , https://fallout.wiki/wiki/Porn_Star ,
  https://fallout.wiki/wiki/Prizefighter , https://fallout.wiki/wiki/Gigolo — special titles
- https://fallout.wiki/wiki/Fallout_2_endings — per-town ending conditions
- https://fallout.wiki/wiki/Fallout_2_quests — quest index (truncated)
- https://fallout.wiki/wiki/Fallout_2_random_encounters — encounter chance bands, avoidance
- https://fallout.wiki/wiki/Fallout_2_special_encounters — special encounter list
- https://fallout.wiki/wiki/Temple_of_Trials — layout, XP, Tim Cain's comment on the marketing mandate
- https://fallout.wiki/wiki/Highwayman — car
- https://fallout.wiki/wiki/Fallout_2_patches — 1.02d readme summary
- https://twinysam.github.io/fallout2guide — mirror of Per Jorner, "The Nearly Ultimate Fallout 2 Guide" v1.3 (character design, early areas, Vault City/Gecko; first ~300k characters read)
- https://f2rp.bgforge.net — Restoration Project walkthrough addendum
- https://bgforge.net/docs/fallout/unofficial-patch-updated — community continuation of killap's patch
- https://www.ludo.guide/guide/fallout-2/derived-statistics — derived stat formulas (from the manual)
- https://fodev.net/files/fo2/criticals.html — critical effect table mechanics
- https://www.alteredgamer.com/fallout-2/80518-the-navarro-run-power-armor-exploit — Navarro rush
- http://www.gamebanshee.com/k4c6k — "The Complete History of Fallout" (Avellone and Cain quotes on Fallout 2)
- https://80.lv/articles/fallout-creator-explained-why-he-left-fallout-2 — Tim Cain's reasons for leaving
- https://www.pcgamer.com/original-fallout-co-creator-finally-explains-what-made-him-leave-the-sequel-i-made-an-ip-from-scratch-that-nobody-believed-in-except-the-team-and-my-reward-for-that-was-more-crunch (headline/lede only)
- https://en.wikipedia.org/wiki/Fallout_2 — reception, sales, awards

Seen only as search-result summaries (not opened; pages blocked or search budget exhausted):

- https://nma-fallout.com/threads/fix-ap-ammo-bug.159124 — No Mutants Allowed thread on the AP ammo bug (403 on fetch)
- https://nma-fallout.com/threads/extra-bullets-after-weapons-mod-ap-and-jhp-damage-question.176206
- https://nma-fallout.com/threads/yet-another-ammo-mod-yaam-feedback-thread.192202
- https://forums.bgforge.net/viewtopic.php?p=1231 — Glovz formula discussion
- https://www.gamebanshee.com/news/111901-fallout-2-restoration-project-22-a-unofficial-patch-released.html
- https://rpgcodex.net/article.php?id=6020 — Avellone interview (Edge) summary
- Nukapedia (fallout.fandom.com) pages returned HTTP 402 and could not be read; StrategyWiki and TweakTown returned 403.
