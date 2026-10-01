---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-01T19:24:51.225094+00:00'
exported_at: '2026-10-01T19:24:54.337756+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ibc-news-2026
structured_data:
  about: []
  author: ''
  description: At IBC, NVIDIA is announcing a major expansion to NVIDIA AI for Media
    to unlock new ways to understand motion, verify and enhance video, localize programming
    and build AI-powered media applications.
  headline: NVIDIA Brings Real-Time AI to Broadcast, Sports and Global Streaming at
    IBC
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ibc-news-2026
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Brings Real-Time AI to Broadcast, Sports and Global Streaming at IBC
updated_at: '2026-10-01T19:24:51.225094+00:00'
url_hash: 507a075c9a26389e1d5bbd764b3b74009b84cec7
---

At the IBC conference, running Sept. 11-14 in Amsterdam, the creative, technology and business communities are coming together to turn ideas into action and discuss innovations across the media and entertainment industries. More than 44,000 attendees from 170+ countries are gathering to explore 1,300+ exhibitions in 14+ halls and outdoor spaces, with over 600 speakers delivering insights.

Read on to learn more about what NVIDIA’s highlighting at the show.

---

Media companies are increasingly integrating AI into live production, sports, news and streaming workflows to unlock richer performance insights, verify video authenticity, and enhance and localize content — all without disrupting trusted broadcast environments.

At IBC 2026 in Amsterdam, NVIDIA announced a major expansion to NVIDIA AI for Media — a collection of GPU-accelerated software development kits (SDKs), NVIDIA NIM microservices, playbooks, and blueprints that enhance audio, video and augmented-reality effects for media and entertainment workflows — to unlock new ways to understand motion, verify and enhance video, localize programming and build AI-powered media applications.

The
[**NVIDIA Synthetic Video Detector**](https://build.nvidia.com/nvidia/synthetic-video-detector)
**(SVD)**

NIM microservice, announced earlier this year at
[SIGGRAPH](https://blogs.nvidia.com/blog/siggraph-news-2026/#synthetic-video)

,

helps organizations assess the probability of whether footage is authentic or AI-generated, giving editorial, content-authentication, digital-forensics and media-integrity teams another point of analysis in their review process.

Since its initial release, SVD’s accuracy has reached 99.3% for text-to-video content and 97.7% for image-to-video content, with especially large gains on difficult image-to-video cases.

Dalet is integrating SVD into a secure, cloud-hosted verification workflow for news organizations. This allows editorial teams to submit footage through SVD, inspect and review the resulting scores and metadata within a Dalet interface.

TwelveLabs announced the general availability of Compliance by TwelveLabs, its first application built on the company’s video intelligence platform, helping media and broadcast teams rapidly screen content against regional and custom compliance standards. The solution integrates SVD to add frame-level authenticity signals and confidence scores, enabling media teams to identify potentially synthetic media within the same compliance workflow.

Wowza
*,*

whose
[Wowza Streaming Engine](https://www.wowza.com/streaming-engine)

media server technology powers more than 35,000 video deployments across over 170 countries, will distribute SVD through the
[Wowza Video Intelligence Framework](https://www.wowza.com/video-intelligence-framework)

. The solution, powered by NVIDIA-accelerated infrastructure, will enable broadcasters, streaming providers and other organizations to analyze live video feeds and extract data around detected objects, scenes and signs of AI generation in real time. It can be deployed and run on premises, at the edge, in the cloud, across hybrid deployments or fully air-gapped, giving organizations greater control over critical media workflows.

**NVIDIA 3D Body Pose**

estimates 2D and 3D human joint locations and angles from video captured by a single camera, helping turn motion into structured data without marker-based capture systems.

For sports organizations, that data can support player and athlete movement tracking, biomechanics and performance analysis, replay enhancement, officiating and adjudication workflows, player-safety applications, and virtual interaction and immersive experiences.

The technology can also provide structured human-motion data for content-creation workflows. When mapped to a compatible character rig, joint and motion data can serve as input for animation blocking, digital doubles, character retargeting and virtual-production experiences.

Vizrt is using Body Pose technology in live virtual-studio environments, with tracked body movement driving real-time 3D lighting effects such as reflections, shadows and environmental rendering.

**Video Frame Generation (VFG)**

makes video motion appear smoother by using generative AI to create new frames between the original frames of a video. It can increase frame rates by 2x or 4x while preserving visual quality and temporal consistency, enabling more fluid sports, slow-motion replays, live media and other high-motion video experiences. VFG also supports frame-rate conversion and frame boosting for generative AI video workflows.

Ross Video is integrating VFG into its Rio Replay platform to create AI-assisted slow-motion video for sports production.

The work supports 6x slow-motion generation for sports replay. Development is underway toward 8x interpolation, meaning generated intermediate frames can give replay teams smoother motion without requiring every frame to be captured by an ultrahigh-frame-rate source camera.

**NVIDIA Video Super Resolution**

(VSR) uses AI to upscale video while reducing noise, blur and compression artifacts. New streaming modes let developers choose between real-time performance and higher image quality, while adjustable controls help achieve the desired level of enhancement. VSR also adds 10-bit video support and improves overall performance and quality. VSR is available through the NVIDIA Video Effects SDK and a NIM microservice for use in streaming, broadcast, conferencing, video playback and content-creation applications.

The technology can support video players, conferencing applications, creator tools, streaming services, transcoders and broadcast systems through a common interface.

**NVIDIA TrueHDR**

converts standard-dynamic-range video into high-dynamic-range output in real time, reaching up to approximately 2,000 nits while preserving local contrast and adapting brightness to the content.

VSR, VFG and TrueHDR can be combined within a single video-effects pipeline — helping media companies enhance existing content libraries for streaming, transcoding, gaming and creator workflows.

The
[**NVIDIA LipSync**](https://build.nvidia.com/nvidia/lipsync)

and
[**Active Speaker Detection**](https://build.nvidia.com/nvidia/active-speaker-detection)

NIM microservices help developers build localization systems for interviews, news, sports, entertainment and other programming where multiple people may appear on screen.

LipSync transforms mouth movement in an input video to match a target audio track while preserving natural head pose, blinking and body movement. The new release improves facial occlusion handling and better preserves teeth, lip and facial textures.

The new Active Speaker Detection NIM microservice no longer requires speaker diarization for multiple audio tracks, adds voice activity detection and expands NIM microservice deployment support through a gRPC interface and broader GPU compatibility.

[NDI](https://ndi.video/stories/press/ndi-nvidia-ai-multilingual-content/)

is using NVIDIA AI for Media, including the NVIDIA LipSync NIM microservice, to enable real-time translation, lip-synced dubbing and regional language adaptation within existing broadcast workflows. By generating multiple language experiences from a common media stream, the approach can help broadcasters reach global audiences while reducing the bandwidth, infrastructure and production complexity traditionally required for multilingual distribution.

**Studio Voice**

includes new Microphone Profiles built on NVIDIA Studio Voice NIM microservices, giving users more control over the tonal character of enhanced speech.

The capability is designed to suppress background noise, reduce room reverberation and improve speech clarity, then shape the enhanced output into a selected microphone profile for more polished live communications, streaming, podcasting and content creation.

*Try*
[*NVIDIA AI for Media NIM microservices*](https://build.nvidia.com/models?label=nvidia+ai+for+media)
*. See the latest NVIDIA and partner workflows at*
[*IBC 2026*](https://www.nvidia.com/en-us/events/ibc/)
*.*

---

## **NVIDIA Holoscan for Media Provides Open Media Exchange Layer to Build and Connect Live Media Applications** [***🔗***](https://blogs.nvidia.com/blog/ibc-news-2026/#mxl)

![](https://blogs.nvidia.com/wp-content/uploads/2026/09/holoscan-for-media-1920x1080-1-1680x945.jpg)

As broadcasters, streaming services and sports organizations adopt software and AI, the infrastructure behind live content is becoming more flexible, more connected and increasingly built on shared accelerated computing.

The integration of Media Exchange Layer (MXL) with
[NVIDIA Holoscan for Media](https://developer.nvidia.com/holoscan-for-media)

accelerates that transition — providing the common exchange layer that helps media applications connect and operate together.

Holoscan for Media is an open reference architecture and developer toolkit for building AI-powered media functions and applications for software-defined live production. MXL adds an open way for those software-based media functions to exchange live video, audio and data across a distributed environment.

As production functions move into software, developers can build applications that share accelerated infrastructure, connect dynamically and evolve independently. That can help media companies use infrastructure more efficiently, introduce new capabilities faster and reduce the amount of custom integration required between applications.

The integration also creates a stronger foundation for AI in live media. AI processing, video applications and traditional media functions can increasingly operate on the same accelerated infrastructure and in the same software-defined environment.

For technology vendors, this expands the opportunity to build applications that can work across broader, multi-vendor ecosystems. For media companies, it creates a path toward infrastructure that can adapt as formats, applications and AI capabilities change.

*See the demo at IBC in*
[*EBU Stand 10.D21*](https://directory.ibc.org/8_0/floorplan/?hallID=F&amp;level=1&amp;st=exhibitor&amp;selectedBooth=booth%7E10.D21)
*. ​Learn more about*
[*Holoscan for Media*](https://developer.nvidia.com/holoscan-for-media)
*.*

---

## **NVIDIA Sports Intelligence Playbooks Chart a Path to Multimodal AI for Sports** [***🔗***](https://blogs.nvidia.com/blog/ibc-news-2026/#sports-intelligence-playbooks)

![](https://blogs.nvidia.com/wp-content/uploads/2026/09/sports-intelligence-playbooks-1920x1080-1-1680x945.jpg)

Sports is becoming a proving ground for a broader shift in AI: from general-purpose models toward fine-tuned open models built on proprietary data.

[NVIDIA Sports Intelligence Playbooks](https://nvidia.github.io/sports-intelligence-playbooks/latest/)
are designed to accelerate that transition. They give leagues, media companies and technology providers structured frameworks to fine-tune NVIDIA open models on their own sports footage and annotations, creating multimodal AI that can understand the rules, players, scoring, strategy and context unique to a sport.

Sports organizations hold large volumes of proprietary video, metadata and performance information that are difficult for competitors to replicate. The playbooks provide a practical blueprint for converting those assets into AI capabilities that can underpin new analytics products, media experiences, automation tools and revenue streams.

The playbooks span the AI lifecycle, including data preparation, fine-tuning, inference, evaluation, optimization and deployment, and bring together NVIDIA technologies including
[Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

,
[NeMo AutoModel](https://docs.nvidia.com/nemo/automodel)

,
[Megatron Bridge](https://docs.nvidia.com/nemo/megatron-bridge/latest/)

,
[NIM microservices](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)

and
[NVIDIA accelerated computing](https://www.nvidia.com/en-us/data-center/solutions/accelerated-computing/)

.

By providing an integrated path from model customization to production, Sports Intelligence Playbooks can reduce the cost and complexity of building specialized sports AI while increasing demand across its compute, software and inference stack.

Early testing demonstrates the potential of domain specialization. When evaluated on previously unseen footage using question formats similar to those used in training,  multiple-choice accuracy increased from approximately 53% to 94% and open-ended evaluation from approximately 5.7% to 66%.

Machina Sports is integrating Sports Intelligence Playbooks with its sports-native data, evaluation and agent infrastructure, enabling rights holders to turn proprietary media and expertise into private, deployable intelligence for live production, content and fan experiences.

The opportunity also expands as agentic AI becomes increasingly adopted. With the
[NVIDIA AI-Q Blueprint](https://build.nvidia.com/nvidia/aiq)

, organizations can use their domain-specific sports models as expert intelligence within agents that reason across video, enterprise data and software systems, extending the playbook from sports understanding into decision-making and automation.

Wowza is integrating vision language models, including NVIDIA Cosmos 3 and Nemotron, into the Wowza Video Intelligence Framework, fine-tuned through NVIDIA Sports Intelligence Playbooks to detect sports-specific moments in live streams and reduce time to action.

*Explore*
[*NVIDIA Sports Intelligence Playbooks*](https://github.com/NVIDIA/sports-intelligence-playbooks)
*.*

---

## **NVIDIA Brings Multilingual Content Localization to Live Broadcast** [***🔗***](https://blogs.nvidia.com/blog/ibc-news-2026/#content-localization)

Reaching global audiences with live programming requires more than translating words. Language nuances, voice, timing, facial movement, captions and onscreen graphics must work together in real time, while preserving the editorial intent and production quality of the original program.

To help broadcasters, sports leagues, rights holders and streaming services bring these elements into a unified, software-defined, real-time localization workflow, NVIDIA is bringing its Content Localization technologies to the NVIDIA Holoscan for Media developer toolkit. Designed for broadcast and streaming developers, the reference workflow enables captions, translated audio, dubbing, synchronized video and localized graphics.

Content Localization with Holoscan for Media provides a reference for how localization technologies can work together in software-defined broadcast applications. Developers can select the capabilities needed for each program, market or distribution channel rather than deploying separate infrastructure for every localized version.

Content Localization with Holoscan for Media incorporates the latest advancements from NVIDIA AI for Media, including improved LipSync when faces are partially obscured and enhanced Active Speaker Detection to help applications identify who’s speaking in multi-person scenes.

### **Expanding the Reach of Live Programming**

Localization can transform the reach and economics of live programming. A shared, composable workflow can help media companies introduce regional coverage faster, serve more audiences and tailor experiences for individual markets — while preserving the timing, visual context and editorial control required for live production.

Technologies from

AI-Media

,

CAMB.AI

, Chyron and

Panjaya

each address a specific part of content localization with Holoscan for Media, from adapting voice and onscreen delivery to creating multilingual captions and translated audio, localizing graphics, and preserving expression and identity across live and on-demand content.

The Content Localization technologies also support file-based, streaming and post-production applications. Developers can use application programming interfaces for on-demand workflows and the Holoscan for Media reference workflow when localization must run as part of a live media environment. Together, they provide a consistent foundation for building multilingual media services across production and distribution.

*Learn more about NVIDIA*
[*Holoscan for Media*](https://developer.nvidia.com/holoscan-for-media)
*and*
[*AI for Media*](https://developer.nvidia.com/topics/ai/generative-ai/ai-for-media)
*.*