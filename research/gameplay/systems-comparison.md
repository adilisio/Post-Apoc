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
- V.A.T.S. is a "bridge" mechanic: it lets a stat-driven character fight in a shooter. It went pause + 90%
  damage reduction (FO3) -> pause + 25% reduction (FNV) -> slow-motion + banked crit meter (FO4) -> real-time aim
  assist (FO76). The more the real-time half improved, the less the bridge was needed (section 22).
- Real-time vs. turn-based changes what stats are *for*: turn-based makes AP/Sequence the master stats; real-time
  makes aim and reflex player-owned, so stats must be re-routed into damage, durability and utility (section 23).
- Item condition existed only in FO3, FNV and FO76. FO4 removed it for weapons and armor (power armor excepted)
  and replaced the repair sink with junk-to-components crafting. FO76 then sold repair kits for premium currency
  (April 2019, patch 8.5) and drew a pay-to-win backlash (section 24).
- Hard numbers worth remembering: FO1/2 aimed-shot penalties Head -40, Eyes -60, Groin -30, Arms -30, Legs -20;
  FO3 VATS hit cap 95%, crit +15, player takes 10% damage; FNV VATS player takes 75%; FO4 queue limit 16
  attacks; FO3 repair cap = 40% + 0.6% x Repair skill.

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
| Agility | **Action Points (5 + AG/2)**; Armor Class; gun skills | AP (65 + 2/pt); Small Guns, Sneak | AP (65 + 3/pt); reload and draw speed; Guns, Sneak | AP (60 + 10/pt); sneak; gates Gunslinger, Commando, Sneak | AP 105 + 10/pt per fallout.wiki (earlier draft said 60 + 10; corrected); sneak; pistol/auto cards |
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
| Critical hits | Luck % roll per shot; crit tables with instant-death and knockdown results | Luck % in real time; +15 crit chance in VATS (fVATSCriticalChanceBonus = 15, fallout.wiki; FNV's VATS bonus is only 5) | Luck % × weapon crit multiplier | **No random crits outside perks**; meter fills in VATS, player banks and spends | Same meter |
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

## 22. V.A.T.S. evolution

Verification key for sections 22-24: figures marked with a fallout.wiki page name were read this session.
Developer quotes reached only as search-result summaries or headlines are labelled as such. Anything else is
`[UNVERIFIED]`.

### 22.1 Lineage in one table

| | FO1 / FO2 aimed shots | FO3 V.A.T.S. | FNV V.A.T.S. | FO4 V.A.T.S. | FO76 V.A.T.S. |
|---|---|---|---|---|---|
| Time model | Turn-based; the whole game is paused between actions | **Full pause**; cinematic slow-motion kill cam on execution | Same pause | **Slow-motion, not pause** | **Real time, no slowdown**; you can move; enemies can dodge |
| Targeting | 8 body regions chosen from a menu: head, eyes, torso, groin, arms, legs | Limbs, head, torso (no eyes/groin) | Same; melee and grenades are "full body" only | Same; hit chance shown per part and per target | Off by default for limbs: needs the **Concentrated Fire** perk card; otherwise it auto-targets the body |
| Cost model | AP; aimed shot costs extra AP | AP pool 65 + 2 x AG, spent per queued shot | AP pool 65 + 3 x AG; unarmed special moves 20 AP | AP pool 60 + 10 x AG, **shared with sprint**, scope breath-hold and jetpack; up to 16 queued attacks | AP pool 105 + 10 x AG (fallout.wiki; Agility starts at 1, so early VATS is rare); in power armor it drains the fusion core (a fresh core equals 2,000 AP) |
| Hit chance | Dice: skill, range, light, AC, then the region penalty | Capped 95% (fVATSMaxChance); non-linear range falloff (fVATSDistanceFactor 2); spread halved (0.5) | Same family | Capped by Perception-driven percentage; Penetrator shoots through cover | Capped 95%; reduced by distance, visibility, body-part difficulty, range, cone of fire, fire rate and recoil; Perception made more relevant by patch 1.7.21.25 |
| Crits | Region penalty converts to crit chance (see 22.2) | +15 crit chance in VATS | +5 crit chance in VATS | **No random crit chance**: a meter fills from VATS hits, guaranteed hit when spent | Same meter, spent by a button on the VATS screen |
| Damage to player while in VATS | n/a (turn-based) | **10%** of normal (fVATSPlayerDamageMult 0.1) | **75%** of normal | Reduced; magnitude `[UNVERIFIED]` | None (real time) |
| What it was for | The only way to shoot, so a core tactical layer | Bridge: stat-driven hit chance inside a first-person shooter | Optional bridge; iron sights make real-time viable | Resource game layered on a competent shooter | Aim assist with a stat-based hit chance in a shared world |

### 22.2 FO1 / FO2: aimed shots (the ancestor)

- **Region penalties** (default hit modifiers from the Fallout 2 critical-table documentation at fodev.net):
  Head -40, Eyes -60, Groin -30, each arm -30, each leg -20, Torso 0. An uncalled shot counts as torso.
- **Crit coupling.** For a normal attack the game rolls against critical chance minus the region modifier. Because
  the modifiers are negative, an aimed shot gains crit chance equal to the penalty. A harder target is a riskier
  shot with a higher crit ceiling. That is the whole design in one line: the player buys crit chance with hit chance.
- **Crit severity roll.** Once a hit is a crit, the game rolls 1-100 and adds the attacker's Better Criticals
  stat (+20; Heavy Handed subtracts 30). Result tiers: up to 20 = tier 0, 21-45 = 1, 46-70 = 2, 71-90 = 3,
  91-100 = 4, above 100 = 5. Tables are indexed by target type and hit location.
- **Crit effects** in the tables: knockout, knockdown, blinding, crippled limb (left/right arm or leg, or random),
  instant death; extra flags include ignoring armor, dropping the weapon, losing the next turn and setting the
  target on fire.
- **AP cost.** The community-patch fo2238 wiki lists an aimed shot at +2 AP for eyes, head or groin and +1 AP for
  other regions. Original-game values were not confirmed `[UNVERIFIED]`.
- **Fast Shot** (trait) blocks aimed shots entirely in exchange for cheaper single shots (the official-style wiki
  lists 1 AP less; the fo2238 wiki lists 1 or 2 less depending on weapon hands). Burst fire cannot aim, so bursts
  land on the torso and rarely crit (NMA forum thread; whether burst crits roll per bullet or per burst is
  disputed `[DISPUTED]`).
- **Dominance.** Aimed shots were optional but were the signature of the strongest builds (sniper-style
  Perception/Luck characters with Better Criticals and Sniper) while Bonus Rate of Fire/burst builds went the other
  way and ignored them. A choice of "precision or volume" per weapon is the part VATS inherited.
- **Reception.** Not a controversy; it was simply how the game worked. Worth noting that the eyes shot, the
  crit-text log and the death animations are the most remembered flavour of the combat.

### 22.3 FO3: why it was built, and what it cost

Why Bethesda built it:

- Howard's origin story, repeated in several interviews and summarised by PC Gamer and fallout.wiki: Burnout's
  crash mode "with body parts" ("imagine the car parts are like eyeballs and guts"). He wanted combat that mixed
  real-time and turn-based and was "cinematic" (Wikipedia, FO3 article). He has also compared the structure to
  phase-based combat in KOTOR (PC Gamer summary).
- A slow-motion version was considered, but a full pause was chosen so players could "assess the situation
  tactically" (fallout.wiki). AI programmer Jean Simonet built the changing slow-motion camera (Wikipedia).
  Lead artist Istvan Pely told EDGE that the team agonised over whether a low-skill character who misses what it
  aims at would be satisfying or merely frustrating, spent a long time wondering "is this even fun?" and only
  just got VATS working shortly before shipping (frvr.com summary of the EDGE interview).
- Emil Pagliarulo's framing, from interviews (Play.tm repost, Strategy Core 2007, GameTap): Bethesda wanted to
  honour the original's tactical turn-based roots without forcing an isometric turn-based game on everyone ("not
  every Fallout fan wants a turn-based isometric game"). The name is a homage to the FEV vats of the original game
  (fallout.wiki). He also said the studio had not done gun combat since the Terminator games, so shooting itself
  was a hard problem (GamesRadar). I could not retrieve the full original articles; wording is from summaries
  `[UNVERIFIED exact quotes]`.
- Joel Burgess: "We didn't really have first-person shooter experts" (Wikipedia, FO3 article). Developers later
  judged the shooting a weak point, and Howard has reportedly agreed it is only mediocre as a shooter.

Numbers (fallout.wiki Fallout 3 V.A.T.S. page):

| Item | Value |
|---|---|
| Max hit chance | 95% |
| Crit chance bonus | +15 |
| Damage taken by player while in VATS | 10% (a 90% reduction) |
| Spread in VATS | multiplied by 0.5; stealth also halved |
| Automatic melee damage | doubled |
| Max engage distance | 5,000 units; melee reach doubled |
| Weapon wear in VATS | the page says 4x in text and lists a setting of 5 `[DISPUTED]` |
| Concentrated Fire | +5% accuracy per extra shot at the same part |
| Cripple effects | head cripple gives the target -4 Perception; crippled arms lower melee damage 5-10% |
| Perk hooks | Paralyzing Palm (30% of VATS hits), Mysterious Stranger (10% chance, targets under 150 HP) |
| Limits | you cannot move or dodge; mines show 0% |
| AP cost per shot | set per weapon; no table retrieved `[UNVERIFIED values]` |

How the real-time half worked (this is what made VATS necessary): in real time the Small Guns skill adds about
3.5% damage per 5 points with diminishing returns and shrinks projectile spread; scoped weapons have no sway at
skill 100 (fallout.wiki Small Guns (FO3)). A low-skill character therefore genuinely misses at the crosshair.
VATS is the escape from that: hit chance is a number, not an aim.

How dominant and how exploitable:

- Dominance: effectively mandatory for low-skill builds and for anything past mid-range; optional for skilled
  characters with short-range shotguns and melee.
- The 90% damage reduction is the central exploit: anything inside a VATS sequence is nearly safe, and you can
  fire, cripple and reset on AP regeneration. Designers describe the net effect as an "I win" button (the
  analysis in section 6 above).
- Weapon wear multiplied while in VATS (see the table) is the only built-in cost; see section 24.

Reception:

- Praised as the identity of the game and a clever bridge. 1UP's Demian Linn found VATS enjoyable but the
  real-time encounters imprecise (Wikipedia summary).
- Savaged by classic-RPG fans. A CanardPC review quoted by RPG Codex called the VATS slow-motion kill cam ugly,
  unskippable and so long that players would avoid using the targeted-shot system, and guessed it was padding or
  face-model showmanship. Codex forum voices called VATS a "gimmicky compromise" and a failure to use basic RPG
  ideas properly (search summaries of RPG Codex pages).
- The game it served scored 91 on Metacritic PC at launch (see Quick Reference), so the gimmick did not hurt sales
  or scores.

### 22.4 FNV: reduced invulnerability, real sights, melee moves

- **Player takes 75% of normal damage** in VATS (fallout.wiki), a 25% reduction instead of FO3's 90%. VATS
  became a damage-and-accuracy tool rather than a shield. Melee and unarmed damage is still automatically doubled.
- **VATS crit bonus fell from +15 to +5.**
- **AP pool** 65 + 3 x Agility (fallout.wiki Action Points): more AP than FO3 per point, spent on each shot.
- **Special moves.** Any melee weapon unlocks a special attack at Melee Weapons 50; unarmed Uppercut and Stomp at
  skill 50, Cross at 75. Unarmed specials cost a flat 20 AP. This gave melee builds a real VATS identity instead of
  a free-for-all.
- **Real iron sights** and skill/Strength/condition-based spread (existing section 6 table) made the real-time half
  viable, which is why FNV VATS reads as an option. Mines always show 0%, thrown explosives show 0% on PC (bug,
  fixed by community patch), and automatic weapons always fire a full burst.
- **Reception.** The reduced safety window and the 25% number were rarely complained about; the common view in
  the community is that FNV's gunplay is better balanced than FO3's `[UNVERIFIED, forum consensus, no source
  retrieved]`. Sawyer's DT work (section 23) did more to restore tactical meaning than VATS changes did.

### 22.5 FO4: slow-motion and the banked critical

- **Slow-motion rather than pause.** The enemy keeps acting, you can still be hurt, and reloads are not slowed
  (fallout.wiki lists a bug about reload sounds). The slow-down factor and the exact damage reduction were not
  published on the page I could reach `[UNVERIFIED]`.
- **AP is shared with sprint** (60 + 10 x Agility). Every VATS use competes with movement, so VATS stops being a
  free reset button. Power armor with an empty fusion core cannot use VATS at all.
- **Queue up to 16 attacks.** An automatic weapon's single AP cost covers one burst of about three rounds. Scopes
  roughly double the AP cost; reflex sights lower it; muzzles do nothing. Quick Hands rank 2 makes reloads free of
  AP.
- **The critical meter** (the best idea of the FO3-era VATS): a meter fills from successful VATS hits, and Luck
  sets how quickly. Spent crits are guaranteed to hit if the displayed chance is above zero and **bypass damage
  and energy resistance** (fallout.wiki V.A.T.S. page). Hits needed to fill the meter by Luck (fallout.wiki Luck):

| Luck | 1 | 2 | 3 | 4 | 5 | 6-7 | 8-9 | 10-12 | 13-18 | 19-29 | 30-62 | 63+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hits to fill | 14 | 12 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

- **Banking.** Critical Banker (Luck 7, ranks at levels 17, 43 and 50) stores 1-4 crits while the meter keeps
  filling. Four Leaf Clover (Luck 9) gives hits a chance to fill the meter outright. Mysterious Stranger, Grim
  Reaper's Sprint and Ricochet can also fill it.
- **Exploits.** A Lucky weapon plus the Isodoped companion perk fills the meter in two shots at Luck 14 (wiki
  note), and meter-recharge stacking lets high-Luck builds crit nearly every shot. Gun Fu rank 3 guarantees a
  crit from the fourth target onward. Known glitches: a crouching enemy's body can block headshots, and the camera
  can freeze when you strafe.
- **Perk web.** About fifteen perks touch VATS: Iron Fist, Awareness (shows resistances), Concentrated Fire (+10,
  +15 or +20% accuracy on repeat hits to one part), Penetrator, Sniper (+25% headshot accuracy with scoped
  non-automatic rifles at rank 3), Action Boy/Girl, Blitz, Gun Fu, Quick Hands, Better Criticals, Critical Banker,
  Four Leaf Clover, Grim Reaper's Sprint, Mysterious Stranger, Killshot (companion).
- **Dominance and what it was for.** VATS is optional for most players because the shooter is competent; it is
  mandatory only for Luck-crit builds, which turn it into a turn-based minigame inside the real-time world. The
  design intent was "bridge between stats and shooting" less than "reward a banked resource".
- **Reception.** Players overwhelmingly liked the slow-motion version and the crit meter (including because
  it replaced FO3's invulnerability). Critics' complaints concentrate on Luck as a god stat and on the
  resistance bypass making high-DR enemies trivial for VATS builds `[UNVERIFIED, community opinion, no source
  retrieved]`.

### 22.6 FO76: real-time and card-gated

- Todd Howard told Geoff Keighley at E3 2018 that VATS is real-time with no slowing but still lets you pick
  targets and body parts (PCGamesN / PC Gamer / GamingBolt coverage, summaries). Reporters tied the change to
  multiplayer: slowing time for one player would slow it for everyone, which is also hard to do technically in
  an online game with PvP. I found no direct Howard quote about alternatives `[UNVERIFIED]`.
- Mechanics: you can move while queued; enemies can dodge; targeting limbs needs the Concentrated Fire card
  (Shacknews, Prima Games). The crit meter is spent from a button on the screen, and critical damage is **added
  to** paper damage rather than multiplied, with a base multiplier of usually 2.0 (fallout.wiki FO76 damage).
- **Why multiplayer forced it:** a shared server cannot honour a pause or a slow-down for one client; any
  VATS must therefore be an aim assist with hit-chance math, not a time-bending mode.
- **Dominance:** an essential tool for VATS-stealth and crit builds, optional for the large share of players using
  automatic weapons manually. The hit-chance changes of patch 1.7.21.25 (recoil and cone of fire matter more,
  large enemies measured from their outer bounds) show Bethesda retuning it for fairness.
- **Reception:** PC Gamer's headline on the reveal footage called it "pretty disappointing", and Altchar called
  it "underwhelming and unfinished" (headlines only); later reviewers described real-time VATS as "out of place".
  Players kept using it for the build flexibility, not for any tactical pause.

### 22.7 Judgement: what VATS solves, and the alternatives

| Problem | How VATS solves it | Cost | Alternative solutions used elsewhere |
|---|---|---|---|
| A stat-based character needs a stat-based chance to hit inside a first-person shooter | Hit chance is a displayed number, not your aim | Breaks pacing; creates a second combat mode; invites invulnerability exploits | **Skill-driven reticle bloom and sway**: Deus Ex (2000) improves accuracy +0, +5%, +12.5%, +25% from untrained to master and reduces recoil and scope sway (Deus Ex wiki). Fallout 3 and 4 both tried versions of this in real time. Pure RPG dice in real time was Mass Effect 1's approach, and its remaster retuned bloom to be more controlled (EA/GameBanshee note) |
| Player is not a twitch shooter | Pause or slow lets thinking players compete | Turns a shooter into a menu | **Real-time with pause**, **turn-based hybrids** (Fallout Tactics CTB, Wasteland 2/3, Van Buren's planned dual mode), or **auto-aim and cover systems** `[UNVERIFIED for specific games]` |
| Players want aimed shots and body-part gore | Targeted limbs, cripples, cinematics | Heavy animation budget | **Always-on location damage** that applies to real-time aim (limb damage as in FO4 itself); or **stat-gated headshot multipliers** |
| Character power must remain visible | You can see the percentage rise with Perception/Agility | Number may be irrelevant if you can aim | **Decouple hit from stats** and let stats scale damage, durability and utility instead (FO4/FO76 direction) |
| Rewarding mastery | Crit meter turns a hidden roll into a banked, timed resource | Luck becomes god stat | Cooldown-based skill triggers; bonus damage for stat-gated headshots |

Opinion: VATS is the best answer to "character skill vs. player skill" when the studio cannot make the shooting
good (FO3's case), and the worst answer when it can (FO4, FO76). Its most transferable parts are not the pause but
(a) a displayed hit chance per target region, (b) a cost in a spendable resource and (c) FO4's banked crit.

---

## 23. Real-time vs. turn-based balance

### 23.1 How each model changes the value of stats and builds

| Axis | FO1 / FO2 (turn-based) | FO3 (real-time + VATS) | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Master stat | **Agility** (AP = 5 + AG/2) and **Perception** (Sequence decides who acts first) | Intelligence for skill points; Agility for VATS AP (65 + 2 x AG) | Same as FO3 but AP is 65 + 3 x AG | Agility/Luck for VATS crit builds (AP 60 + 10 x AG) | Weapon-class stat via card slots; AP 105 + 10 x AG |
| What the stat does in the fight | Decides how many actions you get, in what order, with what accuracy | Skills drive spread and sway; stats drive VATS pool | Skills and Strength drive spread; Strength has weapon minimums | Barely touches accuracy; mostly damage perks | Same as FO4 |
| Companion value | Each companion is a pool of AP that can finish the fight on the turn they act; uncontrollable in FO1 | Meat shield and extra damage; one at a time | Wheel commands; perks | Command cursor; invulnerable essential | None |
| Encounter design | Hand-built positions and random encounters; combat is a gear check | Level-scaled spawns; you meet whatever the lists produce | Fixed placements with DT-gated threats | Level bands; legendary mutants | Event-based public arenas |
| Difficulty lever | Enemy stats and your build | HP multipliers and damage multipliers | DT thresholds and enemy placement | Enemy HP scaling and legendary spawns | Server-side balance |
| Natural dominant build | Burst fire or sniper with Better Criticals | Small Guns/Energy build abusing VATS invulnerability | Guns with AP rounds plus DT-breaking ammo | Luck-crit VATS or rifle build | Whatever the current meta is |

**FO1 / FO2: the AP economy.**
- Base AP is 5 + Agility/2 (fallout.wiki Action Points). Typical costs from the existing section 6 table: move 1/hex,
  shoot 4-6, reload 2, inventory 4 (2 in FO2 `[UNVERIFIED]`). One extra AP point therefore is worth roughly
  one extra hex of movement or a quarter of a shot, which is why Agility is the god stat.
- **Sequence** (2 x Perception, existing section 1.2) decides who acts first. A fast opponent that hits first can
  win the fight outright, so Perception and the Kamikaze trait (which trades defence for Sequence) are considered strong for the same
  reason `[UNVERIFIED: trait numbers not re-checked]`.
- **Burst fire and crit dominance.** Guides for FO2 list Bonus Rate of Fire, Better Criticals, Sniper, Slayer and
  Bonus Ranged Damage as standard burst-build perks (Steam/GOG/NMA threads). The NMA community notes that burst
  shots land on the torso, so burst builds trade crit potential for volume, and that a sniper with Luck 10 and
  the Sniper perk is described by one reader as a 100% crit chance (disputed `[DISPUTED]`). Fast Shot is mocked in
  FO2 and defended only for burst/rocket builds.
- **Effect on difficulty.** Turn-based combat is solvable: more AP, a better first strike, and a good weapon beats
  most encounters. The challenge comes from setup and resource attrition rather than from execution.

**FO3: skills versus a player who is aiming.**
- The game spent a character's skill on spread and sway and let the player's own aim also matter. Result: a
  low-skill character misses at the crosshair even when the cursor is on target. Pely's EDGE remark (22.3) shows the team
  knew this would "feel frustrating".
- Small Guns skill adds roughly 3.5% damage per 5 points with diminishing returns. A skill-100 sniper rifle has no sway.
  By the time skills could be maxed (cap raised to 30), skill stopped mattering.
- Percentage-only DR (cap 85%) removes the "right weapon for the job" decision; the numbers are on the Pip-Boy but
  the enemy health bar shows only a percentage, so players cannot see whether armor is working (RPG Codex
  summary of Sawyer, May 2010).

**FNV: DT versus DR and why Sawyer changed it.**
- Sawyer announced that damage threshold was returning to the series (RPG Codex, 2 May 2010). Stated problems with
  FO3: enemy health bars that show only a percentage hide how well armor is working, whereas FO1/FO2 numbers made
  it clear. FNV added a shield icon that shows when a hit does no more than the target's threshold.
- Rationale in his own words, as relayed by search summaries: a small percentage of damage can still get through
  the thickest armor, but a threshold can neutralise small arms. That is the tactical value: small-damage weapons
  stop working against heavy armor, which creates weapon-class roles.
- Formula (section 7): `afterDR = damage x (100 - min(DR, 85))/100`, then `final = max(afterDR - DT, damage x 0.2)`.
  The 20% floor stops DT from becoming a dead end.
- Sawyer says his balance work was "mostly vibes", using a weapons spreadsheet by ammo type and base damage for
  maybe a couple of months and then playtesting by feel (PC Gamer / GamesRadar headlines). He also said he
  wanted FNV to be harder than FO3 or Skyrim without just raising numbers (PC Gamer summary). A forum claim that he
  considered BB guns damaging power armor deliberate is unverified `[UNVERIFIED]`.

**FO4: bullet sponges and level scaling.**
- Enemies' health scales inside zone bands, and legendary enemies add mutation and healing. Steam and Nexus
  Mods threads repeatedly call this a bullet-sponge design ("7-8 headshots with a sniper to kill a super mutant,
  double or triple that for a legendary") and argue the legendary mutation heal is pointless on Survival
  (community forum quotes; no critic piece retrieved).
- Counter-argument players give: durability cuts both ways, since enemies that die in one shot also mean you die
  in one shot; Survival mode reportedly increases your damage to compensate for the sponginess `[UNVERIFIED]`.
- Mods such as SCOURGE plus True Damage exist to rebalance this.

**FO76: server-side balance and damage metas.**
- A shared economy and PvP force Bethesda to retune numbers on live servers. Damage bonuses became mostly additive
  after One Wasteland (Sept 2020); the resistance multiplier is clamped between 0.1 and 0.99; ranged damage
  falls to 0.5x at 200% of range (fallout.wiki FO76 damage page).
- **Bloodied** adds 1.37% damage per 1% missing health: 0% at full health, 68.42% at 50% and 130% at 5% (fallout.wiki
  Bloodied). Builds stack it with low-health perks and VATS stealth crits.
- Nerf history seen in coverage: Patch 5 nerfed the explosive shotgun and other legendaries (Newsweek); players
  reported unlisted "stealth" nerfs in December 2018, including reduced enemy XP and production (MP1st, mein-mmo);
  Patch 6 nerfed Scorchbeasts (mein-mmo); PC Gamer reported another Atlantic City weapon nerfed with
  compensating buffs. Users report bloodied/VATS builds halved by Gleaming Depths-era changes (Steam, anecdotal)
  `[UNVERIFIED]`.
- Pattern: each nerf punishes whoever followed the meta, so balance becomes a recurring community fight.

### 23.2 The argument and the counter-argument

| | Classic-fan position (NMA, RPG Codex) | Counter-position |
|---|---|---|
| Core claim | Fallout *is* a turn-based tactical RPG; real-time with VATS is a gimmick that wastes the stat system | Fallout was always a mix: a real-time exploring RPG that switches to turn-based combat; Bethesda wants both audiences |
| Evidence cited | RPG Codex called VATS "a gimmicky compromise" and a failure to capitalise on basic RPG concepts; CanardPC mocked the slow-motion kill cam | Pagliarulo: "not every Fallout fan wants a turn-based isometric game"; VATS is the nod to tactical players |
| Strength of argument | Skills mean little when aim decides hits (FO4); characters converge | Turn-based combat costs animation and AI budget, and sells to a smaller audience; FO3 scored 91 and FO4 84 on Metacritic PC |
| Weakness | Dismisses many players who prefer real-time | Real-time versions repeatedly removed stat identity |
| Truth in between | Stat expression requires a mechanism that translates stats into outcomes | The mechanism does not have to be turns |

### 23.3 Hybrid models and their reception

| Model | Game | Detail | Reception |
|---|---|---|---|
| Continuous turn-based plus real-time | Fallout Tactics (2001) | Three modes: Continuous Turn-Based (everyone acts at once, AP regenerates with Agility), Individual Turn-Based, Squad Turn-Based; sentry modes. Combat planned as strict turn-based; the real-time at E3 2000 was faked; developers redesigned for real-time after the turn-based mode was not fun (fallout.wiki) | Metacritic 82; GameSpy 89, IGN/GameSpot 8.3; praised combat, criticised for linearity and combat-focus; enemy AI mostly reacts only after you shoot; later called "the black sheep of the series" (PCGamesN via Wikipedia) |
| Real-time with pause | Baldur's Gate, Pillars-style RPGs | Pause-and-queue orders `[UNVERIFIED, no source retrieved]` | n/a |
| Turn-based party | Wasteland 2 (2014) and Wasteland 3 (2020) | Turn-based, squad, tactical; Wasteland 2 Director's Cut added Precision Strike (target body parts to cripple or stun, or shatter armor) | WL2: Metacritic PC 81, Director's Cut 87, PC World GOTY 2014; Kickstarter $2.93M against a $900k goal. WL3: Metacritic PC 85, 2M+ players by Dec 2021 |
| Dual mode (unreleased) | Van Buren (cancelled Dec 2003) | Planned player choice between real-time and turn-based combat, "somewhat like VATS" (Giant Bomb, Wikipedia). Sawyer took over as lead designer and resigned; the project was cancelled | None; design remains a fan topic `[UNVERIFIED claims of engine completion]` |
| Pause hybrid | FO3 / FNV VATS | See section 22 | Hit with the mainstream, divisive with the fans |

Take-aways: the best-reviewed turn-based Fallout-adjacent entries (Wasteland 2, 3) show demand for classic combat;
Fallout Tactics shows that a continuous turn-based mode can work mechanically but is fragile in tone and AI;
Van Buren shows the mixed mode never shipped, so there is no market evidence for it.

---

## 24. Durability and repair

### 24.1 Per-game table

| | FO1 / FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|
| Item condition exists? | No (ammo is the attrition resource) | Yes, weapons and armor, 0-100% | Yes, weapons and armor | **Removed** for weapons and armor; power armor pieces still have condition | Yes, durability bars, 0% = broken |
| Effect on damage | n/a | Weapons lose damage and accuracy; jam more often. One fan wiki gives 100% damage at full condition falling linearly to 66% at 0 for firearms, another gives full damage at 75% falling to half at 0 (sources conflict `[DISPUTED]`) | Full damage and DT at 75-100%; each point below 75 removes 0.67% of damage/DT (Game8); the GECK spread-from-condition setting is unused | n/a | **None**: weapons deal the same damage at any condition above broken (fallout.wiki) |
| Effect on spread / rate of fire | n/a | Condition spread can be restored by GECK setting; rate of fire falls about 2% per 10% condition (fan wiki, mixed FO3/NV) `[UNVERIFIED]` | No spread effect in vanilla | n/a | None |
| Jam chance | n/a | Reload jam chance by condition band (GECK defaults): 100% in 0-10%, 75% in 10-20%, 50% in 20-30%, 25% in 30-40%, 10% in 40-50%, 0 from 50%; firing jam defaults are 0 | Jams below 75% condition (Game8); no chance table retrieved | n/a | n/a |
| Effect on DR / DT | n/a | Armor DR falls | DT falls 0.67% per point below 75 | n/a | Broken armor stays equipped but gives no resistance |
| Effect on value | n/a | Yes | Yes | n/a | Yes: value falls to zero at broken; above 100% adds nothing |
| Degradation rate | n/a | Documented figures conflict: "3% of base weapon damage per shot" for Small Guns vs. 0.2 HP per shot (Chinese wiki mirror) `[DISPUTED]`; **VATS multiplies wear by 4-5x** | VATS adds no extra wear | n/a | Weapons: about 0.25-1% per hit on a target; armor: scaled by health damage you take (fallout.wiki, estimate) |
| Repair method | n/a (Repair skill fixes robots and machinery, not gear) | Like-for-like cannibalising, merchant repair, Gun Nut/Mr. Fixit perks | Combine duplicates, vendors, Weapon Repair Kits, Jury Rigging | Power armor station; armor frames not scrapped | Workbench with junk components; Basic/Improved Repair Kits |
| Repair skill link | n/a | Max condition = 40% + 0.6% x Repair (every 5 points adds 3%); duplicates formula below | **Repaired to 100% regardless of skill**; skill sets the efficiency of duplicate repairs | n/a (perk gated mods instead) | Perk cards; over-repair `[UNVERIFIED perk names]` |
| Merchant repair | n/a | Capped by merchant's own Repair skill, e.g. Crazy Wolfgang 15-50-75, Somah 100 | Each NPC has a max repair (58% for Dale Barton up to 100%); cost = 2 x (value at max capped condition - value now) | n/a | None (use workbench) |
| Repair consumables | n/a | None as such | **Weapon Repair Kit**: +10/15/20/25/30% by Repair 0-24/25-49/50-74/75-99/100; crafted at a workbench at Repair 50 from scrap metal x2, scrap electronics, wrench, Wonderglue, duct tape; value 20 caps. No armor kits | n/a | Basic: restore one item to 100%. Improved: buff to 150%; rare Scorchbeast Queen drop. Neither can be crafted, sold or traded |

FO3 duplicate-repair formula (fallout.wiki Repair (Fallout 3)): `result = 5% + higher item's condition + 0.05 x lower
item's condition + 0.15 points x Repair skill`, capped by your maximum. Example: repairing a 20% minigun with a 10% one
gives 27% at Repair 10 and 33% at Repair 50. So the duplicate is a minor ingredient; Repair skill is the main driver.
FO3 homemade weapons also depend on Repair: one schematic builds at 75% of your Repair skill, two at 100% and
three at 125% (capped at 100% condition). FNV keeps the same duplicate formula with a fixed 100% cap and adds
Jury Rigging (Repair 90, level 14 per Game8), which lets any similar gun repair another of the same category
(for example a .357 revolver for a .44), and lets common versions repair unique weapons at the risk of destroying
the unique.

### 24.2 FO76: kits, cash and controversy

- Patch 8.5 notes (Bethesda, 23 April 2019): Basic Repair Kits restore one item in inventory or stash to 100% and
  require no components; they cannot be crafted, dropped, sold or traded; you buy them in the Atomic Shop (premium
  currency, which can also be earned from challenges). Improved Repair Kits buff one item to 150% and drop only
  from the Scorchbeast Queen.
- Backlash: players saw this as pay-to-win because Atomic Shop items had been promised as cosmetic only (Pete Hines
  had said so; PC Gamer, PCGamesN, TheGamer, SlashGear, HotHardware, GameRevolution coverage). The worry was PvP
  advantage, and the broader worry that a monetised repair kit rewards Bethesda for leaving durability irritating.
  Bethesda's reply: it remains committed to no competitive advantage in the shop, and would adjust the kits
  according to feedback (PC Gamer summary). A Steam reply claims basic kits were in the shop earlier; treat that as
  unverified.
- Mechanics context: condition in FO76 affects value and broken-state only (fallout.wiki), so the kit removes the
  nuisance of breakage, not a power loss. Armor repair triggers on damage taken, weapons on hits landed.
- Over-repair: a Steam forum post lists perk cards that allow more than 100% condition (Fix It Good, White Knight,
  Weapon Artisan) `[UNVERIFIED perk names and numbers]`.

### 24.3 Why FO4 removed it, and what replaced it

- **No official reason found.** In 2015 PC Gamer asked about a rumoured new repair system and Pete Hines relayed
  that Todd Howard would not go into details yet (PC Gamer). Fan speculation holds that it was cut. Bethesda's
  Skyrim also has no weapon degradation `[UNVERIFIED general knowledge]`, so the FO4 design follows that lineage.
- **Inference (analysis, not a statement):** FO4's weapon mod system and junk crafting needed the loot economy
  to point at components rather than duplicates; condition would have competed with mod tiers as an upgrade axis;
  and the shooter pace of FO4 leaves little room for a hold-repair loop.
- **What replaced it as a sink:** junk to components (adhesive, screws, aluminium), weapon and armor mod tables,
  power armor stations and fusion cores. Power armor kept a limited form of condition plus fuel (the core drains
  with time and AP use).
- **Reaction.** Gamesas and Steam threads show complaints ("upset no armor and weapons degradation in Fallout 4")
  and a trail of mods that restore degradation. Reviewers did not make it a headline issue
  `[UNVERIFIED, no review piece retrieved]`.
- **FO3 reaction.** Condition and the duplicate-gun system were widely used and were part of the economy, but I
  retrieved no critic piece that evaluates them `[UNVERIFIED]`. FNV's repair kits are generally liked as an
  emergency fix, and a Steam complaint about 10,000 caps to repair a half-broken tesla cannon shows vendor repair
  scaled to value `[UNVERIFIED anecdote]`.

### 24.4 Economy role

| Role | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|
| Caps sink | Merchant repair (capped by merchant skill) | Repair costs scale with item value: 2 x (value at cap - value now), so high-end gear is the real sink | None for gear | Repair costs scrap and components, plus premium kits |
| Reason to pick up duplicate guns | Yes: duplicates are repair ingredients and the main reason to loot common weapons | Yes: duplicates repair; Jury Rigging adds "similar gun" repair | No: weapons are mod platforms; junk is the reason to loot | Weak: scrip, legendary rolls |
| Skill/perk investment | Repair 40% + 0.6%/pt cap; Gun Nut | Repair skill; Jury Rigging at Repair 90 | Armorer, Gun Nut gate mods | Cards |
| Effect on loot | Every weapon is potentially a repair part | Same | Every junk item is a component | Mixed |

### 24.5 Judgement: decision or chore

| Condition is a good decision when | Condition is a chore when |
|---|---|
| Wear is visible and predictable (a bar you can read) | Wear is constant, invisible or random until a sudden break |
| It costs something you were going to spend anyway (caps, ammo, time) and the payoff is clear (FNV's DT/damage scaling) | Repair is a pause-menu errand with no trade-off |
| There is a substitution path (duplicates, kits, vendors) so the player chooses cost vs. convenience | The only path is a cash-shop item (FO76 kits) |
| It makes you choose between tools (a worn favourite vs. a spare; VATS costs extra wear in FO3) | Everything is cheap to fix, so nothing is at stake |
| Penalties are soft (damage falloff, jams below a threshold) | Penalties are hard (broken item cannot be equipped) at the worst moment |

Opinion: durability is worth it only when it turns *loot* into *maintenance choices*. FNV came closest: soft
penalties below 75%, several repair paths of different cost, vendor prices tied to item value and a kit as a
safety valve. FO3's duplicate-parts system was the best loot-recycling idea but its numbers (VATS wear, jam
bands) were unreadable. FO4 replaced condition with crafting, which is a better loot sink but removed the reason to
love a battered old gun. For a new game: soft thresholds, visible condition, a free repair path that costs time or
components, a paid path inside the world (vendors, perks) and never a real-money shortcut. Breath of the Wild's
weapon-durability debate (Unwinnable, TheGamer, GamesRadar, Zelda Dungeon) shows the same split: it works when
breakage drives improvisation and fails when it removes attachment.

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

Real-time vs. turn-based, targeting and durability (sections 22-24)

- **Decide the combat model before the stat system.** Turn-based makes AP and initiative the master stats;
  real-time makes aim the player's, so stats must be routed into damage, durability, utility and hit chance
  *displays*. Do not ship a real-time shooter whose stats only do what the player's hands already do (FO4).
- **If skill must matter in real time, make it a visible, bounded input** (Deus Ex-style reticle bloom that
  shrinks with skill, with a floor so low-skill players can still hit) rather than letting a skill-0 character
  miss a centred crosshair (FO3's complaint from its own lead artist).
- **Aimed shots are worth keeping, but price them in risk, not just AP.** FO1/2's "harder region, higher crit"
  coupling (Eyes -60, crit chance rises by the same amount) is the cleanest version.
- **If you build a targeting-assist mode, never make it invulnerable.** FO3's 90% damage reduction made it a
  win button; FNV's 25% and FO4's AP-sharing show the pressure valves. Banked, timed resources (FO4's critical
  meter, Luck-driven) beat a pause.
- **A hybrid combat mode that exists only for stat expression will always be criticised by both camps.** If the
  project wants a pause-style tactical mode, build it as a full second interface (queued orders, cover, AP), not
  a gimmick on top of a shooter, and let the player choose per fight (Van Buren's unreleased dual mode is the
  design to study; Fallout Tactics' continuous turn-based is the shipped precedent and was well scored but
  stylistically divisive).
- **Armor models should make weapon choice tactical and visible.** FNV's DT-with-floor, shield icons when a hit
  is blocked, and numbers instead of percentage-only bars solved FO3's "armor is invisible" problem.
- **Do not let balance depend on live-service nerfs.** FO76 shows each balance patch punishing the build
  players picked last month. Choose scaling rules (additive vs. multiplicative, clamped resistances) up front
  and keep damage-stacking stats few.
- **Durability must be a decision, not a ritual.** Use soft thresholds (FNV's 75%), several repair paths of
  different cost (duplicates, vendors, kits), prices tied to item value, and visible condition. Hard breakage
  at the wrong moment is a chore.
- **Never sell a real-money shortcut around a friction you designed.** FO76's repair-kit backlash (April 2019,
  patch 8.5) is the cautionary tale; the friction was the product.
- **If you remove durability, replace the sink.** FO4's junk-to-components worked as a loot loop but killed the
  attachment to a battered favourite gun; give the player some other reason to keep and maintain a signature
  weapon.

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

Added for sections 22-24 (fetched unless marked as search summary):

- fallout.wiki, V.A.T.S. overview and per-game pages (FO3, FNV, FO4, FO76): https://fallout.wiki/wiki/V.A.T.S. , https://fallout.wiki/wiki/Fallout_3_V.A.T.S. , https://fallout.wiki/wiki/Fallout:_New_Vegas_V.A.T.S. , https://fallout.wiki/wiki/Fallout_4_V.A.T.S. , https://fallout.wiki/wiki/Fallout_76_V.A.T.S.
- fallout.wiki, Luck (Fallout 4): https://fallout.wiki/wiki/Luck_(Fallout_4)
- fallout.wiki, Action Points and Sequence: https://fallout.wiki/wiki/Action_Points , https://fallout.wiki/wiki/Sequence
- fallout.wiki, Small Guns (Fallout 3): https://fallout.wiki/wiki/Small_Guns_(Fallout_3)
- fodev.net, Fallout 2 critical hit tables: https://fodev.net/files/fo2/criticals.html
- fo2238 / Fallout wiki search summaries on aimed-shot AP and Fast Shot: https://fo2238.fodev.net/wiki/Fast_Shot , https://fallout.wiki/wiki/Fast_Shot_(Fallout_Tactics)
- NMA / GOG / Steam burst and crit build threads (search summaries): https://nma-fallout.com/threads/critical-hits.178020/page-2 , https://nma-fallout.com/goto/post?id=4469963
- PC Gamer, Burnout origin of VATS (headline only): https://www.pcgamer.com/games/fallout/the-fallout-vats-system-was-inspired-by-burnouts-crash-mode-of-all-things-or-as-todd-howard-puts-it-imagine-the-car-parts-are-like-eyeballs-and-guts
- GamesRadar, VATS compensating for shooting (headline only): https://www.gamesradar.com/games/fallout/fallout-3s-vats-system-helped-compensate-for-bethesdas-lack-of-shooting-chops-we-were-never-going-to-create-gun-combat-that-was-on-par-with-call-of-duty-or-battlefield
- frvr.com summary of Istvan Pely's EDGE remarks: https://frvr.com/blog/news/fallout-3-devs-wondered-if-vats-was-even-fun-during-development-as-bethesda-wondered-if-its-gunplay-felt-good-or-just-frustrating
- Pagliarulo interviews (search summaries): https://www.strategycore.co.uk/articles/interviews/fallout-3-interview/ , https://rpgcodex.net/article.php?id=4937 , https://rpgcodex.net/article.php?id=4983
- RPG Codex, "VATS slow motion may be the worst crime against video gaming": https://rpgcodex.net/article.php?id=5659
- RPG Codex, Sawyer on damage threshold (May 2010): https://rpgcodex.net/article.php?id=6694
- PC Gamer / GamesRadar, Sawyer on "vibes-based" weapon balance (headline and search summaries): https://www.pcgamer.com/games/fallout/fallout-new-vegas-director-reveals-that-game-balance-is-mostly-vibes-based-says-he-only-used-a-weapons-spreadsheet-for-maybe-a-couple-of-months
- PC Gamer, FO76 real-time VATS (headline only): https://pcgamer.com/fallout-76-will-have-real-time-vats ; PC Gamer FO76 VATS footage: https://www.pcgamer.com/fallout-76-vats/
- Shacknews / Prima, how to use VATS in FO76 (search summary): https://shacknews.com/article/108601/how-to-use-vats-in-fallout-76
- Altchar, GamingBolt, PCGamesN FO76 VATS coverage (search summaries): https://www.altchar.com/game-news/fallout-76-vats-system-seems-to-be-underwhelming-a0mlZ3h1n0do , https://gamingbolt.com/fallout-76-will-have-real-time-vats-non-human-npcs-and-a-world-filled-with-things
- fallout.wiki, Fallout 76 damage; Bloodied (Fallout 76); Durability (Fallout 76): https://fallout.wiki/wiki/Fallout_76_damage , https://fallout.wiki/wiki/Bloodied_(Fallout_76) , https://fallout.wiki/wiki/Durability_(Fallout_76)
- Bethesda, Fallout 76 Wild Appalachia patch 8.5 notes (23 April 2019): https://fallout.bethesda.net/en-US/news/fallout-76-wild-appalachia-patch-8-5-notes-april-23-2019
- FO76 repair-kit controversy coverage (search summaries): https://www.pcgamer.com/fallout-76-fans-are-unhappy-that-bethesda-is-adding-pay-to-win-items , https://www.thegamer.com/fallout-76-repair-kit-fiasco-explained/ , https://hothardware.com/news/fallout-76-repair-kits
- FO76 balance and nerf coverage (search summaries): https://www.newsweek.com/entertainment/video-games/fallout-76-update-patch-notes-legendary-shotgun-weapons-nerf-carry-weight-1311507 , https://mp1st.com/news/fallout-76-stealth-nerfs-discovered-in-latest-patch-includes-reduced-enemy-xp-production-nerf-more , https://mein-mmo.de/fallout-76-patch-notes-nerfs-kritik/
- fallout.wiki, Repair (Fallout 3), Repair (Fallout: New Vegas), Fallout 3 crafting, Weapon Repair Kit: https://fallout.wiki/wiki/Repair_(Fallout_3) , https://fallout.wiki/wiki/Repair_(Fallout:_New_Vegas) , https://fallout.wiki/wiki/Fallout_3_crafting , https://fallout.wiki/wiki/Weapon_Repair_Kit
- Game8, Fallout: New Vegas repair and condition thresholds: https://game8.co/games/Fallout-New-Vegas/archives/454068
- GECK wiki, weapon condition jam settings (search summaries): https://geck.uesp.net/wiki/FWeaponConditionReloadJamXX , https://geck.uesp.net/wiki/FWeaponConditionJam
- PC Gamer, FO4 repair system deferral (search summary): https://www.pcgamer.com/fallout-4-might-have-a-new-repair-system-but-bethesda-isnt-ready-to-talk-about-it
- Gamesas forum, FO4 durability complaints (search summary): https://www.gamesas.com/upset-armor-and-weapons-degradation-fallout-t390274.html
- Steam / Nexus / Gamesas threads on FO4 bullet sponges and legendaries (search summaries): https://forums.nexusmods.com/topic/3562725-legendary-stuff-my-main-problem-with-fallout-4 , https://www.gamesas.com/don-you-hate-bullet-sponging-t390429-25.html
- Wikipedia: https://en.wikipedia.org/wiki/Fallout_Tactics:_Brotherhood_of_Steel , https://en.wikipedia.org/wiki/Wasteland_2 , https://en.wikipedia.org/wiki/Wasteland_3 , https://en.wikipedia.org/wiki/Van_Buren_(video_game)
- fallout.wiki, Fallout Tactics: https://fallout.wiki/wiki/Fallout_Tactics:_Brotherhood_of_Steel
- Deus Ex wiki, weapons and skills (search summary): https://deusex.fandom.com/wiki/Weapons_(DX) ; Mass Effect Legendary Edition accuracy notes: https://www.gamebanshee.com/a9ywr
- Breath of the Wild durability debate (search summaries): https://unwinnable.com/2017/04/27/weapon-durability-in-breath-of-the-wild/ , https://www.thegamer.com/weapon-durability-in-breath-of-the-wild-is-good-and-im-tired-of-pretending-its-not/ , https://www.gamesradar.com/zelda-breath-of-the-wild-broke-the-mould-and-me-by-breaking-its-weapons

Not reachable this session (attempted): fallout.wiki pages for Aimed shot and Fallout 3 item condition (404), CanardPC/TechRadar/Windows Central/AOL full text (truncated or 404), breezewiki mirror (bot block), GECK Gun Spread Formula (403); Nukapedia "Fallout 76 combat" (HTTP 402), fallout.wiki FNV reputation
page (404), a Tim Cain video-summary wiki (login wall). Josh Sawyer's GDC 2012 talk
(https://gdcvault.com/play/1015758/Do-(Say)-The-Right-Thing) was identified but not viewed.
