# CNS 9.0 publication sources

**Version:** 0.1 · **Date:** 15 November 2026 · **Byline:** GTCode.com.

This package describes an unvalidated conceptual research proposal. No CNS 9.0 implementation, experiment, registered protocol, peer review or demonstrated superiority is claimed.

## Public text and downloads

- [Research paper](https://gtcode.com/papers/cns-9/)
- [Illustrated overview](https://gtcode.com/guides/cns-9/overview/)
- [Proposed evaluation](https://gtcode.com/guides/cns-9/evaluation/)
- [Compiled PDF](https://gtcode.com/papers/cns-9/cns-9-research-proposal.pdf)
- [Portable manuscript source ZIP](https://gtcode.com/papers/cns-9/cns-9-latex-source.zip)
- [Proposed protocol YAML](https://gtcode.com/papers/cns-9/proposed-evaluation-protocol.yaml)
- [Annotated reference registry](https://gtcode.com/papers/cns-9/references.json)
- [Bibliography](https://gtcode.com/papers/cns-9/references.bib)
- [Self-citation](https://gtcode.com/papers/cns-9/cns-9-citation.bib)

`latex/manuscript.md` is the shared scientific text. `render_manuscript.py` renders it into `main.tex` using `template.tex`; in a site checkout its `--hugo` option also produces the complete web paper, including linked references and matching figure captions. `--check --hugo` verifies text parity without writing. See the manuscript README for dependencies and exact commands. The PDF build uses supplied vector figures and needs no network access.

All three figures are included as editable SVG and vector PDF, with a Matplotlib generation script. No raster image masters or generated review screenshots are distributed. The figures use publication typography and palette conventions from figures4papers; they plot no empirical data.

`SOURCE_AND_CLAIM_AUDIT.md` records source depth and the proposal's evidential limits. `PUBLICATION_MANIFEST.json` inventories the current files. `SHA256SUMS.txt` hashes those files relative to the repository root, excluding itself and unrelated shared site files. `VALIDATION_REPORT.md` describes production checks only; it is not scientific validation.

The original research input was a five-document CNS 9.0 packet. Its staffing assumptions and original comparator/count arithmetic are not current study commitments. The current proposed protocol and manuscript govern the published design, with feasibility and statistical freeze decisions explicitly outstanding. No third-party source paper or dataset is redistributed. No new blanket content license has been supplied; source is offered for inspection and document reproduction, not as a transfer of third-party rights.
