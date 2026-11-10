# Fallout 4 (2015) — Gameplay, Systems and Balance

Scope: mechanics, numbers and balance of Fallout 4 (Bethesda Game Studios, released 10 November 2015 on PC, PS4
and Xbox One), its six add-ons, the 2016 Survival overhaul, Creation Club and the 2024 next-gen update. Story and
lore are out of scope except where they constrain systems.

Confidence note: figures taken from a wiki page or article opened during this research pass are stated plainly.
Figures that are standard community knowledge but could not be re-opened in this pass (Nukapedia/Fandom blocked
automated access, and the search budget ran out part-way) are tagged `[UNVERIFIED]`. Conflicting sources are
tagged `[DISPUTED]`.

## Quick Reference

- **Identity shift:** Fallout 4 is a first-person shooter-looter with RPG trimmings. Its own director later
  conceded the dialogue system "didn't work as well" as the rest; the shooting, crafting and exploration are
  what people praise.
- **Gunplay:** rebuilt with advice from id Software and a systems designer hired from Bungie (Destiny was the
  reference point). Aim-down-sights on every gun, real recoil/spread, cover leaning, hot-keyed grenades, sprint.
  No weapon degradation, no ammo sub-types.
- **V.A.T.S.** slows time instead of pausing it. Critical hits are no longer random: a meter fills per hit and
  the player spends it on a guaranteed, armour-ignoring hit.
- **Skills are gone.** One 7 x 10 perk chart (70 perks, about 229 ranks at launch, 243 with DLC) gated by SPECIAL
  rank and character level. One point per level, spent on either a perk rank or a SPECIAL point. No level cap.
- **28 SPECIAL points at creation** (1 in each stat plus 21 to distribute) `[UNVERIFIED]`; everything can be
  maxed at level 272 (base) / 286 (with DLC), so builds converge over a long game.
- **Damage formula:** damage taken = damage x min(0.99, (0.15 x damage / resistance)^0.365). Armour has steep
  diminishing returns and is far better against many small hits than against one big hit.
- **Power armour** is a wearable vehicle: a frame plus six pieces with their own hit points, fuelled by fusion
  cores (about 20 real minutes each). The first suit is handed over in the second main quest.
- **Junk economy:** every clutter object breaks into one or more of 31 base components used for weapon mods,
  armour mods and settlement building. This turns the series' decorative clutter into the core loot loop.
- **Legendary enemies** (starred, mutate mid-fight) drop an item with one random prefix from a pool of about 50.
  A few prefixes (Explosive, Wounding, Two Shot, Instigating, Bloodied/Junkie's) dominate everything else.
- **Settlements:** 30 base-game sites (37 with DLC), population cap 10 + Charisma, a happiness score built from
  food/water/beds/defence, supply lines via a Charisma perk. Loved by builders, ignored by many, and almost
  entirely optional for the main quest.
- **Radiant quests** are infinite templated jobs. The Minutemen version ("another settlement needs your help")
  became a meme because it auto-assigns, has hidden timers and never ends.
- **Dialogue:** four paraphrased options on a wheel, fully voiced protagonist (about 13,000 lines per actor,
  111,000 lines in the game). Only Charisma checks remain, colour-coded yellow/orange/red.
- **Companions:** 13 base + 3 DLC, an affinity score from -1000 to +1100, a permanent perk at 1000.
- **World:** small map, extremely dense. Difficulty is zoned by region (easy north-west, hard south and
  south-west) with per-zone level ranges rather than pure global scaling.
- **Survival mode (patch 1.5, April-May 2016):** no fast travel, save only by sleeping, hunger/thirst/fatigue,
  disease, weighted ammo, lethal damage both ways. Widely regarded as the best way to play because it makes
  every other system matter.
- **Balance verdict:** mid-game onward the player is overpowered through crafting, stealth multipliers, chems
  and a handful of legendary prefixes. The game feels great minute to minute and thin as a role-playing game.

## 1. Context and reception

| Item | Value |
|---|---|
| Release | 10 November 2015 (PC, PS4, Xbox One) |
| Engine | Creation Engine (Skyrim's engine, extended) |
| Metacritic | 84 (PC), 87 (PS4), 88 (Xbox One) |
| Launch shipment | 12 million units shipped for day one |
| Voice work | about 111,000 recorded lines; each protagonist actor recorded 13,000+ over two years |
| Awards | D.I.C.E. and Game Developers Choice Game of the Year (2016) |
| Level cap | None (game crashes past level 65,535) |

Critical consensus at launch was "excellent open-world shooter, shallower RPG". The fan shorthand that stuck is
"good game, bad Fallout / bad RPG". Player review scores were consistently lower than critic scores.

## 2. Gunplay

### What changed from Fallout 3 / New Vegas

| Area | Fallout 3 / New Vegas | Fallout 4 |
|---|---|---|
| Hit resolution in real time | Skill-driven spread; shots visibly miss the crosshair | Shots go where the gun points; spread and recoil are properties of the gun and its mods |
| Aim down sights | Zoom only in FO3; true iron sights added in NV | Every gun; hip-fire and sighted accuracy are separate stats, both improved by crouching |
| Cover | None | Contextual lean around corners when aiming next to cover |
| Grenades / melee | Must be equipped as a weapon | Dedicated button: tap to gun-bash, hold to throw |
| Movement | No sprint | Sprint costs Action Points |
| Weapon upkeep | Condition degrades, repair needed | No degradation at all |
| Ammo types | NV had AP/HP/surplus variants and reloading bench | Removed; one ammo type per calibre |
| Quick access | Hotkeys | 12-slot favourites wheel/cross |

### Why it is regarded as the series' best shooting

- Todd Howard said before launch that the team "wanted to not make any excuses for how the action felt in a
  role-playing game", and that because id Software is a sister studio "the first thing we did was call them".
- Game Informer's 2015 coverage reported that Bethesda hired a senior systems designer from Bungie (Josh
  Hamrick) to tune firearms and used Destiny as a touchstone, partly because Destiny also targets 30 fps on
  console and still feels responsive.
- Feedback layers: strong hit reactions, limb dismemberment, a hit-marker and XP tick, slow-motion kill cams,
  distinct audio per receiver/muzzle mod, and visible weapon changes when modded.
- The removal of character-skill-based spread means player aim is honoured. The cost: the character sheet no
  longer decides whether you can shoot, only how hard the shot hits.

### Weapon perk structure

Damage perks are flat multipliers by weapon class: Gunslinger (non-automatic pistols), Rifleman (non-automatic
rifles), Commando (automatic), Big Leagues (melee), Iron Fist (unarmed), Heavy Gunner, Demolition Expert. Each
is +20% per rank to +100% at rank 5, with small riders (armour penetration, stagger, hip-fire accuracy)
`[UNVERIFIED exact riders]`. Class is decided by the mods on the gun: a pistol grip makes it a Gunslinger
weapon, a stock makes it a Rifleman weapon, an automatic receiver makes it a Commando weapon. This is the main
long-term damage scaling and is widely criticised as dull ("+20% damage" five times).

## 3. V.A.T.S. and criticals

| Rule | Fallout 4 behaviour |
|---|---|
| Time | Slowed heavily, not paused; enemies keep moving and hit chances change while you choose |
| Damage taken while in V.A.T.S. | fallout.wiki states 10% of normal (New Vegas: 75%) |
| Targets | Six body regions on humanoids; up to 16 queued attacks |
| AP cost | Per weapon and its mods; scopes roughly double cost, reflex sights reduce it; automatics pay per short burst |
| Criticals | No random crits. Hits in V.A.T.S. fill a meter; when full, the player presses a button to convert a queued shot into a critical |
| Critical properties | Guaranteed to hit if displayed chance is above 0%; ignores damage and energy resistance |
| Critical damage | Paper damage + (weapon base damage x CritMult); CritMult = 2 + bobblehead 0.25 + magazines 0.05-0.5 + weapon mod 1.0 or 2.0 |
| Meter fill | Community-tested: about (Luck x 1.5 + 6)% per hit, i.e. roughly 14 hits at Luck 1 and 5 at Luck 10 `[UNVERIFIED]` |

Supporting perks (Luck column): Better Criticals (+50/100/150% critical damage `[UNVERIFIED]`), Critical Banker
(store extra criticals), Four Leaf Clover (chance for a hit to fill the meter outright), Grim Reaper's Sprint
(chance for a kill to refill AP). Together these produce a "crit loop" build in which V.A.T.S. chains almost
indefinitely.

Design reading: converting crits from a dice roll into a banked resource is one of the game's cleanest ideas.
It makes Luck a tactical stat and gives V.A.T.S. a purpose even when real-time aiming is good.

## 4. Character system: SPECIAL and the perk chart

### Structure

| Element | Detail |
|---|---|
| Stats | Seven SPECIAL stats, 1-10 each; start at 1 each plus 21 points to distribute (28 total) `[UNVERIFIED]` |
| Chart | 7 columns (one per stat) x 10 rows; a perk in row N needs base stat N |
| Perk count | 70 perks; about 229 ranks at launch, +7 ranks from Far Harbor and +7 from Nuka-World (derived from the level-272 / level-286 "everything" thresholds) |
| Points | 1 per level, spent on a new perk, a further perk rank, or +1 to a SPECIAL stat |
| Rank gates | Higher ranks need a character level; top ranks sit around levels 40-50 |
| XP to next level | 75 x (level - 1) + 200; cumulative threshold 37.5n^2 + 87.5n - 124 |
| Level cap | None; all perks and stats at level 272 (286 with DLC) |
| Other perk sources | 20 bobbleheads (7 SPECIAL +1, 13 named after the old skills), perk magazines in collectible series, one perk per companion |
| Intelligence | About +3% XP per point `[DISPUTED: 3% vs 3.33%]` |
| Idiot Savant | Chance of 3x (rank 1) or 5x (rank 2) XP on any award; chance falls as Intelligence rises (about 11% at INT 1 down to 1% at INT 11+) `[UNVERIFIED]` |

Derived stats `[UNVERIFIED this pass]`: hit points 80 + 5 x Endurance, plus (Endurance / 2 + 2.5) per level;
Action Points 60 + 10 x Agility; carry weight 200 + 10 x Strength.

### What replaced skills

The 13 skills of Fallout 3 were folded into perks. Lockpicking and hacking became four-rank perks that unlock
tiers (Novice free, then Advanced / Expert / Master) with level gates. Crafting skills became Gun Nut, Armorer,
Science! and Blacksmith, each with ranks gated around levels 1 / 13 / 25 / 39 (Science! 1 / 17 / 28 / 41)
`[UNVERIFIED exact levels]`. Speech became the Charisma stat itself.

### Effect on build identity

- **Positive:** every level gives a visible, named reward; there are no wasted 3-point skill dribbles; the chart
  is readable at a glance; stats matter because they gate rows.
- **Negative:** with no cap and no exclusive choices, characters converge. By level 50-60 most players have the
  same crafting perks, the same weapon-class perk and Lone Wanderer or a companion. Traits (New Vegas) and
  tag skills are gone, so there is no defining choice at creation except the stat spread, which is itself
  repairable one point per level.
- A large share of the chart is "+20% damage with X" or tier-unlock perks rather than new verbs. The
  interesting perks are the ones that change behaviour: Blitz (V.A.T.S. melee teleport), Penetrator (shoot
  through cover), Mysterious Stranger, Wasteland Whisperer / Intimidation (pacify and command enemies),
  Nuclear Physicist rank 3 (eject cores as bombs), Pain Train (power armour charge).
- Because there are no skills, there is nothing for dialogue or the world to test other than Charisma, a perk
  tier, or a keycard. This is the mechanical root of the "bad RPG" complaint.

## 5. Damage and armour

### Core formula (ballistic)

```
DamageCoeff  = min(0.99, (Damage x 0.15 / DamageResist) ^ 0.365)
DamageTaken  = PaperDamage x DamageCoeff x HeadshotMult x SneakMult
PaperDamage  = WeaponBase x perk multipliers x RangeMult
RangeMult    = 1.0 inside listed range, falling linearly to 0.5 at 2x range
```

Game settings: `fPhysicalDamageFactor = 0.15`, `fPhysicalArmorDmgReductionExp = 0.365`. Some community posts
quote the exponent as 0.366 or restate the formula as 0.5 x (damage / resist)^0.365, which is the same curve
(0.15^0.365 is about 0.5) `[DISPUTED third decimal only]`.

| Damage per hit | Resistance | Coefficient | Reduction |
|---|---|---|---|
| 50 | 50 | 0.50 | 50% |
| 10 | 10 | 0.50 | 50% |
| 100 | 1000 | about 0.22 | about 78% |
| 250 | 1000 | about 0.17 | about 83% |
| 1000 | 1000 | 0.50 | 50% |
| any | under 15% of damage | 0.99 | 1% (floor) |

Consequences worth copying or avoiding:

- Reduction depends on the **ratio** of hit damage to resistance. Equal damage and resistance always gives 50%.
  Doubling armour never doubles protection; it cuts damage taken by about 22% more (2^-0.365 = 0.78).
- Armour is far stronger against rapid low-damage hits than against slow heavy ones. A minigun (8 base damage)
  is nearly useless against armoured targets while a Gauss rifle ignores most armour. Fat fingers on the
  design side: automatic weapons end up under-powered unless they carry a flat-damage legendary rider.
- Flat add-on damage that is evaluated as its own small hit (explosive rounds, bleed) breaks the curve. Bleed
  has no resistance at all.
- There is no damage threshold (New Vegas's flat subtraction) and no hard cap other than the 1% floor.
- All worn armour sums to one resistance number regardless of hit location.
- Difficulty multipliers apply after resistance, so armour is equally valuable at every difficulty.

### Other damage types

| Type | Handling |
|---|---|
| Energy | Own resistance stat; same curve, but uses weapon base damage rather than perk-boosted paper damage in the ratio; armour-penetration effects are reported bugged against energy resistance |
| Radiation | Each point that gets through removes 0.1% of maximum HP (rads shrink the health bar rather than being a separate meter with thresholds) |
| Poison | Damage per second, typically 10 seconds, each tick resisted |
| Bleed | Like poison but unresisted; works even on robots |
| Explosive | Sub-type of physical; Padded mod -25%, Dense mod -50% base explosion damage, stacking before resistance |

### Sneak and difficulty multipliers

| Source | Multiplier |
|---|---|
| Ranged sneak attack | 2.0x base; Ninja raises to 2.5 / 3.0 / 3.5x `[UNVERIFIED]` |
| Melee sneak attack | Ninja raises to 4 / 5 / 10x `[UNVERIFIED]` |
| Mister Sandman (suppressed weapons) | +15 / 30 / 50% sneak damage `[UNVERIFIED]` |
| Deacon's Cloak & Dagger | +20% sneak damage |
| Melee power attack | 1.5x paper damage |

| Difficulty | Player deals | Player takes | Legendary spawn multiplier |
|---|---|---|---|
| Very Easy | 2.0x | 0.5x | 0.25 |
| Easy | 1.5x | 0.75x | 0.5 |
| Normal | 1.0x | 1.0x | 1.0 |
| Hard | 0.75x | 1.5x | 1.25 |
| Very Hard | 0.5x | 2.0x | 1.5 |
| Survival (1.5+) | 0.75x (up to about 1.1x with full Adrenaline) | 4.0x | higher than Very Hard; exact value `[DISPUTED]` |

Deal/take values for Very Easy to Very Hard are `[UNVERIFIED this pass]` but consistent with fallout.wiki's
statement that Survival is 1.5x dealt and 2.0x taken *relative to Very Hard*, i.e. 0.75x and 4.0x relative to
Normal. Many guides misreport Survival as "1.5x dealt, 2x taken" in absolute terms.

### Conventional armour

Layered system `[UNVERIFIED details]`: an under-layer outfit, five armour pieces (chest, two arms, two legs)
and headgear. Families are raider, leather, metal, combat and synth, each in normal / sturdy / heavy tiers,
with a material mod slot and a misc mod slot (pocketed, deep pocketed, padded, dense, muffled, lead-lined and
so on). The Railroad's **ballistic weave** unlock adds up to roughly +110 damage and energy resistance to
ordinary clothing and hats, which stacks under armour and is the single strongest defensive upgrade outside
power armour. It is hidden behind a faction's radiant quests, which is a classic discoverability problem.

## 6. Power armour

| Aspect | Detail |
|---|---|
| Structure | A frame (60 DR on its own) that the player climbs into, plus six pieces: helmet, torso, two arms, two legs |
| Piece health | Each piece has its own hit points and breaks; repaired at a power armour station with components |
| Fuel | Fusion core: about 20 real-time minutes (about 10 game hours) of jogging; value 200 caps |
| Drain | None standing still, less when walking; much more for sprinting, V.A.T.S., scoped breath-hold, and most of all the jet pack |
| Core empty | Still wearable, but slow, effectively over-encumbered, no V.A.T.S. |
| Extending cores | Repair bobblehead +10%; Nuclear Physicist up to +100% |
| Built-in benefits | Each piece gives the player 5% flat damage reduction (after resistance) and 14% radiation reduction; no fall damage; Strength raised while worn (set to 11 `[UNVERIFIED]`); landing damages nearby characters |
| Restrictions | Replaces normal armour bonuses; cannot swim (walks on the bottom); no wrist/hand weapons |
| Training | None required (Fallout 3 and New Vegas required a perk) |
| Mods | Six upgrade tiers per piece plus paint, torso modules (jet pack needs Science! 4 and Armorer 4), leg and arm modules |

| Model | Full-set damage resistance, base to top tier | Piece health | Appears on world frames at player level |
|---|---|---|---|
| Raider | 500 to 620 | 350 to 700 | any |
| T-45 | 500 to 1100 | 450 to 1125 | 1-13 |
| T-51 | 740 to 1340 | 720 to 1395 | 14-20 |
| T-60 | 980 upward | 990 upward | 21-27 |
| X-01 | 1220 to 1820 | 1260 to 1935 | 28+ |

Randomised partial sets shift later (T-45 pieces from level 15, T-51 from 25, T-60 from 35, X-01 from 45).

### The first-hour problem

The second main quest in Concord gives the player a T-45 suit, a minigun and a deathclaw fight, typically
within the first hour. Criticisms that recur in reviews and retrospectives:

- It spends the series' two biggest escalations (power armour as end-game reward, the deathclaw as end-game
  terror) before the player has earned or feared either. Later deathclaws are just another large enemy.
- The intended brake is fuel scarcity, but cores are sold by vendors, sit in generators across the map and
  last twice as long with one perk. By the mid-game most players hold dozens, and the fuel system stops being
  a decision. On Survival, where cores weigh 4 each, the constraint partly returns.
- Counter-view: as a mechanical object the suit is the best the series has had. It has weight, its own HUD,
  entry/exit animation, per-limb damage and a garage-style upgrade bay. The idea (armour as vehicle with fuel
  and repairs) is strong; the pacing and the fuel tuning are what failed.

## 7. Crafting, modification and the junk loop

### Stations

Weapons workbench, armour workbench, power armour station, chemistry station, cooking station, and the
settlement workshop. DLC adds the robot workbench (Automatron), manufacturing machines such as ammunition
plants and weapon forges (Contraptions Workshop), and the Nuka-Mixer (Nuka-World).

### Components

Thirty-one base components: acid, adhesive, aluminium, antiseptic, asbestos, ballistic fibre, bone, ceramic,
circuitry, cloth, concrete, copper, cork, crystal, fertiliser, fibre optics, fibreglass, gears, glass, gold,
lead, leather, nuclear material, oil, plastic, rubber, screws, silver, springs, steel, wood.

- Every junk item lists its yield (a desk fan gives steel, gears and screws; duct tape gives adhesive and
  cloth). Crafting auto-consumes junk from the workbench, breaking items as needed and returning the remainder.
- Components can be **tagged for search**, which puts a magnifying-glass icon on any junk in the world that
  contains them. This small UI feature is what makes the loop tolerable.
- Scrapping weapons and armour returns only a fraction: common components always, uncommon ones (aluminium,
  screws, copper; scalar 0.25) need Scrapper rank 1, rare ones (fibre optics, nuclear material, ballistic
  fibre) need rank 2. Adhesive and oil are never returned and must come from junk or be cooked/crafted.
- Bottlenecks by design: **adhesive** (every weapon mod), **screws**, **aluminium**, **oil**, **copper**
  (settlement power), **fibre optics/nuclear material** (high-tech mods), **ballistic fibre**. Adhesive is
  craftable from farmed crops (vegetable starch), which links farming settlements to gun crafting.

### Weapon mods

- More than 700 weapon mods. Ballistic slots: receiver, barrel, grip/stock, magazine, sights, muzzle. Energy
  slots: capacitor, barrel, grip, sights, muzzle. Melee: one or two slots.
- A single base gun spans roles. The pipe gun or the combat rifle can be a pistol, carbine, sniper rifle or
  automatic depending on mods, and its perk class changes with it.
- Mods removed from a gun are kept as loose items and can be fitted to another gun of the same type, so
  looted weapons are valuable as mod donors even without crafting perks.
- Gating: Gun Nut (ballistic), Science! (energy and high-tech), Blacksmith (melee), Armorer (armour and power
  armour). Top receivers need rank 4 at around level 39-41.
- Legendary prefixes cannot be crafted, removed or transferred in the base game. The random drop is the only
  source, which keeps the loot treadmill alive after crafting is maxed.

### Why the loop works

Explore, fight, hoover up clutter, return to base, convert clutter into a visibly better gun or a bigger base,
go out again. Environmental set-dressing, which in earlier games was physics noise, becomes loot with a
purpose. Costs: carry weight becomes the main constraint (constant trips, companions as pack mules), and the
world's objects all start to look like their component lists.

## 8. Legendary enemies and loot

### Enemies

- Any ordinary enemy spawn can roll as "Legendary" (star beside its name). Base chance rises with player level
  and is multiplied by difficulty (0.25 / 0.5 / 1 / 1.25 / 1.5 from Very Easy to Very Hard; Survival higher,
  figures of 2x and 3x both circulate `[DISPUTED]`).
- A legendary enemy "mutates" once when reduced to about half health, restoring its health and hitting harder
  `[UNVERIFIED exact threshold]`.
- It almost always drops one legendary weapon or armour piece. The base item and the prefix are both rolled
  from level-gated lists; saving before entering an area lets players re-roll, a widely used exploit
  `[UNVERIFIED exact roll timing]`.
- Fixed uniques from vendors and quests are ordinary items with a pre-set prefix and a custom name.

### Weapon prefixes (selection; values from fallout.wiki)

| Prefix | Effect | Balance note |
|---|---|---|
| Two Shot | Fires an extra projectile, +25% recoil | Near-double damage on high-damage single shots; the vendor-sold two-shot combat rifle is a common early-game carry. The added projectile reportedly uses base rather than modded damage `[UNVERIFIED]` |
| Explosive | Each bullet explodes for 15 area damage | Flat per-bullet damage scaled by the explosives perk, so it is overwhelming on shotguns (per pellet), miniguns and SMGs. Top tier. Can kill the user at close range |
| Wounding | 25 bleed damage over 5 seconds per hit | Bleed stacks and ignores resistance; top tier on fast automatics and fast melee |
| Instigating | 2x damage to targets at full health | Best for sneak snipers: stacks with sneak multipliers for one-shot kills |
| Bloodied | +5% damage per 5% health missing, up to +95% | Strong with low-health perk synergies |
| Junkie's | +15% per addiction, up to +195% | Highest raw multiplier; cost is manageable debuffs |
| Furious | +15% per consecutive hit on same target | Strong on automatics and melee against bosses |
| Never Ending | Magazine equals carried ammo | Removes reloading; transforms slow-reload guns |
| Penetrating | Ignores 30% of resistances | Solid, unexciting |
| Powerful / Violent | +25% damage (Violent adds limb damage and recoil) | Baseline |
| Kneecapper | 20% chance to cripple a leg | Trivialises melee enemies on automatics |
| Staggering / Crippling / Freezing / Incendiary / Plasma Infused / Irradiated / Poisoner's | Chance or flat riders (10 cryo, 15 fire, +10 energy, +50 rads, 3 poison/s for 10 s) | Flat riders favour fast weapons |
| Assassin's / Hunter's / Mutant Slayer's / Ghoul Slayer's / Troubleshooter's / Exterminator's | +50% against one enemy category | Feel like bad rolls; force weapon swapping few players do |
| Lucky / Relentless / Quickdraw / VATS Enhanced / Stalker's | Crit and AP manipulation (2x crit damage and +15% meter; crits refill AP; -25% AP cost; +33% hit chance) | Core of V.A.T.S. loop builds |
| Berserker's / Nocturnal / Nimble / Cavalier's / Sentinel's | Conditional | Mostly ignored |
| Far Harbor additions | Deadeye, Defiant, Hitman's, Resilient, Resolute, Steadfast, and melee block effects | Mostly weak |

Armour prefixes follow the same pattern (stat boosts, damage reduction by enemy type, conditional effects
such as slowing time at low health or turning invisible while sneaking and still) `[UNVERIFIED list]`.

### Assessment

- The idea fits Fallout 4's shooter-looter identity: a reason to fight optional enemies and a jackpot moment.
- The pool is poorly balanced. Four or five prefixes are build-defining; around a third are filler. Because the
  base item is also random, most drops are "Hunter's pipe pistol" or "Ghoul Slayer's leather left leg" and go
  straight to a vendor.
- Flat-damage riders interacting with the resistance curve (section 5) are the root of the outliers. A flat
  +15 on a weapon whose base hit is 8 nearly triples it; on a 100-damage rifle it is noise.
- No pity mechanic, no targeted farming and no way to move prefixes means the optimal strategy is save-scumming.
  Fallout 76 later added legendary crafting and scrip to address exactly this.

## 9. Settlements

### Rules

| Element | Rule |
|---|---|
| Number | 37 unlockable: 30 base game, 1 Automatron, 4 Far Harbor, 1 Vault-Tec Workshop, 1 Nuka-World |
| Unlocking | Clear enemies or do a small job for residents, then activate the workshop |
| Population cap | 10 + Charisma (20 at Charisma 10; up to 43 with gear and chems); recruitment stops if more than four settlers are jobless |
| Recruitment | A powered recruitment beacon draws settlers over time |
| Food | One farmer works 6 food units; most crops yield 0.5 per plant, mutfruit 1.0; each settler eats 1 |
| Water | Each settler needs 1; hand pump 3, powered purifier 10, industrial purifier 40 `[UNVERIFIED outputs]` |
| Beds | One per settler, under a roof for full happiness |
| Defence | A guard staffs up to three posts; defence rating should meet or exceed population, and food + water to deter attacks |
| Power | Generators, wires, pylons, switches and logic gates (expanded in Contraptions) |
| Passive junk | Idle settlers produce 1 junk per update, scavenging-station settlers 2; stops above 100 + 5 per settler stored |
| Brahmin | Boosts food output and produces fertiliser (cap 3 per settlement) |
| Stores | Six shop types in three tiers; pay caps into the workbench and add happiness |
| Supply lines | Local Leader rank 1 (Charisma 6): assign a settler as provisioner between two settlements to share junk, components, aid and ammo (not weapons or armour) for crafting and building. Rank 2 allows shops and crafting stations |
| Build budget | A per-settlement size bar limits object count for performance |

### Happiness

Per human or ghoul settler, base needs add to a maximum of 80: bed 10, bed under shelter 10, food 20, water
20, defence 20. Bonus happiness comes from shops (food/drink stalls 15 / 20 / 40 by tier, clinics 10 / 20 /
30, clothing 8 / 10 / 10, general traders 10 / 10 / 15; weapon and armour shops give nothing) and from pets
and DLC objects. Caps: all settlers are held to 60 if defence is below population; a settler without a
sheltered bed is held to 60; food or water shortfall holds affected settlers to 30. Robot settlers are fixed
at 50 and drag the average. A temporary modifier (range -50 to +20) decays by a factor of 0.8 per update:
-20 when a settler dies, -20 when a Minutemen radiant quest for that settlement triggers, +20 when it is
completed. Reaching 100 is an achievement and in practice needs a small population of settlers who all run
top-tier food stalls or clinics.

### Attacks

Each settlement has a daily attack chance that rises with stored/produced food and water and falls with
defence and population. Community formulas agree on the shape and disagree on constants; a common version is
2% base + (food + water) / 10, minus defence and half of population, with a floor of 2% `[DISPUTED]`. If the
player does not travel to the settlement, the outcome is rolled, and even heavily defended settlements can
lose and take damage `[UNVERIFIED odds]`. Caged or tamed creatures (Wasteland Workshop) raise attack odds.

### Reception

- **Praise:** an unusually deep building toolset for an RPG, with snapping structures, wiring and logic; it
  gave the junk economy a second sink and spawned an enormous building community and mods such as Sim
  Settlements, which automates construction with plot-based city growth.
- **Criticism:** almost nothing in the main quest requires it (one late device build aside); the interface is
  first-person and fiddly, with unreliable snapping; settlers have no personality, needs beyond the five
  numbers, or stories; settlements do not visibly change the world or faction balance; the system is barely
  tutorialised; it competes with hand-authored towns for development effort, and the Commonwealth has only
  two or three real towns as a result. Many players report ignoring it entirely.
- **Economy leak:** industrial water purifiers deposit purified water in the workbench daily. A handful of
  them produce more caps than any other activity, removing money as a constraint within a few hours.

## 10. Radiant quests and the "another settlement" problem

| Faction | Typical radiant templates |
|---|---|
| Minutemen | Clear raiders / ghouls / super mutants troubling a settlement, rescue a kidnapped settler, defend a settlement, claim a new site |
| Brotherhood of Steel | Clear a location of ferals or mutants, retrieve a piece of technology, escort a squire, obtain crops from settlements |
| Railroad | Clear or secure a safehouse site, eliminate a target, recover caches, the technology-recovery chain that unlocks ballistic weave |
| Institute | Kill creatures threatening an operation, pressure or persuade a settlement, recover material |

How they are built: a template picks a location from a pool of dungeons, repopulates it and places an
objective. Rewards are small caps and XP plus, in some chains, a one-off unlock.

Why the Minutemen version became notorious:

- The quest-giver hands over the next job the moment the last is turned in, and sometimes merely on greeting.
  There is no way to decline.
- Several have hidden timers. Ignoring one fails it and costs settlement happiness; accepting one applies -20
  temporary happiness until it is done.
- The pool of targets is small, so the same building is cleared repeatedly, and the same lines of dialogue
  repeat. "Another settlement needs our help" became shorthand for content that is generated rather than
  written.
- They never end and never resolve the faction's situation, which undercuts the fiction of rebuilding.

General lesson visible across Fallout 4: radiant jobs are acceptable as optional padding after authored
content, and corrosive when they are pushed at the player, timed, and mixed into the same log as real quests.
Fallout 4 also gated meaningful rewards (ballistic weave) behind them, forcing engaged players through them.

## 11. Dialogue and the voiced protagonist

### The system

- Every player response is one of at most four options mapped to the four face buttons (or arrow keys),
  shown as a paraphrase of one to three words. The spoken line is often longer or different in tone.
- The camera cuts cinematically or stays in first person; the player can walk away mid-conversation.
- The only stat check is **Charisma persuasion**, colour-coded yellow (easy), orange (medium) and red (hard).
  Success chance depends on Charisma and gear; success gives XP. Results are rolled, so save-reload and
  Charisma clothing swaps beat it `[UNVERIFIED exact chance formula]`.
- Skill, perk and other SPECIAL checks, which Fallout 3 used and New Vegas made central, are essentially absent
  from the base game. Far Harbor restored some variety and more outcome choice `[UNVERIFIED extent]`.

### The critique

The widely shared summary is that the four slots are usually "yes", "sarcastic yes", "no, which the quest
turns into yes or defers", and "ask a question". The specific complaints:

- **Four-slot quota.** Writers had to fill exactly four slots every time. Where a scene had two real choices,
  two filler slots were added; where it deserved six, options were cut. Howard later said the system was hard
  on designers and writers.
- **Paraphrase mismatch.** The player cannot predict the line. The most downloaded early mods simply replaced
  paraphrases with full text.
- **Little consequence.** Most choices alter tone, not outcome. The main quest's branch is a single late
  choice of faction.
- **No character expression.** With no skill checks, a scientist, a brute and a thief say the same things.

### Voiced protagonist: costs

| Cost | Mechanism |
|---|---|
| Budget and schedule | Two actors, 13,000+ lines each, recorded over about two years; every added response costs two recordings |
| Fewer options | Recording cost is the practical reason for the four-option limit |
| Fixed identity | A defined pre-war spouse and parent with a set emotional goal; players who want to be a raider, a loner or a comedian fight the voice performance |
| Stat-blind writing | Low-Intelligence or skill-specific lines would multiply recording, so they were dropped |
| Mod friction | Quest mods must either leave the protagonist silent or splice existing lines |

Developer admissions: at E3 2016 Howard told GameSpot "the way we did some dialogue stuff, that didn't work as
well", and pointed to Far Harbor as a response. In a later interview (reported as GQ; date not verified in
this pass) he said the team "spent forever" on the system and that it "really did not resonate". Bethesda's
next two RPGs (Fallout 76's later NPC update and Starfield) returned to a silent protagonist with full-text
list dialogue and skill-based options.

## 12. Companions and affinity

| Rule | Value |
|---|---|
| Roster | 13 base game, plus Ada and custom robots (Automatron), Old Longfellow (Far Harbor), Porter Gage (Nuka-World) |
| Active limit | One at a time |
| Mortality | Essential while following; downed companions revive after combat (need a stimpak on Survival) |
| Affinity range | Starts 0; milestones at 250, 500 (admiration), 750, 1000 (idolise, perk granted); max 1100; -500 disdain, -1000 hatred and possible permanent departure |
| Event values | Like +15, love +35, dislike -15, hate -35, scaled x0.5 / x1 / x1.5 by event size; most repeatables are small (+7.5) |
| Cooldown | The same action cannot be farmed back-to-back; different actions count separately |
| Passive gain | Every 10 minutes of travelling together (if XP was earned): 40 - 0.033 x current affinity; 0 to 1000 takes about 520 minutes passively |
| Romance | Eight companions romanceable via a Charisma check at max affinity |

| Companion | Perk at max affinity |
|---|---|
| Cait | AP regenerates 25% faster below 25% health |
| Codsworth | +10 damage resistance against robot energy attacks |
| Curie | Heal 100 HP when below 10% health (once per day) |
| Danse | +20% damage against ferals, super mutants and synths |
| Deacon | +20% sneak attack damage, +40% Stealth Boy duration |
| Hancock | Critical meter fills 20% faster at 250+ rads |
| MacCready | +20% V.A.T.S. head hit chance |
| Nick Valentine | One extra hacking guess, 50% shorter terminal lockout |
| Piper | Double XP for persuasion and location discovery |
| Preston | +20% damage resistance and +20% damage against three or more opponents |
| Strong | +20% melee damage below 25% health |
| X6-88 | +20 energy resistance |
| Old Longfellow | Animals and sea creatures have 25% less damage and energy resistance |
| Porter Gage | +10 damage resistance, +5% kill XP |
| Dogmeat | No affinity; does not count against the Lone Wanderer perk |

Observations: companion perks are permanent and stack, so the optimal play is to cycle through every companion
to 1000 and then travel alone or with the dog. Affinity triggers are visible ("Piper liked that") and mostly
keyed to cheap repeatable actions (lockpicking, hacking, generosity, modding weapons), which encourages
farming rather than role-play. Companions do react to faction choices and can turn hostile, which is the
system's strongest role-playing hook. The Lone Wanderer perk (less damage taken, more carry weight, later more
damage `[UNVERIFIED values]`) is a rare example of the game paying the player for a play-style choice.

## 13. World design

- **Density over size.** The map is modest in area but packed: a marked location every few dozen metres in
  the urban core, with unmarked interiors, rooftops and vignettes between them. Travel time between points of
  interest is the shortest in the series.
- **Downtown Boston** is the showcase and the technical weak point: dense overlapping encounters (raiders,
  super mutants, Gunners fighting each other across streets) and the worst frame-rate drops in the game.
- **Verticality.** Elevated highway sections with camps on top, multi-storey ruins entered at street level and
  exited by rooftop, office towers with interior climbs, scaffolding and elevators as dungeon spines, and
  vertibird travel later. Power-armour jet packs open rooftop routes.
- **Regional difficulty.** The start is in the north-west corner. Enemy level bands rise roughly with distance
  south and east, peaking in the far south and the irradiated south-west zone. Each area (encounter zone)
  has a minimum and maximum level; enemies scale to the player inside that band. Community data-mining
  indicates central-city minimums are low, so scaling is still doing much of the work, and some random
  encounters ignore zones `[UNVERIFIED specifics]`. The practical effect is New Vegas-style soft walls with
  Bethesda-style scaling underneath.
- **Enemy tier ladders.** Each enemy family has named tiers (for example raider, raider scum, raider psycho,
  raider veteran) selected by level, plus a skull marker when an enemy far out-levels the player.
- **Environmental storytelling** is the game's best writing: staged skeleton tableaux, terminal logs,
  holotapes, and self-contained vault experiments told through spaces rather than dialogue.
- **Few towns.** One large city, a second smaller one, a handful of hamlets. Player-built settlements were
  meant to fill the gap and do not, because they have no authored characters or quests.
- **Loot placement** mixes hand-placed rewards (bobbleheads, magazines, power-armour frames, uniques) with
  levelled containers. Collectibles with permanent perks give every dungeon a known prize.

## 14. Enemies and AI

| Improvement | Detail |
|---|---|
| Cover use | Human enemies take and lean from cover, relocate, and throw grenades to flush the player |
| Feral ghouls | Lunging, tumbling attacks; play dead in ambush positions; limbs can be shot off to slow them |
| Limb-specific behaviour | Robots lose arms/weapons, self-destruct when crippled; insects fly or burrow |
| Burrowing and ambush | Mole rats and radscorpions tunnel and re-emerge behind the player |
| Suicide units | Super mutants carrying a live mini-nuke that can be shot in the arm |
| Enemy power armour | Raiders and others in suits; the fusion core can be shot or pickpocketed to force them out |
| Large set pieces | Behemoths, mirelurk queens, sentry bots that overheat and expose cores |
| Faction infighting | Patrols of different factions fight each other in the open world |
| Synths and Coursers | Teleporting elite enemies, stealth fields |

Weaknesses: high-level variety comes mainly from palette-swapped tiers with larger health pools (bullet
sponges at the top end, especially on higher difficulties where the player's damage is cut). Human enemies
remain predictable; stealth detection is generous once the relevant perks are taken. Enemy grenades and
molotovs are the main cause of sudden deaths, particularly on Survival.

## 15. Survival mode (patch 1.5, 2016)

Timeline: announced with a Steam beta on 29 March 2016; released in patch 1.5 on 28 April 2016 (PC) and
6 May 2016 (consoles). It replaced the launch "Survival" difficulty, which only changed damage numbers and
healing speed.

| System | Rule |
|---|---|
| Saving | No manual, quick or auto saves. Sleeping in a bed, mattress or sleeping bag saves. An exit-save exists but is deleted on load |
| Fast travel | Disabled. Exceptions: the faction teleport and vertibird signal grenades |
| Damage | Player deals 0.75x and takes 4.0x relative to Normal (1.5x / 2.0x relative to Very Hard) |
| Adrenaline | One rank per five kills, up to +50% damage dealt; reduced by sleeping in proportion to hours slept |
| XP | Enemies give double XP |
| Compass | Enemies no longer shown; location detection range reduced |
| Carry weight | Reduced; ammunition has weight (10mm round 0.025, mini-nuke 12, fusion core 4); over-encumbrance drains stats and damages legs |
| Healing | Stimpaks and food heal slowly; stimpaks and chems cause thirst; RadAway causes fatigue and immune suppression; drinking water heals 1.5 HP instead of 15 |
| Crippled limbs | Do not heal after combat; need a stimpak, a doctor or 2+ hours of sleep |
| Companions | Stay down until healed; go home if abandoned |
| Respawn | Uncleared locations 35 game days (7 normally), cleared 80 (20 normally) |
| Console | Disabled on PC |

| Need | Stages (game hours since satisfied) and penalties |
|---|---|
| Hunger | Peckish 6 h (-1 END), Hungry 12 h, Famished 24 h, Ravenous 36 h, Starving 64 h (-10 END, -5 CHR, -3 LCK, periodic damage) |
| Thirst | Parched 4 h (-1 INT), Thirsty 9 h, Mildly Dehydrated 18 h, Dehydrated 30 h, Severely Dehydrated 45 h (-10 INT, -7 PER, -3 LCK, periodic damage) |
| Sleep | Tired 27 h (-5% AP refresh), Overtired 40 h, Weary 55 h, Exhausted 69 h (cannot sprint), Incapacitated 82 h (-75% AP refresh, cannot run) |

Beds: sleeping bag maximum 3 hours, mattress 5 hours (cannot clear below "Tired"), real bed unlimited; 7+ hours
fully heals and grants a rested bonus. Diseases: fatigue, infection, insomnia, lethargy, parasites, weakness,
lasting 48-168 game hours; at most one per day; caught from creature attacks, raw food, dirty water, chem use
and poor sleep; cured by antibiotics or doctors.

### Why many consider it the definitive mode

- It **connects the systems.** Settlements become necessary waypoints (beds to save, water pumps, doctors,
  supply lines so junk need not be hauled). Cooking, antibiotics crafting, clean water and chems gain purpose.
  Local Leader, Strong Back, Lead Belly, Aquaboy and Medic stop being trap perks.
- No fast travel makes the dense world the content. Players learn routes, and vertibird grenades and
  settlement networks become real rewards.
- 4x incoming damage makes fights short and lethal in both directions. Combined with Adrenaline it avoids the
  bullet-sponge feel of Very Hard, and it makes cover, scouting and mines matter.
- Sleep-to-save produces real tension and real stakes for exploration.

### Complaints

- Sleep-only saving in a game with frequent crashes and quest bugs can cost an hour of play to a fault that is
  not the player's. This is the most common reason people mod the mode or abandon it.
- Disabling the console on PC removed the usual workaround for broken quests.
- Sudden deaths from unseen grenades, mines and suicide enemies feel unfair with long save gaps.
- The early game is brutally hard; by level 40 with stealth or power armour it is trivial again.
- Hunger and thirst are solved permanently by a single water pump and a cooking pot; they become chores
  rather than decisions.

## 16. Economy

- Currency is bottle caps. Vendors carry limited caps and restock on a timer, so selling loot is throttled
  by vendor cash rather than by price.
- Barter prices scale with Charisma and the Cap Collector perk. The commonly cited formula is buy multiplier
  = 3.5 - 0.15 x Charisma with a floor of 1.2, and sell = the reciprocal, capped at 0.8 `[UNVERIFIED]`.
  Charisma gear and chems before trading are standard practice.
- Money sinks are weak: ammunition, fusion cores, shipments of crafting components (25 to 200 units delivered
  as a note), a handful of vendor uniques, top-tier settlement shops, and a player home. There is no repair
  cost, no ammo crafting in the base game and no training cost.
- Money sources overwhelm the sinks: purified-water farming, selling surplus chems made at a chemistry
  station (Jet and its derivatives are cheap to make from fertiliser and plastic), shop income, and loot.
- Result: caps matter for roughly the first ten levels. After that the binding constraints are carry weight,
  specific rare components and perk gates.
- Ammunition is generous on standard difficulties, especially with the Scrounger perk; only on Survival, with
  weighted ammo, does calibre choice matter.

## 17. Add-on mechanics

| Add-on | Date | Price (USD) | Mechanical contribution |
|---|---|---|---|
| Automatron | 22 March 2016 | 9.99 | Robot workbench: build companions from interchangeable heads, torsos, arms, legs and weapons across Protectron, Assaultron, Mister Handy, Sentry Bot and Robobrain part families; robot enemies assembled from the same parts; starts at level 15; four main quests plus a radiant |
| Wasteland Workshop | 12 April 2016 | 4.99 | Cages to capture creatures and raiders, arena fights, more decor |
| Far Harbor | 19 May 2016 | 24.99 | Largest add-on landmass Bethesda had made; radioactive fog as a regional hazard pushed back by condenser devices; three-faction conflict with several endings including a negotiated peace; new perk ranks, legendary prefixes, weapons and armour; four settlements |
| Contraptions Workshop | 21 June 2016 | 4.99 | Conveyors, sorters, manufacturing machines (ammo, weapons, armour), logic gates, elevators |
| Vault-Tec Workshop | 26 July 2016 | 4.99 | Build a vault settlement; run experiments on dwellers |
| Nuka-World | 29 August 2016 | 19.99 | Theme-park map of distinct zones; player becomes boss of three raider gangs and can convert Commonwealth settlements into raider outposts; starts around level 30 |

Season pass: launched at 29.99 and was raised to 49.99 before the larger add-ons shipped `[UNVERIFIED]`.

Notes on the three substantial ones:

- **Automatron** is the strongest pure systems add-on. The part-swap grammar gives enemy robots real variety
  and gives the player a companion that is a build in its own right. Robots as provisioners remove the risk
  of supply-line settlers. It is short, and the robots outclass every authored companion in combat.
- **Far Harbor** is generally rated the best add-on and was explicitly cited by Howard as a response to
  dialogue criticism: more checks, more ways to resolve the central conflict, consequences that depend on
  what the player chooses to reveal. Its weakest part is a block-placement puzzle sequence inside a
  simulation, widely disliked as slow and out of genre. The fog-and-condenser idea (a hazard that defines
  where civilisation can exist) is mostly fiction rather than a manipulable system.
- **Nuka-World** finally lets the player be a villain, but arrives after most players have become the leader
  of the settler-protecting faction. Raider outposts are claimed by force or intimidation, need nearby
  vassal settlements to supply food, pay tribute into a chest, and permanently alienate the Minutemen
  quest-giver. The alternative is to kill the gang leaders at once, which skips most of the add-on's quests.
  Zone-claiming quests include several large collect-a-thons. Critics praised the park zones and criticised
  the binary structure and thin raider role-play `[UNVERIFIED outpost counts]`.

## 18. Creation Club, next-gen update and later editions

| Item | Date | Notes |
|---|---|---|
| Creation Kit and PC mods | 26 April 2016 | Official mod tools |
| Console mods | 31 May 2016 (Xbox One); PS4 later, without external assets | First Bethesda game with console mods |
| Creation Club | 29 August 2017 | Curated paid add-on items bought with credits (launch packs 1500 credits for 14.99, 3000 for 24.99, 5500 for 39.99). Launch catalogue was mostly skins and single items; criticised as paid mods and compared with a notorious earlier cosmetic DLC. Each update also broke script-extender mods |
| Game of the Year Edition | 26 September 2017 | Base game plus all six add-ons |
| Next-gen update | 25 April 2024 | Native PS5 / Xbox Series versions, 60 fps performance and quality modes, ultrawide support on PC, several Creation Club items made free, including a new quest line. Released alongside the TV series. Broke the script extender and many PC mods, shipped with a stretched ultrawide interface and a few new bugs; a follow-up patch came on 13 May 2024 |
| Anniversary Edition | 10 November 2025 | Bundles 150+ Creation Club items and a new in-game Creations menu; drew another round of negative user reviews over mod breakage and pricing |

Lesson: on PC a decade-old game's value is its mod ecosystem, and every official executable change has a cost
to that ecosystem. Players asked the publisher to stop updating.

## 19. Bugs and technical state

- Launch state was typical for the studio: quest-blocking script faults, companions and settlers stuck or
  teleporting onto roofs, settlement counters displaying wrong values (which then lower happiness), physics
  glitches, and crashes in dense downtown cells. A community unofficial patch fixes thousands of entries.
- Frame rate on consoles dropped well below 30 fps downtown and in some add-on areas.
- Physics and game speed are tied to frame rate; running well above 60 fps causes speed and physics faults.
- Notable exploits, several patched `[UNVERIFIED details]`: a launch vendor exploit that returned unlimited
  caps when selling ammunition back piecemeal; item duplication using the dog companion's fetch behaviour;
  duplication through workshop scrapping and conveyor timing; unlimited SPECIAL from re-picking the
  creation-book; settlement build-limit bypass by dropping and storing weapons; XP farming by repeatedly
  building and scrapping cheap settlement objects.
- Survival mode magnifies every stability problem because of sleep-only saves.

## 20. Balance assessment

### Dominant builds and strategies

| Build | Core pieces | Why it dominates |
|---|---|---|
| Stealth rifle | Sneak, Ninja, Mister Sandman, Rifleman, suppressed rifle, ideally Instigating or Two Shot | Multiplicative sneak bonuses on top of +100% rifle damage one-shot most enemies before combat starts; the vendor-sold two-shot rifle is available within hours |
| V.A.T.S. crit loop | High Luck and Agility, Four Leaf Clover, Critical Banker, Better Criticals, Grim Reaper's Sprint, Gunslinger | Crits ignore armour and always hit; AP refills on kills; the player is nearly invulnerable while V.A.T.S. is active |
| Blitz melee | Agility 9 Blitz, Big Leagues, Ninja, Rooted, a fast bleed/poison blade | Teleporting V.A.T.S. melee with damage scaling by distance, up to 10x sneak multiplier |
| Explosive automatics | Explosive shotgun, SMG or minigun plus Demolition Expert | Flat area damage per projectile bypasses the armour curve; clears rooms, including the user if careless |
| Wounding automatics | Wounding on any high-rate weapon | Stacking unresisted bleed kills the largest bosses |
| Junkie's or Bloodied | Stack addictions or stay near death | Largest raw multipliers; penalties are easily offset |
| Power-armour tank | Any late suit, Nuclear Physicist, Pain Train, Heavy Gunner | Over 1000 resistance plus flat reduction; cores are not scarce |
| Chem stacking | Chemist, Chem Resistant, Psycho-Jet variants, Overdrive | Time-slow plus damage boosts with no downside once addiction is negated |
| Idiot Savant levelling | Low Intelligence, save before quest hand-ins | Out-levels high-Intelligence characters; reload to force the 5x roll |

### Structural causes

- **Multiplicative stacking without caps:** weapon-class perk x sneak x legendary x chems x crit.
- **Flat riders versus a ratio-based armour curve** (section 5), which makes a few prefixes outliers and
  ordinary automatics weak.
- **No scarcity after the opening hours:** caps, ammunition, stimpaks and fusion cores all inflate.
- **Crafting outruns loot:** with rank 3-4 crafting perks, any base gun is better than most finds, so only
  legendary prefixes matter as drops.
- **No level cap and no exclusive choices:** every weakness can be bought off.
- **Enemy scaling by health pool:** high-tier enemies are slow to kill unless the player uses one of the
  dominant builds, which pushes players toward them.

### What feels great

- Moment-to-moment shooting, hit feedback and weapon handling.
- The crit meter and slowed V.A.T.S. as a tactical layer on real-time combat.
- The scavenging loop: clutter to components to visible upgrades.
- Modular weapons that change form, role and perk class on the bench.
- Power armour as a physical machine.
- Dense, vertical exploration with a prize in every location.
- Survival mode's way of making every sub-system relevant.
- A perk every level, always named and readable.

### What was lost as an RPG

- Skills, tag skills and traits, and with them distinct character sheets.
- Skill and attribute checks in dialogue; only Charisma remains.
- Dialogue breadth, predictability of what the character will say, and low-Intelligence or specialist lines.
- A blank-slate protagonist: voice and backstory fix who the character is.
- Non-violent quest resolution. Most quests are "go to a place and kill everything in it".
- Faction reputation and karma; only companion affinity and binary faction hostility remain.
- Meaningful mutually exclusive choices before the final act.
- Authored towns and side quests in quantity, displaced by settlements and radiant jobs.
- Equipment upkeep and ammunition variety as resource decisions (outside Survival).
- The slow climb to power: power armour and a deathclaw kill arrive in hour one.

### One-paragraph verdict

Fallout 4 solved the series' oldest mechanical weakness, the combat, and built an addictive loot-and-craft
loop around it. It paid for this by removing the systems through which a role-playing game lets the player
define a character and have the world respond to it. Its balance is loose in the player's favour from the
mid-game on, which suits a power-fantasy shooter and undermines a survival fiction. The Survival overhaul
shows that the underlying systems interlock well when scarcity and risk are restored; the base game simply
does not ask the player to engage with them.

## Design Takeaways

- **Fix the shooting first, but keep the character sheet in the loop.** Honour player aim, and let stats and
  skills change handling (sway, recoil recovery, reload speed, malfunction chance) rather than only damage.
- **Steal the crit meter.** A banked, player-triggered critical is better than a hidden roll. Extend the idea
  to other luck-style effects.
- **Slow-time targeting beats paused targeting** for tension, provided the damage reduction while targeting is
  not so large that it becomes an invulnerability button.
- **Do not replace skills with flat "+20% damage" perks.** If perks are the only progression, every perk must
  add a verb, a rule exception or a trade-off. Consider mutually exclusive branches and a level cap so builds
  stay distinct.
- **Keep non-combat checks.** Whatever replaces skills must still give dialogue, locks, machines and the world
  something to test besides Charisma. Show the check and the reason.
- **Unvoiced protagonist, full-text responses, variable option counts.** The voiced four-slot wheel cost two
  years of recording and bought the most criticised feature of the game. The studio itself reversed course.
- **Use a ratio-based armour curve with care.** It is elegant and scale-free, but flat bonus damage must be
  folded into the main hit before mitigation or it will break balance. Decide deliberately how rapid-fire
  weapons are meant to beat armour (armour penetration, shred, ammo types).
- **Make all clutter useful, and make it findable.** Component tagging is essential. Add friction through
  weight and through a small number of bottleneck components that tie into other systems (farming, trade).
- **Give money real sinks.** Repairs, ammunition crafting, training, bribes, base upkeep. Audit every passive
  income source; one uncapped faucet (water farming) ends the economy.
- **Make the powered suit a vehicle, and make fuel bite.** Keep frames, per-piece damage and a repair bay;
  make fuel rare, heavy and unsold by ordinary vendors. Do not hand out the fantasy in the first hour: let
  the player see one, fear one, then earn one.
- **Random legendary loot needs a floor and a ceiling.** Cull filler prefixes, cap outliers, and give players
  agency (re-rolling, transferring, targeted sources) so save-scumming is not the best strategy.
- **Base building must be woven into the main structure or left out.** If it exists, give settlers names,
  wants and stories, let settlements change the map and faction balance, and never let it replace authored
  towns. Keep the supply-line idea; it is an excellent reward for investment.
- **Never push generated quests.** Radiant jobs belong on a notice board the player opts into, with no hidden
  timers, no penalties for ignoring them, a separate log, and no unique rewards locked behind them.
- **Zone difficulty by geography and tell the player.** Regional level bands with visible warning signs give
  the world shape. Avoid health-pool inflation as the top-end difficulty lever.
- **Design the survival rules as the default, then offer relief.** The needs, travel and save rules that make
  the systems interlock should be the tuned baseline, with accessibility options layered on, rather than a
  patch a year later. Pair restricted saving with rock-solid stability and an emergency exit-save.
- **Needs must stay decisions.** If one pump and one pot solve hunger and thirst forever, they are chores.
  Tie them to route planning, spoilage, contamination and trade.
- **Companion approval should respond to meaningful choices,** not to repeatable trivia, and permanent
  companion perks should not reward cycling through everyone once and then discarding them.
- **Protect the mod ecosystem.** If the game is moddable, treat executable updates as breaking changes and
  avoid paid micro-content that fragments it.

## Sources

Consulted directly during this research pass:

- https://fallout.wiki/wiki/Fallout_4 (release, scores, shipment, DLC dates, update history)
- https://fallout.wiki/wiki/Fallout_4_combat (V.A.T.S. behaviour, damage taken in V.A.T.S., cover, sights)
- https://fallout.wiki/wiki/Fallout_4_V.A.T.S. (AP costs, queue limit, critical rules, related perks)
- https://fallout.wiki/wiki/Damage_Resistance_(Fallout_4) (damage formula, game settings, examples, critical formula, radiation, poison, bleed)
- https://fallout.wiki/wiki/Overview:Damage (cross-game comparison of damage systems)
- https://fallout.wiki/wiki/Fallout_4_perks (chart structure, level-286 figure, bobbleheads)
- https://fallout.wiki/wiki/Level_(Fallout_4) (XP formula, level limits)
- https://fallout.wiki/wiki/Fallout_4_power_armor (frame, models, spawn levels, per-piece reduction, restrictions)
- https://fallout.wiki/wiki/Fusion_core_(Fallout_4) (duration, drain, value, perk effects)
- https://fallout.wiki/wiki/Fallout_4_crafting (stations, 31 components, scrapping rarity and scalars)
- https://fallout.wiki/wiki/Fallout_4_weapon_mods (mod count, slots, perk gating, class by grip/receiver)
- https://fallout.wiki/wiki/Fallout_4_legendary_weapon_effects (prefix list and values)
- https://fallout.wiki/wiki/Fallout_4_settlements (count, population cap, production, supply lines)
- https://fallout.wiki/wiki/Happiness_(Fallout_4) (happiness components, caps, modifiers)
- https://fallout.wiki/wiki/Survival_mode (all Survival rules, stages, dates)
- https://fallout.wiki/wiki/Fallout_4_companions (roster, essential status, romance)
- https://fallout.wiki/wiki/Affinity (thresholds, event values, passive formula, companion perks)
- https://fallout.wiki/wiki/Automatron_(add-on) (start level, robot families, price, date)
- https://fallout.wiki/wiki/Far_Harbor_(add-on) (factions, endings, price, date)
- https://fallout.wiki/wiki/Nuka-World_(add-on) (premise, gangs, zones, price, date)
- https://www.kitguru.net/gaming/matthew-wilson/id-software-helped-build-the-shooting-mechanics-for-fallout-4 (Howard quotes on id Software, September 2015)
- https://www.pushsquare.com/news/2016/06/e3_2016_bethesda_admits_fallout_4s_dialogue_system_isnt_all_that_great (Howard's E3 2016 dialogue admission, via GameSpot)

Found through search and used via result summaries (not opened in full, or blocked/truncated on fetch):

- https://www.gamespot.com/articles/fallout-4-gunplay-modeled-after-destinys/1100-6431981/ (Destiny as reference; ex-Bungie designer)
- https://www.gamespot.com/articles/fallout-4-gun-gameplay-built-with-doom-devs-help/1100-6430602/ (id Software assistance)
- https://www.pcgamer.com/au/fallout-4-lead-todd-howard-dialogue-system-didnt-work-as-well (2016 admission)
- https://www.pcgamer.com/games/rpg/todd-howard-says-that-fallout-4s-cinematic-dialogue-system-really-did-not-resonate-with-players-even-though-bethesda-spent-forever-working-on-it (later admission)
- https://gamingbolt.com/fallout-4s-dialogue-system-was-hard-for-designers-and-writers-to-work-with-todd-howard
- https://techraptor.net/content/fallout-4s-dialogue-wheel-short-answers-make-no-sense (paraphrase critique)
- https://www.gameinformer.com/b/news/archive/2015/09/05/bethesda-completes-recording-of-fallout-4-39-s-111-000-lines-of-dialogue.aspx (111,000 lines)
- https://www.pcgamesn.com/fallout-4/fallout-4-is-going-to-talk-your-ear-off-with-over-111000-lines-of-spoken-dialogue
- https://www.tweaktown.com/news/46484/fallout-4-voice-acting-took-2-years-13-000-lines-dialogue/index.html (13,000 lines, two years)
- https://forums.nexusmods.com/topic/7197986-damage-formula-and-damage-resistance (formula cross-check)
- https://steamcommunity.com/app/377160/discussions/0/135510194253391896 (alternative statement of the armour formula)
- https://fallout4.wiki.fextralife.com/Difficulty+Modes (difficulty and legendary multipliers)
- https://www.nexusmods.com/fallout4/mods/218 (vanilla legendary spawn multipliers as documented by a mod)
- https://www.nexusmods.com/fallout4/mods/4078 (encounter-zone level data as documented by a mod)
- https://forums.nexusmods.com/topic/13466922-fallout-4-encounter-zones-and-their-minmax-levels-does-a-documented-list-exist-anywhere
- https://eip.gg/fallout4/guides/settlement-happiness/ and https://forums.nexusmods.com/topic/3646230-4-things-about-settlements-settlers-you-should-know (attack-chance formulas, conflicting)
- https://www.gameskinny.com/tips/idiot-savant-is-the-best-way-to-play-fallout-4/ (Idiot Savant)
- https://www.ibtimes.co.uk/fallout-4-survival-mode-bethesda-details-brutal-new-difficulty-announces-pc-beta-1552058 and https://www.tomshardware.com/uk/news/fallout-4-survival-mode-details,31499.html (Survival announcement coverage)
- https://www.pcgamer.com/the-fallout-4-creation-club-goes-live-with-3-horse-armor/ and https://www.tweaktown.com/news/58963/gamers-protest-bethesdas-creation-club/index.html (Creation Club launch and pricing)
- https://www.dexerto.com/fallout/fallout-4-next-gen-update-broken-mods-ultrawide-2664456 and https://gamesradar.com/fallout-4-devs-have-worked-to-minimize-the-number-of-mods-that-the-new-update-breaks (2024 update)

Not reachable in this pass: Nukapedia (fallout.fandom.com) returned HTTP 402 to automated fetches and its
mirror blocked bots, so Nukapedia-specific figures are among those tagged `[UNVERIFIED]`.
