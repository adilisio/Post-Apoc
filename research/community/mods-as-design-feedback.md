# Mods as Design Feedback: What Players Fix, Add and Rebuild

Purpose: treat the most-installed and most-recommended Fallout mods as an unsolicited bug report and feature request from the player base. Where a mod category is near-universal in modding guides, the shipped game left a gap.

**Evidence quality note.** Nexus Mods, ModDB, Fandom and most review sites returned 403/402/404 to fetches and the search quota ran out during this session. Verified here: the structure and contents of the Viva New Vegas (VNV) and The Midnight Ride (TMR) guides, the sfall and Restoration Project GitHub READMEs, and Wikipedia facts. Exact Nexus download counts could NOT be retrieved; every "popularity" statement below is therefore either (a) "appears in the curated guide" (verified inclusion) or (b) marked `[UNVERIFIED]` where it rests on background knowledge. No download totals are quoted except where a source was fetched.

## Quick Reference

- Every serious modding guide for Fallout 3/NV/4 opens with the same thing: stability. VNV's own intro lists "stability, performance, customization" as goals; TMR lists the same four. The shipped games were not stable enough to play as-is.
- Community unofficial patches exist for every post-FO1 game (FO2 unofficial patch inside the Restoration Project; YUP/UNVP for NV; UFO4P for FO4). TMR calls UFO4P a fix for "thousands of bugs" in base game and DLC; VNV says the same of YUP.
- Engine-level fixes via script extenders (sfall for FO2; xNVSE plus JIP LN, JohnnyGuitar, ShowOff, ITR for NV; F4SE plus Addictol for FO4) are mandatory in modern setups. The 4GB patcher is a first-run step for NV.
- Performance fixes are separate from bug fixes: New Vegas Tick Fix (micro-stutter), mesh/LOD fixes, previsibine repair for FO4, BSA decompression. Players fix frame pacing, not graphics fidelity.
- UI is the second most-modded layer. VNV lists 13 UI mods (menu search, config menu, HD HUD/screens, recipe menu, hardcore-needs preview). TMR's UI list is tiny because the mainstream FO4 UI replacers are in Extended/other lists; but FO4 players also patch crafting and workshop highlight readability.
- Search in inventory/barter/crafting lists is a top QoL request (VNV "Menu Search" adds Ctrl-F to six menus).
- Rebalancing is the third pillar: VNV Extended's first gameplay entry is "Agua Fria - JSawyer Redone" (lower starting HP and carry weight, slower leveling, lower level cap, reworked Hardcore). Players want a slower, scarcer power curve.
- Loot density is a complaint in FO4: TMR ships Loot Logic and Reduction (less ammo/meds/pins, sensible containers) and SPARS (fewer power armor parts). Over-generous, random loot undermines scarcity.
- Quest-giver friction is fixed by mods: TMR ships "Who's The General" to stop Preston Garvey issuing a new quest on every turn-in and to cut reporting back. Radiant quest spam and nagging NPCs are a consistent pain.
- Vendors: TMR "Complex Vendors" makes merchants buy only what they sell. Players want a coherent economy.
- Combat feel is patched: manual reload, ammo memory, recoil systems, hit markers, hit indicators, dynamic crosshair, cookable grenades, viewmodel shake and iron-sight alignment (all in VNV). Shooting was the weak half of Bethesda-engine hybrids.
- Companions: follower AI fixes (F4SE approach-reaction fix), Dogmeat as an extra companion, Dogmeat lagging behind instead of running ahead. Followers are a major source of friction.
- World reactivity: VNV Extended's "The Living Desert" adds hundreds of NPCs and scripted events "to make the world feel more alive"; TMR adds consequences for clearing dungeons (Reinforcements and Retribution) and checkpoint refresh. Static cleared worlds feel dead.
- Total conversions are the biggest evidence of unmet demand. Fallout: London (FO4 mod, 25 July 2024) was downloaded over 500,000 times in 24 hours (Wikipedia, citing GOG) with ~100 modders and 100+ voice actors, despite being widely reported as buggy at launch (IGN 7/10).
- Players want the previous game's best-loved qualities more than new tech: Tale of Two Wastelands (FO3 + NV in one engine) and Fallout 1 in Fallout 2's engine (Fo1in2, 851 GitHub stars) are mergers of old content into better engines.
- Survival/needs are optional-by-mod for NV (Hardcore mode extensions, "Sleep Wait Hardcore Needs") and a Survival-mode patch for FO4 (Unlimited Survival Mode, Safe Travels). Players want hardcore modes, but want the annoying parts (no saves, no fast travel) made configurable.
- Fallout 76 has no mod support beyond cosmetic/UI; Bethesda has banned players for mod use (Wikipedia), and players said bans hit mods that fixed visuals/technical issues. Ban risk is itself a community grievance.
- Verified note: the Fallout 4 Anniversary Edition (2025) "broke popular mods" and was received negatively (Wikipedia). The next-gen update (April 2024) also broke mod support. Breaking the modding ecosystem is a recurring community flashpoint.

## 1. Fallout 1 and Fallout 2 (classic engine)

| Problem | Mods / projects | Evidence in sources | Design lesson |
|---|---|---|---|
| Modern OS, resolution, crashes | sfall (DLL engine modification; fixes bugs, adds scripting opcodes, item highlight button, party member control, configurable skills/perks/crit tables); now bundled with Steam/GOG FO2 (SFALL 4.4.5 per Wikipedia) | sfall GitHub README; Wikipedia Fallout 2 | A fan DLL became the official-distribution default. Ship modern resolution, scaling, saves and compatibility yourself. |
| Shipped bugs and cut content | Killap's Restoration Project (RP) and its successor "Restoration Project, updated" (RPU): bundles Unofficial Patch, hero appearance, NPC armor visuals, Party Orders, enhanced worldmap, hi-res patch, etc.; 6,154 commits on GitHub | RPU GitHub README (verified) | Interplay's last patch (1.02d, 11 Feb 1999) fixed "major bugs" but the community kept patching for 25+ years. Content cut for schedule gets restored by fans. |
| Party control | "Party Orders" (RPU), sfall party member control | RPU / sfall READMEs | Players want some command over companion tactics. FO1 reviews already faulted lack of direct companion control (Wikipedia). |
| FO1 in a better engine | Fo1in2 (Fallout 1 in Fallout 2 engine): merchant restocking, motorcycle travel, "tougher mutants" option, integrated Hero Appearance | GitHub README (verified) | Two content sets, one engine: fans merge games. Design for forward-compatibility of saves/content. |
| Fan sequels / total conversions on classic engine | Fallout 1.5: Resurrection, Olympus 2207, Fallout: Nevada, Fallout: Sonora, Nuclear Highway (ModDB) | ModDB blocked (403); existence from background knowledge `[UNVERIFIED]` for details | Classic-engine TCs exist because the isometric, turn-based, text-heavy form has no modern commercial equivalent from the franchise holder. |
| Appearance customization | Hero Appearance Mod (bundled in RPU and Fo1in2) | READMEs | Character visibility in isometric view is a long-standing want. |

Confidence: the sfall/RPU/Fo1in2 rows are verified from READMEs. The specifics for Resurrection, Olympus 2207, Nevada and Sonora (release dates, scope, completion) are `[UNVERIFIED]` this session.

## 2. Fallout 3 (Capital Wasteland)

Fetched sources gave little FO3-specific modding detail. Entries here are from background knowledge and are marked.

| Problem | Mods | Status | Design lesson |
|---|---|---|---|
| Crashes, memory, quest-breaking bugs | Fallout 3 Unofficial Patch (Arwen etc.), FOSE, 4GB-aware patches, "Begin Again" modding guide | `[UNVERIFIED]` - Wikipedia FO3 confirms crashes and quest-breaking bugs were a launch complaint | Quest-breakers on a critical path kill goodwill; ship a quest-state QA pass. |
| Perks/stats/economy not balanced | Fallout Wanderers Edition (FWE), Mart's Mutant Mod, Operation Anchorage/Broken Steel overhauls | `[UNVERIFIED]` | Players want slower progression, harder survival, tougher enemies. |
| Combat | Reworked weapon/damage overhauls | `[UNVERIFIED]` | Developers later admitted shooting was among the weaker elements (Wikipedia FO3). |
| Writing/choices | Retrospectives fault limited meaningful choice (Wikipedia FO3). Mods rarely fix writing; fans instead migrated to NV and merged FO3 content into it via Tale of Two Wastelands. | Verified for retrospective critique; TTW listed on Wikipedia NV page | Mods can add content but cannot easily repair thin choice architecture. |
| Merge with NV | Tale of Two Wastelands (TTW): play Capital Wasteland and Mojave in the NV engine, with a dedicated guide (The Best of Times, moddinglinked) and a Discord-based community; forum read-only, 3.x versions | taleoftwowastelands.com, moddinglinked, Wikipedia NV | Fans think the NV engine and rules are preferable to FO3's; they move content to the better systems rather than the reverse. |
| Remaster demand | Fallout 3 and NV remasters announced in development in 2026 | Wikipedia FO3 (reports) | The market for faithful improved re-releases is proven. |

## 3. Fallout: New Vegas

New Vegas has the best-documented ecosystem. VNV is a curated, philosophy-driven install guide split into a "required fixes" base and a subjective "Extended" layer.

### 3.1 Stability, engine and performance (all in VNV base)

| Category | Mods (VNV) | What they fix | Lesson |
|---|---|---|---|
| Script extender and loader | xNVSE; Game Patcher (4GB Patcher / Epic patcher); Vanilla BSAs Patcher | Memory ceiling, scripting limits, audio and archive decompression for load speed | "Use up to 4GB RAM" was a first-step requirement for a 2010 game. Ship 64-bit, large-address-aware executables. |
| Base data fixes | Ultimate Edition ESM Fixes Remastered; YUP (Yukichigai Unofficial Patch, "thousands of bugs"); Unofficial Patch NVSE Plus | Records, quests, base-game and DLC bugs | Unofficial patches are the single most demanded mod type. |
| Engine hooks | JIP LN NVSE, JohnnyGuitar, ShowOff, ITR, lStewieAl's Tweaks and Engine Fixes/Optimizations | New functions, engine bug fixes, faster save/load | Modders fix the engine; plan for scripting extensibility. |
| Frame pacing and stutter | New Vegas Tick Fix (micro-stutter, safe to ~120 FPS); Combat Lag Fix; VATS Lag Fix; ActorCause Save Bloat Fix (15-30% smaller saves); FNV Mod Limit Fix | Specific, measurable hitches | Save bloat and VATS delay are design bugs, not just tech debt. |
| Crash diagnostics | Yvile's Crash Logger, ML Utilities Checker | Player-run triage | Provide crash logs and a self-check. |
| Visual correctness | Mesh and skinned-mesh improvement mods, LOD Fixes/Flicker Fix, Vanilla Plus Terrain (raises light limit from 3 to 24), Strip Lights Region Fix, 3rd Person Animation Fixpack, Viewmodel Shake Fix, Iron Sights Aligned | LOD flicker, missing Strip lights, floating objects, third-person aim and animation | Visual polish gaps cluster in lighting, LOD and weapon viewmodels. |

Verified from vivanewvegas.moddinglinked.com utilities and bugfix pages.

### 3.2 UI (VNV hud page, 13 mods)

| Mod | Function | Lesson |
|---|---|---|
| Mod Configuration Menu, MCM Extender | In-game mod settings | Settings accessible in-game, not INI files. |
| Vanilla UI Plus, UI Improvements, PipBoy UI Tweaks | Quality-of-life while keeping the style | Players like the style, dislike the friction. |
| Clean Vanilla HUD, High Resolution Screens, High Res Local Maps, Clean Companion Wheel | HD remake of interface, Pip-Boy/terminal and map resolution | Low-resolution UI textures are an immediate "dated" signal. |
| Menu Search | Ctrl-F in Pip-Boy, container, barter, recipe, perk and save/load menus | Search/filter everywhere. |
| JIP Improved Recipe Menu | Easier crafting list | Crafting lists need filtering and "craftable now". |
| Sleep Wait Hardcore Needs | Preview of H2O/FOD/SLP effect of waiting | Survival meters need forecasts. |
| Faster Main Menu | Load speed | Time-to-play. |

DarNified UI and similar skins are `[UNVERIFIED]` here (not in the fetched list but widely known); VNV chooses vanilla-style over replacement skins.

### 3.3 Gameplay rebalance (VNV gameplay page)

| Mod | Change | Lesson |
|---|---|---|
| Agua Fria - JSawyer Redone | Lower starting HP and carry weight, slower leveling, lower level cap, rebalanced Hardcore mode. Descended from Josh Sawyer's own "JSawyer" mod (Sawyer was NV project director `[UNVERIFIED]` this session) | When the lead designer's post-release rebalance becomes the community default, ship that tuning at launch. |
| JAM (Just Assorted Mods) | Dynamic crosshair, hit marker, hit indicator, loot menu, weapon wheel | Basic combat feedback and quick loot. |
| Enhanced Movement | Diagonal movement, sprint, sneak, lean, prone; fixes | Movement is stiff; players add it. |
| B42 Recoil | Configurable modern recoil | Gunplay feel. |
| Manual Reload and Ammo Memory | No auto-reload, remembers ammo types | Control and clarity in ammo handling. |
| Better Caravan | Makes the card minigame usable, fixes AI | Minigames need a coherent UI. |
| Cookable Grenades | Shorter fuse by holding | Expected FPS convention. |
| Faster Sleep-Wait, Auto-Save Manager | Waiting speed, timed autosaves | Autosave rotation and fast waiting should be built in. |
| Bad Touch NVSE | Fire and shock hazards deal damage | Environmental hazards should matter. |
| Essential DLC Enhancements Merged | DLC gameplay fixes | DLC polish matters. |

Other known NV overhauls such as Project Nevada, Unbogus and the "Hardcore Mode" variants are `[UNVERIFIED]` from background knowledge; they are the same lesson (time-to-kill, ammo scarcity, perk rebalance).

### 3.4 Content and reactivity (VNV content page)

| Mod | Function | Lesson |
|---|---|---|
| The Living Desert | Hundreds of NPCs and scripted events for a more alive, reactive wasteland | Overworld encounters should have more authored variety and reactivity. |
| Better Brotherhood | Fame sources, fixed ending slides, repair services, leveled-list changes | Cut/under-served factions get filled in. |
| Goodies | Large collection of restored cut content and consistency fixes | Restored cut content is a standing community project. |

### 3.5 Total conversions and merges for NV

| Project | What it is | Verified facts | Lesson |
|---|---|---|---|
| Tale of Two Wastelands | FO3 + NV in one engine | Listed on Wikipedia NV page; dedicated guide exists | See Section 2. |
| Fallout: New California | Prequel mod on NV engine by Radian-Helix Media (Brandan Lee) | Started as Project Brazil, renamed 1 Sept 2017. First installment 31 May 2013, second installment public beta 23 Oct 2018; ~5,000 lines of voiced dialogue in part 1, over 16,000 in the second beta; team of three plus a roster of actors; Mod DB Mod of the Year 2018 (Players Choice and Editors Choice); official GOG release July 2026 per Wikipedia | A small team with strong writing and full voice can earn a decade of attention. |
| Fallout: The Frontier | Large NV-engine mod set in the Pacific Northwest | ModDB blocked; controversy details (release date, alleged Nexus/Bethesda issues) not verified this session. `[UNVERIFIED]` | Long-awaited TCs ship late; scope management matters. |
| Fallout 4: New Vegas, Capital Wasteland, Miami, Cascadia (FO4 mods) | Ports/new regions in FO4 engine | Not verified this session. `[UNVERIFIED]` | Fans repeatedly recreate the regions they love; setting reuse is a long-term pull. |

## 4. Fallout 4

TMR (The Midnight Ride) is the equivalent of VNV. Everything below is verified from the TMR pages unless marked.

### 4.1 Stability and engine

| Mod | Function | Lesson |
|---|---|---|
| Unofficial Fallout 4 Patch (UFO4P) | Fixes thousands of bugs in base game and DLC | Same as NV. |
| Community Fixes Merged, Glitchfinder AIO | Small community fixes | |
| Previsibines Repair Pack | Fixes placement/mesh issues needing previs regeneration; performance gains | A rendering optimization (previs) caused mesh/placement bugs. |
| Addictol (Buffout + X-Cell + Mentats merged) | Engine fixes and crash prevention | Engine instability. |
| F4SE fixes (Empty Vendor List, Magic Effect/Spell fixes, Follower AI Approach Reaction) | Engine bugs | Vendor and follower bugs are visible to everyone. |
| Visual fixes (Wetness Shader, Fixed Gobo, Foliage Flicker, Motion Vector fixes, Blood Fixes: over 1,100 decals, rain-shelter roofs, Gutsy voice) | Polish | |
| Midnight Cult Fix | Settler AI problem in extra-large settlements | Settlement scale limits. |

### 4.2 UI and tweaks

| Mod | Function | Lesson |
|---|---|---|
| Mod Configuration Menu | In-game mod config | |
| Crafting Highlight Fix, Workshop Highlight Fix | Replace opaque selection shader with outline | Players cannot see what they select. |
| Simple FOV Slider | FOV in menu | PC basics. |
| Remember Lockpick Angle | Next pin starts at same angle | Minigame frustration. |
| To Your Face FO4 | NPCs stop greeting from behind | Ambient dialogue spam. |
| Simple Offence Suppression | Friendly NPCs do not turn hostile from accidents | Friendly-fire consequences are harsh. |
| Faster Workbench Exit, Dogmeat Lags Behind, Less Annoying Berry Mentats | Small friction removers | Animation and companion behavior friction. |
| Unlimited Survival Mode | Re-enable fast travel and normal saves in Survival | Hardcore modes should be configurable. |

The widely used dialogue-wheel replacement (Full Dialogue Interface, which restores full sentences instead of the paraphrased 4-option wheel) and FO4 UI replacements (DEF_UI, FallUI) are not in the fetched TMR pages; they are `[UNVERIFIED]` here, but the demand is well-documented. Reviewers faulted FO4's simplified role-playing versus FO3 and NV (Wikipedia FO4), and Dexerto calls dialogue and quests "blander" (Dexerto).

### 4.3 Gameplay

| Mod | Function | Lesson |
|---|---|---|
| Loot Logic and Reduction | Less ammo, meds, bobby pins; loot spread to appropriate containers | Loot is too generous and unthemed. |
| Complex Vendors | Vendors buy only related items | Economy coherence. |
| SPARS | Fewer power armor parts | Power armor lost its specialness. |
| Keep Radiants in the Commonwealth | Radiant quests will not send you outside the region | Radiant quest logic is clumsy. |
| Encounter Zone Recalculation | Update enemy levels in revisited zones | Level scaling vs. zone persistence. |
| Who's The General | Fixes Minutemen quest cadence and Preston turn-in spam | Quest-giver nagging. |
| No Sneaking in Power Armor | Sneaking harder in power armor | Class fantasy coherence. |
| Molotov Cocktail Nerf, Hit Those Objects | Balance and feedback | |
| Safe Travels | Unlock fast travel in Survival via settlements | |
| Reinforcements and Retribution | Consequences for clearing dungeons | Worlds should respond. |

### 4.4 Content and settlements

| Mod | Function | Lesson |
|---|---|---|
| You And What Army 2 | Rebuild the Minutemen as a faction tied into the world | The settlement-defense loop needs purpose. |
| More Diamond City Bounties, More Weathervanes | Reworks/expands radiant bounties | Radiant content wants more variety. |
| Legendary Mutation Messages Fix | Restores cut messages | |

Sim Settlements 1 and 2 (city-planner framework with story, buildings automated), Place Everywhere, Alternate Start - Live Another Life, Start Me Up, Commonwealth Captures, Horizon, Nuka World/Far Harbor overhauls, and the major FO4 total conversions (Fallout: London, Fallout 4 New Vegas, Capital Wasteland, Miami, Cascadia) are `[UNVERIFIED]` for downloads and detail; their existence and general popularity are well known from background knowledge, and Place Everywhere exists mostly because the vanilla workshop imposes snapping and placement limits. Another reference point (Wikipedia, Mod article): Caliente's Beautiful Bodies Edition has been downloaded at least 8.2 million times, showing body/appearance mods can dwarf gameplay mods in raw download counts (Nexus).

### 4.5 Fallout: London (the major FO4 total conversion)

| Fact | Value | Source |
|---|---|---|
| Release | 25 July 2024 (development began 2019) | Wikipedia |
| First-day downloads | Over 500,000 in 24 hours; "fastest redeemed title ever" on GOG | Wikipedia |
| Team | Almost 100 modders, 100+ voice actors, ~20 testers (versus ~150 for FO4) | Wikipedia |
| Reception | IGN 7/10, Gamereactor 8/10, GamingBolt 8/10, PCGamesN 9/10; praised setting and British culture; criticized bugs, crashes, performance; one reviewer called it "barely playable" at launch | Wikipedia |
| Platform fallout | Delayed by Bethesda's next-gen update; Steam users had to roll back the game, GOG users did not | Wikipedia |
| Later | VR version 28 May 2025; expansion "Rabbit and Pork" 30 Sept 2025 | Wikipedia |

Lesson: fans prefer a new setting with fresh culture over additional content in a familiar setting; a free mod nearly outpaced many commercial releases in day-one demand. Distribution through a storefront (GOG) with a compatible build mattered.

## 5. Fallout 76

- No general mod support. Bethesda banned players for mod use and duplication; players said bans hit people who used mods for visual/technical fixes (Wikipedia FO76).
- Launch Metacritic scores 49-53 (Xbox/PC/PS4), Eurogamer called the launch "a bizarre, boring, broken mess"; Wastelanders (April 2020) added human NPCs and improved reception (Wikipedia).
- Evidence of unmet need: human NPCs and quests (added later). No mod-based evidence is available.

## 6. Cross-cluster lessons

| Cluster | Players consistently fix | Therefore ship |
|---|---|---|
| Stability | Crashes, save bloat, quest blockers, memory limits, stutter | A QA budget sized to content, a 64-bit engine, a crash logger, autosave rotation. |
| UI | Search, filter, HD textures, readable highlights, config menus, preview of needs effects | Searchable, filterable lists; readable outlines; in-game settings. |
| Rebalance | Slower leveling, lower carry weights, scarcer loot, longer meaningful progression | Tuned progression with level cap and loot density audited by designers. |
| Quest friction | Nagging givers, radiant spam, region-leaking radiant quests | Authored quest cadence; limit radiant content; let player decline. |
| Combat | Reload control, recoil, hit feedback, movement | Good gunfeel at launch, readable feedback. |
| Survival | Optional hardcore needs with forecast UI and configurable saves/travel | Offer a difficulty tier with transparent needs and flexible rules. |
| Start | Alternate starts (Alternate Start, Start Me Up for FO4; "Live Another Life") `[UNVERIFIED]` | Let players skip or choose the opening, avoid forced backstories (evidence from existence, not verified numbers). |
| Settlements | Placement freedom (Place Everywhere), automated city-planning (Sim Settlements) `[UNVERIFIED]` | Build tools that are flexible, not fiddly; give settlement activity story purpose. |
| Content | Restored cut content, fuller factions, more NPCs/events | Ship fuller factions and ambient life. |
| Companions | AI behavior, Dogmeat as extra | Companions must pathfind and react well. |
| Visuals | Meshes, LOD, lights, terrain, textures | Fix LOD and lighting; fidelity is secondary to polish. |
| Total conversions | New settings, cultures, voiced writing | Large voice-acted dialogue pays off. |

## Design Takeaways

- Budget for stability first. Both VNV and TMR open with "required fixes" before any opinionated change. Treat unofficial-patch-level quality as the floor, not a patch.
- Ship an official bug-fix/QA-pass tool budget, a crash logger, and make the executable large-address aware and 64-bit.
- Build modding in from day one: a script extender-class feature set, in-game config menu support, and stable file formats so updates do not break mods (Anniversary Edition and next-gen updates are cautionary examples).
- Ship searchable/filterable inventory, crafting and barter lists, a clean legible HUD, readable item/workshop highlights, and survival-meter forecasts.
- Tune progression conservatively: slower leveling, lower early carry weight, scarcer ammo/meds. Let designers own a "Hardcore" ruleset and make its parts toggleable.
- Avoid radiant-quest spam and "report back" loops. Authored quests should not nag; let faction hubs issue content on request.
- Loot should be themed and constrained to appropriate containers; vendors should buy only what they sell.
- Put real work into gunfeel and feedback (hit markers, recoil, reload control) even for an RPG-first design.
- Make the overworld alive: more NPCs and scripted events, consequences for clearing locations, and refreshing enemy checkpoints.
- Let players choose their start and not be forced into a backstory (the alternate-start mods exist because players want it; verify numbers before citing).
- Offer a settlement/base system only if its placement is flexible and its output feeds the story.
- Write with a distinct culture and voice. Fan projects that last (New California, London) win on setting and voiced writing, not graphics.
- Do not punish modders or ban players for fixing the game; the community's fixes are a free QA team.

## Sources

Consulted this session:
- https://vivanewvegas.moddinglinked.com/ (index, intro, utilities, bugfix, hud, gameplay, content, wabbajack)
- https://themidnightride.moddinglinked.com/ (index, intro, bugfix, hud, tweaks, gameplay, content)
- https://thebestoftimes.moddinglinked.com (Tale of Two Wastelands guide landing page)
- https://taleoftwowastelands.com/
- https://github.com/sfall-team/sfall
- https://github.com/BGforgeNet/Fallout2_Restoration_Project
- https://github.com/rotators/Fo1in2
- https://en.wikipedia.org/wiki/Fallout:_London
- https://en.wikipedia.org/wiki/Fallout:_New_California
- https://en.wikipedia.org/wiki/Fallout:_New_Vegas
- https://en.wikipedia.org/wiki/Fallout_2
- https://en.wikipedia.org/wiki/Fallout_3
- https://en.wikipedia.org/wiki/Fallout_4
- https://en.wikipedia.org/wiki/Fallout_76
- https://en.wikipedia.org/wiki/Mod_(video_games)
- https://en.wikipedia.org/wiki/Tale_of_Two_Wastelands (redirects to the Fallout: New Vegas article)
- https://www.dexerto.com/fallout/new-fallout-fans-are-playing-the-wrong-games-2653166/

Attempted but blocked (403/402/404): nexusmods.com top lists and mod pages, moddb.com (Restoration Project, Nevada, Olympus 2207, Resurrection, Sonora, Frontier), fallout.fandom.com, pcgamer.com best-mods pages. Nexus download totals, Sim Settlements, Full Dialogue Interface, DarNified, Alternate Start and The Frontier controversy remain `[UNVERIFIED]`.
