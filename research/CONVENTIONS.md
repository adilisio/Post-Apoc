# Research Conventions

This repo is the study phase for an **original** post-apocalyptic game. We are studying the Fallout series
(1, 2, 3, 4, New Vegas, 76) to understand what works and what doesn't. We are **not** remaking Fallout and
will not reuse its names, characters, art, music, or text. Research documents describe and analyse; they do
not copy.

## Rules for every research document

1. **Markdown, one topic per file**, in the path you were assigned. Only write inside your assigned paths.
2. **Start with a `## Quick Reference` block** — 10-25 bullets a designer can skim in a minute.
3. **Use tables** for anything enumerable (factions, stats, weapons, locations, scores, dates).
4. **Cite sources.** Every file ends with `## Sources` listing URLs actually consulted. Use multiple
   independent sources (wikis such as fallout.wiki / Nukapedia, developer interviews, GDC talks, design
   documents such as the Fallout Bible, reviews, retrospectives, forum consensus). Never rely on one source.
5. **Mark confidence.** Flag anything disputed, retconned, or semi-canon with `[DISPUTED]`, `[RETCON]`,
   `[SEMI-CANON]`, or `[UNVERIFIED]`. If you could not verify a figure, say so rather than guess.
6. **Summarise in your own words.** Short quotes (under ~25 words) with attribution are fine. Do not paste
   long passages of game text, wiki text, or reviews.
7. **No copyrighted binaries in git.** Do not download game art, screenshots, or audio into tracked folders.
   Link to them instead. `research/art/_local/` is git-ignored if a local copy is truly needed.
8. **End with `## Design Takeaways`** — what this topic teaches us for our own game: what to learn from,
   what to avoid. Keep these as concrete, opinionated bullets.
9. Depth over breadth-padding: specific numbers, formulas, names, and dates beat general prose.
10. Do not run git commands. The orchestrator commits.
