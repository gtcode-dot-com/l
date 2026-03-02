---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-02T01:12:52.906128+00:00'
exported_at: '2026-03-02T01:12:55.582856+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/project-silicas-advances-in-glass-storage-technology
structured_data:
  about: []
  author: ''
  description: Project Silica introduces new techniques for encoding data in borosilicate
    glass, as described in the journal Nature. These advances lower media cost and
    simplify writing and reading systems while supporting 10,000-year data preservation.
  headline: Project Silica’s advances in glass storage technology
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/project-silicas-advances-in-glass-storage-technology
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Project Silica’s advances in glass storage technology
updated_at: '2026-03-02T01:12:52.906128+00:00'
url_hash: b3986ac1316c63888347ad3c67c5e408ab56ee29
---

![A blue-to-green gradient background featuring three white icons: a networked globe on the left, a cloud in the center, and a stacked database on the right.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/02/NatureSilica-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* Microsoft Research publishes breakthrough in
  *Nature*
  on glass-based data storage that could preserve information for 10,000 years.
* New technique extends technology from expensive fused silica to ordinary borosilicate glass found in kitchen cookware.
* Innovations enable faster parallel writing, simplified readers (one camera instead of three), and easier manufacturing.
* Phase voxel method requires only a single laser pulse, significantly reducing complexity and cost.

Long-term preservation of digital information has long challenged archivists and datacenters, as magnetic tapes and hard drives degrade within decades. Existing archival storage solutions have limited media lifespans that make them less than ideal for preserving information for future generations.

Now, we are excited to report significant progress on
[Project Silica
(opens in new tab)](https://unlocked.microsoft.com/sealed-in-glass/)
, our effort to encode data in glass using femtosecond lasers, a technology that could preserve information for 10,000 years. Glass is a permanent data storage material that is resistant to water, heat, and dust.

In findings published in
*[Nature
(opens in new tab)](https://www.nature.com/articles/s41586-025-10042-w)*
, we describe a breakthrough that extends the technology beyond expensive fused silica to ordinary borosilicate glass. A readily available and lower-cost medium, this is the same material found in kitchen cookware and oven doors. This advance addresses key barriers to commercialization: cost and availability of storage media. We have unlocked the science for parallel high-speed writing and developed a technique to permit accelerated aging tests on the written glass, suggesting that the data should remain intact for at least 10,000 years.

Storing data inside glass with
[femtosecond
(opens in new tab)](https://www.bing.com/search?q=femtosecond)
laser pulses is one of the few technologies on the horizon with the potential for durable, immutable, and long-lived storage. Although we have been leading innovation in
[this type of storage for years](https://www.microsoft.com/en-us/research/blog/project-silica-sustainable-cloud-archival-storage-in-glass/)
, prior to this research the technique only worked with pure fused silica glass, a type of glass that is relatively difficult to manufacture and available from only a few sources.

In the paper, we show how data can be stored in borosilicate glass. The new technique stores hundreds of layers of data in glass only 2mm thin, as with previous methods, but with important improvements. The reader for the glass now needs only one camera, not three or four, reducing cost and size. In addition, the writing devices require fewer parts, making them easier to manufacture and calibrate, and enabling them to encode data more quickly.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## Key scientific discoveries

The
*Nature*
paper details several key new scientific discoveries:

**Advances in
[birefringent voxel
(opens in new tab)](https://www.bing.com/search?q=birefringent%20voxel&qs=n&form=QBRE&sp=-1&lq=0&pq=birefringent%20voxel)
writing**
: For the previous type of data storage in fused silica glass using birefringent (i.e., polarization) voxels, we developed a technique to reduce the number of pulses used to form the voxel from many to only two, critically showing that the polarization of the first pulse is not important to the polarization of the voxel formed. We further developed this to enable pseudo-single-pulse writing, in which a single pulse can be split after its polarization is set to simultaneously form the first pulse for one voxel (where the polarization doesn’t matter) and the second pulse of another (where the set polarization is essential). We demonstrated how to use this pseudo-single-pulse writing to enable fast writing with beam scanning across the media.

**Phase voxels, a new storage method**
: We invented a new type of data storage in glass called phase voxels, in which the phase change of the glass is modified instead of its polarization, showing that only a single pulse is necessary to make a phase voxel. We demonstrated that these phase voxels can also be formed in borosilicate glass and devised a technique to read the phase information from phase voxels encoded in this material. We showed that the much higher levels of three-dimensional inter-symbol interference in phase voxels can be mitigated with a machine learning classification model.

**Parallel writing capabilities**
: By combining a mathematical model of pre-heating and post-heating within the glass with the invention of a multi-beam delivery system, we showed that many data voxels can be written in proximity in the glass at the same time, significantly increasing writing speed. We explained a method for using light emissions (a side effect of voxel formation) for both static calibration and dynamic control to fully support automatic writing operations.

**Optimization and longevity testing**
: We developed a new way to optimize symbol encodings using machine learning and a better way to understand the tradeoff between error rates, error protection, and error recovery when evaluating new digital storage systems. We also created a new
[nondestructive optical method
(opens in new tab)](https://www.bing.com/search?pglt=161&q=nondestructive+optical+method)
to identify the aging of data storage voxels within the glass, using this and standard accelerated aging techniques to support data lasting 10,000 years. We extended the industry standard Gray codes to apply to nonpower-of-two numbers of symbols.

[Skip slideshow for:](#skip-wp-block-msr-cards-1)

Previous slide



Previous slide

A piece of Project Silica media written with data.

A research-grade Writer used to set the record for high speed data writing into glass.

A research-grade Reader for retrieving data from glass.

Close up of Writer showing high-speed multi-beam data encoding on laser pulses.

End of slideshow for:

## Demonstrating the technology

As a research initiative, Project Silica has demonstrated these advances through several proofs of concept, including
[storing Warner Bros.’ “Superman” movie on quartz glass
(opens in new tab)](https://news.microsoft.com/source/features/innovation/ignite-project-silica-superman)
, partnering with
[Global Music Vault
(opens in new tab)](https://unlocked.microsoft.com/sealed-in-glass/)
to
[preserve music under ice for 10,000 years
(opens in new tab)](https://www.fastcompany.com/90757574/with-glass-buried-under-ice-microsoft-plans-to-preserve-music-for-10000-years)
, and working with students on a
[“Golden Record 2.0” project
(opens in new tab)](https://www.geekwire.com/2024/microsoft-silica-golden-record-glass/)
, a digitally curated archive of images, sounds, music, and spoken language, crowdsourced to represent and preserve humanity’s diversity for millennia.

## Looking ahead

The research phase is now complete, and we are continuing to consider learnings from Project Silica as we explore the ongoing need for sustainable, long-term preservation of digital information. We have added this paper to our
[published works](https://www.microsoft.com/en-us/research/project/project-silica/publications/)
so that others can build on them.

[Project Silica](https://www.microsoft.com/en-us/research/project/project-silica/)
has made scientific advances across multiple areas beyond laser direct writing (LDW) in glass, including archival storage systems design, archival workload analysis, datacenter robotics, erasure coding, free-space optical components, and machine learning-based methods for symbol decoding in storage systems. Many of these innovations were described in our
[ACM Transactions on Storage publication
(opens in new tab)](https://aka.ms/Silica)
in 2025.

Opens in a new tab