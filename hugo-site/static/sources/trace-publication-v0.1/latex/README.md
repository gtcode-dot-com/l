# TRACE v0.1 manuscript source

Full source for **TRACE: Contrast-Guided Discovery from Conflicting Accounts**, GTCode.com, 15 November 2026. Unvalidated conceptual proposal; no scientific experiment is reported.

## Build the PDF

Install LuaLaTeX, latexmk, BibTeX or bibtex8, and standard TeX Live packages including `fontspec`, `unicode-math`, `microtype`, `amsmath`, `mathtools`, `titlesec`, `fvextra`, `needspace`, `xcolor`, `natbib`, `hyperref`, `graphicx`, `booktabs` and `fancyhdr`. Fonts are TeX Gyre Pagella, Pagella Math, Heros and Cursor. The build performs no network requests once dependencies are installed.

```sh
sh build.sh
```

The output is `main.pdf`. The source ZIP contains pre-generated `main.tex` and vector figure PDFs, so normal compilation does not require Python, Pandoc or Matplotlib.

## Edit the scientific text

`manuscript.md` is the authoritative scientific text. `template.tex` controls title/abstract layout, fonts, headings, captions and page furniture. With Python 3 and Pandoc installed:

```sh
python3 render_manuscript.py
sh build.sh
```

In the complete Hugo checkout, `python3 render_manuscript.py --hugo` also updates the web paper using its existing front matter and the annotated reference registry. `python3 render_manuscript.py --hugo --check` checks both generated text files without writing. The standalone ZIP supports generation of TeX without access to the site or registry.

Inline identifiers use a uniform monospace macro with discretionary, hyphenless breaks. The abstract is full-width and flush left. The algorithm remains a single ruled block. All three figures are vector PDFs with editable SVG counterparts; `figure-source/README.md` describes optional regeneration and design provenance. `references.bib` contains the external/lineage bibliography, with protected title capitalization; `trace-citation.bib` cites the proposal.

No original Lopez-Paz TeX inputs, licensed datasets, package caches, TeX build logs or unpublished evaluation answers are bundled. No blanket redistribution license was supplied for the manuscript or third-party materials.

The cross-case interchange schema is `trace-records.schema.json` in the LaTeX source directory and public paper downloads. Sections 4.1–4.6 specify its semantic requirements and the generator, compiler, acquisition and adjudication stages. The schema is a proposed interface, not an implemented scientific engine.

The prior-art audit and contribution matrix are included as prior-art-audit.md and contribution-matrix.md in the portable source. The protocol prioritizes H2 with development cases and an exploratory pilot; H1 supplies quality measures and H3 is conditional subsequent work. Named comparator adaptations require implementation-fidelity review before experiments.
