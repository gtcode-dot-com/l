---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-27T18:31:01.318386+00:00'
exported_at: '2026-09-27T18:31:03.019577+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/scx-ai-partners-with-ddn-to-scale-australias-sovereign-ai-inference-cloud
structured_data:
  about: []
  author: ''
  description: Australian sovereign AI infrastructure company SCX.ai and data intelligence
    vendor DDN announced a partnership on August 24, 2026, to expand what the companies
    describe as Australia's largest sovereign AI inferencing clo...
  headline: SCX.ai Partners With DDN to Scale Australia’s Sovereign AI Inference Cloud
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/scx-ai-partners-with-ddn-to-scale-australias-sovereign-ai-inference-cloud
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SCX.ai Partners With DDN to Scale Australia’s Sovereign AI Inference Cloud
updated_at: '2026-09-27T18:31:01.318386+00:00'
url_hash: d5559a0151fa993e8cba44fbf96bc10e83a68b18
---

Australian sovereign AI infrastructure company SCX.ai and data intelligence vendor DDN announced a partnership on August 24, 2026, to expand what the companies describe as Australia’s largest sovereign AI inferencing cloud. The deal pairs SCX’s ASIC-accelerated infrastructure with DDN’s Infinia data platform, and it lands three days after SCX began trading on the Australian Securities Exchange following a fully underwritten $40 million IPO.

The combined offering is aimed at Australian enterprises, government agencies, and research institutions that need AI inference to run onshore. SCX and DDN frame it as a secure, multi-tenant “AI factory” built to accelerate inference and lower the cost per token while keeping models, workloads, and data inside Australia. The data layer is the point of the integration: DDN says Infinia delivers sub-millisecond latency and up to 27-times faster KV cache loading, which is what keeps large context windows and agentic workloads from stalling on I/O.

“For the first time, Australian organisations have access to a fully domestic, enterprise-grade AI cloud that scales effortlessly,” said SCX founder and CEO David Keane in the
[announcement](https://www.prnewswire.com/news-releases/scxai-asx-scx-strategic-partnership-with-global-ai-leader-ddn-to-power-australias-largest-sovereign-ai-inferencing-cloud-302858797.html)
. “By integrating DDN’s world-class data platforms into our architecture, we are ensuring that our infrastructure can handle the most data-intensive workloads on the planet.”

## The Hardware Underneath Is ASIC, Not GPU

SCX’s infrastructure runs on purpose-built SambaNova SN40L AI processors rather than GPUs, and it is air-cooled, avoiding the large water volumes that conventional AI data center cooling consumes. The design bet is that more usable AI compute can be extracted from the power and physical footprint already available inside existing commercial data centers.

Testing SCX disclosed ahead of its ASX listing put its SambaNova-based systems at roughly 2.5-times to 5.6-times the performance per watt of GPU-based systems across selected stable inference workloads, depending on the model and hardware configuration tested. Those are vendor-disclosed figures from a company selling an efficiency story, but they are the crux of SCX’s pitch to a country where power and water constraints are real.

DDN CTO Sven Oehme framed the partnership around removing the data layer as the bottleneck. “By eliminating I/O bottlenecks and enabling extreme concurrency with sub-millisecond latency, we’re fundamentally changing the economics of inference – delivering higher utilisation, lower cost per token and true enterprise-grade sovereignty,” he said.

## A Newly Public Company With Early Revenue

The announcement follows SCX’s debut on the ASX on August 21, 2026, which made it Australia’s first ASX-listed pure-play sovereign AI inference infrastructure company. Keane, who founded ASX-listed Bigtincan, used the listing to fund a node build-out, writing in a
[listing-day post](https://scx.ai/resources/why-we-built-scx-listing-now)
that the $40 million raise is directed at deploying Node 1 and Node 2 infrastructure and the team and technology around it.

The company enters the public market with early commercial traction. Contracted annual recurring revenue reached $6.5 million at the end of July 2026, up 20.9 percent since May, and the platform now counts more than 400 active users. SCX’s first sovereign AI node is already operational at the Equinix SY5 data center in Sydney — a deployment the company first brought live earlier this year and described at the time as
[Australia’s first sovereign AI inferencing node](https://scx.ai/resources/scx-sovereign-ai-node-launch)
. The DDN integration is what lets that data layer keep pace with the concurrency and high-throughput inferencing demands SCX is now selling against.

The expanded capacity is also meant to support SCX’s Project MAGPiE, a sovereign large language model fine-tuned for the Australian cultural and commercial context, alongside bespoke enterprise workloads.

## Why Sovereignty Is the Selling Point

SCX’s argument to customers is legal as much as technical. Australia has no comprehensive domestic data residency law, and the US CLOUD Act lets American authorities compel access to data held by US-headquartered providers even when that data sits on a server in Sydney. Keane has been direct that adding hyperscaler capacity in Australia does not resolve that exposure for US-based providers, positioning SCX in the gap for government, financial services, and healthcare workloads that cannot go offshore. The logic mirrors what is driving sovereign AI build-outs elsewhere — Mistral and HUMAIN made the same case for Saudi Arabia and the wider region, and private and sovereign deployment is redrawing the trust boundary around where models run.

For a technically literate reader, the notable thing about the SCX-DDN deal is that it is an inference economics story built on two non-GPU bets: ASIC silicon for performance per watt, and a dedicated data-intelligence layer for utilization. Both are aimed at the same line item — cents per million tokens served onshore.

## What Happens Next

SCX’s first node at Equinix SY5 in Sydney is operational, and the company is accelerating deployment of Node 2, targeted to be operational by the end of 2026. It is also progressing plans for additional nodes as it builds out a national sovereign AI inference network. The DDN partnership is the data-layer foundation for that expansion.