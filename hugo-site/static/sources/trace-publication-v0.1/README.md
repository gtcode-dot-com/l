# TRACE publication sources

**Version:** 0.1 · **Date:** 15 November 2026 · **Byline:** GTCode.com.

This package describes an unvalidated conceptual research proposal. No TRACE implementation, experiment, registered protocol, peer review or demonstrated superiority is claimed.

## Public text and downloads

- [Research paper](https://gtcode.com/papers/trace/)
- [Illustrated overview](https://gtcode.com/guides/trace/overview/)
- [Proposed evaluation](https://gtcode.com/guides/trace/evaluation/)
- [Compiled PDF](https://gtcode.com/papers/trace/trace-research-proposal.pdf)
- [Portable manuscript source ZIP](https://gtcode.com/papers/trace/trace-latex-source.zip)
- [Proposed protocol YAML](https://gtcode.com/papers/trace/proposed-evaluation-protocol.yaml)
- [Annotated reference registry](https://gtcode.com/papers/trace/references.json)
- [Bibliography](https://gtcode.com/papers/trace/references.bib)
- [Self-citation](https://gtcode.com/papers/trace/trace-citation.bib)

`latex/manuscript.md` is the shared scientific text. `render_manuscript.py` renders it into `main.tex` using `template.tex`; in a site checkout its `--hugo` option also produces the complete web paper, including linked references and matching figure captions. `--check --hugo` verifies text parity without writing. See the manuscript README for dependencies and exact commands. The PDF build uses supplied vector figures and needs no network access.

All three figures are included as editable SVG and vector PDF, with a Matplotlib generation script. No raster image masters or generated review screenshots are distributed. The figures use publication typography and palette conventions from figures4papers; they plot no empirical data.

`SOURCE_AND_CLAIM_AUDIT.md` records source depth and the proposal's evidential limits. `PUBLICATION_MANIFEST.json` inventories the current files. `SHA256SUMS.txt` hashes those files relative to the repository root, excluding itself and unrelated shared site files. `VALIDATION_REPORT.md` describes production checks only; it is not scientific validation.

The original research input was a five-document TRACE packet. Its staffing assumptions and original comparator/count arithmetic are not current study commitments. The current proposed protocol and manuscript govern the published design, with feasibility and statistical freeze decisions explicitly outstanding. No third-party source paper or dataset is redistributed. No new blanket content license has been supplied; source is offered for inspection and document reproduction, not as a transfer of third-party rights.

The cross-case interchange schema is `trace-records.schema.json` in the LaTeX source directory and public paper downloads. Sections 4.1–4.6 specify its semantic requirements and the generator, compiler, acquisition and adjudication stages. The schema is a proposed interface, not an implemented scientific engine.

The prior-art audit and contribution matrix are included as prior-art-audit.md and contribution-matrix.md in the portable source. The protocol prioritizes H2 with development cases and an exploratory pilot; H1 supplies quality measures and H3 is conditional subsequent work. Named comparator adaptations require implementation-fidelity review before experiments.
