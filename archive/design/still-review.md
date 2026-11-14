# The Still: Twelve-Lens Review

10 Nov 2026. Twelve independent reviewers read `design/game-concept-outline.md` v0.1 and critiqued the still
(sections 2.6 and 8 especially), each from one lens. Reviewers were told to criticise, not confirm. This file is
the record of what they found and what they agree on. Nothing in the outline has been changed yet.

## 1. Scoreboard

| Lens | Verdict | Score | Headline |
|---|---|---|---|
| Tactics and systems | Keep with changes | 5 (7.5 after fixes) | With current numbers the gas is close to decorative in combat |
| Readability and UX | Keep with changes | 5 | A faint 3D volume on a fixed overhead camera is the wrong presentation |
| Science | Plausible with fixes | 7 | Core physics is real; four details would draw an informed objection |
| Prior art | Distinctive with care | 7 | "Live above heavy gas" is not unclaimed; how it plays is |
| Story | Keep with changes | 7 | Strong on place, class and ritual; the debt plot and the gas are only half joined |
| Level design | Keep with changes | 5.5 | Scale model is incoherent; most outdoor gas is static terrain |
| Engineering | Keep with changes | 5 (7 after fixes) | The simulation is cheap; the spec is incomplete and the budget undercounts authoring |
| Sceptical player | Keep with changes | 6 (8 after fixes) | Loves the hazard, resents the logistics around it |
| Marketing | Workable with changes | 6 | Good icon, but nothing visible to sell until the gas has a look |
| Devil's advocate | Ship a simplified still | 6 | Full live simulation overspends; keep the flow where it is seen |
| Consistency audit | Not ready to paper-prototype | n/a | 16 contradictions, 11 missing rules |
| Onboarding and accessibility | Keep with changes | 5 | Learnable; accessibility is entirely unspecified |

No reviewer recommended replacing the still. Every reviewer wanted changes.

## 2. What they agree is strong

- Height and posture as the variable: the three-flame staff, sneaking lowering your head, air-marks on walls.
- The gas knocks out before it kills, which makes it a weapon, a non-lethal tool and a moral choice at once.
- Gas ignores armour, so it answers heavily armoured enemies without bigger numbers.
- Doors, caps and contained rooms are real tactical levers.
- "Harm cannot be kept, only moved" gives every faction a case and a flaw.
- Height as property and class (*Nine Metres*) is a dilemma no other setting offers.
- Deterministic, coarse, integer state is cheap to simulate, save and test automatically.

## 3. Findings raised by several reviewers

| # | Finding | Raised by | Proposed fix |
|---|---|---|---|
| 1 | **Scale model is broken.** Combat gas tops out at 2 m; the fiction has a line at 9.2 m, walks at 5-6 m, towns under the line. Layer and head-height arithmetic in 2.6 does not add up | Audit, level, engineering, UX, tactics | Store one absolute gas-surface elevation per map column in 0.5 m steps; depth at a square is derived from it. Publish one height table |
| 2 | **Seeing the gas is locked behind stats.** Reading radius is 2 + Wits; forecasts need Sounding; a perk shows the rest. Players choose these before they know what the still is | UX, onboarding, player, devil's advocate | Everyone sees the gas in sight and gets a one-round preview. Sounding buys longer forecasts and hidden sources; Wits widens exploration reading |
| 3 | **Presentation.** A faint tint cannot be read on the fixed camera; the art rules (no glow, no tint, muted palette) fight it; flames show three states against five layers | UX, marketing, onboarding, engineering, level | Draw a surface with a hard edge and contour lines at standing, crouched and prone head heights; a tide-line on bodies; treat the overlay as interface, exempt from the art bans |
| 4 | **Accessibility is absent.** Insect silence cannot be captioned; depth relies on colour; two real-time clocks have no pause or scale | UX, onboarding | A visual twin for every sound; pattern-based depth; numeric depth on tiles; clock options. Add an accessibility section |
| 5 | **Combat numbers make gas decorative.** Breath lasts 5-7 turns in fights of 3-5 rounds; bottled still cannot submerge a standing target; the hook-pole is weaker than shooting; only two enemy types use gas; gasping damage kills small creatures before they pass out | Tactics, audit, player | Shorter hold with pressure from the first turn under (AP loss, not a hard clock); bottled still deep enough to matter; pull knocks prone; enemies have breath and use gas on default difficulty; no damage while gasping |
| 6 | **Day is safe and waiting is free.** Nothing forces or rewards night, so most still content can be skipped at noon; the dusk bell is a curfew (about 2 real minutes' warning) | Player, level, tactics, story | Night-only content and rewards; hazards that ignore the clock (pulsing vents, cellars, dead-calm days); a longer, graduated dusk |
| 7 | **Full live simulation everywhere is poor value.** Outdoors the gas is effectively static per time of day; live flow only shows in enclosed spaces and fights | Devil's advocate, level, engineering | Two tiers: computed or baked levels outdoors by hour, act and wind; live round-by-round flow in contained volumes and combat |
| 8 | **Underspecified rules.** No flow rule, flow speed, conservation, time model, breath recovery, companion breathing, or rule for a knocked-out player | Audit, engineering, level | Write the rules before any prototype (engineering proposed a concrete model) |
| 9 | **Tallow as fuel is busywork** | Player, audit | The staff burns freely; the cost of light is being seen |

## 4. Findings from single lenses

**Science**
- Flames go out at roughly 15-20% CO2, well above the level that drops people. A flame reads "lethal", not
  "dangerous". Add earlier tells: limewater clouding (lime is already the economy), a caged bird, headache.
- Sail-driven air-mills stall on exactly the calm nights that matter. Use treadle, water or vent pressure.
- A leaking store loses pressure, so "still pressurising" needs a deep natural source or failing wells.
- "Masks do not help" should become "filters do not help"; a lime-burning culture would invent lime scrubbers.
- CO2 does not burn: the Lung's engines must run on vent pressure, not combustion.
- Rescue is too cheap: real rescuers die going in. Pulling someone out should need a rope or hook.
- Unused real detail: the crater lakes as Nyos-style eruption risks; the basin's lowest rim as the spill height.

**Prior art**
- Closest work: the 2018 French film *Dans la brume* (heavy mist fills Paris; survivors live on upper floors;
  the safe height shrinks). High overlap on premise and image, low on everything else.
- An unreleased colony sim, *Above: Colonies of the Mist*, shares the pitch and the first word of our title.
- Steer: never say "mist" or "fog"; lead with flames, silence, the ledger and the Lift Towns.
- Apparently unclaimed: flame and insect-silence read-out, gas in height layers with posture in a tactics game,
  carbon-storage failure as cause, matched clay tally tokens backed by the hazard's cure.

**Story**
- Debt and gas are two stories side by side. Fix: make the strongbox the legal standing to consent to venting.
- The High Vent reads as the correct answer. Fix: it creates a permanent maintenance duty; no ending clears the debt.
- Gravity versus play: a nation suffocated in its sleep, yet gas is sold as a combat trick.
- The player never faces a present-day loss. Fix: one night where sleepers are in the still and you choose whom to carry.
- Climate reading: put the Keeping's sin in the promise of permanence, not the technology.

**Level design and engineering**
- Every space has roughly 30-50 gas states to test; the plan had no level designer.
- Authoring rules needed: an exit within minimum breath from every tile; clear spawn and rest tiles; a rule for waking after a knock-out.
- The 30 person-month cap is over half the v0.1 programming budget. Scope is now flexible, so this is a staffing note.
- Smallest useful prototype: about 8 person-weeks, one 60 x 60 map, with stated pass marks.

**Marketing**
- Lead with "heavy air that floods the night"; keep "carbon dioxide" as a reveal.
- The staff's three flames are the logo, the HUD and the store image.
- "Above the Line" is memorable but generic and needs a tagline.

## 5. The test everyone converged on

Four reviewers independently proposed the same experiment for the prototype: play the same encounters with live
flow and with scripted or static gas, blind. If players cannot tell the difference, or never change a plan because
of where the gas will be next round, the live flow is not earning its cost.

## 6. Decisions owed by the owner

1. Simulation shape: full live flow everywhere, two tiers, or authored zones only.
2. Night: optional curfew as written, or made worth entering with day no longer fully safe.
3. Tone: whether using the gas as a weapon sits comfortably beside the premise's gravity.
4. Tone: whether the debt can ever be paid down, or only passed on.
