---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-26T03:02:12.353845+00:00'
exported_at: '2026-09-26T03:02:14.140645+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nvlink-fusion-xpu-ai-factory
structured_data:
  about: []
  author: ''
  description: Deploying custom silicon with leading AI infrastructure enables hyperscalers
    and AI-native companies to build flexible AI factories that combine specialization
    with scale.
  headline: How XPUs Meet a World-Class AI Factory
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nvlink-fusion-xpu-ai-factory
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How XPUs Meet a World-Class AI Factory
updated_at: '2026-09-26T03:02:12.353845+00:00'
url_hash: 141e6e188d62b50e0df0234f5edbd90bcc88a988
---

To generate intelligence at scale, AI factories run continuously, and their economics are defined by delivered output: tokens per second, tokens per watt, cost per token, utilization and uptime.

That requires AI infrastructure designed and built as a full factory, not a collection of individual accelerators.

Hyperscalers and AI-native companies building custom XPUs must consider not just XPU design, but the design and development of the entire AI platform, including scale-up and scale-out networking, rack-scale architecture, production factory software and a robust supplier ecosystem.

At AI factory scale, this path is complex and costly, and represents a fundamental obstacle to getting XPUs to market quickly.

Breaking the constraint means combining custom XPUs with proven, mature infrastructure — allowing builders to focus innovation where it matters most while harnessing established technology for the rest.

NVLink Fusion delivers on that need, connecting XPUs to NVIDIA’s world-leading AI infrastructure to increase performance, accelerate time to market and mitigate risk for semi-custom AI factories.

## **Unlock XPU Performance With Fast Scale-Up**

For modern workloads such as running trillion-parameter models,
[mixture-of-experts](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)

architectures and agentic AI, if the scale-up fabric cannot keep up, utilization drops and cost per token rises.

A scale-up networking solution must excel on three dimensions:

* **Delivered performance:**

  End-to-end network performance, in-network compute and  mature software integration.
* **Factory resiliency:**

  Uptime, continuous health monitoring and telemetry, and component-level serviceability while the factory keeps running.
* **Platform maturity:**

  Reduced operational risk by using a mature technology stack with a demonstrated track record of large-scale deployments and realized return on investment.

As an example, NVLink Fusion brings XPUs into the
[NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)

scale-up domain. Sixth-generation NVLink provides leading high-bandwidth, low-latency networking across a 72-XPU domain. The end-to-end latency for XPU-to-XPU transfers is 3x lower than alternative solutions based on off-the-shelf Ethernet, and the packet rate is 10x higher.

For end-to-end performance, NVIDIA GB300 NVL72 systems help deliver significantly higher throughput and better interactivity compared with configurations that don’t use NVL72, and future NVLink roadmap configurations include domains of up to 1,152 accelerators and co-packaged optics.

![A Pareto chart comparing GB300 NVL72 with B300 inference throughput performance in tokens per second per GPU on DeepSeek-V4-Pro at ISL=1K and OSL=1K sampled at various interactivity points in tokens per second per user. GB300 NVL72 is more than 10x the throughput of B300 in the middle of the Pareto between 70 and 100 tokens per second per user.](https://blogs.nvidia.com/wp-content/uploads/2026/08/nvlink-thought-leadership-graph-1920x1080-1-1680x945.jpg)


The 72-GPU NVLink scale-up domain enables GB300 NVL72 to deliver higher per-GPU throughput and interactivity compared with NVIDIA B300. Results from NVIDIA’s AI Inference Performance Benchmarks page.

NVLink Fusion also includes NVIDIA NVLink-C2C for connecting XPUs to
[NVIDIA Vera CPUs](https://www.nvidia.com/en-us/data-center/vera-cpu/)

or other ecosystem CPUs, delivering up to 6x the energy efficiency of a PCIe interface — helping remove barriers between control and compute for agentic systems.

## **A Proven Stack and Ecosystem for Development and Deployment**

Teams developing custom XPUs often underestimate the effort and complexity of turning XPU innovation into data center deployment. This includes:

* Integrating high-speed CPU and scale-up interfaces
* Sourcing and validating a scale-up network solution
* Designing compute and switch trays
* Designing and validating a rack architecture, including cooling and power
* Integrating security and storage
* Managing a complex supplier ecosystem

The ideal platform provides all of this, allowing teams to focus on targeted innovation while using proven solutions for the rest.

NVLink Fusion is supported by an ecosystem designed for rapid development, integration and deployment, spanning ASIC design, CPU, and IP and optical interconnect partners.

*“NVLink Fusion gives customers the ability to choose the CPU architecture, the performance level, the software capabilities that best meet their needs for the workloads that they care about,” said Tim Wilson, vice president and general manager of data center silicon engineering at Intel.*

NVLink Fusion adopters can also use the NVIDIA MGX rack-scale architecture and the same supply chain used for MGX-based systems such as
[NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)

. Manufacturing partners manage design and integration, while MGX suppliers provide the building blocks for rack, cooling, power and emerging
[800 VDC designs](https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/)

.

*“With Vera Rubin [NVL72], we are looking at almost 100% automation of system builds in the manufacturing line,” said Jack Luoh, head of product and solution at QCT and Quanta Computer. “Most of those investments can be leveraged if the XPU leverages NVLink Fusion.”*

The NVIDIA AI infrastructure platform is vertically integrated and horizontally open. NVLink Fusion adopters can optionally incorporate NVIDIA Rubin GPUs, Vera CPUs, co-packaged optics switches, ConnectX SuperNICs, BlueField DPUs, Mission Control software and full-rack solutions including NVIDIA Vera Rubin NVL72, Vera CPU Rack, LPX, STX and SPX.

## **Managing Risk With Infrastructure Standardization**

AI factory planning doesn’t wait for silicon. Power procurement, facility design, cooling, rack layout and network architecture begin long before the final accelerator mix is available. A data center locked to one chip can become a schedule risk.

Different workloads may favor different accelerators, including XPUs, GPUs, CPUs and LPUs. GPU systems may work alongside semi-custom systems for training, post-training, reasoning, retrieval and serving.

*“The value of the NVLink Fusion program is … [customers] can deploy their rack-level solution with the NVIDIA GPU, and then they can decouple the development of their XPU and put it at a different pace,” said Vince Hu, corporate senior vice president and general manager of the data center and computing business group at MediaTek.*

NVLink Fusion addresses these challenges  through a unified architecture. XPU- and GPU-based systems such as Vera Rubin NVL72 can share rack footprints, networking, cooling, power delivery and management systems. Operators can move forward with buildout while deferring the precise silicon mix, then reprovision capacity as workload demand, silicon supply and business priorities change.

*“NVLink

Fusion allows the hyperscalers or the custom ASIC designers to integrate their own custom CPU or XPU and bridges the NVIDIA technology with a third-party process to create a unified rack-scale architecture,” said Lie-Szu Juang, chair and chief strategy officer at GUC.*

## **Designed, Validated and Operated as a Factory**

Factory buildout is expensive, and mistakes can require costly rework. Infrastructure must be validated before construction begins. NVLink Fusion aligns with the
[NVIDIA DSX](https://www.nvidia.com/en-us/data-center/products/dsx/)

reference architecture for AI factories: codesigning buildings, power, cooling, compute and networking. The NVIDIA Omniverse DSX AI Factory Blueprint provides a digital twin and open reference design for gigawatt-scale AI factories, enabling partners to model facilities and technology together before deployment.

At the rack level, serviceability is part of performance. Reference compute trays feature 100% liquid cooling with no fans, cables or hoses, and allow trays to be removed while the rest of the rack remains operational. NVLink Switch trays are also liquid cooled and support continued operation during service.

*“With NVLink Fusion we can use proven NVL72 rack design to have time-to-market, and we can have access to multiple suppliers to help us to deliver more into the hands of our customers,” said CC Lee, senior hardware development manager at Annapurna Labs, an Amazon company.*

Software completes the factory. NVIDIA NCCL for distributed workloads, NVIDIA Dynamo and NIXL for disaggregation and NVIDIA Mission Control for cluster management, telemetry and debugging help operators run mixed AI infrastructure as a coordinated system.

With NVLink Fusion, XPUs can now meet a world-class AI platform, enabling hyperscalers and AI-native companies to build unified, semi-custom AI factories that combine the strengths of many builders into infrastructure no one company could build alone.

*Learn more about*
[*NVLink Fusion*](https://www.nvidia.com/en-us/data-center/nvlink-fusion/)
*.*