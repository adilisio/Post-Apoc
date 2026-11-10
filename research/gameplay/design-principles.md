# Design Principles and Central Tensions of the Fallout Series

Scope: the *stated* design pillars of the three studios that made mainline Fallout games (Interplay / Black
Isle, Obsidian, Bethesda Game Studios), followed by an analysis of the six tensions that explain why the games
differ and how audiences reacted. Companion file: `systems-comparison.md` (mechanics side by side).

Verification note: the web-search budget for this session ran out part-way through. Statements traced to a
source this session are cited inline. Material from general knowledge of developer talks and reception that was
not re-checked this session is marked `[UNVERIFIED]`.

## Quick Reference

- The original team wrote a short **vision statement** (14 points in the surviving GURPS-era copy). Cain's
  postmortem credits it with keeping the team aligned.
- Its core promises: brutal violence, moral dilemmas with no clean answer, **multiple solutions to every
  problem**, a world that **reacts** to the player, urgency, free travel, player-defined morality, an easy
  interface, and "useful non-combat skills".
- Cain's working rule for quests: every quest supports at least two of fight / talk / sneak; the *main* quest
  must be finishable by any build.
- Cain's humour rule: "If the player doesn't get them, they shouldn't notice them." Fallout 2 broke it;
  Bethesda's lead writer explicitly preferred FO1's bleakness to FO2's camp.
- Perks, the series' most imitated mechanic, were a late addition after the GURPS licence was lost and the rules
  were rebuilt in about two weeks.
- Sawyer's New Vegas principles: respect the build the player made, check many skills, make outcomes
  deterministic rather than reload-bait, track what factions think rather than a morality score, and accept
  that the player cannot fix everything.
- Bethesda's pillars are different in kind: **the world is the main character**. Go anywhere you can see,
  find a self-contained story when you get there, and never be locked out of content by your build.
- "See that mountain? You can go there" is a paraphrase from Todd Howard's 2011 Skyrim presentations, not a
  Fallout quote, but it describes FO3, FO4 and FO76 accurately.
- Bethesda's FO3 combat goal, per Howard: mix real-time and turn-based to appeal to both shooter and RPG fans.
- Every tension below is a trade between **authored depth** and **open-ended breadth**. Black Isle and Obsidian
  spend budget on consequences; Bethesda spends it on places.
- Critics reward breadth and polish at launch (FO3: 91). Long-tail fan reputation rewards depth (FNV: 84 at
  launch, now the consensus favourite among series enthusiasts).
- Sales reward accessibility: FO4 shipped 12 million units in 24 hours and has passed 35 million sold.
- The one experiment Bethesda itself retracted is FO4's voiced protagonist and dialogue wheel ("really did not
  resonate").
- FO76's launch shows the limit: remove authored NPCs and reactivity entirely and the formula collapses
  (Metacritic 49-53). Adding them back (Wastelanders, 2020) began the recovery.
- For an original game the useful question is never "old or new Fallout?" but "which of these trades do we
  make on purpose?"

---

## 1. The original team's rules (Interplay, 1994-1997)

### 1.1 The vision statement

The document was written during development, when the game still used the GURPS tabletop rules. It is credited
to Chris Taylor following team discussion with Tim Cain and others (fallout.wiki / Nukapedia attributions,
via search summary). A forum post claims it was written with management and marketing in mind rather than as
the team's private creed `[UNVERIFIED]`. The copy on RPG Codex lists 14 points:

| # | Point (paraphrased) | Survived into shipped FO1? | Survived the series? |
|---|---|---|---|
| 1 | "Mega levels of violence": shoot almost anything, called shots to body parts, varied gruesome deaths | Yes | Yes, in every game; it is the most durable pillar |
| 2 | Moral dilemmas where nobody can be fully satisfied (the example is taking a part one town needs to save another) | Yes | Strong in FO2/FNV; simplified to good/evil in FO3; faction preference in FO4 |
| 3 | "There will always be multiple solutions": fight, sneak, talk, or walk away | Yes for major quests | Strong in FNV; weak in FO3/FO4; absent in FO76 |
| 4 | The world reacts: NPCs notice what you do; reputation changes how people treat you | Partly | Peak in FO2/FNV; minimal in FO4 |
| 5 | Urgency: a running clock, the villain expanding over time, but enough time to explore | Yes (150 days) | Dropped after FO1 |
| 6 | Open world: travel freely, return to places, find hidden locations | Yes | Yes; became Bethesda's core pillar |
| 7 | Clear goals and a journal device that tracks them | Yes (the Pip-Boy) | Yes |
| 8 | The player chooses to be good or evil; even the villain's offer can be accepted | Yes | Varies; FO4 has no evil path to speak of |
| 9 | Interface that is easy but allows complex actions | Mostly | The 3D Pip-Boy kept the identity, not the ease |
| 10 | Conversations with visible NPC reactions, memory of what you said, and lines limited by the character's intelligence | Yes | Stat-limited dialogue peaks in FNV; gone in FO4 |
| 11 | Big, varied arsenal; gear and injury visible on the character | Yes | Yes |
| 12 | Point-buy character creation, or three pre-mades (fighter, sneak, talker) | Yes | Pre-mades dropped; point-buy survives |
| 13 | Tabletop-grade rules in service of fun: tactical combat, reaction-driven NPCs, **useful non-combat skills** | Partly (several dead skills) | See skills analysis in `systems-comparison.md` |
| 14 | Team enthusiasm; mission "to make a fun RPG in a reasonable amount of time" | - | - |

The phrase "no useless skills" does not appear verbatim in the copy consulted; the nearest text is the
"non-combat skills that are useful" bullet. Treat "no useless skills" as a community paraphrase.

### 1.2 Cain's working rules (from the GDC 2012 postmortem and later commentary)

| Rule | Statement / evidence | Notes |
|---|---|---|
| Three paths | Every quest needed at least two of fighting, talking, sneaking. Main-story quests had to be completable by *any* build and were fixed when they were not. Side quests could be narrower. | Attendee notes of the GDC 2012 talk. A separate summary of Cain's remarks says the main quest must always allow fight, talk or sneak. |
| Consequences over morality | Cain disliked black-and-white morality. Players may behave badly as long as they live with the result. Ending slides exist to show consequences. | Same notes; other interview summaries. |
| Never take the player's agency | Quest ideas of the form "and then the player does this" were rejected. Design assumes nothing about order: do not assume who the player talks to first or where they go. | PC Gamer report of a Cain video on non-linear design (search summary). |
| The game does not expect you to be good | Unlike earlier RPGs that assumed a virtuous hero, Fallout has no such expectation. | Headline-level report of Cain's remarks (search summary). |
| Jokes must be invisible if missed | "If the player doesn't get them, they shouldn't notice them." References must not date or break the fiction. | GDC 2012 notes. |
| Setting first, systems serve it | Systems should support the setting and story. | Report of a Cain video on design documents (search summary). |
| Less is more | "A game that includes everything is about nothing" (quoted by Cain from another designer). | PC Gamer headline (search summary). |

Other facts from the postmortem that matter for design reasoning:

- GURPS's owner withdrew late, objecting to violence and art style; the team rebuilt skills and combat in
  about two weeks. Cain wanted the system named for its attribute initials; a colleague suggested arranging
  them as SPECIAL.
- **Perks were added late**, were quick to implement and gave characters variety.
- The team aimed for a Teen rating and got Mature. Children could be killed, with a heavy reputation penalty;
  the European release removed children.
- The time limit was argued over for months, and Cain says removing the timed quest is the one change he
  would make. (The notes say a release-day patch removed it; the shipped game retains the 150-day limit, so
  this likely refers to the second, hidden deadline. `[DISPUTED]`)
- After Diablo's success the publisher asked for real-time and multiplayer. The team investigated and declined.
  The pressure toward action existed in 1997; Bethesda did not invent it.
- The pacifist route was, by Cain's account, unplanned: it fell out of the multiple-solutions rule and the
  team kept it (PC Gamer headline; article body not retrievable this session).

### 1.3 The humour ratio

There is no verified numeric "dark humour ratio" in the sources consulted this session; any specific percentage
attributed to the original team should be treated as `[UNVERIFIED]`. What is documented:

- The tone target was a serious, brutal world with dry, ironic humour arising from the contrast between
  cheerful pre-war optimism and the ruin it produced.
- Cain's invisibility rule (above).
- Silly content in FO1 was quarantined in rare *special random encounters* that scale with the Luck stat. The
  main locations are played straight.
- Fallout 2 (made largely without Cain, Boyarsky and Anderson, who left early in production `[UNVERIFIED]`)
  moved jokes into main locations and dialogue: film and TV references, talking animals, fourth-wall breaks.
  Reporting on Cain's views says he felt too much of that humour needed outside pop-culture knowledge.
- Emil Pagliarulo is on record (per Wikipedia's FO3 article) as preferring FO1's oppressive, bleak atmosphere
  over FO2's campier tone when setting FO3's voice.
- FNV made the split explicit with the **Wild Wasteland** trait: the overt gags are opt-in.

Working formulation for our purposes: *the world never knows it is funny*. Characters are sincere; the comedy
is in the gap between their sincerity and their circumstances. Jokes that wink at the player belong in an
optional layer.

### 1.4 Moral ambiguity

The vision document's own examples are structural, not atmospheric: a resource two towns both need; two
flawed leaders where backing one dooms the other. FO1's ending adds the sharpest instance: success is
"rewarded" with exile. The principle is not "grey for its own sake" but **every gain has a named loser**.

---

## 2. Sawyer and Obsidian (Fallout: New Vegas, 2010)

Josh Sawyer was project director and lead designer of FNV, built in about 18 months on FO3's engine with an
"add to it, don't change it" approach to the inherited toolset (Wikipedia). His GDC 2012 talk "Do (Say) The
Right Thing: Choice Architecture, Player Expression, and Narrative Design in Fallout: New Vegas" is the
primary statement; it was identified but not viewed this session, so points attributed to it below are from
secondary summaries and general knowledge `[UNVERIFIED]` unless another source is given.

| Principle | Statement / evidence | How FNV implements it |
|---|---|---|
| Respect the build | Front-loading varied skill checks tells the player "we're paying attention to the character that you made" (GamesRadar report of Sawyer). | The first town offers checks for Speech, Barter, Explosives, Sneak, Medicine, Science in one quest. |
| No useless skills, enforced | Obsidian tracked skill-check distribution with an internal tool; the aim is "a rewarding level of feedback", judged by feel, not strict numeric parity (80.lv). A PC Gamer headline has him describing people who go through the game ensuring every skill gets enough to do. | Every skill has dialogue checks; Survival, Barter and Repair gained uses FO3 never gave them. |
| Deterministic, visible checks | "I didn't like the randomization and the save scumming that resulted" from FO3's percentages (Gameranx, citing a Kinda Funny interview). | Threshold checks with the requirement shown; temporary boosts from magazines make planning part of play. |
| Meaningful, not merely numerous, choices | The talk's abstract says RPG conversation structure had barely changed in a decade and asks how branching dialogue can be good gameplay, serve the narrative and support agency. A forum summary of the slides: no single right answer; each option has virtue and sacrifice. | Major faction choices each cost something concrete; false choices and "ask everything" hubs are minimised. |
| Reputation, not morality | His talk "Reputation Overload" traces reputation mechanics historically (GameBanshee). | Fame and infamy per faction; karma kept only vestigially. |
| The player cannot fix everything | Reported remarks: RPGs should be messy and force hard decisions; he finds it uninteresting when the protagonist can save everyone (inkl / Kotaku / Game Developer headlines). | No "golden" ending. Every victor leaves someone worse off in the slides. |
| The world has shape | Deadly creatures near the start are a warning to players expecting FO3's roam-anywhere ease (PC Gamer / 80.lv headlines). | A soft-gated loop road; fixed rather than scaled danger. |
| Slow the power curve | Halved perk rate, raised weapon requirements, optional Hardcore mode. His later personal mod lowers the level cap and lightens the player's carrying capacity `[UNVERIFIED]`. | Scarcity as an opt-in design stance. |
| Let anyone die | Nearly every NPC is killable; one indestructible robot guarantees an ending. | Kill-everyone and zero-kill runs are both documented. |

Reading: Sawyer's programme is the 1997 vision statement turned into *process*. The original team stated
"multiple solutions" and "useful non-combat skills"; Obsidian built tracking tools and review passes to make
them true.

Known weaknesses of the approach, acknowledged by critics and partly by Sawyer: threshold checks have no
tension; tagged options are nearly always optimal; one faction (the slaver army) is thinly built in the east
of the map because of schedule, so the "balanced" choice is lopsided in practice `[UNVERIFIED]`; and the world
map is sparser and less inviting to wander than FO3's.

---

## 3. Bethesda Game Studios (Fallout 3, 4, 76)

Bethesda has never published a Fallout vision statement comparable to Interplay's. Its pillars are inferred
from repeated public statements and from the games.

| Pillar | Statement / evidence | Implementation |
|---|---|---|
| The world is the main character | Howard's 2011 Skyrim demos produced the "see that mountain, you can go there" line (meme form of his statements; PC World's write-up has him saying you can walk to the top of the mountain). He also described designing for what the player sees from any vantage point. | Seamless map, landmark silhouettes on the horizon, a compass that pulls you toward undiscovered icons. |
| Live another life; be anyone | Reported Howard rationale for classless builds: players should not waste time by committing to a wrong build early (TweakTown report, search summary). | No build can be locked out of the main content. Uncapped levelling in FO4. |
| Environmental storytelling | Not a slogan but the studio's signature craft: posed skeletons, terminal diaries, vault experiments. Pagliarulo has said the difference in writing Fallout is how the player pieces the story together (GamesRadar headline). | Most locations contain a small closed narrative told by objects, independent of quests. |
| Accessible, cinematic combat | Howard wanted FO3 combat to blend real-time and turn-based to serve shooter and RPG fans; the slow-motion kill camera drew on racing-game crash replays (Wikipedia). | VATS; later a full shooter. |
| Legible progression | FO4 removed skills because perks had grown to cover their role; one chart shows the whole character (Escapist and contemporaneous coverage). | The perk poster. |
| Keep the story simple | Pagliarulo's conference talks argue for simple, clear plots because players in an open world will ignore and scramble the narrative `[UNVERIFIED wording]`. | Family-search main quests (find father; find son) as a spine that tolerates distraction. |
| Player-made content | Settlements (FO4) and camps (FO76); deep official mod support. | Building as a main loop. |
| Systems that generate endless play | Radiant quests (from Skyrim), legendary loot rolls, daily events. | "Another settlement needs help" errands; FO76's live structure. |
| Tone | Pagliarulo preferred FO1's bleakness and wanted "rawness" (Wikipedia). In practice Bethesda's Fallout leans on retro-future Americana iconography and spectacle. | Giant robot, nuclear town, mascot branding. |

Reading: Bethesda is not failing at Interplay's goals; it is pursuing different ones. Its implicit vision
statement would read: *the player can go anywhere, find something there, and never be told no*. "Never be
told no" is in direct conflict with "your choices have consequences", because a consequence is a "no" to some
other path.

Self-criticism on record: Howard has said FO4's dialogue system "didn't work as well" (2016) and "really did
not resonate" (later interview), tying it to players wanting more role-play than a voiced protagonist allowed.
FO3 developers considered the shooting one of the weaker elements (Wikipedia). FO76's launch premise (every
human is a real player) was reversed by Wastelanders in April 2020.

---

## 4. Pillars side by side

| Question | Interplay / Black Isle (FO1/2) | Obsidian (FNV) | Bethesda (FO3/4/76) |
|---|---|---|---|
| What is the game about? | A character you built, making hard choices | Factions and what they cost | A place you explore |
| Unit of content | The town and its problem | The faction and its quest web | The location and its found story |
| What does a stat do? | Opens and closes solutions | Opens and closes solutions, visibly | Makes you better at what everyone can do |
| What is a quest? | A problem with several exits | A problem with several exits and a political price | A reason to visit a location |
| Can the player fail or be locked out? | Yes, routinely | Yes, with warnings | Rarely |
| Where does humour live? | Dry irony; gags in rare encounters (FO1), everywhere (FO2) | Dry irony; gags opt-in | Iconography, spectacle, terminals |
| How does the story end? | A reckoning: slides | A reckoning: slides | It doesn't; keep playing |
| Replay model | New build, new outcomes | New allegiance, new build | Same save, more map; or mods |

---

## 5. The central tensions

For each: the two poles, where each game sits, how audiences responded, and a position.

Positions use a 1-5 scale where 1 is fully the first pole and 5 fully the second. They are this author's
judgement, informed by the mechanics in `systems-comparison.md`.

### 5.1 RPG depth vs. action accessibility

Does the *character's* ability or the *player's* reflexes decide outcomes?

| Game | Position (1 = character skill, 5 = player skill) | Evidence |
|---|---|---|
| FO1 | 1 | Turn-based; to-hit is a dice roll; a bad build cannot be rescued by dexterity |
| FO2 | 1 | Same |
| FO3 | 3 | Real-time shooting with skill-driven spread; VATS as dice mode; weak gunplay |
| FNV | 3 | Same base, iron sights added, more stats feeding weapon handling |
| FO4 | 4.5 | Competent shooter; stats affect damage, not whether you hit |
| FO76 | 5 | Online shooter; real-time VATS as aim assist |

Audience response:

- FO3 was the commercial and critical breakthrough: Metacritic 91-93, 4.7 million shipped in week one, and it
  outsold all prior entries combined (Wikipedia). The fan communities of the originals (No Mutants Allowed,
  RPG Codex) rejected it as "Oblivion with guns" `[UNVERIFIED phrasing]`; the mainstream never heard the
  objection.
- FO4 sold far more again (12 million shipped in 24 hours; 35 million lifetime by 2026 per Wikipedia) while
  reviews specifically criticised simplified role-playing.
- FNV scored lower at launch (82-84), mainly for bugs, and has since become the entry most often cited by
  enthusiasts and other developers as the series' best RPG.

Position: accessibility wins sales and depth wins loyalty, and they are not strictly opposed. The mistake is
letting action *replace* character expression instead of sitting beside it. VATS, the critical meter and
FNV's stat-driven weapon handling show the two can stack. An original game should let player skill decide
*execution* while character build decides *what options exist* (which weapons are usable, which routes are
open, which conversations are possible).

### 5.2 Authored reactivity vs. sandbox freedom

Does the game remember what you did, or let you do everything?

| Game | Position (1 = authored reactivity, 5 = unreactive sandbox) | Evidence |
|---|---|---|
| FO1 | 2 | Small, dense, per-town outcomes; unplanned pacifist route |
| FO2 | 1.5 | Town reputations, titles, wide quest interlock |
| FO3 | 4 | A handful of famous big choices (the bomb town); most content sealed off from the rest; essential NPCs |
| FNV | 1 | Faction web, mutual exclusivity, killable NPCs, granular slides |
| FO4 | 4.5 | Three factions playable in parallel; endings converge; radiant filler; wheel dialogue |
| FO76 | 5 (launch) → 4 | Shared persistent world cannot change for one player; instanced choices added later |

Audience response:

- FO3's ending drew enough criticism (a forced sacrifice that ignored available companions; Cain's remark that
  the endings were not built from player decisions) that Bethesda rewrote it in DLC.
- FO4's reception is the cleanest data point: strong reviews and sales alongside a durable complaint about
  thin choice and the dialogue wheel, acknowledged by its own director.
- FO76 at launch had no human NPCs so that any human you met was a real player (Wikipedia). Metacritic 52 /
  53 / 49. Wastelanders reintroduced NPCs, dialogue lists and stat checks; re-reviews rose to the 60s.

Why the tension is real and not just a budget excuse: reactivity scales with the *product* of choices, a
sandbox scales with the *sum* of places. A studio can afford 300 locations or 30 locations that know about
each other. Bethesda's seal-each-location approach is what makes its content pipeline parallelisable.

Position: for a new game with a smaller budget, reactivity is the affordable differentiator. It is cheap per
unit (flags, alternate lines, slides) and catastrophically expensive only when voiced and cinematic. Build a
smaller world that knows itself.

### 5.3 Build identity vs. master-of-all

Is a character defined by what they cannot do?

| Game | Position (1 = hard identity, 5 = everyone converges) | Evidence |
|---|---|---|
| FO1 | 1.5 | Cap 21, about 7 perks, fixed stats |
| FO2 | 2.5 | Cap 99 lets grinders converge; normal play does not |
| FO3 | 5 | Every skill maxable; perk per level; a perk that sets all stats to 9 |
| FNV | 3 | Slower perks; DLC cap of 50 erodes it |
| FO4 | 4 | Early identity, no cap, convergence by attrition |
| FO76 | 3 | Owns everything, equips a slice; identity is a loadout |

Audience response: players rarely complain about power in the moment. Convergence shows up as *lack of
replay motive* and as forum consensus that "every FO3/FO4 character ends up a stealth sniper". Conversely
FO1/FO2/FNV sustain build-challenge communities decades on (low-Intelligence, unarmed-only, pacifist runs).
Bethesda's counter-argument is honest: most players finish one playthrough, and locking them out of content
for a choice made in hour one is a cost. FO76's "own all, equip some" is the only design in the series that
answers both sides.

Position: commit. A build should close doors, and the game should make the closed doors visible enough that
players want a second run. Offer limited, costly respec rather than convergence.

### 5.4 Scarcity and survival vs. power fantasy

Is the wasteland something you endure or something you conquer?

| Game | Position (1 = scarcity, 5 = power fantasy) | Evidence |
|---|---|---|
| FO1 | 2 → 4 | Brutal opening hours; power armor and plasma make the last third a victory lap |
| FO2 | 2 → 4.5 | Famously harsh start (spear and loincloth), absurd late-game power |
| FO3 | 3.5 | Early ammo pressure, quickly drowned in supplies and caps |
| FNV | 3 (2 in Hardcore) | Tighter economy, real sinks, optional needs |
| FO4 | 4.5 (2 in Survival) | Power armor and a minigun in the first hour; Survival mode inverts the whole game |
| FO76 | 3 → 4 | Launched as a survival game; upkeep penalties later removed |

Audience response:

- FO4 handing over power armor in its first major quest is the most cited example of the series abandoning the
  long climb. It makes a great trailer and removes the best reward the earlier games had to give.
- FNV Hardcore and FO4 Survival are both praised well beyond their usage numbers and are frequently named as
  the "right" way to play. Both are opt-in.
- FO76's mandatory needs were unpopular and were turned into optional bonuses.

Every game in the series has the same curve problem: scarcity collapses by the midpoint because loot is
additive and sinks are few. No entry sustains it to the end without a special mode.

Position: scarcity should be the default identity of a post-apocalyptic game and should be defended by
systems (weight, sinks, repair, fixed loot in key places), not by a difficulty toggle. Power should arrive
late, be earned and come with upkeep. The first suit of heavy armor should be a mid-game event the player
remembers.

### 5.5 Humour vs. bleakness

| Game | Position (1 = bleak, 5 = zany) | Evidence |
|---|---|---|
| FO1 | 2 | Grim main line, dry irony, gags hidden in rare encounters |
| FO2 | 4 | Pop-culture references, talking creatures, fourth-wall jokes in main content |
| FO3 | 2.5 | Bleak palette and tone by intent; absurd set-pieces (a superhero feud, a town around a bomb) |
| FNV | 2.5 (3.5 with Wild Wasteland) | Political and dry by default; gags behind a trait; the most comedic DLC is fenced off |
| FO4 | 3 | Sentimental family drama plus mascot-heavy retro kitsch |
| FO76 | 3.5 | Tragic backstory told through holotapes; theme-park presentation and cosmetics |

Audience response: FO2's humour is the oldest fault line in the fandom; it is loved as content and blamed for
diluting the setting, and both original leads and Bethesda's writer came down on the bleaker side. The
franchise's mass-market image is nonetheless the *comic* one: the smiling mascot, the jingles, the 1950s
kitsch. The 2024 television adaptation's success with that blend (and the resulting record FO76 logins)
suggests the general audience comes for the tonal contrast itself `[UNVERIFIED causal link]`.

Position: the contrast is the asset; neither pole works alone. Follow Cain's rule (invisible if missed) and
the sincerity rule (the world does not know it is funny). Quarantine reference humour. Above all, an original
game needs its *own* source of irony. Fallout's is pre-war consumer optimism; borrowing that would be both
derivative and off-limits. Find a different sincere lie for the old world to have believed.

### 5.6 Handcrafted vs. radiant / procedural content

| Game | Position (1 = all handcrafted, 5 = generated) | Evidence |
|---|---|---|
| FO1 | 1.5 | Authored quests; random encounters as procedural seasoning |
| FO2 | 1.5 | Same, more of both |
| FO3 | 2 | Handcrafted; a few repeatable turn-ins; scaled spawn lists |
| FNV | 1.5 | Handcrafted; minimal repeatables |
| FO4 | 3.5 | Radiant faction errands, settlement defence, legendary loot rolls, build-your-own towns |
| FO76 | 4.5 | Dailies, public events, loot rolls and seasons as the core loop |

Audience response:

- FO4's radiant settlement errands became a long-running joke and are consistently named among its worst
  features in reviews and community discussion; critics noted that some are required for faction progress.
- The *systems* that generate play (legendary drops, junk economy, building) are popular. The *quests* that
  are generated are not. Players accept procedural rewards and reject procedural stories.
- FO1/FO2's random encounters are remembered fondly because they were short, optional, sometimes unique, and
  never pretended to be quests.

Position: generate *situations*, not *quests*. Random encounters on the road, patrol clashes, weather,
scarcity events and loot variance are welcome. Anything with a quest-giver, a journal entry and a line of
dialogue should be authored. Never gate authored progress behind generated chores.

### 5.7 Summary matrix

| Tension | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Character skill (1) vs. player skill (5) | 1 | 1 | 3 | 3 | 4.5 | 5 |
| Reactive (1) vs. sandbox (5) | 2 | 1.5 | 4 | 1 | 4.5 | 5 → 4 |
| Build identity (1) vs. master-of-all (5) | 1.5 | 2.5 | 5 | 3 | 4 | 3 |
| Scarcity (1) vs. power fantasy (5) | 2 → 4 | 2 → 4.5 | 3.5 | 3 | 4.5 | 3 → 4 |
| Bleak (1) vs. zany (5) | 2 | 4 | 2.5 | 2.5 | 3 | 3.5 |
| Handcrafted (1) vs. generated (5) | 1.5 | 1.5 | 2 | 1.5 | 3.5 | 4.5 |

| Reception | FO1 | FO2 | FO3 | FNV | FO4 | FO76 |
|---|---|---|---|---|---|---|
| Metacritic (PC) | high 80s `[UNVERIFIED]` | mid 80s `[UNVERIFIED]` | 91 | 84 | 84 | 52 (68 after Wastelanders) |
| Commercial | Modest hit `[UNVERIFIED]` | Modest `[UNVERIFIED]` | 4.7M shipped week one; est. 12.4M by 2015 | 5M in three weeks; est. 11.6M by 2015 | 12M shipped day one; 35M+ lifetime | Est. 1.4M digital in 2018; 17M players by 2024 |
| Enthusiast standing today | Revered | Revered, tone disputed | Respected for atmosphere and exploration | Most admired as an RPG | Admired for feel, building, mods; criticised as an RPG | Rehabilitated; still divisive |

Pattern: moving right on the first four rows correlates with larger audiences. Staying left on the second
and third rows correlates with lasting esteem. FNV is the proof that left-leaning design can still sell
(5 million in three weeks) when it rides an accessible chassis.

---

## 6. How the pillars interact

The tensions are not independent. Three causal chains explain most of the series:

1. **Seamless open world → sealed locations → low reactivity.** If the player can arrive anywhere in any
   order, each location must work alone. That favours found stories over interlocked quests. FNV escaped this
   by shaping the map into a soft loop so designers could predict order.
2. **No lock-outs → no cap → convergence → scaling.** If no build may miss content, everyone must be able to
   do everything; then enemies must scale to keep up; then progression feels flat; then loot variance
   (legendaries) is added to restore excitement.
3. **Voiced cinematic dialogue → fewer options → wheel → no skill checks.** Voice budget caps line count;
   capped lines cap branching; four slots cap expression. The reverse chain (silent protagonist → cheap lines →
   many gated options → failure content) is why FNV could ship its breadth in 18 months.

A fourth, on the older side: **dice-driven combat + free saving → reload culture → consequences feel
optional.** The originals' reactivity was always partly undermined by the quick-load key.

---

## Design Takeaways

Process

- **Write a one-page vision statement and use it to cut features.** Cain credits the document itself. Ours
  should name what the game refuses to be, since "a game that includes everything is about nothing".
- **Turn every pillar into an audit.** "Multiple solutions" becomes a checklist per quest (two of three
  paths minimum; main quest passable by every build). "No useless skills" becomes a tracked count of uses per
  skill per region. Obsidian's tooling is the lesson; Interplay's good intentions were not enough.
- **Pick positions on the six tensions before building anything**, write them down, and treat drift as a
  decision requiring sign-off. Fallout's weakest moments are drift (FO3's skills, FNV's level cap, FO4's
  dialogue), not choices.

Recommended positions for an original, smaller-budget game

- **Depth vs. action: hybrid, with the build deciding options and the player deciding execution.** Do not
  ship combat where stats are cosmetic, and do not ship combat where the player's hands are irrelevant.
- **Reactivity vs. sandbox: lean hard to reactivity.** A compact map where factions and towns know about each
  other, silent protagonist, text-first dialogue, no essential NPCs, one fail-safe ending path, ending slides.
  This is the cheap, defensible niche that large studios have vacated.
- **Identity vs. mastery: hard budget.** Scarce rule-changing perks, creation-time trade-offs, a real cap.
  Make closed doors visible so they advertise the next playthrough.
- **Scarcity vs. power: scarcity by default, defended by systems.** Design sinks first. Delay the power-armor
  moment. Fold the "survival mode" rules into the base game at a tolerable intensity rather than hiding the
  best version of the game behind a toggle.
- **Humour vs. bleakness: sincere world, dry irony, reference humour quarantined behind an opt-in.** Invent an
  original ironic engine for the setting; do not borrow the atomic-age-optimism one.
- **Handcrafted vs. generated: generate situations and rewards, author everything with a name and a voice.**
  Bring back the travel-encounter layer as the procedural spice.

Specific things to copy in spirit

- The rule that the game "does not expect you to be good", paired with consequences rather than a morality
  meter.
- Dilemmas built as *resource conflicts with a named loser*, not as good/evil prompts.
- Front-loaded build recognition in the first settlement.
- Environmental vignettes as a second narrative channel, used *alongside* reactive quests rather than instead
  of them. Bethesda's craft here is real and is compatible with Obsidian-style structure; no game in the
  series has fully combined them.
- A diegetic interface device as the visual identity of the game.

Specific things to avoid

- A hard timer on the opening objective; equally, a premise that screams urgency with no mechanical truth.
- Percentage-roll dialogue with free reloads.
- A voiced protagonist or a capped-slot dialogue wheel.
- Perks that are mandatory damage taxes.
- Global level scaling and health-sponge difficulty.
- Protecting content from the player with unkillable NPCs.
- Generated chores presented as quests, or placed on the critical path.
- Letting DLC or late-game rewards dissolve the build budget.
- Handing out the setting's most iconic power in the first hour.

## Sources

Consulted this session (fetched, or search-result summaries used):

- Fallout GURPS-era vision statement (full 14-point text and commentary), RPG Codex: https://rpgcodex.net/article.php?id=8028
- Fallout vision statement, wiki attributions (search summary): https://fallout.fandom.com/wiki/Fallout_vision_statement
- GamesRadar, "Fallout: The original vision" (search summary): https://gamesradar.com/fallout-the-original-vision
- Notes on Tim Cain's GDC 2012 "Classic Game Postmortem: Fallout": https://thiscageisworms.com/2012/04/09/tim-cains-gdc-2012-talk-fallout/
- GDC announcement of Cain's postmortem (search summary): https://gdconf.com/news/fallout-dev-timothy-cain-heads-gdc-showcase-revisit-classic-game-postmortem
- PC Gamer, Cain on non-linear design and never assuming player behaviour (search summary): https://www.pcgamer.com/games/fallout/fallout-co-creator-says-non-linear-design-is-all-about-never-assuming-how-players-will-act-illustrates-his-point-by-fantasising-about-an-npc-guard-he-seems-to-really-hate/
- PC Gamer, Cain: "a game that includes everything is about nothing" (search summary): https://www.pcgamer.com/gaming-industry/fallout-co-creator-tim-cain-says-less-is-often-more-in-game-design-as-a-very-wise-designer-once-said-to-me-a-game-that-includes-everything-is-about-nothing
- Game World Observer, Cain on reactivity (search summary): https://gameworldobserver.com/2022/11/18/tim-cain-fallout-inverview-reactivity-rpg-system-professional-limits
- PC Gamer, FO1 pacifist route was accidental (headline only): https://www.pcgamer.com/the-original-fallouts-pacifist-playthrough-was-an-accidental-inclusion-but-its-designers-loved-the-idea-so-much-they-kept-it-in
- GDC Vault listing, Sawyer, "Do (Say) The Right Thing" (abstract via search; talk not viewed): https://gdcvault.com/play/1015758/Do-(Say)-The-Right-Thing
- Obsidian forum thread on the GDC 2012 talks (search summary): https://forums.obsidian.net/topic/59386-obsidian-at-gdc-2012/
- GameBanshee, "Reputation Overload" by Josh Sawyer (search summary): https://www.gamebanshee.com/36qhk
- Gameranx, Sawyer on FO3 percentage checks and save scumming: https://gameranx.com/updates/id/402854/article/fallout-new-vegas-director-didnt-like-save-scumming-in-fallout-3/
- 80.lv, Sawyer on distributing skill checks: https://80.lv/articles/fallout-new-vegas-lead-on-how-game-developers-distribute-skill-checks
- GamesRadar, Sawyer on the FNV opening respecting skill choices (search summary): https://www.gamesradar.com/games/fallout/fallout-new-vegas-director-josh-sawyer-explains-why-the-rpgs-opening-is-a-perfect-example-of-respecting-the-players-skill-choices
- PC Gamer, Sawyer on skill coverage (headline only): https://pcgamer.com/games/fallout/fallout-new-vegas-director-josh-sawyer-says-obsidian-has-karma-police-who-go-through-the-game-making-sure-every-skill-gets-enough-cool-stuff-to-do-were-not-gonna-leave-you-out-to-dry/
- PC Gamer, Sawyer on deathclaws and cazadores as a warning (search summary): https://pcgamer.com/games/rpg/josh-sawyer-says-fallout-new-vegas-has-deathclaws-in-cazador-as-a-warning-to-fallout-3-players-expecting-another-easy-ride-you-cant-just-slide-all-over-the-map-and-not-feel-the-heat
- Kotaku / Game Developer, Sawyer on players not controlling everything (search summaries): https://kotaku.com/reported-director-of-obsidians-upcoming-fallout-game-says-rpgs-are-at-their-best-when-you-cant-control-everything-2000717793 and https://www.gamedeveloper.com/design/pentiment-director-emphasizes-the-importance-of-rpg-players-not-controlling-everything
- PC World, E3 2011 Skyrim demo write-up (origin of the mountain line; search summary): https://www.pcworld.idg.com.au/article/389723/e3_2011_watch_elder_scrolls_v_skyrim_demo/
- Unwinnable, "Climbing the Virtual Mountain" (search summary): https://unwinnable.com/?p=70284
- TweakTown, Howard on classless builds (search summary): https://www.tweaktown.com/news/89748/all-new-bethesda-rpgs-to-offer-classless-builds-so-gamers-dont-waste-time/index.html
- Escapist, "Fallout 4 Eliminates Skills From Character System" (search summary): https://www.escapistmagazine.com/fallout-4-eliminates-skills-from-character-system/
- PC Gamer, Howard on FO4 dialogue: https://www.pcgamer.com/au/fallout-4-lead-todd-howard-dialogue-system-didnt-work-as-well and https://www.pcgamer.com/games/rpg/todd-howard-says-that-fallout-4s-cinematic-dialogue-system-really-did-not-resonate-with-players-even-though-bethesda-spent-forever-working-on-it
- GamesRadar, Pagliarulo on piecing the story together and on FO4's interwoven factions (search summaries): https://www.gamesradar.com/games/fallout/bethesda-lead-says-the-biggest-difference-between-a-fantasy-rpg-like-skyrim-and-a-sci-fi-rpg-like-fallout-is-how-you-piece-together-the-story and https://www.gamesradar.com/games/fallout/fallout-4s-interweaving-quests-were-a-massive-departure-from-oblivion-and-skyrim-but-it-makes-the-rpg-the-most-replayable-of-all-the-fallout-games
- GameBanshee, Pagliarulo STORY conference keynote (listing only): https://gamebanshee.com/kwyyw
- SiliconANGLE, "What Fallout 4 should have learned from The Witcher 3" (radiant quests; search summary): https://siliconangle.com/2015/12/04/what-fallout-4-should-have-learned-from-the-witcher-3/
- Kotaku, FNV zero-kill run (search summary): https://kotaku.com/this-guy-beat-fallout-new-vegas-with-zero-kills-5683023
- Guinness World Records, FO4 Survival pacifist run: https://www.guinnessworldrecords.com/world-records/438856-fastest-pacifist-completion-of-fallout-4-on-survival-mode
- fallout.wiki pages on FO4 perks, FO76 SPECIAL, One Wasteland, FNV damage threshold (see `systems-comparison.md` for URLs)
- Wikipedia: https://en.wikipedia.org/wiki/Fallout_3 , https://en.wikipedia.org/wiki/Fallout:_New_Vegas , https://en.wikipedia.org/wiki/Fallout_4 , https://en.wikipedia.org/wiki/Fallout_76 , https://en.wikipedia.org/wiki/Fallout_(video_game) (search summary)

Not reachable or not viewed this session: Tim Cain's own YouTube videos (only third-party reports), Sawyer's
GDC 2012 talk recording and slides, Pagliarulo's conference talk, RPG Codex / NMA / Reddit reception threads
(search budget exhausted before these were queried). Claims that depend on them are marked `[UNVERIFIED]`.
