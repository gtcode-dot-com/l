---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-22T14:15:36.556864+00:00'
exported_at: '2026-04-22T14:15:38.744586+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/google-cloud-agentic-physical-ai-factories
structured_data:
  about: []
  author: ''
  description: Companies can build AI factories with NVIDIA Vera Rubin-powered A5X
    instances scaling up to nearly 1 million Rubin GPUs, Gemini on Google Distributed
    Cloud, confidential NVIDIA Blackwell GPUs and agentic AI built on Gemini Enterprise
    Agent Platform with NVIDIA Nemotron and NeMo.
  headline: NVIDIA and Google Cloud Collaborate to Advance Agentic and Physical AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/google-cloud-agentic-physical-ai-factories
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA and Google Cloud Collaborate to Advance Agentic and Physical AI
updated_at: '2026-04-22T14:15:36.556864+00:00'
url_hash: a9da74a9ba8ab489ebab3e620912aa322479e8ee
---

NVIDIA and Google Cloud have collaborated for more than a decade, co‑engineering a full‑stack AI platform that spans every technology layer — from performance‑optimized libraries and frameworks to enterprise‑grade cloud services.

This foundation enables developers, startups and enterprises to push agentic and physical AI out of the lab and into production — from agents that manage complex workflows to robots and digital twins on the factory floor.

At Google Cloud Next this week in Las Vegas, the partnership reaches a new milestone, with advancements to expand Google Cloud AI Hypercomputer for AI factories that will  power the next frontier of agentic and physical AI.

These include the new
[NVIDIA Vera Rubin](https://www.nvidia.com/en-us/data-center/technologies/rubin/)

-powered A5X bare-metal instances; a

preview

of Google Gemini on Google Distributed Cloud running on
[NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)

and NVIDIA Blackwell Ultra GPUs; confidential VMs with NVIDIA Blackwell GPUs; and agentic AI on Gemini Enterprise Agent Platform with
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

open models and the
[NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/)

framework.

## **Next-Generation Infrastructure: From NVIDIA Blackwell to Vera Rubin**

At Google Cloud Next, Google announced A5X powered by
[NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)

rack-scale systems, which — through extreme codesign across chips, systems and software — deliver up to 10x lower inference cost per token and 10x higher token throughput per megawatt than the prior generation.

A5X will use
[NVIDIA ConnectX-9 SuperNICs](https://www.nvidia.com/en-us/networking/products/ethernet/supernic/)

, combined with next-generation Google Virgo networking, scaling to up to

80,000

NVIDIA Rubin GPUs within a single site cluster and up to

960,000

NVIDIA Rubin GPUs in a multisite cluster, enabling customers to run their largest AI workloads on NVIDIA‑optimized infrastructure.

“At Google Cloud, we believe the next decade of AI will be shaped by customers’ ability to run their most demanding workloads on a truly integrated, AI‑optimized infrastructure stack,” said

Mark Lohmeyer, vice president and general manager of AI and computing infrastructure at Google Cloud.

“By combining Google Cloud’s scalable infrastructure and managed AI services with NVIDIA’s industry‑leading platforms, systems and software, we’re giving customers flexibility to train, tune and serve everything from frontier and open models to agentic and physical AI workloads — while optimizing for performance, cost and sustainability.”

Google Cloud’s broad NVIDIA Blackwell portfolio ranges from A4 VMs with NVIDIA HGX B200 systems to rack-scale A4X VMs with NVIDIA GB200 NVL72 and A4X Max NVIDIA GB300 NVL72 systems, all the way to
[fractional G4 VMs](https://cloud.google.com/blog/products/compute/google-cloud-ai-infrastructure-at-nvidia-gtc-2026#:~:text=of%20Engineering%2C%20Imgix-,Introducing%20fractional%20G4%20VMs%C2%A0,-We%20are%20excited)

with
[NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/)

.

Customers can right-size their acceleration capabilities, whether using multiple interconnected NVL72 racks that scale out to tens of thousands of NVIDIA Blackwell GPUs, a single rack that can scale up to 72 Blackwell GPUs with fifth-generation NVIDIA NVLink and NVLink 5 Switch, or just one-eighth of a GPU.

This comprehensive platform helps teams optimize every workload, from mixture-of-experts reasoning, multimodal inference and data processing to complex simulations for the next frontier of physical AI and robotics.

Leading frontier AI labs are already putting this infrastructure to work.
[Thinking Machines Lab](https://www.googlecloudpresscorner.com/2026-04-22-Thinking-Machines-Expands-Use-of-NVIDIA-GPUs-through-Google-Cloud)

is scaling its Tinker application programming interface (API) on A4X Max VMs with GB300 NVL72 systems to accelerate training, while
[OpenAI](https://www.googlecloudevents.com/next-vegas/session-library?session_id=3912935&name=how-openai-builds-kubernetes-gpu-clusters&_gl=1*sm49ye*_up*MQ..&gclid=CjwKCAjwyYPOBhBxEiwAgpT8P0jnAu2Y19tTXTZkTgC8O2I0zSOvzUi_KoaLLGWJmbIWkZShLG4MVhoCjPYQAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAApdQcwelAABlHDeA_C2gSApVjSwSs)

is running large‑scale inference on NVIDIA GB300 (A4X Max VMs) and GB200 NVL72 systems (A4X VMs) on Google Cloud for some of its most demanding inference workloads, including for ChatGPT.

## **Secure AI Wherever It Needs to Run: Sovereign and Confidential**

Google Gemini models running on NVIDIA Blackwell and Blackwell Ultra GPUs are now
[in preview](https://cloud.google.com/blog/topics/hybrid-cloud/google-distributed-cloud-at-next26)

on Google Distributed Cloud, so customers can bring Google’s frontier models wherever their most sensitive data resides.

[NVIDIA Confidential Computing](https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/)

with the NVIDIA Blackwell platform enables Gemini models to run in a protected environment where prompts and fine‑tuning data stay encrypted and can’t be seen or altered by unauthorized parties, including the infrastructure operators.

In the public cloud, the
[preview](https://cloud.google.com/blog/products/identity-security/next26-redefining-security-for-the-ai-era-with-google-cloud-and-wiz)

of Confidential G4 VMs with NVIDIA RTX PRO 6000 Blackwell GPUs brings these protections to multi‑tenant environments — helping safeguard prompts, AI models and data so customers in regulated industries can access the power of AI without compromising on security or performance.

This is the first confidential computing offering of NVIDIA Blackwell GPUs in the cloud, giving Google Cloud customers a new foundation for secure, high‑performance AI.

## **Open Models and APIs for Agentic AI**

The NVIDIA platform on Google Cloud is optimized to run every kind of model — from Google’s frontier Gemini and
[Gemma](https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/)

families to NVIDIA Nemotron open models and the broader open weight ecosystem — equipping developers to build agentic AI systems that reason, plan and act.

[NVIDIA Nemotron 3](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)

Super is available on Gemini Enterprise Agent Platform, giving developers a direct path to discovering, customizing and deploying NVIDIA‑optimized reasoning and multimodal models for agentic workflows.

Google Cloud and NVIDIA are also making it easier to train and customize open models at scale. Managed Training Clusters on Gemini Enterprise Agent Platform introduced a new managed reinforcement learning (RL) API built with
[NVIDIA NeMo RL](https://github.com/NVIDIA-NeMo/RL)

for accelerating RL training at scale while automating cluster sizing, failure recovery and job execution, so teams can focus on agent behavior and model quality instead of infrastructure management.

Cybersecurity leader
[CrowdStrike](https://www.googlecloudevents.com/next-vegas/session-library?session_id=4033904&name=accelerate-domain-ai-agents-on-google-cloud-vertex-ai-with-nvidia-nemo-and-nvidia-nemotron)

uses
[NVIDIA NeMo](https://github.com/NVIDIA-NeMo)

open libraries such as NeMo Data Designer, NeMo Automodel and NeMo Megatron Bridge to generate synthetic data and fine-tuning Nemotron and other open large language models for domain-specific cybersecurity. Running on Managed Training Clusters on Gemini Enterprise Agent Platform with NVIDIA Blackwell GPUs, these capabilities accelerate threat detection, investigation and response.

## **Building the Future of Industrial and Physical AI**

Building industrial and physical AI at scale demands powerful hardware and a combination of open models, libraries and frameworks to develop these complex end-to-end workflows.

NVIDIA AI infrastructure, open models and physical AI libraries available on Google Cloud, is mainstreaming
[industrial](https://nvidianews.nvidia.com/news/nvidia-and-global-industrial-software-giants-bring-design-engineering-and-manufacturing-into-the-ai-era)

and physical AI applications, enabling customers to simulate, optimize and automate real-world workflows.

Solutions from leading industrial software providers, including

Cadence

and

Siemens Digital Industries Software

, are now available on Google Cloud, accelerated on NVIDIA AI infrastructure. These applications are powering the next-generation design, engineering and manufacturing of everything from chips to autonomous vehicles, robotics, aerospace platforms, heavy machinery and large-scale production systems.

With
[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)

libraries and the open source
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)

robotics simulation framework available on
[Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?_gl=1*6u2y51*_up*MQ..*_gs*MQ..&gclid=Cj0KCQjwqPLOBhCiARIsAKRMPZoXw6AmBoY0n3Ogp2aZPgYaBvypBXygQfMyiyPjN_LCtFrOl99PP_QaApBwEALw_wcB&gclsrc=aw.ds&pli=1&rapt=AEjHL4PbiwiHdb9qi9WEmm8smGFoRJsO0_no2rD3cR5YybMNyg8tSG97i5ihTlfBK2_YjiXIV5NFPoRfgpK8Ej-_smBjtUVSYsNqxcxd6YuIzYOhyVdP9bA&q=nvidia%20omniverse)

, developers can build physically accurate digital twins and develop custom robotics simulations pipelines to train, simulate and validate robots before real-world deployment.

NVIDIA NIM microservices for models like
[NVIDIA Cosmos Reason 2](https://huggingface.co/blog/nvidia/nvidia-cosmos-reason-2-brings-advanced-reasoning)

can be deployed to Google Vertex AI and Google Kubernetes Engine. This enables robots and vision AI agents to see, reason and act in the physical world like humans, powering use cases such as automated data curation and annotation, advanced robot planning and reasoning, and intelligent video analytics agents for real-time insights and decision-making.

Together, these technologies help developers seamlessly move from computer-aided design to living industrial digital twins and AI‑driven robots, accelerating processes from design sign‑off to factory optimization on the NVIDIA platform running on Google Cloud.

## **Proven Impact: From Startups to Global Enterprises**

Global enterprises, AI labs and high‑growth startups are using NVIDIA and Google Cloud’s co-engineered platform to move from prototyping to production faster, including

Snap

,

Schrödinger

and

Salesforce

.
[Snap](https://blogs.nvidia.com/blog/snap-accelerated-data-processing/)

is cutting the cost of large‑scale A/B testing by shifting data pipelines to GPU‑accelerated Spark on Google Cloud.
[Schrödinger](https://www.youtube.com/watch?v=607ZZ0Zp5jo)

is shrinking weekslong drug discovery simulations into just hours with NVIDIA accelerated computing on Google Cloud.

Startups are orchestrating the next wave of AI innovation — building new agents and AI‑native applications using NVIDIA accelerated computing on Google Cloud.

As part of a
[broader ecosystem](https://cloud.google.com/blog/topics/startups/startups-are-building-the-agentic-future-with-google-cloud)

highlighted through
[NVIDIA Inception](https://www.nvidia.com/en-us/startups/?ncid=ref-kc-319196-vt18&sfdcid=Google)

and Google for Startups,
[CodeRabbit](https://www.coderabbit.ai/blog/faster-code-reviews-with-nemotron-3-super)

and
[Factory](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Ffactory.ai%2F&data=05%7C02%7Cjmein%40nvidia.com%7C9ce17d3a05a241f0a59d08de9af61e3f%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C639118579083595885%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=XDthv%2FmX3KwuqjxIOqw0vss%2BpMX8v437XoDGR2cVo9Y%3D&reserved=0)

are using NVIDIA Nemotron‑based models on Google Cloud to power code review and autonomous software development agents, while

Aible

,

Mantis AI

,
[Photoroom](https://www.photoroom.com/inside-photoroom)

and

Baseten

are building enterprise data, video intelligence, generative imagery and managed inference solutions on the full‑stack NVIDIA platform on Google Cloud.

More than 90,000 developers have become a part of the joint NVIDIA and Google Cloud
[developer community](https://developers.google.com/community/nvidia?utm_source=linkedin&utm_medium=unpaidsoc&utm_campaign=fy25q2-googlecloud-blog-ai-in_feed-no-brand-global&utm_content=-&utm_term=-&linkId=14552521)

in just over a year, tapping this platform to build and scale new AI applications.

In addition, NVIDIA has been honored at Next as
[Google Cloud Partner of the Year](https://cloud.google.com/blog/topics/partners/2026-partners-of-the-year-winners-next26)

in two categories — AI Global Technology Partner and Infra Modernization Compute — in recognition of deep technical expertise and go-to-market alignment.

Together, NVIDIA and Google Cloud are giving customers a cloud‑scale platform to turn experimental agents and simulations into production systems that review code, secure fleets, enable new AI applications and optimize factories in the real world.

*Learn more about the companies’ collaboration by attending*
[*NVIDIA sessions, demos and workshops*](https://www.nvidia.com/en-us/events/google-cloud-next/)
*at Google Cloud Next.*