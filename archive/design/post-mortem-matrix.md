# The Post-Mortem Matrix

What makes a post-apocalyptic RPG work, and what we will never repeat. This is the acceptance checklist that
every later design decision is audited against. Version 1, 10 Nov 2026, built from `research/` as it stood on
that date (39 documents). Fallout is evidence only. Nothing here permits reusing its names, factions, art,
music or text.

---

## 1. How to read this

- **IDs are the interface.** `MH-xx` = must-have, `NDA-xx` = never do again, `CM-xx` = contested question.
  Later design docs cite these IDs. A review comment reads "fails MH-11" or "risks NDA-06", not "feels off".
- **Passing an audit** means: every MH audit question has a "yes" backed by a pointer into our spec, and no NDA
  pattern appears without a written, signed waiver that says which evidence we think does not apply to us.
- **Evidence** names the research file (paths relative to `research/`) and the specific fact, with source
  confidence tags carried over unchanged (`[UNVERIFIED]`, `[DISPUTED]`, `[SNIPPET]`, `[C]` = derived estimate).
  Quotes are reproduced exactly as the research file gives them.
- **Section 4** is where we take positions on questions the evidence does not settle. **Section 6** says what is
  cheap and what is expensive. **Section 7** lists the soft spots: claims a decision here depends on that are
  not yet verified.
- `design-insights/designer-lessons.md` was being rewritten while this was compiled and is not cited. Tim Cain
  and Josh Sawyer positions are taken from `gameplay/design-principles.md`, the per-game files and
  `design-insights/sawyer-new-vegas-design.md`.

### Thesis

The evidence supports one through-line: **an RPG in a ruined world is remembered for how visibly the world
records the specific character the player chose to be.** Critics reward launch polish and breadth (FO3 scored
91 on PC, FO76 scored 52). Long-term esteem follows reactivity, which is why New Vegas went from 84 at launch
to first place in every fan poll, and why Fallout 1 and 2 still sit at about 94-95% positive on Steam
(`gameplay/systems-comparison.md`, `reception/fallout-new-vegas.md`, `reception/fallout-1-and-2.md`). Every
lasting failure in the series is a case where one system was allowed to stop the world from noticing the
player. A voiced protagonist capped the lines, which capped the options and removed the checks. "No lock-outs"
removed the level cap, which made builds converge and forced enemy scaling. Radiant generation replaced
authored quests. A global karma number flattened dilemmas. An empty map removed the people who could notice
anything at all (`gameplay/design-principles.md` §6 sets out these causal chains). Bugs, the other big
complaint, fade: the community patched every game. Structural reactivity cannot be patched in later ("Fixable
flaws fade, structural strengths compound", `reception/fallout-new-vegas.md`). The cheapest way to get it is
also the best fit for a small team: text-first, legible consequences in a compact world, scarcity defended by
systems rather than a toggle, and a stable launch. In `design-insights/production-metrics.md` New Vegas
matched Fallout 4's PC score with about 30% of the labour `[C]`. That is the niche large studios have left
empty, and it is where we build.

---

## 2. MUST-HAVES

34 items in 12 groups. Each one has a rule (testable), why (the mechanism), evidence, and an audit question.

### World & exploration

**MH-01 · Density over area**
- *Rule:* On a critical-path traversal on foot, the player reaches a new authored point of interest at least
  every 2 minutes. Before anything is built, each location has a written one-line answer to "what happened
  here?"
- *Why:* How often the player finds something new drives the exploration loop. Short gaps keep the "one more
  marker" pull going and make the map read as places rather than distance.
- *Evidence:* FO3 fits "well over a hundred named places in about three square miles", which is "something new
  roughly every one to two minutes of walking". The UESP cell count gives about 3.3 sq mi; the popular "16 square
  miles" figure is `[DISPUTED]` (`gameplay/fallout-3.md` §13). The world was FO3's most praised feature and
  "worth a 93 Metacritic on its own" (`reception/fallout-3.md`). Bethesda claimed FO76's map was four times FO4's,
  and at launch GameSpot called it "little more than just an environmental exhibit with things to kill"
  (`art/art-direction.md` §5.2). "Space is cheap to generate and expensive to make meaningful"
  (`design-insights/production-metrics.md` §9).
- *Audit:* What is the measured median walking time between new points of interest on the critical path? Does
  every location have its one-liner?

**MH-02 · Danger is geography, and it is signposted**
- *Rule:* Enemy strength is fixed per region. Level bands within a region are allowed; global scaling is banned.
  Every lethal zone next to a safe route can be read before contact (corpses, warnings from locals, signs,
  creature sound). At least three landmarks are visible from any outdoor point.
- *Why:* Fixed danger turns the map into a progression system and a memory. It teaches players to read the
  world and lets skilled players break sequence by choice instead of being walled in.
- *Evidence:* NV's deathclaws at Quarry Junction and the "monster badlands" north of Goodsprings were deliberate.
  Players who "attempted to bulldoze their way through" mostly failed, but nothing blocked them (Sawyer, 19 Aug
  2011, `design-insights/sawyer-new-vegas-design.md`). "Fixed worlds create memories". FO4's zone bands are "the
  best compromise in the series". "Difficulty-as-HP-multiplier is universally the least liked option"
  (`gameplay/systems-comparison.md` §18). The three-landmark rule is from the Sawyer file (takeaway 12).
- *Audit:* Can a new player tell which direction is dangerous from the starting town without a UI warning?

**MH-03 · The time since the collapse is fixed, and every settlement shows how it lives**
- *Rule:* The setting bible fixes the number of years since the catastrophe and derives a table of what has
  rotted, regrown, been looted, cleaned or rebuilt. Every settlement visibly answers five questions: where is the
  water, where is the food, what do they trade, who protects them, why here.
- *Why:* Players accept bleakness but reject implausibility. A visible economy makes the stakes of scarcity
  legible and gives factions a material basis.
- *Evidence:* FO3's long-tail critique: set 200 years on, it "looks like it is 20 years after"; there are no farms
  or trade that could feed the towns. This is ranked the #2 long-term complaint (Shamus Young, NMA, RPG Codex, via
  `reception/fallout-3.md`). NV answered "what do they eat?" with visible farms and trade routes
  (`gameplay/systems-comparison.md` §14). The five questions come from `lore/games/fallout-3.md`. Real rewilding
  timelines: roofs and gutters fail first, pioneer trees colonise cracks within 5-20 years
  (`art/visual-reference-catalogue.md`).
- *Audit:* For each settlement, point to the asset (field, caravan, well, wall, guard post) that answers each of
  the five questions.

**MH-04 · Environmental story runs alongside living stakes, never instead of them**
- *Rule:* Every location carries a found story (props, logs, tableaux), with the consequence at the door and the
  cause in the last room. No main-path stake is carried only by records of the dead. Every main-path quest has a
  living character who wants something and can be persuaded, refused or killed.
- *Why:* Found stories work for any build, in any order, and cannot fail, so they are cheap. Living characters
  supply consequence. One channel without the other fails.
- *Evidence:* Environmental vignettes are FO3's and FO4's best-reviewed narrative channel. In FO4 they are
  "immune to dialogue-system weaknesses" (`lore/games/fallout-4.md`). FO76's launch story was told entirely
  through holotapes, which made "every quest end at a corpse" (`lore/games/fallout-76.md`); PC World called them
  "no substitute for an actual conversation" (`audio/sound-design-and-voice.md`). On combining the two
  approaches: "no game in the series has fully combined them" (`gameplay/design-principles.md`).
- *Audit:* List the main-path quests whose key information exists only in recordings. Target: zero.

### Quests & consequence

**MH-05 · Two of three on every quest, all three on the main path**
- *Rule:* Every quest with a quest-giver supports at least two of fight / talk / sneak (or a tech route). Every
  main-path quest supports all three. The final confrontation has a non-combat resolution earned with evidence
  the player had to find, not with a stat number alone.
- *Why:* Multiple routes make build choices matter and make replays different. Gating the talk-down on evidence
  rewards curiosity rather than min-maxing.
- *Evidence:* Cain's vision-document rule is that every major quest supports at least two of fight / talk /
  sneak and the main quest can be finished by any build (`gameplay/design-principles.md`,
  `gameplay/fallout-1.md`). FO1's final boss can be argued into destroying himself (IN 7, high Speech, one piece of
  evidence). This is "the single most-praised moment in either game"; FO2's fight-only finale "is remembered as a
  step down" (`reception/fallout-1-and-2.md`). FNV lets both possible final opponents be talked down. FO3/FO4:
  "Combat default" (`gameplay/systems-comparison.md` §15).
- *Audit:* In the quest table with F/T/S columns, does any main-path row have an empty cell?

**MH-06 · A web, not a list**
- *Rule:* Every hub has at least one quest whose outcome changes a quest, price, population or ending slide in a
  different hub. Each minor faction's arc is read three times: by its employer, by the finale, by the epilogue.
- *Why:* Cross-references are how a world appears to remember. They multiply the value of each authored quest
  without new assets.
- *Evidence:* FO2: Vault City, Gecko, NCR, New Reno and Redding each have endings decided by quests done in the
  other towns. It is "the highest value-per-cost feature in this game", and "Five towns with ten shared flags beat
  fifteen isolated towns" (`gameplay/fallout-2.md`). NV's minor factions as modular stories read three times are
  "the cheapest high-reactivity structure in the genre" (`lore/games/fallout-new-vegas.md`). Causal chain #1 in
  `gameplay/design-principles.md` §6: a seamless world that can be visited in any order pushes design toward
  sealed locations and low reactivity. NV escaped this by shaping its map into a soft loop.
- *Audit:* Draw the flag graph. Does any hub lack an outbound edge?

**MH-07 · Per-community ending slides, every branch tested**
- *Rule:* The ending reports an outcome for every settlement, faction and companion, including a "you neglected
  it" variant. Every slide trigger has an automated reachability test.
- *Why:* Slides turn hundreds of flags into a felt verdict. They are the main reason players believe their choices
  mattered. Making neglect visible turns inaction into a choice.
- *Evidence:* FNV has 28 state-driven slides (`lore/games/fallout-new-vegas.md`) and is "the gold standard".
  "The cinematic endings of FO3 and FO4 cost more and say less" (`gameplay/systems-comparison.md` §16). FO4 has
  "only two cutscenes" (`lore/games/fallout-4.md`). FO1 shipped several good endings unreachable or bugged, and its
  Junktown endings were inverted late (`lore/games/fallout-1.md`).
- *Audit:* Count communities x variants. Is the CI reachability run green?

**MH-08 · Anyone can die; one route cannot**
- *Rule:* Every visible adult NPC is killable. The critical path has one fail-safe route to an ending, and that
  route costs the player something. The game tells the player when they have locked out content. Unique loot is
  never gated behind murder.
- *Why:* Protecting NPCs tells players their agency is decorative. A fail-safe plus lockout notices keeps both
  freedom and completability.
- *Evidence:* Sawyer's kill policy: any visible non-child NPC can be killed without blocking the critical path
  (27 Nov 2010, 9 Dec 2012). Failed-quest messages are shown on purpose (18 Oct 2012). The main quest falls
  through to Yes Man (`design-insights/sawyer-new-vegas-design.md`). Kill-everyone runs work in FO1, FO2 and FNV.
  They are blocked in FO3 and FO4 by essential NPCs (`gameplay/systems-comparison.md` §15). Caveat: the
  faction-free route lets players finish "without getting your hands dirty" (`lore/universe/factions.md`), so the
  fail-safe must cost something.
- *Audit:* Does an automated kill-everyone run reach an ending?

**MH-09 · The world talks back cheaply**
- *Rule:* An in-world broadcaster (radio, crier, newssheet, graffiti) has a before, an after and a failed line for
  every major quest, and reacts to reputation. Tie it to a mechanical unlock or a failure state (reach, a
  replacement host).
- *Why:* A few variant lines make the whole world appear to notice the player. It is the cheapest global
  reactivity channel.
- *Evidence:* Radio New Vegas has 50 news stories, 42 of which depend on quest progress
  (`audio/ambient-radio-pacing-and-foley.md`). Three Dog addresses the player by Karma title, and Travis's
  confidence arc is told in audio alone. Both DJs are among the best-loved NPCs "because they react"
  (`audio/licensed-music-and-radio.md`). FO3's GNR dish quest turns the station's reach into a reward.
- *Audit:* Does every major quest have its three broadcast variants written?

### Dialogue & role-playing

**MH-10 · Show the line; let the content set the option count**
- *Rule:* Before committing, the player sees the exact words, or a specific, faithful paraphrase of their content,
  never a tone label. The number of options varies by node. Every quest hook has a real refusal, a conditional
  accept and a hostile reply, each with different consequences. A lint rule flags any two options that lead to
  identical replies.
- *Why:* The player authors the character through the words. Hiding them turns conversation into gambling and
  removes ownership.
- *Evidence:* FO4 shipped four prompts of one to three words, one per face button. Full Dialogue Interface
  appeared on 18 Nov 2015, eight days after launch. XDI exists only to remove the "hardcoded 4-option limit"
  (`community/mods-as-design-feedback.md` §4.2.1). Howard, 2016: "Obviously the way we did some dialogue stuff,
  that didn't work as well." FO76 Wastelanders (2020) and Starfield (2023) went back to full-text lists
  (`design-insights/bethesda-dialogue-postmortems.md`).
- *Audit:* Does any node have a label-only option, or two options with the same reply?

**MH-11 · Deterministic, visible thresholds across every skill and stat**
- *Rule:* Dialogue and world checks use fixed thresholds, displayed with the requirement and the player's current
  value. Every skill and every stat gates options somewhere. A failed check has its own authored line and never
  leaves the player worse off than before. At least one in five skill-tagged options is costly, wrong for the
  situation, or merely different, rather than best.
- *Why:* Deterministic checks reward investment and end reload loops. Visible requirements tell players the game
  sees their build. Tags that are not always best keep role-playing a choice rather than a lookup.
- *Evidence:* Sawyer: random checks "just lead to save-scumming" (27 Jul 2011); "I didn't like the
  randomization and the save scumming that resulted" (`gameplay/systems-comparison.md` §10). FNV's checks use all
  13 skills (`gameplay/fallout-new-vegas.md`). Sawyer's own later correction is that a visible unlocked option
  implies "you should pick it" (GDC 2012 "Choice Conflict"; GDS Prague 2024; `design-insights/sawyer-new-vegas-design.md`).
  FO4 reduced checks to Charisma-only colour-coded rolls (`design-insights/bethesda-dialogue-postmortems.md` §4.1).
- *Audit:* In the tool-generated check-distribution table, does any skill or stat have zero dialogue uses? What
  share of tagged options are non-optimal?

**MH-12 · An unvoiced, player-authored protagonist whose premise survives a selfish player**
- *Rule:* The player character is unvoiced. They have no fixed family, profession or motive beyond what character
  creation sets. The main-quest hook works for a cruel or indifferent character, either through an alternative
  motive or through a premise that tolerates any motive.
- *Why:* Role-play means the player supplies the voice. A hook the player cannot refuse internally turns the game
  into someone else's story.
- *Evidence:* Pagliarulo on the dropped Starfield voiced lead: "this guy is too specific" (2023). Howard: "Players
  want to role-play more and we had a voiced protagonist." Bethesda, 13 Jun 2022: "your character does not have a
  voice" (`design-insights/bethesda-dialogue-postmortems.md`). FO4's alternate-start mods include Another Life
  (104,757 unique downloads, `[SNIPPET]`) (`community/mods-as-design-feedback.md`). "A personal main quest must
  still work for a selfish or cruel protagonist" (`lore/games/fallout-3.md`). NV's small revenge hook hands over a
  large political question (`lore/games/fallout-new-vegas.md`).
- *Audit:* Read the first hour as a selfish character. Does any line assume a motive the player did not choose?

**MH-13 · One extreme stat rewrites the game's voice**
- *Rule:* Pick one character-sheet extreme (the classic case is very low intellect). Write an alternate dialogue
  register for every main-path conversation, with NPC reactions. Budget it in pre-production and do it for one
  stat only.
- *Why:* It is the strongest possible signal that the character sheet matters, and it creates a distinct replay.
- *Evidence:* In FO1, Intelligence below 4 replaces dialogue with grunts and closes most quests
  (`gameplay/fallout-1.md`). FO2 expanded it: "players will cite it for decades. Do not try to do it for every
  stat" (`gameplay/fallout-2.md`). It "is also expensive, which is why it vanished". NV has only "a handful of
  lines" (`gameplay/systems-comparison.md` §10, §15).
- *Audit:* What share of main-path nodes has alternate-register lines? Target: 100%.

### Character systems & progression

**MH-14 · A hard power budget**
- *Rule:* The level cap is fixed in pre-production and never raised by DLC. At the cap, a character can master
  roughly a third of the skill list. Collectible stat and skill boosts are scarce. Capstone perks deepen a
  specialisation and never erase trade-offs.
- *Why:* Scarce power is what makes builds distinct. Convergence turns every playthrough into the same character
  and then forces enemy scaling to keep fights relevant.
- *Evidence:* In FO3, a level-30 character can have 100 in every skill and 9-10 in every stat. "Builds stop
  mattering around level 15-20". Almost Perfect sets every SPECIAL to 9 (`gameplay/fallout-3.md`). In FO4
  everything can be maxed at level 272 (286 with DLC) (`gameplay/fallout-4.md`). NV's DLC cap raises are "widely
  seen, including by Sawyer, as breaking late-game balance", and his mod cuts the cap from 30 to 15 (35 with DLC)
  (`gameplay/fallout-new-vegas.md`). Causal chain #2: no lock-outs, then no cap, then convergence, then scaling
  (`gameplay/design-principles.md` §6).
- *Audit:* In the progression spreadsheet, is skill points at cap divided by points needed to max every skill
  about 0.33?

**MH-15 · No dump stat**
- *Rule:* Every primary stat is read by at least two systems, one of them non-combat, and offers something
  nothing else provides. No stat multiplies XP or skill points.
- *Why:* A stat players can safely ignore breaks the promise that builds matter. A stat that multiplies
  progression becomes mandatory.
- *Evidence:* FO1's Charisma is the dump stat; CH 1 is viable (`gameplay/fallout-1.md`). Sawyer: if players call a
  stat a dump stat, "you probably screwed up" (13 Dec 2011, `design-insights/sawyer-new-vegas-design.md`). FO2's
  party size of Charisma/2 "turned Charisma from a dump stat into a real choice" (`gameplay/fallout-2.md`). NV
  caps implant count by Endurance, a one-line hook between systems (`gameplay/fallout-new-vegas.md`).
- *Audit:* Does every row of the stat x system matrix have two or more entries? What do playtesters answer to
  "which stat did you dump?"

**MH-16 · Rule-changing perks at a slow cadence; traits with real costs**
- *Rule:* A perk every 2-3 levels. Every perk adds a verb, a rule exception, information or a trade-off. No flat
  "+X% damage with class Y" perks. Each creation-time trait pairs an upside with a downside, and at least two
  thirds of traits see real use in playtests.
- *Why:* Rare, rule-changing choices are what players describe when they describe a build. Flat percentages are
  mandatory taxes.
- *Evidence:* Perk cadence is "the single best predictor of build identity" (`gameplay/systems-comparison.md`).
  FO1's best early perk "does nothing but show enemy HP" (`gameplay/fallout-1.md`). FO76's flat damage perks are
  "a slot tax disguised as a choice", and Bethesda spent 2024-2025 on a combat rebalance to break the "three
  mandatory damage cards" pattern (`gameplay/fallout-76.md`). FO1's Gifted is the near-universal best trait.
- *Audit:* Tag every perk as verb / exception / information / trade-off. Any perk that is only "+%" fails.

**MH-17 · Every skill earns its place, and the opening proves it**
- *Rule:* About 10-12 skills at most. A skill x hub content matrix with at least five uses per skill per hub,
  tracked by a tool and reviewed every milestone. The first settlement pays off every taggable skill and contains
  a multi-solution quest. Tutorials are skippable on replay.
- *Why:* A skill without content is a trap for the player who chose it. Front-loading checks teaches in the first
  hour that the game is paying attention to the build.
- *Evidence:* Roughly half of FO1's 18 skills are skippable (`gameplay/fallout-1.md`). Obsidian tracked check
  distribution with an internal tool and front-loaded checks; Goodsprings was built so every tagged skill pays off
  (`design-insights/sawyer-new-vegas-design.md`, `gameplay/systems-comparison.md` §10). FO2's Temple of Trials
  forces spear and unarmed combat on every build and is "the most disliked part of the game"
  (`gameplay/fallout-2.md`). FO1's second town has a hostage rescue with five solutions that teaches the whole
  game (`lore/games/fallout-1.md`).
- *Audit:* Is the minimum cell in the matrix at least 5? Does every skill have a use in the opening hub?

### Combat

**MH-18 · Fix the combat model first; show the build in every fight; make combat good on its own**
- *Rule:* The combat model is fixed before the stat system. Every stat and skill has a visible combat effect
  (numbers shown, not hidden multipliers). Combat is enjoyable without any assist mode: speed controls and batched
  enemy turns if it is turn-based, solid feedback (hit markers, recoil, reload control) if it is real-time.
- *Why:* The series' worst-received features are layers built for a different game than the layers next to them.
  Stats that only do what the player's hands already do are cosmetic.
- *Evidence:* "Do not ship a real-time shooter whose stats only do what the player's hands already do (FO4)".
  Turn-based combat makes AP and initiative the master stats; real-time hands aim to the player
  (`gameplay/systems-comparison.md` §23). FO3: Burgess, "We didn't really have first-person shooter experts", and
  low-skill characters miss at the crosshair. FO4's gunplay, built with id and Bungie advice, was "this game's most
  uncontested win" (`reception/fallout-4.md`). For FO1/2: "Slowness and early randomness, not turn-based play
  itself, are what modern players reject" (`reception/fallout-1-and-2.md`).
- *Audit:* For each stat, name its visible readout in combat.

**MH-19 · Threshold-plus-floor armour that the player can read**
- *Rule:* Armour subtracts a flat threshold with a guaranteed minimum bleed-through (start at 20% of base
  damage). An "absorbed" indicator shows when a hit is mostly stopped. The maths is checked on paper for every
  weapon class at every tier. Each calibre has 3-4 ammo variants with one trade-off each, and armour-piercing beats
  standard ammo against armour in an automated test.
- *Why:* A threshold creates weapon roles (small arms stop working against heavy armour). The floor prevents
  dead ends. Visibility makes the choice a decision rather than a guess.
- *Evidence:* NV: `Final = max(Base × (1 − DR) − DT, Base × 0.20)`, plus a red shield icon
  (`gameplay/fallout-new-vegas.md`). FO3's percentage-only DR, capped at 85%, hid whether armour was working
  (`gameplay/systems-comparison.md` §23). FO2 applies the ammo multiplier before armour, so armour-piercing rounds
  do worse than hollow-points against almost everything. It is "the best-known balance bug in the game"
  (`gameplay/fallout-2.md`).
- *Audit:* Is the weapon x armour spreadsheet signed off? Is the AP-vs-standard test green?

**MH-20 · Every creature has a verb and a tell**
- *Rule:* Every creature family has at least one combat behaviour (burrow, charge, feign death, revive allies,
  spit, explode) and a distinct sound heard before it is seen. Higher tiers add behaviours, weak points or
  compositions, not hit points.
- *Why:* Behaviour makes fights decisions. Sound tells the player what is coming, which makes danger fair.
- *Evidence:* "Give every creature a combat verb... Prefer new behaviours over recoloured tiers"
  (`lore/universe/creatures-and-mutation.md`). "Creature audio should work as warning"
  (`audio/sound-design-and-voice.md`). Mart's Mutant Mod, which adds creature variety and sharper AI, is a staple
  FO3 fix (`community/mods-as-design-feedback.md` §2). See NDA-17 for the HP-sponge alternative.
- *Audit:* Bestiary sheet: do all families have a verb and a recorded tell?

### Economy, survival & crafting

**MH-21 · Sinks before faucets; money still matters in the last act**
- *Rule:* Expensive, build-relevant sinks (implants or equivalents, training, rare ammo, repairs priced by item
  value) are designed before loot tables. Every repeatable faucet is capped inside the fiction. In the final act,
  the player still wants money.
- *Why:* Once nothing is worth buying, loot stops being a reward and the economy stops being a system.
- *Evidence:* Every game except FNV "runs out of things to buy". FNV's stat implants cost 4,000 caps each with the
  count capped by Endurance; special implants cost 8,000-12,000; casinos ban big winners
  (`gameplay/systems-comparison.md` §13.2, `gameplay/fallout-new-vegas.md`). FO3: "Drowning in caps, nothing to
  buy". FO4: "one uncapped faucet (water farming) ends the economy" (`gameplay/fallout-4.md`).
- *Audit:* Plot the simulated wealth curve against sink prices at 25/50/75/100% of content.

**MH-22 · Scarcity defended by systems, junk that matters, lists that work**
- *Rule:* The default rules include weighted ammunition and healing items, non-instant healing, loot themed to
  plausible containers, and vendors that buy only what they trade in. All junk breaks into a small set of
  components, with a few bottleneck parts tied to other systems. Every inventory, barter and crafting list has
  search, sort and filter.
- *Why:* Scarcity is the genre's core feeling. Without systemic defence it collapses at the midpoint. Components
  give every object a purpose; good lists keep that purpose from becoming bookkeeping.
- *Evidence:* "Every game in the series has the same curve problem: scarcity collapses by the midpoint"
  (`gameplay/design-principles.md` §5.4). FO4's Survival mode is "widely regarded as the best way to play because
  it makes every other system matter" (`gameplay/fallout-4.md`). The FO4 modding list ships Loot Logic and Reduction
  and Complex Vendors (`community/mods-as-design-feedback.md` §4.3). Junk-to-components is "the series' best loop
  invention" (`gameplay/systems-comparison.md` §13.1). VNV's Menu Search adds Ctrl-F to six menus.
- *Audit:* On Normal difficulty, at 50% of content, are the player's ammo and healing stocks still a
  consideration? Does every list have search?

### Factions & companions

**MH-23 · Factions with an argument, an economy and a home**
- *Rule:* Each faction has a one-paragraph case a smart member would make, and the one fact that most damages it.
  Its material basis (food, trade, shortage, debt) is on screen. It has at least three named dissenters, and a
  walkable home territory with civilians and a questline comparable to its rivals'. If any of this cannot be
  funded, cut the faction whole rather than starve it.
- *Why:* A choice between factions is only a dilemma if every side's case can be seen and its cost visited.
- *Evidence:* The best-regarded factions "each have a real argument". The NCR is believable because the game shows
  "its brahmin barons, taxes, water-backed currency, conscripts and supply lines". The Minutemen are "a faction that
  is only a gameplay system" (`lore/universe/factions.md`). The Legion's positives "did not happen" because its
  territory east of the Colorado was cut, and it is "by far the least frequently selected ending" (Sawyer, 4 and 7
  May 2012, `design-insights/sawyer-new-vegas-design.md`).
- *Audit:* Is the faction sheet complete? Does each faction have walkable home territory?

**MH-24 · Companions as embodied arguments, with bodies that work**
- *Rule:* Each companion ties to a faction or theme. Each has a personal quest with two defensible outcomes and its
  own ending slide, and a gameplay perk that changes how the player plays. Companions take commands (stance,
  target, inventory, wait), never hurt the player through ordinary fire, and object or leave when the player acts
  against their values.
- *Why:* A companion carries a theme at human scale and changes play. A companion that blocks doors and shoots the
  player is a cost.
- *Evidence:* FO1's companions were a last-minute addition: no inventory screen, no armour changes, and burst-fire
  allies that shoot the player. Friendly fire and blocked corridors were "the number one complaint in 1997"
  (`gameplay/fallout-1.md`, `reception/fallout-1-and-2.md`). FNV gives each companion a personal quest that changes
  its ending slide, plus a companion wheel and perks (`gameplay/systems-comparison.md` §12). FO4's affinity is "a
  reputation system with an audience of one" (§11).
- *Audit:* Does every companion pass the checklist above?

### Tone & writing

**MH-25 · A written tone bible with one owner**
- *Rule:* Before content production, a short vision and tone document names what the game refuses to be and
  includes a humour rule of the form "If the player doesn't get them, they shouldn't notice them". One named person
  signs off on every area's register and has a veto.
- *Why:* Tone is what fans remember and what parallel teams drift apart on. A written rule can be applied by
  anyone; an owner keeps the drift from shipping.
- *Evidence:* FO1 survived losing the GURPS licence because its tone and rules were already written down
  (`design-insights/development-history.md`). A tone document is "cheap to write and expensive to lose"
  (`design-insights/production-metrics.md` §9). FO2's areas went to many designers. Avellone called it "a slapdash
  project without a lot of oversight", and it ranks below FO1 among its most devoted audience "mainly because of
  tone" (`reception/fallout-1-and-2.md`). The Cain rule is quoted in `gameplay/design-principles.md`.
- *Audit:* Does the document exist? Is the owner named? Is there a sign-off log per area?

**MH-26 · Our own ironic engine**
- *Rule:* Define one original tonal contrast: a sincere belief the old world held, drawn from a different era than
  mid-century America. Apply it consistently across four channels: mascot or figure, interface, propaganda and
  advertising, and technology. The world itself never knows it is funny.
- *Why:* Contrast is the asset; neither pure bleakness nor pure comedy works alone. Borrowing Fallout's contrast
  would make us derivative.
- *Evidence:* Fallout's device is "cheerful surface over lethal subtext" (`lore/universe/pre-war-world.md`), the
  cheerful mascot giving a thumbs-up over horror (`art/art-direction.md`). "The contrast is the asset; neither pole
  works alone"; "an original game needs its *own* source of irony" (`gameplay/design-principles.md` §5.5).
- *Audit:* Can the team state the contrast in one sentence and show it in each of the four channels?

### Art

**MH-27 · One governing visual rule, and the hero silhouette first**
- *Rule:* A one-page look bible: a material or silhouette rule that can be applied to any new prop in ten
  seconds, a ban list of 3-6 technologies or forms, the palette set and sign typography. Our one hero silhouette is
  art-directed before any other asset.
- *Why:* A single filter gives a large or changing team a consistent shape language and an identity players can
  recognise in one frame.
- *Evidence:* Boyarsky's filter, "the aesthetics of the world of the future as envisioned by the culture of the
  1940's and 50's", was the standard every asset was judged against. The vacuum-tube rule was an art decision
  first. In FO3 the power armour was "the first asset built" (`art/art-direction.md`,
  `lore/universe/technology-and-items.md`). The FO3-to-FO4 palette swings show what drift looks like without a
  bible (`art/art-direction.md` takeaway 15).
- *Audit:* Does the look bible exist? Do asset-review rejections cite it?

**MH-28 · Regional palettes, with saturated colour reserved for meaning**
- *Rule:* 5-8 regional palettes, each with its own architecture, vegetation, light colour and sound. Base terrain
  is muted; the most saturated colour is reserved for settlements, hazards and faction markers. Any global colour
  grade is mild and player-adjustable.
- *Why:* Distinct regions prevent fatigue over long sessions. Reserving saturated colour lets players find what
  matters at a glance.
- *Evidence:* Howard on FO3: "a sameness to the environment" that "can be, if you're playing the game for an
  eight-hour stretch, a little depressing". Menze on NV: brown "gets very challenging to use over and over again".
  FO4's muted terrain with coloured man-made objects raised location legibility (Engadget, cited in
  `art/art-direction.md` takeaways).
- *Audit:* In greyscale screenshots, can regions be told apart? In a wide shot, does the settlement read first?

**MH-29 · An in-world interface that is also a good list**
- *Rule:* The menu is an in-world device with a manufacturer, a model history and a colour justified in the
  fiction (re-tintable). It also meets list usability: search, sort, compare, a dense PC layout, legible
  highlights, and the vision-document rule "easy to use while still supporting complex actions".
- *Why:* An in-world menu is the cheapest immersion multiplier. Poor lists tax the most frequent verbs in the
  game.
- *Evidence:* The Pip-Boy is "the series' strongest piece of identity design" and, as a list interface,
  "mediocre in every game". "Identity and usability were never both achieved" (`gameplay/systems-comparison.md`
  §20). UI is the second most-modded layer: VNV lists 13 UI mods, and FO76's only mod scene is UI
  (`community/mods-as-design-feedback.md`).
- *Audit:* Benchmark: how many seconds to find a named item in a 200-item inventory?

### Audio

**MH-30 · An adaptive score, with silence as a designed state**
- *Rule:* The music engine is specified before the composer is contracted: cue types, layered location tracks,
  day/night and intensity mixes, combat intro/loop/outro with hysteresis (so music does not flip with every
  skirmish), and an explicit silent state with timers. Exploration is near-silent and ambience carries it. Music
  ducks under ambience, not the reverse.
- *Why:* Silence makes cues land. Layered hub themes give wayfinding by ear. Dark ambient beds are cheap per hour
  and age well.
- *Evidence:* NV (Lawlor): five cue types; incidentals of 5-15 seconds; location tracks with three layers; "the
  system will go silent until a new command is given" (`audio/ambient-radio-pacing-and-foley.md`). Morgan's
  ambient approach "is far cheaper to produce per hour and holds up for 25+ years" (`audio/score-analysis.md`). IGN
  praised FO3's "minimalist" wind and dust (`audio/sound-design-and-voice.md`).
- *Audit:* Does the state-machine spec exist before the composer contract?

**MH-31 · In-world sounds that carry information**
- *Rule:* Two or three signature sounds double as interface or hazard information (a hazard ticker, the
  interface device's own clicks), recorded from real equivalents. Every creature family has a learnable warning
  call. Gunfire has near and far layers.
- *Why:* Information by ear keeps the player looking at the world, and makes the identity recognisable within
  one second.
- *Evidence:* Pip-Boy sounds came from everyday clicks plus recordings of an old 7200 RPM hard drive; the Geiger
  crackle reports radiation without UI (`audio/ambient-radio-pacing-and-foley.md`,
  `audio/sound-design-and-voice.md`). NV's near/far gun layers (`audio/ambient-radio-pacing-and-foley.md`).
- *Audit:* With the screen covered, can a tester identify the hazard level and the nearest creature type by ear?

### Production & launch

**MH-32 · Stability before content**
- *Rule:* Lock scope early enough that the final months are bug-fixing. QA is a named budget line sized to the
  amount of branching, because reactivity multiplies script state. Prototype the densest hub on the weakest target
  hardware first. Build the middle of the map first so cuts fall at the edges. Quest logic has fail-safes
  (alternate triggers, redundant information). The rule is "less content, fewer bugs".
- *Why:* A review score is a snapshot of the worst build, and reputations attached to it last. Quest-blocking
  bugs are a design failure as well as a QA one.
- *Evidence:* Every game after FO1 has a community unofficial patch: FO2's fixes 800+ bugs; UFO4P is described as
  fixing "thousands of bugs" (`community/mods-as-design-feedback.md`). Edge on NV: "Creatively... gets almost
  everything right. Mechanically and technically, it's a tragedy" (`community/fan-sentiment.md`). NV scored 84 and
  missed its bonus by one point; "A review score is a snapshot of the worst build" (`reception/fallout-new-vegas.md`).
  Sawyer: "less content, fewer bugs would have been better" (9 Apr 2011). The Strip was split into load zones
  because of console memory crashes (`design-insights/sawyer-new-vegas-design.md`).
- *Audit:* Are there zero known quest blockers at release candidate? Is crash-free play time measured against a
  target?

**MH-33 · One expensive pillar; text by default**
- *Rule:* Budget each feature in person-months before pricing anything. Pick at most one expensive pillar (open
  world scale, voice, systemic building, multiplayer). Text is the default and voice the exception. Use inherited
  or off-the-shelf technology. Show a playable vertical slice to whoever funds us, early.
- *Why:* Labour spent on presentation does not return as reactivity. Reactivity per person-month is our
  competitive edge.
- *Evidence:* NV produced about 65 voiced lines per person-month, against about 22 for FO3 and 32 for FO4 `[C]`.
  NV's 84 took about 1,000 person-months; FO4's 84 on PC took about 3,500 `[C]`. FO4 combined a voiced
  protagonist, a renderer rewrite, gun modding and settlements. Van Buren had a demo the executives never saw
  (`design-insights/production-metrics.md` §7, §9).
- *Audit:* Does the feature list have person-month ceilings? Is the count of expensive pillars 1 or fewer?

### Community & modding

**MH-34 · Moddable from day one, with the designer's hard mode in the box**
- *Rule:* Documented, open data formats; scripting hooks; a 64-bit executable; an in-game config menu.
  Post-launch updates are treated as breaking API changes: versioned, offered as opt-in branches, coordinated with
  the major mod teams. Ship a named Hardcore ruleset owned by the designers, with every part individually
  toggleable.
- *Why:* The long tail of every beloved entry was maintained by its community. The most-used rebalance in the
  series was the director's own list, so ship it rather than wait for a fan fork.
- *Evidence:* FO4's 25 Apr 2024 update broke the script extender and delayed Fallout: London by three months;
  the 2025 Anniversary Edition bundle page went "Mostly Negative" (`reception/fallout-4.md`). FO2's text-table data
  is why it is still playable (`gameplay/fallout-2.md`). JSawyer cut carry weight from 150 to 50, set base HP to
  50, cut the cap from 30 to 15 and doubled need rates (`design-insights/sawyer-new-vegas-design.md`). Unlimited
  Survival Mode and Safe Travels show players want the annoying parts of a hard mode configurable
  (`community/mods-as-design-feedback.md` §4.2).
- *Audit:* Is the modding SDK available on release day? Is the Hardcore toggle list published?

---

## 3. NEVER DO AGAIN

28 anti-patterns. Each has the canonical offender, why it fails, and what we do instead.

### Dialogue & role-playing

**NDA-01 · Tone-label prompts that hide the actual line (the "Sarcastic" problem)**
- *Offender:* FO4. Prompts were one to three words; Kotaku named "SARCASM" and "HOLD ON" as prompts whose spoken
  lines differed from what the player intended. Game Informer: prompts "can lead players to say things they didn't
  intend". A Steam thread reports "Sarcastic" in reply to "Can you help me?" producing a harsh insult. (These are
  reports; no verbatim prompt/line pair was obtained `[UNVERIFIED]`.) Lead artist Pely says the team chose to
  "simplify it and not even make you read the response before clicking on it", and that players "feel like they're
  missing something". Revealed preference: Full Dialogue Interface shipped eight days after launch; its authors
  called the prompts "inconsistent and confusingly arranged" and conversation "a crapshoot"
  (`design-insights/bethesda-dialogue-postmortems.md` §4; `community/mods-as-design-feedback.md` §4.2.1). Howard,
  2025: "it really did not resonate".
- *Why it fails:* The player cannot predict their own character's words, so they no longer author the character.
  Every mismatch reads as the game lying, and consequences feel random.
- *Instead:* MH-10. A paraphrase is allowed only if it states the content ("Refuse and threaten him"), never the
  register alone.

**NDA-02 · An option count fixed by controller geometry, and false choices**
- *Offender:* FO4: "The dialog wheel always has four dialog options, one assigned to each face button". The
  pattern critics name is "Yes, Question (Yes), Sarcastic (Yes), No (Yes)". A Steam user reports every option at one
  scene giving the same reply (`design-insights/bethesda-dialogue-postmortems.md` §4.1). XDI exists to remove the
  "hardcoded 4-option limit" (`community/mods-as-design-feedback.md`).
- *Why it fails:* Fixed slots force filler variants of "yes", so refusal disappears. Recording cost caps branching:
  voiced dialogue means fewer options, then a wheel, then no skill checks (`gameplay/design-principles.md` §6,
  chain #3).
- *Instead:* Variable counts in a scrollable list that works on a gamepad. Lint for identical replies. Every quest
  hook offers a real "no" with its own consequence (MH-10).

**NDA-03 · A voiced, fixed-backstory protagonist**
- *Offender:* FO4's Sole Survivor: a pre-war veteran or lawyer whose spouse is murdered and son kidnapped, voiced
  by two actors with "more than 13,000 lines of dialogue each" out of 111,000 in the game. Howard: "Players want to
  role-play more and we had a voiced protagonist"; "It was also hard on our designers to write that way."
  Pagliarulo dropped Starfield's recorded voiced lead because "this guy is too specific"
  (`design-insights/bethesda-dialogue-postmortems.md`). Mod evidence: a crowded alternate-start category
  (`community/mods-as-design-feedback.md` §4.4.2). Narrative mismatch: "find my kidnapped baby" against forty
  hours of settlement building, "Worst mismatch of the series" (`gameplay/systems-comparison.md` §17).
- *Why it fails:* A voice fixes the personality and doubles every line across two actors. That caps branching and
  makes modding new quests harder. A fixed backstory contradicts the promise to be anyone, and a fixed urgent motive
  fights an open world.
- *Instead:* MH-12. Spend the voice budget on the world (CM-10). If we ever want a defined hero, call the game a
  defined-protagonist RPG from day one.

**NDA-04 · Percentage-roll speech checks with free saving**
- *Offender:* FO3: a visible percentage, one attempt per conversation, reloadable. "A 30% check is passed by
  pressing F9 three times" (`gameplay/systems-comparison.md` §10). FO4's colour-coded Charisma percentages can be
  rerolled by reloading (`reception/fallout-4.md`). Sawyer replaced them because they "just lead to save-scumming",
  and "Randomized resolution of stand-alone tasks is pointless" with unlimited save and reload
  (`design-insights/sawyer-new-vegas-design.md`).
- *Why it fails:* Free saving turns probability into tedium, so the check tests patience rather than the build.
  "The save system quietly dictates what consequences a game can afford" (`gameplay/systems-comparison.md` §19).
- *Instead:* MH-11. If a random outcome is wanted, restrict saving around it, or make failure open a different
  path rather than a dead end.

**NDA-05 · A binary global karma meter**
- *Offender:* FO3: one number from −1000 to +1000 gates companions and decides which hit squad hunts the player.
  Stealing lowers it even when unseen, and it invites absurdities like "nuke a town, then donate water to return to
  sainthood" (`gameplay/systems-comparison.md` §11). Shamus Young: "saint-or-monster options" with few
  consequences (`reception/fallout-3.md`). Even after NV demoted it, Sawyer says karma had "very little effect" and
  was "mostly just there for player feedback" (`design-insights/sawyer-new-vegas-design.md`).
- *Why it fails:* One all-knowing axis collapses every dilemma into good or bad, makes atrocity cancellable by
  charity, and reacts to deeds no one witnessed. World reactions feel arbitrary and grey dilemmas lose their
  ambiguity.
- *Instead:* Per-community reputation on two tracks (fame and infamy, which do not cancel), driven by witnessed
  acts, plus a short list of earned titles with concrete trade-offs (FO2's Made Man, Slaver, Childkiller,
  `gameplay/fallout-2.md`). No vestigial meter alongside them.

### Quests & consequence

**NDA-06 · Radiant or procedural filler in place of bespoke quests**
- *Offender:* FO4's Minutemen ("another settlement needs your help"): the jobs auto-assign, have hidden timers and
  never end, and they are woven into faction progress. The quest-giver became a meme (`gameplay/fallout-4.md`,
  `community/fan-sentiment.md`). GamesRadar noted that too many faction quests are radiant
  (`reception/fallout-4.md`). Revealed preference: "Who's The General" exists to stop a new quest being issued at
  every turn-in (`community/mods-as-design-feedback.md` §4.3). No Bethesda statement acknowledging the problem was
  found (`design-insights/bethesda-dialogue-postmortems.md`).
- *Why it fails:* A named quest-giver promises authored content. Template content then cheapens both the faction
  and the giver into a nag, and hidden timers punish the player for ignoring it. "Players accept procedural
  rewards and reject procedural stories" (`gameplay/design-principles.md` §5.6).
- *Instead:* Generate situations, not quests: road encounters, patrol clashes, weather, scarcity events, loot
  variance. Any repeatable job sits on an opt-in board, in a separate log, with no hidden timers, no penalty for
  ignoring it, no unique rewards, a cap on repeats per source, and never on the authored progress path.

**NDA-07 · A world where choices leave no visible trace**
- *Offender:* FO4: four faction routes that converge on "destroy the other bases"; "only two cutscenes exist"; no
  slides for towns or companions (`reception/fallout-4.md`, `lore/games/fallout-4.md`). FO76: "story choices that
  cannot change a shared world" (`reception/fallout-76.md`). Revealed preference: Reinforcements and Retribution
  adds consequences for clearing dungeons, and The Living Desert adds "hundreds of NPCs and scripted events"
  (`community/mods-as-design-feedback.md`). FO4's launch user scores were 4.7 on PC against critic scores of 84-88.
- *Why it fails:* Long-term esteem tracks reactivity. Dozens of hours with no trace tells the player their choices
  were decorative, and players stop making them deliberately.
- *Instead:* MH-06, MH-07, MH-09. Also, before the ending, every major quest changes at least one visible thing in
  the world: a population, a price, a building, a patrol, a broadcast.

**NDA-08 · Essential, unkillable NPCs as a crutch**
- *Offender:* FO3's Little Lamplight: unkillable child NPCs who insult the player and gate the main quest, "almost
  universally seen as not surviving a moment's thought" (`lore/games/fallout-3.md`). FO3 and FO4 protect "dozens"
  of essential NPCs, and FO4's companions are essential (`gameplay/systems-comparison.md` §12, §15).
- *Why it fails:* "protect the content from the player. It is cheaper and it tells players their agency is
  decorative" (`gameplay/systems-comparison.md` §15).
- *Instead:* MH-08. If something must be protected, keep it off the critical path, and never put an insult in its
  mouth.

**NDA-09 · Real-time or hard-fail clocks on exploration**
- *Offender:* FO1: 150 days to find the water chip, plus hidden deadlines on which mutants overrun towns. Patch
  1.1 (13 Nov 1997) removed the 500-day limit after complaints (`gameplay/fallout-1.md`). The timer was the top
  early customer complaint per Cain, and he says the timed quest is the one thing he would remove. Exactly what the
  patch removed is `[DISPUTED]` (`gameplay/systems-comparison.md` §17). Note the split: "a vocal minority of
  veterans now defend it" as the source of urgency (`reception/fallout-1-and-2.md`). Related failures: FO2's
  dreams nag without teeth; FO4's urgency is fake; in FO76, "Pressure moved from the fiction to the calendar" through
  daily caps and limited-time rewards (`gameplay/systems-comparison.md` §17, `gameplay/fallout-76.md`).
- *Why it fails:* It punishes curiosity in a game whose reward is curiosity. Hidden clocks can make a save
  unwinnable. Calendar clocks turn play into an obligation.
- *Instead:* Local, visible world-state clocks that the player can affect: a town declines if a quest is ignored,
  and the player is told. Never a game-over countdown, never a hidden deadline, and every seasonal or daily reward
  can be earned again later.

**NDA-10 · Finales that contradict the player's own tools**
- *Offender:* FO3's original ending: the player or Sarah Lyons must enter the radiation, while radiation-immune
  companions refuse; then the game hard-stops. It was "the single biggest launch flashpoint". Broken Steel (May
  2009) removed the hard stop and let companions do the job (`reception/fallout-3.md`).
- *Why it fails:* It breaks the rules the game itself taught. Players see the seam, and the climax becomes a
  complaint.
- *Instead:* Audit every scripted beat against party abilities, items and skills. Never hard-stop without slides
  and a clearly labelled save made before the finale.

**NDA-11 · An opening that ignores the build**
- *Offender:* FO2's Temple of Trials, a mandatory tutorial dungeon "demanded by marketing", forces spear and unarmed
  combat on every build and is "the most disliked part of the game" (`gameplay/fallout-2.md`). FO1's rat cave
  (`reception/fallout-1-and-2.md`). FO3's hour-long opening is "a replay tax" (`gameplay/fallout-3.md`).
- *Why it fails:* The first hour teaches that the build does not matter, and it is where players quit.
- *Instead:* MH-17. Teach inside the first real town; let replays skip the opening; never let an outside mandate
  dictate the first hour.

### Factions & companions

**NDA-12 · Shallow or arbitrary faction lockouts, and joining every side at no cost**
- *Offender:* FO4: "Within hours the player can be General, Director-designate, a Brotherhood Knight and a
  Railroad agent at once, and nobody objects until a scripted lock-out" (`lore/games/fallout-4.md`). The player can
  work three factions deep before lockout (`gameplay/systems-comparison.md` §15). There is no peaceful or refuse-all
  resolution. The raider route in Nuka-World is open only by betraying the Minutemen. In FO76, both Settlers and
  Raiders reputations can be maxed. Contrast NV, where factions are mutually exclusive "at defined points with
  explicit warnings" (`gameplay/systems-comparison.md` §15), with a one-time amnesty after act one
  (`lore/games/fallout-new-vegas.md`). FO2's Made Man
  status with one New Reno family turns the others (`lore/games/fallout-2.md`).
- *Why it fails:* Membership without cost means factions differ in whom they shoot, not in what they mean. A late
  scripted lockout then feels arbitrary, because the world ignored the contradiction until the plot needed it.
- *Instead:* Commitment costs show early: dialogue reacts to dual loyalties, promotions require a deed that offends
  a rival, and the lock points are signposted in fiction with a warning. One amnesty. Outcomes include truce,
  absorption, coup, exile and reform; total destruction is one option with a price, never mandatory
  (`lore/universe/factions.md`).

**NDA-13 · A faction whose case is only hearsay**
- *Offender:* NV's Legion. Its selling point ("safe roads") is told, not seen; its homeland was cut; it is the
  least-chosen ending (`lore/universe/factions.md`, `design-insights/sawyer-new-vegas-design.md`). FO4's Institute:
  "strong aesthetic, incoherent motive"; replacing farmers with synths, "nobody in the game can say why".
- *Why it fails:* The choice tilts toward the side the player can see, and the dilemma collapses.
- *Instead:* MH-23. Deliver every faction's best claim in play.

**NDA-14 · Companions as turrets or friendly-fire hazards**
- *Offender:* FO1: companions cannot change armour, take no orders, and their burst fire hits the player
  (`gameplay/fallout-1.md`). FO3: karma-gated and thin. "Do not ship followers as karma-gated gun turrets"
  (`gameplay/fallout-3.md`). Revealed preference: follower AI fixes and "Dogmeat Lags Behind" in FO4 mod lists
  (`community/mods-as-design-feedback.md`).
- *Why it fails:* A companion with no arc, no control and a bad path-finder adds friction and no meaning.
- *Instead:* MH-24, or no companions at all.

### Character systems & progression

**NDA-15 · Build convergence: a perk every level, no cap, flat-percentage perks**
- *Offender:* FO3 (a perk every level, skills maxed by level 30), FO4 (no cap; 70 perks with about 229 ranks,
  many flat damage increases; everything owned by level 286), FO76 (flat damage cards). Bethesda's stated reason for
  deleting skills, that they "ended up spreading your choices too thin" (`design-insights/bethesda-dialogue-postmortems.md`),
  removed the gating function and kept the convergence. NV's DLC cap raises (`gameplay/fallout-new-vegas.md`).
- *Why it fails:* No lock-outs, then no cap, then convergence, then enemy scaling, then loot variance to restore
  excitement (`gameplay/design-principles.md` §6, chain #2). The character stops being a choice.
- *Instead:* MH-14, MH-16.

**NDA-16 · The setting's most iconic power in the first hour, or top gear in an unguarded locker**
- *Offender:* FO4 hands over power armour and a minigun in its second main quest: "the most cited example of the
  series abandoning the long climb" (`gameplay/design-principles.md` §5.4). In FO2, Advanced Power Armor sits in an
  unguarded Navarro locker that a level 1-3 character can reach with one dialogue check
  (`gameplay/fallout-2.md`). Revealed preference: SPARS (fewer power armour parts) exists because "Power armor lost
  its specialness" (`community/mods-as-design-feedback.md` §4.3).
- *Why it fails:* It spends the best reward on a trailer moment and collapses the scarcity curve.
- *Instead:* See one, fear one, earn one. Gate top gear behind capability, or make the world react to sequence
  breaking (the gear gets you recognised, hunted, refused service). Best gear is a capstone with upkeep.

### Combat

**NDA-17 · Level-scaled bullet-sponge enemies**
- *Offender:* FO3's level-scaled lists, then Broken Steel's sponges: Albino Radscorpion 1,500 HP, Super Mutant
  Overlord 1,250, Feral Ghoul Reaver 1,100, against 100-500 HP for most base-game enemies (`gameplay/fallout-3.md`).
  FO4's health scales inside zone bands; forum quotes cite "7-8 headshots with a sniper to kill a super mutant,
  double or triple that for a legendary"; mods (SCOURGE, True Damage) exist to fix it
  (`gameplay/systems-comparison.md` §23). FO76's One Wasteland (Sep 2020) scaled every enemy to each player.
- *Why it fails:* Progression becomes an illusion ("The world grows with you"). Fights get longer, not harder.
  Difficulty by HP multiplier is the least liked lever in the series.
- *Instead:* MH-02 and MH-20. Fix the armour model (MH-19), not enemy health. Difficulty settings change scarcity,
  AI and healing rules, not just multipliers, and harder difficulty never awards more XP
  (`gameplay/fallout-3.md`).

**NDA-18 · A targeting mode that makes the player invulnerable**
- *Offender:* FO3's V.A.T.S.: the player takes 10% of normal damage while it plays out. It is effectively an "I
  win" button, and the combat was balanced assuming its use (`gameplay/systems-comparison.md` §22.3). FNV cut the
  reduction to 25% (player takes 75%); FO4 moved to slow motion with AP shared with sprint.
- *Why it fails:* If pausing is safe, real-time play becomes the penalty phase, and the assist becomes the game.
- *Instead:* Aimed shots priced in risk (accuracy traded for crit chance) and in a spendable resource. Never a
  damage shield (CM-02).

### World & exploration

**NDA-19 · A world with no people in it**
- *Offender:* FO76 at launch: zero living human NPCs; every faction already dead. GameSpot gave it 4/10,
  "soulless"; it was "little more than just an environmental exhibit with things to kill"
  (`reception/fallout-76.md`, `art/art-direction.md`). Kotaku's 2022 investigation: most designers wanted NPCs and
  were overruled. Wastelanders added them 17 months later, and the PC score rose from 52 to 68
  (`design-insights/production-metrics.md`; `reception/fallout-76.md` gives 69, so the files differ by a point).
- *Why it fails:* "Removing a pillar is not innovation." Dropping NPCs removed dialogue, choice, consequence and
  companionship, "the reasons people play this series" (`reception/fallout-76.md`).
- *Instead:* Every region has living inhabitants who want things before it has collectibles. Dead factions are
  seasoning, used for one lesson about the living. Other players are never a substitute for authored characters.

**NDA-20 · Invisible walls, and hubs chopped into loading cells**
- *Offender:* NV's invisible walls (Sawyer, 5 Dec 2012: in retrospect most should have been dropped). NV's Strip
  split into load zones for console memory: "the game is named after a city whose centrepiece is its weakest space"
  (`reception/fallout-new-vegas.md`). FO3's downtown D.C. in pockets joined by metro tunnels; Burgess later called
  that layout "the big mistake" (`art/art-direction.md` §4.3). Revealed preference: Freeside Open rebuilds Freeside
  as one worldspace (`community/mods-as-design-feedback.md` §3.4.1).
- *Why it fails:* It breaks the open map's promise, and partitioned hubs feel empty.
- *Instead:* Terrain that looks impassable, honest map edges. The densest hub is memory-budgeted first (MH-32).
  Split cities by design into districts with identities, with short, distinct, mapped connectors.

### Tone & writing

**NDA-21 · Pop-culture jokes that break the fiction**
- *Offender:* FO2: overt pop-culture jokes, talking animals, a Scientology parody, kung-fu duels. This is "the
  game's most persistent criticism" (`lore/games/fallout-2.md`), and "Fallout 2's pop-culture jokes are its
  most-cited flaw" among fans; Avellone: "slapdash" (`reception/fallout-1-and-2.md`). "Both original leads and
  Bethesda's writer came down on the bleaker side" (`gameplay/design-principles.md` §5.5). Shamus Young on FO3: a
  "fundamental misunderstanding of the Fallout tone and themes" (`reception/fallout-3.md`).
- *Why it fails:* Jokes that need outside knowledge date fast, shrink the world into a reference, carry legal risk
  when they parody real organisations, and cause tonal whiplash between areas.
- *Instead:* Humour comes from the world's own logic and is invisible if missed (MH-25). Out-and-out jokes are
  opt-in, the way NV's "Wild Wasteland" trait fences them off, or confined to optional fringe content. No parody of
  real people or organisations, and no breaking the fourth wall.

**NDA-22 · A mystery antagonist with no answer, or a question the plot never tests**
- *Offender:* FO4's Institute. Its motives "do not hold up" (`reception/fallout-4.md`), and the synth question is
  raised repeatedly, but the game "never commits to an answer" and supplies contradictory facts
  (`lore/games/fallout-4.md`).
- *Why it fails:* "Secrecy without an answer reads as incoherence" (`lore/universe/factions.md`).
- *Instead:* Decide what the hidden power wants first, then what to conceal. Every sinister act traces to a motive
  a member could defend aloud. If the game asks a question, scenes test the evidence and the endings differ by the
  answer.

### Art

**NDA-23 · Ruins that look unswept after two centuries**
- *Offender:* FO3: set 200 years on, it looks like 20; people eat 200-year-old packaged food; intact wooden houses
  stand near ground zero (`reception/fallout-3.md`). FO3 and FO4 show skeletons still in beds after 200-210 years
  (`lore/universe/factions.md`). Pely likes the world "messy... inconsistent" because it "mimics the real world"
  (`art/art-direction.md`).
- *Why it fails:* The objection is not ruin; it is ruin with no causal story, "ruin as *wallpaper*". It breaks
  plausibility and drains the tension Shamus Young identifies: two centuries in which the only culture to emerge is
  raiders (`art/art-direction.md` §5.2).
- *Instead:* MH-03. Rebuilt zones show labour (repairs, patchwork, cleaned paths). Every ruin answers "who, and
  what next?" New culture visibly outweighs old branding (`lore/universe/pre-war-world.md`).

**NDA-24 · A single colour tint across the whole world**
- *Offender:* FO3's grey-green grade. Pely says they "definitely wanted to make it very clear" the game differed
  from Oblivion and may have gone too far. Howard calls the result "a sameness to the environment"
  (`art/art-direction.md`). Revealed preference: Fellout, which removes the green tint, is listed alongside the
  Unofficial Patch in a 2024 roundup (`community/mods-as-design-feedback.md` §2). Then FO4 swung back into colour:
  "defining oneself *against* another game produces swings" (`art/art-direction.md` takeaway 18).
- *Why it fails:* A screen-space grade is the cheapest form of identity and the first thing players delete. It
  causes fatigue over long sessions and makes regions blur together.
- *Instead:* MH-28. Distinction lives in materials, signs, light and regional palettes. Grading is seasoning,
  and there is a slider.

### Audio

**NDA-25 · Tiny radio playlists**
- *Offender:* Radio New Vegas: 19 tracks, about 52 minutes `[est.]`. Mojave Music Radio: 15 tracks, no host. GNR:
  20 songs, 55:27. With random picks, the expected first audible repeat comes after about 5.5 songs, roughly 17
  minutes (derived), which matches a Steam anecdote of about 20 minutes `[SNIPPET]`. Fans wrote "No Repeat Day"
  mods (`audio/ambient-radio-pacing-and-foley.md` §3.3). Polygon noted that only Magnolia and RedEye make new music
  in a setting that runs from 2102 to 2287 (`audio/licensed-music-and-radio.md`).
- *Why it fails:* Repetition inside a single session turns the signature device into noise. A catalogue that never
  grows says the world never changes.
- *Instead:* About 1.25 songs per planned game hour (the file's model, at f = 0.4, R = 6), so about 50 for a
  40-hour game. A second station with contrasting taste, tiered unlocks, and a no-repeat window of at least N/2.
  In-world musicians record new songs as the story advances. Public-domain compositions with new recordings as the
  default. Mute and mod hooks.

### Production & launch

**NDA-26 · Launching unfinished, then monetising before fixing**
- *Offender:* FO76. Launch Metascores of 52/53/49. Howard: "very little we didn't screw up". The trust incidents
  within seven weeks: a nylon bag sold as canvas, a 500-Atom compensation offer, a data leak caused by that process,
  refused refunds (`reception/fallout-76.md`). Repair kits went into the Atomic Shop in April 2019 (patch 8.5),
  breaking the "cosmetic only" promise. Fallout 1st ($12.99 a month) sold an unlimited scrap box, relief from the
  game's own stash limit, and launched broken. Kotaku: "every major launch bug was known to QA"; QA worked 10-hour
  days, six days a week; there was no proper beta, which Howard regretted (`design-insights/production-metrics.md`
  §6). User scores are still 2.7-3.0 in 2026. FO4's season pass was raised from $29.99 to $49.99 after sale
  (`reception/fallout-4.md`).
- *Why it fails:* "Launch scores are permanent." Trust failures compound faster than product failures. Selling the
  cure for a friction you designed corrupts your incentive to fix it (`reception/fallout-76.md`).
- *Instead:* The date moves or scope is cut. A public beta for anything networked. QA's known issues are
  release-blocking. No paid relief from designed friction. Never change the price or scope of a pre-sold bundle.
  Over-compensate on the first attempt.

**NDA-27 · Growing scope while the schedule shrinks, or retrofitting tech in a short window**
- *Offender:* FO2: a mandate to be bigger, with about nine months of real production; shipped very buggy, the
  ending thin. NV: 18 months on an engine nobody at the studio had shipped on, with a bonus tied to Metacritic 85,
  missed by one point. FO76: multiplayer on a single-player engine that "doesn't load except around one player"
  (Mayer), on a fixed date after E3 (`design-insights/production-metrics.md`). Urquhart's own conclusion was to slip
  the date rather than crunch.
- *Why it fails:* Each case produced a launch that needed heavy patching and visible damage. Incentives tied to
  review aggregates breed resentment, not quality.
- *Instead:* Fix scope first (MH-32, MH-33). Choose technology for the game being made. No pay or bonus tied to
  review aggregates; milestones use things the team controls (crash rate, completion rate).

### Community & modding

**NDA-28 · Breaking, banning or monetising the modding commons**
- *Offender:* FO4's next-gen update (25 Apr 2024) broke F4SE and delayed Fallout: London by three months; the
  Anniversary Edition (2025) "broke popular mods" (`reception/fallout-4.md`). FO76 banned players for mods,
  including some who fixed visuals (`community/mods-as-design-feedback.md` §5). Paid Skyrim mods were reversed in
  about four days after a petition passed 51,000 signatures in a day, and Creation Club was read as "paid mods"
  again (§4.6).
- *Why it fails:* The community is the free QA team and the long tail. Fallout: London's 500,000+ redemptions in 24
  hours show the size of the audience that breaking the tools alienates.
- *Instead:* MH-34. Paid content is only ever additive and curated, and never monetises existing free work.

---

## 4. The contested middle

Twelve questions where the evidence splits. For each: the best case on each side, then our position as a small
original team.

**CM-01 · Turn-based or real-time combat?**
- *For real-time:* It is what the mass audience bought. FO4's gunplay was "this game's most uncontested win", and
  FO4 led the 2022 r/Fallout poll for gameplay at 65.9% (`community/fan-sentiment.md`). Modern players bounce off
  FO1/2's slow combat and early whiffs.
- *For turn-based:* Stats are expressed natively (AP and Sequence become master stats) with no bridge mechanic.
  Wasteland 2 (Metacritic PC 81, Director's Cut 87; $2.93M Kickstarter against a $900k goal) and Wasteland 3 (85;
  2M+ players) show live demand (`gameplay/systems-comparison.md` §23.3). FO1/2 still sit at 94-95% positive on
  Steam. Bethesda twice needed outside shooter expertise and still shipped weak shooting in FO3.
- *Resolution:* **Turn-based tactical combat, presented fast**: speed settings on by default, batched enemy
  turns, low early whiff rates, aimed shots. Three reasons. Our thesis is build identity, and turn-based expresses
  stats without a bolted-on bridge (MH-18). A small team cannot reach FO4-grade gunfeel: Bethesda had no shooter experts on FO3,
  and its lead artist recalls the team asking of its hybrid "is this even fun?" (`gameplay/systems-comparison.md`
  §22.3). And a non-first-person camera lowers per-location art cost, which buys the
  density of MH-01. We accept a smaller ceiling on market size; the Wasteland and FO1/2 long-tail numbers say the
  floor is viable. One soft spot: Pagliarulo's "not every Fallout fan wants a turn-based isometric game" is
  `[UNVERIFIED exact quotes]`, but the market point stands without it.

**CM-02 · A targeting-assist mode (the V.A.T.S. question)**
- *For:* It lets a character's skill exist inside a player's shooter, gives stats a visible job, and was the
  identity of FO3. The banked crit meter in FO4 is "the best idea of the FO3-era VATS".
- *Against:* FO3's 90% damage reduction made it a win button. FO76's real-time version was "out of place". "A
  hybrid combat mode that exists only for stat expression will always be criticised by both camps"
  (`gameplay/systems-comparison.md` §22-23).
- *Resolution:* **No separate mode.** With turn-based combat (CM-01) the assist is unnecessary. Keep the
  transferable parts natively: a hit chance displayed per body region, FO1/2's crit coupling (Eyes −60 to hit, +60
  crit chance), capped so bosses are never one-shot, and a banked, player-triggered crit resource driven by our
  luck-equivalent stat, replacing hidden crit rolls.

**CM-03 · Weapon and armour durability**
- *For:* It turns loot into maintenance choices, provides a money sink, makes duplicates useful (FO3), and builds
  attachment to a battered favourite.
- *Against:* It becomes a chore when wear is invisible or a break comes at the worst moment. FO4 removed it and
  replaced the sink with components, without becoming a headline complaint (`[UNVERIFIED]`, no review piece
  retrieved). FO76's cash-shop repair kits caused a backlash (`gameplay/systems-comparison.md` §24).
- *Resolution:* **Keep it, at FNV softness.** Full effectiveness at 75% condition and above, then a gradual
  falloff and no hard break mid-fight. Visible condition bars. Three repair paths: duplicates or components scaled
  by skill, vendors priced by item value, and scarce kits. No real-money path, ever. It serves MH-21 and MH-22.
  Armour condition is cut if playtests show it is a chore; weapon condition stays.

**CM-04 · Settlement building**
- *For:* It gave junk a purpose and is the real core loop for many FO4 players. FO76's C.A.M.P. became "the game's
  most loved feature and its main social surface". Sim Settlements shows demand once the system has a purpose.
- *Against:* "The 30-odd buildable sites are mostly empty lots"; players felt they replaced hand-authored towns;
  one faction's whole questline runs through it (`reception/fallout-4.md`). Workshop was a late-schedule risk Gardiner
  expected to be cut (`design-insights/production-metrics.md` §6). It counts as one of the "expensive pillars".
- *Resolution:* **No free-form builder.** One player base with authored upgrade slots, where each upgrade is a
  quest outcome with a named resident and a visible change, and the authored towns change in response to the
  player's deeds. Expose the hooks so modders can build the sandbox if they want it.

**CM-05 · Survival needs (hunger, thirst, sleep)**
- *For:* FO4 Survival and NV Hardcore are "praised well beyond their usage numbers", and design-principles argues
  for folding survival into the base game rather than "hiding the best version of the game behind a toggle".
- *Against:* FO76's mandatory needs were unpopular and were turned into buffs. Sawyer: "I don't think Hardcore Mode
  is 'really' hard". Mods exist to make no-save and no-fast-travel rules configurable.
- *Resolution:* **Split it into two layers.** The scarcity mechanics that are real decisions are on for
  everyone: weighted ammo and healing, healing over time, limited carry weight, contamination that affects route
  planning. Needs meters and save restrictions live in the named Hardcore ruleset (MH-34), tuned from the JSawyer
  numbers, with every part toggleable. Needs must touch route planning, spoilage and trade, or they are cut
  (`gameplay/fallout-4.md`).

**CM-06 · A level cap**
- *For a cap:* Build identity (MH-14). JSawyer's cap of 15. FO1's cap of 21 is rarely reached.
- *Against:* Dead XP late in the game feels bad ("Do not let the level cap arrive before the content ends",
  `gameplay/fallout-3.md`). Endless games need endless progression (FO76).
- *Resolution:* **A hard cap, fixed in pre-production**, timed so a completionist reaches it in the final act at
  roughly 85-90% of content. XP earned after the cap converts into horizontal, non-power rewards. DLC adds
  horizontal options and never raises the cap.

**CM-07 · Skills, or perks only**
- *For perks only:* Bethesda said skills "had some confusing parts and ended up spreading your choices too thin".
  Critics liked FO4's perk chart for its clarity (`reception/fallout-4.md`).
- *For skills:* Removing them removed dialogue and world gating: "character build affects *how you kill* far more
  than *what you can do or say*" (`reception/fallout-4.md`). FNV's audited 13 skills are "best in series".
- *Resolution:* **Keep about 10-12 skills**, on a coarse scale where thresholds carry the meaning (steps of 25,
  `design-insights/sawyer-new-vegas-design.md` takeaway 17). Money-only skills (gambling, barter) become perks or
  small systems. Perks are a separate, rarer channel (MH-16, MH-17).

**CM-08 · World size and structure**
- *For seamless:* Presence, found stories, "go anywhere you can see". FO3 and FO4 are best in series for
  exploration.
- *For a node map:* It sells scale and big towns at almost no content cost; random encounters make the journey "a
  dice-driven story generator" (`gameplay/systems-comparison.md` §14). Seamless worlds that can be visited in any
  order push design toward sealed, low-reactivity locations (`gameplay/design-principles.md` §6).
- *Resolution:* **A hybrid**, the one the research calls "under-explored": compact, hand-built seamless regions
  (a hub plus its surroundings, dense per MH-01), joined by an abstract overland layer with encounters. The number
  of hubs stays small (5-7) so the flag web (MH-06) can be complete. This puts the procedural layer where the
  evidence says it is welcome (situations on the road) and keeps authored content where it is needed.

**CM-09 · Fast travel**
- *For free fast travel:* It respects player time; mods restore fast travel to FO4 Survival (Unlimited Survival
  Mode, Safe Travels).
- *Against:* FO4 Survival's lack of fast travel "makes every other system matter"; beds and routes gain weight;
  FO1/2's travel spends time and supplies and produces encounters.
- *Resolution:* **Overland travel is the fast travel.** It is instant in real time but costs in-game time and
  supplies, and can trigger encounters. Inside a region, travel between a hub's discovered points is free.
  Hardcore can add costs. Fast travel is never a paid convenience.

**CM-10 · The voice budget for NPCs**
- *For more voice:* The durable fan projects win on voiced writing (Fallout: London had 100+ voice actors; New
  California: about 5,000 voiced lines in part 1 and over 16,000 in the part-2 beta; "Large voice-acted dialogue pays off",
  `community/mods-as-design-feedback.md`). Starfield shipped 200,000+ spoken lines without a voiced lead. FO76's
  text-and-tapes launch failed.
- *Against:* "Voice is the single largest labour sink in the Bethesda games". FO3 cut about 30% of its dialogue
  late (`design-insights/production-metrics.md`). Actor reuse was severe in FO3 (one actor about 55 roles,
  `audio/sound-design-and-voice.md`).
- *Resolution:* **The player is never voiced. Voice the cast that carries the themes** (companions, faction
  leaders, the antagonist, the broadcaster) in key scenes, plus barks for everyone. Everything else is text. At most
  about 10 speaking roles per actor per region. Record after content lock so no recorded lines get cut. FO1's 21
  voiced NPCs in a text-heavy game are the model of proportion.

**CM-11 · Show the check requirement, or hide it?**
- *For showing:* FNV's transparency was "repeatedly singled out as respectful of the player". Hidden rolls mean
  the "player cannot tell skill from luck" (`gameplay/systems-comparison.md` §10).
- *For hiding:* Sawyer's own critique: a visible unlocked option implies "you should pick it"; thresholds bring
  "No tension; players 'shop' for the tagged option".
- *Resolution:* **Show the requirement and the player's value.** Fix the "tag means win" problem in the writing,
  not the interface: at least one in five tagged options carries a cost or is merely different (MH-11). Never hide
  whether a check is deterministic.

**CM-12 · Ending slides, or play after the ending?**
- *For slides and stop:* A world that keeps running "cannot show a mutually exclusive future". NV cut its
  post-game because reactivity could not be supported "to the extent that it deserved".
- *For continuing:* FO3's hard stop caused a backlash, and Broken Steel added post-game play. NV's lack of a
  post-game is "still a standing complaint". FO2's "slides, then keep playing" is "a workable middle".
- *Resolution:* **Slides first, then free play** in the world with the finale's consequences applied to the
  finale region and its hub only. Other hubs keep their pre-finale state, plus any ending-slide flags that have
  cheap in-world expressions. This is decided in pre-production and built into the quest state model. If it
  cannot be afforded by first playable, it is cut cleanly, with a labelled save made before the finale.

---

## 5. The matrix

Ratings: **●●●** exemplar (copy the structure) · **●●** solid, with known flaws · **●** weak · **✕** cautionary
(a named NDA case) · **—** absent or not applicable.

| Dimension | FO1 | FO2 | FO3 | NV | FO4 | FO76 | Best-in-series practice to learn from |
|---|---|---|---|---|---|---|---|
| Quest solutions | ●●● two-of-three rule; talk-down | ●●● many routes | ●● few, multi-solution side quests | ●●● all paths plus skill routes | ● combat by default | ✕ combat only | FO1's rule plus NV's skill-specific routes |
| Cross-hub reactivity | ●● mostly saved for slides | ●●● towns decide each other | ● karma, radio, Megaton | ●●● reputation; minor factions read three times | ✕ essentials, converging routes | ✕ shared world resets | FO2's flag web plus NV's modular minor factions |
| Endings | ●●● per-town slides; exile | ●●● ~13 communities, then free play | ✕ forced sacrifice, hard stop | ●●● 28 state-driven slides | ✕ two cutscenes | — none | NV's slide matrix plus FO2's free play |
| Dialogue & checks | ●● full text; hidden rolls | ●● low-INT dialogue expanded | ● full text; reloadable % rolls | ●●● visible thresholds, all skills | ✕ four paraphrased slots | ●● lists return (2020) | NV thresholds, fixing the "tag means win" problem |
| Protagonist identity | ●●● blank vault dweller | ●● tribal, open | ●● silent; vault biography | ●●● silent courier, small grudge | ✕ voiced fixed parent | ●● communal, unvoiced | NV: a small personal hook, open identity |
| Morality & standing | ●● karma plus titles | ●●● per-town reputation plus titles | ✕ binary karma | ●●● fame and infamy per faction | ✕ companion approval only | ● reputation via dailies | NV's two tracks plus FO2's titles |
| Factions | ● towns more than factions | ●●● contested Redding, New Reno | ● transplanted good and evil | ●●● four-way contest; Legion thin | ● braided, costless until lockout | ✕ dead at launch | NV's argument plus material basis |
| Companions | ✕ uncontrollable, shoot you | ●● party, orders, Charisma | ✕ karma-gated turrets | ●●● arcs, perks, command wheel | ●● affinity; strong writing | — none (allies later) | NV's arcs, perks and commands |
| Build identity | ●● traits; many dead skills | ●● cap 99; sniper meta | ✕ everything maxed | ●● audited skills; DLC cap creep | ✕ no cap, % perks | ● cards, free respec | FO1 traits, NV audit, hard cap |
| Combat feel | ● slow; early whiffs | ● same engine | ✕ weak gunplay | ●● iron sights; viable | ●●● id/Bungie-tuned shooter | ●● solid, online | FO4's feedback; FO1/2's pace problems fixed |
| Combat depth | ●● aimed shots, crit coupling | ● AP-ammo order bug | ✕ DR only; VATS as shield | ●●● DT floor, ammo types | ●● crit meter; opaque armour | ● damage-card metas | NV's DT, FO1's aimed shots, FO4's crit bank |
| Difficulty & scaling | ●● fixed; hard opening | ● brutal start, absurd end | ✕ scaled lists, sponges | ●●● authored danger map | ●● zone bands; sponges | ✕ per-player scaling | NV's danger geography; FO4's bands |
| Economy & scarcity | ● rich by the third act | ✕ top armour in open locker | ✕ drowning in caps | ●● real sinks; lenient Hardcore | ●● Survival fixes it; water farms | ✕ wallet caps, paid relief | NV's sinks plus FO4's Survival rules |
| Crafting & building | — none | — none | ● duplicate repair | ●● ammo, campfire, kits | ●● junk loop; settlements divide | ●●● C.A.M.P. as social core | FO4's components; FO76's visitable base |
| World structure & density | ●● node map, encounters | ●● larger map, a car | ●●● dense vignettes, first vista | ●● soft-gate loop; walls, load cells | ●●● dense, vertical | ●● handsome, no people | FO3's density plus NV's soft-gate loop |
| Environmental storytelling | ● limited by sprites | ● same | ●●● tableaux, terminals | ●● Vault 11 | ●●● found story everywhere | ●● carried everything alone | FO3/FO4 craft, alongside living NPCs |
| Tone discipline | ●●● bleak; invisible jokes | ✕ pop-culture whiplash | ●● earnest; kitsch outliers | ●●● dry; wackiness opt-in | ●● pulp versus family drama | ●● folk horror; theme park | FO1's rule plus NV's Wild Wasteland fence |
| Visual identity | ●●● the founding filter | ●● inherited, unchanged | ✕ green tint; 20-year-old ruins | ●● Googie; more colour | ●● accent colour for wayfinding | ●● regional folklore palette | FO1's filter plus FO4's accent palette |
| Audio & radio | ●●● Morgan's ambient score | ●● reused, extended | ●● reactive DJ; 20 songs | ●● adaptive engine; tiny radio | ●● 37 songs; piano motif | ●● 50 songs; warm DJ | NV's engine and news; FO76's catalogue size |
| Launch quality & trust | ●● timer patch; lost endings | ✕ 800+ bugs, saves broken | ● crashes; PS3 worse | ✕ crashes, save corruption | ● bugs; season-pass price hike | ✕ 49-53; the bag; Fallout 1st | FO1-scale scope with a real QA budget |
| Moddability & long tail | ●● fan-maintained (Fixt) | ●●● text data; restoration; total conversions | ●● G.E.C.K.; FWE | ●●● JSawyer; VNV; total conversions | ● huge scene; updates break it | ✕ bans; UI-only mods | NV's tools plus FO2's open data |

Reading across: NV has the most ●●● cells in the rows that drive long-term esteem (reactivity, endings,
dialogue, factions, companions). FO3 and FO4 own the exploration and environmental-storytelling rows. FO1 owns
tone and identity. No entry combines all three, and that combination is our target.

---

## 6. Cost-to-value ranking

Costs are relative and anchored in `design-insights/production-metrics.md` §9 where possible. All person-month
figures there are `[C]` estimates (±25% at best), and no ending-slide cost figure is sourced. **L** = mostly
writer and designer time plus script flags. **M** = needs dedicated tooling, art or audio passes. **H** = needs
specialist hires, large asset volume, or carries high schedule risk.

| Must-have | Cost | Value signal | Note |
|---|---|---|---|
| MH-25/26 Tone bible, ironic engine | L | FO1 survived losing its licence because of it | Cheapest item on the list; protects every other one |
| MH-27 Look bible, hero silhouette | L | 25+ years of recognisable identity | The decision is cheap; executing it is art cost |
| MH-10/11/12 Full-text, threshold dialogue; unvoiced lead | L | Top fan wish; FDI eight days after launch; Bethesda reversed course | NV: about 65 lines per person-month `[C]` |
| MH-05 Two of three per quest | L-M | Most-praised moment in FO1/2 | Writer time plus level hooks |
| MH-06/23 Flag web, faction reputation | L | FO2: "highest value-per-cost"; NV: "cheapest high-reactivity structure" | A handful of variables drives prices, access, dialogue |
| MH-07 Ending slides | L `[cost unsourced]` | "Gold standard"; a top reason players replay | A painting plus narration per slide, per systems-comparison; requires flag discipline from day one |
| MH-08 Kill anyone, with a fail-safe | L-M | Enables pacifist and kill-all runs | QA cost grows with branching; budget it |
| MH-09 Broadcaster reactivity | L-M | Best-loved NPCs "because they react" | Text or a small voice budget |
| MH-13 One extreme-stat register | M | "Players will cite it for decades" | Doubles main-path dialogue; one stat only |
| MH-14/15/16/17 Power budget, stat/skill audits | L | Fixes the series' most common systems complaints | Spreadsheets and a check-tracking tool |
| MH-21/22 Sinks, systemic scarcity | L-M | FO4 Survival "best way to play" | Tuning time; the components system is M |
| MH-02/20 Danger geography, creature verbs | M | "Fixed worlds create memories" | Behaviours cost AI and animation |
| MH-03 Settlement economy shown | M | #2 long-term FO3 complaint | Art props, not systems |
| MH-01/04 Density and environmental stories | M-H | FO3's 93 "on its own" | Dense hand-built content is labour-heavy; the hybrid map (CM-08) keeps it bounded |
| MH-18/19 Combat model, armour | M (turn-based) / H (real-time) | FO4's "most uncontested win" | Real-time gunfeel needed outside expertise at Bethesda |
| MH-24 Working companions | M-H | NV's companions are among the most loved | AI, path-finding, commands; FO1 shows the cost of doing it last |
| MH-28/29 Regional palettes, usable interface | M | "Sameness"; UI is the second most-modded layer | Art passes and UX iteration |
| MH-30/31 Adaptive score, information sounds | M | Morgan's ambient approach is cheap per hour | Engine spec is L; content is M |
| MH-32 Stability | M-H | Every game needed fan patches | Non-negotiable, whatever it costs |
| MH-34 Modding, Hardcore toggles | M up front, then amortised | Long tail; London's 500,000+ redemptions | Formats are cheap if decided early, expensive if added late |
| CM-12 Post-ending play | H | A standing complaint about NV | Sawyer estimated 5-8 months for a wish list that included it |

**Top 10 for a team with a limited budget** (order = do first):

1. **Tone bible plus look bible** (MH-25, MH-26, MH-27). Near-zero cost; every later cut is judged against them.
2. **Unvoiced protagonist; full-text, deterministic, visible checks across all skills** (MH-10, MH-11, MH-12).
   It buys the largest share of the role-playing audience's goodwill per hour of work.
3. **Two-of-three quest rule plus the skill x hub content matrix with its tracking tool** (MH-05, MH-17). It
   makes "builds matter" a production process.
4. **Per-community, two-track reputation instead of karma** (MH-06 web, NDA-05). A handful of variables drives
   the whole world.
5. **Ending slides per community, with reachability tests** (MH-07). The cheapest proof that the game was paying
   attention.
6. **Kill-anyone plus one fail-safe route** (MH-08). One rule that also forces robust quest logic.
7. **Hard power budget and the no-dump-stat audit** (MH-14, MH-15, MH-16). Spreadsheets, not content.
8. **Broadcaster before/after/failed lines** (MH-09). World-wide reactivity for a few hundred lines.
9. **Sinks before faucets, with scarcity defended by systems** (MH-21, MH-22). Tuning, not assets.
10. **Stability and an early scope lock, with open data formats from day one** (MH-32, MH-34). Not cheap, but the
    cheapest point to pay for them is now.

The expensive items we will fund only after these are secure: dense handcrafted locations (bounded by CM-08),
companion AI, selective NPC voice (CM-10), and the low-intellect register (MH-13).

---

## 7. Open evidence gaps

These claims are tagged `[UNVERIFIED]`, `[DISPUTED]`, `[SNIPPET]` or `[C]` in the research, or the research files
disagree about them. A decision in this document leans on each one. None of them changes a verdict on its own,
but these are the places to firm up before a decision is called final.

| Claim | Status and source | Leaned on by | How to firm it up |
|---|---|---|---|
| FO3's map is ~3.3 sq mi with a discovery every 1-2 minutes | Derived from a UESP cell count via a search summary. The popular "16 square miles" is `[DISPUTED]` (`gameplay/fallout-3.md`). `gameplay/systems-comparison.md` §14 still lists "About 16 square miles" `[UNVERIFIED]`, so the files disagree | MH-01 threshold | Time a walking route in FO3 ourselves; set our threshold from our own prototype |
| What FO1's launch patch removed (the water-chip quest or the hidden deadline) | `[DISPUTED]` (`gameplay/systems-comparison.md` §17) | NDA-09 | Cain's GDC 2012 video, not attendee notes |
| Real prompt/spoken-line pairs from FO4 ("Sarcastic" mismatches) | Reports only; no verbatim pair obtained `[UNVERIFIED]` (`design-insights/bethesda-dialogue-postmortems.md` §4.2) | NDA-01 examples | Extract from game dialogue data or capture video before using any example publicly |
| Full Dialogue Interface as "the most popular FO4 mod"; its download rank | `[SECONDARY, weak]`; `[UNVERIFIED download rank]` (`reception/fallout-4.md`) | NDA-01 strength (the eight-day date is primary, so the verdict holds) | Nexus endorsement and download data |
| Another Life's 104,757 unique downloads | `[SNIPPET]`, snapshot date unknown (`community/mods-as-design-feedback.md`) | MH-12, NDA-03 revealed preference | Nexus page |
| Sim Settlements as PC Gamer's Best Mod of 2017 | Snippet-only | CM-04 | PC Gamer article |
| Cost of ending slides | No sourced figure (`design-insights/production-metrics.md` §9); "a painting and a paragraph" is the analyst's assertion | Section 6, MH-07 cost rating | Measure in our own vertical slice |
| All person-month, lines-per-person-month and points-per-labour figures | `[C]` derived, ±25% (`design-insights/production-metrics.md` §7) | Thesis, MH-33, Section 6 | Not fixable externally; track our own numbers from day one |
| NV's 65,000 lines | `[A: Guinness]` in production-metrics but tagged `[UNVERIFIED]` in `gameplay/systems-comparison.md` §10; the three games' line counts come from different counters | MH-33 ratio | Guinness entry text |
| NV's gunplay being better balanced than FO3's | Forum consensus `[UNVERIFIED]` (`gameplay/systems-comparison.md` §22.4) | Matrix "Combat feel" (NV ●●) | Contemporary reviews |
| FO4 VATS damage reduction; whether Survival raises player damage | `[UNVERIFIED]` (§22.5, §23.1) | CM-02, NDA-17 context | fallout.wiki game settings |
| No headline complaint about FO4 removing durability | `[UNVERIFIED]`, no review piece retrieved (§24.3) | CM-03 "against" case | Review sweep |
| Radio repetition player reports; DJ timing and pick logic | `[SNIPPET]`; timing assumptions `[UNVERIFIED]`; the song formula is the file's own model (`audio/ambient-radio-pacing-and-foley.md` §3.3-3.5) | NDA-25 song budget | Listening logs from our own playtests |
| Shamus Young's decay critique; the "unswept ruins" player threads | Search excerpt or snippet-only in `art/art-direction.md` §5.2 (the fuller summary in `reception/fallout-3.md` is better sourced) | NDA-23 | Read the full series |
| Fan wish list (choice and consequence, fewer radiants, survival options) and "most beloved" rows | `[CONSENSUS - NOT RE-VERIFIED]` (`community/fan-sentiment.md`) | Background support for several MH items | Re-check against r/Fallout, r/fnv, NMA and Codex lists |
| Polls ranking NV first | Self-selecting Reddit samples; the Windows Central details are `[UNVERIFIED]` | Thesis (esteem tracks reactivity) | Treat as directional only; corroborated by Steam ~95% positive |
| NV mixed-reputation title names; FO3 pacifist run "not practical" | `[UNVERIFIED]` (`gameplay/systems-comparison.md` §11, §15) | NDA-05 replacement, matrix cells | fallout.wiki pages |
| Pagliarulo's "not every Fallout fan wants a turn-based isometric game" | `[UNVERIFIED exact quotes]` (§22.3) | CM-01 context only | Original Play.tm or GameTap interview |
| The TV show's success being due to the tonal contrast | `[UNVERIFIED causal link]` (`gameplay/design-principles.md` §5.5) | MH-26 (supporting only) | None needed; MH-26 stands on design grounds |
| Bethesda acknowledging the radiant-quest problem | Not found (absence of evidence) (`design-insights/bethesda-dialogue-postmortems.md`) | NDA-06 (verdict rests on fans and mods, not on an admission) | Keep searching; do not claim an admission |
| Companion counts for FO3 and FO4 | `[UNVERIFIED]` in §12 | Matrix only | fallout.wiki |
| Sawyer positions as relayed in `design-insights/designer-lessons.md` | Tagged `[UNVERIFIED]` there; that file is being rewritten | Not used; Sawyer claims here come from the separately sourced Sawyer file | Reconcile once the rewrite lands |
