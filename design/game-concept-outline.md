# Above the Line: Game Concept Outline

*Working title.* Version 0.1, 10 Nov 2026. First unified design document for our original post-apocalyptic RPG.
It is audited against `design/post-mortem-matrix.md` (v1). IDs in brackets (MH-xx, NDA-xx, CM-xx) mark the
checklist items that a decision satisfies or resolves. Section 15 is the full audit. Numbers marked *provisional*
are concrete enough to prototype on paper and will be retuned from the vertical slice. Nothing in this document
comes from Fallout or any other existing game, film or book. Where we use a structural device that belongs to the
genre (reputation, ending slides, skill checks, a broadcaster), the matrix says so and we cite it.

---

## 1. One-page pitch

**Working title:** *Above the Line*. In the world, "the line" is the height above which the air is safe to breathe
tonight. It is also the accountant's line, and the game is about debts.

**Logline:** Sixty-six years after the gas a nation buried under its own feet came back up and drowned its
lowlands in their sleep, you climb off a dead caravan holding a strongbox full of other people's debts. Every
power in the valley wants the box, and some of them want you dead.

**The fantasy in one sentence:** You go down where the air is heavy, reading it by three small flames on a pole,
and you come back up owing, or owed.

**Design pillars**

| # | Pillar | What it means in play | Matrix |
|---|---|---|---|
| 1 | **The world keeps the ledger** | Every significant act is recorded and read back by other towns, by the evening broadcast, and by the ending slides. Choices change prices, populations, patrols and who rules. | MH-06, MH-07, MH-09, NDA-07 |
| 2 | **Read the air** | One systemic hazard, the *still* (heavy air that pools and flows), runs through exploration, combat, the economy and the map. Danger is geography and it can be read. | MH-02, MH-20, MH-22, MH-31, MH-33 |
| 3 | **Your words, your build** | Unvoiced protagonist, full-text options, fixed visible checks for every skill and stat, written failure, one stat extreme that rewrites the game's voice. | MH-10, MH-11, MH-12, MH-13, MH-17 |
| 4 | **Every debt has a name** | Factions are arguments about who pays for an inherited harm. Each has a home, an economy and dissenters. Dilemmas are resource conflicts with a named loser. | MH-05, MH-23, MH-24, NDA-12, NDA-13 |
| 5 | **Small, scarce, finished** | A compact, dense valley; scarcity defended by systems; a hard power budget; one expensive pillar; stable at launch. | MH-01, MH-14, MH-21, MH-32, MH-33 |

**What the game is NOT**
- Not an open-world sandbox. Five hubs in one basin, joined by an overland layer (CM-08).
- Not a shooter. Combat is fast turn-based tactics (CM-01).
- Not a base-builder or survival-crafter. One authored base; needs meters live only in the optional ruleset (CM-04, CM-05).
- Not a mutant, zombie or monster game. Every creature is a real animal whose behaviour has changed.
- Not a comedy and not misery tourism. Dry, sincere, humane (MH-25, NDA-21).
- Not voiced for the player, not cinematic, not online.

**Target**

| Item | Decision |
|---|---|
| Platform | PC (Windows, Linux; Steam Deck verified). Console ports only after a stable PC launch. |
| Presentation | Simple 3D on a fixed three-quarter overhead camera, four-step rotation, cutaway floors. Low-poly, painted textures. 3D rather than 2D sprites because the premise is vertical and heights must read. |
| Session length | 45-90 minutes. Natural breaks every 15-25 minutes (an overland leg, the dusk bell). |
| Total length | Main path 18-22 hours; typical first run 30; completionist about 40. |

**The one expensive pillar (MH-33):** the still. A deterministic, readable heavy-air system that flows through
every region map and every fight, is forecast on the broadcast, and can be used as a tool or a weapon. It is the
identity of the game and the one place we spend engineering and level-design money beyond the norm.

**Deliberately cheap:** voice (about 3,500 NPC lines, protagonist silent), cinematics (none; painted slides
only), world scale (five hubs), building (eight authored base slots), animation (no facial animation; portraits
plus text), procedural content (road situations only, never quests), multiplayer (none). Section 14 gives the
cut list.

---

## 2. Premise and world

### 2.1 What ended the old world

The old country solved its emissions problem by burying it. For forty years a national body, **the Keeping
Authority** ("the Keeping"), compressed carbon dioxide from every power station and cement works and pumped it
two kilometres down into old gas fields and saline rock under the nation's lowland basins. Each storage field was
called a **Crown** after the dome of caprock that sealed it. The Keeping's promise was printed on every
certificate: *Kept deep. Kept safe. Kept for good.* People called the stored gas "the nation's breath", without
irony.

Above the storage fields the Keeping built **Lift Towns**: concrete service cores with steel space-frame decks
and plug-in housing capsules, raised twelve metres above ground so the land beneath could be "given back" as
wetland reserve. The two programmes were one idea: put the problem below, live above, let the ground heal.

Then injection pressure triggered a swarm of small earthquakes under the Wend Basin's Crown. The caprock cracked.
Gas came up through old wells, faults and mine shafts. Carbon dioxide is half again as heavy as air: on calm
nights it ran downhill like water and pooled in every hollow, street and cellar. On the **First Still** a
winter night with no wind, it drowned the lowland towns of the Wend in their beds. Releases continued for three
years (**the Exhale**). Other Crowns in the old country failed under the shifted pressure. Groundwater turned
acid, crops failed, the state lost the lowlands and then lost itself. What happened beyond the old country is
out of scope and nobody in the basin knows.

**Why this cause and not a war.** It generates the game rather than only the backstory:
- *Hazard:* gas that pools by height and weather (the still), acid groundwater (sour water), venting ground
  (breathers). Section 2.6.
- *Gameplay:* height, posture, wind and time of day become tactical variables; doors and caps become weapons;
  the lowland's old-world goods are unlooted because the still guards them; the rising line is the slow clock.
- *Visual identity:* everything alive is lifted; white dead trees ring the vents; painted "air-marks" record the
  height of the gas on every lowland wall; flames are carried at measured heights. Section 11.
- *Theme:* deferred harm, and who inherits it. Section 2.4.

### 2.2 How long ago

**Year 66 After the Still.** Fixed in the setting bible (MH-03). Sixty-six years puts the world at its third
generation. The last people who remember the old country are in their seventies and eighties; one of them is a
quest-giver. Concrete cores still stand; timber houses in the lowland have collapsed; plastics have crumbled;
willow and alder forest has closed over the lowland streets. Interiors in the Lift Towns are enterable; lowland
houses are mostly landscape. The table in 2.8 fixes what has rotted, regrown, been looted, cleaned and rebuilt.

### 2.3 The present-day society

This is a **post-post-apocalypse**: currencies, guilds, a religion, a labour dispute, a debt market. We choose
it over an earlier "scavenger" phase for three reasons.
1. The research says players reject implausible stagnation (NDA-23, MH-03). After 66 years a settled economy is
   the plausible state.
2. Our theme is inheritance: people living with obligations they did not make. That needs institutions that
   record and enforce obligations.
3. Living institutions supply living stakes for every quest (MH-04) and factions with material bases (MH-23).

About 4,000 people live in the basin, almost all on the rim, the Edge and the Brow, above the still. Lowland
farming happens by day ("day-farming"): people walk down at dawn and climb back before dusk. The lime-burning
guild on the escarpment issues the currency (tallies, 9.1) and holds most of the valley's debts. The single
political fact everyone agrees on: **the line is rising.** Air-marks painted ten years ago are a metre below
this year's. The Crown is still pressurising. Within a lifetime the rim towns will drown too, unless the Crown
is relieved somewhere. Where it vents decides who loses their home. That question is the main plot.

### 2.4 The central thematic question and the ironic engine

**Thematic question:** *When the dead leave a debt, who pays it, and is it ever paid?*

Every faction answers it differently (Section 4), every currency token is a debt record, the hero's first object
is a box of debts, and every ending is an answer.

**Ironic engine (MH-26).** The old world's sincere belief: **harm can be kept**, stored safely out of sight,
certified, settled. It is drawn from planned, civic, late-modernist optimism, not mid-century consumer
America. The world never knows it is funny. The contrast appears in four channels:

| Channel | Old-world expression | How the present uses it, sincerely |
|---|---|---|
| Figure | **The Steward**: a faceless pictogram figure in a circle, shown only performing actions (sealing a cap, planting a sapling, carrying a child up a stair). It never smiles, never gestures approval. | Revered as a near-saint by the Stewardry; painted over doors as a blessing; our perk and skill illustrations are drawn in its pictogram system. |
| Interface | **Form K field ledgers**: the Keeping's printed survey forms with "Balance carried forward" boxes and a SETTLED stamp. | The player's whole UI is a K-series ledger filled in by hand (11.6). Quests close with the SETTLED stamp. |
| Propaganda and advertising | Posters and enamel plates: "Your breath, kept deep." "The ground is grateful." "Every tonne tucked in." Offset seals on goods: "Balanced by the Keeping." | Plates are salvaged as roofing and shrine panels; children learn letters from them. |
| Technology | Wellhead caps, monitoring masts, the Lift Towns ("giving the ground back"). | The caps are shrines, the masts are homes, the Lift Towns are the only reason anyone lived. |

### 2.5 The region: the Wend Basin

A bowl roughly 30 km across. The river **Wend** enters from the east over the **White Edge**, a limestone
escarpment, crosses a broad lowland (**the Low**) and leaves west through an estuary (out of scope). North-west,
a volcanic plateau (**the Brow**) carries old crater lakes (**the Eyes**). South, an isolated hill carries the
Keeping's compressor station. The storage field, the **Crown**, sits under the centre of the bowl. Because the
still flows downhill, **danger rises toward the centre**: the rim is safe, the Low is dangerous at night, the
Crown is lethal at almost any hour.

Real-world landscape type: a temperate sedimentary river basin with old gas fields, ringed by a chalk or
limestone escarpment and a maar-lake volcanic plateau (the kind of country where natural carbon dioxide springs
already occur). Temperate and wet on purpose: not desert, not snow, not a green city.

### 2.6 The signature hazard: the still

**What it is.** Pooled carbon dioxide. Invisible, odourless at these concentrations, heavier than air. Locals
call it *the still* ("there's still in the cellar"), vents are *breathers*, the safe height in a place tonight is
*the line*, and painted height records are *air-marks*.

**Rules (deterministic, readable):**
- The still flows to lower ground and pools. Wind clears it; calm, cold nights deepen it. Walls and closed doors
  hold it; opening a door lets it pour through.
- It is measured in 0.5 m layers (0 to 4). Your head height decides whether you are *under*: standing heads go
  under at layer 4 (1.5 m and up), crouched at layer 3, prone or unconscious at layer 1. **Sneaking puts your head
  closer to it.**
- Under the still you spend breath: one breath per combat turn (or per 10 seconds out of combat). Breath-hold is
  2 + Breath attribute turns. At zero you are *gasping* (half AP, 5 damage a turn); two turns later
  *unconscious*; three turns after that, dead. The still knocks out before it kills, which makes it a non-lethal
  tool if you pull people out (8.6).
- **Detection is physical.** Flames dim and die in it (the sounding staff, 11.6). Insects go silent and drop.
  Low-nesting birds are absent. Breathers carry columns of midges drawn by the gas. Dead patches of white trees
  ring strong vents. Ure herds climb to high ground before the line rises.
- Daily cycle: day (wind) mostly clear; dusk rising; night pooled in all low ground; dawn white ground-mist where
  fresh gas vents. Every hub rings a dusk bell.

**Secondary hazards from the same cause.** *Sour water*: groundwater turned acid by dissolved gas, leaching metal.
Drinking it gives the *Sour* condition (Breath reduced by one until treated with lime or physic). *Breathers*:
vents that pulse; capping one diverts the gas somewhere else.

**Why it is not radiation by another name.** Radiation in the genre is an invisible cumulative dose fixed to a
place, read by a counter, eroding maximum health. The still is acute, fluid and moving; it depends on height,
posture, hour and wind; it can be moved, released and weaponised; it is read by flames and by silence; and it
leaves no dose meter. Masks do not help against it (you cannot filter out suffocation), so **there are no gas
masks or filter timers anywhere in the game**. The counters are height, wind, breath and time.

### 2.7 One root

Every major element grows from the same idea: *a harm stored below comes back up, and someone must pay.*

| Element | How it comes from the root |
|---|---|
| Cause | Buried carbon, released |
| Hazard | The still rising from below; the line climbing year by year |
| Currency | Tallies: split clay debt tokens backed by lime, the substance that sweetens sour water (9.1) |
| Factions | Four answers to "who pays": the creditor, the debtor, the keeper, the engineer (Section 4) |
| Hook | A strongbox of the lowland's debts (4.6) |
| Art | Life lifted above the line; the old world's raised towns built to "give the ground back" (Section 11) |
| Music | Everything in the score is moved by air: bellows, breath, reeds (Section 12) |
| Broadcaster | The evening line report: the height of the debt, read aloud every night (12.2) |
| Interface | The Keeping's own ledger forms, stamped SETTLED (11.6) |
| Endings | Where the Crown vents, and who loses their home (Section 13) |

### 2.8 Sixty-six years: what has happened to things (MH-03, NDA-23)

| Material or place | State in Year 66 | Visible as |
|---|---|---|
| Timber houses in the Low | Collapsed (50+ years wet) | Chimney stacks and foundations under willow |
| Lift Town concrete cores | Standing, spalled, rust-bled | Inhabited; patched with lime render |
| Steel space-frame decks | Corroded; some bays down | Missing bays bridged with timber and rope |
| Asphalt | Broken; trees through it | Lowland roads are forest tracks |
| Glass | Mostly broken; intact panes valuable | Glazing is a status sign in hubs |
| Plastics | Brittle, crumbled | Coloured fragments in soil; nothing usable |
| Electronics and batteries | Dead | Salvaged for copper and parts only |
| Packaged food | Gone | Nobody eats old food. Ever. |
| Bodies | Gone where scavengers reach; partly preserved in deep still, where there are no insects and little oxygen | Remains only in the Crown and deep cellars |
| Old-world goods | Looted above the line for 66 years; **unlooted below it**, because the still guards them | Salvage diving is a trade |
| Settlement paths and walls | Swept, whitewashed, repaired with dated stair-treads | Labour shows everywhere people live |
| New building | Timber, rope, lime mortar, hung off old frames | Pale new wood against black concrete |

---

## 3. World structure

### 3.1 Map model (CM-08, CM-09)

A hybrid, as the matrix recommends: **five compact, hand-built, seamless hub regions plus two non-hub regions**,
joined by an **overland chart** drawn on the player's ledger.
- **Region maps** are dense, walkable, one seamless space each (no internal loading cells, NDA-20). Vertical
  floors are cutaways, not loads. Each region is about 600 x 600 m of authored ground, plus its verticality.
- **The overland chart** is a node map of the basin. Travel is instant in real time but costs in-game hours,
  tallow and (in the optional ruleset) food and water, and can trigger road situations. Inside a region, travel
  between discovered points is free. Overland travel *is* the fast travel; it is never a paid convenience (CM-09).
- Each overland leg has a **rim road** (long, safe) and often a **low road** (half the hours, higher danger band,
  spill risk at night). The player trades time against risk on every leg.

### 3.2 Regions and hubs

**Ladderfoot (starting hub; neutral).** About 400 people living in storeys 6 to 14 of **Lift Town 4**, a 40-storey
core-and-capsule frame at the foot of the White Edge where the Wend leaves the escarpment. The old ground floors are
dead; air-marks on the stairwells climb to 9.2 m. Bucket-lifts and ladders run up the Edge to Quicken. Here live the
**Sounders' Lodge** (guides who read the still for hire), a salvage market fed by the Divers, and **Fourtop**, the
valley's one broadcaster, on the roof. Tenants want height; the upper floors belong to the Kiln Houses and are let
at rents the lower tenants cannot pay. What is wrong: the line rose 1.2 m in a decade, and calm nights now reach
storey 7. Connections: up the Edge to Quicken; down the river path to Reedhithe; Lodge guides everywhere; Mast 31,
the player's base (9.7), a short walk along the rim.

**Quicken (Kiln Houses).** About 1,200 people on terraces cut into the White Edge: rows of bottle kilns, quarry
faces, coppice woods for charcoal, and the stone **Counting House** where the counterfoils of every tally are kept.
Everything is lime-white and soot-black. The Edge's limestone springs are the only naturally sweet water in the
basin, which is the root of Quicken's wealth. The Kilns want the lowland debt box back: they sold it, the buyer
never received it, and both claim it. What is wrong: the kilns are running out of charcoal, so fewer tallies are
issued and money is getting scarce everywhere; bonded debtors ("slakers") work the quarries to pay debts they
inherited; lime dust is in everyone's lungs. Connections: lime and tallies to every hub; buys grain and willow
charcoal from Reedhithe.

**Reedhithe (the Lowmoot).** About 900 people in three stilted villages in the willow carr along the Wend, on old
bridge piers and stilts, linked by plank walks at 5 to 6 m. Sail-driven **air-mills** turn wooden fans across the
day-fields to keep them breathable. It is the most beautiful place in the game and the most dangerous to sleep in.
The richest soil in the basin is here, fattened by the gas, and it feeds everyone. The Lowmoot wants inherited debt
cancelled (the Clean Slate), the Draught's relief wells kept shut, and to stay. What is wrong: lime prices are up,
the fields are souring, and the dead caravan's guide was one of theirs. Connections: grain to Quicken and
Ladderfoot; willow charcoal to the kilns; the relief wells sit in its fields; the Drowned Towns begin downstream.

**Capstone (the Stewardry).** About 300 people plus pilgrims in a cloister built around a capped wellhead on the
Brow, above the crater lakes. The cap is a concrete disc 30 m across, painted with Steward pictograms. The Stewards
keep the valley's longest air-mark records, seal small breathers with clay, and hold one of the three keys to the
Keeping's control station. They want the ground kept closed forever. What is wrong: sealing does not destroy gas, it
diverts it, and their caps on the Brow have been pushing still into Reedhithe's fields; their doctrine forbids
admitting that the Keeping itself planned to vent. The largest lake, the Mother Eye, fizzes at its edges.
Connections: sells air-mark data to Fourtop; clay from the Eyes; pilgrim traffic to every hub.

**The Lung (the Draught).** About 500 workers and families in the Keeping's old compressor station on Lung Hill,
south of the Low: manifolds, pressure vessels, gauges, and the basin's only working engines, driven by vent gas. The
Draught pumps sweet water from deep wells, grows tomatoes in gas-fed glasshouses all year, and builds air rifles,
air bladders and bottled still. It wants to relieve the Crown through the relief wells into the Low, under its own
control, and it holds the second key. What is wrong: its chief engineer's night test of Well 9 killed the caravan;
its workers are close to a strike; it sells bottled still to people who use it on caravans. Connections: water and
engines to Ladderfoot and Quicken; buys lime; its approach crosses the vent fields.

**The Drowned Towns (non-hub region).** Old Wendmouth and its suburbs, between Reedhithe and the Crown: an old-world
town under 30 m willow forest, dead below the line and full of unlooted goods. Diver camps sit on the rooftops.
Danger is graded by depth: the edge is safe by day, the centre lethal after dusk. The Keeping's district office here
holds the evidence for the High Vent (6.10). Connections: salvage to Ladderfoot; pipe for the High Vent; Divers
everywhere.

**The Crown (non-hub region; endgame).** The storage field at the bottom of the bowl: wellheads with green enamel
pictograms, manifold runs, a white forest of dead trees, no insects, no birds, and the **Listening House**, the
Keeping's control station, on a raised podium. The densest still in the game. Draught crews work it in shifts; ure
herds graze its upper rim at midday. Everything flows here, literally.

### 3.3 Every settlement answers five questions (MH-03)

| Hub | Water | Food | Trade | Protection | Why here |
|---|---|---|---|---|---|
| Ladderfoot | Roof cisterns; river water sweetened in lime tanks on storey 6 | Terrace day-fields below; Reedhithe grain | Lodge guide fees, salvage market, Fourtop's sponsor reads | The Watch (paid by market levy) and Lodge sounders | The only standing frame at the river crossing, and the bucket-lifts up the Edge |
| Quicken | Limestone springs (naturally sweet) | Upland sheep, terrace barley, bought grain | Lime and tallies | Kiln collectors; terrace walls | The stone and the springs |
| Reedhithe | Rain barrels; lime-treated river water | Day-fields (beans, barley), feral orchards, eels | Grain, eels, willow charcoal, baskets | Night ropes (a watch on the walks) and the still itself: raiders cannot come at night | The best soil; the families refuse to leave |
| Capstone | Rain catch; lime bought from Quicken | Goats, heather honey, upper-layer lake fish, pilgrims' gifts | Air-mark records, sealing work, pilgrimage | Sanctity (no weapons drawn on the rim) and hired Lodge guards | The great cap, "the first seal" |
| The Lung | Deep wells pumped by gas engines | Gas-fed glasshouses; bought grain | Pumps, air bladders, air rifles, sweet water, bottled still | The Draught Guard in pressure-plate armour | The machinery and the vents that drive it |

Each answer is a placed asset that an artist can point to in review: cistern, terrace, stall, guard post.

### 3.4 Soft gating and the intended first route (MH-02, NDA-20)

Map edges are honest: the White Edge cliffs, the Brow's lava scarps, the estuary marsh. No invisible walls.

| Region | Danger band (1-5) | Soft gate | Intended level |
|---|---|---|---|
| Ladderfoot and terraces | 1 | None | 1-3 |
| Reedhithe | 1-2 (3 at night) | Still nights; longshanks packs at dusk | 2-5 |
| Quicken | 1-2 | Collectors, if you are in debt | 3-6 |
| Capstone and the Eyes | 2-3 | Breather fields; papermaker nests in the frames | 5-8 |
| The Lung approach | 3 | Draught Guard (armour threshold 8: standard ammunition barely works) | 6-10 |
| Drowned Towns | 2 at the edge to 4 at the centre | Depth of still; Drowners | 7-11 |
| The Crown | 4-5 | Deep still at all hours; ure bulls on the rim; Pressure Guard | 10-14 |

**Intended first route:** Ladderfoot, Reedhithe, Quicken, Capstone, the Lung, the Drowned Towns, the Crown. It is a
**soft loop around the rim** with the Low in the middle, so designers can predict the likely order (design-principles
§6, chain 1) while any build can break sequence. A sneaking talker can reach the Lung at level 2 under safe-conduct;
a reckless player can walk into the Low at dusk and learn why nobody does.

**Signposting before contact (MH-02):** corpses and dead birds in hollows; mourner flocks circling a fresh still;
dated air-marks; locals' warnings; ure herds moving uphill; the insect bed going silent; midge columns over
breathers. **Landmarks:** from any outdoor point you can see at least three of the kiln smoke on the White Edge,
Lift Town 4, the Lung's stacks, the Capstone mast, and the white forest and Keeping mast at the Crown.

### 3.5 Travel and encounters (NDA-06)

- **Legs** take 2 to 8 in-game hours and cost one tallow fill per four hours for the sounding staff; the low road
  at night costs double and risks a spill.
- **Situations, not quests.** A road-situation generator picks from 30 templates (patrol clash, Diver salvage
  party, day-farmers caught by dusk, longshanks hunt, a spill across the road, a collector serving a writ, a
  pilgrim column). Inputs: region band, hour, current line, wind, reputation (high Grudge draws hunters). About one
  situation every two legs. A Sounding check on departure (rank 4 or 6, by leg) reads the route and avoids one.
- **12 unique authored road encounters**, each met once. The *Tall Tales* trait adds 6 odd ones (6.4).
- Generated situations never carry a quest-giver or a journal entry. Repeatable bounty and haul jobs exist only on
  opt-in boards (9.2).

### 3.6 How the world changes: the state model (MH-06, NDA-07)

Each hub carries a small set of tracked states, each visible somewhere in the world:

| State | Values | Seen as |
|---|---|---|
| Population | 4 bands | Occupied capsules or stilts; stalls open; crowd density |
| Prosperity | 3 bands | Price index; whitewash, glazing, fresh rope |
| Ruling power | Which faction holds it | Banners, guards, who staffs the gate |
| Local line | Global act height plus local modifiers (capped breathers nearby, fans built, wells opened) | Air-marks repainted; floors abandoned or reoccupied |
| Stake clock | 0-4 steps (5.4) | A named decline: a field abandoned, a village emptied |
| Named outcome flags | 4-8 per hub, one per significant quest result | Specific people, buildings, patrols, prices |
| Reputation | Regard and Grudge per community (4.5) | Greetings, prices, access, hunters |

**Hubs read each other** through named outcome flags. Every hub has at least one outbound edge. The complete flag
graph is a pre-production deliverable (MH-06 audit); its spine:

| Source (quest) | Read by | Effect |
|---|---|---|
| Ladderfoot, *Nine Metres* | Reedhithe, Quicken | Evicted tenants arrive in Reedhithe and swell the radicals; a legal win becomes the "Ladderfoot Ruling" cited in Quicken (6.9) |
| Quicken, *Cold Kilns* (charcoal shortage) | All hubs | Tally supply: vendors' cash reserves +/-30% valley-wide; Reedhithe's charcoal income; a Draught gas-burner contract |
| Reedhithe, *Sour Fields* | Ladderfoot, Quicken | Grain prices in both; whether Reedhithe's south village survives |
| Capstone, *The Quiet Caps* | Reedhithe | Exposing the diversion stops the souring of Reedhithe's north fields and starts a Steward schism |
| The Lung, *Pressure Wages* (strike) | Ladderfoot, Quicken, main quest | Engine output (Ladderfoot's water price, Quicken's burners); Lusk's timetable; access to the Lung key |
| Ladderfoot, *The Reader's Stock* | Every hub | What the evening broadcast says, and how truthfully (12.2) |

Before the ending, every major quest changes at least one visible thing: a population, a price, a building, a patrol
or a broadcast (NDA-07).

### 3.7 Density targets, sized to the team (MH-01)

| Target | Value |
|---|---|
| Walking time between new authored points of interest on the critical path | 90 seconds or less, measured in the slice |
| Points of interest per hub region | 14-20, each with a written one-line answer to "what happened here?" |
| Minor overland sites (one-screen maps) | 18 |
| Named NPCs | About 150 (25-40 per hub), plus about 60 generic types |
| Bespoke region encounters (combat or hazard set pieces) | 45 |

Example one-liners. *The Hanging Laundry*: a capsule family dried clothes on a line they did not take in the night
the still rose, and the clothes are still there. *Pask's Turn*: where the caravan left the rim road, and the guide's
chalk mark that sent it there.

---

## 4. Factions

Four major, joinable factions, each with a walkable home hub, civilians and a six-quest line, and two minor factions
whose arcs are read three times (MH-06, MH-23). Each major faction is one answer to the thematic question. If a
faction cannot be funded to this standard it is cut whole, never starved (MH-23); the cut order is in 14.4.

| Faction | Home | Answer to "who pays?" | Material basis on screen |
|---|---|---|---|
| **Kiln Houses** | Quicken | The debtor, and the debtor's heirs. A debt recorded is a debt owed. | Kilns, quarries, springs, the Counting House, the tally currency |
| **The Lowmoot** | Reedhithe | Nobody alive. Cancel what the dead owed and start clean. | Day-fields, air-mills, grain lifts, eel weirs |
| **The Stewardry** | Capstone | The ground is owed patience. Keep it closed and pay by watching. | The cap, clay works, air-mark archive, pilgrims |
| **The Draught** | The Lung | Whoever is cheapest to move. Vent it now, where it costs least. | Engines, wells, glasshouses, workshops |
| Sounders' Lodge (minor) | Ladderfoot | Whoever hires us. | Guide fees, the Lodge hall, route chalk |
| The Divers (minor) | Drowned Towns rooftops | The dead. Their goods belong to the living. | Salvage rafts, rope rigs, the market at Ladderfoot |

### 4.1 Kiln Houses

- **Their case:** Before the tallies there were the hungry years, when anyone who had food kept it with a knife.
  A token that any stranger will honour let strangers trade, let towns plan a harvest ahead, let a widow borrow
  seed. Records are the only thing in this valley that remembers fairly. Break them and you get the knife back.
- **The fact that most damages it:** Children inherit their parents' debts. A third of the quarry workers are
  slakers paying debts they were born into, and the Kilns sold the lowland's debts to the Draught knowing what the
  Draught planned to do with the land.
- **Right about:** Honest records protect the weak as often as the strong; land boundaries and water shares are
  tally records too. **Wrong about:** that an inherited debt is a fair debt.
- **Leader:** Reckoner Maud Calloway. **Dissenters:** Bertil Ashe, a kiln-master who wants slakers' debts capped at
  one generation; Juno Teague, a clerk forging counterfoils to free children; Tamsin Pye, a quarry foreman who wants
  to buy Draught gas-burners and end the charcoal crisis.
- **Questline (6):** includes *Cold Kilns*, *The Slakers' Ledger*, and a quest that shows the case in play: a family
  saved from eviction because the Counting House kept a record the family itself had lost (NDA-13).
- **Binding deed:** *Calling In*. Enforce a foreclosure on a named Reedhithe family (the Haskets), or collect the
  broadcaster's debt. **Joining costs:** Lowmoot Grudge; Sefa leaves the party (6.8); Reedhithe's prices rise for you.

### 4.2 The Lowmoot

- **Their case:** We feed the valley. The Kilns' lime and the Draught's water would be worth nothing to people
  who were starving. Our great-grandparents did not sign for the dead's debts and neither did we. A debt that
  can never be paid is not a debt, it is ownership.
- **Damaging fact:** The caravan was killed partly by one of their own. Teo Marl, a Lodge guide and Clean Slate
  sympathiser, steered it into the Well 9 hollow to destroy the box, knowing a test was planned. And they will not
  look at the air-marks: they would rather the whole Low drown than leave it.
- **Right about:** inherited debt is unjust, and their fields are the basin's real wealth. **Wrong about:** burning
  every record (including the ones that protect them), and denial of the rising line.
- **Leader:** Speaker Elsa Fenwick of the Moot. **Dissenters:** Wenna Hask, an elder who would accept the Kilns'
  terms to save this harvest; Coll Brake, who believes the air-marks and wants to move the villages up to the rim;
  Pim Ollerton, who opposes the Clean Slate's violence.
- **Questline (6):** includes *Sour Fields*, *The Night Ropes*, and a quest showing the case in play: the grain lift
  that feeds Ladderfoot, worked by people who walk down into the Low every dawn.
- **Binding deed:** *Burn the Stocks*. Burn the Ladderfoot tally-house counterfoils, or the box if you hold it.
  **Joining costs:** Kiln Grudge (collectors hunt you); prices in Ladderfoot jump 25% because its money is now
  doubtful; Hollis leaves (6.8).

### 4.3 The Stewardry

- **Their case:** The Keeping meant well and did one thing right: it kept the gas down for forty years. Every cap
  we keep is a village that sleeps safe. Venting is murder by another route. We have the records, and we are the
  only ones who still know the old procedures by heart.
- **Damaging fact:** Their caps divert gas into Reedhithe's fields. And the Stewardry's own sealed archive contains
  the Keeping's contingency plan to vent the Crown at height (the High Vent). Mother Isaura Venn has read it and
  keeps it sealed because it contradicts the doctrine.
- **Right about:** some seals can be maintained; their observations are the best data in the valley; their rote
  procedures work. **Wrong about:** that the Crown can be kept closed forever.
- **Leader:** Mother Isaura Venn. **Dissenters:** Brother Ammon Pell (companion, 6.8), who doubts the doctrine;
  Steward Cato Lisle, who wants the Stewardry to operate the Listening House itself; Novice Bree Hollin, who wants the
  archive opened to everyone.
- **Questline (6):** includes *The Quiet Caps*, *The Long Hold* (a breath ordeal), and a quest showing the case in
  play: a cap the Stewards maintain saves a pilgrim camp during a breather surge.
- **Binding deed:** *The Vow and the Seal*. Take the vow and cap Well 9 with clay at night. **Joining costs:**
  Draught Grudge; the vow forbids using the still as a weapon (no bottled still, no opening doors or caps to flood
  enemies) for as long as you are bound. A mechanical cost every fight.

### 4.4 The Draught

- **Their case:** The Crown is filling. Sealing buys years and kills our grandchildren; prayer buys nothing. It has
  to vent somewhere, and the relief wells the Keeping drilled are ready. Our engines pump the only sweet water you
  did not dig yourself. We are the only people in this valley doing arithmetic.
- **Damaging fact:** Chief Engineer Ora Lusk ran the Well 9 test at night without warning anyone, and eleven people
  died. She covered it up and has agents hunting the survivor. Her plan drowns the Low permanently, and Reedhithe
  with it, because the Lowmoot are debtors who cannot resist.
- **Right about:** the Crown must vent; their engineering is real. **Wrong about:** who decides where, and secrecy.
- **Leader:** Chief Engineer Ora Lusk. **Dissenters:** Idris Vane (companion, 6.8), who was on the test crew;
  Foreman Arno Gilt, who prefers the slower High Vent route because it costs no homes; Tessaly Marr, who is
  organising the workers against Lusk's secrecy and hours.
- **Questline (6):** includes *Pressure Wages*, *Glass and Tomatoes*, and a quest showing the case in play: Draught
  engines restore sweet water to a Ladderfoot cistern during a drought.
- **Binding deed:** *Quiet on Fourtop*. Buy the broadcaster's debt for the Draught or cut Fourtop's relay so news of
  Well 9 stops spreading. **Joining costs:** Stewardry Grudge; the broadcast turns to Draught propaganda or goes
  silent (12.2); Ammon leaves.

### 4.5 Minor factions (read three times, MH-06)

| | Sounders' Lodge | The Divers |
|---|---|---|
| Ideology | The Low belongs to whoever can read it. Neutral, for hire. | The dead do not need their things. Salvage is honest work; drowners give it a bad name. |
| Right about | Knowledge of the still is the valley's real safety net | Old-world goods keep the living alive |
| Wrong about | Neutrality: they guided the caravan to its death and say nothing | They sell to anyone; some crews drive caravans into stills and loot them |
| Joining cost | Lodge oath: you may not refuse a rescue call (some calls arrive at bad moments) | Divers' share: a third of all salvage you take in the Drowned Towns |
| Read 1: employer | Lodgemaster Sim Agard's jobs | Captain Rue Malley's jobs |
| Read 2: finale | Lodge sounders will or will not guide you down to the Crown | Divers supply High Vent pipe, sell it to the Draught, or ambush the crews |
| Read 3: epilogue | Own slide | Own slide |

### 4.6 The strongbox (the shared object)

The caravan carried the **stocks** (the creditor halves) of the lowland's debts, which the Kilns had sold to the
Draught. Whoever holds them owns Reedhithe on paper. All four factions want it: the Kilns to reclaim it, the
Draught for legal title to the land its wells would drown, the Lowmoot to burn it, the Stewardry to seal it in the
cap where nobody can ever collect or be freed. The player can keep it (title: *Stockholder*). If the player leaves
it in the wagon, the Diver Kett takes it and the Divers sell it to the Draught in Act 1; it can be stolen back. Its
fate is an ending axis (Section 13).

### 4.7 Lockouts, warnings and the amnesty (NDA-12, MH-08)

- **Act 1:** small jobs for anyone. Dialogue reacts to dual loyalties from the first job ("You were in Quicken
  Tuesday. Who paid you?").
- **Act 2, binding deeds:** taking a faction's binding deed is the lock point. The option is labelled in full text
  with what it closes (*"This will end your standing with the Lowmoot."*), the faction's own NPC says so in fiction,
  and the ledger stamps the closed page CLOSED with one line naming what was lost. No late scripted lockout.
- **One amnesty:** once per game, after a binding, the Lodge can broker a reversal at the Ladderfoot Moot: Regard with
  the bound faction resets to zero, Grudge stays, and it costs 1,000 tallies.
- **Outcomes are never only destruction.** Truce, absorption, coup (dissenters take over), exile and reform are all
  authored for each faction. Destroying a faction is possible and has a price on every slide.

### 4.8 Reputation model (NDA-05)

- Per community (the four factions, Ladderfoot, the Lodge, the Divers): two tracks, **Regard** and **Grudge**, 0-100
  each, which never cancel. Acts count only if witnessed by a member or traced (a body found in their territory the
  same day you were seen there).
- Standing labels come from the pair: *Unknown, Known, Liked, Trusted* by Regard; *Disliked, Feared, Hated, Hunted* by
  Grudge; combined labels where both are high (*Dangerous Friend*, *Necessary Evil*). Labels change prices (+/-20%),
  access, dialogue options and hunters.
- **Titles** (earned, each with a trade-off; no global morality meter anywhere):

| Title | Earned by | Upside | Downside |
|---|---|---|---|
| Survivor of the Eleven | Default | People will talk to you about the caravan | The Draught's agents know your face |
| Stockholder | Holding 3+ people's stocks | Debtors must hear you out; Kilns treat you as a peer | Lowmoot Grudge on sight; theft attempts |
| Slate-Burner | Burning tally records | Free meals in Reedhithe | Collectors' bounty; no Kiln credit |
| Seal-Breaker | Opening a capped well | Draught respect | Capstone closes its gate |
| Collector | Enforcing 3 debts | Debt dialogue options everywhere | Children run from you in the Low |
| Low-Walker | 10 nights spent below the line | Lodge pay +25% | Rim folk think you bring the still with you |

### 4.9 The fail-safe (MH-08)

Every visible adult NPC can be killed, including leaders, companions and the broadcaster. Children are not
killable and are never placed where combat can reach them. The critical path survives a kill-everyone run:
- The three keys are physical objects and can be taken from bodies. The **Diver's way**, a flooded Keeping
  maintenance gallery, reaches the Listening House valve hall from below without keys, through deep still.
- The Listening House's emergency procedures are printed as **pictogram-only cards**: the Keeping designed them so
  anyone could operate a shut-in or a relief. No living expert is needed.
- **The cost:** companions cannot follow the Diver's way; the High Vent ending is unavailable (it needs the labour
  of at least three factions); only the Low Relief, Shut-in, Hold the Valves and Walk Away resolutions remain, and
  their slides are the harshest variants. An automated kill-everyone run must reach an ending (14.5).
- Unique loot is never gated behind murder: every key, document and unique item has a trade, persuasion or theft
  route.

---

## 5. Core gameplay loop

### 5.1 Minute to minute

```
Read the air       staff flames, insect sound, air-marks, wind, hour
  -> Choose height  walk the low path or climb the frame; stand or crouch
    -> Act          talk, search, salvage, sneak, fight (turn-based, still on the grid)
      -> Spend      breath, tallow, ammunition, daylight
        -> Record   the ledger updates; a stamp, a debt, a name
```

### 5.2 Hour to hour

```
Hub (talk, trade, take work)
  -> Prepare (lime, tallow, bladders, ammunition; check the evening line)
    -> Go down by day (region or overland leg: salvage, quest site, evidence)
      -> Dusk bell: climb out, or stay low and pay for it
        -> Return and settle (sell, repair, report, stamp SETTLED)
          -> The broadcast reports what you did; another hub reacts
```

A typical cycle is 40-70 minutes and contains one or two quest beats, one or two fights or hazard set pieces, one
overland leg and one market visit.

### 5.3 Whole game

| Act | Hours | The player is | Ends when |
|---|---|---|---|
| Prologue | 0-0.2 | A survivor on a wagon roof | You walk into Ladderfoot (skippable on replay, NDA-11) |
| 1. Survivor | 0.2-6 | Holding (or chasing) the box; learning the still; being hunted | You decide the box's fate: lock point 1 |
| 2. Witness | 6-15 | Working the factions; finding out what happened at Well 9 | You bind to a faction or refuse all, and hold two keys |
| 3. Settlement | 15-22 | Gathering keys, evidence and allies; going down to the Crown | You choose at the valves |
| Epilogue | | Reading the slides; free play (13.3) | |

### 5.4 The pressure system: the world moves when you move the story (NDA-09)

There is no real-time deadline and no hidden clock. Pressure comes from three visible sources.
1. **The nightly line (hours).** Every day has a dusk. Time of day advances outside combat, dialogue and menus at
   one game hour per four real minutes, so a day is about 96 minutes of play. The dusk bell gives half an hour's
   warning. This is weather, not a deadline.
2. **The rising line (acts).** At each act transition the global line rises 0.5 m in low ground. Air-marks are
   repainted, a few low paths become night-impassable, Ladderfoot's storey 7 empties. Act transitions happen only
   when the player triggers them, with a written warning first ("Lusk will move once she knows you hold two keys").
3. **Stake clocks (hubs).** Each hub has one or two named 4-step clocks shown on the ledger's *Standing Matters*
   page. Each advances one step at an act transition unless its quest is resolved. Example: Reedhithe's *Sour
   Fields*; at step 4 the south village is abandoned, Reedhithe drops a population band and its slide changes. The
   broadcast and a ledger stamp (OVERDUE) announce every step. Exploring inside an act costs nothing.

### 5.5 What the player is always short of

**Daylight, lime and breath.**
- *Daylight* is the safe window in the Low. Salvage, evidence and the best fields are down there; every extra hour
  of searching is an hour closer to dusk and a heavier climb out.
- *Lime* is money (tallies are lime claims), clean water (it sweetens sour water), repair mortar and field dressing.
  Spending it on survival means not spending it on power.
- *Breath* is capacity: bladders are few, breath-hold is short, and the best salvage lies deepest.

Each scarcity forces a choice that is visible to the build: a high-Breath diver, a high-Wits reader who wastes no
time, a Reckoning trader who turns salvage into lime efficiently. Scarcity is defended by systems (weight, sinks,
vendor reserves), not by a difficulty toggle (MH-22).

---

## 6. Role-playing and progression

### 6.1 Attributes

Five attributes, each rated **1 to 5** (pips, not a 1-10 scale). Everyone starts at 3 in each (15 points). At creation
you may lower any attribute to 1 to raise others, to a maximum of 5. Level-ups raise one attribute by one pip at
levels 7 and 13 only. No attribute multiplies XP or skill points (MH-15).

| Attribute | Combat (visible readout) | Hazard and travel | Dialogue and world | Economy | Why it is not a dump stat |
|---|---|---|---|---|---|
| **Frame** (size, strength) | HP 25 + 5 per pip; melee damage +1 per pip above 2; heavy weapons need Frame 4 | Carry 40 kg + 8 per pip (salvage you can haul up) | Force, shove and haul checks; presence options [Frame 4] | More salvage per dive | Low Frame means fragile and poor |
| **Breath** (lungs, endurance) | Push: spend 2 breath for +3 tiles once per turn | Breath-hold 2 + Breath turns; overland legs cost 10% fewer hours per pip above 3; Sour resistance | The Long Hold and climbing contests; endurance options [Breath 4] | Deep salvage | The still is everywhere |
| **Hands** (dexterity) | AP 6 + Hands; reload and item use 1 AP cheaper at 4+ | Climbing costs | Sleight options (palm a token in a dispute) [Hands 4]; some Tinkering checks need Hands 3 | Crafting yield | AP is valuable, but Wits sets hit chance and Nerve sets crits |
| **Wits** (perception, reasoning) | Initiative (which side moves first); hit chance +5 per pip; enemy stats shown at 4+ | Still-reading radius 2 + Wits tiles (exact depths); spill forecasting | Deduction and notice options [Wits 4]; the Plain register at 1 (6.7) | Appraisal hints | Blind to the still and to lies without it |
| **Nerve** (composure, will) | Composure capacity = Nerve (the banked crit resource, 8.3); no panic under the still at 3+ (at 1-2, breath drains double on the first turn under) | Night travel without penalty at 4+ | Intimidate and hold-your-ground options [Nerve 4]; companions allowed: 1 at Nerve 1-2, 2 at 3-4, 3 at 5 | Haggling under pressure | Companions and crits both need it |

Every attribute is read by at least three systems, at least one of them non-combat, and gates dialogue somewhere in
every hub (MH-11, MH-15).

### 6.2 Skills

Eleven skills, ranked **0 to 10**. Checks are set only at 2, 4, 6, 8 and 10, so each threshold means something
(CM-07). Every skill has at least five uses in every hub, tracked by the check-distribution tool (MH-17).

| Skill | World and combat uses | Dialogue use |
|---|---|---|
| **Sounding** | Still depth and flow forecast in combat (1/2/3 rounds ahead at 2/5/8); route reading on overland legs; spill timing | Contradict a guide; Lodge negotiation; air lore that wins a Steward's respect |
| **Shooting** | Air guns, breech-loaders, old cartridge rifles; hit chance | Read a weapon's maker and loader as evidence; threaten credibly; Draught armoury talk |
| **Melee** | Hooks, bills, mauls, hook-poles, unarmed; grapple and non-lethal holds | Accept or decline a Quicken "stick settlement" duel; size up a fighter |
| **Stealth** | Sneak, hide, pickpocket, plant items | Claim you overheard; lie about where you were; notice a watcher |
| **Tinkering** | Repair, craft, locks, traps, valves, pumps | Talk an engineer through a fix; spot a sabotaged valve; argue engine figures |
| **Physic** | Healing rates, poultices, Sour cure, surgery | Diagnose (a still death versus poison: main path evidence); calm the panicked; detect feigned illness |
| **Letters** | Read Keeping forms and documents; forge tallies; operate Keeping control panels | Quote Keeping law or doctrine; read the room's paperwork; cite a document you hold |
| **Persuasion** | | Reason, appeal, deceive. The broadest dialogue skill, never the only route |
| **Reckoning** | Barter margins; appraisal; detect forged tallies | Debt law, leases, loopholes; read accounts as evidence; price a person's debt |
| **Wildcraft** | Forage, track, handle and drive animals (stampede ures, calm longshanks), cook | Talk shop with farmers and herders; Stewardry plant lore |
| **Rigging** | Climbing, rope lines, crossing gaps, structural reading; reach high ground in combat; rope traps | Argue whether a floor or frame will hold; deal with lift crews and riggers |

Money-only functions (gambling, pure haggling) are perks, not skills (CM-07).

### 6.3 Backgrounds (MH-12)

The protagonist is unvoiced and has no fixed family, history or motive. A background is a **social position others
can read**, not a biography. It sets one skill +1, one starting item, how the first hour's NPCs treat you, about 6-10
reactive lines per hub and one unique option per main-path beat.

| Background | Why you were on the caravan | How the world reads you | +1 / item |
|---|---|---|---|
| Bonded | Being moved to the quarries; your own stock is in the box | Kilns: property in arrears. Lowmoot: kin. | Rigging / quarry hammer |
| Hired Hand | Paid guard | A professional; nobody's friend | Shooting / air pistol |
| Lodge Apprentice | You walked with Teo Marl, the guide | Suspected of the diversion until cleared | Sounding / a better staff |
| Pilgrim | Travelling to Capstone | Stewards trust you; the Draught laughs at you | Letters / a Steward plate |
| Tally Clerk | Custodian of the box on paper | Kilns expect delivery; you can claim legal title with the right papers | Reckoning / Kiln seal |
| Stowaway | Hidden in the load, no papers | Nobody knows you survived (the Draught does not hunt you in Act 1), and nobody vouches for you (prices +10%) | Stealth / nothing |

The hook tolerates any motive. The box is the most valuable object in the valley (greed), its contents are people's
lives (conscience), someone tried to kill you (survival or revenge), and every faction will pay or threaten for it
(ambition). A cruel or indifferent character has as many reasons to continue as a kind one.

### 6.4 Traits (MH-16)

Choose up to two at creation. Each pairs an upside with a cost. Target: at least six of nine see real use in
playtests.

| Trait | Upside | Cost |
|---|---|---|
| Long Lungs | +2 breath-hold turns | Healing items heal 25% less (your heart races) |
| Night-Eyed | See 2 tiles further at night without a flame | -10 hit chance in full daylight |
| Heavy-Handed | Melee +3 damage | Aimed attacks cost +1 extra AP |
| Snap Shot | All shots -1 AP | You cannot make aimed attacks |
| Small | Fit crawlspaces (new routes); enemies detect you at 2 tiles less | Your head goes under the still one layer sooner |
| Debtor's Luck | Start with 300 extra tallies | You owe the Kilns 600 from day one; collectors appear in Act 2 |
| Light Sleeper | Never ambushed when camping | Resting heals at half rate |
| Cold Blood | Composure fills one point faster per fight | Companion approval gains halved |
| Tall Tales | Enables rare odd and absurd encounters (the humour fence, NDA-21) | None mechanical |

### 6.5 Perks, levels and the cap (MH-14, MH-16, CM-06)

- **Level cap 14**, fixed now, never raised by later content. A completionist reaches it at about 85-90% of content.
  XP after the cap becomes **Marks**, spent only on horizontal rewards: lore entries, base decoration, ledger tints,
  or moving one skill rank to another skill.
- **Perks at every even level**: seven perks in a full run, from a list of 36. Every perk is tagged verb,
  exception, information or trade-off. No flat percentage perks.
- **Skill ranks:** tagged skills start at 3 (three tags), untagged at 0, background +1, 2 ranks per level-up (26 by
  the cap), and four trainers or manuals in the game (+1 each, expensive). Total about 40 ranks of the 110 needed to
  max every skill: roughly three skills mastered at the cap (ratio 0.36; MH-14 target about 0.33).
- Collectible boosts are scarce: two attribute raises and four skill trainers in the whole game.

Sample perks:

| Perk | Tag | Effect |
|---|---|---|
| Read the Ripple | Information | Exact still depth shown for every tile in sight, not only your reading radius |
| Pull Up | Verb | Drag an unconscious adjacent body out of the still (2 AP) and climb with it |
| Uncork | Verb | Release pooled still deliberately: hook a cellar door or crack a small cap from 3 tiles |
| Collector's Eye | Information | See every NPC's debts; adds "call in a debt" options |
| Bellows Chest | Exception | Breath does not drain on a turn in which you neither move nor act |
| Ladder Work | Exception | Climbing costs 1 AP; no penalty to attack from a ladder |
| Quiet Flame | Trade-off | Your staff does not reveal you at night; tallow burns twice as fast |
| Steady Hands | Trade-off | Composure capacity +1; -2 AP on any turn you moved |
| Bad Debt | Trade-off | Vendors give you up to 500 tallies of credit; miss a due date and collectors come |
| Witness | Information | When you hold relevant evidence, lies against it are flagged in dialogue |
| Ure-Wise | Verb | With Wildcraft 6, steer a stampede's direction |
| Second Wind | Exception | Once per fight, a kill refills your breath |

### 6.6 How checks work (MH-11, CM-11, NDA-04)

- **Deterministic.** Every dialogue and world check is a fixed threshold. No rolls outside combat.
- **Visible.** The option shows the requirement and your value: `[Reckoning 4] (you: 2)`.
- **Selectable even when you fall short.** You may try; the result is an authored failure line, and the option is
  then removed. A failed check never leaves you worse off than before you tried.
- **Every skill and every attribute gates options somewhere in every hub.** The check tool's distribution table is
  reviewed at every milestone.
- **Not always best.** At least one in five tagged options is costly, wrong for the situation or merely different.
  Examples: winning the legal argument in *Nine Metres* sets a precedent that makes the Kilns harsher elsewhere; an
  intimidation success gets the information and a Grudge; a Letters success correctly quotes a doctrine and
  offends the Steward who quietly doubts it.
- **Knowledge gates are separate.** Options that depend on evidence you hold appear only when you hold it. They are
  not skill checks and are never hidden behind a stat.

### 6.7 The Plain register (MH-13)

One extreme, budgeted now: **Wits 1**. A Wits-1 protagonist is literal, unlettered and direct.
- Every main-path conversation has an alternate register: short, literal player lines and NPCs who react (some
  cheat you on price, some are kinder, the Stewardry treats the plain-spoken as "Steward-touched", and Lusk
  underestimates you, which opens a unique talk-down route in the finale).
- The UI changes: the ledger's quest pages and item notes are shown in the Keeping's pictograms instead of words.
  The Keeping designed its pictogram system for universal reading; a character who cannot read the forms can read
  the pictures.
- Writing rule: the plain-spoken character is never the joke. When an NPC mocks them, the scene is about the NPC.
- The register follows current Wits, so a level-7 raise to Wits 2 returns normal dialogue.
- **Cost:** about 30,000 additional words (about a third of main-path dialogue words), and about 250 extra
  pictogram icons. Budgeted in Section 14. Target: 100% of main-path nodes.

### 6.8 Companions (MH-24, NDA-14)

Four companions, one per major faction. Party size is set by Nerve (one to three companions).

| Companion | Faction and theme | Gameplay perk (changes how you play) | Personal quest: two defensible outcomes | Objects to / leaves if |
|---|---|---|---|---|
| **Sefa Orrin**, day-farmer, Teo Marl's partner | Lowmoot; inherited debt | *Low Path*: low-road legs take 25% fewer hours and her hook-pole can pull enemies into the still | *What Teo Did*: make Teo's diversion public (the truth; it costs the Clean Slate its moral standing), or bury it (protects the movement; leaves the Draught carrying all the blame) | You bind to the Kilns; you vent into the Low; you sell the box to the Draught |
| **Ammon Pell**, steward of the air-marks | Stewardry; faith versus evidence | *Clay Hands*: cap a small breather mid-fight (3 AP), turning the still off in a radius of 2 | *The Sealed Shelf*: reveal the High Vent plan to Capstone (schism, truth), or keep it within the order and reform from inside (protects the community) | You open a capped well; you desecrate the cap; you bind to the Draught |
| **Idris Vane**, Draught engineer, on the Well 9 crew | Draught; complicity | *Pressure Work*: valves and locks 2 AP cheaper; crafts bladders with +2 breaths | *Confession*: testify publicly (ruins her and helps the truth), or sabotage Lusk quietly from inside | You kill Draught workers in numbers; you destroy the Lung |
| **Hollis Crane**, retired Kiln collector | Kilns; debt as duty | *Collector's Eye* while he is with you; collectors stand down when he speaks | *The Crane Account*: accept a settlement that frees him but passes the debt to his niece, or challenge the inheritance rule in the Counting House and lose his pension | You burn tally records; you bind to the Lowmoot |

- Each has a voiced key-scene set, barks, an ending slide with 3 variants, and opinions on 20+ choices.
- **Commands:** direct control in combat by default (they are party members on your turn), or an AI stance. Out of
  combat: follow, wait, go home, open inventory, keep distance.
- **No friendly fire from ordinary attacks.** A friendly in the line of fire blocks the shot rather than taking it.
  Area effects (bottled still, scatter shot) can hurt allies and are always previewed.
- **Objection before departure.** Each leaving condition is preceded by one written warning scene, except in a
  single act of atrocity (killing their own people), which ends the relationship at once.
- Companions are killable like anyone else and never essential (NDA-08).

### 6.9 Worked example: *Nine Metres* (Ladderfoot, first settlement)

**Situation.** On calm nights the still now reaches storey 7. Thirty tenants on storeys 6 to 8, led by old Dov Kettle
(one of the last people who remembers the old country), are being told by the Kiln agent Marrit Sallis that the
empty storeys 12 to 14 are let, and let means paid. The tenants plan to break in. Below them, a Diver crew under
Lark Dunmore has dug from the sub-basement into a Keeping pipe gallery for salvage and opened a small breather,
which is why the still is worse this year. This quest is built to pay off every taggable skill in the opening hub
(MH-17) and has three or more solutions (MH-05).

| Solution | Route | Requirements (any one path) | Immediate result |
|---|---|---|---|
| The Charter | Talk | Reckoning 4 or Letters 4 (find and quote the Lift Town Charter's air-emergency refuge clause), or Persuasion 4 (dead tenants pay no rent) | Upper storeys opened at night "pending a ruling" |
| The Stack | Tech | Tinkering 4 and Rigging 2: restore Lift Town 4's ventilation stack and its wind cowl; one mechanism part (from the Divers, the Lung, or the base) | Lower storeys clear on calm nights; market reopens on storey 6 |
| The Breather | Sneak or fight | Stealth 2 or Melee or Shooting: reach the sub-basement and cap the breather (Wildcraft 2 clay, Tinkering 2 plate, or Ammon's Clay Hands); deal with Lark's crew by stealth, threat, bribe (60 t) or force | The still drops by one storey, but capped gas resurfaces on the day-terraces below |
| The Eviction | Hostile or selfish | Side with Marrit; clear the tenants (Nerve 4 intimidation, or force) | Paid 150 t, Kiln Regard; thirty people leave |
| The Payment | Money | Pay the tenants' arrears: 400 t | Tenants move up; Kilns are content; you are poorer |

Refusal is real: if you decline, the tenants break in on their own at the next act transition, two die in the
fight with the Watch, and the eviction follows anyway.

**Downstream consequences (MH-06)**

| Outcome | Ladderfoot | Another hub | Broadcast |
|---|---|---|---|
| Charter | Upper storeys occupied at night; Marrit hostile but polite | **Quicken:** the "Ladderfoot Ruling" is argued in the Counting House. Kiln agents tighten leases elsewhere (Ladderfoot lime +10%), but slakers cite the ruling, unlocking a Reckoning route in *The Slakers' Ledger* | "The Kilns will hear the tenants' case at the next sitting." |
| Stack | Population band +1 by Act 2; storey 6 market reopens | **The Lung:** Draught engineers come to study the stack, a Draught job opens | "Lift Town 4 breathes again, they say. Fourtop's stairs smell of soot." |
| Breather capped | The still drops one storey | **Reedhithe** day-terrace families who sell in Ladderfoot lose a field: a Reedhithe vendor's stock shrinks; Ammon notes the diversion, which foreshadows *The Quiet Caps* | "A new breather on the Ladderfoot terraces. Day-farmers, take the north path." |
| Eviction | Population band -1; storeys 6-8 sealed and dark | **Reedhithe:** the tenants arrive; Clean Slate influence +1; Dov Kettle becomes a radical voice in the Moot, adding supporters to *Burn the Stocks* | "Thirty more mouths on the river path tonight." |
| Payment | As Charter, without the ruling | None beyond the Kilns' slight Regard | "Somebody paid the Kettle arrears. Nobody will say who." |

**Ending slide (Ladderfoot) variants:** *The Four Stood Full* (Stack, tenants stayed); *Ladderfoot Climbed* (Charter;
the ruling spread to every Lift Town tenancy); *Ladderfoot Let* (Eviction; the town became Kiln rental property and
its lower storeys were given to the still); and the neglect variant, *Ladderfoot Waited* (refused; storeys 6-8 were
bricked up within the year). Each variant is further modified by the Crown resolution.

### 6.10 Main path: fight, talk, sneak on every beat (MH-05, MH-04)

Every beat has a living character who wants something and can be persuaded, refused or killed.

| Beat | Living stake | Fight | Talk | Sneak / tech |
|---|---|---|---|---|
| P. Dawn at the Wagon | Kett, a Diver who arrives to loot | Drive longshanks off the oxen; fight Kett | Bargain with Kett: share, hire or bluff him | Wait on the roof until the still drains; hook the box from above |
| 1. Who Asks After the Dead | Corin Dask, Draught agent hunting survivors | Ambush or duel him | Bluff your identity, sell him a story, or turn him (he owes the Kilns: Reckoning 4) | Shadow him to his dead-drop under Fourtop's stair |
| 2. The Camp of Eleven | Bram Tull, Draught cleanup foreman | Fight the cleanup crew | Question Tull with the evidence you find | Gather evidence unseen: the opened valve (Sounding 4: gas came from upslope), still-death signs (Physic 2), Teo's chalk (Letters 4 or Lodge Apprentice) |
| 3. A Price on the Box | All four factions' agents | Take the box by force from whoever holds it | Auction it (Reckoning), or bargain terms | Steal it back; swap in a forged decoy (Letters 6 or Tinkering 6) |
| 4. Binding deed | The bound faction and its victim | Per faction (4.1-4.4) | Per faction, with a talked alternative | Per faction, with a covert alternative |
| 5. Well 9 | Idris and the Draught test crew | Take the wellhead | Idris testifies; persuade the crew to stand down | Go at night, through the still, under the guards' line |
| 6. The Three Keys | Calloway, Venn, Lusk | Raid the Counting House, the reliquary, the Lung | Legal claim as box-holder; Venn persuaded with evidence; Tessaly's strike as leverage | Heists (Stealth, Tinkering locks) |
| 7. The Keeping's Contingency | Bree Hollin; Rue Malley's Divers | Clear the Divers from the district office | Bree opens the sealed archive | Dive the flooded office; read the survey (Letters 6) |
| 8. Down to the Crown | Sim Agard's Lodge; the Draught line | Break the Draught line | Lodge guides you down, or Draught safe-conduct | The still route under the guards; a ure stampede as cover (Wildcraft 6) |
| 9. The Listening House | Ora Lusk | Fight the Pressure Guard on a flooding podium | Talk Lusk down: **requires the contingency survey and proof that cooperation exists** (two factions' pledges or a repaired High Vent segment), not a stat alone | Bypass to the valve hall by the maintenance gallery; lock her out of the valves (Tinkering 8 or Letters 8) |
| 10. The Valves | Whoever stands with you | | Choose a resolution (Section 13) | |

Lusk's talk-down is the finale's non-combat resolution. It is earned with evidence the player had to find
(MH-05). Key information on every beat lives with living witnesses as well as documents: Idris, Tull, Kett and Teo's
partner Sefa all know parts of what happened at Well 9 (MH-04).

**The truth of Well 9, decided now (NDA-22).** Lusk ran the test at night without warning, knowing caravans
sometimes camp in the hollow. Teo Marl, who knew of the test from a Draught friend, diverted the caravan there to
destroy the stocks, believing the gas would come later in the night. He was wrong, and he died with the others.
Both acts are provable. The broadcast and the endings differ by which truth the player makes public.

---

## 7. Dialogue system spec

### 7.1 UI rules (MH-10, NDA-01, NDA-02)

- The player sees the **exact words** their character will say. A paraphrase is allowed only when it states content
  ("[Refuse, and threaten to tell the Moot]"), never a tone label.
- **Variable option count**, 1 to 9 on screen, numbered, with scrolling beyond that. Mouse, keyboard and gamepad all
  navigate a vertical list. No wheel, no fixed slots.
- Skill and attribute options show the tag, requirement and current value: `[Rigging 4] (you: 5)`. Options you fall
  short on are muted, still selectable, and lead to an authored failure line (6.6).
- Options that cost something show it: `[Give 60 tallies]`, `[Binding: ends Lowmoot standing]`.
- **Lint rules:** two options that lead to the same reply fail the build; every quest hook node must contain a real
  refusal, a conditional accept and a hostile reply with different consequences.

### 7.2 Conversation structure

- **Greeting** chosen from memory flags (first meeting; returning; after a deed; with a companion present; after a
  broadcast mentioned you).
- **Topic hub**: persistent topics (the person, the place, rumours, trade) plus quest branches. Topics close when
  exhausted and reopen when new information arrives.
- **Beats**: scenes that must play once (a confession, a confrontation). Exit is available everywhere except in
  three authored confrontations, which say so before they begin.
- **Barks**: short voiced or text lines on approach, in combat and at dusk.

### 7.3 How NPCs remember

Each named NPC tracks: met, knows your name, background noticed, promises made, kept or broken, lies caught, threats
made, debts between you, favours, and the last topic. Each NPC also reads their community's Regard and Grudge, the
hub's outcome flags and your titles. Writers get a rule: **every named NPC references at least one thing you did
elsewhere**, by the end of Act 2.

### 7.4 How the player says no

Every hook offers: **refuse** (the giver finds someone else; the quest resolves off-screen at the next act transition
with an authored default outcome, reported on the broadcast); **conditional accept** ("If the Moot pays half up
front"); **hostile** (threaten, extort, attack). A refused quest is re-offered once if circumstances change. Refusal
is never punished with a fake consequence; it has a real one.

### 7.5 Voice plan

The protagonist is never voiced (MH-12, NDA-03). Voiced lines: the broadcasters, four companions in key scenes, four
faction leaders in key scenes, Lusk, and barks for everyone. All other dialogue is text with portraits. Recording
happens after content lock (CM-10). Numbers in 12.6 and 14.1.

---

## 8. Combat spec

The combat model is fixed before the stat system (MH-18). Turn-based, presented fast (CM-01). All numbers are
*provisional* and sized for paper prototyping.

### 8.1 Space and turn structure

- **Grid** of 2 m squares with height levels (floors, ladders, stilts, roofs). The still occupies each square in
  0.5 m layers (0-4) and is drawn as a faint tinted volume inside your reading radius (2 + Wits tiles; full sight
  with *Read the Ripple*).
- **Side phases.** Combat starts with a side-initiative check: the leader with the higher Wits (+2 if their side
  ambushed) moves first. In the player's phase you move party members in any order. In the enemy phase all enemies
  act; their animations are batched and played at 2x by default (1x, 2x, 4x, or "skip movement"; MH-18).
- **The still moves at the end of every round**: it flows to lower adjacent squares, sources add, wind and fans
  remove, closed doors hold. Flow is deterministic and, with Sounding, previewed 1-3 rounds ahead.
- **Saving:** the game autosaves when combat starts and cannot be saved mid-fight, so to-hit rolls are played, not
  reloaded (design-principles §6, fourth chain; NDA-04).

### 8.2 Action economy

AP per turn = 6 + Hands (7-11). Up to 2 unspent AP become Guard (+5 defence each) until your next turn.

| Action | AP |
|---|---|
| Move one square | 1 |
| Climb one level (ladder, stilt, rope) | 2 (1 with *Ladder Work*) |
| Crouch or stand | 1 |
| Pistol or air pistol shot | 3 |
| Rifle or air rifle shot | 4 |
| Breech-loader shot | 5 |
| Aimed attack | +1 |
| Melee strike (light / heavy) | 3 / 4 |
| Reload (air rifle pump, cartridge) | 2; breech-loader 3; Hands 4+ is 1 cheaper |
| Use an item, open or close a door | 2 / 1 |
| Watch (reaction shot at the first enemy to move into your sight) | All remaining AP, minimum 4 |
| Push (Breath) | Spend 2 breath: +3 squares of movement |

### 8.3 Hit chance, aimed attacks and Composure (CM-02, NDA-18)

- **Hit chance** = 50 + 5 per skill rank + 5 per Wits pip, minus range penalty (-4 per square beyond effective
  range), cover (half -15, full -35), target Guard and aim penalty. Clamped 10-95. A level-1 tagged shooter with
  Wits 3 hits 80% at effective range in the open: low early whiff rates.
- **Aimed attacks** by region: head -40, arms -20, legs -15, creature weak point -30. On hit: head x1.5 damage and
  Dazed (-2 AP next turn); arm -20 hit chance for the target next turn; leg halves movement for two turns. There is
  no separate targeting mode, no slow motion and no damage shield.
- **Composure** is the banked, player-triggered critical resource, replacing hidden crit rolls. Capacity = Nerve
  (1-5). Start a fight with 1 if Nerve is 4+. Gain +1 for each aimed hit that lands and +1 for each kill.
  **Steady Shot:** spend 1 Composure; the next attack hits if its displayed chance is 10% or more, deals x1.5 damage,
  halves the target's threshold, and applies the full region effect (arm: disarm; leg: knockdown, which can drop a
  target into the still). Against named and major enemies a Steady Shot cannot deal more than 35% of maximum HP, so
  bosses are never one-shot.

### 8.4 Armour (MH-19)

**Final damage = the larger of (base damage minus armour threshold) and 20% of base damage.** Piercing ammunition
lowers the threshold by its pierce value *before* subtraction; ammunition damage modifiers change base damage. When a
hit is 80% or more stopped, the target shows a stamped **TURNED** mark. One armour number per piece; no percentage
layer.

| Armour | Threshold | Notes |
|---|---|---|
| Work clothes, oilskin | 0-1 | Everyone |
| Hide jerkin | 2 | Reedhithe, Divers |
| Quarry leathers, strapped iron | 5 | Kiln collectors; Frame 3 |
| Keeping survey coat (salvage) | 6 | Rare; no movement penalty |
| Draught pressure plate | 8-12 | Draught Guard; Frame 4; -1 square movement |
| **The Kept Suit** | 6 | Old-world sealed suit with air cylinder: immune to the still for 20 turns per fill (8.7) |

**Ammunition, one calibre worked (Draught air rifle bolts, base 12):**

| Bolt | Base | Pierce | Trade-off | vs T0 | vs T5 | vs T10 |
|---|---|---|---|---|---|---|
| Standard | 12 | 0 | Cheap (1 t) | 12 | 7 | 2.4 (floor) |
| Hardnose | 10 | 4 | Worse against the unarmoured | 10 | 9 | 4 |
| Barbed | 14 | 0 | Bleed 2 a turn for 3 turns; armour counts +3 against it | 14 + bleed | 6 | 2.8 (floor) |
| Chalk-ball | 6 | 0 | Non-lethal: knocks out instead of killing | 6 | 1.2 | 1.2 |

Hardnose beats standard against any threshold of 3 or more; standard beats hardnose against bare targets. An
automated test checks the piercing-versus-standard rule for every calibre and tier (MH-19). The weapon-versus-armour
sheet is signed off on paper before production.

**Representative weapons** (tier is set by skill rank: full accuracy at 0/3/5/7/9; -10 hit per rank short):

| Weapon | Skill rank | Damage | AP | Notes |
|---|---|---|---|---|
| Knife | 0 | 6 | 2 (melee) | Silent |
| Hook-pole | 3 | 7 | 3 | Reach 2; *pull* the target one square toward you |
| Billhook | 3 | 10 | 3 | |
| Quarry maul | 5 | 18 | 4 | Frame 4; knockdown on Steady |
| Air pistol | 0 | 8 | 3 | Quiet; 4 shots per charge |
| Draught air rifle | 3 | 12 | 4 | 3 shots per charge; pump 2 AP |
| Kiln long gun (breech-loader) | 5 | 20 | 5 | Loud: alerts the whole map |
| Pneumatic bolt-thrower | 7 | 16, pierce 3 | 4 | Draught masterwork |
| Old-world survey rifle | 9 | 24 | 4 | 5-round magazine; cartridges 40 t each |
| Bottled still (thrown) | 3 | 0 | 3 | 2 layers of still over 3 x 3 squares for 3 rounds |
| Quicklime bomb (thrown) | 3 | 4 + blind | 3 | -30 hit chance for 2 turns; illegal in every hub |

Player HP is 25 + 5 per Frame pip at level 1 (40 at Frame 3), +3 per level (79 at level 14, Frame 3).

### 8.5 Enemy design rules (MH-02, MH-20, NDA-17)

- **Fixed danger per region**, by band (3.4). No global level scaling, ever. Bands within a region are allowed.
- **Higher tiers add behaviours, weak points or compositions, not hit points.** A longshanks lead herds the pack; a
  Drowner veteran carries bottled still; a Draught squad flanks and floods.
- Every creature family has a combat verb and a sound heard before it is seen (11.5).
- **Soft gates** are fixed-danger zones next to safe routes: the ure herds in the middle Low, the Draught Guard on
  Lung Hill, the deep still of the Crown. Each is signposted before contact.

| Enemy | HP | Threshold | Verb |
|---|---|---|---|
| Rooter (boar) | 30 | 2 | Charge; *uncork*: crashing a cellar door releases pooled still |
| Longshanks | 16 | 0 | *Herd*: moves to push you toward still squares; avoids still itself |
| Slick | 9 | 0 | *Submerge*: hides inside still squares; bites legs (cripple) |
| Mourner flock | 12 per flock square | 0 | *Mob*: -15 hit chance for anyone adjacent; calls more to the wounded |
| Papermaker swarm | 10 per swarm | ignores threshold up to 2 | *Swarm*: moving area follows the last attacker; dies in still |
| Ure cow / bull | 90 / 120 | 3 / 4 | *Stampede*: line charge, 25 damage, knockdown |
| Drowner | 28 | 2 | Opens doors and caps to flood you |
| Kiln collector | 38 | 5 | Maul; nets |
| Draught Guard | 44 | 8 | Air rifle; flanks; bottled still |
| Pressure Guard (finale) | 52 | 12 | Opens valve lines on the podium in turns |

### 8.6 Stealth and non-lethal options

- Detection by sight cones and noise. Crouching reduces visibility by 40% **and lowers your head one still layer**.
- **Your flames give you away.** A lit staff reveals you at night at 8 squares; dimmed, you cannot read the still.
- Non-lethal kit: chalk-ball ammunition, chokeholds (Melee 3), knockout blows, and **the lull**: a target put under
  the still falls unconscious before it dies. Pull them out (*Pull Up*, or 2 AP to drag) and they live. Leaving them
  is killing them, and NPCs who find the bodies treat it as murder.
- Pacifist completion is possible on the main path (6.10).

### 8.7 Top gear, earned late (NDA-16)

The **Kept Suit** is the setting's iconic piece of power: the one thing that lets you walk in deep still. *See one*:
a dead Keeping surveyor in a ruined suit in the Drowned Towns (Act 1). *Fear one*: a Draught diver in a working suit
hunts you through the still (Act 2). *Earn one*: the Divers' questline or the Listening House stores (Act 3). Upkeep:
air refills (120 t) only at the Lung or at the base with the compressor slot; gaskets need the rare old-world parts.
Draught pressure plate is likewise visible early on guards and purchasable only at Trusted standing.

### 8.8 Difficulty and length

| Setting | What changes (never just multipliers; never more XP) |
|---|---|
| Lantern | More loot, heals 25% stronger, enemies retreat at half HP, unconscious-in-still outside combat means "rescued by the Lodge" for 20% of your tallies |
| Line (default) | As specified |
| Low | 30% scarcer loot, smarter AI that uses still tactics every fight, healing items scarcer, vendors' reserves smaller |

The *Below the Line* ruleset (9.8) layers on any setting. **Expected encounter length:** 3-5 rounds, 4-7 minutes at
default speed; set pieces 8-12 minutes. Target share of play time in combat: about 25%.

---

## 9. Economy, survival, crafting, durability and the base

### 9.1 Currency: tallies

A **tally** is a fired-clay token stamped by a kiln house and broken across a notched edge. The kiln keeps the other
half (the counterfoil) in its Counting House. A token is worth one measure of quicklime at the issuing kiln, and
the break pattern is unique, so a token is checked by matching it, not by trusting it. Lime is valuable because it
sweetens sour water, makes the mortar everything above the line is built with, sweetens souring fields and marks
safe routes in whitewash. Money is therefore literally a debt record backed by the cure for the hazard. Burn a
Counting House and its tokens become doubtful: prices in that hub rise 25% until the matter is settled (a quest
outcome).

**Money supply is set in the fiction.** Kilns issue tallies only when they burn, and burning needs charcoal. The
*Cold Kilns* quest moves every vendor's cash reserve up or down 30% across the basin. Vendors hold finite reserves
that refill weekly; you cannot sell everything to everyone.

### 9.2 Faucets and sinks (MH-21)

Sinks were designed first:

| Sink | Price (t, provisional) | Why it still matters late |
|---|---|---|
| Skill trainers (4 in the game) | 600 / 900 / 1,200 / 1,500 | Build-relevant |
| Masterwork weapon commissions | 2,000-3,000 | Top-tier power with upkeep |
| Kept Suit refills | 120 each | Late-game exploration |
| Repairs | Priced by item value | Scales with tier |
| Base upgrades | 300-1,500 each, plus parts | Eight slots |
| **Buying debts** | The broadcaster's stock 1,800; the Kettle arrears 400; Reedhithe's lowland stocks redeemed 8,000 | The final-act sink with a meaning: freedom or ownership |
| Old-world cartridges | 40 each | Top weapon |

Faucets: loot themed to plausible containers (purses on people, strongboxes in houses; nothing in a bird's nest),
quest rewards, salvage sales capped by vendor reserves, and opt-in job boards in Ladderfoot, Quicken and the Lung.
Boards follow NDA-06: separate log, no timers, no penalty for ignoring them, no unique rewards, at most three repeats
per source, never on the main path. Target wealth curve (cumulative earned): about 600 t at 25% of content, 2,500 at
50%, 6,000 at 75%; debt-buying and masterworks are sized to absorb the last quarter.

### 9.3 Barter

Vendors buy only what they trade in (MH-22). You sell at 35% of value + 3% per Reckoning rank (max 65%) and buy at
130% - 2% per rank (minimum 110%), adjusted by standing. Barter mixes goods and tallies on one screen with search,
sort and compare.

### 9.4 Scarcity across the game

| Phase | Short of | Pressure release |
|---|---|---|
| Act 1 | Ammunition, heals, tallow | Day-farming jobs; first salvage |
| Act 2 | Lime and repairs as gear tier rises; daylight for deep dives | Salvage diving opens; base cistern |
| Act 3 | Breath for the Crown; cartridges | Wealth flows into debts and masterworks; ammunition and heals stay weighted |

**On for everyone** (CM-05): weighted ammunition and healing items, healing over time (poultices heal 6 a turn for 3
turns in combat; rest heals over hours), limited carry weight, the still and sour water. Check at 50% of content: on
Line difficulty, are ammunition and heals still a consideration? (MH-22 audit.)

### 9.5 Durability (CM-03, overruled in part)

- **Weapons have condition, at FNV softness.** Full effectiveness at 75 or above; each point below 75 removes 1% of
  damage; guns below 50 gain 1% jam chance per point (clearing a jam costs 2 AP). Nothing breaks mid-fight: an item
  that reaches 0 is "worn out" only after combat ends. Condition bars are always visible.
- **Repair paths:** field repair with a duplicate or one metal and one mechanism part restores 10 + 4 per Tinkering
  rank, up to a maximum condition of 60 + 4 per rank; vendors repair to 100 for 60% of value times the missing
  fraction; fitter's rolls (12 in the game, craftable at Tinkering 6) restore 30 anywhere. No real-money path, ever.
- **We overrule the matrix default on armour condition: armour has none, from day one.** The matrix keeps armour
  condition provisionally and says to cut it if playtests show it is a chore. We cut it now because our hazard
  already taxes attention every minute, armour in our model is a single threshold number that wear would make
  unreadable (against MH-19's purpose), and a second maintenance list costs UI and tuning time a small team does not
  have. The sink role moves to weapon repair, debt-buying and Kept Suit upkeep.

### 9.6 Crafting

Junk breaks into ten components (MH-22): metal, wood, cord, hide and cloth, glass, clay, lime, tallow, and two
**bottleneck parts**, mechanism parts (springs, valves) and old-world parts (gaskets, bearings, membranes), which
gate base upgrades, masterworks and the Kept Suit. About 60 recipes in two tiers: ammunition handloading and bolts,
air bladders, tallow and wicks, water sweetener, poultices and Sour cure, traps, clay caps, quicklime bombs, one
modification slot per weapon. Crafting happens at any fire (tier 1) or the base workshop (tier 2). Lists are
searchable and show what each component is for.

### 9.7 The base: Mast 31 (CM-04)

A Keeping monitoring mast on the rim between Ladderfoot and Reedhithe: a 30 m lattice tower with a cabin at 18 m,
claimed in Act 1 through a Lodge job (cleared, bought or talked out of a Diver crew). No free-form building. Eight
authored slots, each a quest outcome with a named resident and a visible change:

| Slot | Resident | Effect |
|---|---|---|
| Rope lift | Ash Tolland, rigger | Haul salvage up; free climb |
| Workshop | Bel Cray, fitter (or Idris) | Tier-2 crafting and repairs |
| Cistern and lime bed | Marta Lune, water-keeper | Four days of sweet water, capped by cistern size (no infinite farming) |
| Relay aerial | Fourtop's apprentice | Extends the broadcast into the Low and the Crown (MH-09 reach) |
| Physic's cot | Orla Fenn, a Reedhithe healer | Faster healing; Sour cure |
| Strongroom | A Kiln mason | Safe storage (the box can be kept here) |
| Air-mill fan | A Lowmoot millwright | Clears the still around the mast at night; a small day-field |
| Mourner perch | Gil Rooke, rook-keeper | Early word of world events; reveals one overland situation per leg |

Modders get the hooks to build a sandbox if they want one (CM-04, MH-34).

### 9.8 The optional hardcore ruleset: *Below the Line* (MH-34, CM-05)

Owned by the design team, shipped at launch, every part individually toggleable, list published:

| Toggle | Rule |
|---|---|
| Needs | Hunger, thirst and sleep. Thirst is met only by sweet water; sour water stacks *Sour* (-10% max HP each) until treated. Needs touch route planning, spoilage and trade, or they get cut |
| Saving | Save only at beds, the base, or on entering a hub |
| Carry | Carry weight x0.6 |
| Healing | Over time only; no in-combat burst |
| Ammunition weight | x1.5 |
| Travel | Overland tallow and food costs x2; no free travel inside regions |
| Breath | Breath-hold -1 |
| Companions | Downed companions die if not stabilised within 3 rounds |
| Nights | Still nights 50% more frequent |

It never awards more XP and never changes the level cap.

---

## 10. Tone and writing guide (MH-25, MH-26, NDA-21)

**Owner:** the lead writer holds sign-off and veto on every area's register, with a sign-off log per area. Until
that person is hired, the lead designer holds it. (The owner must be a named person before content production; see
Section 16.)

**The game refuses to be:** a joke about the end of the world; misery for its own sake; a lecture about climate
policy; a world of monsters; a power fantasy in its first half.

### 10.1 Tone rules, written to be testable

| # | Rule | Test |
|---|---|---|
| 1 | **The world never knows it is funny.** | No NPC comments on the irony of a Keeping slogan. Any line that winks fails review. |
| 2 | **A joke must also be true.** If a player does not get it, they should read it as an ordinary fact about the world. | Read the line to someone who misses the joke; they must not notice anything odd. |
| 3 | **No outside knowledge.** | A line that needs knowledge of our real world, a real brand, a real person or another work to land is cut. |
| 4 | **Nobody is a villain in their own sentence.** | Every antagonist line can be read aloud by a member of their faction as a defence. |
| 5 | **No local explains the still to another local.** | Exposition is addressed to the player only when the player's background makes them a stranger to it. |
| 6 | **Every death has a cause on screen.** | Each body placed in the world has a reason the player can find. |
| 7 | **Grief is shown by maintenance, not tears.** | Mourning scenes show repainting, mending, keeping a place. |
| 8 | **Old forms are used straight.** | Present-day people fill in Keeping forms correctly and seriously. |
| 9 | **Children are kept high.** | No child is ever placed where combat or the still can reach them. Their absence from the Low is noticed. |
| 10 | **Debts are specific.** | Any debt mentioned has an amount, a creditor and a date. |

### 10.2 Humour and darkness

- **Allowed humour:** dry; situational; from people's competence and stubbornness; from the earnest bureaucracy of
  the Keeping's forms; from the distance between how the old world described itself and what is left. Out-and-out
  absurdity only behind the *Tall Tales* trait, or in one or two optional fringe locations.
- **Not allowed:** pop-culture references, fourth-wall breaks, parodies of real people or organisations, talking
  animals, jokes at the expense of the still's victims or the plain-spoken (6.7).
- **Darkness:** the still killed a nation in its sleep and is shown frankly: bodies in deep still, emptied capsules,
  the quarry slakers. Atrocities committed in the present are shown as aftermath and consequence, never lingered on.
  No sexual violence. Debt-bondage is shown as an ordinary, accepted institution, which is the horror of it.

### 10.3 Naming conventions

| Category | Convention | Examples |
|---|---|---|
| Present-day places | Plain compounds of landform and trade | Ladderfoot, Quicken, Reedhithe, Capstone, the Lung |
| Old-world things | Bureaucratic numbers and titles | Lift Town 4, Well 9, Form K-7, the Listening House |
| People | Short given names; trade or landscape surnames | Sefa Orrin, Hollis Crane, Ora Lusk, Dov Kettle |
| Creatures | Folk names from behaviour or look, never monstrous or pseudo-Latin | longshanks, slicks, mourners, ures |
| Items | What users call them | sounding staff, hardnose bolt, fitter's roll |
| Forbidden | Real brands, real organisations, puns on real names, anything from Fallout | |

### 10.4 Sample text

**An item description.**

> **Sounding staff (ash, three cups)**
> Three tin cups on an ash pole, at knee, hip and shoulder. Fill them with tallow, light them, and walk. When the
> knee cup goes out, mind your feet. When the hip cup goes out, mind the children. When the shoulder cup goes out,
> you are already standing in it.
> *1.5 kg. 12 t. The heights are scratched into the pole in someone else's hand.*

**A found document: an old-world notice, with present-day pencil.**

> **THE KEEPING AUTHORITY: NOTICE TO RESIDENTS OF LIFT TOWN 4**
> Your home stands twelve metres above restored ground. Beneath you, the Wend Wetland Reserve is returning to the
> way it was before us. Further beneath, at a depth of two thousand one hundred metres, forty years of the
> nation's breath are kept under sealed shale. They will stay there for longer than there have been people.
> You do not need to do anything. That is the point.
> Please do not feed the cattle.
>
> *(pencil, along the margin)* line 8.1 in the spring, 8.6 at harvest. Moved Ma up to 11. D.K.
> *(different pencil, later)* 9.2.

**An NPC exchange with a visible check and its failure line.** The player is talking to Marrit Sallis, the Kiln
agent, in *Nine Metres*.

> **Marrit:** "Twelve to fourteen are let. Let means paid. If your friends on six can pay, they can climb."
>
> 1. "They can't pay. On the next calm night they'll be dead, and dead tenants owe you nothing either."
> 2. `[Reckoning 4] (you: 2)` "The Lift Town Charter gives anyone below the line refuge above it in an air
>    emergency. Your lease is written on that charter. Read it."
> 3. "How much to open one floor for one season?"
> 4. "Then I'll open it myself." *(leave)*
>
> **Failure line (option 2, Reckoning 2):** You start quoting a charter you have only heard about in the market.
> Marrit lets you get to the end. "Which clause?" You do not know which clause. "Come back when you do. I'll still
> be here. So will the floors." *(The option is removed; the others remain.)*
>
> **Success line (option 2, Reckoning 4):** Marrit reads the clause twice, then a third time with her finger on it.
> "Refuge isn't tenancy." She writes in her book. "Nights only. Until the Counting House rules. They'll rule
> against you, you know. And they'll remember who brought it."

---

## 11. Art vision

### 11.1 The founding visual idea (MH-27)

**Life is lifted; the ground belongs to the past.**

Every asset passes a ten-second test:
1. **What height does it live at, and what does it stand on?** Anything alive or in use is raised, hung, stilted or
   climbing. Anything at ground level in the Low is old-world, dead, or deliberately sacrificial and marked as such.
2. **Where is its line?** Every lowland vertical surface carries air-marks; every inhabited place shows its safe
   height.
3. **Is its colour earned?** Saturated colour is allowed only for flame and safety orange, fresh lime white, the
   Keeping's pictogram-plate green, and faction markers.

The rule is a direct expression of the premise: the old world lifted its towns to give the ground back, the ground
became lethal, and the lifted frames are the only reason anyone lived.

**Source territory:** the old world's architecture draws on **Japanese Metabolism and Expo '70** (catalogue §8,
"unclaimed territory", row 1): concrete service cores, plug-in capsules, space-frame decks, raised artificial ground.
We take the architectural principle, not the culture. The old country is fictional; there are no Japanese cultural
signifiers, no neon, no dense city streets (the catalogue's warning about Akira and Cyberpunk overlap). These are
isolated megastructures in a temperate rural wetland. Present-day building literally enacts the Metabolist idea of
growth by plug-in: survivors hang their own timber capsules off the old frames. We will consult an architectural
historian on the movement before the look bible is locked.

**Ban list (six):** no glowing technology, energy effects or neon; no gas masks, filters or face respirators (the
answer to the still is height, never a mask); no chrome, tail fins or atomic motifs; no robots or powered armour; no
fantasy biology (spores, mutants, giant insects); no global colour tint.

**Hero silhouette, art-directed before any other asset:** *the Sounder*. A walker in a high-collared oilskin with a
coiled air bladder over one shoulder, carrying a staff taller than they are with three small flames at knee, hip and
shoulder. Vertical lines dominate; the three flames read at any distance and at night. The staff is the poster image
and the player's HUD (11.6).

### 11.2 Palette strategy (MH-28, NDA-24)

Base terrain is muted everywhere; the highest chroma is reserved for settlements, hazards and factions. Any global
grade is mild and has a slider.

| Region | Base palette | Light | Accent (meaning) |
|---|---|---|---|
| Ladderfoot | Concrete grey-ochre, rust capsules, laundry colours | Cool, shadowed between towers | Flame orange lamps; air-marks |
| Quicken | Lime white, chalk, kiln-soot black | Bright, dusty, warm white | Kiln ochre tally banners |
| Reedhithe | Deep willow green, silver reed, brown water | Soft, humid; white dawn ground-mist | Lowmoot blue on painted stilts |
| Capstone and the Eyes | Basalt dark, ink-blue lakes, grey-violet heather | Wind-scoured, high and cold | Keeping pictogram green, the only colour Stewards wear |
| The Lung | Oxide-red pipe, brass, steam white | Hard, industrial | Gauge red; Draught black-and-red |
| Drowned Towns | Olive, grey, straw-yellow kill patches | Green gloom under canopy | Diver rope yellow |
| The Crown | Bleached grey, white dead trees | Flat, shadowless | Green enamel pictograms; your flames |

**Time of day:** dawn is white ground-mist over fresh vents and cool light; day is neutral; dusk is long warm light,
bells, and lines of people climbing; night is black lowland with settlements reading as lines of flame at height.
In greyscale screenshots each region must still be distinguishable by architecture and vegetation (MH-28 audit).

### 11.3 Architecture and the technology rule

- **Old world:** concrete cores (round service towers), steel space-frame decks, capsule dwellings, raised walkways
  8-12 m up, Keeping wellheads with concrete caps, manifold pipe runs, lattice monitoring masts, rounded geometric
  signage on green enamel plates with Steward pictograms.
- **Present:** timber, rope, salvaged steel, lime mortar and whitewash; capsules hung from old frames; stilts; rope
  lifts and bucket-lifts; sail air-mills driving wooden fans; flame lamps fixed at measured heights; hand-cut
  stencil numerals for air-marks in signal orange; brush lettering on shops; chisel-cut tallies.
- **The technology rule:** *nothing in this world thinks, glows on its own, or runs unless someone feeds it.* Power
  comes from muscle, wind, water, fire and vent-gas pressure. Old electronics are dead. Weapons are blades, hooks,
  air guns, handmade breech-loaders and a few old cartridge rifles. Medicine is herbal, distilled and surgical.
  The two exceptions are maintained by named people and are fragile: Fourtop's wind-driven transmitter, and the
  Listening House's mechanical valve controls.

### 11.4 Decay versus rebuild at each hub (Year 66; NDA-23)

| Hub | Decay reads as | Rebuild reads as |
|---|---|---|
| Ladderfoot | Spalled core, missing deck bays, dead ground floors silted with flood mud | Timber capsules on the frame; dated stair-treads; whitewashed storey 6 |
| Quicken | Collapsed old quarry sheds | The newest-looking place in the basin: fresh stone terraces, lime render everywhere |
| Reedhithe | Old houses as chimney stacks under willow | New stilts every season; patched walks; fresh fan sails |
| Capstone | Cracked old observatory buildings | A cloister of lime-mortared stone around the cap; repainted pictograms |
| The Lung | Rust on everything not in use | Polished, oiled working machinery; replaced gaskets; glass glasshouses |
| Drowned Towns | Forest through streets; roofs gone; silt-filled lower floors | Diver rope rigs and rooftop camps only |
| The Crown | Intact but bleached; bodies partly preserved | Draught work crews' fresh scaffolds and chalk marks |

### 11.5 Creatures and flora (MH-20)

Design logic: a real animal, one behaviour the still has selected for, one tell. No mutation. Sixty-six years is
twenty to thirty generations for dogs and boar, which allows strong selection on behaviour and a little on build,
nothing more.

| Creature | Silhouette | Real basis | Behaviour | Gameplay role | Tell |
|---|---|---|---|---|---|
| **Longshanks** | Lean, tall, long-legged dogs, heads always high | Feral dogs; only the tallest survived still nights; real gas-pool caves kill low animals while standing people live | Hunt at dusk along the line; drive prey into hollows and wait for the still to finish it | Early threat that teaches the still | Relay yips moving along a ridge |
| **Slicks** | Low, wet, sinuous, small | Feral mink and otter, with a diving reflex | Dive into the still like water to take carrion and bite legs | Ambusher in hollows; punishes crouching | Wet chitter and a dragging rattle |
| **Mourners** | Black ragged clouds of corvids | Rooks; corvids learn food sources fast | Gather at dawn where something died overnight; mob the wounded | Hazard signpost and nuisance | Dawn cawing over a hollow |
| **Ures** | Massive long-horned cattle, shoulder above a standing person | Back-bred wild cattle released by the Keeping's rewilding programme; Pleistocene megafauna as reference | Graze only by day and wind; climb to rises before the line rises | Living still forecast; soft gate; hunt quest | Low bellow; ground thud |
| **Papermakers** | Grey paper nests the size of a cart, high in the frames | Hornets; nesting above the line | Swarm the last attacker | Area hazard; drop the nest into the still to kill it | A drone heard through walls |
| **Rooters** | Bristled, heavy-shouldered | Wild boar (real exclusion-zone recolonisers) | Root in old ground; crash cellar doors | Mid-slope brawler that releases pooled still | Grunting, snapping branches |

**Flora:** willow and alder carr closing over the Low; feral orchards fattened by the gas; **white standing dead
trees** ringing strong breathers (vent tree-kill); acid-red sour moss in wet hollows; chalk-grassland orchids on the
White Edge; heather on the Brow. Flora is information: lush means moderate seepage, dead white means stay out.

### 11.6 UI as an in-world object (MH-29)

- **The ledger.** The whole interface is a **Form K field ledger**, the Keeping's standard survey book (models K-7
  survey and K-9 seal inspection; later cheap reprints by the Kiln Houses). Pages: *Particulars* (character),
  *Holdings* (inventory), *Accounts* (tallies, debts owed and owing), *Chart* (overland map you annotate), *Standing
  Matters* (quests and stake clocks), *Persons* (reputation and NPC notes). The paper is the Keeping's
  "survey buff" with red-orange register lines, because orange was the old world's air-safety colour; re-tint with
  other found stocks (blue carbon, green duplicate). Quests close with a SETTLED stamp; locked-out content gets
  CLOSED.
- **The staff as HUD.** The three flames sit at the screen edge and report the still at your feet: lit, guttering,
  out. Breath shows as pips over your head only when you are under.
- **It is also a good list.** Every list has search, sort, filter and compare; a dense PC layout; legible highlight.
  Benchmark: find a named item in a 200-item inventory in under 5 seconds.

### 11.7 Mood-board pointers (rows in `research/art/visual-reference-catalogue.md`)

| Use | Catalogue row |
|---|---|
| Old-world architecture (primary) | §8 Japanese Metabolism and Expo '70 |
| Concrete mass and weathering | §6 Brutalist architecture; §4a Hashima Island |
| Lattice masts in forest | §4a Duga radar |
| Trees through civic ruins at 10-50 years | §4a Pripyat (birches through asphalt only); §4b rows "10-50 years" and "50-100 years" |
| Raised walkways gone wild | §4b High Line |
| Breathers and smoking ground | §4a Centralia |
| Still-killed drifts of animals on shorelines | §4a Salton Sea |
| Silt-filled lower floors | §4a Kolmanskop |
| Stranded boats in the estuary marsh | §4a Aral Sea |
| Roots as architecture on the oldest frames | §4a Ta Prohm |
| Tree-kill colour reference | §5 Red Forest |
| Ures | §5 Megafauna |
| Rooters | §4a Fukushima exclusion zone (wild boar) |
| **Distance checks** (what we must not resemble) | §6 Stalker, S.T.A.L.K.E.R., Metro (no masks), The Last of Us (no reclaimed-city green), Nausicaa (our lush Low has no fantasy biology), Death Stranding, Stalenhag |

Each pin on a mood board carries a stated purpose. Prototype one environment, Ladderfoot's storey 6, before the look
bible locks (catalogue takeaways).

---

## 12. Audio vision

### 12.1 Score identity (MH-30)

**Everything in the score is moved by air.** Pump reed organ (harmonium), concertina and bass concertina, wooden
flutes, hummed and breathed voices, and occasionally a brass band. No strings, no synth pads, no orchestral swell, no
industrial drones. This is neither dark-ambient industrial pastiche nor the orchestral default.

- **Signature timbre:** the reed organ *with its bellows left in the mix*. You hear the pump's inhale and exhale
  between chords. Phrases end when the bellows run out, so musical phrase length is breath length.
- **Main motif:** a rising four-note figure that never completes. It resolves to a major cadence only in the High
  Vent ending; in the Reseal ending it is held on one long breath and left unresolved (deferral, again).
- Modal (mostly Dorian), sparse, and near-silent in exploration, where ambience carries the world.

**Music engine, specified before the composer is contracted:**

| Cue type | Rule |
|---|---|
| Location themes | Three layers per hub (drone, melody, rhythm); day and night mixes; layers rise as you approach the hub |
| Incidentals | 5-15 s, after discoveries or quest beats |
| The climb | Dusk tension cue, starts with the dusk bell, scales with how far below the line you are |
| Combat | Intro, loop, outro. Starts when hostiles have seen you; outro after 10 s without hostile action; no re-entry within 30 s (hysteresis) |
| Stingers | Level-up, binding, SETTLED, CLOSED, slide transitions |
| **Silence** | An explicit state. After any cue, no music for 3-6 minutes. Exploration defaults to silence plus ambience. Music ducks under ambience, never the reverse |

### 12.2 The broadcaster: Fourtop and the evening line (MH-09, NDA-25)

**What it is in this world.** On the roof of Lift Town 4 a wind-driven transmitter built from old-world parts sends
on one frequency. Receivers are crystal sets, which need no power: an earpiece, a coil and a wire. Everyone in the
basin listens at dusk, because **Fourtop reads the line**: the expected safe height for every place tonight, built
from the Stewardry's air-marks and Lodge reports, in a fixed ritual order. It is weather radio, the news and the
only music most people hear. The player carries a crystal set.

**The host.** Ivo Strand, "the Reader", a former Kiln clerk who is still bonded to the Kilns, which means sponsors
can lean on what he says. His arc is told only in audio:
- If the player buys his stock (1,800 t) he is free and reports straight, including what he knows about Well 9.
- If the Draught buys it (their binding deed), the news tilts: Well 9 becomes "Lowmoot sabotage".
- If he dies, his apprentice **Wren Abel** takes over: younger, frightened, honest, and she plays Lowmoot day-songs
  instead of his heritage records. The station survives; its taste changes.
- If the relay is cut, the Low and the Crown go silent until the base relay slot is built (reach as a mechanical
  unlock).

**Reactive content.** Every major quest (20) has a *before*, *after* and *failed* news item, plus variants where the
outcome splits. The Reader names the player by their title. Hub stake clocks are announced. The line report is
assembled from about 120 short recorded words and numbers in the Reader's voice ("Reedhithe. Five. Rising after
dark."), the way automated weather broadcasts are, so it reacts to the real state at almost no cost.

> *"Evening line, from Fourtop. Ladderfoot, nine point two, steady. Reedhithe, five, rising after dark. The Steps
> clear. Capstone clear. The Lung don't tell us. Keep out of the hollow under Well Nine. We've had no word from
> there since the Pask caravan."*

**Playlist size, computed from the pacing model** (`audio/ambient-radio-pacing-and-foley.md` §3.5: N = 19 x f x H / R,
R = 6 plays tolerated per song):
- Planned hours H = 35 (between a first run and a completionist run).
- Main station listening share f = 0.3: N = 19 x 0.3 x 35 / 6 = **33 songs**. We ship **34** on Fourtop, rising to 40
  through tiered unlocks.
- Two minor stations at f = 0.05 each: 19 x 0.05 x 35 / 6 = 5.5, so **9 each**: *Capstone Hours* (chant and readings)
  and the *Lung Works Band* (brass).
- **Total: 52 tracks.** No-repeat window of at least half the active pool. Time-of-day blocks.
- Speech: about 10.5 listening hours on Fourtop gives about 79 link plays (at 7.5 per hour); at R = 2 that is
  **40 link lines**. News: about 79 news plays at R = 1.5 is about 53 items; we write **60** (20 quests x 3) plus
  variants.
- **Unlock tiers:** 22 songs at the start; +6 when Deposit crates are recovered from the Drowned Towns (Act 1 quest);
  +6 new songs by Ladderfoot singer Nell Garrow about events in Act 2, whose lyrics name what the player did (in-world
  musicians record new songs as the story advances).

**In-world source of the music.** The Keeping, true to its creed, buried a **Cultural Deposit** of the nation's
heritage music on durable discs, meant to be kept for ten thousand years. Its curators chose the oldest and most
canonical repertoire: parlour songs, hymn tunes, brass marches, early dance tunes. That gives the radio its in-world
logic and gives us public-domain compositions. The irony is felt and never stated: the old world's sincere idea of
what deserved keeping, played over the ruin its other keeping caused.

### 12.3 Music sourcing a small team can legally afford

- **Public-domain compositions, newly recorded by us.** US compositions published before 1931 are public domain as
  of 2026 (research `ambient-radio-pacing-and-foley.md` §2.6). We hire musicians to record new arrangements and own
  the masters. Every item is checked for the specific arrangement and lyric, not just the melody. A rights lawyer
  reviews the list before recording. No historical recordings are used for identity.
- **New lyrics on public-domain folk tunes** for Lowmoot day-songs (a broadside practice): words we own about our
  world.
- **16 commissioned originals** (work for hire, masters owned): Nell Garrow's songs, the Reader's station ident,
  Capstone chants.
- **No hero licences.** Every contract separates game, soundtrack-album and marketing rights.
- Instrumentation for radio arrangements stays inside the family: reed organ, concertina, voice, brass band, upright
  piano, fiddle. Recorded mono, with a lo-fi chain, as if pressed on old discs.
- Players can mute any station; stations are moddable (MH-34).

### 12.4 Sound as interface (MH-31)

Three signature sounds carry information, recorded from real equivalents:
1. **The flames.** The staff's tallow flames hiss and drop in pitch as gas rises, then gutter and pop out. Recorded
   from real tallow and oil flames in a closed jar. You can hear the still's depth.
2. **The insect bed goes silent.** Every lowland ambience has an insect layer that drops out square by square where
   the still is. In this game, silence is the alarm. This inverts the familiar clicking-counter device.
3. **The ledger.** Pencil on paper, page turns, the tally token's clay clack, the SETTLED stamp.

Also: every hub rings a **dusk bell** (half an hour's warning); every creature family has a learnable call heard
before it is seen (11.5); when you go under, ambience muffles and your heartbeat comes up; air guns have a sharp
near crack and a far snap, breech-loaders a near boom and a far rolling echo. Audit: with the screen covered, a tester
names the still level and the nearest creature by ear.

### 12.5 Ambient beds per region

| Region | Bed |
|---|---|
| Ladderfoot | Wind through concrete, rope creak, distant handbells, capsule doors, market voices high above, dead quiet below storey 6 |
| Quicken | Kiln roar, quarry picks, carts on stone, sheep on the tops |
| Reedhithe | Willow rustle, water, air-mill sails, frogs, the insect bed (and its silence at dusk) |
| Capstone | Wind over the rim, lake lapping, the fizz of gas bubbles at the Mother Eye's edge, chant at the hours |
| The Lung | Vent hiss, engine thump, relief valves, the band rehearsing |
| Drowned Towns | Dripping, mourners, the groan of a frame settling, Diver calls |
| The Crown | Almost nothing: breathers hissing, your flames, your breath |

### 12.6 Voice plan

| Role | Lines (provisional) |
|---|---|
| The Reader (links, news, line words) | 450 |
| Wren Abel (replacement set) | 250 |
| Four companions (key scenes and barks) | 4 x 250 = 1,000 |
| Four faction leaders (key scenes) | 4 x 120 = 480 |
| Ora Lusk | 150 |
| Barks for everyone (about 12 actors) | 1,170 |
| **Total** | **about 3,500** |

At most 10 speaking roles per actor per region. Recorded after content lock. The player is never voiced.

---

## 13. Endings (MH-07, CM-12, NDA-10)

### 13.1 Structure

About 14 slides per playthrough, each a painting with a paragraph:
1. **The Crown** (the central resolution).
2. **The debts** (what became of the box).
3. **Each hub** (five), with a "you neglected it" variant for each.
4. **Each companion** recruited or met (four), three variants each.
5. **The minor factions** (Lodge, Divers).
6. **Fourtop** (who is reading the line, and what they say).
7. **The protagonist** (background plus earned title).

### 13.2 The central resolution

The Crown must vent somewhere or keep rising. The choice is made at the valves, and what is available depends on
what you hold.

| Resolution | Requires | Who pays |
|---|---|---|
| **Low Relief** | Lusk's plan: open Wells 9-14 into the Wend lowland | The Lowmoot: the Low becomes a permanent still basin; Reedhithe is abandoned. The rim is safe for a lifetime |
| **The High Vent** | The Keeping's contingency survey, a repaired pipe route, Trusted standing with three factions or bound to one and Trusted with two | Everyone, a little: the Kilns fund it and lose their monopoly, the Stewardry breaks its doctrine and vents on its holy rim, the Draught shares control. The line falls over years |
| **Reseal** | Stewardry and Kilns: lime slurry pumped into the wells | The grandchildren: thirty years of a stable line, then a worse return |
| **Shut-in** (fail-safe) | The pictogram emergency card alone | The same as Reseal, but buys ten years, not thirty |
| **Hold the Valves** | All three keys and force | Whoever displeases you: you become the valley's keeper of its breath |
| **Walk Away** | Break the controls, or leave | Everyone, slowly: nothing can vent or seal; the rim towns climb or leave over a generation |

No resolution is required to involve a fight or a sacrifice that contradicts the player's tools (NDA-10). Every
scripted beat in the finale is audited against party abilities: companions with bladders or a Kept Suit can enter
the valve hall; Physic, Tinkering and Letters routes apply; a labelled save is made before the finale.

**Materially different end states: 9 central** (Low Relief under Draught or Kiln rule; High Vent; Reseal under
Stewardry or Kiln management; Shut-in; Hold the Valves benevolent or extortionate; Walk Away as evacuation or
collapse), crossed with **5 debt outcomes** (stocks returned to the Kilns, held by the Draught, burned, sealed in the
cap, kept by you). About 70 slide variants in all, drawn from about 30 paintings with variant overlays. Every slide
trigger has an automated reachability test (14.5).

Sample slide (Reedhithe, Low Relief):

> They opened Well Nine on the first calm night of autumn, and the Low took a breath it has not let go of. The
> Lowmoot walked out along the night ropes with what they could carry. Elsa Fenwick refused to climb. They painted
> her air-mark at the top of the old bridge pier, higher than anyone thought the still could reach, and it reached it.

### 13.3 After the ending

**Slides first, then free play** (CM-12). The Crown region and Reedhithe (the hub nearest the finale) are rebuilt to
the chosen outcome. Other hubs keep their pre-finale state plus cheap expressions of the ending: repainted
air-marks, who staffs the gate, and a post-ending broadcast set from Fourtop. This is built into the quest state model
in pre-production. If it cannot be afforded by first playable, it is cut cleanly: the game ends after the slides,
with the labelled pre-finale save offered.

---

## 14. Scope and production plan (design level)

### 14.1 Team assumption and content budget (MH-33)

**Assumed team:** seven full-time equivalents for 36 months (lead designer and writer, writer, quest and systems
designer at half time, 1.5 programmers on an off-the-shelf engine, two artists, producer and QA lead), about 250
person-months, plus about 45 person-months of contractors (composer and musicians 8, voice 6, external QA 18, art
outsourcing 13). **Total about 300 person-months.** For scale: Fallout 1 about 750, New Vegas about 1,000, Fallout 4
about 3,500 (`design-insights/production-metrics.md` §7, all `[C]`).

| Content | Budget | Rationale |
|---|---|---|
| Hubs | 5, plus 2 non-hub regions | The matrix's 5-7 band, at the bottom, so the flag web can be complete (CM-08). "Five towns with ten shared flags beat fifteen isolated towns" |
| Overland minor sites | 18 one-screen maps | Cheap per site; carries road situations |
| Quests | **63 authored**: main 11 beats; faction 4 x 6 = 24; companion 4; hub side 5 x 4 = 20; minor factions 4 | Text-driven reactivity is the cheapest high-value feature (§9 of the metrics file) |
| Bespoke encounters | 45 region set pieces; 12 unique road encounters; 30 situation templates | Situations, not quests (NDA-06) |
| Words | About 240,000 dialogue + 30,000 Plain register + 80,000 other (items, documents, ledger, broadcast, slides) = **about 350,000** | About 270 finished words per writer-day over 26 months for 2.5 writers `[C, our estimate]`; measured in the slice |
| Voiced lines | About 3,500 | About 5% of New Vegas's 65,000; voice is the largest labour sink in the evidence, so it is the exception |
| Named NPCs | About 150, plus about 60 generic types | All with two-state schedules (day position, night position above the line) and no more |
| Creatures | 6 families, 15 behaviour-based variants; 10 human archetypes | Behaviour costs AI and animation (matrix §6); kept to six families |
| Items | 30 weapons, 6 armour types, about 45 consumables and crafted items, 10 components, about 70 quest items, about 80 junk | |
| Perks / traits / backgrounds | 36 / 9 / 6 | Perks are cheap and replay-heavy |
| Ending slides | About 70 variants on about 30 paintings | Cost unsourced in the research; measured in the slice |
| Music | 52 diegetic tracks; about 50 minutes of adaptive score | Section 12.2 |
| Pictograms | About 250 (UI, Plain register, perks) | Flat icons in one system |

**The expensive pillar's budget:** the still system (simulation, AI awareness, previews, level-design tools) is
capped at **30 person-months** of programming and design, with a go/no-go at month 4 (14.6).

### 14.2 Schedule (design level)

| Months | Phase | Exit criterion |
|---|---|---|
| 1-6 | Pre-production: combat model and still prototype first (MH-18); tone bible and look bible (MH-25, MH-27); the Sounder silhouette; tools (check tracker, flag graph, slide reachability, reply lint); music engine spec | Still prototype passes the readability test (14.6); bibles signed |
| 7-9 | Vertical slice | Shown to funders at month 9 |
| 10-28 | Production, **middle first**: Ladderfoot, Reedhithe, Quicken; then Capstone and the Lung; then the Drowned Towns; the Crown last, so cuts fall at the edges (MH-32) | Content lock at month 28 |
| 28-30 | Voice recording after lock; external QA burst; closed beta of the full game with 200 players | Zero known quest blockers |
| 30-36 | Bug fixing and performance only | Release candidate; the date moves rather than the scope growing (NDA-27) |

### 14.3 Vertical slice definition

Ladderfoot and its surrounding region (terraces, sub-basement, one Drowned Towns edge site), the prologue, and one
overland leg toward Reedhithe. It must contain: *Nine Metres* with all five solutions and its cross-hub flags
stubbed; three fights including one where the still is used as a weapon and one where it is used to spare a life;
Sefa recruitable with her perk; Fourtop with before, after and failed lines and a live line report; the full ledger
UI with search; every one of the 11 skills used at least five times in the hub (MH-17); every attribute gating at
least one option; the Plain register for every slice main-path node; one ending slide generated from slice state;
and stable play on the weakest target hardware. The slice also produces our first real numbers: words per writer-day,
cost of one slide, still-system cost.

### 14.4 Cut list, in priority order (first to go first)

1. Post-ending free play (CM-12): slides then end, with the labelled save.
2. The two minor stations (Capstone Hours, Lung Works Band); Fourtop grows to 40 songs instead.
3. The third companion slot (Nerve 5 allows two).
4. Base slots from eight to five (keep rope lift, workshop, cistern, relay, strongroom).
5. The Drowned Towns halved in area.
6. Tier-2 crafting folded into vendor services.
7. Weapon durability simplified to a jam threshold only.
8. Unique road encounters from 12 to 6.
9. Last resort, per MH-23: cut a faction whole. The Stewardry goes first (its key moves to the Kilns' Counting House;
   its archive moves to the Drowned Towns office; Ammon is cut). Never starve a faction instead.

**Already cut to make this buildable:** a voiced protagonist; all cinematics; open-world scale; free-form building;
procedural quests; multiplayer; mounts and vehicles; romance; facial animation; console launch; the estuary region
and its trading faction (first expansion candidate); armour condition (9.5); weather beyond wind and calm.

### 14.5 Stability, QA and mod openness (MH-32, MH-34, NDA-26, NDA-28)

- **QA is a named budget line**, about 12% of person-months, sized to branching (reactivity multiplies script state).
- **Automated checks run on every build:** kill-everyone run reaches an ending; every ending slide is reachable; the
  check-distribution table (no skill or attribute at zero uses per hub; at least 20% non-optimal tagged options);
  identical-reply lint; the flag graph shows an outbound edge from every hub; piercing beats standard ammunition for
  every calibre; a simulated wealth curve against sink prices at 25/50/75/100% of content.
- **Quest logic has fail-safes:** alternate triggers, redundant information from living witnesses and documents.
- **Densest hub first on the weakest hardware:** Ladderfoot is the first region built and profiled.
- **Launch commitments:** known quest blockers are release-blocking; crash-free play time is measured against a
  target; no paid relief from any friction we designed; no score-linked bonuses; any paid content is additive and
  curated.
- **Mod openness from day one:** documented, human-readable data for dialogue, quests, items, creatures, stations
  and slides; scripting hooks; a 64-bit executable; an in-game configuration menu; the *Below the Line* toggle list
  published; station definitions moddable; base hooks exposed. Post-launch updates are treated as breaking API
  changes: versioned, offered first as opt-in branches, coordinated with major mod teams. We publish a cut-content
  record so restorers can tell restored from new.

### 14.6 Top risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| The still is unreadable or unfair | It is the expensive pillar and the identity | Coarse layers, deterministic flow, previews, the lull before death; a month-4 readability test: 8 of 10 testers predict next-round flow correctly. If it fails, fall back to static still zones with scripted changes |
| The still system overruns | Engineering on a small team | 30 person-month cap; reuse the same grid for exploration and combat |
| Text volume and branching outgrow QA | Reactivity multiplies bugs (MH-32) | Measured words-per-day in the slice; content lock at 28; automated tests; "less content, fewer bugs" |
| The Plain register reads as mockery | Tone and reputational risk | Writing rule 6.7; sensitivity readers; one owner |
| Metabolist architecture read as a cultural skin, or the lush Low read as Nausicaa | Originality | Consultant review; the ban list; distance checks on every mood board |
| Public-domain music clearance errors | Legal | Per-item arrangement and lyric checks; lawyer review before sessions |
| Turn-based limits market size | Commercial | Accepted (CM-01); fast presentation; the Wasteland and Fallout 1/2 long-tail evidence |
| The debt theme turns into a lecture | Tone | Rule 4 (no villains in their own sentence); every faction's case shown in play (NDA-13) |
| Key-person dependency | Seven people | Bibles written down early; tools, not memory, track checks and flags |

---

## 15. Matrix audit

Status key: **Met** = this document makes the decision and names where it is specified. **Partial** = decided, but
a stated deliverable or measurement is still owed. **Open** = needs detail before the item can pass.

### 15.1 Must-haves

| ID | Item | Where | Status |
|---|---|---|---|
| MH-01 | Density over area | 3.7 (90 s target, one-liners) | Partial: must be measured in the slice |
| MH-02 | Danger is geography, signposted | 2.5, 3.4, 8.5 | Met |
| MH-03 | Fixed time; settlements show how they live | 2.2, 2.8, 3.3 | Met |
| MH-04 | Environmental story with living stakes | 3.7, 6.10 (living stake per beat; witnesses as well as documents) | Met |
| MH-05 | Two of three; all three on the main path; evidence-gated talk-down | 6.9, 6.10 | Met for the main path; per-quest F/T/S table for all 63 quests owed |
| MH-06 | A web, not a list | 3.6, 4.5, 6.9 | Partial: spine drawn; full flag graph owed in pre-production |
| MH-07 | Per-community slides, every branch tested | 13.1-13.2, 14.5 | Met (reachability test specified; to be built) |
| MH-08 | Anyone can die; one costly fail-safe; lockout notices; no murder-gated loot | 4.7, 4.9 | Met |
| MH-09 | The world talks back cheaply | 12.2 (before/after/failed for 20 quests; reach unlock; replacement host) | Met |
| MH-10 | Show the line; variable option count; real refusal | 7.1, 7.4 | Met |
| MH-11 | Deterministic visible thresholds; written failure; 1 in 5 tags non-optimal | 6.1, 6.6, 10.4 | Met (audit tool owed, 14.5) |
| MH-12 | Unvoiced, player-authored, selfish-proof hook | 6.3, 7.5 | Met; needs the "read the first hour as a selfish character" review |
| MH-13 | One extreme stat rewrites the voice | 6.7 | Met (budgeted, 14.1) |
| MH-14 | Hard power budget | 6.5 (cap 14; ratio 0.36) | Met |
| MH-15 | No dump stat | 6.1 | Met on paper; playtest question owed |
| MH-16 | Rule-changing perks every 2 levels; traits with costs | 6.4, 6.5 | Partial: 12 of 36 perks specified |
| MH-17 | Every skill earns its place; opening proves it | 6.2, 6.9, 14.3 | Partial: skill x hub matrix (minimum 5 per cell) owed |
| MH-18 | Combat model first; build visible in every fight; fast | 6.1 readouts, 8.1-8.3, 14.2 | Met |
| MH-19 | Threshold-plus-floor armour | 8.4 | Met; full weapon x armour sheet owed |
| MH-20 | Every creature has a verb and a tell | 8.5, 11.5 | Met; human archetypes' tells owed |
| MH-21 | Sinks before faucets; money matters late | 9.2 | Met; wealth simulation owed |
| MH-22 | Scarcity defended by systems; junk matters; lists work | 9.1-9.6, 11.6 | Met |
| MH-23 | Factions with an argument, an economy, a home | 4.1-4.4 | Met (case, damaging fact, basis, three dissenters, home, questline each) |
| MH-24 | Companions as embodied arguments | 6.8 | Partial: pathfinding and door-blocking rules owed |
| MH-25 | Tone bible with one owner | 10 | **Open: owner must be a named person** |
| MH-26 | Our own ironic engine, four channels | 2.4 | Met |
| MH-27 | One visual rule; hero silhouette first | 11.1 | Partial: one-page look bible and sign typography sheet owed |
| MH-28 | Regional palettes; saturated colour for meaning | 11.2 | Met; greyscale test owed |
| MH-29 | In-world interface that is also a good list | 11.6 | Met; 200-item benchmark owed |
| MH-30 | Adaptive score; silence as a state | 12.1 | Met (spec precedes composer contract) |
| MH-31 | Sounds that carry information | 12.4 | Met |
| MH-32 | Stability before content | 14.2, 14.5 | Met as plan |
| MH-33 | One expensive pillar; text by default | 1, 14.1 | Met (the still; 30 pm cap) |
| MH-34 | Moddable day one; designer's hard mode | 9.8, 14.5 | Met as commitment |

### 15.2 Never-do-agains

| ID | Pattern | How this design avoids it |
|---|---|---|
| NDA-01 | Tone-label prompts | Exact words, or content paraphrase only (7.1) |
| NDA-02 | Fixed option count; false choices | 1-9 options, scrolling list; identical-reply lint (7.1) |
| NDA-03 | Voiced fixed-backstory protagonist | Silent protagonist; backgrounds are positions, not biographies (6.3) |
| NDA-04 | Percentage speech checks | Fixed thresholds and no rolls outside combat (6.6). Combat keeps to-hit rolls, but saving is disabled mid-fight (autosave at combat start), so reloading cannot replace play (8.1) |
| NDA-05 | Global karma | Two-track per-community reputation, witnessed acts, titles with trade-offs (4.8) |
| NDA-06 | Radiant filler | Situations, not quests; opt-in capped boards off the main path (3.5, 9.2) |
| NDA-07 | Choices leave no trace | Hub state model; every major quest changes something visible (3.6) |
| NDA-08 | Essential NPCs | None; children kept out of reach and off the critical path (4.9) |
| NDA-09 | Real-time or hidden clocks | Act-driven, announced stake clocks; the line rises only when the player advances the story (5.4) |
| NDA-10 | Finales that contradict the player's tools | Finale audit against party abilities; labelled save; no forced sacrifice (13.2) |
| NDA-11 | Opening that ignores the build | Ten-minute prologue with three routes, skippable on replay; teaching in Ladderfoot (5.3, 6.9) |
| NDA-12 | Shallow lockouts; joining every side free | Binding deeds that offend a rival, written warnings, CLOSED stamp, one amnesty (4.7) |
| NDA-13 | A faction's case only as hearsay | Each faction has one quest that shows its best claim in play (4.1-4.4) |
| NDA-14 | Companions as turrets or hazards | Commands, no ordinary friendly fire, arcs and perks (6.8) |
| NDA-15 | Build convergence | Cap 14, perks every 2 levels, no flat-percentage perks, 0.36 skill ratio (6.5) |
| NDA-16 | Iconic power in the first hour | Kept Suit seen in Act 1, feared in Act 2, earned in Act 3 with upkeep (8.7) |
| NDA-17 | Level-scaled sponges | Fixed bands; tiers add behaviour; difficulty changes scarcity and AI (8.5, 8.8) |
| NDA-18 | Invulnerable targeting mode | No separate mode; aimed shots priced in hit chance; Composure is a resource, not a shield (8.3) |
| NDA-19 | A world with no people | Every region has living inhabitants, including Draught crews and Divers in the Crown and the Drowned Towns (3.2) |
| NDA-20 | Invisible walls and loading cells | Honest terrain edges; each hub one seamless map with cutaway floors (3.1, 3.4) |
| NDA-21 | Pop-culture jokes | Tone rules 1-3; *Tall Tales* fence (6.4, 10.1-10.2) |
| NDA-22 | Mystery antagonist with no answer | The truth of Well 9 decided (6.10); Lusk's motive defensible aloud (4.4); endings differ by which truth is made public |
| NDA-23 | Unswept ruins | 66-year material table; labour visible in every hub (2.8, 11.4) |
| NDA-24 | One global tint | Regional palettes; mild grade with slider (11.2) |
| NDA-25 | Tiny playlists | 52 tracks from the formula, tiers, no-repeat window, in-world musicians (12.2) |
| NDA-26 | Launching unfinished; monetising | Bug-fix-only final six months; no paid relief; date moves (14.2, 14.5) |
| NDA-27 | Scope grows as schedule shrinks | Scope fixed now with a cut list; no score-linked pay (14.2, 14.4) |
| NDA-28 | Breaking or monetising mods | Versioned opt-in updates; open data; free mod support (14.5) |

### 15.3 Contested middle: positions taken

| ID | Matrix default | Our decision |
|---|---|---|
| CM-01 | Fast turn-based | Adopted (8.1) |
| CM-02 | No separate mode; aimed shots; banked crit | Adopted; Composure driven by Nerve (8.3) |
| CM-03 | Soft durability; armour condition cut if a chore | **Partly overruled**: weapons at FNV softness; armour condition cut from day one (reasoning in 9.5) |
| CM-04 | One authored base | Adopted: Mast 31, eight slots (9.7) |
| CM-05 | Scarcity for all; needs in the hardcore ruleset | Adopted (9.4, 9.8) |
| CM-06 | Hard cap; post-cap horizontal rewards | Adopted: cap 14, Marks (6.5) |
| CM-07 | 10-12 skills, coarse thresholds | Adopted: 11 skills, 0-10, checks at even ranks (6.2) |
| CM-08 | Hybrid map, 5-7 hubs | Adopted: 5 hubs (3.1) |
| CM-09 | Overland travel is the fast travel | Adopted (3.1) |
| CM-10 | Unvoiced player; voice the theme carriers | Adopted: about 3,500 lines (12.6) |
| CM-11 | Show requirement and value | Adopted (6.6) |
| CM-12 | Slides then free play, or cut cleanly | Adopted (13.3) |

---

## 16. Open questions for the next phase

1. **Name the tone owner** (MH-25). Until a person is named, MH-25 fails.
2. **Still prototype:** is a 0.5 m layer grid with end-of-round flow readable to players who have never seen it? What
   is the minimum preview that makes it fair? (Month-4 test, 14.6.)
3. **Composure tuning:** does +1 per aimed hit make aimed shots dominant over volume? Paper-test one burst-style and
   one precision build against the same fights.
4. **Hands and AP:** does +1 AP per pip make Hands the god stat, as Agility was? If playtests say yes, move to
   AP = 7 + half Hands and give Hands more non-combat weight.
5. **Plain register scope:** is 30,000 words enough for full main-path coverage, and does the pictogram ledger
   remain usable for a full run?
6. **The skill x hub matrix:** confirm at least five uses per skill per hub (275 minimum) in quest outlines before
   writing begins (MH-17).
7. **Full flag graph** for all 63 quests, with an outbound edge from every hub and each minor faction read three
   times (MH-06).
8. **Per-quest F/T/S table** for every quest with a giver (MH-05).
9. **Cultural review** of the Metabolist architectural source and sensitivity review of the Plain register.
10. **Music rights list:** which specific public-domain compositions and arrangements; lawyer sign-off before
    sessions.
11. **Post-ending free play:** confirm cost by first playable or cut (CM-12).
12. **Slide cost:** measure one painting and paragraph in the slice; the research has no figure.
13. **Engine choice** against the 3D-with-cutaway requirement, 64-bit and modding needs; no custom engine.
14. **The wider world:** the setting bible keeps it unknown. Confirm no plot thread or slide ever needs an answer,
    or decide one now (NDA-22 discipline).
15. **The estuary and its trading faction** as the first expansion: decide only after launch stability is proven;
    it adds horizontal content and never raises the level cap.

