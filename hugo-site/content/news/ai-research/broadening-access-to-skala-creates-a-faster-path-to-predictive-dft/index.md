---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-19T02:48:46.344522+00:00'
exported_at: '2026-09-19T02:48:54.817837+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft
structured_data:
  about: []
  author: ''
  description: Skala 1.1, the updated deep-learning exchange-correlation functional
    from Microsoft Research, provides greater accuracy, expanded accessibility across
    the computational chemistry ecosystem, and a living benchmark to track computational
    performance.
  headline: Broadening access to Skala creates a faster path to predictive DFT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Broadening access to Skala creates a faster path to predictive DFT
updated_at: '2026-09-19T02:48:46.344522+00:00'
url_hash: ed976920bb9831e6f4445c801b56921046c574ca
---

![Schematic of the Skala architecture, showing how meta-GGA electronic features are transformed through point-wise processing and non-local atomic interactions to predict density functional theory energies.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Skala-BlogHeroFeature-1400x788-1-1.jpg)

## At a glance

* Skala 1.1 demonstrates the continuously improving nature of Microsoft Research’s deep-learning DFT approach: trained on 2.5× more data than its predecessor, it delivers substantially higher accuracy across key molecular simulation challenges, including thermochemistry, reaction kinetics, and molecular structure prediction.
* Skala is now available in
  **CP2K**
  and is being integrated into
  **Psi4**
  ,
  **FHI-aims**
  ,
  **ORCA**
  and
  **VASP**
  , bringing next-generation DFT accuracy closer to the communities that rely on these codes every day.
* Microsoft Research is also introducing a living benchmark that will track the computational performance of successive, increasingly optimized Skala releases to help the community measure and accelerate progress toward ever greater accuracy and efficiency.
* Together, these developments mark another milestone toward a future in which computational chemistry simulations are both predictive and integrated in all relevant scientific and industrial workflows.

**Bringing density functional theory (DFT) to predictive accuracy is a journey, not a single breakthrough.**
Since
[introducing Skala](https://www.microsoft.com/en-us/research/blog/breaking-bonds-breaking-ground-advancing-the-accuracy-of-computational-chemistry-with-deep-learning/)
, our deep-learning exchange-correlation functional, we have continued to advance along two complementary fronts: improving accuracy and expanding accessibility across the computational chemistry ecosystem.

![Fig. 1: Table of errors for Skala-1.1 and competing density functionals on the 55 subsets of GMTKN55. Skala-1.1 delivers the lowest error on 32 subsets, indicating broad and consistent accuracy across a wide range of chemical properties and reaction types.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/fig1-blog_SKALA1.1-scaled.png)


Figure 1: Accuracy of Skala-1.1 for thermochemistry, kinetics, and non-covalent interactions. At the computational cost of a meta-GGA functional, Skala 1.1 outperforms the best, most expensive global hybrid functionals, ranking first (earning gold medals) in 32 of the 55 categories of the widely used GMTKN55 benchmark, which spans a broad range of chemical problems.

On the accuracy front, the
[release of
**Skala-1.1**

(opens in new tab)](https://arxiv.org/abs/2506.14665)
provides the first demonstration of the continuous-improvement paradigm underlying Skala. Trained on 2.5x more data than the first public version of Skala, the updated  model delivers substantially improved performance across key challenges in molecular simulation, including main-group thermochemistry, reaction kinetics, and molecular structure prediction.

But accuracy alone is not enough. DFT is the computational engine behind a vast range of scientific and industrial workflows, spanning chemistry, materials science, catalysis, energy technologies, and drug discovery. To have real-world impact, advanced functionals must be accessible where scientists already perform their calculations. That is why we are also expanding the Skala ecosystem through collaborations with leading electronic-structure software developers.

Today, we are announcing that Skala is available in
**CP2K**
and is being integrated into
**Psi4**
,
**FHI-aims**
,
**ORCA**
and
**VASP**
,  bringing next-generation DFT accuracy closer to the communities that rely on these codes every day. Alongside these integration efforts, we are introducing a living benchmark that tracks the computational performance of successive, increasingly optimized Skala releases. By providing a transparent and continuously updated reference for implementations across software packages and hardware platforms, this resource will help the community measure and accelerate progress toward ever greater accuracy and efficiency.

Together, these developments mark another milestone toward a future in which computational chemistry simulations are both predictive and accessible across a broader range of relevant scientific and industrial workflows.

Want to learn more about Skala and why DFT plays such an important role in in-silico discovery? Read also
[our first blog post
(opens in new tab)](https://aka.ms/skaladft/blog)
.

## Skala as a continuously improving functional

Unlike the traditional “functional zoo”, where new functionals accumulate without replacing older ones, Skala follows a different philosophy: each release is designed to supersede the previous one. As new data, model architectures, and training strategies become available, the model improves while maintaining the same practical computational cost.

**Skala-1.1**
is the latest demonstration of this approach. It achieves a weighted average error of
**2.8 kcal/mol on GMTKN55**
, a widely used benchmark suite comprising 55 categories of chemistry, including thermochemistry, reaction barriers, and noncovalent interactions. This level of accuracy surpasses today’s leading global (range-separated) hybrid functionals while retaining the efficiency of a semi-local functional. Beyond energies, Skala-1.1 also provides highly accurate electron densities, dipole moments, and molecular geometries.

These advances were enabled by major expansions of the
**[Microsoft Research Accurate Chemistry Collection
(opens in new tab)](https://www.nature.com/articles/s41597-026-07200-8)
(MSR-ACC)**
, our large-scale collection of high-accuracy quantum-chemistry reference data generated with expensive wavefunction methods. For Skala-1.1, we added new categories, including electron affinities and noncovalent clusters, increasing both the size and, crucially, the diversity of the training data. This data-driven approach allows Skala to improve systematically with each generation, moving us closer to a truly scalable and predictive DFT framework.

## Available where scientists work

To fully realize the potential of Skala’s continuously evolving approach to DFT, we need dedicated infrastructure that allows new releases to be rapidly and seamlessly integrated into the major software packages used by scientists in industry and academia. In turn, this will establish the fast feedback loop essential for accelerating Skala’s ongoing development.

We first made Skala available through our
[open-source community release
(opens in new tab)](https://github.com/microsoft/skala)
, built on (GPU4)
[PySCF
(opens in new tab)](https://pyscf.org/)
and
[integrated with ASE
(opens in new tab)](https://aka.ms/SkalaDFT/ASE)
. This enables researchers to evaluate and apply Skala with minimal effort while benefiting from highly optimized CPU and GPU performance.

But no single software package can meet the needs of every application or research community. Computational chemistry and materials science rely on a rich ecosystem of electronic-structure codes, each shaped over decades to tackle specific scientific and industrial challenges. Bringing Skala to this broader ecosystem has therefore been a major focus of the past year. We are fortunate to build on the remarkable foundations created by the DFT community and grateful to the many researchers and developers who are helping to make Skala available within the software platforms that scientists use every day.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

In collaboration with the team of Prof. Thomas D. Kühne at the
[Center for Advanced Systems Understanding (CASUS)
(opens in new tab)](https://casus.science)
, Skala has been successfully integrated into the open-source
[CP2K
(opens in new tab)](https://www.cp2k.org/)
package. With more than 25 years of development, CP2K is a powerhouse for DFT simulations, particularly for large-scale systems and long-timescale molecular dynamics, while also providing a rich portfolio of high-accuracy electronic-structure methods. Skala expands the frontiers of what is possible within CP2K, delivering a step change in DFT accuracy while preserving the computational efficiency needed for simulations at scale. We are excited to see how CP2K’s scale and versatility, combined with Skala’s continuously improving accuracy, will enable new scientific applications and discoveries in the years ahead.

There is more to come. Together with its vibrant developer’s community , we are actively integrating Skala into the open-source
[Psi4
(opens in new tab)](https://psicode.org/)
package, an essential platform for molecular electronic-structure research. Combined with the PySCF-based Skala Community Edition, this will make Skala available in three widely used open-source quantum chemistry packages.

Beyond open-source software, we are working closely with leading developers behind
[FHI-aims
(opens in new tab)](https://www.fhi-aims.org/)
,
[ORCA
(opens in new tab)](https://www.faccts.de/orca/)
, and
[VASP
(opens in new tab)](https://vasp.at/)
, with the goal of making Skala broadly accessible across the major software platforms used in computational chemistry and materials science.

## Validating accuracy across implementations: CP2K as case study

Thorough testing is essential for any new implementation. We want to ensure that Skala delivers consistent accuracy across different codes and computational settings. Together with the CP2K team, we developed a comprehensive suite of integration tests to verify that Skala produces numerically correct and reliable results. We are particularly grateful to the CASUS team, whose deep expertise in the numerical verification of computational methods was instrumental in designing and validating this testing framework.

![Fig. 2: Plot comparing signed errors for Skala-1.1 using the CP2K and PySCF implementations on a representative subset of GMTKN55. The two implementations show nearly identical results, agreeing within 0.04 kcal/mol and confirming that the CP2K integration reproduces the accuracy of the community release.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/cp2k_vs_pyscf_error-3_SKALA.png)


Figure 2: Signed errors relative to high-accuracy reference values for a representative subset of GMTKN55, comparing the CP2K and PySCF implementations of Skala-1.1 using as closely matched numerical settings as possible. The two implementations agree to within 0.1 kcal/mol MAD across the entire subset.

A detailed discussion of the implementation, validation strategy, and testing infrastructure for Skala in CP2K can be found in our joint paper with the CASUS team: “
[Molecular Implementation of the Machine-Learned Skala Exchange-Correlation Functional in CP2K through GauXC](https://www.microsoft.com/en-us/research/publication/molecular-implementation-of-the-machine-learned-skalaexchange-correlation-functional-in-cp2k-through-gauxc/)
.”

## A living performance report for Skala

Accuracy and broad availability only translate into scientific impact if Skala is also fast. Today, Skala can deliver performance comparable to semi-local meta-GGAs on both CPU’s (with an overhead that disappears for molecules with more than 20-30 atoms) and GPUs, and we are committed to preserving that efficiency as it is integrated across the electronic-structure software ecosystem.

But performance is not a fixed property. New Skala releases, improvements in libraries such as GauXC, and hardware-specific optimizations continuously improve efficiency and reveal new opportunities for further gains. Capturing this progress requires more than a single benchmark snapshot.

To provide a transparent and up-to-date view of Skala’s performance, we are publishing a
[benchmarking harness together with a living performance report
(opens in new tab)](https://aka.ms/SkalaDFT/timing)
that will be updated as new optimizations become available. This report tracks performance across a range of tasks and hardware platforms, while the harness enables package developers to benchmark, validate, and improve their own Skala implementations.

![Fig. 3 (figure attached): Benchmark of the computational cost of Skala-1.1 relative to r2SCAN, B3LYP, and M06-2X on GPUs and CPUs. Skala-1.1 achieves performance comparable to r2SCAN on GPUs and approaches semilocal-functional cost on CPUs for larger systems, while remaining significantly less expensive than hybrid functionals.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/fig3_SKALA1.1.png)


Figure 3: Computational cost of Skala on GPU and CPU, compared with a popular metaGGA functional (r2SCAN) and two hybrid functionals (B3LYP and M06-2X). On GPU, Skala 1.1 has the same cost as r2SCAN, and the hybrid functionals become more expensive for systems with more than ~1000 orbitals. On CPU, Skala has an overhead with respect to the other functionals for smaller systems, that disappears for systems with more than ~300 orbitals.

## Acknowledgments

Skala is the product of a truly collaborative effort across AI for Science, and we thank our engineering, project management, and business operations teams for making this work possible. We also thank MSR Accelerator for their partnership in advancing data generation efforts and accelerating software integrations that help bring Skala to the broader scientific community.

Opens in a new tab