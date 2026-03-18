---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T22:15:39.658430+00:00'
exported_at: '2026-03-18T22:15:42.605549+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/dsx-air-simulation-ai-factories
structured_data:
  about: []
  author: ''
  description: Setting up AI factories in simulation — decreasing deployment time
    from months to days — is accelerating the next industrial revolution. Nowhere
    was that more apparent than at GTC 2026, in San Jose, where NVIDIA founder and
    CEO Jensen Huang introduced NVIDIA DSX Air. Part of NVIDIA DSX Sim in the DSX
    platform, NVIDI...
  headline: NVIDIA DSX Air Boosts Time to Token With Accelerated Simulation for AI
    Factories
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/dsx-air-simulation-ai-factories
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA DSX Air Boosts Time to Token With Accelerated Simulation for AI Factories
updated_at: '2026-03-18T22:15:39.658430+00:00'
url_hash: 04654360e3200d39d419fc8ca96367aada3a5c73
---

Setting up AI factories in simulation — decreasing deployment time from months to days — is  accelerating the next industrial revolution.

Nowhere was that more apparent than at GTC 2026, in San Jose, where NVIDIA founder and CEO Jensen Huang introduced NVIDIA DSX Air. Part of NVIDIA DSX Sim in the
[DSX platform, NVIDIA’s blueprint for AI factories](https://nvidianews.nvidia.com/news/nvidia-releases-vera-rubin-dsx-ai-factory-reference-design-and-omniverse-dsx-digital-twin-blueprint-with-broad-industry-support)
, DSX Air is a software-as-a-service platform for logically simulating AI factories. It delivers high‑fidelity digital simulations of NVIDIA hardware infrastructure, including GPUs, SuperNICs, DPUs and switches, and it integrates with leading partner solutions for storage and routing, security, orchestration and more via open, API-based connectivity.

NVIDIA DSX Air enables a complete AI factory ecosystem, uniting NVIDIA infrastructure with partner technologies to deliver full‑stack simulation and accelerate complex AI deployments.

Companies building some of the world’s most advanced AI infrastructure, including

CoreWeave

,

are already using DSX Air to simulate and validate their environments long before hardware reaches the loading dock. The development underscores a new reality: simulation is now essential to accelerating AI deployment at scale.

DSX Air allows organizations to construct a full digital twin of their AI factory — compute, networking, storage, orchestration and security — before a single server is unboxed. By shifting integration and troubleshooting into simulation, customers are reducing the time to first token from weeks or months to mere days or hours, saving enormous amounts of time and costs.

An industry analogy for this AI factory simulation phenomenon explains it well: It’s like IT mirroring your laptop to set up a new one, except the “laptop” is a hyperscale AI factory and the “mirroring” is a complete, high‑fidelity replica of the production environment.

For operators racing to bring new AI capacity online, this change is transformative.

## **Building a Platform for an Entire Ecosystem**

The NVIDIA DSX Air simulation platform is designed to support the entire AI factory ecosystem. Server manufacturers, orchestration vendors, storage providers and security partners can all validate their offerings alongside NVIDIA infrastructure — together, in one environment, at scale.

This ecosystem‑wide capability is already reshaping partner workflows.

Server manufacturers, which serve as the primary channel for enterprise inference, can now model and validate their reference architectures without building expensive physical labs. Enterprise AI environments rarely fit rigid designs, and customers often require bespoke configurations. With DSX Air, manufacturers can create digital twins tailored to specific customer needs, test their software stacks and deliver validated solutions without touching hardware.

Orchestration vendors — critical for enterprises and tier‑2 clouds that need turnkey AI services — gain the ability to test at scale. At GTC, NVIDIA showcased a multi‑tenant RTX PRO Server environment running entirely in simulation, with

Netris

providing network orchestration,

Rafay

handling host orchestration and
[NVIDIA Run:ai](https://www.nvidia.com/en-us/software/run-ai/)

optimizing GPU allocation. These partners can now validate complex workflows under realistic conditions without deploying physical clusters.

The simulation environment is also valuable for validating the data platforms that power AI factories. Instead of requiring large physical clusters, DSX Air allows ecosystem partners to model complete AI workflows alongside NVIDIA compute, networking and software infrastructure. At GTC, the booth demonstration features a video retrieval-augmented generation workload running on the

VAST

AI Operating System, including a fully operational VAST cluster with DataEngine nodes and the video search and summarization front end. DataEngine triggers and functions process and index video content through an end-to-end pipeline, illustrating how AI applications can be designed, tested and validated inside the DGX Air simulation before deploying physical infrastructure.

Security vendors — facing some of the most demanding validation requirements — can now test multi‑tenant policies, DPU‑accelerated isolation and threat detection in a realistic environment. The GTC demo includes

Check Point

’s distributed firewall running on simulated BlueField DPUs,

TrendAI Vision One

for threat detection and Keysight AI Inference Builder, an emulation and analytics platform designed to validate inference-optimized AI infrastructure at scale.

Security partners can identify vulnerabilities and validate policies in a customer’s digital twin long before production goes live.

Across the ecosystem, partners emphasized the same point: DSX Air gives them a complete, scalable and cost‑effective way to validate their solutions with NVIDIA infrastructure and with each other.

## **Operating With a New Model to Accelerate Time to Token**

NVIDIA DSX Air isn’t just a deployment accelerator — it introduces a new operational model for AI factories.

On the first day, customers build their intended production environment entirely in simulation. They configure networking, compute, storage, orchestration, security and scheduling exactly as they plan to deploy them. They validate that everything works together, identify issues early and ensure the environment behaves as expected.

Next, they can deploy with confidence. Because the environment has already been tested end to end, the probability of a smooth bring‑up increases dramatically. Time to first token shrinks, and teams can focus on running workloads rather than troubleshooting infrastructure.

Afterward and beyond, DSX Air becomes a safe environment for change management. Long‑lived simulations allow customers to test upgrades, rehearse maintenance windows, validate patches and predict operational impact before touching production. Only after changes succeed in simulation are they applied to the live environment, maximizing uptime and ensuring infrastructure availability.

This lifecycle approach reflects how modern AI factories can operate as they scale.

## **Simulating AI Factories Becomes the Backbone of AI Infrastructure**

GTC showed that simulation is no longer a future concept — it is the new backbone of AI infrastructure deployment and operations.

NVIDIA DSX Air enables customers and partners to simulate everything in one place, accelerating deployment, reducing risk and ensuring day‑one performance at scale.

## **Adopting NVIDIA DSX Air to Accelerate Deployments With Simulation**

Siam.AI,

Thailand’s largest AI cloud provider, has accelerated its infrastructure deployment with NVIDIA DSX Air. Using simulation, Siam.AI embraced NVIDIA best practices well ahead of schedule, ensuring day-one operational expertise and validating their architecture in a virtual environment before the physical hardware even arrived.

Similarly,

Hydra Host

is using DSX Air to accelerate development of Brokkr, its AI factory operating system for bare-metal GPU provisioning that’s used by dozens of GPU deployments globally. By simulating full-stack environments in DSX Air before deploying to production, Hydra Host can validate Brokkr’s automation and orchestration workflows across diverse networking and hardware configurations at scale. This simulation-first approach lets Hydra Host ship validated infrastructure faster to customers worldwide while minimizing risk to live systems as global AI demand grows.

As AI factories grow in size and complexity, the ability to validate full‑stack environments before hardware arrives will define the pace of innovation. NVIDIA DSX Air delivers that capability today, giving organizations the fastest possible path to first token and a more reliable way to operate AI infrastructure over time.

[*Learn more*](http://www.nvidia.com/air/)
*about NVIDIA DSX Air.*