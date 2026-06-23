---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-23T04:00:28.654802+00:00'
exported_at: '2026-06-23T04:00:31.527587+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ai-for-science-software-cuda
structured_data:
  about: []
  author: ''
  description: NVIDIA CUDA-X libraries, microservices and reference code accelerate
    AI for science.
  headline: From Materials Simulation to Experimental Astronomy, New NVIDIA AI Software
    Unlocks Scientific Discoveries
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ai-for-science-software-cuda
  publisher:
    logo: /favicon.ico
    name: GTCode
title: From Materials Simulation to Experimental Astronomy, New NVIDIA AI Software
  Unlocks Scientific Discoveries
updated_at: '2026-06-23T04:00:28.654802+00:00'
url_hash: 71966ba95af1445456b8bd5a973338b7a6c21e72
---

At the ISC conference running in Hamburg this week, NVIDIA is introducing new software that speeds AI for science, from chemistry and materials discovery to the search for dark matter.

The NVIDIA DAQIRI library and new NVIDIA ALCHEMI NIM microservices — as well as the NVIDIA cuPhoton reference code, coming soon — turn work that once took hours or days on CPUs into real-time, GPU-accelerated pipelines.

They’re a part of
[NVIDIA CUDA-X](https://www.nvidia.com/en-us/technologies/cuda-x/)

, a collection of tools and libraries that deliver dramatically higher performance across application domains, including AI and high-performance computing.

These performance gains are large and have real impact. Across disciplines, scientists are using AI and accelerated computing to generate data and insights with instruments and surveys faster than ever.

For example, running on NVIDIA GB200 NVL72 systems, cuPhoton speeds loading, reading, processing and analysis of FITS data — the standard astronomical file format — from observatories and telescopes. In early access, cuPhoton accelerated loading and reading of FITS images collected by the

Rubin Observatory’s

Legacy Survey of Space and Time (LSST) by 14,900x. It also enabled up to 8,400x faster signal processing and analysis using 32 NVIDIA Grace Blackwell superchips.

Ultimately, this means faster insights from the LSST camera — the
[largest digital camera ever built](https://rubinobservatory.org/explore/how-rubin-works/technology/camera)

— which captures images of billions of far-away galaxies, as well as closer, faint objects that don’t reflect much light.

VIDEO

## **New Software, From the Lab Bench to the Telescope**

The new software accelerates research on dark matter, materials simulation and more.

**NVIDIA cuPhoton**

is a reference code for scientists looking to extract insights from multidimensional data collected from telescopes, X-rays and laser experiments. It’s built to load, process, analyze and visualize petabytes of data, and can be used alongside other NVIDIA CUDA-X technologies to build an end-to-end accelerated pipeline for work in fields including astrophysics and astronomy.

Researchers at

Princeton University

collaborated with NVIDIA to develop cuPhoton and will use it — along with

Harvard University

— for processing and analysis of massive data collected from observatories and  dark energy surveys.

[**NVIDIA DAQIRI**](https://github.com/NVIDIA/daqiri)

— short for Data Acquisition for Integrated Real-time Instruments — is a high-performance networking library that streams data from fast detectors and sensors into NVIDIA software. Older systems are tied to fixed hardware and can drop data when instruments produce it faster than they can save it. DAQIRI keeps up by handling the stream as it arrives.

A research project called A-GHOST was developed by scientists from

CERN

, the University of Chicago and University College London, in the framework of

CERN

openlab. It uses DAQIRI to run AI in real time on collision data recorded by the ATLAS Experiment at CERN. A-GHOST analyses data that  would normally be rejected by ATLAS  — over 99% of it, due to storage constraints — allowing it to catch potentially interesting signals that would otherwise be lost.

[**NVIDIA ALCHEMI**](https://developer.nvidia.com/cuda/cuda-x-libraries/alchemi)

comprises a collection of domain-specific microservices and a toolkit for accelerating chemical and materials discovery, with applications across battery materials, catalysts, OLED displays, beauty products and more.

NVIDIA released in March two ALCHEMI NIM microservices for
[batched geometry relaxation](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/alchemi-bgr?version=1.0.0)

(BGR) and
[batched molecular dynamics](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/alchemi-bmd?version=1.0.0)

(BMD). These AI-accelerated tools let researchers simulate millions of molecules and materials at once: BGR to find their most stable structures, BMD to simulate how they move over time.

In addition, ALCHEMI is expected to soon include a microservice for the widely used Vienna Ab initio Simulation Package (VASP), enabling researchers to run materials simulations with higher GPU throughput. By running multiple VASP calculations on a single GPU with the
[NVIDIA Multi-Process Service](https://docs.nvidia.com/deploy/mps/latest/index.html)

, the microservice achieves a 3x speedup for geometry optimization — the process of finding the most stable arrangement of atoms in a material.

Plus, developers and researchers can use the
[ALCHEMI Toolkit](https://github.com/NVIDIA/nvalchemi-toolkit)

to accelerate training of AI surrogate models called machine learning interatomic potentials and easily build custom, high-performance atomistic simulation workflows.

## **How Lila Sciences Runs the Scientific Method Nonstop With NVIDIA ALCHEMI**

Lila Sciences

— which is building a scientific superintelligence platform and autonomous lab for life sciences, chemistry and materials science — collaborated with NVIDIA on a high-fidelity magnet simulation using ALCHEMI, demoed at NVIDIA GTC San Jose in March.

Lila Sciences accelerated high-throughput materials screening by 50x using the ALCHEMI NIM microservice for BGR, identifying stable candidates that have higher chances of being synthesized. It then accelerated the calculation of magnetic properties by 30% for shortlisted candidates using the ALCHEMI VASP microservice in early access.

![](https://blogs.nvidia.com/wp-content/uploads/2026/06/lila-image.png)


Lila Sciences conducts materials simulation with NVIDIA ALCHEMI. The image above, courtesy of Lila Sciences, depicts film coupons cut out from a sample synthesized in a sputterer, a system for creating ultrathin, highly uniform coatings of metals or ceramics onto a surface.

The speedups compound. ALCHEMI’s specialized kernels for TensorNet gave Lila a 6x speedup in training and inference and reduced memory usage by 3x, enabling simulations that previously took weeks in just days.

Instead of running one experiment at a time, this approach evaluates multiple materials simultaneously in GPU memory and can be generalized for use cases spanning:

* Materials discovery — screening novel, stable compositions at scale
* Energy — discovering active, earth-abundant catalysts for producing chemicals and fuels
* Electromagnetics — understanding and predicting complex magnetic behaviors

ALCHEMI sits at the simulation layer, generating the physical-science data that feeds the rest of the loop.

In addition, Lila Sciences accelerates scientific discovery with the full NVIDIA stack, using
[NVIDIA Megatron-LM](https://github.com/nvidia/megatron-lm)

and
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

for training — including the Nemotron 3 Nano and Nemotron 3 Super open models, as well as the NeMo RL and NeMo Gym libraries. The company also taps into
[NVIDIA BioNeMo](https://www.nvidia.com/en-us/industries/healthcare-life-sciences/)

for molecular generation,
[NVIDIA Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)

and
[NIM](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)

microservices for inference serving, and
[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)

libraries for
[digital twins](https://www.nvidia.com/en-us/glossary/digital-twin/)

.

“The work showcases using a powerful computing stack assembled to accelerate discovery at a scale no individual scientist could achieve alone,” said Andy Beam, cofounder and chief technology officer of Lila Sciences.

## **Availability**

The NVIDIA ALCHEMI
[Toolkit](https://github.com/NVIDIA/nvalchemi-toolkit)

and
[Toolkit-Ops](https://github.com/NVIDIA/nvalchemi-toolkit-ops)

are available for download from Github and PyPI. ALCHEMI NIM microservices are available for download from the
[NVIDIA NGC](https://catalog.ngc.nvidia.com/)

catalog. The ALCHEMI NIM microservice for VASP is expected to be available later this summer.

DAQIRI is now available on
[GitHub](https://github.com/NVIDIA/daqiri)

. CuPhoton is expected to be available this summer.

*Learn more about*
[*NVIDIA AI for science*](https://blogs.nvidia.com/blog/tag/science/)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*