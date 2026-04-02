---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:59:15.970630+00:00'
exported_at: '2026-04-02T04:59:19.846619+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/augmenting-citizen-science-computer-vision-fish-monitoring-0325
structured_data:
  about: []
  author: ''
  description: Monitoring river herring migration is essential for conservation and
    fisheries management. Researchers have now demonstrated a method using video and
    computer vision to supplement traditional methods and volunteer-based programs.
  headline: Augmenting citizen science with computer vision for fish monitoring
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/augmenting-citizen-science-computer-vision-fish-monitoring-0325
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Augmenting citizen science with computer vision for fish monitoring
updated_at: '2026-04-02T04:59:15.970630+00:00'
url_hash: 400b1558ffcee656d57c6c18ad4e7afc455372f4
---

Each spring, river herring populations migrate from Massachusetts coastal waters to begin their annual journey up rivers and streams to freshwater spawning habitat. River herring have faced severe population declines over the past several decades, and their migration is extensively monitored across the region, primarily through traditional visual counting and volunteer-based programs.

Monitoring fish movement and understanding population dynamics are essential for informing conservation efforts and supporting fisheries management. With the annual herring run getting underway this month, researchers and resource managers once again take on the challenge of counting and estimating the migrating fish population as accurately as possible.

A team of researchers from the Woodwell Climate Research Center, MIT Sea Grant, the MIT Computer Science and Artificial Intelligence Lab (CSAIL), MIT Lincoln Laboratory, and Intuit explored a new monitoring method using underwater video and computer vision to supplement citizen science efforts. The researchers — Zhongqi Chen and Linda Deegan from the Woodwell Climate Research Center, Robert Vincent and Kevin Bennett from MIT Sea Grant, Sara Beery and Timm Haucke from MIT CSAIL, Austin Powell from Intuit, and Lydia Zuehsow from MIT Lincoln Laboratory — published a paper describing this work in the journal
*Remote Sensing in Ecology and Conservation*
this February.

The open-access paper, “
[From snapshots to continuous estimates: Augmenting citizen science with computer vision for fish monitoring](https://zslpublications.onlinelibrary.wiley.com/doi/10.1002/rse2.70055)
,” outlines how recent advancements in computer vision and deep learning, from object detection and tracking to species classification, offer promising real-world solutions for automating fish counting with improved efficiency and data quality.

Traditional monitoring methods are constrained by time, environmental conditions, and labor intensity. Volunteer visual counts are limited to brief daytime sampling windows, missing nighttime movement and short migration pulses, when hundreds of fish pass by within the span of a few minutes. While technologies like passive acoustic monitoring and imaging sonar have advanced continuous fish monitoring under certain conditions, the most promising and low-cost option — manual review of underwater video — is still labor-intensive and time-consuming. With the growing demand for automated video processing solutions, this study presents a scalable, cost-effective, and efficient deep learning-based system for reliable automated fish monitoring.

The team built an end-to-end pipeline — from in-field underwater cameras to video labeling and model training — to achieve automated, computer vision-powered fish counting. Videos were collected from three rivers in Massachusetts: the Coonamessett River in Falmouth, the Ipswich River (Ipswich), and the Santuit River in Mashpee.

To prepare the training dataset, the team selected video clips with variations in lighting, water clarity, fish species and density, time of day, and season to ensure that the computer vision model would work reliably across diverse real-world scenarios. They used an open-source web platform to manually label the videos frame-by-frame with bounding boxes to track fish movement. In total, they labeled 1,435 video clips and annotated 59,850 frames.

The researchers compared and validated the computer vision counts with human video reviews, stream-side visual counts, and data from passive integrated transponder (PIT) tagging. They concluded that models trained on diverse multi-site and multi-year data performed best and produced season-long, high-resolution counts consistent with traditionally established estimates. Going one step further, the system provided insights into migration behavior, timing, and movement patterns linked to environmental factors. Using video from the 2024 Coonamesset River migration, the system counted 42,510 river herring and revealed that upstream migration peaked at dawn, while downstream migration was largely nocturnal, with fish utilizing darker, quieter periods to avoid predators.

With this real-world application, the researchers aim to advance computer vision in fisheries management and provide a framework and best practices for integrating the technology into conservation efforts for a wide range of aquatic species. “MIT Sea Grant has been funding work on this topic for some time now, and this excellent work by Zhongqi Chen and colleagues will advance fisheries monitoring capabilities and improve fish population assessments for fisheries managers and conservation groups,” Vincent says. “It will also provide education and training for students, the public, and citizen science groups in support of the ecologically and culturally important river herring populations along our coasts.”

Still, continued traditional monitoring is essential for maintaining consistency in long-term datasets until fisheries management agencies fully implement automated counting systems. Even then, computer vision and citizen science should be seen as complementary. Volunteers will be necessary for camera maintenance and for contributing directly to the computer vision workflow, from video annotation to model verification. The researchers envision that integrating citizen observations and computer vision-generated data will help create a more comprehensive and holistic approach to environmental monitoring.

This work was funded by MIT Sea Grant, with additional support provided by the Northeast Climate Adaptation Science Center, an MIT Abdul Latif Jameel Water and Food Systems seed grant, the AI and Biodiversity Change Global Center (supported by the National Science Foundation and the Natural Sciences and Engineering Research Council of Canada), and the MIT Undergraduate Research Opportunities Program.