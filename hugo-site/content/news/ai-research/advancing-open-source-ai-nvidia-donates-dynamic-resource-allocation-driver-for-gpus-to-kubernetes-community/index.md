---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:21:53.743282+00:00'
exported_at: '2026-04-02T04:21:56.406176+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026
structured_data:
  about: []
  author: ''
  description: In addition, NVIDIA announced at KubeCon Europe a confidential containers
    solution for GPU-accelerated workloads, updates to the NVIDIA KAI Scheduler and
    new open source projects to enable large-scale AI workloads.
  headline: Advancing Open Source AI, NVIDIA Donates Dynamic Resource Allocation Driver
    for GPUs to Kubernetes Community
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Advancing Open Source AI, NVIDIA Donates Dynamic Resource Allocation Driver
  for GPUs to Kubernetes Community
updated_at: '2026-04-02T04:21:53.743282+00:00'
url_hash: 308132c515b14e2d3b12027bbbe69285962cb40a
---

Artificial intelligence has rapidly emerged as one of the most critical workloads in modern computing.

For the vast majority of enterprises, this workload runs on Kubernetes, an open source platform that automates the deployment, scaling and management of containerized applications.

To help the global developer community manage high-performance AI infrastructure with greater transparency and efficiency, NVIDIA is donating a critical piece of software — the
[NVIDIA Dynamic Resource Allocation (DRA) Driver for GPUs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/dra-intro-install.html)

— to the Cloud Native Computing Foundation (CNCF), a vendor-neutral organization dedicated to fostering and sustaining the cloud-native ecosystem.

Announced today at KubeCon Europe, CNCF’s flagship conference running this week in Amsterdam, the donation moves the driver from being vendor-governed to offering full community ownership under the Kubernetes project. This open environment encourages a wider circle of experts to contribute ideas, accelerate innovation and help ensure the technology stays aligned with the modern cloud landscape.

“NVIDIA’s deep collaboration with the Kubernetes and CNCF community to upstream the NVIDIA DRA Driver for GPUs marks a major milestone for open source Kubernetes and AI infrastructure,”

said Chris Aniszczyk, chief technology officer of CNCF. “

By aligning its hardware innovations with upstream Kubernetes and AI conformance efforts, NVIDIA is making high-performance GPU orchestration seamless and accessible to all.”

In addition, in collaboration with the CNCF’s Confidential Containers community, NVIDIA has introduced GPU support for Kata Containers, lightweight virtual machines that act like containers. This extends hardware acceleration into a stronger isolation, separating workloads for increased security and enabling AI workloads to run with enhanced protection so organizations can easily implement confidential computing to safeguard data.

## **Simplifying AI Infrastructure**

Historically, managing the powerful GPUs that fuel AI within data centers required significant effort.

This contribution is designed to make high-performance computing more accessible. Key benefits for developers include:

* **Improved Efficiency:**

  The driver allows for smarter sharing of GPU resources, delivering effective use of computing power, with support of
  [NVIDIA Multi-Process Service](https://docs.nvidia.com/deploy/mps/index.html)

  and
  [NVIDIA Multi-Instance GPU](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)

  technologies.
* **Massive Scale:**

  It provides native support for connecting systems together, including with
  [NVIDIA Multi-Node NVlink](https://developer.nvidia.com/blog/enabling-multi-node-nvlink-on-kubernetes-for-gb200-and-beyond/)

  interconnect technology. This is essential for training massive AI models on
  [NVIDIA Grace Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)

  systems and next-generation AI infrastructure.
* **Flexibility:**

  Developers can dynamically reconfigure their hardware to suit their needs, changing how resources are allocated on the fly.
* **Precision:**

  The software supports fine-tuned requests, allowing users to ask for the specific computing power, memory settings or interconnect arrangement needed for their applications.

## **A Collaborative, Industry-Wide Effort**

NVIDIA is collaborating with industry leaders — including

Amazon Web Services,
[Broadcom](https://blogs.vmware.com/cloud-foundation/2026/03/23/strengthening-the-cloud-native-ecosystem-through-upstream-collaboration/)

,
[Canonical](https://ubuntu.com/blog/canonical-nvidia-kubecon-2026)

,
[Google Cloud](https://cloud.google.com/blog/products/containers-kubernetes/gke-and-oss-innovation-at-kubecon-eu-2026)

,

Microsoft

,

Nutanix

,

Red Hat

and
[SUSE](http://suse.com/c/the-power-of-community-for-enterprise-ai)

— to drive these features forward for the benefit of the entire cloud-native ecosystem.

“Open source will be at the core of every successful enterprise AI strategy, bringing standardization to the high-performance infrastructure components that fuel production AI workloads,”

said Chris Wright, chief technology officer and senior vice president of global engineering at Red Hat

. “NVIDIA’s donation of the NVIDIA DRA Driver for GPUs helps to cement the role of open source in AI’s evolution, and we look forward to collaborating with NVIDIA and the broader community within the Kubernetes ecosystem.”

“Open source software and the communities that sustain it are a cornerstone of the infrastructure used for scientific computing and research,”

said Ricardo Rocha, lead of platforms infrastructure at CERN

. “For organizations like CERN, where efficiently analyzing petabytes of data is essential to discovery, community-driven innovation helps accelerate the pace of science. NVIDIA’s donation of the DRA Driver strengthens the ecosystem researchers rely on to process data across both traditional scientific computing and emerging machine learning workloads.”

## **Expanding the Open Source Horizon**

This donation is just part of NVIDIA’s broader initiatives to support the open source community. For example,
[NVSentinel](https://github.com/NVIDIA/NVSentinel)

— a system for GPU fault remediation — and
[AI Cluster Runtime](https://github.com/NVIDIA/aicr)

, an agentic AI framework, were announced at GTC last week.

In addition, NVIDIA
[announced at GTC new open source projects](https://nvidianews.nvidia.com/news/nvidia-announces-nemoclaw)

including the
[NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw)

reference stack and
[NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell)

runtime for securely running autonomous agents. OpenShell provides fine-grained programmable policy security and privacy controls, and natively integrates with Linux, eBPF and Kubernetes.

NVIDIA also today announced that its high-performance AI workload scheduler, the KAI Scheduler, has been onboarded as a CNCF Sandbox project — a key step toward fostering broader collaboration and ensuring the technology evolves alongside the needs of the wider cloud-native ecosystem. Developers and organizations can
[use and contribute to the KAI Scheduler today](https://github.com/kai-scheduler/KAI-Scheduler)

.

NVIDIA remains committed to actively maintaining and contributing to Kubernetes and CNCF projects to help meet the rigorous demands of enterprise AI customers.

In addition, following the release of
[NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo)

1.0

, NVIDIA is expanding the Dynamo ecosystem with
[Grove](https://github.com/ai-dynamo/grove)

, an open source Kubernetes application programming interface for orchestrating AI workloads on GPU clusters. Grove, which enables developers to express complex inference systems in a single declarative resource, is being integrated with the llm-d inference stack for wider adoption in the Kubernetes community.

*Developers and organizations can begin using and contributing to the*
[*NVIDIA DRA Driver today*](https://github.com/NVIDIA/k8s-dra-driver-gpu)
*.*

*Visit the*
[*NVIDIA booth at KubeCon*](https://www.nvidia.com/en-eu/events/kubecon-cloudnativecon-europe/)
*to see live demos of this technology in action.*