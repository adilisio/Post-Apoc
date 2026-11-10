# Fallout 76 (2018–present): Gameplay, Systems and Balance

Scope: how Fallout 76 plays, how its systems are tuned, and how both changed between the November 2018
launch and the state of the game in November 2026 (latest shipped update: *The Slasher*, 15 September 2026).
Story, factions and art are covered elsewhere; this file is about mechanics, numbers and live-service design.

Confidence markers follow `CONVENTIONS.md`. Many launch-era numbers were patched repeatedly; where I could
not re-confirm a figure against a source in this pass it is tagged `[UNVERIFIED]` (it comes from general
knowledge of the game and should be re-checked before being relied on).

## Quick Reference

- **Format:** always-online shared-world survival RPG. ~24 players per public server on a map roughly 4x
  Fallout 4's; teams of 4; no dedicated public servers, no server browser, no persistent world state.
- **Launch (14 Nov 2018):** zero living human NPCs (robots, holotapes, terminals only), severe bugs, 400 lb
  stash, unstable servers, Metacritic in the low 50s `[UNVERIFIED exact score]`. Todd Howard later said there was
  "very little we didn't screw up".
- **Redemption arc was mechanical, not marketing:** *Wastelanders* (Apr 2020) added human NPCs and dialogue;
  *One Wasteland* (Sep 2020) scaled every enemy to each player; *Steel Dawn* (Nov 2020) turned hunger/thirst
  from penalties into buffs; stash went 400 -> 600 -> 800 -> 1,200 lb.
- **Builds:** 56 SPECIAL points by level 50 (1 per stat + 49), max 15 per stat, perk cards cost points equal
  to their rank. Six legendary perk slots unlock at levels 50/75/100/150/200/300. Respec is cheap and got
  cheaper every year.
- **V.A.T.S. is real-time:** no pause or slow-mo; it is an AP-fuelled aim-assist/crit engine. It defined the
  ranged meta for seven years and was rewritten in 2025.
- **C.A.M.P.** (movable personal base, later two+ slots, shelters, vending, allies, pets, "Best Builds")
  became the game's most loved feature and its main social surface.
- **Mutations** (19, up to 18 at once) are the cheapest large power spike in the game; nearly every endgame
  build runs a standard mutation package locked in by one perk card.
- **Legendary gear:** 1–3 random stars at launch, RNG re-rolls from 2021, deterministic mod crafting from
  Sep 2024, 4th star from Dec 2024.
- **Dominant builds:** low-health "bloodied/unyielding", power-armor heavy gunner, stealth commando,
  V.A.T.S. railway/crit builds, auto-melee (Auto Axe/Chainsaw). Bethesda spent 2024–2025 doing a ground-up
  combat rebalance to break the "three mandatory damage cards" pattern.
- **Endgame:** player-launched nukes spawn world bosses (Scorchbeast Queen, Earle Williams, Ultracite Titan);
  Daily Ops (2020), Expeditions (2022), a 4-player raid (Dec 2024), Infestations (Jun 2026).
- **PvP failed.** Consent-based "slap damage" PvP, the Survival mode (2019) and the Nuclear Winter battle
  royale (2019–2021) were all removed or sidelined; the audience was overwhelmingly PvE/co-op.
- **Monetisation** broke a "cosmetic only" promise (repair kits, Apr 2019) and added a US$12.99/month
  subscription (Fallout 1st, Oct 2019) whose headline perk, an unlimited scrap box, sells relief from the
  game's own stash limit.
- **Community:** famously friendly; veterans gift newcomers. Developers say they expected the opposite.
- **Audience:** Steam all-time peak ~73k concurrent in April 2024 after the TV show; ~1 million players
  across platforms in one day; a second, smaller bump after show Season 2 (Dec 2025).
- **Current direction (2026):** depth over map size; native PS5/Xbox Series versions (Sep 2026); pets as
  combat companions (Dec 2026); Raven Rock expansion planned for summer 2027.

## 1. Timeline of major updates

Dates from the falloutbuilds.com update index, cross-checked against Bethesda release notes where fetched.

| Date | Update | Mechanical significance |
|---|---|---|
| 14 Nov 2018 | Launch | 24-player servers, no human NPCs, 400 lb stash, hunger/thirst penalties |
| 4 Dec 2018 | Patch 1.0.2 | Stash 400 -> 600 lb |
| 19 Feb 2019 | Patch 6 | Stash 600 -> 800 lb |
| 13 Mar 2019 | Wild Appalachia | Brewing, Fasnacht seasonal event, Survival mode (beta), legendary vendor, player vending (May) |
| Apr 2019 | Repair kits | First non-cosmetic Atomic Shop item |
| 10 Jun 2019 | Nuclear Winter | 52-player battle royale (shut down Sep 2021) |
| 20 Aug 2019 | Vault 94 raid | First raid; removed with Wastelanders |
| 23 Oct 2019 | Fallout 1st | Subscription: private worlds, scrap box, tent |
| 14 Apr 2020 | Wastelanders | Human NPCs, dialogue trees, reputation, gold bullion, allies; Steam release |
| 30 Jun 2020 | Seasons / The Legendary Run | Battle-pass-style scoreboard; Public Teams |
| 15 Sep 2020 | One Wasteland for All | Per-player level scaling, Daily Ops, legendary perks, damage formula change |
| 24 Nov 2020 | Steel Dawn | Shelters (instanced interiors); hunger/thirst penalties removed |
| Jan 2021 | Inventory Update | Stash 800 -> 1,200 lb |
| 27 Apr 2021 | Locked & Loaded | SPECIAL loadouts (Punch Card Machine), second C.A.M.P. slot |
| 7 Jul 2021 | Steel Reign | Legendary crafting (random re-rolls), currency cap raises |
| 8 Sep 2021 | Fallout Worlds | Public Worlds + Custom Worlds; Nuclear Winter removed |
| 13 Sep 2022 | Expeditions: The Pitt | Instanced off-map missions, Stamps currency |
| 6 Dec 2022 | Nuka-World on Tour | New region boss (Ultracite Titan) |
| 28 Feb 2023 | Mutation Invasion | Mutated public events |
| 5 Dec 2023 / 26 Mar 2024 | Atlantic City (2 parts) | Second expedition hub; Season 16 replaces scoreboard with ticket-based pass |
| 12 Jun 2024 | Skyline Valley | First map expansion; start of the combat rebalance |
| 3 Sep 2024 | Milepost Zero | Deterministic legendary crafting, caravans, Best Builds |
| 3 Dec 2024 | Gleaming Depths | 4-player raid, 4-star legendaries, C.A.M.P. pets, perk consolidation |
| 18 Mar 2025 | Ghoul Within | Playable ghoul; perks catalog |
| 3 Jun 2025 | Gone Fission | Fishing |
| 2 Sep 2025 | C.A.M.P. Revamp | Relaxed build rules, new build UI, item locking; large weapon/perk rebalance |
| 2 Dec 2025 | Burning Springs | New region (SE Ohio), repeatable bounty hunting, 16 new legendary effects |
| 3 Mar 2026 | The Backwoods | Cryptid boss content, event changes |
| 2 Jun 2026 | Infestations | Roaming faction takeovers with guaranteed 4-star boss drops; radiation overhaul |
| 15 Sep 2026 | The Slasher | Weekly-unlocking story event, Legacy Seasons, re-moddable unique weapons, native PS5/Series X\|S |
| Dec 2026 (planned) | World Pets | C.A.M.P. pets follow, level and fight; four commands (Stay/Follow/Protect/Kill) |
| Spring 2027 (planned) | Expanded Bounties, Hideouts | Mid-tier challenge spaces between events and raids, soloable |
| Summer 2027 (planned) | Raven Rock | Largest planned addition; Enclave-focused region |

## 2. Online structure

| Mode | Players | Persistence | Notes |
|---|---|---|---|
| Adventure (public) | ~24 per server, teams of 4 | Character persists; world does not | No server browser; you are dropped onto a random instance. Your C.A.M.P. loads in if its spot is free |
| Private World (Fallout 1st) | Up to 8 `[UNVERIFIED]` | Same character | Added Oct 2019. At launch players found them not truly private/fresh (looted containers, friends-list joins) |
| Public Worlds (Sep 2021) | ~24 | Separate progression | Rotating Bethesda-authored rule sets; later dropped from focus `[UNVERIFIED current status]` |
| Custom Worlds (Sep 2021, Fallout 1st) | Up to 8 `[UNVERIFIED]` | Progress does not transfer to Adventure | Sliders for building rules, enemy difficulty, weather, etc. |
| Nuclear Winter (2019–2021) | 52 | Separate perk set and rank track | Battle royale; removed |
| Instanced content | 4 (raid, Daily Ops, Expeditions); 8 (Earle Williams boss) `[UNVERIFIED 8]` | — | Matchmade through Public Teams |

Design consequences:

- **24 players on a very large map means you rarely collide by accident.** Density is created by free fast
  travel to public events, to teammates and to player C.A.M.P.s. The game is functionally a solo RPG with
  pop-in co-op.
- **No world persistence.** Workshops (capturable resource bases) reset when you log out, which made them
  poor long-term investments and removed most reason to fight over them.
- **No human NPCs at launch** was a deliberate thesis: "every human you meet is a real player". In practice
  quests became scavenger hunts ending at corpses and holotapes, and with 24 players there were not enough
  humans to fill the role. Wastelanders reversed it 17 months later. Lesson: players can add *texture* to a
  world but cannot replace authored characters as quest-givers, merchants or moral stakes.
- **Public Teams (Jun 2020)** were a quiet structural fix: one-click, no-obligation teams with a themed bonus
  (e.g. bonus XP for Casual/Events teams, shared Intelligence scaling). Most servers run full public teams
  where nobody talks and everyone benefits. This is the game's real grouping model.

## 3. SPECIAL and the perk-card system

### 3.1 Core rules

| Rule | Value |
|---|---|
| Starting SPECIAL | 1 in each of 7 stats |
| Points gained | 1 per level from 2 to 50 (49 points) -> 56 total (Nukes & Dragons planner shows 49 to allocate) |
| Cap per stat | 15 (base) |
| Perk card cost | Points equal to the card's rank; a stat of N holds N points of cards |
| Card ranks | 1–5 depending on card (most are 1–3); ranking up historically needed duplicate cards |
| Perk card packs | Every 2 levels from 4 to 10, then every 5 levels; 4 random cards per pack |
| Past level 50 | No more SPECIAL points; each level grants a card pick or (from early 2019) a one-point SPECIAL move |
| Level cap | None |
| Card sharing | Team perk sharing gated by Charisma (3 CHA per rank shared) `[UNVERIFIED ratio]` |

The base model is Fallout 4's perk chart cut into a deck: SPECIAL is both your attributes *and* your slot
budget. Strength 15 means 15 points of Strength cards, so a stat is valuable twice over. This is elegant and
readable, and it makes "what do I drop to fit this?" the core build question.

### 3.2 Legendary perks (Sep 2020)

| Rule | Value |
|---|---|
| Slots | 6, unlocking at levels 50 / 75 / 100 / 150 / 200 / 300 (account-wide once reached) |
| Ranks | 4 per card; rank 1 free |
| Upgrade cost | 50 + 100 + 150 = 300 perk coins to max a card `[per-rank split UNVERIFIED; 300 total confirmed]` |
| Perk coins | Scrapping normal cards: 2 coins per card rank |
| Legendary SPECIAL cards | +1/+2/+3/+5 to a stat *and* its perk-point budget (stat cap for points stays 15) |

Maxing six cards costs ~1,800 coins, i.e. hundreds of levels of surplus cards. This is the long-tail grind
that gives levels 50–500+ a purpose. The slot at level 300 is widely seen as too far out.

### 3.3 Respec and loadouts over time

| Period | Respec friction |
|---|---|
| Launch | None possible except swapping equipped cards; SPECIAL locked forever |
| Early 2019 | After 50, trade a level-up for moving 1 SPECIAL point (56 levels to fully rebuild) |
| Apr 2021 (Locked & Loaded) | Punch Card Machine: free full SPECIAL reallocation + saved loadouts (2 slots at first, more added/sold later `[UNVERIFIED counts]`) |
| Dec 2024 (Gleaming Depths) | Many 3-rank utility cards collapsed to 1 rank (Lone Wanderer, Starched Genes, Bloodsucker, First Aid...), weight-reduction cards cut from 3 to 2 ranks at 45%/90% — freeing points |
| Mar 2025 (Ghoul Within) | "Perks catalog" UI; ghoul-only card set (sources say 30–35 cards `[DISPUTED count]`) |
| 2025 rebalance | Flat "+damage%" weapon cards removed/reworked (see §8) |

Assessment: the system supports builds well *in principle* (transparent budget, free swapping, shareable
planners such as Nukes & Dragons). In practice, for six years it was distorted by:

1. **Mandatory damage tax.** Each weapon class had three cards (base/Expert/Master) at up to +20% each.
   Nine of your ~15 points in a stat went to a non-choice.
2. **Quality-of-life cards competing with combat cards.** Weight reduction, lockpicking, hacking, crafting
   and repair perks had to be swapped in and out manually, which is busywork, not a decision. The community
   called it "perk card shuffling"; loadouts and the 2024 consolidation were direct responses.
3. **Random packs at low level** occasionally hand a new player nothing usable; harmless but pointless RNG.

## 4. Real-time V.A.T.S.

- No pause, no slow motion. Activating V.A.T.S. locks onto a target with a percentage hit chance; each shot
  spends Action Points. Limb targeting requires a perk card (Concentrated Fire) rather than being default.
- A crit meter fills per hit (scaled by Luck) and can be banked and spent for a guaranteed hit with bonus
  damage. With high Luck and the right cards, players reached a guaranteed critical **every second shot**.
- Effects: (a) accessibility — players who cannot aim well can still play a shooter; (b) lag compensation in
  an engine with shaky hit registration; (c) a parallel "AP economy" build axis (AP regen, AP cost reduction,
  crit damage) distinct from free-aim builds.
- It was also the strongest thing in the game. Bosses' damage reduction was partly bypassed by V.A.T.S.
  crits until Milepost Zero (Sep 2024) closed that.
- **2025 rewrite** (Bethesda "Upcoming combat and perk changes", 27 Jun 2025; shipped with the September 2025
  update): hit chance capped at 95% and falls off with distance, visibility, body-part difficulty, recoil
  and fire rate; beyond roughly half a weapon's range it trends to 0%. Luck's contribution to the crit meter
  was cut so a fill takes about 3–4 hits instead of 2. Perception now reduces range penalties. Free-aim got
  compensating buffs (tighter cones, less recoil, damage falloff to 10% at double range rather than a cliff).

Takeaway: a real-time V.A.T.S. works as an *assist mode with its own resource*, but if it also guarantees
hits at any range and feeds a guaranteed-crit loop it will out-compete manual aim for everyone.

## 5. C.A.M.P. building

How it works: a deployable device defines a build radius almost anywhere on the map. Structures are saved as
a blueprint and travel with you between servers; moving costs a trivial cap fee `[UNVERIFIED: later free]`.
A build "budget" bar (not a piece count) limits complexity for server-performance reasons.

| Date | C.A.M.P. change |
|---|---|
| Launch | One C.A.M.P.; budget widely seen as too small; base could fail to place if another player's occupied the spot |
| May 2019 | Vending machines: sell to other players, map icon advertises your shop, free-ish fast travel point |
| Apr 2020 | Allies (NPC companions that live at camp and give daily quests) |
| Nov 2020 | Shelters: instanced interiors with their own separate budget |
| Apr 2021 | Second C.A.M.P. slot (more sold via Atomic Shop) |
| Sep 2024 | Best Builds: submit a camp, others visit as a fast-travel location and "Like" it; rotates hourly |
| Dec 2024 | Pets (cat, dog; one pet + one ally per camp; pets bring small loot) |
| Sep 2025 | C.A.M.P. Revamp: three snap/placement modes incl. free placement, pick-up-and-move edit mode, replace-in-place, new menu |
| 2026 | Radhog and Deathclaw pets (paid); pets become field companions (planned Dec 2026) |

Why it became the most loved feature:

1. **It is the one persistent mark a player leaves on a non-persistent world.** Everything else resets; the
   camp follows you.
2. **It is advertised to everyone.** Camps appear on the map; visiting one is a free fast-travel hop. The
   vending machine gives strangers a reason to come, so building has an audience. Shopping tours of player
   camps became a core activity in their own right.
3. **It is functional.** Crafting benches, stash access, resource extractors, buff-granting items, a bed for
   the rested XP bonus. A camp is a tool before it is a dollhouse.
4. **Location is expression.** Cliff edges, lake houses, a shack beside a boss arena to sell ammo.
5. **Players routinely beat the rule set.** For years the best builds relied on glitch techniques (merging,
   floating foundations). The 2025 revamp effectively legalised them — a strong signal that restrictive
   placement rules were never serving players.
6. **It is the monetisation sweet spot.** Most Atomic Shop revenue is cosmetic building kits, which players
   tolerate far better than convenience items.

Persistent complaints: the budget cap, camp-placement conflicts, and that most of the best building pieces
are paid.

## 6. Survival meters

| | Launch (2018) | After Steel Dawn (24 Nov 2020) |
|---|---|---|
| Hunger / thirst | Decaying meters; low values cut AP/AP regen and eventually drained health `[UNVERIFIED exact thresholds]` | No negative effects at any level |
| Reward for maintaining | None (avoid penalty only) | Tiered buffs; full bars also grant +1 Endurance and +1 Strength (Bethesda Steel Dawn notes). Nukes & Dragons lists "Fully Fed: Max HP +35", "Fully Hydrated: AP regen +35%" |
| Food spoilage | Yes; condition bar on food | Still present, mitigated by fridge items/perks/backpack mods |
| Diseases | Random from creatures, water, sleeping on the ground | Still present, minor; 2024 perks reward being *not* diseased |
| Radiation | Reduces max HP; chance of mutation | Same; overhauled Jun 2026 (stronger per-point resistance, much hotter hazard zones, non-power-armor rad resistance cut 45–65%) |
| Ghoul characters (2025) | — | No hunger/thirst at all; radiation heals and builds a "Glow" overshield; a separate "feral" meter replaces food pressure |

The conversion from penalty to buff is the single cleanest design lesson in the game. As a penalty, the meter
was a chore tax on every session with no interesting decision (food was abundant; the cost was inventory
weight and interruptions). As a buff it became an opt-in optimisation layer that feeds cooking, farming and
player trading. Nobody asked for the penalties back.

## 7. Mutations

Acquired randomly from radiation exposure or deterministically from serums (recipes sold by an endgame vendor
at ~17,500–24,000 caps each depending on barter modifiers; serums themselves are cheap on the player market).
19 mutations exist; 18 can be held at once (Carnivore and Herbivore exclude each other). RadAway can cure
them unless you equip Starched Genes.

| Mutation | Upside | Downside |
|---|---|---|
| Marsupial | Much higher jump, +20 carry weight | -4 INT |
| Speed Demon | +20% move speed, +30% reload speed | +50% hunger/thirst drain while moving |
| Adrenal Reaction | Now: +5% damage per kill-streak stack (10 stacks). Originally: more damage at low HP `[RETCON — reworked in the 2025 rebalance]` | -50 max HP |
| Bird Bones | +4 AGI, slow fall | -4 STR |
| Eagle Eyes | +50% crit damage, +4 PER | -4 STR |
| Egg Head | +6 INT | -3 STR, -3 END |
| Herd Mentality | +2 all SPECIAL in a team | -2 all SPECIAL solo |
| Healing Factor | +300% health regen | -55% chem effects |
| Scaly Skin | +50 damage and energy resistance | -50 AP |
| Grounded | +100 energy resistance | -50% energy weapon damage |
| Twisted Muscles | +25% melee damage, limb damage | -50% gun accuracy |
| Talons | +25% unarmed damage, bleed | -4 AGI |
| Empath | Teammates take -25% damage | You take more |
| Carnivore / Herbivore | Double benefit from meat / plants, no disease | No benefit from the other |
| Chameleon, Electrically Charged, Unstable Isotope, Plague Walker | Situational procs | Minor or none |

Supporting cards: **Starched Genes** (never gain/lose mutations; 1 rank since Dec 2024), **Class Freak**
(reduces downsides, up to -75% at rank 3 `[UNVERIFIED]`), **Strange in Numbers** (+25% upsides when
teammates are mutated `[UNVERIFIED]`).

Balance reading: the intended trade-off evaporates. With Class Freak, penalties shrink to rounding errors,
and because Herd Mentality is positive in the ever-present public teams, the "standard package" (Marsupial,
Speed Demon, Bird Bones, Eagle Eyes, Egg Head, Herd Mentality, Adrenal Reaction, Carnivore/Herbivore...) is
close to universal. Marsupial changes traversal so much that level design is effectively built around it.
Mutations are *identity-defining for the game* but not *differentiating between builds*.

## 8. Legendary items

### 8.1 Structure

| Star | Slot role | Typical examples |
|---|---|---|
| 1 | Prefix — defines the item | Bloodied (damage scales as health drops), Anti-Armor, Two Shot, Vampire's, Quad (4x magazine), Furious, Instigating, Junkie's; armor: Unyielding, Overeater's, Vanguard's |
| 2 | Major | Explosive bullets, faster fire rate, +50% crit damage, V.A.T.S. hit chance; armor: +SPECIAL, AP regen |
| 3 | Minor | -25% V.A.T.S. AP cost, faster reload, 90% reduced weight, +1 stat |
| 4 (Dec 2024) | Raid/endgame tier | Stacking set-like bonuses, e.g. armor pieces each adding 5% (to 25%); crits restoring 5% HP/AP to nearby teammates; Stabilizer's; Severing (+50% vs bleeding, 2026); Tarnished (damage rises as condition falls, up to +120%, 2026) |

### 8.2 Acquisition model over time

| Era | Model | Problem |
|---|---|---|
| 2018 | Pure drop RNG from legendary enemies | "God rolls" astronomically rare; duped copies flooded trade |
| May 2019 | Legendary scrip: scrap unwanted legendaries, buy random ones from a vendor; daily scrip earn limit (150, later raised `[UNVERIFIED later values]`) | Still slot-machine RNG; daily caps create login chores |
| Jul 2021 | Legendary crafting: spend modules + cores to re-roll all stars on any item | Deterministic *item*, random *effects*; thousands of rolls for one target |
| 3 Sep 2024 | Scrap legendaries for scrip, a chance at a loose mod box, and a (low) chance to permanently learn that mod; craft learned mods; attach chosen mods for scrip with rising cost per swap; crafted items become character-bound; cores converted 1:1 to scrip | Learn rates considered very low by players `[UNVERIFIED exact %]`; binding removes crafted items from the trade economy (intended anti-dupe) |
| Dec 2024 | 4-star mods from the raid; loose mods tradeable, applied mods not | Raid farm became the dominant source |
| Dec 2025 | 16 new 1–3 star effects from bounty hunts, many keyed to kill streaks | — |
| Jun 2026 | Infestation bosses guarantee a 4-star drop | Devs admit they are cleared in ~a minute; difficulty being raised |
| Sep 2026 | 80+ named unique weapons can have their legendary mods changed | Removes "trap" uniques |

The 2024 overhaul is the important lesson: after six years the game moved from *RNG on outcome* to *RNG on
unlock, determinism on outcome*. Players can now plan a build and work toward it. Reception was strongly
positive in principle with complaints about unlock rates.

## 9. Dominant builds and nerf history

| Build | Why it dominated | What was done |
|---|---|---|
| **Two Shot Explosive (TSE) guns** (2018–Jan 2019) | Two Shot doubled damage, Explosive doubled it again; trivialised everything; mass-duplicated | Jan 2019: Two Shot cut to +25%, Explosive to +20% `[UNVERIFIED exact values]`. Two Shot later reduced further (2024) |
| **Explosive energy "legacy" weapons** (2018–2023) | Effect combination removed from drop tables early, but existing (heavily duped) copies kept working for four years; orders of magnitude above legal gear | Removed/neutralised in an early-2023 patch `[UNVERIFIED exact date]` |
| **Bloodied + Unyielding** (2018–2025) | Stay at ~20% HP by holding radiation damage. Bloodied weapon bonus + Adrenal Reaction + Nerd Rage, and Unyielding armor giving up to +3 to six SPECIAL stats per piece (+15 with five pieces): more damage, more AP, more carry weight, and more XP via Intelligence. Survivability from dodge perks and V.A.T.S. alpha damage | One Wasteland (2020) made damage bonuses additive rather than multiplicative (fallout.wiki), cutting the ceiling. 2025: Adrenal Reaction decoupled from low health (now kill-streak based); low-health damage shifted toward the weapon effect and Nerd Rage. Still viable, no longer strictly best |
| **Stealth commando** (2019–2025) | Suppressed automatic rifle (The Fixer, Handmade), sneak multiplier, V.A.T.S. crit every other shot, usually also bloodied. Highest single-target DPS with good ammo economy | V.A.T.S. accuracy nerfs (2021 `[UNVERIFIED]`, Dec 2024, 2025); weak-point multiplier 2.0x -> 1.5x (Dec 2024); crit meter slowed (2025). Sneak damage made multiplicative and suppressors given +50% sneak damage (2025) — stealth compensated |
| **Heavy gunner in power armor** (2018–present) | The "can't die" build: power armor's flat damage reduction, Emergency Protocols, Vampire's weapons; forgiving for casual play; the standard boss/event build | Mostly buffed: heavy weapon V.A.T.S. AP costs slashed (Minigun, Gatling Laser 30 -> 8; Dec 2024). 2025 rework replaced the three flat damage cards with a "Bullet Storm" stacking mechanic (+3/6/9% per stack, 10 stacks, stack per 50 rounds, lost on reload) |
| **Auto-melee** (Auto Axe, Chainsaw; 2022–2024) | Continuous-hit weapons multiplied every on-hit effect; with Vampire's, unkillable | Auto Axe damage 31 -> 24 (Dec 2024); AP cost 4 -> 9 (2025) |
| **Railway rifle V.A.T.S.** (2022–2024) | Auto receiver + very low AP cost + crit loop | Sep 2024: auto piston fire rate reduced, AP reduction removed |
| **Cremator / fire DoT** (2024) | Burn stacked and bypassed boss resistances | Sep 2024 DoT overhaul: burn reduced, DoT made subject to resistances, overlapping DoTs no longer stack |
| **Ghoul builds** (2025–) | Radiation as healing + Glow overshield; strong full-health tank/melee | Jun 2026: rad-to-health conversion raised to 35% but default rad resistance set to -50 and hazard values raised |

### The 2024–2025 combat rebalance

Bethesda's stated problem: build diversity had collapsed because flat multiplicative-feeling damage stacks
(three weapon cards, bloodied, Adrenal, crits) dwarfed everything else, and enemies were tuned for it.
Phases:

1. **Jun 2024 (Skyline Valley):** creature health/resistance/damage pass begins.
2. **Sep 2024:** damage-over-time overhaul; ~70 items retuned; 19 creatures retuned; boss damage reduction can
   no longer be partly bypassed by crits and DoT.
3. **Dec 2024:** perk consolidation, weak-point multiplier 2.0x -> 1.5x, heavy armor reclassification, AP cost
   pass.
4. **Mar 2025:** "Onslaught" stacking system for pistols etc. (stacks build while firing and expire after 10 s;
   the Furious effect became +5% per stack, 9 stacks, per PTS notes `[UNVERIFIED final values]`).
5. **Sep 2025:** the big one. Flat damage cards for heavy, melee, bow classes replaced with conditional
   mechanics (vs crippled, vs bleeding, bounce shots, area cleave), and the lost damage baked into base
   weapons. Examples from Bethesda's preview: Assault Rifle 66 -> 112, Combat Rifle 53 -> 95, Hunting Rifle
   171 -> 285, Super Sledge 107 -> 271, Tomahawk 100 -> 506, Fat Man explosion 455 -> 1,386, Frag Grenade
   150 -> 300. Prime receivers went from +25% to +100% damage with drawbacks. Auto-revive perks became 100%
   reliable on cooldowns instead of chance-based.

Design reading: this is a live game admitting that **"+X% damage with weapon type" perks are a design
failure** — a tax that looks like a choice — and replacing them with perks that change *how* a weapon plays.
It took seven years and a multi-phase rebuild to undo. Community reception was mixed: melee and explosives
praised, V.A.T.S./commando players unhappy, general agreement that more weapons are viable than ever.

## 10. Friction systems: durability, weight, stash

| System | Rule | Player response |
|---|---|---|
| Weapon/armor durability | Gear degrades with use and breaks; repaired with scrap at a bench; perks can repair to 200% | Tolerated as a scrap sink, resented when Bethesda sold Repair Kits for real money (Apr 2019). The raid team buff that *reduces* durability loss shows the devs know it bites hardest in long fights |
| Carry weight | Base 150 + 5 per Strength `[UNVERIFIED]`; over-encumbered = AP drain, no fast travel | Whole perk categories exist only to offset weight (cut to 2 ranks at 45%/90% in Dec 2024) |
| Stash | 400 lb (launch) -> 600 (4 Dec 2018) -> 800 (19 Feb 2019) -> 1,200 (Jan 2021). Shared across all stash boxes | The most persistent complaint in the game's history. Bethesda cited server item-tracking limits for the original cap |
| Scrap box | Unlimited component storage, Fallout 1st only (Oct 2019) | Seen as selling the cure to a deliberately induced problem |
| Ammo box | Unlimited ammo storage, Fallout 1st only (added 2022 `[UNVERIFIED date]`) | Same |
| Currency caps | Caps max 40,000 (shown in Nukes & Dragons; 25,000/30,000 earlier `[UNVERIFIED]`); daily vendor cap pool; daily scrip and bullion limits | Daily limits read as retention levers, not economy design |

A loot-heavy crafting game with a weight-limited stash produces a specific failure: the dominant minute-to-
minute activity becomes **inventory accountancy**. Fallout 76's entire loop says "pick everything up" while
its storage says "you can't keep it". Every stash increase was received as the best feature of its patch.

## 11. Public events, world bosses and nukes

- **Public events** start on a regular cadence (roughly every 20 minutes `[UNVERIFIED]`), appear on everyone's
  map and offer free fast travel. They are the main way 24 scattered players converge. The best-loved
  (Radiation Rumble, Eviction Notice, Moonshine Jamboree, Fasnacht parade) are short, readable defence or
  escort objectives with high legendary/XP yield.
- **Seasonal events** (Fasnacht, Mothman Equinox, Invaders from Beyond, Mischief Night, the 2026 Slasher
  arc) carry ultra-rare cosmetic drops (often 2–5% or lower) that drive the trading scene.
- **Mutated events** (2023) add a random enemy modifier and better rewards for team participation.

| World boss | Trigger | Notes |
|---|---|---|
| Scorchbeast Queen ("Scorched Earth") | Nuke Fissure Site Prime | Original endgame; timed fight; drops Improved Repair Kits, rare plans |
| Wendigo Colossus / Earle Williams ("A Colossal Problem") | Nuke Monongah Mine | Added 2020; instanced, small-group entry |
| Ultracite Titan ("Seismic Activity") | Nuka-World on Tour event (Dec 2022) | Region boss |
| Storm-themed boss ("Neurological Warfare") | Nuke in Skyline Valley (2024) `[UNVERIFIED details]` | — |
| Imposter Sheepsquatch ("Encryptid") | Player spends a crafted keycard | One player pays to start a server-wide event — a nice generosity mechanic |
| Raid bosses (Gleaming Depths, Dec 2024) | 4-player instanced raid, 5 encounters, no revives mid-encounter, no lockout timer | Source of 4-star gear |

**Nuke launching** is the most distinctive endgame idea: collect code fragments from special enemies, solve a
weekly cipher, fight through a missile-silo dungeon, then target any point on the map. The blast zone becomes
a temporary high-level area with unique crafting materials (flux) and, at the right coordinates, a world
boss. What worked: a player-authored, server-wide event that everyone can join; real spectacle. What did not:
the cipher was solved by community websites within days and codes are simply published weekly, so the
"puzzle" became a lookup; nuking player camps was a griefing vector (camps are repairable, so the sting is
small); three simultaneous nukes crashed a server at launch. After 2020 it is essentially "the button a
high-level player presses to start the boss fight".

## 12. Instanced endgame

| Activity | Added | Format | Assessment |
|---|---|---|---|
| Vault 94 raid | Aug 2019 | 4-player, no matchmaking, bug-ridden | Removed with Wastelanders (Apr 2020) |
| Daily Ops | Sep 2020 | Short randomised instanced mission; enemy faction + mutator rotate daily; time-tiered rewards; ammo effectively refunded | Good "20-minute" content; mutators that hard-counter builds (e.g. melee-kill-only) are disliked |
| Expeditions | Sep 2022 (The Pitt), Dec 2023/Mar 2024 (Atlantic City) | Story missions off-map; Stamps currency for a fixed reward shop | Deterministic reward shop praised; initial gating behind daily chores was removed after backlash |
| Caravans | Sep 2024 | Escort event with a personal outpost progression; faster if others help | Closed/retired by Dec 2025 (rewards redistributed) — weak reception |
| Gleaming Depths raid | Dec 2024 | See above | Called by Bethesda the biggest endgame change; rewards re-scaled to progress in Dec 2025 |
| Bounty hunting | Dec 2025 | Repeatable 10-minute hunts (13 spawn points, 3 most recent excluded); legendary target with a random mutation; a poster item upgrades one into a server-wide public "Head Hunt" | Solo-friendly, opt-in escalation to group content |
| Infestations | Jun 2026 | Factions seize open-world locations; elite boss guarantees a 4-star | Too easy at launch by the devs' own account |
| Hideouts | Planned 2027 | Solo/co-op challenge spaces between events and raids | Acknowledges a missing middle tier |

Pattern: every successful addition is **short, repeatable, soloable-but-better-together, and pays into a
deterministic reward track**. Every failure demanded organised groups, fixed schedules or long chains.

## 13. Seasons, the Atomic Shop and Fallout 1st

### 13.1 Seasons

- **Jun 2020:** free 100-rank "scoreboard" (a board-game track) advanced by S.C.O.R.E. from daily/weekly
  challenges; ranks purchasable for Atoms. Replaced the older challenge system that paid Atoms directly —
  which also quietly cut free premium-currency income.
- **Jun 2022:** Fallout 1st subscribers get bonus scoreboard rewards.
- **Mar 2024 (Season 16):** scoreboard replaced with pages of rewards bought with earned Tickets. More choice,
  but less charm and more of the best items placed behind premium/late pages; contentious at launch.
- **Jun 2026:** Bethesda commits to fewer recoloured filler rewards and more unique items tied to each
  update's content.
- **Sep 2026:** Legacy Seasons — one past season runs alongside the current one, sharing the same ticket
  pool, with already-owned rewards pre-marked. A direct answer to fear-of-missing-out complaints.

### 13.2 Monetisation controversies

| Date | Event | Why it mattered |
|---|---|---|
| Nov–Dec 2018 | Collector's edition shipped a nylon bag instead of the advertised canvas; support-ticket data exposure; premium cosmetics priced near the cost of the discounted game | Destroyed goodwill at the worst moment |
| Apr 2019 | **Repair Kits** sold for Atoms | First non-cosmetic item, contradicting pre-launch "cosmetic only" statements. Bethesda called it a "convenience" |
| 2019 | Scrap kits, refrigerator, resource-collecting robot sold in shop `[UNVERIFIED dates]` | Each a small gameplay advantage; established pay-for-convenience as policy |
| 23 Oct 2019 | **Fallout 1st**: US$12.99/month or US$99.99/year. Private worlds, unlimited scrap box, fast-travel tent with stash, monthly Atoms (1,650 `[UNVERIFIED]`), exclusive cosmetics | Launched weeks before a full-price competitor RPG, on a game still missing its NPC update. Launch bugs: scrap boxes deleting contents, "private" worlds that were not fresh. A fan registered a parody domain; subscribers were harassed in-game |
| 2020–2026 | Lunchboxes, extra camp/loadout slots, paid pets (Radhog 2025, Deathclaw 2026), premium season tiers | Accepted grudgingly; the cosmetic camp catalogue is the tolerated core |

Assessment: the scrap box is the textbook case of **monetising a pain point the designers control**. It is
also, by all community accounts, the reason most subscribers subscribe — which means the stash limit can
never be truly fixed without undercutting revenue. Avoid building that trap.

## 14. PvP

### 14.1 The designs

| System | Rule | Outcome |
|---|---|---|
| Open-world "consent" PvP (launch) | From level 5, shooting another player does token "slap" damage until they shoot back; then full damage, winner takes some caps and dropped junk | Slap damage could still kill weakened players and grief; later removed for pacifists `[UNVERIFIED date]` |
| Wanted system | Kill a non-consenting player or break into locked property -> you are marked Wanted, hidden from seeing others on the map, with a bounty paid **from your own caps** | Clever on paper; in practice bounties became a social toy among friends |
| Pacifist mode | Toggle: you cannot damage players | Became the default state of nearly the whole population |
| Workshops | Claiming a public workshop flags you for PvP by anyone contesting it | The only remaining open-world PvP hook; widely used as a trap by geared players against newcomers, so most players avoid workshops entirely |
| Hunter/Hunted | Opt-in radio queue assassination game | Rarely populated |
| Survival mode (beta, Mar–Oct 2019) | Separate servers, no slap damage, bonus XP, drop items on death, leaderboards | Low population, spawn-camping and exploit builds; shut down in Oct 2019 |
| Nuclear Winter (Jun 2019–Sep 2021) | 52-player battle royale with its own perk deck | Critically the best-received PvP mode, but Bethesda cited matchmaking times and the cost of updating it alongside the main game; "the vast majority of players" preferred other content |

### 14.2 Why PvP failed

1. **Audience mismatch.** The buyers were single-player Fallout fans. They wanted co-op exploration, not
   extraction-shooter tension.
2. **RPG gear variance makes fights non-skill-based.** With legendary effects, mutations, chems and perks the
   time-to-kill between optimised and normal players was near-instant in one direction and near-infinite in
   the other. One-shot stealth builds and unkillable tank builds made duels degenerate.
3. **Duped/legacy gear** poisoned competitive integrity for years.
4. **Netcode and V.A.T.S.** A real-time auto-aim system plus unreliable hit registration is a poor PvP base.
5. **Nothing to win.** No territory persistence, tiny cap stakes, workshop rewards obtainable elsewhere.
6. **Half-measures satisfied nobody.** Consent mechanics removed danger for PvE players without removing
   annoyance, and removed prey for PvP players without giving them an arena.
7. **PvE balance always took priority.** Every balance pass in 2020–2025 was PvE-driven; PvP got damage caps
   and little else.

## 15. Level scaling: One Wasteland (15 Sep 2020)

- Before: zones had fixed level bands (the starting forest ~1–10, the far east 50+). High-level players
  one-shot everything in two-thirds of the map; low-level players could not join friends or high-level events.
- After: each enemy's level is calculated **per player** viewing it, within a regional band — early regions
  cap at 50, late regions at 100 (fallout.wiki). Two players shooting the same creature see different levels
  and deal appropriately scaled damage. Loot and XP scale too. Player power effectively plateaus at 50 because
  SPECIAL gains stop there.
- Shipped with a damage-formula change: stacking bonuses became additive instead of multiplicative.

| Worked | Did not |
|---|---|
| Level 20 and level 800 players fight the same boss together and both matter | The world lost its geography of danger; no more "I'm not ready for that region" |
| The whole map is relevant content forever | Low-level players found themselves facing level-appropriate but *tankier* enemies with bad gear; early game felt harder |
| Removed the need to out-level friends | Removes the power fantasy of returning to stomp old zones (floors mitigate this partially) |

For a multiplayer game with drop-in grouping, per-player scaling was close to mandatory. It is the system
that makes the "friendly veteran helps newbie" culture mechanically possible.

## 16. Economy, duping and trading

- **Currencies:** caps (general; hard wallet cap), legendary scrip (daily-limited), gold bullion (Wastelanders
  faction vendors; daily-limited conversion), Stamps (expeditions), season Tickets, Atoms (premium).
- **Player vending (May 2019):** list items at your camp for caps; a ~10% sales tax acts as a sink
  `[UNVERIFIED rate]`. This works very well for the low-to-mid economy: plans, ammo, serums, chems, common
  legendaries. It gives camps traffic and gives hoarders an outlet.
- **High-end economy broke the cap.** Because wallets max out at 40,000 caps, the best items could not be
  priced in currency. A barter economy emerged using stable consumables and rare apparel as de facto
  currency, organised on third-party Discords/subreddits with reputation ("courier") systems, plus real-money
  trading. A wallet cap intended to limit inflation simply pushed the real market off-platform.
- **Duplication exploits** recurred from the first weeks:
  - Late 2018–early 2019: mass duping of top-roll weapons; vigilante "duper hunting" by players; Bethesda
    purged items from accounts and reported under 1% of players had abused exploits.
  - Jan 2019: players reaching an unfinished developer test cell with unreleased items were banned.
  - 2019–2020: display-case and vending-machine dupes; Bethesda disabled vending and displays server-wide
    until fixed.
  - Legacy explosive energy weapons persisted until removal in early 2023.
- **Anti-dupe by design (2024):** crafted legendary items are character-bound; only loose mods trade. This
  finally cut the link between duping and character power, at the cost of killing the traditional weapon
  trading scene.
- **Inflation of generosity:** endgame players have far more than they can store or spend, so surplus flows
  to newcomers for free (see §17).

## 17. The friendly community as an emergent outcome

Widely reported and acknowledged by the developers, who say they expected players to "all want to kill one
another" and found "the complete opposite" (Bill LaCoste / Jon Rush, via PC Gamer). Todd Howard called it
"the most friendly apocalypse". Veterans wait outside the starting vault to hand new characters stimpaks,
water, ammo and crafted gear; players stock donation containers at train stations; community groups run
free buff/crafting services.

It was not designed as such, but the mechanics explain it:

1. **PvP is opt-in and unrewarding**, so there is no predation incentive and no reason to distrust strangers.
2. **Loot is instanced per player.** Another player at your event never takes anything from you; more players
   only means faster kills.
3. **Per-player level scaling** means helping a newbie is trivially safe and actually effective.
4. **Hard storage and currency caps create structural surplus.** Giving items away is literally the efficient
   way to manage a full stash.
5. **Public Teams and event XP reward proximity without requiring coordination.**
6. **Camps and vending make players hosts.** The dominant social role is shopkeeper/homeowner, not rival.
7. **Emotes over voice.** A limited, mostly positive emote wheel is the default communication channel.
8. **Selection effect.** After the launch disaster and the removal of PvP modes, the players who stayed were
   those who liked the co-op/roleplay loop; the culture then self-perpetuated and became part of the game's
   reputation, which attracted more of the same.
9. **Shared siege mentality.** Staying with a mocked game produced unusual in-group solidarity.

## 18. The launch disaster in mechanical terms

| Problem | Detail |
|---|---|
| Stability | Frequent server disconnects and crashes; quest progress loss; the beta launcher bug that deleted the ~50 GB client; a launch-window console patch of ~48 GB |
| Engine fit | Single-player Creation Engine retrofitted with netcode: physics/animation tied to framerate (speed-hack exploits on PC), poor hit registration, enemies T-posing or desyncing, no FOV/ultrawide/push-to-talk options on PC |
| Emptiness | No living NPCs; story delivered via holotapes and terminals; quests ended at corpses. 24 players could not populate the map |
| Friction stacked on friction | 400 lb stash, hunger/thirst penalties, durability, carry weight, caps cost to fast travel and move camp, random camp displacement |
| Endgame | One world boss, nuke loop, and RNG legendaries; exhausted in ~50–80 hours |
| Exploits | Item duplication within weeks; out-of-bounds dev room; damage and carry-weight overflows |
| Balance | TSE weapons trivialising all content; then heavy-handed nerfs |
| Trust | Canvas-bag substitution, support data leak, refund disputes, rapid price cuts, then repair kits and Fallout 1st |
| Reception | Lowest-reviewed mainline Bethesda Game Studios release; aggregate scores around 50/100 `[UNVERIFIED exact]` |

### What specifically produced the redemption arc

Ranked by impact (my assessment, consistent with retrospectives and community consensus):

1. **Wastelanders (Apr 2020)** — human NPCs, dialogue with skill checks, two factions with reputation,
   companions. Fixed "empty". Coincided with the Steam release and a ~33k Steam concurrent peak (May 2020).
2. **One Wasteland (Sep 2020)** — fixed "can't play with friends" and "70% of the map is trivial".
3. **Friction removal** — stash to 1,200; hunger/thirst penalties removed; free camp moves; loadouts; loot
   sharing; shared team XP; legendary determinism (2024).
4. **Cadence** — a predictable quarterly update + season rhythm from mid-2020, with a public test server.
5. **Short-session content** — Daily Ops, public event rotation, expeditions.
6. **Dropping what did not work** — Survival, Nuclear Winter, Vault 94, human-less storytelling.
7. **Map growth and novelty late in life** — Skyline Valley (2024), playable ghouls (2025), fishing (2025),
   Burning Springs (Dec 2025).
8. **External luck** — Game Pass exposure and the TV series.

Not fixed: engine jank, inventory management as a core activity, and pay-for-convenience.

## 19. Player numbers

| Point | Figure | Source quality |
|---|---|---|
| Pre-show baseline (early 2024) | ~5–6k average, ~13k three-month best on Steam | Press citing SteamDB |
| Previous Steam record | 32,982 (May 2020, free weekend after Steam release) | Press citing SteamDB |
| 14 Apr 2024 | 39,455 Steam concurrent (new record, four days after the series premiered) | Multiple outlets |
| ~21 Apr 2024 | **~73,368** Steam concurrent, all-time peak | SteamDB/Steambase; date reported as 21 or 24 Apr `[DISPUTED date]` |
| Apr 2024 | **1 million players in a single day** across all platforms; ~5 million across the franchise | Bethesda statement, widely reported |
| Lifetime players | 20+ million announced mid-2024 `[UNVERIFIED]` | From memory; not re-confirmed |
| Jan–Feb 2026 (after show Season 2, 16–17 Dec 2025, and Burning Springs) | ~17.4k–17.7k *average* concurrent on Steam | Steambase monthly table |
| Mar / Apr / May / Jun 2026 | ~12.4k / 8.0k / 6.0k / 6.9k average | Steambase (other trackers differ slightly) |

Steam is a minority of the audience (console and Game Pass are not public), so treat these as shape, not
size. The shape: a transmedia event produced a ~10x spike in 2024 and a ~3x spike in 2025–26, each decaying
toward a slowly rising baseline. The game was in a state to *retain* a meaningful share only because the
2020–2024 fixes had already landed, and because veterans onboarded the influx.

## 20. Balance assessment

**Strengths**

- The SPECIAL-as-slot-budget card system is the most legible build system in the series and respec is now
  nearly free. Experimentation is encouraged.
- Per-player scaling plus instanced loot plus public teams makes cooperation frictionless and non-zero-sum.
- Camp building is a deep, expressive, social and monetisable pillar with no real competitor in the genre.
- The 2024–2025 rebalance genuinely widened viable weapons; conditional perks are more interesting than the
  flat cards they replaced.
- Deterministic legendary crafting gives long-term goals without lottery despair.

**Weaknesses**

- **Power ceiling vs content floor.** Optimised characters delete world bosses in seconds; new events are
  cleared "in about a minute" (devs on Infestations, 2026). Difficulty is added mainly as health/resistance,
  and scaling means there is no content that is hard *because of where it is*.
- **Mutations and legendary SPECIAL perks are non-choices.** Universal picks are balance debt.
- **Years of low-health dominance** shows what happens when a risk mechanic is paired with tools that remove
  the risk.
- **V.A.T.S.** was either dominant or (post-2025) resented; the game never found a comfortable middle.
- **Daily caps everywhere** (caps, scrip, bullion, challenges) substitute appointment mechanics for economy
  design.
- **Inventory and weight management** remain the largest time sink, and its relief valve is paywalled.
- **Survival identity is gone.** With hunger/thirst as buffs, scaling, free fast travel and abundant loot,
  the game is a cosy looter-builder in post-apocalyptic dress. That is what the audience chose — but it means
  the "survival" pitch was abandoned rather than solved.
- **Balance by multi-year rebuild** is costly: each phase invalidated builds and gear players had ground for.

## 21. What the multiplayer experiment proved

| Proved to work | Proved not to work |
|---|---|
| A Bethesda-style open world is enjoyable with other people present *as ambient co-inhabitants* | Players as a replacement for authored NPCs and story |
| Drop-in, no-obligation grouping (public teams, map-wide events with free travel) | Organised-group requirements without matchmaking (Vault 94) |
| Player housing in the open world, visible and visitable, with shops | Capturable territory in a non-persistent world (workshops) |
| Player-triggered server-wide events (nukes, keycard bosses, premium bounty posters) | Puzzle gates that the internet solves once for everyone (nuke ciphers) |
| Per-player scaling and instanced loot for mixed-level play | Fixed level zones in a shared world |
| Opt-in buffs for survival upkeep | Survival upkeep as a penalty in a long-session online game |
| Deterministic reward shops and craftable targets | Pure-RNG legendary drops as the endgame |
| Cosmetic and housing monetisation | Selling relief from designed inconvenience; breaking a stated "cosmetic only" line |
| A cooperative culture when the rules make others non-threatening and surplus easy to give | Bolting PvP onto a gear-driven PvE RPG; consent-toggle half-measures; a battle royale side mode with a separate player base |
| Long-tail recovery through steady friction removal | Shipping a live game on single-player tech without soak-testing at scale |

## Design Takeaways

For our own (original) post-apocalyptic game:

1. **Decide whether other humans are threat or company, then build every system to match.** Fallout 76's
   friendliness came from instanced loot, per-player scaling, opt-in PvP and structural surplus. If we want
   tension between players, each of those must be designed the other way, deliberately — not half-way.
2. **Never use players as a substitute for authored characters.** If we go multiplayer, ship with NPCs,
   dialogue and factions on day one. Other players add colour; they do not carry narrative.
3. **Survival upkeep should grant advantages, not avert penalties**, unless scarcity is the core fantasy *and*
   sessions are short. If we want real scarcity, make it a mode or a region, not a universal tax.
4. **Do not ship flat "+X% damage with weapon class" perks.** They are a slot tax disguised as a choice.
   Perks should change behaviour (conditions, stacks, area, bounce), not raw multipliers.
5. **Separate utility perks from combat perks** (different slots or automatic context-switching) so nobody
   shuffles cards to pick a lock.
6. **Make respec free early.** Fallout 76's builds only became fun once swapping cost nothing.
7. **Risk mechanics need un-removable risk.** If a low-health build can also stack dodge, damage reduction
   and auto-revive, it is simply the best build. Cap how many mitigations a risk state can combine with.
8. **Mutation-style trade-offs must keep their downsides.** Do not ship a perk that shrinks every penalty by
   75%; do not let one package be universal. Consider mutually exclusive mutation families.
9. **RNG on unlocks, determinism on outcomes.** Let players learn a modifier through play, then craft it on
   demand. Budget unlock rates so a target build takes weeks, not years.
10. **Player bases should be visible, visitable and useful to strangers.** Map markers, fast travel, shops and
    a rating/showcase loop turned building from a solo hobby into the social core. Design placement rules
    permissively from the start; players will glitch past restrictive ones anyway.
11. **Storage limits must be justified in-fiction and by gameplay, and never monetised.** If our loop says
    "scavenge everything", storage for crafting components should be generous or abstracted. Selling the cure
    for a designed pain permanently corrupts the incentive to fix it.
12. **Avoid hard wallet caps.** They do not stop inflation; they move the real economy to barter and
    off-platform markets. Use sinks instead.
13. **Assume duplication exploits will happen.** Server-authoritative inventories, item provenance IDs and the
    ability to bind or invalidate crafted power items should exist before launch, not six years in.
14. **Scaling: prefer banded per-player scaling with strong floors**, so regions keep an identity of danger
    but friends at different levels can still play together. Keep a few zones genuinely unscaled as
    aspirational threats.
15. **Player-triggered world events are a great endgame verb** (one player's effort becomes everyone's
    content). Gate them with effort and resources, not with a global puzzle that is solved once on a wiki.
16. **Build a missing-middle tier on purpose:** short solo activity -> open event -> small-group challenge ->
    raid. Fallout 76 only planned its "hideouts" tier in year nine.
17. **If PvP exists, isolate its power curve** (normalised gear, bounded time-to-kill) and give it something
    persistent to fight over. Otherwise leave it out; a neglected PvP mode costs trust and dev time.
18. **Real-time assisted aiming is worth having for accessibility**, but give it an accuracy model and resource
    cost that keep manual aim competitive from the start, so it never needs a late nerf.
19. **Launch quality is not recoverable by marketing.** Fallout 76 needed ~18 months and its two largest
    updates to become what it should have been. A smaller, stable, complete launch beats a large broken one.
20. **Avoid fear-of-missing-out as the retention engine.** The 2026 Legacy Seasons and the devs' stated wish to
    avoid FOMO are corrections to a self-inflicted problem; make seasonal rewards re-earnable from day one.
21. **Ration daily caps.** One or two appointment mechanics are fine; a wallet of six daily-limited currencies
    reads as a job.
22. **Plan for transmedia or viral spikes.** A sudden 10x influx only converts if onboarding is smooth and the
    existing community is positively disposed to newcomers — which is itself a product of the rules.

## Sources

Official (Bethesda):

- https://bethesda.net/en-US/news/fallout-76-infestations-release-notes
- https://fallout.bethesda.net/en-NZ/news/fallout-76-milepost-zero-release-notes
- https://fallout.bethesda.net/en-AU/news/fallout-76-the-gleaming-depths-release-notes
- https://fallout.bethesda.net/en-AU/news/inside-the-vault-upcoming-combat-and-perk-changes
- https://fallout.bethesda.net/en-AU/news/fallout-76-c-a-m-p-revamp-release-notes (via search summary)
- https://fallout.bethesda.net/en-US/news/fallout-76-inside-the-vault-steel-dawn-update-highlights (via search summary)
- https://fallout.bethesda.net/en-AU/news/fallout-76-patch-notes-february-19-2019 (via search summary)

Wikis and planners:

- https://fallout.wiki/wiki/One_Wasteland_For_All
- https://www.falloutbuilds.com/fo76/updates/
- https://www.falloutbuilds.com/fo76/updates/burning-springs/
- https://www.falloutbuilds.com/fo76/updates/the-slasher/
- https://www.falloutbuilds.com/fo76/mutations/
- https://nukesdragons.com/fallout-76/character
- https://fallout.fandom.com/wiki/Burning_Springs_(update) (search summary only; page fetch blocked)
- https://fallout.fandom.com/wiki/Fallout_76_legendary_perks (search summary only; page fetch blocked)
- https://nukaknights.com/articles/raid-gleaming-depths-guide-and-rewards.html (via search summary)

Press, interviews and retrospectives:

- https://finalweapon.net/2026/06/17/interview-fallout-76-devs-on-infestations-update-potential-switch-2-support-and-whats-coming-next-in-2026/
- https://gaminghq.eu/2026/10/04/fallout-76-roadmap-raven-rock-expansion-2027/
- https://www.pcgamer.com/games/fallout/fallout-76-devs-were-surprised-the-community-turned-out-to-be-so-friendly-its-post-apocalyptic-its-fallout-theyre-going-to-all-want-to-kill-one-another-its-the-complete-opposite
- https://www.pcgamer.com/amp/todd-howard-there-was-very-little-we-didnt-screw-up-on-fallout-76-launch/
- https://www.pcgamer.com/games/rpg/fallout-76-hits-an-all-time-player-count-record-on-steam-following-the-fallout-tv-series-on-amazon-and-the-other-games-are-spiking-too
- https://www.pcgamer.com/fallout-76-fans-are-unhappy-that-bethesda-is-adding-pay-to-win-items
- https://www.pcgamer.com/player-claims-fallout-1st-domain-to-protest-fallout-76s-subscription
- https://www.pcgamer.com/fallout-76-duped-items-are-being-removed-from-inventories
- https://www.pcgamer.com/fallout-76-testing-stash-size-increases-and-better-pip-boy-sorting
- https://www.thegamer.com/fallout-76-repair-kit-fiasco-explained/
- https://www.gamesradar.com/bethesda-defends-fallouts-76s-paid-for-repair-kits-its-simply-just-a-strict-convenience-thing
- https://bit-tech.net/news/bethesda-raises-hackles-with-100-a-year-fallout-1st-subscription/1
- https://kotaku.com/fallout-76-players-are-punishing-people-they-suspect-of-1831775419
- https://gamedeveloper.com/business/fallout-76-hits-1-million-players-in-a-day-brings-overall-series-to-near-5-million-players
- https://www.windowscentral.com/gaming/the-fallout-revival-continues-as-nearly-5-million-players-have-journeyed-into-the-wasteland-in-a-single-day
- https://videogameschronicle.com/news/fallout-76-beats-its-all-time-concurrent-player-count-again-on-steam
- https://steambase.io/apps/fallout-76 (monthly Steam averages, 2026)
- https://www.neowin.net/news/fallout-76s-battle-royale-mode-is-being-shut-down-in-september/
- https://egmnow.com/fallout-76s-nuclear-winter-battle-royale-mode-is-being-removed/
- https://www.gamepro.de/artikel/fallout-76-survival-modus,3349452.html
- https://comicbook.com/gaming/news/fallout-76-vault-94-shut-down
- https://www.rpgsite.net/news/8061-fallout-76s-first-december-patch-increases-stash-storage-limit-by-50-two-more-updates-on-the-way
- https://www.rpgsite.net/news/10703-fallout-76s-inventory-update-increases-player-stash-added-pip-boy-functions-and-more
- https://www.pcgamesn.com/fallout-76/fallout-76-perk-card-system-details
- https://www.gamerevolution.com/news/659379-fallout-76-one-wasteland-update-low-level-scaling
- https://mp1st.com/title-updates-and-patches/fallout-76-new-update-2-29-brings-the-slasher-current-gen-upgrade-september-15
- https://massivelyop.com/2026/08/20/fallout-76-is-launching-the-slasher-and-legacy-seasons-on-september-15/
- https://www.pcgamer.com/games/fallout/fallout-76s-burning-springs-draws-its-main-influences-from-fallout-3-and-fallout-new-vegas-as-players-venture-to-a-whole-new-state-ohio
- https://insider-gaming.com/fallout-76-camp-revamp-update-notes-new-season-22-revealed/
- https://www.windowscentral.com/gaming/xbox/fallout-76-ghoul-within-update-live
- https://mein-mmo.de/en/fallout-76-list-of-all-legendary-perks-how-to-obtain-and-upgrade-them,580197

Community (Reddit r/fo76 mirrors and Steam discussions, used for consensus/sentiment only):

- https://steamcommunity.com/app/1151340/discussions/ (multiple threads on V.A.T.S. nerfs, bloodied changes, level scaling)
- r/fo76 Bethesda community-manager patch-note threads (Milepost Zero, Oct 2024, Jan 2025)

Research limitations: fallout.wiki's update index and several Fandom pages refused automated fetches, and the
session's web-search quota ran out before I could re-confirm some launch-era numbers, lifetime player totals,
legendary-crafting unlock percentages, and scrip/bullion limits. Those are the `[UNVERIFIED]` tags above.
