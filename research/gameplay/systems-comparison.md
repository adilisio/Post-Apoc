# Cross-Game Systems Comparison: Fallout 1, 2, 3, New Vegas, 4, 76

Scope: side-by-side comparison of the core RPG systems of the six mainline games and the design reasoning
behind each change. Per-game detail lives in the individual game documents; this file is about the *deltas*.

Abbreviations: FO1 (1997, Interplay), FO2 (1998, Black Isle), FO3 (2008, Bethesda), FNV (2010, Obsidian),
FO4 (2015, Bethesda), FO76 (2018, Bethesda; live service, heavily patched).

Verification note: the web-search budget for this session ran out part-way through. Figures confirmed against a
source this session are stated plainly. Figures written from general knowledge of the games and not re-checked
this session carry `[UNVERIFIED]`. Treat those as "very probably right, check before quoting".

## Quick Reference

- The series is three different games wearing one costume: a **turn-based isometric stat RPG** (FO1/2), a
  **first-person hybrid RPG-shooter** (FO3/FNV), and a **looter-shooter with RPG trim** (FO4/76).
- SPECIAL has survived every game, but its job changed: in FO1/2 it *is* your character (40 points, almost
  never changes); in FO3/FNV it is a modest modifier under skills; in FO4 it is the perk-tree gate (28 points,
  raised freely); in FO76 it is a 56-point *equip budget* for perk cards.
- Skills shrank 18 → 13 → 13 → 0. FO4 deleted skills and folded their effects into perk ranks.
- Perk cadence is the single best predictor of build identity: every 3 levels (FO1/2), every level (FO3),
  every 2 levels (FNV), every level with no cap (FO4), swappable cards (FO76).
- Level caps went 21 → 99 → 20 (30 with DLC) → 30 (50 with DLC) → none → none. Uncapped levelling ends build
  identity: an FO4 character can own everything at level 286.
- Armor model: flat threshold + percentage (FO1/2) → percentage only, cap 85% (FO3) → threshold-led with a 20%
  bleed-through floor (FNV) → non-linear diminishing-returns curve (FO4/76).
- Speech checks: hidden rolls (FO1/2) → visible percentage, reloadable (FO3) → visible fixed thresholds across
  many skills (FNV) → colour-coded Charisma percentage on a 4-option wheel (FO4) → list with SPECIAL thresholds
  (FO76 after April 2020).
- Sawyer's stated reason for FNV thresholds: he disliked "the randomization and the save scumming that
  resulted" from FO3's percentage checks.
- Karma (one global morality number) was the series default; FNV demoted it in favour of per-faction
  fame/infamy; FO4 dropped both and kept only companion approval.
- Only FO1 has real main-quest time pressure (150-day water deadline). Tim Cain says it is the one thing he
  would remove.
- World structure flipped from **node map + random encounters** (FO1/2) to **seamless open world** (FO3 on).
  This is the root cause of most other changes: density, level scaling, environmental storytelling.
- Kill-anyone freedom: FO1, FO2 and FNV let you kill nearly every NPC and still finish. FO3 and FO4 protect
  dozens of "essential" NPCs. FO76 has no meaningful NPC killing at all.
- Pacifist completion is clean in FO1, FO2 and FNV; technically achieved in FO4 only through proxy kills and
  with the game breaking; not practical in FO3 or FO76.
- Ending slides (FO1, FO2, FNV) are the series' cheapest and most-loved reactivity device. FO3 and FO4 replaced
  them with short cinematics and were criticised for it.
- Crafting grew from nothing (FO1) to the central loop (FO4/76: every junk object is components).
- Fallout 4's voiced protagonist and dialogue wheel are the one change Bethesda itself publicly walked back;
  Todd Howard said it "really did not resonate".
- Reception snapshot (Metacritic PC): FO3 91, FNV 84, FO4 84, FO76 52 at launch (Wastelanders re-review 68).
  Critical score tracks polish at launch; long-term fan esteem tracks reactivity (FNV, FO1/2).

---

## 1. Character creation and SPECIAL

### 1.1 Creation flow and budgets

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Creation framing | Menu screen; 3 pre-mades or custom | Same | Diegetic childhood sequence (birth, age 10, age 16 exam) | Diegetic: doctor's exam after being shot | Diegetic: mirror + salesman at the door | Diegetic: photo ID in the vault; stats assigned later |
| Base value per stat | 5 | 5 | 5 | 5 | 1 | 1 |
| Free points | 5 | 5 | 5 | 5 | 21 | 0 at start; +1 per level to level 50 |
| Total budget | 40 | 40 | 40 | 40 | 28 | 56 at level 50 |
| Range | 1-10 | 1-10 | 1-10 | 1-10 | 1-10 base (gear can exceed) | 1-15 base (buffs higher) |
| Can you lower stats for points? | Yes | Yes | Yes | Yes | n/a (all start at 1) | n/a |
| Raising stats later | Rare: paid surgery, a few events, Gain X perks | Rare: Gain X perks, implants/modules | Bobbleheads (+1 each), Intense Training perk, "Almost Perfect" (all 9s, DLC) | Implants (count limited by Endurance), Intense Training | Any level-up point; bobbleheads; one bonus book | Every level to 50; legendary perks later |
| Respec | None | None | None | One re-do when leaving the starting town | None in base game `[UNVERIFIED]` | Free, any time (move points and swap cards) |
| Tag skills | 3 of 18 | 3 of 18 | 3 of 13 | 3 of 13 | none | none |
| Traits | Up to 2 of 16 | Up to 2 of 16 | none | Up to 2 of 10 (16 with DLC) | none | none (mutations are the nearest analogue) |

Sources: fallout.wiki pages on FO1 primary statistics, FO4 perks and FO76 SPECIAL confirm the 1-10 range, FO4
one-point-per-level rule, and FO76's 1-per-stat start, +1 per level to 50 (56 total) and 15 cap. The 40-point
totals for FO1-FNV and FO4's 21 free points are from general knowledge `[UNVERIFIED]`.

Design reading:

- **FO1-FNV: SPECIAL is a commitment.** 40 points across 7 stats averages 5.7. You cannot be good at
  everything, and you live with it for the whole game. Traits and tags sharpen the build further before the
  first step outside.
- **FO3 kept the numbers and removed the commitment.** Bobbleheads, plentiful skill points, a perk per level
  and the "Almost Perfect" perk mean every character converges.
- **FO4: SPECIAL is a currency you buy with levels.** Starting low (28) creates early identity; the absence of a
  level cap removes it later.
- **FO76: SPECIAL is a loadout budget.** A point of Strength is a slot for a Strength card. Identity is whatever
  you equipped this morning. Good for an online game with shifting group roles; fatal for role-playing.

### 1.2 What each stat governs

Derived-stat formulas for FO1 and FO76 were confirmed on fallout.wiki this session. FO3/FNV/FO4 formulas are
from general knowledge `[UNVERIFIED]`.

| Stat | FO1 / FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Strength | Carry 25 + 25/pt lb; melee damage (ST − 5, min 1); weapon min-ST accuracy penalty; HP (+1/pt) | Carry 150 + 10/pt; melee damage; Melee skill | As FO3 plus **weapon Strength requirements** (sway / slower attacks below) | Carry 200 + 10/pt; melee damage; gates Armorer, Blacksmith, Heavy Gunner | Carry 150 + 5/pt; melee +5%/pt; shotgun/heavy/melee cards |
| Perception | Ranged to-hit at distance; Sequence (2 × PE); spotting traps; dialogue observations | Compass detection range; Energy, Explosives, Lockpick skills | As FO3; a few dialogue checks | VATS accuracy; gates Rifleman, Locksmith, Demolition | VATS accuracy; detection; rifle cards |
| Endurance | HP (+2/pt, plus per-level gain); healing rate (EN/3); poison/rad resistance | HP 20/pt; Big Guns, Unarmed skills | HP 20/pt; **implant limit**; Survival, Unarmed | HP 5/pt plus per-level gain; sprint drain | HP 250 + 5/pt; sprint drain; disease resistance |
| Charisma | NPC reaction; barter prices; **FO2 party size (CH/2)** | Speech and Barter skill base only | Speech/Barter base; **companion "Nerve"** (+5% damage and armor per point) | Persuasion chance; prices; **settlement population (10 + CH)**; Local Leader | Prices; quest reward scaling; **perk sharing with team** |
| Intelligence | **Skill points/level (5 + 2 × IN)**; dialogue options; IN < 4 gives "dumb" dialogue | Skill points/level (10 + IN); Science, Repair, Medicine | Skill points (10 + IN/2); many dialogue checks | **XP gain (+3%/pt)**; gates Gun Nut, Science!, Hacker | XP bonus (about +2%/pt); crafting quality; hacking |
| Agility | **Action Points (5 + AG/2)**; Armor Class; gun skills | AP (65 + 2/pt); Small Guns, Sneak | AP (65 + 3/pt); reload and draw speed; Guns, Sneak | AP (60 + 10/pt); sneak; gates Gunslinger, Commando, Sneak | AP 60 + 10/pt; sneak; pistol/auto cards |
| Luck | Crit chance (1%/pt); random events; gambling; jinx outcomes | Crit chance (1%/pt); +0.5 to all skills per point | Crit chance; **casino odds**; all skills | **Critical meter fill rate**; loot perks (Fortune Finder, Scrounger); Idiot Savant | Crit meter recharge; loot condition; luck cards |

### 1.3 God stats and dump stats

| Game | God stat(s) | Dump stat(s) | Why |
|---|---|---|---|
| FO1 | Agility (AP is everything in turn-based), Intelligence | Charisma (almost no mechanical effect; Speech skill does the work), Endurance | The "Gifted" trait (+1 all stats) is close to mandatory. No party-size rule makes CH nearly worthless. |
| FO2 | Agility, Intelligence | Endurance, often Strength (power armor gives +3/+4) | Charisma was patched into relevance: party size = CH/2. Still skippable for solo play. |
| FO3 | Intelligence (skill points), mildly | Charisma, Perception; in truth all of them | Skills cap at 100 and you can max nearly all; stats barely matter. The weakest SPECIAL of the series. |
| FNV | Intelligence, Endurance (implants), Luck (crits, casinos) | Charisma (most notorious dump stat in the series), Perception | Sawyer has acknowledged Charisma's weakness; companions' Nerve bonus was the attempted fix. Community mods routinely rework it. |
| FO4 | Intelligence (XP, crafting perks), Agility/Luck (VATS builds), Charisma (settlements) | Perception outside VATS builds; Endurance | First game where Charisma is strong, because it gates settlement supply lines and all persuasion. |
| FO76 | Depends on weapon class; Luck and Agility for crit/VATS metas | Whatever your weapon does not use | Stats matter only as card slots. "Dump" is fluid since respec is free. |

Lesson: a stat is only as good as the *systems that read it*. Charisma was dead until designers attached it to
something concrete (party size, settlement cap, companion power). Intelligence is perennially strongest
because it multiplies progression itself, which is a design smell: a stat that speeds up levelling is a tax
every optimiser pays.

---

## 2. Skills

### 2.1 Lists per game

| Category | FO1 / FO2 (18) | FO3 (13) | FNV (13) | FO4 | FO76 |
|---|---|---|---|---|---|
| Ranged | Small Guns, Big Guns, Energy Weapons, Throwing | Small Guns, Big Guns, Energy Weapons | **Guns** (merged Small Guns), Energy Weapons (heavy weapons split between the two and Explosives) | Perks by weapon class: Gunslinger, Rifleman, Commando, Heavy Gunner | Perk cards by weapon class |
| Close | Unarmed, Melee Weapons | Unarmed, Melee Weapons | Unarmed, Melee Weapons | Iron Fist, Big Leagues | Cards |
| Explosives | Traps (and Throwing) | **Explosives** (merged Traps + Throwing) | Explosives | Demolition Expert | Cards |
| Medical | First Aid, Doctor | **Medicine** (merged) | Medicine | Medic | Cards |
| Thief | Sneak, Lockpick, Steal | Sneak (absorbed Steal), Lockpick | Sneak, Lockpick | Sneak, Locksmith, Pickpocket | Cards |
| Technical | Science, Repair | Science, Repair | Science, Repair | Hacker, Science!, Gun Nut, Armorer | Cards |
| Social | Speech, Barter, Gambling | Speech, Barter | Speech, Barter | Charisma stat only; Cap Collector | Charisma stat |
| Wilderness | Outdoorsman | (none) | **Survival** (new) | (none) | Cards |
| Scale | 0-200% (FO1), 0-300% (FO2) | 0-100 | 0-100 | 2-5 ranks per perk | 1-5 ranks per card |
| Points per level | 5 + 2 × IN; tagged skills rise double | 10 + IN | 10 + IN/2 | n/a | n/a |

(Skill lists are from general knowledge; counts 18/13/13 are well established but were not re-fetched this
session `[UNVERIFIED]`.)

### 2.2 Consolidation timeline and reasoning

| Step | Change | Reasoning / effect |
|---|---|---|
| FO1 → FO2 | Same list. Raised cap to 300%. | Did not fix the dead skills. Gambling, Throwing, First Aid, Traps, Barter and Outdoorsman remained low-value despite the "useful non-combat skills" goal in the vision document. |
| FO2 → FO3 | 18 → 13. Merged First Aid + Doctor, Traps + Throwing, Steal into Sneak; removed Gambling and Outdoorsman. | Sensible pruning. But FO3 also made skills trivially maxable (books, 10 + IN per level, cap raised to 30), so the pruning did not create identity. |
| FO3 → FNV | Small Guns + Big Guns → Guns; added Survival. Skills now gate weapon sway, crafting recipes and dozens of dialogue checks. | Sawyer's fix for "Big Guns arrive too late to justify tagging". Every skill got audited usage: Obsidian tracked skill-check distribution with an internal script-tracking tool so no skill was starved. |
| FNV → FO4 | Skills removed entirely. Seven SPECIAL columns × 10 perks each (70 perks, 229 ranks; 243 with DLC ranks). | Bethesda's argument: skills and perks overlapped, and +1% increments are invisible. A rank that says "+20% rifle damage" is legible. Cost: no granular character expression, no skill checks in dialogue, non-combat competence becomes binary gates (Locksmith rank 3 or nothing). |
| FO4 → FO76 | Perk cards slotted under SPECIAL. | Makes builds swappable and monetisable/grindable (card packs every few levels). |

### 2.3 Which skills actually worked

| Verdict | Skills | Why |
|---|---|---|
| Always worth it | Small Guns/Guns, Speech, Lockpick, Science, Repair (FNV) | Used constantly, clear payoffs, gate content |
| Worth it only in one game | Outdoorsman (FO2, avoids encounters), Survival (FNV Hardcore), Barter (FNV, has dialogue checks) | The skill needs a system that bites |
| Traps | Big Guns (FO1-3, weapons arrive late), Energy Weapons early game, Throwing, Gambling, First Aid | Either gear-gated or dominated by a sibling skill |
| Honest finding | "No useless skills" was a stated goal that the original games failed and FNV came closest to meeting | It takes active auditing, not good intentions |

---

## 3. Traits

Traits are optional creation-time picks with a benefit and a drawback. They are the purest "build-defining"
tool in the series and Bethesda removed them twice.

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Count | 16 | 16 (Sex Appeal replaces Night Person) | 0 | 10 base, 16 with Old World Blues | 0 | 0 |
| Pick limit | 2 | 2 | - | 2 | - | - |
| Signature examples | Gifted (+1 all stats, fewer skill points), Fast Shot (cheaper shots, no aimed shots), Jinxed (everyone fumbles), Bloody Mess, Finesse, Skilled | Same | - | Wild Wasteland (toggles silly encounters), Four Eyes, Built to Destroy, Trigger Discipline, Kamikaze, Skilled, Logan's Loophole (level cap 30 for chem immunity) | - | Mutations (19, each with a plus and a minus, acquired in play, removable) `[UNVERIFIED count]` |
| Balance | Poor: Gifted is near-mandatory; several are traps | Same | - | Better, though Skilled and Good Natured are near-free | - | Strong meta role; drawbacks often negated by a perk |

Notable design idea: FNV's **Wild Wasteland** turned the series' tonal argument (grim vs. goofy) into a player
toggle. That is a rare case of solving a design dispute by handing it to the player.

FO76's mutations show the idea still works in a live game: risk/reward modifiers acquired diegetically
(radiation exposure) rather than at a menu.

---

## 4. Perks

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Rate | Every 3 levels (4 with Skilled) | Every 3 levels | Every level | Every 2 levels | 1 point per level (shared with SPECIAL raises) | 1 card pick per level; SPECIAL point per level to 50; card packs periodically |
| Picks in a full base-game run | about 7 | open-ended, about 8-12 in normal play | 19 (29 with Broken Steel) | 15 (25 with all DLC) | unbounded | unbounded collection; equipped set limited by 56 points |
| Catalogue size | about 50 `[UNVERIFIED]` | about 75 `[UNVERIFIED]` | 58 base `[UNVERIFIED]` | 88 base `[UNVERIFIED]` | 70 perks / 229 ranks (243 with DLC) | hundreds of cards `[UNVERIFIED]` |
| Gating | Level + stat + skill | Level + stat + skill | Level + stat + skill | Level + stat + skill | SPECIAL rank + level per rank | SPECIAL points available |
| Typical perk | Rule-changer: Bonus Rate of Fire, Slayer, Sniper, Awareness, Mysterious Stranger | Same plus social oddities | Mix; many "+10 to two skills" fillers (e.g. Gun Nut, Daddy's Boy) | Mostly rule-changers and conditional builds: Jury Rigging, Cowboy, Shotgun Surgeon, Grunt, Hand Loader; challenge-earned perks | Mostly ranked +20% damage steps, with a rule-changer at the top rank | Mostly +10/15/20% steps; a few rule-changers |
| Non-chosen perks | A few quest/implant perks | Quest/reputation perks | Quest perks, bobbleheads | Challenge perks, companion perks, implants | Magazines, companion perks, bobbleheads | Legendary perks (slot every 50 levels, six slots at level 300), mutations |

Tim Cain's GDC 2012 postmortem (per attendee notes) says perks were added late, were quick to implement and
gave characters more variety. Perks exist because GURPS was pulled and the replacement system needed a
personality layer fast. The series' most copied mechanic was a late patch.

Philosophy comparison:

- **Scarce and transformative (FO1/2, FNV).** A perk every 2-3 levels makes each pick a decision you remember.
  The best ones change rules (extra attacks, new dialogue, different crit tables), not percentages.
- **Abundant and incremental (FO3).** A perk every level, and filler perks that just add skill points, erase
  the difference between "perk" and "skill point". FNV's halved rate was a direct correction.
- **Perks as the whole system (FO4).** Elegant chart, legible ranks, and a satisfying poster. But roughly four
  ranks in five are "+20% damage with weapon class X" or "unlock crafting tier N". Damage perks are a tax, not
  a choice: you need them to keep pace with scaled enemy health.
- **Perks as equipment (FO76).** Cards can be swapped for free. That converts character identity into an
  inventory problem, and the game eventually added loadout slots to ease the chore.

Opinion: the quality bar for a perk is "would a player describe their character by naming it?" FO1's Slayer,
FNV's Cowboy and FO2's Jinxed pass. FO4's Rifleman rank 3 does not.

---

## 5. Levelling and caps

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Level cap | 21 | 99 | 20; 30 with Broken Steel | 30; +5 per story DLC to 50 | None (engine limit 65,535) `[UNVERIFIED]` | None; SPECIAL growth stops at 50 |
| Typical end-of-game level | 12-18 | 20-35 | cap reached well before content ends | 30-50 | 40-80 | 50-500+ |
| XP sources | Kills, quests, skill use (lockpick, heal) | Same | Kills, quests, lockpick/hack, discovery, speech | Same plus challenges | Kills, quests, **crafting and building**, discovery | Same plus events, dailies |
| Per-level reward | HP, skill points; perk every 3 | Same | HP, 10 + IN skill points, perk | HP, skill points, perk every 2 | HP, 1 point | 1 SPECIAL (to 50), 1 card |
| Can one character do everything? | No | Eventually, with grinding | **Yes, easily** | Mostly, by 50 with high IN | **Yes** (all perks and stats at level 286 per fallout.wiki) | Yes, but only a 56-point slice is active |
| "Master of all" severity | Low | Medium | Very high | Medium (Sawyer's own mod lowers the cap to 35) `[UNVERIFIED]` | High but slow | Managed by loadout limit |

Reasoning:

- FO3's cap of 20 was hit so early that players complained of wasted XP; raising it to 30 made the convergence
  problem worse (almost every skill at 100).
- FNV's 50 cap with DLC undermined its own slowed perk rate. This is the standard DLC trap: each expansion
  wants to hand out power.
- FO4 removed the cap so players "never stop progressing" in a 400-hour sandbox. It fits Bethesda's goal of one
  save file that sees everything, and contradicts the replay-a-new-build goal of the older games.
- FO76's approach is the only one that keeps both: infinite progression *and* a hard budget on what is active.

---

## 6. Combat model

| | FO1 / FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Core | Turn-based on hex grid, isometric | Real-time first/third person + VATS pause | Same + iron sights, ammo types, DT | Real-time shooter + VATS slow-motion | Real-time online shooter + real-time VATS |
| Action economy | AP per turn (5 + AG/2): move 1/hex, shoot 4-6, reload 2, inventory 4 (2 in FO2 `[UNVERIFIED]`) | AP pool for VATS only (65 + 2 × AG) | AP for VATS (65 + 3 × AG) | AP for VATS **and sprinting** (60 + 10 × AG) | Same; AP also for jumping |
| Hit determination | Dice: skill %, range, light, AC; max 95% | Real-time: hitscan with skill-driven spread. VATS: dice | Real-time: spread from skill, Strength, condition; true iron sights. VATS: dice | Real-time: player aim dominant, stats barely affect accuracy. VATS: dice from Perception | Same as FO4, server-authoritative |
| Targeted shots | Aimed shots at 8 body regions incl. eyes and groin; accuracy penalty, crit bonus | VATS limbs; no eyes/groin | VATS limbs | VATS limbs; **manual critical meter** | VATS limbs once a card is equipped |
| Player safety in VATS | n/a | Takes 10% damage while in VATS | Takes 75% damage; melee doubled | Time slowed, not stopped; vulnerable | No slowdown at all |
| Critical hits | Luck % roll per shot; crit tables with instant-death and knockdown results | Luck % in real time; +15% in VATS `[UNVERIFIED]` | Luck % × weapon crit multiplier | **No random crits outside perks**; meter fills in VATS, player banks and spends | Same meter |
| Companion control | FO1 none (Ian shoots you in the back); FO2 behaviour panel | Minimal orders | Companion wheel: tactics, range, stance | Point-and-command | none (allies stay in camp) |
| Signature flavour | Death animations, crit text log, "eyes shot" | Slow-motion kill cam (inspired by Burnout crash replays, per Wikipedia) | Same, more lethal | Gun-feel overhaul, power armor as a vehicle, legendary enemies | Group events, bosses, nukes |

Sources: fallout.wiki damage overview footnotes (VATS damage-taken reductions of 90% and 25%, melee doubling);
Wikipedia FO3 (Howard wanted a mix of real-time and turn-based to appeal to both shooter and RPG fans; devs
later judged the shooting a weak point).

Analysis:

- **VATS is a brilliant compromise and a poor combat system.** It preserved aimed shots, AP and gore in a
  shooter shell and gave non-twitch players a way to fight. But FO3's VATS is close to an "I win" button (90%
  damage immunity while queued shots play).
- **FNV made the real-time half viable** (iron sights, less skill-driven spread). FO4 finished the job with
  help from id Software staff on gun-feel `[UNVERIFIED]`, at which point stats stopped deciding whether you hit.
- **The trend is from character skill to player skill.** In FO1 a character with 30% Small Guns misses. In FO4
  a new character headshots as well as the player can aim. That is more fun minute-to-minute and removes the
  main reason to specialise.
- **FO4's critical meter** is the best single VATS-era idea: it converts a hidden roll into a banked,
  player-timed resource.
- FO76's real-time VATS shows what is left when pausing is impossible: an aim-assist with a stat-based hit
  chance. It still supports whole builds, which says players value the *auto-aim plus crit* loop, not the pause.

---

## 7. Damage and armor formulas

| Game | Formula (simplified) | Caps / floors | Confidence |
|---|---|---|---|
| FO1 / FO2 | `A = weapon roll × ammo damage multiplier (and crit, difficulty)`; `B = A − DT`; `final = B × (1 − (armor DR + ammo DR modifier)/100)`. Separate DT/DR per damage type (normal, laser, fire, plasma, explosive, electrical/EMP). Armor Class is a separate to-hit penalty. | DR capped at 90% `[UNVERIFIED]`. DT can zero a hit entirely. | Order (ammo → DT → DR) confirmed by NMA / BGforge / GOG forum reconstructions. FO1's ammo modifiers are reported as bugged in the executable; FO2's AP ammo is notoriously weak. `[DISPUTED]` details. |
| FO3 | `final = damage × (1 − DR/100)`. No DT. Weapon damage scales with skill and condition. | DR capped at 85% (fallout.wiki). | Confirmed cap; skill-scaling constants not checked. |
| FNV | `afterDR = damage × (100 − min(DR, 85))/100`; `final = max(afterDR − DT, damage × 0.2)`; difficulty multiplier last. Crit damage is added before DT. Ammo types multiply target DT (AP lowers, hollow point raises). | 20% minimum bleed-through. DR is rare and effectively caps at 80-85%. | Confirmed on fallout.wiki. Some sources state DT before DR. `[DISPUTED]` order; irrelevant in most cases since few things have both. |
| FO4 | `coeff = min(0.99, (damage × 0.15 / resistance)^0.365)`; `final = damage × coeff`. Separate ballistic, energy, radiation and poison resistances. | Always at least 1% reduction; never 100%. Resistance equal to damage gives 50% reduction; you need huge resistance for small gains. | Confirmed on fallout.wiki (constants `fPhysicalDamageFactor` 0.15 and exponent 0.365). |
| FO76 | Same family of non-linear curve as FO4. Additive rather than multiplicative damage bonuses since One Wasteland (Sept 2020). | PvP per-hit damage cap of 110 (fallout.wiki footnote). | Exact constants not verified. `[UNVERIFIED]` |

Worked comparison (same intuition, different feel):

| Scenario | FO1/2 | FO3 | FNV | FO4 |
|---|---|---|---|---|
| Weak fast weapon (10 dmg) vs. heavy armor | Often 0 damage; "bounces off" | Reduced by the same % as anything else | Floors at 2 (20%) | Heavily reduced, about 30-50%+ |
| Strong slow weapon (100 dmg) vs. heavy armor | Most gets through | Same % reduction | Loses only the flat DT | Mildly reduced |
| Player lesson | Bring the right gun or do not fight | Any gun works; armor is a single number | Weapon/ammo choice matters; automatic weapons are bad against armor | High per-shot damage favoured, but nothing is ever useless |

Analysis:

- **Percentage-only DR (FO3) is the dullest model.** It makes weapon choice a DPS comparison.
- **Threshold models create tactics** (carry AP rounds, bring an anti-materiel rifle for deathclaws) and
  create *feel* (small arms pinging off power armor). FNV's 20% floor is the key safety valve: thresholds
  without a floor produce "zero damage" dead ends that players read as bugs.
- **FO4's curve is mathematically elegant and experientially flat.** It depends on the ratio of hit damage to
  armor, so it keeps a threshold-like bias against weak hits without ever saying no. Players cannot predict
  outcomes from the number on the Pip-Boy; "armor 200" means nothing intuitive.
- **Bullet sponge** is the common failure of FO3 (Broken Steel's high-HP enemies), FO4 (level-scaled health)
  and FO76 (pre-rebalance). It comes from scaling health instead of scaling threat.

Difficulty settings: in FO3/FNV the slider is a pure damage-dealt/damage-taken multiplier (Very Hard doubles
incoming damage per fallout.wiki; halves outgoing `[UNVERIFIED]`). FO3 also increases XP on higher
difficulties `[UNVERIFIED]`. FO4 adds more legendary spawns at higher settings `[UNVERIFIED]`.

---

## 8. Healing and survival

| | FO1 / FO2 | FO3 | FNV (normal) | FNV (Hardcore) | FO4 (normal) | FO4 (Survival, 2016 patch 1.5) | FO76 |
|---|---|---|---|---|---|---|---|
| Stimpaks | Instant | Instant, usable in paused Pip-Boy | Instant | **Heal over time** | Heal over time with an animation | Slower; cause thirst; have weight | Heal over time; hotkey |
| Skill healing | First Aid / Doctor, limited uses per day | Medicine scales stimpaks | Medicine scales | Same | Medic perk | Same | Cards |
| Food | Trivial | Heals, adds rads | Heals; Survival skill scales it | Required: hunger meter | Heals; cooked food buffs | Required: hunger | Originally required; penalties removed in 2021 and replaced with bonuses for being fed `[UNVERIFIED]` |
| Water | Plot only | Heals, rads; purified water as currency-like | Same | Required: thirst meter | Heals | Required | As food |
| Sleep | Passes time, heals | Full heal, "Well Rested" XP | Same | Required; beds matter | Full heal | **Only way to save**; bed quality limits sleep; fatigue reduces AP | "Well Rested" bonus only |
| Crippled limbs | Need Doctor skill or a doctor | Stimpak to limb or sleep | Same | **Doctor's Bag or a doctor only** | Auto-heal after combat / stimpak | Stimpak needed | Stimpak / auto |
| Radiation | Hidden counter, stat loss, death; Rad-X/RadAway | Tiered stat penalties, death at 1000 | Same | Same | **Reduces max HP** (visible red bar) | Same; RadAway causes fatigue | Reduces max HP; also causes mutations |
| Addiction | % chance per use; withdrawal penalties | Same; cured by any doctor | Same | Same | Same; Addictol item | Same | Same |
| Disease | Poison only | - | - | - | - | Illnesses from food, water, creatures | Diseases from creatures, bad sleep |
| Ammo weight | Yes (all items weigh) | No | No | **Yes** | No | **Yes** | Yes |
| Companion death | Permanent | Permanent | Unconscious only | **Permanent** | Never (essential) | Left behind if not healed | n/a |

Analysis:

- FO4 changing radiation from stat penalties to **max-HP reduction** is a quiet design win: one visible bar,
  an immediate consequence, and a real reason to carry RadAway.
- **Pausing to eat forty items** is the healing problem of the 3D games. FNV Hardcore and FO4 fixed it with
  heal-over-time.
- FNV's Hardcore mode and FO4's Survival mode are the two most praised optional modes in the series. Both
  work by making *existing* systems matter (weight, beds, cooking, map knowledge), not by adding enemies' HP.
  FO4 Survival removing fast travel and manual saves makes the settlement network meaningful for the first
  time.
- FO76 shipped with mandatory hunger and thirst and later removed the penalties. In an always-online game
  with session-based play, upkeep meters read as chores. Survival pressure wants a single-player, pausable,
  self-paced context, or it must be the whole game.

---

## 9. Stealth

| | FO1 / FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Activation | Toggle Sneak skill; periodic hidden rolls | Crouch | Crouch | Crouch | Crouch |
| Feedback | Almost none; you find out when combat starts | HIDDEN / CAUTION / DANGER text | Same | Bracket width + states | Same, plus other players |
| Inputs | Sneak skill, light, armor? `[UNVERIFIED]` | Sneak skill, light, movement speed, noise, line of sight | Same | Sneak perk ranks, Agility, light, armor weight | Cards, Agility, armor effects |
| Sneak attack | Bonus crit chance from behind? `[UNVERIFIED]` | Guaranteed crit; ×2 ranged, ×5 melee `[UNVERIFIED]` | Same | ×2 base; Ninja up to ×3.5 ranged, ×10 melee | ×2; cards to ×2.5+ |
| Pickpocket | Steal skill; planting explosives works | Sneak-based; reverse-pickpocket grenades | Same | Pickpocket perk | n/a |
| Stealth items | Stealth Boy (FO1/2) | Stealth Boy, Chinese stealth armor (DLC) | Stealth Boy, faction disguises | Stealth Boy, shadowed/Chameleon armor | Chameleon effects |
| Stealth as quest solution | Often supported: sneak into bases, steal quest items | Sometimes | Often; disguises open whole factions | Rare; stealth is a damage multiplier | Rare |

Trend: stealth moved from an **alternative route** (get in, take the thing, never fight) to a **damage
multiplier** (the stealth-sniper build). The 3D games made stealth far more readable and usable, and far less
meaningful as a quest path. FNV's faction disguises are the standout idea: social stealth layered on the
reputation system.

---

## 10. Dialogue systems

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Presentation | Full-sentence list; ~20 "talking heads" with lip-sync, rest text | Same | Full-sentence list, first-person zoom, time frozen | Same | **4-option wheel**, paraphrases, cinematic camera, real-time (can walk away) | At launch: no human NPCs; holotapes, robots, terminals. Since Wastelanders (April 2020): full-sentence list |
| Player voice | Silent | Silent | Silent | Silent | **Fully voiced** (male and female) | Silent |
| Keyword input | "Tell me about..." typed query | Removed | - | - | - | - |
| Stat gating | Intelligence filters which lines appear; IN < 4 gives separate "dumb" lines; hidden NPC reaction score from Charisma, karma, prior remarks | Same, more extensive low-IN content | Occasional [Intelligence], [Strength], perk lines; always succeed if shown | Frequent SPECIAL, skill, perk, reputation lines | Charisma only (base game); some SPECIAL checks in Far Harbor `[UNVERIFIED]` | SPECIAL thresholds, e.g. Charisma 4+ |
| Skill checks | Speech rolled invisibly | Same; Empathy perk colour-codes lines | **Visible % chance** (e.g. Speech 47%), one roll, reloadable | **Visible threshold** (e.g. Speech 50); failed checks show a distinct, often funny, weak line and your value vs. required | Yellow / orange / red persuasion; hidden % from Charisma; can retry some | Pass/fail thresholds |
| Skills checked | Speech (plus Barter, Science via scripts) | Same | Mostly Speech; a few Science/Medicine/Repair | Speech, Barter, Science, Medicine, Repair, Explosives, Guns, Survival, Sneak and more | n/a | SPECIAL only |
| Temporary boosts | Chems (Mentats) | Same | Clothing, chems | Skill magazines (+10, +20 with Comprehension), clothing, chems | Clothing, chems, alcohol | Buffs, team perks |
| Volume | Small, dense | Large | Large | Very large (65,000 lines at release, a record at the time) `[UNVERIFIED]` | 111,000 lines (Wikipedia) | Small at launch; grows by update |

Developer statements gathered:

- Vision document point: conversations show NPC reactions that change with what you say and are remembered;
  the character's intelligence limits available lines.
- Sawyer (Kinda Funny interview, reported by Gameranx, Nov 2022): "I looked at how Fallout 3 did their
  percentage-based skill checks, and I didn't like the randomization and the save scumming that resulted".
- Sawyer (video reported by 80.lv, Aug 2024): skill checks are deliberately **front-loaded** so the player
  learns early that the game is paying attention to their build; the team tracked check distribution with an
  internal tool; the goal is "a rewarding level of feedback", not numerical parity.
- Howard on FO4 (GameSpot 2016 and a later GQ interview, via PC Gamer and others): the dialogue system
  "didn't work as well" and "really did not resonate"; players wanted to role-play and "we had a voiced
  protagonist".

Analysis of each model:

| Model | Strength | Weakness |
|---|---|---|
| Hidden roll (FO1/2) | Feels like a conversation, not a lock | Player cannot tell skill from luck; invites reloading |
| Keyword query (FO1) | Sense of open inquiry | Mostly returned nothing; cut in FO2 |
| Visible % (FO3) | Clear | Purely a reload prompt. A 30% check is passed by pressing F9 three times |
| Visible threshold (FNV) | Rewards investment deterministically; magazines create planning; fail lines add comedy | No tension; players "shop" for the tagged option; the tagged option is almost always the best one, so it becomes a win button rather than a choice |
| Wheel + voice (FO4) | Cinematic, fast, console-friendly | Four slots force "yes / sarcastic yes / question / no"; paraphrases mislead; recording cost caps branching; a fixed voice and backstory fights role-play |
| List + SPECIAL (FO76) | Cheap, flexible, works with free respec | Free respec means checks test nothing permanent |

Opinion: FNV's threshold system is the best base, with one fix it never made: skill-tagged lines should
sometimes be the *wrong* or merely *different* thing to say, so the tag is information rather than a
guaranteed win. Low-intelligence dialogue (FO1/2, small traces in FNV) is the series' best proof that
stat-driven dialogue creates replay value; it is also expensive, which is why it vanished.

---

## 11. Karma vs. reputation

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Global morality | Karma number + a few titles (Champion, Berserker, Childkiller) | Karma + many special titles (Slaver, Gravedigger, Made Man, Prizefighter...) | Karma (−1000 to +1000) is the main system; karma-by-level titles | Karma exists, almost nothing reads it | None | None |
| Local/faction standing | Per-town reaction hidden | **Per-town reputation** (Idolized to Vilified) | None | **Per-faction and per-town fame AND infamy**, tracked separately | Binary faction membership / hostility | Settlers and Raiders reputation tracks (Wastelanders), raised mainly by daily quests |
| Mixed states | - | - | - | Yes: high fame + high infamy gives distinct labels (e.g. "Wild Child", "Merciful Thug") `[UNVERIFIED names]` | - | - |
| Consequences | Dialogue reactions, bounty hunters | Access to towns, quests, companions; bounty hunters | Companion gating; rival hit squads; radio DJ commentary; a few perks | Prices, access, safehouses, faction hit squads, companions leaving, ending slides | Companion affinity only | Vendor stock unlocks |
| Disguise | - | - | - | Faction armor temporarily sets you to neutral | - | - |
| Theft | Karma neutral unless caught | Same | **Stealing lowers karma even unseen** | Same oddity retained | No effect unless seen (companions react) | n/a |

Gavin Carter (FO3 lead producer, per Wikipedia) framed karma as showing immediate consequences so players
question their choices. In practice a single axis collapses every situation into good/bad and invites
gamified absurdities (nuke a town, then donate water to return to sainthood).

Sawyer's position, across his "Reputation Overload" talk (GameBanshee summary, not viewed in full this
session) and the FNV design: morality is the player's business; what the *world* can track is what specific
groups have seen you do. Two separate axes (fame, infamy) per faction mean good deeds do not erase atrocities.

FO4's deletion of both systems removed bookkeeping and also removed the world's memory. Companion affinity
("X liked that") is a reputation system with an audience of one, and it nudges players toward gaming the
approval of whoever is standing next to them.

---

## 12. Companions

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Count | 4 (three humans + dog) | About a dozen | 8 `[UNVERIFIED]` | 8 (6 humanoid, 2 non) | 13 base, more with DLC `[UNVERIFIED]` | No followers; camp "allies" since Wastelanders; other players |
| Active limit | No formal limit | Charisma / 2 | 1 + dog | 1 humanoid + 1 non-humanoid | 1 | 1 ally at camp |
| Recruit gate | Dialogue / payment | Charisma, quests, karma | **Karma tier** | Dialogue, skills, faction standing | Quests | Quests |
| Control | None; barter to change gear; cannot change armor | Combat settings panel; armor swap; they level up | Basic orders | **Companion wheel** (tactics, inventory, stance) | Command cursor | - |
| Depth | Minimal | Personality, some banter | Thin | Each has a personal quest that upgrades them and a passive perk for the player | Affinity meter, personal quest for some, romance, perk at max affinity | Daily quests, light romance |
| Mortality | Permanent | Permanent | Permanent | Essential normally, permanent in Hardcore | Essential | - |
| Reaction to your choices | Little | Some | Leave on karma shift | Leave on faction/reputation conflict; comment on locations | Constant like/dislike feedback; can leave | - |

Evolution: gun-mules (FO1) → party members (FO2) → characters with arcs tied to the setting's themes (FNV)
→ relationship meters (FO4). FNV's companion-granted perks (e.g. a tracker who highlights targets, a mechanic
who improves repair) are worth copying: the companion changes *how you play*, not just your DPS.

---

## 13. Crafting, economy and currency sinks

### 13.1 Crafting

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Player crafting | None | None (a few NPC upgrades) | 7 schematic weapons at workbenches `[UNVERIFIED count]`; repair by cannibalising duplicates | Workbench, reloading bench, campfire; ammo breakdown and hand-loading; food/chems via Survival; purchasable weapon mods (up to 3 per gun) | Everything: weapon and armor mod trees, cooking, chems, power armor, settlement building; all junk breaks into components | FO4's system + learned plans, camp building, legendary rerolls |
| Gating | - | - | Repair skill, schematics | Skills (Repair, Science, Survival, Explosives) | Perk ranks (Gun Nut, Armorer, Science!, Local Leader) | Plans (drops/vendors), cards |
| Item condition | None | None | Yes; degrades; affects damage and value | Yes; repair kits; Jury Rigging perk | **Removed** (except power armor pieces) | Yes |
| Junk | Flavour or quest | Same | Mostly vendor trash; a few schematic parts | Recipe ingredients | **All of it matters**; tag-for-search | Same, with heavy stash-weight pressure |

FO4's junk-to-components system is the series' best loop invention. It gave every desk fan a purpose and made
looting the reward for exploration, which fits the "go there" philosophy exactly. The cost: inventory
micromanagement becomes the main activity, and found gear is devalued because built gear is better.

### 13.2 Economy

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Currency | Bottle caps (trader-backed) with true barter | Coins (NCR money) with true barter | Caps | Caps + NCR dollars + Legion coin (exchange rates); casino chips | Caps | Caps (hard wallet cap) + gold bullion, scrip, other tokens + premium Atoms |
| Trade UI | Barter table: goods vs. goods | Same | Buy/sell with merchant cap pool | Same | Same | Same + player vending machines |
| Merchant limits | Small inventories of money | Same | Limited caps per merchant | Same; some rich vendors | Same; settlement stores | Shared daily vendor pool |
| Main sinks | Stat surgery, best armor, combat training | Car, implants, armor upgrades | House themes, repairs, ammo | **Implants (thousands each), high-tier guns and mods, repairs, casino play**, faction bribes | Shipments of materials, settlement stores, a few unique items | Fast travel fees, plans, repairs, camp upkeep, bullion items, cosmetics |
| Typical late-game state | Rich but done | Very rich | Drowning in caps, nothing to buy | Still wanting money until late | Rich; materials are the true currency | Wallet-capped; grinding alternate currencies |
| Faucet abuse | Gambling skill, barter exploits | Same; stealing | Selling repaired loot | Casinos (limited by ban thresholds per casino) | Water purifier farms | Player trading, events |

Observations:

- Every game except FNV runs out of things to buy. FNV's implants (count limited by Endurance, cost rising
  into the thousands) and expensive ammo types are proper sinks tied to character power.
- FNV's casino winnings caps (you get banned after a threshold) are a tidy way to let Luck builds profit
  without breaking the economy.
- Multiple currencies in FNV are worldbuilding first (faction legitimacy expressed as exchange rates) and
  mechanics second. FO76's multiple currencies are grind pacing: each has a daily or weekly earn limit.
- FO4 quietly changed the true currency to adhesive, screws and aluminium. Scarcity of a few key components is
  a better economy than caps ever were.

---

## 14. World structure and travel

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Structure | World map of nodes; each location is a set of small maps | Same, larger | Seamless open world + interior cells; downtown split by metro tunnels | Seamless open world; walled Strip in cells | Seamless; dense city with fewer loads | Seamless shared server (24 players); region difficulty bands |
| Scale feel | Abstract: weeks of travel | Abstract, bigger | About 16 square miles of walkable terrain `[UNVERIFIED]` | Similar, emptier desert | Smaller footprint, much denser, vertical | About four times FO4 by Bethesda's claim `[UNVERIFIED]` |
| Marked locations | About a dozen major | About two dozen | 160+ `[UNVERIFIED]` | 180+ `[UNVERIFIED]` | 300+ with DLC `[UNVERIFIED]` | Hundreds |
| Travel | Click-to-move on map; time passes; random encounters by terrain, Outdoorsman and Luck | Same + a **car** (fuel cells, trunk storage) | Walk; free fast travel to discovered markers | Same | Same; vertibird signal late; **no fast travel in Survival** | Fast travel costs caps by distance; free to teammates, own camp, some hubs |
| Random encounters | Core content: patrols, traders, special one-off joke encounters | Same, many more special encounters | Scripted random-event spawn points | Few; mostly hand-placed | Random event points, settlement attacks | Public events on timers |
| Direction of play | Open after first town; the map itself hides distant places | Open but level-gated by enemy difficulty | Open in all directions; level scaling smooths it | **Soft-gated loop**: deadly creatures north of the start push new players along the southern road | Open; difficulty rises with distance from start (south and east) | Open; originally region-banded, then per-player scaling |
| Environmental storytelling | Low (sprite limits); text descriptions | Low | **High**: skeleton tableaux, terminals, vault experiments | High | Very high; most locations have a self-contained found story | Carried the whole game at launch (holotapes of the dead) |

Sawyer has said the deathclaws and cazadores near the FNV start were placed as a warning to players expecting
FO3's go-anywhere ease (PC Gamer / 80.lv headlines on his remarks). Players who know the game can still sneak
through, which preserves freedom while teaching respect.

Design consequences of the node-map → open-world switch:

1. **Abstraction vs. presence.** FO1's map sells a vast, empty, dangerous wasteland at almost no content cost.
   FO3's world must put something every 90 seconds of walking, which compresses geography (a "city" of thirty
   people next to a raider camp).
2. **Random encounters vs. placed encounters.** Node maps make the journey a dice-driven story generator.
   Open worlds make it a tour of authored vignettes.
3. **Towns shrink.** FO2's New Reno or NCR are large because the engine only had to draw towns. FO3's Megaton
   and FO4's Diamond City are small because the whole world shares the budget.
4. **Settlement logic strains.** Critics of FO3 keep asking "what do they eat?", a question FNV answered with
   visible farms and trade routes and FO4 answered by making the player build them.

---

## 15. Quest structure and ways to finish

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Main quest shape | Two-act hunt (find the part, then end the threat); final targets doable in either order | Long hunt, linear final act | Linear chain of about a dozen steps | Linear first act, then a four-way faction branch converging on one battle | Linear first half, then a four-faction branch with forced mutual destruction | Linear solo chains; group endgame events |
| Skippable main steps | Yes; you can go straight to end targets with knowledge | Partly; speedrun routes exist | Some steps skippable by finding the father early | First act skippable by walking to the Strip | Limited | No |
| Solve by combat / stealth / talk | All three for major quests (design rule: at least two of three) | Mostly | Combat default; talk occasionally | All three widely, plus skill-specific routes | Combat default | Combat |
| Talk the final boss down | **Yes** | No (must fight, can turn his guards and turrets) | Yes (Speech) for one antagonist | Yes, both possible final opponents | No | n/a |
| Kill-everyone run | Possible | Possible | Blocked by essential NPCs and unkillable children | **Possible**: one indestructible robot ally guarantees a path to an ending | Blocked by many essentials | n/a |
| Pacifist (zero kills) | Possible | Possible | Not practical `[UNVERIFIED]` | **Possible, with kill counter at 0** (documented runs) | Achieved once on Survival via proxy kills; the game "broke" repeatedly | No |
| Low-Intelligence run | Distinct dumb dialogue; many quests closed, a few unique reactions | More extensive and funnier | No | A handful of lines | No (Idiot Savant perk is a joke on the idea) | No |
| Joinable opposed factions | Minor | Crime families, towns | Effectively none | 4 major + many minor, mutually exclusive at defined points with explicit warnings | 4 major; can play three of them deep before lock-out | 2 (Settlers / Raiders), both can be maxed |
| Radiant / repeatable quests | None | None | A few repeatable turn-ins | A few repeatable turn-ins | **Many** (settlement defence, faction errands) and woven into faction progress | Daily quests and public events are the core |

Notes:

- Tim Cain has said the pacifist route in FO1 was not planned; it emerged from the multiple-solutions rule and
  the team kept it (PC Gamer headline; article body not retrievable this session).
- FNV's guarantee that *some* ending is reachable no matter whom you kill is the correct engineering answer to
  "let the player kill anyone": do not protect NPCs; provide a fail-safe path.
- FO4's essential NPCs and FO3's unkillable quest-givers are the opposite answer: protect the content from the
  player. It is cheaper and it tells players their agency is decorative.
- FO4 lets you work for three factions far into their arcs before lock-out, which serves the "see everything in
  one save" goal. FNV closes doors earlier and tells you when.

---

## 16. Endings

| | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Format | Narrated still slides, one per settlement/group | Same | Short narrated film montage | Narrated slides; several narrators including companions and faction voices | Short live-action-style/cinematic monologue | None; seasonal content |
| Variables | Each community's fate from your quest outcomes | Same, more of them | Karma tier, final choice, one optional atrocity | Faction victor, each town, each minor faction, each companion, karma tint | Mostly which side won | - |
| Post-ending play | No | **Yes** (with joke rewards) | No at launch; **added by Broken Steel** after backlash | No (final-battle autosave) | Yes | n/a |
| Reception | Beloved; the emotional gut-punch of the player's own exile | Liked | Criticised (forced sacrifice despite radiation-immune companions; Cain faulted endings not built from player decisions, per Wikipedia) | The gold standard | Criticised as thin; factions' endings nearly identical | - |

Ending slides cost a painting and a paragraph of narration each, and they are the main reason players believe
"my choices mattered" in FO1, FO2 and FNV. The cinematic endings of FO3 and FO4 cost more and say less.

The trade-off is real though: slides require the story to *stop*. Bethesda's players expect to keep playing,
and a world that keeps running cannot show a mutually exclusive future. FO2's "slides, then keep playing" is
a workable middle.

---

## 17. Time pressure

| Game | Mechanism | Outcome |
|---|---|---|
| FO1 | 150 in-game days to deliver the water part; buying water caravans adds 100 days (and hastens the enemy). Version 1.0 also had a hidden later deadline for the enemy army overrunning settlements, relaxed by patch. `[UNVERIFIED patch detail]` | Tension that suits the theme. Also the most common reason new players bounce. Cain says the timed quest is the one thing he would remove. Note: attendee notes of his GDC talk say a release-day patch "removed the quest", which conflicts with the shipped game still having the 150-day limit `[DISPUTED]`; most likely the patch removed the second, hidden deadline. |
| FO2 | No real limit (an engine limit of 13 years). Recurring dream sequences nag the player. | Nagging without teeth; players found the dreams annoying. |
| FO3 | None. | Father-hunt urgency is narrative only. |
| FNV | None. | The premise (revenge, then a slow-brewing war) fits untimed play. |
| FO4 | None. | Worst mismatch of the series: "find my kidnapped baby" vs. a game about building settlements for forty hours. |
| FO76 | Real-world timers: daily quests, seasons, limited events. | Pressure moved from the fiction to the calendar. |

The vision document explicitly wanted urgency ("a running clock keeps the player moving") while still giving
time to explore. The lesson of the series is not "timers are bad"; it is that a hard fail-state timer on the
*first* quest, before the player knows the world, punishes curiosity. FNV's lesson is to write a premise that
does not need one. FO4's lesson is that fake urgency is worse than none.

---

## 18. Difficulty and scaling

| | FO1 / FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Difficulty setting | Separate game difficulty (skill modifiers) and combat difficulty | 5-step slider: damage dealt/taken multipliers | Same slider + independent Hardcore toggle | Slider + Survival mode | None; fixed |
| Enemy placement | Fixed by location; random encounters by region | Level-scaled lists; each area's level locked at first visit `[UNVERIFIED]` | Mostly fixed placement; geographic danger | Encounter zones with minimum and maximum levels; scaled within band | Region bands at launch; **per-player scaling since One Wasteland (15 Sept 2020)** |
| Loot | Fixed | Level-scaled lists | Mostly fixed; level-gated vendor stock | Scaled lists + random legendary drops | Scaled + legendary rolls |
| Late-game threat | Gear check (power armor trivialises most things) | Bullet sponges after Broken Steel | DLC areas tuned for high level; base game gets easy | Health scales forever; legendary enemies mutate mid-fight | Bosses designed for groups |
| Feel | The world is what it is; you grow into it | The world grows with you | The world has dangerous places | The world has zones and grows with you inside them | The world is your level |

Reasoning:

- **Fixed worlds create memories** ("I ran from that thing at level 3 and came back at 20"). They also create
  walls for explorers and trivial late games.
- **Full scaling (FO3, post-update FO76)** guarantees content is always viable and guarantees progression is
  partly an illusion. FO76 needs it so friends of different levels can play together, which is a legitimate
  reason FO3 did not have.
- **FO4's zone bands** are the best compromise in the series: a level-10 zone and a level-40 zone both exist,
  and scaling only operates inside the band.
- Difficulty-as-HP-multiplier is universally the least liked option. Hardcore and Survival, which change
  rules, are the most liked.

---

## 19. Save systems

| | FO1 / FO2 | FO3 / FNV | FO4 | FO4 Survival | FO76 |
|---|---|---|---|---|---|
| Manual save | 10 slots (per page in FO2) `[UNVERIFIED]`, anywhere, including mid-combat | Unlimited, anywhere | Unlimited, anywhere | **None** | None |
| Quicksave / autosave | Quick-save key (FO2) `[UNVERIFIED]` | Quicksave; autosave on rest, travel, door | Same + exit-save | Save only on sleeping in a bed | Continuous server state |
| Reload culture | Heavy ("save early, save often" printed in manuals of the era) | Heavy; FO3's % speech checks invite it | Heavy; persuasion and legendary drops rerolled | Minimal; death costs real progress | Impossible; death drops carried junk |
| Design effect | Dice-heavy combat and bugs make reloads necessary | Thresholds (FNV) reduce the incentive | - | Makes beds, routes and settlements matter | No irreversible story choices are offered, since they could not be undone |

The save system quietly dictates what consequences a game can afford. Free saving plus random checks equals
reload loops (FO3). Deterministic checks (FNV) or restricted saving (FO4 Survival) both restore weight to
choices. A server-authoritative game (FO76) restores weight to loss but then refuses to offer weighty choices,
because players cannot recover from them.

---

## 20. UI: the Pip-Boy

| | FO1 / FO2 | FO3 / FNV | FO4 | FO76 |
|---|---|---|---|---|
| Device | Handheld Pip-Boy 2000 | Wrist Pip-Boy 3000 | Wrist Pip-Boy 3000 Mk IV | Wrist Pip-Boy 2000 Mk VI |
| What lives in it | Quest log, clock/rest, maps, archived videos. Character sheet and inventory are **separate screens** | Everything: stats, perks, inventory, quests, map, radio, notes | Same + holotape minigames, settlement data; perk chart is a separate poster screen | Same; plus a non-diegetic quick menu; real-money shop is a separate menu |
| Pauses game | Yes | Yes | Yes | **No** |
| Presentation | Full-screen art panel | Diegetic: the character raises an arm; monochrome CRT; tabbed lists | Same, animated mascot icons, colour-customisable; second-screen phone app; power armor has its own cockpit HUD | Same, plus photo mode, emote wheel |
| HUD | Bottom bar: weapon slots, AP lights, HP/AC counters, text log | Compass ribbon with markers, HP/AP bars, sneak state | Same + critical meter, favourites cross | Same + hunger/thirst (later reduced), team panel, event tracker |
| Known pain | Inventory is a single scrolling column; barter is clumsy | Long flat lists, slow on PC, no sorting/search | Lists still flat; junk management heavy; wheel dialogue hides text | Stash-weight management in a live game; menu does not pause in combat |

The Pip-Boy is the series' strongest piece of identity design: a diegetic menu that makes checking your
inventory an act *in the world* and gives the whole game its typeface, colour and mascot. It is also, as an
actual list interface, mediocre in every game. Identity and usability were never both achieved; PC players
have installed UI replacement mods for every 3D entry.

The original vision document's interface goal was "easy to use while still supporting complex actions"
(left-click acts, right-click opens the alternatives). That two-tier rule is still a good spec.

---

## 21. One-table summary: who did each system best

| System | Best in series | Why | Worst | Why |
|---|---|---|---|---|
| Character creation | FO1/FO2 | Stats + traits + tags commit you before play | FO3 | Choices wash out by mid-game |
| Skills | FNV | Audited, checked everywhere | FO3 | Trivially maxed |
| Perks | FO2 / FNV | Scarce, rule-changing | FO3 (filler), FO4 (% tax) | Abundance or incrementalism |
| Combat feel | FO4 | Solid shooter, crit meter | FO3 | Weak gunplay, VATS invulnerability |
| Combat depth | FNV (ammo, DT) / FO2 (tactics) | Meaningful loadout decisions | FO3 | Single-number armor |
| Survival | FO4 Survival / FNV Hardcore | Rules, not multipliers | FO76 launch | Chore meters online |
| Dialogue | FNV | Thresholds, breadth, fail lines | FO4 | Wheel + voice |
| Reactivity | FNV, FO2 | Reputation, slides, killable NPCs | FO4 | Essentials, converging endings |
| Exploration | FO4 / FO3 | Density, found stories | FO1/2 (by modern taste) | Abstract map |
| Crafting / loot loop | FO4 | Junk-as-components | FO1/2 | None |
| Companions | FNV | Arcs + gameplay perks | FO1 | Uncontrollable |
| Economy | FNV | Real sinks, multi-currency worldbuilding | FO3 | Nothing to buy |
| Endings | FNV / FO1 | Granular slides | FO4 | Near-identical outcomes |
| UI identity | FO3 onward | Wrist Pip-Boy | - | - |

---

## Design Takeaways

Character and progression

- **Decide which of the three games you are making** (stat RPG, hybrid, looter-shooter) and build every system
  to agree. Fallout's worst-received features (FO3 skills, FO4 dialogue, FO76 launch) are all cases where one
  layer was built for a different game than the layer next to it.
- **Budget scarcity is build identity.** Keep a hard cap on total character power (a level cap, or FO76-style
  active-slot budget). If the game must be endless, cap what is *equipped*, not what is *owned*.
- **Every stat needs at least two systems that read it, one of them non-combat.** Audit for a dump stat before
  shipping. Do not let any stat multiply XP or skill points; that makes it mandatory.
- **Keep creation-time trade-offs (traits).** They are cheap, memorable and the first thing players describe.
  Balance them so no trait is an auto-pick.
- **Perks should change rules, not add percentages.** Give one every 2-3 levels. Put incremental growth in a
  separate, quieter channel so perks stay special.
- **Audit skill usage with a tool**, the way Obsidian tracked checks. "No useless skills" is a production
  process, not a pillar on a wall.
- **Front-load build recognition.** The first hour should acknowledge several different builds.

Combat and survival

- **Use a threshold-plus-floor armor model** (flat reduction with a guaranteed minimum bleed-through). It makes
  weapon and ammo choice tactical and stays readable. Avoid opaque exponent curves the player cannot reason
  about, and never allow zero-damage dead ends.
- **Scale threat, not health.** New enemy behaviours and compositions at higher tiers; no bullet sponges.
- **If there is an aim-assist/tactical mode, make it a resource game** (a banked critical meter) rather than a
  pause-and-be-invulnerable button.
- **Ship the survival ruleset as a first-class mode from day one**, designed with the map, not patched in.
  Heal-over-time, ammo weight and bed-based saving make existing content matter.
- **Radiation-as-max-health-loss** is the clearest hazard model in the series. Reuse the idea of one visible
  bar being eaten by a persistent environmental cost.

Dialogue and reactivity

- **Silent protagonist, full-sentence responses, visible threshold checks across many skills.** Add what FNV
  lacked: tagged options that are sometimes worse or merely different, so a tag informs rather than wins.
- **Write failure.** Failed checks and low-stat characters should get distinct content, not a greyed-out line.
- **Track per-group reputation on two axes; do not score morality.** Let good and bad deeds coexist. Add
  disguises or other ways to play with identity.
- **Nobody is essential; build one fail-safe route to an ending.** That single design decision buys
  kill-everyone runs, pacifist runs and the feeling that the world is not protecting itself from you.
- **Budget for ending slides early.** They are the cheapest high-impact reactivity in the genre. If the world
  must continue afterwards, show the slides and then resume.
- **No fake urgency.** Either give the main quest a real, fair, visible clock that starts after the player has
  their bearings, or write a premise that tolerates wandering.

World, loot and economy

- **Choose map abstraction deliberately.** A node map buys scale, plausible geography and big towns cheaply.
  A seamless world buys presence and found stories at the cost of compression. A hybrid (seamless regions
  joined by an abstract overland layer with encounters) is under-explored.
- **Make junk matter, but cap the bookkeeping.** Components-from-junk is excellent; pair it with generous
  auto-sorting and avoid stash-weight as a monetised pressure.
- **Design sinks before faucets.** Expensive, build-relevant purchases (implants, rare ammo, training) keep
  money meaningful to the end. Use faction currencies as worldbuilding.
- **Use fixed danger with zone bands**, not global scaling. Let players meet something they must run from, and
  teach the map through it.
- **Tie the save model to the consequence model.** Deterministic checks if saving is free; restricted saves
  if checks are random.
- **Invest in a diegetic interface for identity, and separately make the lists good** (search, sort, compare).
  Fallout proved the first half and never delivered the second.

## Sources

Consulted this session (fetched, or search-result summaries used):

- Fallout GURPS-era vision statement, repost and commentary: https://rpgcodex.net/article.php?id=8028
- Notes on Tim Cain's GDC 2012 "Classic Game Postmortem: Fallout": https://thiscageisworms.com/2012/04/09/tim-cains-gdc-2012-talk-fallout/
- fallout.wiki, damage overview: https://fallout.wiki/wiki/Overview:Damage
- fallout.wiki, Damage Resistance (overview): https://fallout.wiki/wiki/Damage_Resistance
- fallout.wiki, Damage Resistance (Fallout 4): https://fallout.wiki/wiki/Damage_Resistance_(Fallout_4)
- fallout.wiki, Damage Threshold (Fallout: New Vegas): https://fallout.wiki/wiki/Damage_Threshold_(Fallout:_New_Vegas)
- fallout.wiki, Damage Resistance (Fallout 3): https://fallout.wiki/wiki/Damage_Resistance_(Fallout_3)
- fallout.wiki, DT overview: https://fallout.wiki/wiki/DT
- fallout.wiki, Fallout primary statistics: https://fallout.wiki/wiki/Fallout_primary_statistics
- fallout.wiki, Fallout 4 perks: https://fallout.wiki/wiki/Fallout_4_perks
- fallout.wiki, Fallout 76 SPECIAL: https://fallout.wiki/wiki/Fallout_76_SPECIAL
- fallout.wiki, One Wasteland For All: https://fallout.wiki/wiki/One_Wasteland_For_All
- Nukapedia, Damage Modifier (search summary): https://fallout.fandom.com/wiki/Damage_Modifier
- NMA forum threads on the FO1/FO2 damage formula (search summaries): https://nma-fallout.com/threads/need-help-calculating-damage.181260 and https://nma-fallout.com/threads/ammo-explanations-for-dummies.181377
- BGforge forum, AP/JHP ammo analysis (search summary): https://forums.bgforge.net/viewtopic.php?f=26&t=129
- GOG forum, FO2 ammo damage question (search summary): https://gog.com/forum/fallout_series/fallout_2_ammo_damage_question
- Steam discussion on FNV DT/DR (search summary): https://steamcommunity.com/app/22380/discussions/0/1638668751263729391/
- Gameranx on Sawyer and save scumming (Kinda Funny interview): https://gameranx.com/updates/id/402854/article/fallout-new-vegas-director-didnt-like-save-scumming-in-fallout-3/
- 80.lv on Sawyer and skill-check distribution: https://80.lv/articles/fallout-new-vegas-lead-on-how-game-developers-distribute-skill-checks
- GamesRadar on Sawyer and the FNV opening (search summary): https://www.gamesradar.com/games/fallout/fallout-new-vegas-director-josh-sawyer-explains-why-the-rpgs-opening-is-a-perfect-example-of-respecting-the-players-skill-choices
- PC Gamer, Sawyer on skill coverage and persuasion (headlines only retrievable): https://www.pcgamer.com/games/rpg/fallout-new-vegas-director-on-the-art-of-making-sure-all-your-points-in-persuasion-arent-wasted-its-all-about-feelings-but-you-use-numbers-to-arrive-at-that-feeling and https://pcgamer.com/games/fallout/fallout-new-vegas-director-josh-sawyer-says-obsidian-has-karma-police-who-go-through-the-game-making-sure-every-skill-gets-enough-cool-stuff-to-do-were-not-gonna-leave-you-out-to-dry/
- PC Gamer, Sawyer on deathclaws and cazadores as a warning (search summary): https://pcgamer.com/games/rpg/josh-sawyer-says-fallout-new-vegas-has-deathclaws-in-cazador-as-a-warning-to-fallout-3-players-expecting-another-easy-ride-you-cant-just-slide-all-over-the-map-and-not-feel-the-heat
- GameBanshee, "Reputation Overload" by Josh Sawyer (search summary): https://www.gamebanshee.com/36qhk
- PC Gamer, Howard on FO4 dialogue (2016 and later): https://www.pcgamer.com/au/fallout-4-lead-todd-howard-dialogue-system-didnt-work-as-well and https://www.pcgamer.com/games/rpg/todd-howard-says-that-fallout-4s-cinematic-dialogue-system-really-did-not-resonate-with-players-even-though-bethesda-spent-forever-working-on-it
- Escapist, "Fallout 4 Eliminates Skills From Character System" (search summary): https://www.escapistmagazine.com/fallout-4-eliminates-skills-from-character-system/
- PC Gamer, FO1 pacifist playthrough was accidental (headline only): https://www.pcgamer.com/the-original-fallouts-pacifist-playthrough-was-an-accidental-inclusion-but-its-designers-loved-the-idea-so-much-they-kept-it-in
- Kotaku, FNV zero-kill run (search summary): https://kotaku.com/this-guy-beat-fallout-new-vegas-with-zero-kills-5683023
- Guinness World Records, FO4 Survival pacifist completion: https://www.guinnessworldrecords.com/world-records/438856-fastest-pacifist-completion-of-fallout-4-on-survival-mode
- The Mary Sue, "Breaking Fallout 4 With Pacifism" (search summary): https://www.themarysue.com/breaking-fallout-with-pacifism/
- Wikipedia: https://en.wikipedia.org/wiki/Fallout_3 , https://en.wikipedia.org/wiki/Fallout:_New_Vegas , https://en.wikipedia.org/wiki/Fallout_4 , https://en.wikipedia.org/wiki/Fallout_76

Not reachable this session (attempted): Nukapedia "Fallout 76 combat" (HTTP 402), fallout.wiki FNV reputation
page (404), a Tim Cain video-summary wiki (login wall). Josh Sawyer's GDC 2012 talk
(https://gdcvault.com/play/1015758/Do-(Say)-The-Right-Thing) was identified but not viewed.
