# Mods as Design Feedback: What Players Fix, Add and Rebuild

Purpose: treat the most-installed and most-recommended Fallout mods as an unsolicited bug report and feature request from the player base. Where a mod category is near-universal in modding guides, the shipped game left a gap.

**Evidence quality note (two passes).** Pass 1 verified the structure of the Viva New Vegas (VNV) and The Midnight Ride (TMR) guides, the sfall / Restoration Project / Fo1in2 GitHub READMEs, and Wikipedia facts. Pass 2 (this revision) added fetched pages from fallout.wiki (very useful for per-mod pages: author, dates, scope), dtf.ru (a long Fallout 2 modding history with dates), Wikipedia, GameBanshee, Worthplaying, RPG Codex, Kotaku, Game Informer, PCGamesN, GitHub and the BGforge docs. Nexus Mods, ModDB, Fandom, NMA, archive.org, PC Gamer (truncated) and several others still returned 403/402/404 or truncated text. Consequences:

- **No Nexus/ModDB download totals could be retrieved.** Popularity statements below use only what a fetched page states: GitHub stars/commits, GOG's "redeemed" figure for Fallout: London, the 100,000 unique downloads for The Frontier (fallout.wiki), awards, or inclusion in curated guides. A few Nexus figures seen only in search-result snippets are labelled "(snippet-only)".
- **Snippet-only** means a search-engine summary or result snippet was the only evidence; the page itself was not read. Those claims are labelled and, where they carry weight, still tagged `[UNVERIFIED]`.
- The first draft contained two attribution errors that are corrected here: the Unofficial Fallout 3 Patch was not by "Arwen" (the original is credited to Quarn/Quazzy, snippet-only), and "Alternate Start - Live Another Life" is Arthmoor's Skyrim mod, not a Fallout 4 mod (the Fallout 4 equivalents are Start Me Up and Another Life).

The key question the document answers: for each era, which community mods fixed or redefined the game, and what did the community fix that the vanilla game neglected? Section 6 answers it as one table.

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
- Pass 2 additions, by era:
  - **Fallout 1:** Fallout Fixt (Sduibek) bundles Interplay and TeamX patches plus a stack of fan fixes behind a "purist / half-purist / full / custom" installer; Fallout et tu (Fo1in2, Rotators) moves the whole game into the Fallout 2 engine.
  - **Fallout 2:** killap's Unofficial Patch fixed 800+ bugs left after Interplay's last patch; his Restoration Project (RP 1.0 on 9 Jan 2008) restored cut or planned locations (EPA, Primitive Tribe, Abbey, Vault Village, Slaver's Camp...); the community kept it alive (RPU, 2019 onward) and four full-length total conversions followed (Nevada, Olympus 2207, Resurrection, Sonora).
  - **Fallout 3:** the Unofficial Patch, FOSE, FWE (2010; 50+ mods merged, needs/triage/ammo weight), FOOK2, Mart's Mutant Mod and Fellout (green tint removal) are the stability / rebalance / colour trio; the same FWE team then built Project Nevada for NV (2011).
  - **New Vegas:** Josh Sawyer himself published JSawyer on 29 Dec 2011 (lower HP and carry weight, slower leveling, level cap 35, fewer food drops) because he thought the tuning too punishing to ship by default; the community built Ultimate/Agua Fria on top. The Frontier (Jan 2021, 100,000+ unique downloads by 26 Mar 2021) and New California are the flagship total conversions.
  - **Fallout 4:** Full Dialogue Interface appeared 8 days after launch (18 Nov 2015) to undo the paraphrased wheel; UFO4P arrived 25 Apr 2016; Sim Settlements (kinggath; PC Gamer's Best Mod of 2017, snippet-only) gave settlements a purpose; Horizon and Start Me Up rebuilt survival and the opening; Fallout: London (GOG, 500,000+ redemptions in 24h) is the capstone.
  - **Fallout 76:** an online, server-authoritative game with an anti-third-party stance still got a few UI tools (Better Inventory, Perk Loadout Manager, Glowing Items) within weeks of launch.
- Monetisation is itself a flashpoint: Valve and Bethesda reversed paid Skyrim mods in about four days (April 2015) after a petition passed 51,000 signatures in a day; Creation Club (Fallout 4, 29 Aug 2017) was criticised as "paid mods" again.

## 1. Fallout 1 and Fallout 2 (classic engine)

### 1.1 Fallout 1 (1997)

Official support ended early: Wikipedia records patch 1.1 (13 Nov 1997; bug fixes and removal of the 500-day limit on the other two main quests) and 1.2 (removed children from the game for the European release). Everything after that was fan work.

| Mod | Author / year | What it changes | Vanilla shortcoming addressed | Scale / popularity evidence | Design lesson |
|---|---|---|---|---|---|
| **Fallout Fixt** | Sduibek. RPG Codex news dated 11 Sep 2013 covers Alpha 6.1; dtf.ru's modding history dates its creation to 2016 `[DISPUTED]` (the 2013 article shows it existed earlier; dtf.ru may be dating a rewrite) | A "megamod" installer. Alpha 6.1 bundles official patches 1.1/1.2, TeamX patches (1.2, 1.21, 1.3.5), No Children Fix, Cathedral crash fix, Nimrod's dialog fixes, TeamX NPCs 3.5, Fallout 1 Restoration Mod (optional invasions with timing from instant to 4x default, unlinks Deathclaw status between worldmap and cave), Extended Flamer Attack Mod, Endgame Mod, sfall ddraw 1.18e and hi-res patch 4.0.2. Install tiers: Fixes Only [Purist], Standard [Half-Purist], Full, Custom. Snippet-only (NMA page): fixes ~150 bugs left in earlier unofficial patches and adds ~170 features; latest listed 0.81a | Crashes (Cathedral, Military Base, The Glow), dialog typos, unfinished endgame, no modern resolution, a patch history scattered across Interplay and TeamX. Described by RPG Codex as the Fallout 1 equivalent of killap's Fallout 2 patch | No download totals retrievable. Some Fixt ideas were reused by Fallout et tu (dtf.ru). Users still report crashes with some installs (snippet-only) | Offer the same package at several fidelity levels (purist fixes-only vs full). One-installer "known good" bundles beat a 20-mod forum thread. |
| **Fallout et tu (Fo1in2)** | Rotators (the FOnline: 2238 team); GitHub `rotators/Fo1in2`; lead credited as Lexx (snippet-only) | Rebuilds Fallout 1 inside the Fallout 2 engine "almost 1:1": Fallout 2 style merchant restocking, party members that level, change appearance with armor and can be controlled in combat, optional auto-doors, motorcycle for travel, tougher-mutants option, continue play after the ending, Hero Appearance, many bug fixes. v2.0 works with Fallout 2 Community Edition | Fallout 1's engine lacks FO2's party, merchant and quality-of-life features; its saves/bugs were worse | **851 GitHub stars, 3,922 commits** (verified); needs both games installed | Fans port the *older* game into the *newer* engine when the engine has the quality-of-life and the old game has the soul. Design content so it can migrate. |
| **High-resolution patch** | Matt "Mash" Wells. Fallout 2 patch 3.0 on 23 May 2011 (GameBanshee); also adapted for Fallout 1 | Patches the executable in memory to run above 640x480, windowed mode, scaling of splash/help/death/ending screens, 32-bit colour, map edge clipping | A fixed 640x480 screen on 1998 hardware and modern monitors | Superseded in part by sfall's built-in hi-res mode and bundled in RPU and every large Fallout 2 total conversion. Author reported missing (forum post, snippet-only); latest listed 4.1.8 | Resolution scaling was a day-one need for decades; build a resolution-independent UI. |
| **sfall (engine extender)** | Timeslip (original author, verified on README); now maintained by `sfall-team` | A DLL that modifies Fallout 2 in memory without touching the EXE: modern OS support, externalised settings (starting map, skills, perks, critical tables, books), engine bug fixes, new script opcodes, quality-of-life (middle-mouse weapon switch, wheel scrolling, game-speed keys, click-to-transfer items, item highlighting) | A fixed 1998 engine with hard-coded tables and no scripting hooks | **450 stars, 2,220 commits** (verified); bundled with Steam/GOG Fallout 2 (SFALL 4.4.5 per Wikipedia, pass 1); required or supported by nearly every large Fallout 2 mod (dtf.ru, fallout.wiki) | A fan DLL became the distribution default. Expose engine tables as data and scripting hooks; ship modern-OS compatibility yourself. |

### 1.2 Fallout 2 (1998)

Wikipedia notes critics praised Fallout 2 but faulted its frequent bugs; Chris Avellone later called it "a slapdash project without a lot of oversight" and Tim Cain's team reportedly had roughly nine months. Interplay's last patch (1.02d, 11 Feb 1999, pass 1) fixed "major bugs".

| Project | Author / year | What it changes | Vanilla shortcoming addressed | Scale / popularity evidence | Design lesson |
|---|---|---|---|---|---|
| **Unofficial Fallout 2 Patch (UP)** | killap (NMA user). Work began 2005; v1.02.26 shipped alongside RP 2.0 (2010); updates continued to RP 2.3.3 in 2014 (dtf.ru) | Pure bug fixes, no new content, separate from the Restoration Project | Bugs left after the last official patch | Described by killap and a GOG forum post as fixing **well over 800 bugs** after official 1.02 (snippet-only, ModDB listing). `UPU` fork on GitHub: **5,244 commits** (verified) | A single volunteer out-fixed the original publisher. Plan for post-launch fix budgets. |
| **Restoration Project (RP)** | killap. RP 1.0 released 9 Jan 2008 (Worthplaying); 2.0 in 2010; 2.2 "final" in July 2013 (GameBanshee: "I'm done", killap); 2.3.3 in 2014 with source published (dtf.ru) | Restores and invents content that Black Isle planned. **New locations at 1.0 (Worthplaying):** EPA, Primitive Tribe, Abbey, Vault Village, Slaver's Camp, Hubologist Stash, Den residential area, Enclave Vertibird landing pad, Ranger safe houses. The author called it "about 6 new locations" plus new quests/NPCs/items at every old location (snippet-only). Later versions add new party members, concentrated at the EPA. The f2rp.bgforge.net guide has sections for Klamath, The Den, Modoc, Vault City, Gecko, Raiders, Broken Hills, Redding, New Reno, Sierra Army Depot, NCR, San Francisco, Navarro, Enclave, EPA, Umbra Tribe, Abbey, Vault Village and Slaver's Camp. A restored quest for Sulik to find his missing sister is reported by a video-review summary (snippet-only, `[UNVERIFIED]`) | Fallout 2 shipped with cut locations, orphaned content and unfinished companion arcs after a rushed schedule | Landmark of fan restoration; widely recommended (Steam, GOG, NMA). No download count retrievable. TV Tropes and BGForge both warn that the RP's "restored cut content" reputation is exaggerated: it uses design documents but also new material, and "some of it has been cut for a reason" (snippet-only) | Players will rebuild cut content, but they cannot tell *dummied* from *invented* content. Keep clean cut-content records, and cut for reasons you can defend. |
| **Restoration Project, updated (RPU) and Unofficial Patch, updated (UPU)** | Revived 2019 by "Burn"; Pixote's Maps Updated 2020; RPU 32 in 2024 (200+ remaining bugs), RPU 34 in 2025 (all dtf.ru); GitHub `BGforgeNet` | Bundles UP, high-quality music, Hero Appearance, NPC armour visuals, Party Orders (command party tactics), Cassidy talking head, enhanced worldmap, extra flamer/rifle/wakizashi animations, an improved Mysterious Stranger, and the hi-res patch | A ~25-year bug backlog and a missing party-control interface | **6,154 commits** (pass 1, README). Installer via ZAX | A community can maintain a game for a quarter century if the tools (here sfall) and source of the patch are open. |
| **Fallout 2 Reference Edition / Community Edition** | Alexander Batalov (Reference Edition: executable reverse-engineered to C, "with all its imperfections"). Community Edition 2023: Batalov, Gleb Mazovetskiy, Woodrow Douglass, Austin Hurst (fallout.wiki) | A drop-in rebuild of the Fallout 1 and 2 engines: runs on Windows, Linux, macOS, iOS and Android, keeps gameplay, adds engine bug fixes and quality-of-life | The original executables never left 1998 platforms | Fo1in2 v2.0 targets CE. No download counts retrievable | Fans eventually reimplement the engine. If the engine is ever lost, the game dies; keep the source and format specs. |
| **Party control** | "Party Orders" (RPU), sfall party member control | Command tactics and equipment for companions | Wikipedia notes FO1 reviews faulted lack of direct companion control | RPU / sfall READMEs | Players want some command over companion tactics. |
| **Hero Appearance Mod** | Bundled in RPU and Fo1in2 | Visible hero appearance by armour | Character legibility in isometric view | READMEs | Character visibility is a long-standing want. |

### 1.3 Fallout 2 total conversions and sequels

All run on the Fallout 2 engine, and most list sfall and the hi-res patch as dependencies (Sonora, Resurrection) or use their own build (Nevada and Sonora do not strictly need sfall per dtf.ru). None had retrievable download counts.

| Project | Team / dates | Scope (fetched) | Why it matters |
|---|---|---|---|
| **Fallout: Nevada** | Nevada Band Studio (lead Alexander Poshelyuzhin). 0.99a Apr 2011, 0.99b Jan 2012, 1.00 Mar 2015 (fallout.wiki; dtf.ru agrees on 2015); 2023 re-release | Unofficial prequel set before Fallout 1, all-new scripts, plot, dialogue; **100+ quests**; fallout.wiki says 12 major map points, dtf.ru says 16 locations `[DISPUTED count]`; ~2.7 MB of text; original music | Four years of fan work gave a full-length, text-heavy RPG. Proof of demand for pure CRPG form. |
| **Fallout 1.5: Resurrection** | Four Czech fans (Panos, Stipek, Ratican, Lozi). Czech version 2013; English v1.4 15 Jul 2016, patch 1.5 17 Nov 2016; Russian 2018 | Total conversion set 2170 in New Mexico between FO1 and FO2, ~25 hours, amnesiac protagonist, new locations (New Hope, Albuquerque), about 80 locations total (dtf.ru) | A four-person team delivered a "third classic" game. |
| **Olympus 2207** | Nebesa Games (Artyom Samoilov design; Alexander Berezin art). Release 26 Dec 2014, hotfix 30 Dec, v1.1 12 Sep 2015, v1.2 in 2021 (dtf.ru) | "Full conversion" not set in the Fallout universe: Silicon Valley 2207; 80+ quests, 14 locations; successor Olympus 2249 / Project O2 announced | The engine can host a *non-Fallout* IP: relevant to our original game. |
| **Fallout: Sonora** | Nevada Band Studio (lead Alexander Poshelyuzhin; artist Alexander Berezin; composer Alexey Trofimov). First build 21 Mar 2017; released 20 Mar 2020; v1.10 on 28 Jun 2022 (fallout.wiki), 1.16b in 2026 and Dayglow expansion (2 Sep 2023, dtf.ru) | Continues the events of Fallout (1997) in the Sonoran Desert; ~100 quests, 13 major + 9 small locations, 13 special encounters (fallout.wiki) | Three years from first build to release; post-release content kept coming for six years. |
| **Last Hope** | Forgotten Knight. 2009; stable 1.082 in 2021 (dtf.ru) | Not fetched in detail | Evidence of long tails. |
| **Fallout Yesterday** | PJ Hexer (fan version of the cancelled "Van Buren" Fallout 3, per fallout.wiki) | Unreleased at time of dtf.ru snapshot | Shows interest in cancelled-game content. |

Lesson: the isometric, turn-based, text-heavy form has no modern commercial equivalent from the franchise holder, so volunteers supply it, with 100+ quest campaigns each. The engine's longevity depends on sfall.

## 2. Fallout 3 (Capital Wasteland)

Wikipedia (Fallout 3, citing IGN) records physics issues and crashes, "some of which broke quests and prevented progression". The Wikipedia article says nothing about mods, so the entries below rest on fallout.wiki, PCGamesN, SourceForge, GameBanshee and search snippets (labelled). Download totals were not retrievable.

| Mod | Author / year | What it changes | Vanilla shortcoming addressed | Evidence / popularity | Design lesson |
|---|---|---|---|---|---|
| **Unofficial Fallout 3 Patch (UFO3P)** and updated version | Original credited to Quarn/Quazzy (snippet-only); the Updated Unofficial patch by BenWah, with Hairylegs and prisoner416 (Nexus listing, snippet-only). Not "Arwen" (earlier draft was wrong) | "Hundreds of lingering bugs, scripting errors, and crash causes": quest scripts that block progress, NPC and world-interaction glitches, item/container errors (duplication, loss), freezes (SourceForge description). Changes no gameplay or balance | Launch bugs, including quest-breakers | PCGamesN (2024 roundup) still lists it as updated in 2024. Autoloads FOSE (snippet) | Quest-breakers on a critical path kill goodwill; ship a quest-state QA pass. |
| **FOSE (Fallout Script Extender)** | The same team that wrote NVSE: Ian Patterson, Stephen Abel, Paul Connelly (fallout.wiki, NVSE page) | Extends scripting without altering the executable; required by most big mods | The 2008 script engine was too limited for the community's ambitions | Prerequisite for FWE, FOOK2 and most others (snippet) | Ship scripting hooks. The team behind FOSE/NVSE became the de facto engine team for Fallout 3 and NV modding. |
| **Stability tools (4 GB / LAA patch, Stutter Remover, Games for Windows Live disabler)** | Various; Stutter Remover (FOSE plugin) v4.1.36 listing at GamePressure; GFWL Disabler (snippet) | Large-address-aware patch for the 32-bit executable (the Steam/GOG guide step: apply 4 GB patch to Fallout3.exe, Epic build patches fose_loader.exe); stutter removal via plugin, or the `iFPSClamp=59` ini tweak; GFWL removed | A 32-bit exe on a 4 GB machine, frame-pacing stutter, a DRM/online layer | Stutter Remover now causes crashes on newer Windows builds, F3TF suggested as replacement (snippet-only). Verification of tool authors pending `[UNVERIFIED]` | The same four tools are the first-run checklist two games later (see NV). |
| **Fallout 3 Wanderers Edition (FWE)** | Project lead Mezmorki, lead developer Kai Hohiro, with Delamer, jjgun, The 3rd Type, Schlangster (fallout.wiki). Beta 1.0 on 10 Jan 2010, final 6.03a on 14 Sep 2010 (page dates are out of order, infobox says 2009) `[DISPUTED dates]` | "Challenge, immersion, depth of gameplay": built-in alternate start, rebalanced and expanded weapons and armour, stimpaks heal over time, mandatory eating / drinking / sleeping, "Triage" system to heal crippled limbs, rarer loot, ammo has weight, much greater damage; in-game control panel in the Pip-Boy. Integrates over 50 mods (the credits list over 70) | Easy survival, generous loot and thin challenge; no optional hardcore needs; no alternate start | Same team moved to Project Nevada in summer 2010. Search snippet describes it as a compilation of ~50 mods | The community's first slow-progression, scarce-loot, needs-based ruleset. NV later shipped Hardcore mode in the base game. |
| **Fallout Overhaul Kit (FOOK2)** | Team not retrieved for FO3. (FOOK for NV: Jonnyeah guns, Millenia textures, Xporc lead, BAN QA; 2010; ~70 apparel, ~60 weapons, new perk "Communist"; bug fixes were later incorporated into YUP, assets into Project Nevada, per fallout.wiki) | "A customised compilation of user modifications, gameplay balancing changes, and original content" that its developers say fills in "the gaps that Bethesda left behind" (snippet-only) | Perceived gaps in content and balance | Forum consensus: FOOK2 and FWE conflict, bridging patches exist (snippet-only) | Two total-overhaul mods cannot coexist; give players an official ruleset toggle instead of an arms race. |
| **Mart's Mutant Mod** | Author not confirmed `[UNVERIFIED]` | Adds creature and NPC variety (unique stats, sizes, skins), new enemies and friendlies, sharper enemy AI (PCGamesN) | Repetitive enemy roster; weak AI | PCGamesN 2024 roundup | Creature variety and AI are cheap, high-value polish. |
| **Fellout** | Author not confirmed `[UNVERIFIED]` | Removes the game's heavy green tint for a more natural palette, closer to the original Fallout games (PCGamesN) | The overall colour grade | PCGamesN 2024 roundup; listed with the Unofficial Patch and mod manager | A single colour pass can swamp art direction; give players a colour-grade slider. |
| **DarNified UI** | Author/date not retrieved `[UNVERIFIED]` | Changes the font; lets the HUD show time/date, radiation and encumbrance; shows more dialogue options and trade items per screen (German pcgames.de snippet); a New Vegas version is fully "DarNified" while the Fallout 3 HUD is mostly vanilla (Nexus forum, snippet-only) | A UI that was thin on information per screen | Called "one of the best UI mods for Fallout 3" in one blog (snippet-only); font issues with mod managers | A UI that fits two items per scroll is a UI that was designed for a gamepad. Make the PC layout denser. (Inference: the mod's fixes match the pattern of console-first layout.) |
| **Tale of Two Wastelands (TTW)** | TTW Team; predecessor Requiem for the Capital Wasteland by MasterYster; Kuroitsune proposed the FO3-in-NV merge (fallout.wiki); 2012; current v3.3.2 | Merges Fallout 3 and its DLC into New Vegas; brings NV mechanics (companion wheel and perks, weapon mods, crafting, plants, poisons) to the Capital Wasteland; level cap 50 to 60; bobbleheads become mini perks; Union Station connects the two worlds; restores some unused FO3 content; fixes bugs | Fallout 3's systems and bugs compared with NV's | Requires your own FO3; a special installer exists partly because Bethesda monitored distribution of FO3 assets; hosted on mod.pub; YUP fixes NV-side bugs for TTW since TTW 3.2 | Fans think the NV engine and rules are preferable to FO3's; they move content to the better systems, not the reverse. |
| Combat | Reworked weapon/damage overhauls (FWE, FOOK2) | Rolled into the above | Developers later admitted shooting was among the weaker elements (Wikipedia FO3) | | Shooting is where Bethesda-engine RPGs need the most help. |
| Writing/choices | Retrospectives fault limited meaningful choice (Wikipedia FO3). Mods rarely fix writing; fans instead migrated to NV and merged FO3 content into it via TTW | Verified for retrospective critique | | | Mods can add content but cannot easily repair thin choice architecture. |
| Remaster demand | Fallout 3 and NV remasters announced in development in 2026 | Wikipedia FO3 / NV | | | The market for faithful improved re-releases is proven. |

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

**Why NV needed this stack.** Wikipedia (New Vegas) records that Obsidian had 18 months, a contracted schedule and a console release; the game shipped with crashes, corrupted saves, frame-rate problems and poor companion and enemy pathfinding, and an Edge reviewer called it "a tragedy" mechanically and technically. Bethesda patched it months later; Metacritic was 84 (PC/360) and 82 (PS3), narrowly missing an 85 bonus threshold. The community's stability ecosystem is that delta.

| Tool | Author / year | What it does | Evidence |
|---|---|---|---|
| **NVSE** (New Vegas Script Extender) | Ian Patterson, Stephen Abel, Paul Connelly (the FOSE team); first release 2010; later maintained as xNVSE after 5.1b4 by a larger team (lStewieAl, jazzisparis, others; fallout.wiki) | Expands scripting without altering the executable on disk; launched via nvse_loader.exe | Prerequisite for nearly every large NV mod; basis of VNV's utilities page |
| **FNV 4GB Patcher** | RoyBatty (idea, patches) and LuthienAnarion (patcher), 2016 (fallout.wiki) | Makes the 32-bit exe 4 GB aware; auto-loads NVSE; supports Steam and GOG, not Epic/Game Pass | VNV first-run step |
| **Yukichigai Unofficial Patch (YUP)** | Yukichigai, with sandbox6 (later maintainer); first released 15 Aug 2013 (fallout.wiki). Yukichigai retired in 2015 | A "compilation of vital bug fixes" for the base game and DLC in one ESM; **no new features, balance changes or restored content**; changelog nearly 3,000 lines; created as a cleaner alternative to Mission Mojave; became the de facto patch within a year; also fixes NV-side bugs in TTW | VNV says "thousands of bugs"; fallout.wiki: no exact count. Unofficial Patch NVSE Plus is the follow-on |
| **NVTF (New Vegas Tick Fix)** | Carxt, Tgspy, lStewieAl (snippet-only) | Tick count fix, hashtable optimisation, high-FPS fix (micro-stutter) | VNV includes it; guides pair it with the 4GB patcher |
| **NVAC (New Vegas Anti Crash)** | Queue (snippet-only) | NVSE plugin adding structured exception handling to reduce crashes | A 2024 Steam thread calls it deprecated and "can cause damage to savegames", superseded by NVTF, YUP and lStewieAl's fixes (snippet-only) `[DISPUTED]` |

**Viva New Vegas (VNV)** is the curated guide that packages the above: split into a required-fixes base and an "Extended" subjective layer, with an automated Wabbajack installer (verified, moddinglinked). Wikipedia says VNV "was widely praised for its bug fixes and quality-of-life improvements". Fetched pages did not name its authors or start date. Lesson: the community's answer to "which of 100 patches do I install?" is a maintained, opinionated list, which a developer should publish itself.

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

DarNified UI is not in VNV's fetched list: VNV chooses vanilla-style tweaks (Vanilla UI Plus, Clean Vanilla HUD) over replacement skins. DarNified itself is documented only by search snippets (font change, more HUD stats, more dialogue and trade items per screen); see Section 2 for the caveats. fallout.wiki also hosts pages for Clean Vanilla HUD, Clean Companion Wheel, Consistent Pip-Boy Icons (several versions), Vault Girl Status Screen Replacer and B42 Notify, confirming how much community effort goes into UI consistency.

### 3.3 Gameplay rebalance (VNV gameplay page)

| Mod | Change | Lesson |
|---|---|---|
| Agua Fria - JSawyer Redone | Lower starting HP and carry weight, slower leveling, lower level cap, rebalanced Hardcore mode; configurable via INI/config menu. Descended from Josh Sawyer's own "JSawyer" mod (Sawyer was NV project director; verified, fallout.wiki and Wikipedia). Author not named in fetched pages; a GGMods listing shows v1.0.5.1, updated 11 Mar 2026, "completely compatible with Viva New Vegas out-of-the-box" (snippet-only) | When the lead designer's post-release rebalance becomes the community default, ship that tuning at launch. |
| JAM (Just Assorted Mods) | Dynamic crosshair, hit marker, hit indicator, loot menu, weapon wheel | Basic combat feedback and quick loot. |
| Enhanced Movement | Diagonal movement, sprint, sneak, lean, prone; fixes | Movement is stiff; players add it. |
| B42 Recoil | Configurable modern recoil | Gunplay feel. |
| Manual Reload and Ammo Memory | No auto-reload, remembers ammo types | Control and clarity in ammo handling. |
| Better Caravan | Makes the card minigame usable, fixes AI | Minigames need a coherent UI. |
| Cookable Grenades | Shorter fuse by holding | Expected FPS convention. |
| Faster Sleep-Wait, Auto-Save Manager | Waiting speed, timed autosaves | Autosave rotation and fast waiting should be built in. |
| Bad Touch NVSE | Fire and shock hazards deal damage | Environmental hazards should matter. |
| Essential DLC Enhancements Merged | DLC gameplay fixes | DLC polish matters. |

#### 3.3.1 The JSawyer mod, in detail (primary lineage of every "hardcore rebalance")

| Item | Verified detail |
|---|---|
| Author | Josh (J.E.) Sawyer, New Vegas project director, in his spare time. First released **29 Dec 2011** (fallout.wiki); changelog runs V2 to V5.1, with modder xporc helping complete V5.1. Distributed originally from diogenes-lamp.info |
| His stated reason | The changes were ones he liked but was unsure the Fallout 3 audience would accept, and the 18-month cycle left no time to debate them or fix some bugs. Game Informer: it "does provide insight into the aims of the lead developer and contains planned tweaks that never made it into release." Engadget: "I'd rather have people opt-in to those changes than make them the default in a patch." The base game's balance leans easy (partly so Fallout 3 players would not be alienated; fallout.wiki). Goal: "much more challenging without being intentionally punishing" |
| Caveats from the readme (via GitHub gist copy) | "This is not official and it's not a patch"; "I played with this mod for about 20 hours. That's the extent of its testing"; no major new content; light scripting only; "Will probably conflict with some of your 10,000 other mods" |
| Level cap and XP | Base cap lowered from 30 to 15; **35 with all DLC** (the unmodded all-DLC cap is 50). First attempt halved granted XP (Oct 2011) but this was reverted in Jan 2012 and replaced by raising required XP (iXPBase 200 to 275, iXPBumpBase 150 to 200, "a little more than a third" more XP needed). Many news stories simplify this to "XP halved" |
| Health | Base player HP formula 100 + (END x 20) + ((Level - 1) x 5) became 50 + (END x 10) + ((Level - 1) x 5); Sierra Madre Martini HP bonus 75 to 40 |
| Carry weight | Base 150 to **50**; Strong Back 50 to 25; Hoarder 25 to 15; power armour weight bonuses tied to armour weight and Power Armor Training; PAT bonuses halved (Jan 2012) |
| Hardcore needs | Dehydration, sleep and starvation accrue faster (rates doubled) but the first penalty threshold is pushed back to 400 and later ones every 150, so needs bite less often but harder; alcohol restores 10-15 H2O; food and drink drops cut to 5%/10%/20% chances |
| Healing | Stimpaks and Super Stimpaks gain weight (0.25 / 0.5); a weaker "Expired" Stimpak is the common drop (4:1 over normal in random lists, value 75 to 50 caps); craftable "Homemade" Stimpak between them; Stimpaks heal 20 base |
| Items | Pre-order packs (Courier's Stash, Classic, Mercenary, Tribal and Caravan packs) moved into secret locations in the Mojave rather than given at the start; energy ammo lighter; medium and heavy armour gain DR tied to DT; power armour needs no perk (Gamewatcher) |
| Challenge | "I Never Axed For This" hatchet challenge and perk added (Apr 2012) |
| Derivatives | **JSawyer Ultimate Edition** (PushTheWinButton, 2016): full re-implementation for compatibility and balance, fixes text/loading-screen mismatches, uses scripting so changes are optional, adjusts other mods' content, restores the cut .22LR Varmint Rifle, Better Armed Bright Followers and the Scorched Sierra Power Armor Helmet. **SawyerBatty** (2022), **Vigor** ("a vanilla JSawyer fork", 2023), **Agua Fria** (above) |

Design lesson: the person who built the game published, about 14 months after launch and after official support had ended, the tuning he wished had shipped: lower HP and carry weight, slower leveling, scarcer healing. The community adopted it as the baseline for hardcore play for fifteen years. The mod also shows the cost of shipping an easier default: the *fan fork tree* is the proof of a missing difficulty tier. Lesson for us: ship two named rule-sets (Standard / Hardcore) with the designer's preferred numbers in the second.

#### 3.3.2 Project Nevada, FOOK and other overhauls

| Mod | Author / year | What it changes | Vanilla shortcoming | Lesson |
|---|---|---|---|---|
| **Project Nevada** | Team that made Fallout 3 Wanderers Edition (idea by Kai Hohiro; snakster, delamer, T3T, x-quake, TheCastle, Zealotlee, Mezmorki and others). 2011, final update June 2014 (fallout.wiki) | Four optional modules: Core (new shooting and movement), Cyberware (implants with body-part slots), Equipment (weapons, armour, ammo), Rebalance (tougher survival and progression: fewer aid items and ammo, slower leveling). Includes dynamic crosshair, Bullet Time at AP cost, sprinting that can knock down enemies, grenade hotkey, variable zoom, stealth fields, night/heat/EM vision, explosives that open locks. Stated goal: "more interesting - eventually more challenging" with shooting and roleplaying improvements | Stiff movement and gunfeel; generous aid items and ammo (inferred; the page does not name a flaw) | Modular design: allowing players to turn off the features they dislike was the winning architecture. |
| **FOOK - New Vegas** | Jonnyeah, Millenia, Xporc (lead), BAN (QA); 2010 | Bug fixes, NPC stat rebalancing, textures, ~70 apparel, 60 weapons, 15 food items, 4 locations; "Communist" perk; weapon-schematic crafting from Fallout 3; playable raider, lobotomite and tribal presets; night vision; FOOK Menu with QA options (needs NVSE); full DLC support. Assets reused in Project Nevada; many fixes included in YUP | Content gaps and bugs | Overhaul mods are pipelines: fixes migrate to the unofficial patch, content to other overhauls. |

Unbogus and community "Hardcore Mode" variants remain `[UNVERIFIED]`; the lesson is the same (time-to-kill, ammo scarcity, perk rebalance).

### 3.4 Content and reactivity (VNV content page)

| Mod | Function | Lesson |
|---|---|---|
| The Living Desert | Hundreds of NPCs and scripted events for a more alive, reactive wasteland | Overworld encounters should have more authored variety and reactivity. |
| Better Brotherhood | Fame sources, fixed ending slides, repair services, leveled-list changes | Cut/under-served factions get filled in. |
| Goodies | Large collection of restored cut content and consistency fixes | Restored cut content is a standing community project. |

#### 3.4.1 Cut content, console memory, and bounty content

Wikipedia (New Vegas) records the cuts: three Legion-controlled settlements east of the Colorado River and post-story content (extra NPC dialogue and NPC locations that varied with the ending) were dropped; post-story content was dropped in beta to prioritise optimisation; console dev kits showed the Strip was badly optimised, so Obsidian split it into sections separated by loading screens; Havok was a hard console requirement.

| Mod | Author | What it restores or adds | Evidence |
|---|---|---|---|
| **Uncut Wasteland** | sandbox6 (snippet-only; the YUP co-maintainer) | Miscellaneous objects seen in pre-release footage "likely cut for performance"; ships compatibility files with Freeside Open and Outside Bets (snippet) | Nexus mod 56625 (page itself 403) |
| **Freeside Open** (New Vegas Uncut) | moburma80 (snippet-only) | Revamps Freeside as one worldspace instead of the loading-screen-separated Strip, re-enables large amounts of cut content, lets Rotface's cut quest be completed; New Vegas Uncut 1, 3 and 7 are integrated. Conflicts with other mods editing Freeside; TTW lists it incompatible | Nexus snippets; Simple Open Freeside and an Uncut Wasteland patch exist |
| **LD's Improved New Vegas** | LDtheCourier | Restores NPC animations (sleeping, smoking, visiting other areas), better NPC AI, more enemy spawns, the town of Underpass with its removed NPCs, extra cut NPCs (one fully voiced on the road from Goodsprings to Primm); still work in progress | NME (6 Sep 2022); PCGamesN says the content was cut to spare console memory and processing power; NME says hardware limits, not specifically memory |
| **New Vegas Bounties I-III** | Someguy2000; NVB II is fully voiced with an infinite "Radiant" bounty system after the main quest; NVB I LE remaster by RoyBatterian (2022). Original years not retrieved | A bounty-hunter career across the Mojave, a role Fallout never systemised (inference); author cites Fallout 3's Regulators as an early inspiration | Nexus snippets and gfinity coverage of the 2022 makeover |

Lesson: cuts forced by console memory on a 2010 game were rebuilt as PC mods within a decade. Where hardware forced a cut, consider keeping the design in your pipeline so a later patch can restore it.

### 3.5 Total conversions and merges for NV

| Project | What it is | Verified facts | Lesson |
|---|---|---|---|
| Tale of Two Wastelands | FO3 + NV in one engine | Listed on Wikipedia NV page; dedicated guide exists | See Section 2. |
| Fallout: New California | Prequel mod on NV engine by Radian-Helix Media (Brandan Lee) | Started as Project Brazil, renamed 1 Sept 2017. First installment 31 May 2013, second installment public beta 23 Oct 2018; ~5,000 lines of voiced dialogue in part 1, over 16,000 in the second beta; team of three plus a roster of actors; Mod DB Mod of the Year 2018 (Players Choice and Editors Choice); official GOG release July 2026 per Wikipedia | A small team with strong writing and full voice can earn a decade of attention. |
| Fallout: The Frontier | Large NV-engine mod set in the Pacific Northwest (Portland, Oregon; snowy terrain), by the Frontier Team | Development began about May 2014 (Maybenexttime, lead; seven years per Eurogamer headline cited on fallout.wiki); "at least 30-40 active modders", over 100 contributors; 3 major questlines, 60+ side quests, "tens of thousands" of voiced lines, hundreds of armours/weapons, ~40 new creatures by 2019; Game Informer: 15+ hours of new story. **Released on Nexus at the end of Jan 2021; the launch overloaded Nexus servers; over 100,000 unique downloads by 26 Mar 2021** (fallout.wiki). **Controversy (Jan-Feb 2021):** the team found that one artist had made inappropriate content involving anthropomorphic minors; the artist and their contributions (including the Pip-Boy icons) were removed, the team pulled the mod itself by its own account, several voice actors and artists asked to be dissociated from the project, lines from two characters touching slavery were cut, and the Steam launch was postponed. It returned on Nexus with vanilla Pip-Boy icons and the removed content cut; a "Trochili" character was locked pending an optional ESP. fallout.wiki reports that a later 2021 rework was undermined by "poor management", the project fell apart about 18 months later, and some members started *Rose City Tales*. Wikipedia (NV) calls it a DLC-sized expansion that "drew media attention for its size and controversial content" | Long-awaited TCs ship late; scope and staff vetting matter; large volunteer teams need content moderation and a clear leadership structure. Distribution through a storefront with huge traffic (Nexus servers crashed). |
| Fallout 4: New Vegas, Capital Wasteland, Miami, Cascadia (FO4 mods) | Ports/new regions in FO4 engine | Not verified this session. `[UNVERIFIED]` | Fans repeatedly recreate the regions they love; setting reuse is a long-term pull. |

## 4. Fallout 4

TMR (The Midnight Ride) is the equivalent of VNV. Everything below is verified from the TMR pages unless marked.

### 4.1 Stability and engine

| Mod | Function | Lesson |
|---|---|---|
| Unofficial Fallout 4 Patch (UFO4P) | Fixes thousands of bugs in base game and DLC (TMR). First release **25 Apr 2016**, about five months after launch, uploaded by Arthmoor of the Unofficial Oblivion/Skyrim Patch team; the first version fixed "hundreds" of gameplay, quest, NPC, object, item, text and placement bugs, needed game patch 1.5.146+, made no unsafe edits (such as deleting stock objects), and its creators say it will never be sold (Wccftech, 25 Apr 2016). Version 2.0.x kept adding Papyrus and location fixes (snippet-only) | Same as NV. A third-party team has patched every Bethesda-engine RPG since Oblivion; budget QA accordingly. |
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

#### 4.2.1 Dialogue legibility: Full Dialogue Interface and Extended Dialogue Interface

Context (Wikipedia FO4): about 111,000 lines of dialogue and the series' first fully voiced protagonist, including every decision option. Reviewers faulted FO4's simplified role-playing versus FO3 and NV (Wikipedia FO4), and Dexerto calls dialogue and quests "blander". The paraphrased wheel is the visible symptom: the shipped game shows a 2-4 word prompt while the spoken line may say something different.

| Mod | Author / date | What it does | Vanilla shortcoming | Evidence |
|---|---|---|---|---|
| **Full Dialogue Interface (FDI)** | Shadwar (Russian modder; interface, "100% Shadwar's work") with Cirosan (English adaptation). Game Informer reported it on **18 Nov 2015**, eight days after launch; Kotaku followed on 29 Dec 2015 | Replaces the circular paraphrase wheel with a top-to-bottom list showing the exact subtitle text of each line, selectable with number keys or gamepad. Keyboard and gamepad versions. Known limit: English "sarcastic" options show only a "[Sarcastic]" label rather than the line; reported working in all dialogue except dismissing companions; Xbox One / PS4 versions were reported later (snippet-only). Installation needs removing DialogueMenu.swf and editing ini files | The mod's authors say the prompts were "inconsistent and confusingly arranged" and made conversation feel like "a crapshoot" (Kotaku summary of the mod page); "players sometimes said things they didn't intend" (Game Informer). FO3 showed full text; FO4 moved to a prompt system like The Witcher 3 and Mass Effect | Covered by Game Informer, Kotaku, Game Revolution, PC Gamer, DSOGaming (headlines; several bodies unreadable); Nexus page 1235. No download total retrievable |
| **Extended Dialogue Interface (XDI)** | registrator2000 (GitHub `reg2k/xdi`, 31 commits, 21 stars). Date not shown | An F4SE engine modification that removes the **hardcoded 4-option limit** so mods can offer any number of dialogue options; replaces DialogueMenu.swf, so it cannot be used alongside FDI | The engine cannot show more than four player replies at once, which constrains dialogue design | Nexus mod 27216; used as framework for "expanded dialogue" mods such as the 200-line dialogue expansion covered by Gfinity (snippet-only) |

The same author, registrator2000, wrote *Better Inventory* for Fallout 76 (Section 5), showing that a handful of UI-focused modders move between Bethesda games.

Design lesson: the first big FO4 mod, within days of launch, undid a design decision. Dialogue that hides its own words destroys the player's agency; if you want a voiced protagonist, show the line you will speak. Do not engineer a UI to a four-option ceiling.

FO4 UI replacements such as DEF_UI and FallUI remain `[UNVERIFIED]` here (not in the fetched lists).

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

Place Everywhere, Commonwealth Captures, Nuka World/Far Harbor overhauls, and the FO4 ports of other regions (Fallout 4: New Vegas, Capital Wasteland, Miami, Cascadia) remain `[UNVERIFIED]` for downloads and detail (existence from background knowledge; Place Everywhere exists mostly because the vanilla workshop imposes snapping and placement limits). Another reference point (Wikipedia, Mod article): Caliente's Beautiful Bodies Edition has been downloaded at least 8.2 million times, showing body/appearance mods can dwarf gameplay mods in raw download counts (Nexus).

#### 4.4.1 Sim Settlements 1 and 2 (kinggath)

| Item | Detail |
|---|---|
| Author | kinggath. First FO4 mod was *Salvage Beacons* (a settler-based answer to pack-ratting); started Sim Settlements after getting "sick of building all the details necessary to make a cool looking settlement" while playing Survival mode (Nexus interview, snippet-only) |
| What it does | **SS1 (2017):** settlers plan and build their own homes, shops and farms from "city plans" (PC Gamer: assigns NPCs to plan and manage settlements; named PC Gamer's Best Mod of 2017, snippet-only). Expansions included Rise of the Commonwealth and Conqueror (attack and conquer settlements, a raider questline; PCGamesN/PC Gamer snippets). **SS2 (2020):** a sequel that asks "what if there was a reason for my character to help rebuild settlements?" (fallout.wiki): a voiced story with "dozens of fully voiced NPCs", build-yourself or automatic mode, Chapter 2 (the Gunners as a growing threat), Chapter 3 (warfare, capturing non-settlement territory, a Gunner invasion), about ten related SS2 mods 2020-2024. SS1 still received bug fixes after SS2 (kinggath, PC Gamer snippet) |
| Vanilla shortcoming | Bethesda's settlement system is a manual building toy with no narrative payoff, heavy micromanagement and limits on settlement scale (Midnight Cult Fix, Place Everywhere) |
| Scale | SS2 wiki release list (12 Dec 2025) shows Chapter 1 and Chapter 2 at version 3.5.1; works on PC and Xbox via Creations; requires Workshop Framework. Translated into at least Spanish, German, French, Russian, Turkish, Portuguese and Mandarin (Nexus listing, snippet-only). No download totals retrievable |
| Lesson | A system the player must fiddle with needs automation and a reason to exist. The mod turned a build toy into a loop with factions, story and consequences. |

#### 4.4.2 Alternate starts: Start Me Up, Another Life

| Mod | Author | What it does | Evidence |
|---|---|---|---|
| **Start Me Up - Alternate Start and Dialogue Overhaul** | TinyManticore (Nexus 18946). Start Me Up Redux is the maintained continuation; credit attribution for Redux is disputed across Nexus pages `[DISPUTED]` | Not just a quick-start: an overhaul of the opening and early dialogue; warns against combining with other alternate-start mods. Alternatives for a pure skip: SKK Fast Start + Piper Interview Restored; "No Launch Intro" only skips logos | Nexus search snippets |
| **Another Life - Alternative Start** | Xylozi (Nexus 14253) | An alternative-start mod (a quick-start save pack exists that begins in its "Processing Room"); description not fetched, so the detail of the start options is `[UNVERIFIED]` | **104,757 unique downloads** on the Nexus listing when seen in search results (snippet-only; date of snapshot unknown) |
| "Alternate Start - Live Another Life" | **Arthmoor, for Skyrim**, not Fallout 4 | Gave Skyrim the same fix for the Helgen intro; earlier draft misattributed this to FO4 | Nexus snippet |

Vanilla shortcoming: Fallout 4 fixes the protagonist's backstory (the prologue, Vault 111, and the lost spouse and son) and the first hours are the same for every player. Wikipedia lists the simplified role-playing as a main FO4 criticism. The size of the alternate-start category (several competing mods, one with 100,000+ downloads) is the evidence.

#### 4.4.3 Horizon and survival

| Item | Detail |
|---|---|
| Horizon | Nexus mod 17374 (author not confirmed in fetched pages `[UNVERIFIED]` for authorship). Version 1.4 covered by GamingBolt on 6 Dec 2017 (and JikGuard, DSOGaming) as an overhaul of loot, level scaling, combat, medical items, perks, travel, survival and progression across **25 categories**; later releases added a death-revival system, a scrapping tool, crops, vendors and buildings, an Architect tool, NPC scaling and dynamic encounters; Nexus now shows a 1.9.x series. Needs F4SE and Address Library, intended as a whole-playthrough mod ("should not be removed midway"). "Horizon Wormed" eases the survival values |
| Survival mods in general | Healing in Horizon "demands more": resting or eating alone does not restore health. Pass 1 already covered Unlimited Survival Mode and Safe Travels, which configure the official Survival mode |
| Lesson | A modded Survival mode that can be rebalanced is better than a fixed one. Horizon's existence (and a softer fork) proves both the demand for scarcity and the limits of its taste. |

### 4.5 Fallout: London (the major FO4 total conversion)

| Fact | Value | Source |
|---|---|---|
| Release | 25 July 2024 (development began 2019) | Wikipedia |
| First-day downloads | Over 500,000 in 24 hours; "fastest redeemed title ever" on GOG | Wikipedia |
| Team | Almost 100 modders, 100+ voice actors, ~20 testers (versus ~150 for FO4) | Wikipedia |
| Reception | IGN 7/10, Gamereactor 8/10, GamingBolt 8/10, PCGamesN 9/10; praised setting and British culture; criticized bugs, crashes, performance; one reviewer called it "barely playable" at launch | Wikipedia |
| Platform fallout | Delayed by Bethesda's next-gen update; Steam users had to roll back the game, GOG users did not | Wikipedia |
| Later | VR version 28 May 2025; expansion "Rabbit and Pork" 30 Sept 2025 | Wikipedia |

Additional detail from search results (headline/snippet-only unless noted): GOG's own wording is that the game was "redeemed" more than 500,000 times in its first 24 hours, which it called the fastest-redeemed title on the store (PC Gamer, KitGuru, OpenCritic, Ensigame headlines); PC Gamer dates the release 24 July where Wikipedia says 25 July `[DISPUTED by one day, likely time zone]`; it was only available through GOG (not Steam Workshop or Nexus); made by Team FOLON over nearly five years; GOG said most launch problems were due to how complex the install was for individuals. Team size (~100 modders) comes from Wikipedia only; no second source was reachable.

Lesson: fans prefer a new setting with fresh culture over additional content in a familiar setting; a free mod nearly outpaced many commercial releases in day-one demand. Distribution through a storefront (GOG) with a compatible build mattered, and a mod that needed a rollback of the base game (Steam) showed how fragile the mod stack is to base-game updates.

### 4.6 Monetising mods: the paid-mods backlash and Creation Club

| Date | Event | Evidence |
|---|---|---|
| 23 Apr 2015 | Valve and Bethesda open paid Workshop mods for Skyrim; reported split: 25% to modders, 30% to Valve, 45% to Bethesda (snippet-only; sources vary) | Engadget, Game Informer, GameSpot headlines |
| 24-27 Apr 2015 | A petition to remove paid mods passed 51,000 signatures in the first 24 hours (133,013 total in one report); Valve removed the feature within about four days and refunded buyers; Valve's Alden Kroll: "It's clear we didn't understand exactly what we were doing." Bethesda said the feedback "had been clear" | Engadget, Shacknews, CSO, Game Developer (snippets) |
| 2016 | Fallout 4 mod support reaches Xbox One (May 2016) and PS4 (Nov 2016); Howard said the paid-mod effort would not be repeated for FO4 | Wikipedia FO4 |
| E3 2017; **29 Aug 2017** | **Creation Club** announced and launched for FO4 (patch 1.10). Critics called it "paid mods"; Bethesda insisted it was independent creators funded by Bethesda, not paid mods. Complaints: content similar to free mods, and purchases require in-game credits bought with real money. Pete Hines argued modders are developers and should be paid. Some modders supported it for quality control and because it prevents others from stealing and selling their mods | Wikipedia (Creation Club), TechRadar, RPG Site, IBTimes, TweakTown headlines |
| 2019 | A class-action lawsuit alleged Creation Club broke the promise that the FO4 Season Pass covered all DLC; the court compelled arbitration | Wikipedia (FO4, Creation Club) |
| 5 Dec 2023 | Creation Club replaced by "Creations" (free mods plus paid content with a verified-creator royalty program) per Wikipedia; a snippet from the Fallout wiki dates the FO4 change to the Anniversary Edition on 10 Nov 2025 `[DISPUTED]` (probably the same system reaching FO4 later) | Wikipedia (Creation Club); snippet |
| Oct/Nov 2025 | FO4 Anniversary Edition bundles Creation Club content and adds a workshop; reviews mostly negative; popular mods broke because of the Creation Club menu and scripting interface changes. Wikipedia gives conflicting release dates (23 Oct and 10 Nov 2025) `[DISPUTED]` | Wikipedia FO4 |

Lesson: the community treats modding as a commons. Monetisation is accepted when it is clearly additive and curated, and rejected when it appears to monetise existing free work. Do not break the free mod ecosystem with updates.

## 5. Fallout 76

- No general mod support. Bethesda banned players for mod use and duplication; players said bans hit people who used mods for visual/technical fixes (Wikipedia FO76). Bethesda's help page says Fallout 76 "does not support the use of any mods, add-ons, or other third-party programs" (snippet); late-2018 bans targeted third-party applications and offered an appeal that required an essay on why cheat software harms an online community (PC Gamer, HotHardware, Dexerto, TweakTown headlines/snippets). Some players said they were banned for visual-enhancement mods; Bethesda's stated reason was competitive advantage and server impact.
- Launch Metacritic scores 49-53 (Xbox/PC/PS4), Eurogamer called the launch "a bizarre, boring, broken mess"; Wastelanders (April 2020) added human NPCs and improved reception (Wikipedia).
- **Why there is so little modding (analysis):** it is a server-authoritative online game (so a modded client cannot change rules), Bethesda has publicly called third-party programs unsupported and banned for them, and there is no Creation Kit-style official toolchain in the pages consulted (absence not directly verified `[UNVERIFIED]`). What does exist is client-side UI, which is exactly the part of the game the vanilla build neglected.
- **Mods that appeared within weeks of launch** (Kotaku, 3 Dec 2018; all PC; none confirmed safe by Bethesda):

| Mod | Author | What it does | Vanilla shortcoming |
|---|---|---|---|
| Lock pick bar | Not named | Shows the sweet spot for bobby pins | Lockpicking frustration (same as FO4's Remember Lockpick Angle) |
| UI facelift | Not named | Resizes the HUD so it does not block the view | A large, obstructive HUD |
| Better Inventory | "Rigistrator2000" (the same author as FO4's XDI) | Adds inventory filters and shows the combined weight of each item category | A long unfiltered item list in a loot-heavy game |
| Perk Loadout Manager | Keretus | Saves perk loadouts (three at the time; later versions and forks support many more, with hotkeys and an undo backup; snippet-only) and switches in one click | Re-picking perk cards by hand each time you change activity (build respec friction) |
| Glowing Items | bwins95 | Coloured outlines per item type | Hard-to-see loot |

  Nexus has a Fallout 76 section, and PLM works through a community script extender ("SFE") or a "PLM Bridge" without it (snippet-only); one 2020 forum user reported using chat, perk loadout and Better Inventory with no ban (anecdote). Kotaku's author hoped Bethesda would not disable them if it ever released official mods; Bethesda did not respond.
- Evidence of unmet need: human NPCs and quests (added later), inventory filters, perk loadouts, readable loot. The few mods that exist are all UI, which suggests the vanilla UI was the main point of friction.

## 6. Cross-cutting: vanilla neglect to community build to recurrence

Games counted: FO1, FO2, FO3, NV, FO4, FO76. "Verified" means at least one fetched source named a specific mod for that game.

| Vanilla neglect | What the community built (by game) | Recurs in | Frequency | What to ship instead |
|---|---|---|---|---|
| **Bugs at launch; no or short official support** | FO1: Fallout Fixt + TeamX patches. FO2: killap's Unofficial Patch (800+ bugs), RPU. FO3: Unofficial Fallout 3 Patch. NV: YUP (15 Aug 2013), Unofficial Patch NVSE Plus. FO4: UFO4P (25 Apr 2016, about five months after launch). FO76: none (server-side game; mods banned) | FO1, FO2, FO3, NV, FO4 (5 of 6) | **Universal** | A QA budget sized to content; a 12-24 month post-launch fix plan; open the data so volunteers can help (UFO4P's team say it will never be sold) |
| **Engine/script limits and memory ceilings** | FO1/FO2: sfall (Timeslip). FO3: FOSE, 4 GB/LAA patch, Stutter Remover, GFWL disabler. NV: NVSE (same team as FOSE), 4GB Patcher, NVTF, NVAC, lStewieAl's fixes. FO4: F4SE, Addictol, XDI | FO1 (via sfall in Fixt), FO2, FO3, NV, FO4 (5 of 6) | **Universal** | 64-bit, large-address-aware executable; documented scripting hooks; data-driven tables |
| **Resolution, OS and platform compatibility** | FO1/FO2: Mash's hi-res patch (3.0 on 23 May 2011), sfall; Community Edition (2023, 5 platforms). FO3: LAA, GFWL removal. NV: 4GB patcher, High Resolution Screens. FO4: FOV slider | FO1, FO2, FO3, NV, FO4 (5 of 6) | Very high | Resolution-independent UI, native FOV and ultra-wide support, no always-on third-party launcher |
| **UI built for a controller or for low screens: too little information per page, no search, unclear highlights** | FO3: DarNified UI (more HUD data, more items per list; snippet-only), Vanilla UI Plus. NV: 13 UI mods in VNV, Menu Search (Ctrl-F in six menus), Clean Vanilla HUD. FO4: Crafting/Workshop Highlight Fix, FDI, Simple FOV Slider. FO76: Better Inventory, UI facelift, Glowing Items | FO3, NV, FO4, FO76 (4 of 6; FO1/FO2 only resolution) | **High** | Filter/search everywhere; configurable density; legible highlights; a PC-first layout |
| **Colour grade / art direction** | FO3: Fellout (removes the green tint; verified, PCGamesN). NV and FO4: colour/ENB mods exist in general but were not verified here `[UNVERIFIED]` | FO3 (verified) | Single verified case | Give players a colour-grade slider and let art direction survive it |
| **Tuning too easy: loot and healing too generous, levelling too fast** | FO3: FWE (needs, triage, rarer loot, ammo weight), FOOK2. NV: Project Nevada Rebalance, JSawyer (written by the project director), Ultimate, Agua Fria. FO4: Horizon, Loot Logic and Reduction, SPARS. FO1: Fo1in2's optional "tougher mutants" setting (partial) | FO3, NV, FO4 (3 of 6; plus partial FO1) | **High** | A designer-owned Hardcore ruleset shipped at launch with modular toggles |
| **Cut or planned content never shipped** | FO1: Fixt integrates the Fallout 1 Restoration Mod. FO2: Restoration Project (EPA, Primitive Tribe, Abbey, Vault Village, Slaver's Camp, 2008). FO3: TTW restores unused FO3 content. NV: Goodies, Uncut Wasteland, Freeside Open, LD's Improved New Vegas (console cuts). FO4: Legendary Mutation Messages Fix; "Cutting Room Floor" radio mod exists on fallout.wiki | FO1, FO2, FO3, NV, FO4 (5 of 6) | **Universal** | Publish a cut-content record; ship what you can afford; let modders restore the rest |
| **Dialogue legibility and option count** | FO4: Full Dialogue Interface (18 Nov 2015), XDI (removes the 4-option cap). FO3/NV: DarNified shows more options (snippet-only) | FO4 clearly (1 of 6, 2 with FO3/NV partial) | One game, instantly | Show the line you will say; no hidden paraphrase; do not hardcode a 4-option wheel |
| **Fixed opening and protagonist** | FO3: FWE built-in alternate start. NV: Custom Start Resource listed on fallout.wiki. FO4: Start Me Up, Another Life (104,757 unique downloads snippet-only), SKK Fast Start | FO3, NV, FO4 (3 of 6) | Medium | Optional skip and alternate backgrounds; never lock the first hour |
| **Old content stranded in an old engine** | FO1 into FO2's engine (Fo1in2, 851 stars). FO3 into NV (TTW, level cap 50 to 60). FO2 engine reimplemented (Reference/Community Edition 2023). FO4: FO4 New Vegas / Capital Wasteland / Cascadia ports `[UNVERIFIED]` | FO1, FO2, FO3 verified (3 of 6) | Medium | Keep format specs and engine source accessible; forward-compatible save/content formats |
| **No modern commercial equivalent of the game's form, or the setting is exhausted** | FO1/FO2 engine: Nevada, Olympus 2207, Resurrection, Sonora, Last Hope. NV: New California, The Frontier. FO4: Fallout: London (500,000+ GOG redemptions in 24 h) | FO1, FO2, NV, FO4 (4 of 6; none for FO76) | **High, and getting larger** | Strong, distinct setting plus full voice acting; build with modders in mind |
| **Systems without a purpose** (settlements, crafting, bounty hunting) | FO4: Sim Settlements 1 and 2 (PC Gamer Best Mod 2017, snippet-only), Place Everywhere. NV: New Vegas Bounties. FO3: weapon-mod kits (fallout.wiki list) | FO3, NV, FO4 (3 of 6) | Medium | Give each system a loop and a story reason |
| **Survival and needs** | FO3: FWE. NV: Hardcore tweaks inside JSawyer/Agua Fria; Sleep Wait Hardcore Needs. FO4: Horizon, Unlimited Survival Mode, Safe Travels | FO3, NV, FO4 (3 of 6) | Medium | Configurable survival with forecasts; separate the grind from the challenge |
| **Companions and followers** | FO2: Party Orders (RPU). NV: Companion Tweaks and Changes (fallout.wiki list), Clean Companion Wheel. FO4: Follower AI fixes, Dogmeat Lags Behind | FO2, NV, FO4 (3 of 6) | Medium | Companions need pathfinding, commands and personality |
| **Monetisation and ecosystem trust** | 2015 Skyrim paid-mods reversal in four days; FO4 Creation Club (2017) "paid mods" row; FO4 next-gen/Anniversary updates that broke mods; FO76 bans for third-party tools | FO4/FO76 era (2 of 6; also Skyrim) | Recent but hot | Free mod support, stable APIs, no surprise breaks |

Reading the table: three categories (bugs, engine limits, cut content) recur in every game that had a mod scene. Dialogue legibility and colour grading are one-off shocks tied to a specific design choice (a voiced protagonist, an art filter). The rebalance and total-conversion categories are growing, which suggests the player base wants *longer, harder, more authored* versions of the same games.

### 6.1 Cluster summary (pass 1, retained)

| Cluster | Players consistently fix | Therefore ship |
|---|---|---|
| Stability | Crashes, save bloat, quest blockers, memory limits, stutter | A QA budget sized to content, a 64-bit engine, a crash logger, autosave rotation. |
| UI | Search, filter, HD textures, readable highlights, config menus, preview of needs effects | Searchable, filterable lists; readable outlines; in-game settings. |
| Rebalance | Slower leveling, lower carry weights, scarcer loot, longer meaningful progression | Tuned progression with level cap and loot density audited by designers. |
| Quest friction | Nagging givers, radiant spam, region-leaking radiant quests | Authored quest cadence; limit radiant content; let player decline. |
| Combat | Reload control, recoil, hit feedback, movement | Good gunfeel at launch, readable feedback. |
| Survival | Optional hardcore needs with forecast UI and configurable saves/travel | Offer a difficulty tier with transparent needs and flexible rules. |
| Start | Alternate starts (Start Me Up, Another Life for FO4; FWE's built-in start for FO3; Skyrim's "Live Another Life" is the model) | Let players skip or choose the opening, avoid forced backstories (verified existence; one 104,757-download snippet). |
| Settlements | Placement freedom (Place Everywhere `[UNVERIFIED]`), automated city-planning (Sim Settlements, verified through fallout.wiki) | Build tools that are flexible, not fiddly; give settlement activity story purpose. |
| Dialogue | Full Dialogue Interface, Extended Dialogue Interface | Show the exact line; no 4-option cap. |
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
- Let players choose their start and not be forced into a backstory (the alternate-start mods exist because players want it: Start Me Up, Another Life with 104,757 unique downloads in one snippet; FWE had a built-in alternate start in 2010).
- Offer a settlement/base system only if its placement is flexible and its output feeds the story.
- Write with a distinct culture and voice. Fan projects that last (New California, London) win on setting and voiced writing, not graphics.
- Do not punish modders or ban players for fixing the game; the community's fixes are a free QA team.
- Ship the designer's hard mode. The most-used rebalance in Fallout history (JSawyer, then Ultimate/Agua Fria) was the project director's own list of changes he did not think the default audience would accept: lower HP and carry weight, slower leveling, a lower level cap, scarcer healing and food, and survival thresholds that bite less often but harder. Offer it as a named difficulty with toggles instead of waiting for a fan fork.
- Show the exact line the protagonist will say. Full Dialogue Interface appeared eight days after Fallout 4 launched; a hardcoded four-option wheel is a design ceiling, not a feature (XDI had to remove it).
- Do not discard the design record: Restoration Project, Uncut Wasteland and Freeside Open each rebuilt features that were planned and cut for schedule or console memory. Keep cut content documented and re-implementable, and distinguish clearly what is restored from what is new.
- Give every system a purpose. Sim Settlements won PC Gamer's Best Mod of 2017 (snippet-only) by adding story, automation and consequences to a building toy; Settlement mechanics need loops, not just placement.
- Ship a curated list of "known good" patches or a built-in compatibility layer. VNV exists because players cannot choose among 100 fixes themselves; Fallout Fixt's purist / standard / full installer is the same idea at smaller scale.
- Treat total conversions as a growing market, not a threat: Fallout: London logged 500,000+ GOG redemptions in 24 hours, the Frontier passed 100,000 unique downloads within two months of release, and four volunteer teams shipped 100-quest campaigns on a 1998 engine. Keep tools and file formats open, and expect volunteer teams to need moderation, leadership and clear credits (The Frontier's 2021 collapse).
- Avoid surprise monetisation of free community work (the 2015 paid-mods reversal in four days; Creation Club in 2017). If you sell content, sell it as additive and curated, and do not break existing mods with updates.
- For an online game, expect to ship the UI quality-of-life yourself: FO76's only mod scene is UI (inventory filter, perk loadouts, outline colours) under an anti-mod policy.

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

Consulted in pass 2 (pages actually fetched, content read):
- https://fallout.wiki/wiki/Mod:JSawyer
- https://fallout.wiki/wiki/Mod:JSawyer_Ultimate
- https://fallout.wiki/wiki/Mod:Project_Nevada
- https://fallout.wiki/wiki/Mod:Fallout_3_Wanderers_Edition
- https://fallout.wiki/wiki/Mod:Fallout_3_Mods
- https://fallout.wiki/wiki/Mod:Tale_of_Two_Wastelands
- https://fallout.wiki/wiki/Mod:Fallout:_The_Frontier
- https://fallout.wiki/wiki/Mod:Fallout:_Nevada
- https://fallout.wiki/wiki/Mod:Fallout:_Sonora
- https://fallout.wiki/wiki/Mod:Olympus_2207
- https://fallout.wiki/wiki/Mod:Fallout_1.5:_Resurrection
- https://fallout.wiki/wiki/Mod:Fallout_2_Community_Edition
- https://fallout.wiki/wiki/Mod:Fallout_2_Reference_Edition
- https://fallout.wiki/wiki/Mod:Fallout_2_Mods
- https://fallout.wiki/wiki/Mod:Yukichigai_Unofficial_Patch
- https://fallout.wiki/wiki/Mod:FOOK_-_New_Vegas
- https://fallout.wiki/wiki/Mod:FNV_4GB_Patcher
- https://fallout.wiki/wiki/Mod:New_Vegas_Script_Extender
- https://fallout.wiki/wiki/Mod:Sim_Settlements_2
- https://fallout.wiki/wiki/Category:Fallout_3_mods, Category:Fallout:_New_Vegas_mods, Category:Fallout_4_mods, Category:Fallout_2_mods
- https://dtf.ru/games/2955721-fallout-2-luchshee-i-budushee-moddinga (Fallout 2 modding history with dates)
- https://worthplaying.com/article/2008/1/9/news/47869-fallout-2-restoration-project-available-now/
- https://www.gamebanshee.com/news/111901-fallout-2-restoration-project-22-a-unofficial-patch-released.html
- https://www.gamebanshee.com/xq3p (Fallout 2 High Resolution Patch 3.0)
- https://f2rp.bgforge.net/ (Restoration Project guide; location sections only)
- https://bgforge.net/docs/fallout/restoration-project-updated
- https://github.com/BGforgeNet/Fallout2_Unofficial_Patch
- https://raw.githubusercontent.com/BGforgeNet/Fallout2_Restoration_Project/master/README.md
- https://fodev.net/files/fo2/fo1in2.html
- https://rpgcodex.net/article.php?id=9143 (Fallout FIXT Alpha 6.1)
- http://www.gamebanshee.com/kpkf3 (JSawyer v4 changelog)
- https://gist.github.com/dbb/3748244 (copy of the JSawyer changelog/readme)
- https://www.engadget.com/2011-12-30-fallout-new-vegas-designer-makes-his-own-unofficial-mod.html
- https://gameinformer.com/b/news/archive/2011/12/29/fallout-new-vegas-39-lead-designer-releases-mod-for-his-own-game.aspx
- https://www.gamewatcher.com/2011-31-12-unofficial-fallout-new-vegas-mod-released-by-lead-designer
- https://www.gameinformer.com/mod-corner/2021/02/01/why-anticipated-fallout-new-vegas-the-frontier-mod-was-taken-down
- https://www.nme.com/news/fallout-new-vegas-mod-restores-cut-content-from-over-a-decade-ago-3304956
- https://www.pcgamesn.com/fallout-new-vegas/cut-content-mod
- https://www.pcgamesn.com/fallout-3/mods (Fellout, UFO3P, Mart's Mutant Mod)
- https://sourceforge.net/app/updated-unofficial-fallout-3-patch/
- https://kotaku.com/fallout-4-s-full-dialogue-mod-makes-the-game-way-better-1750181929
- https://www.gameinformer.com/b/news/archive/2015/11/18/new-fallout-4-mod-lets-you-know-just-what-youre-saying.aspx
- https://github.com/reg2k/xdi
- https://wccftech.com/unofficial-fallout-4-patch-fixes-hundreds-bugs/
- https://gamingbolt.com/fallout-4s-horizon-1-4-mod-overhauls-the-game-and-its-systems-significantly
- https://kotaku.com/modders-are-making-fallout-76-less-frustrating-to-play-1830831357
- https://en.wikipedia.org/wiki/Creation_Club
- https://en.wikipedia.org/wiki/Fallout_(video_game) (patches 1.1/1.2 only)
- https://github.com/sfall-team/sfall and https://github.com/rotators/Fo1in2 (re-read for stats)

Snippet-only (search-result summaries; pages not read, 403/truncated/unavailable). Treat as unverified leads:
- NMA Fallout Fixt resource pages: https://www.nma-fallout.com/resources/fallout-fixt-full-all-fixes-and-mods.8 (bug/feature counts)
- ModDB Restoration Project page (800+ bugs): https://www.moddb.com/mods/fallout-2-restoration-project
- GOG forum quoting killap: https://www.gog.com/forum/fallout_series/killaps_unofficial_fallout_2_patch_version_1_02_26_has_been_released
- https://recapio.com/digest/fallout-2-restoration-project-is-quirky-by-warlockracy (Sulik's sister)
- https://tvtropes.org/pmwiki/pmwiki.php/Trivia/Fallout2 (RP reputation; the page itself was 403)
- Nexus: Full Dialogue Interface https://www.nexusmods.com/fallout4/mods/1235; Extended Dialogue Interface https://www.nexusmods.com/fallout4/mods/27216; Start Me Up https://www.nexusmods.com/fallout4/mods/18946; Another Life https://www.nexusmods.com/fallout4/mods/14253; Horizon https://www.nexusmods.com/fallout4/mods/17374; Uncut Wasteland https://www.nexusmods.com/newvegas/mods/56625; New Vegas Bounties https://www.nexusmods.com/newvegas/mods/41184; Perk Loadout Manager https://www.nexusmods.com/fallout76/mods/124; Updated Unofficial Fallout 3 Patch https://www.nexusmods.com/fallout3/mods/19122; JSawyer Ultimate https://www.nexusmods.com/newvegas/mods/61592 (all 403 on fetch; titles/descriptions came from search snippets)
- Valve/Bethesda paid-mods reversal: https://www.engadget.com/2015/04/27/valve-reverses-skyrim-mod-payments/ and https://www.shacknews.com/article/89319/valve-removes-paid-mods-from-skyrim (snippets)
- Creation Club reception headlines: https://www.techradar.com/news/bethesdas-new-club-will-sell-premium-mods-for-fallout-4-and-skyrim, https://www.ibtimes.com/bethesda-gets-flak-over-fallout-4-creation-club-items-2583782
- Fallout: London records: https://www.pcgamer.com/games/rpg/fallout-london-sets-a-new-record-by-becoming-the-fastest-redeemed-game-of-all-time-on-gog/, https://opencritic.com/news/3918/fallout-london-was-redeemed-500-000-times-in-24-hours-breaking-gog-records, https://www.kitguru.net (redeemed half a million times)
- The Frontier: https://www.pcgamer.com/massive-fallout-new-vegas-mod-the-frontier-taken-offline-by-its-creators, https://techraptor.net/gaming/news/fallout-the-frontier-pulled-nexus-mods-controversy, https://primagames.com/news/fallout-mod-the-frontier-download (page bodies not read; headline/snippet facts only)
- FO76 bans: https://hothardware.com/news/bethesda-bans-modders, https://dexerto.com/fallout/fallout-76-players-are-being-banned-for-a-surprising-reason-263136, https://pcgamer.com/bethesda-asks-suspected-fallout-76-cheaters-to-write-essay-about-why-cheating-is-bad
- Fallout 3 tools and UI: https://www.gamepressure.com/download/fallout-3-fallout-stutter-remover-v4136-mod/zcf0a5 and Nexus forum threads (snippets); DarNified: https://forums.nexusmods.com/topic/10629648-darnifieduif3-and-fallout-3-updated-and-reverted
- NVAC/NVTF: https://www.gamepressure.com/download/fallout-new-vegas-nvac-new-vegas-anti-crash-v7510-mod/z1ecde and Steam discussion threads (snippets)

Attempted but blocked (403/402/404/unavailable): nexusmods.com mod pages and news (including Kinggath interview https://www.nexusmods.com/news/13717), moddb.com, fallout.fandom.com and falloutmods.fandom.com, nma-fallout.com, web.archive.org (blocked by the fetch tool), tvtropes.org, metafilter.com, gamerevolution.com, dsogaming.com; pcgamer.com, windowscentral.com and eteknix.com returned truncated or interstitial pages. Still `[UNVERIFIED]` after pass 2: all Nexus/ModDB download totals; authors of Mart's Mutant Mod, Fellout, DarNified UI, FOOK2 (Fallout 3), Agua Fria and Horizon; Freeside Open and Uncut Wasteland authorship (snippet-only); Sulik's-sister restoration; Fallout 4 ports of NV/Capital Wasteland/Miami/Cascadia; Place Everywhere; DEF_UI/FallUI; Fallout: London team size beyond Wikipedia; Start Me Up Redux authorship.
