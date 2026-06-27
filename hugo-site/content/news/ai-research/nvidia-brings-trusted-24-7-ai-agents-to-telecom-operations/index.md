---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-27T03:43:39.810416+00:00'
exported_at: '2026-06-27T03:43:41.112556+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/telecom-ai-agents-dtw-ignite-2026
structured_data:
  about: []
  author: ''
  description: At DTW Ignite 2026, NVIDIA and its partners are showcasing the data,
    models, simulation and secure runtime stack enabling telcos to build more secure
    agentic workflows across autonomous networks and operations.
  headline: NVIDIA Brings Trusted, 24/7 AI Agents to Telecom Operations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/telecom-ai-agents-dtw-ignite-2026
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Brings Trusted, 24/7 AI Agents to Telecom Operations
updated_at: '2026-06-27T03:43:39.810416+00:00'
url_hash: 435be69646209d3c852707f696083b16307861cb
---

Telecom operators have seen remarkable
[returns](https://resources.nvidia.com/en-us-ai-in-telco/telco-report-state-o)

from using generative AI to automate network management, customer care and back-office operations. Most of that impact has been task‑based: automation that speeds up predetermined steps while people manually correlate insights and direct next steps.

Automation is no longer the finish line — it’s the launchpad to autonomy.

The industry is now pushing toward truly
[autonomous networks](https://www.nvidia.com/en-us/glossary/autonomous-networks/)

and operations, where AI agents proactively watch for problems and coordinate changes across network, IT and business systems.

Together, synthetic data, telecom-domain models, secure agent runtimes and simulations form critical pieces of a secure,
[telecom autonomy platform](https://developer.nvidia.com/blog/how-telcos-build-autonomous-networks-with-agentic-ai)

, where agents understand operator intent, act safely across business and network domains and keep humans in control of policy.

NVIDIA and its partners are demonstrating these building blocks at TM Forum’s DTW Ignite 2026 — running this week in Copenhagen — giving operators a practical path to running more autonomous, resilient networks and powering richer AI‑driven services for consumers and businesses.

## **Unlock Privacy‑Safe Telecom Data for AI Models**

Reasoning models that understand the telecom domain are the foundation of autonomous networks. These specialized models require fine‑tuning on high‑quality datasets, yet
[54%](https://resources.nvidia.com/en-us-ai-in-telco/telco-report-state-o)

of operators cite data‑related issues as their biggest barrier, with the most valuable network and customer data too sensitive to use directly.

[Synthetic data](https://www.nvidia.com/en-us/glossary/synthetic-data-generation/)

is enabling operators to safely increase the volume and diversity of training data, protect sensitive information and democratize access to production‑like telecom datasets across internal teams and external developers, without exposing raw customer records.

[SoftBank Corp](https://www.softbank.jp/corp/technology/research/topics/221/?adid=nv)

.

is using technologies such as NVIDIA
[NeMo

Safe Synthesizer](https://nvidia-nemo.github.io/Safe-Synthesizer/latest/)

and NVIDIA
[NeMo Anonymizer](https://nvidia-nemo.github.io/Anonymizer/latest/)

to generate privacy‑preserving synthetic datasets that reflect the structure and distribution of real network performance and configuration datasets. These datasets are being used to fine-tune its large telecom model and build specialized network agents.

## **Securely Deploy Autonomous Telecom Agents**

As telecom operators look to achieve autonomy across end-to-end workflows, they need AI agents that can stick with a complex job from start to finish, not just execute a pointed task. Long‑running autonomous agents that operate under strict service-level agreements, change‑management policies and regulatory constraints are key to this shift.

[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/?ncid=pa-srch-goog-984177&amp;_bt=804567865336&amp;_bk=nvidia%20nemoclaw&amp;_bm=p&amp;_bn=g&amp;_bg=197993095849&amp;gad_source=1&amp;gad_campaignid=23744621431&amp;gbraid=0AAAAAD4XAoGg0ZGZS_fDtUGSv3Oxclup9&amp;gclid=CjwKCAjwn4vQBhBsEiwAq3hhN26uZkd5xnI5dPqoOJLx7d0nSMZwcDkBy5VX-QBDfvE_p3M5PpGESxoCAL8QAvD_BwE)

blueprints and the
[NVIDIA OpenShell](https://build.nvidia.com/openshell)

secure runtime give these agents policy‑based guardrails and sandboxed access to telecom systems, so operators can more safely expand the role of agents in operations while keeping behavior predictable, auditable and governed.

[AdaptKey](https://adaptkey.ai/blog/KeySmith)

is collaborating with operators to pilot security‑hardened, long-running agents for self‑healing 5G network operations. NemoClaw and OpenShell power agents that detect security and connectivity issues and submit scoped remediation requests into

AdaptKey

’s KeySmith platform for execution, which orchestrates diagnosis and runs agents that apply auditable fixes across core, radio access network (RAN) and billing systems.

[Amdocs](https://www.amdocs.com/insights/blog/scaling-proactive-agents-telecom-turning-autonomy-trusted-execution)

is showcasing the potential of NemoClaw and OpenShell for proactive customer-care agents, including roaming assistance scenarios where autonomous agents can identify customers whose roaming package is nearing depletion, engage them with approved options and execute actions within defined business policies and operational controls.

Amdocs

is applying this runtime to autonomous data‑science agents that analyze customer accounts and assess migration eligibility, producing ranked, decision‑ready views that help operators intelligently sequence migrations to modern billing and business platforms at the right time and in the right order.

[NTT DATA](https://services.global.ntt/en-us/insights/blog/how-agentic-ai-detects-silent-network-degradation)

is using NVIDIA Nemotron open models with NemoClaw to build long‑running agents for proactive detection of network degradation. These anomaly agents track long‑term performance trends and escalate relevant cases to research agents for fine‑grained telemetry analysis and clear remediation proposals.

[ServiceNow](https://www.servicenow.com/workflow/industries/changing-telecom-operations-nvidia.html)

is bringing
[Project Arc](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx)

to telecom, enabling autonomous network operations center agents that run incident response. Arc pulls context from emails, logs and diagnostics across disconnected systems and orchestrates the full lifecycle from initial alerts to assigned work orders. Secured by NVIDIA OpenShell and governed by ServiceNow AI Control Tower, every Arc action stays contained, auditable and within policy.

Tata Consultancy Services (TCS)

is building a multi‑fidelity “AI sensor” architecture that helps operators spot and resolve network issues faster. NemoClaw orchestrates long-running agents powered by Nemotron and NVIDIA
[NV‑Tesseract](https://developer.nvidia.com/blog/new-nvidia-nv-tesseract-time-series-models-advance-dataset-processing-and-anomaly-detection/)

that scan broadly for issues and selectively trigger deeper diagnosis, giving operators a faster, more efficient path from anomaly to action.

## **Bring Trust to Autonomy With Accelerated Simulation**

As AI agents take on more responsibility in telecom operations, simulation is becoming an integral part of decision support. By accelerating simulation workloads on GPUs, operators can give agents a safe, near-real-time environment to validate their recommendations before acting on live network and business systems.

[Forsk](https://www.forsk.com/white-paper-ai-based-radio-propagation-modelling-autonomous-ran-optimisation)

has integrated an AI‑based radio propagation model into its Naos RAN planning platform, achieving ray‑tracing‑level accuracy up to 200x faster than CPU‑only baselines on NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs. The resulting RAN digital twin lets operators safely optimize the network in near real time, enabling use cases such as network self‑healing and automated antenna tilt.

[VIAVI Solutions](https://blog.viavisolutions.com/2026/06/22/building-the-gpu-accelerated-ran-digital-twins-that-will-run-tomorrows-networks/)

is accelerating its
[TeraVM AI RAN Scenario Generator](https://www.viavisolutions.com/en-us/products/teravm-ai-rsg)

by moving large‑scale RAN simulations from CPUs to NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs. Early results show order‑of‑magnitude improvements in simulation throughput, letting operators run high‑fidelity scenarios at a real deployment scale so autonomous agents can de‑risk proposed network changes.

In addition,

VIAVI

has released an
[IP Network Configuration Blueprint](https://github.com/VIAVI-AIOPS/closed-loop-intent-assurance)

that extends validation into the IP and transport network domains, enabling operators to safely validate routing, traffic‑engineering and resilience changes, before they touch the live network.

[KDDI](https://newsroom.kddi.com/english/news/detail/kddi_nr-1068_4588.html)

and

KDDI Research

are bringing accelerated simulation into the 6G era through a collaboration with NVIDIA,

Keysight

and

Samsung Research America

to build a high‑fidelity RAN digital twin using NVIDIA Aerial Omniverse Digital Twin and

Keysight’s

digital‑twin‑ready emulation tools running on

KDDI’s

AI data centers. In this environment, multiple autonomous agents will be able to safely simulate and validate RAN “what‑if” scenarios, ranging from area‑optimization strategies to future radio conditions, traffic shifts and new AI air‑interface functions.

*Dive deeper into the telecom autonomous networks stack by reading this*
[*NVIDIA technical blog*](https://developer.nvidia.com/blog/how-telcos-build-autonomous-networks-with-agentic-ai)
*.*