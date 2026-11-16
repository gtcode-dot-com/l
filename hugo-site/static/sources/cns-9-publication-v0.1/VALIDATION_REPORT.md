# CNS 9.0 v0.1 — publication validation

**Date:** 15 November 2026. **Scope:** publication text, files, reproducibility, rendering and integrity. This is not empirical validation of CNS 9.0. No scientific model evaluation, registered study or deployment was performed.

## Content and consistency

The full research paper, illustrated overview and proposed evaluation are supplied as Hugo Markdown. The paper's scientific text is shared with LaTeX through `latex/manuscript.md`, `template.tex` and `render_manuscript.py`; source parity is checked without rewriting. The registry has 54 unique reference records; all 38 paper citations resolve to records, BibTeX entries and linked web bibliography anchors. BibTeX titles preserve capitalization. Source review depths and scientific nonclaims are recorded in the audit.

Protocol checks independently reconcile the ten-system planning grid (96,000 system-root runs, 1,056,000 static branches, 96,000 adaptive branches), 3,840 research roots, 1,200/600/600 provisional classes, token ceilings, and 17,280 prospective executions. All counts are conditional planning targets, with target/view and stratum feasibility pending. Required H2 comparator candidates, acquisition constraints, candidate inadequacy, absolute safeguards and pending statistical choices agree across text and YAML. The exact-binomial illustration is checked: at n=600, 20 failures meet the stated one-sided Clopper–Pearson criterion; 21 do not.

## PDF and source archive

The compiled PDF has **17 pages**, with selectable text and embedded Pagella/Heros/Cursor fonts and matching mathematics. The abstract is full-width and flush left; its first-line position matches the body left edge. Uniform monospace identifiers break without added hyphens, and the algorithm is kept together.

LuaLaTeX/latexmk compilation succeeds without unresolved citations, missing glyphs or overfull boxes. Final pages were rendered and visually reviewed in contact sheets, with additional full-size checks of the opening, warrant and algorithm/figure pages. Text-bound checks cover every page. All three figures are vector/text output, with no embedded raster images.

The standalone source ZIP is safely extracted into a clean temporary directory. Its shared-source renderer passes the parity check and the manuscript rebuilds offline with installed dependencies; the result has the same page count and extracted text as the published PDF. Archive paths, CRC integrity and file agreement with unpacked manuscript sources are checked. No dependency cache, TeX build output or original third-party paper is distributed.

## Figures and site

All three SVGs parse, retain editable text and have accessible title/description linkage; no embedded scripts or raster images are present. SVG/PDF copies in the public asset and manuscript-source locations match. The caching rivals use symmetric visual treatment with a shared merge connector. The discovery figure labels the one-way commitment path into sealed evaluation; hidden outcomes never flow into runtime.

The full Hugo production build succeeds. Chromium checks at 390px and 1440px cover the CNS landing, overview, evaluation and paper: figures load, no JavaScript or KaTeX errors occur, and there is no horizontal page overflow. The paper renders 43 math expressions and the evaluation seven. Local main-content links, asset paths and fragment targets resolve. Existing homepage metadata and Korean-dossier regression checks pass.

`PUBLICATION_MANIFEST.json` lists current publication files; `SHA256SUMS.txt` hashes that inventory except itself. Final checks verify inventory coverage and every digest. The publication remains the unpublished v0.1 proposal, with no claim of preregistration, peer review, empirical superiority or scientific readiness for execution.
