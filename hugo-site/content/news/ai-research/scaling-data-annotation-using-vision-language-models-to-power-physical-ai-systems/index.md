---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T03:02:31.095906+00:00'
exported_at: '2026-03-03T03:02:36.074014+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-data-annotation-using-vision-language-models-to-power-physical-ai-systems
structured_data:
  about: []
  author: ''
  description: In this post, we examine how Bedrock Robotics tackles this challenge.
    By joining the AWS Physical AI Fellowship, the startup partnered with the AWS
    Generative AI Innovation Center to apply vision-language models that analyze construction
    video footage, extract operational details, and generate labeled training datas...
  headline: Scaling data annotation using vision-language models to power physical
    AI systems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/scaling-data-annotation-using-vision-language-models-to-power-physical-ai-systems
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scaling data annotation using vision-language models to power physical AI systems
updated_at: '2026-03-03T03:02:31.095906+00:00'
url_hash: 5529250feabc221c7160cdc133f69d74d44d3b6e
---

Critical labor shortages are constraining growth across manufacturing, logistics, construction, and agriculture. The problem is particularly acute in construction: nearly
[500,000 positions](https://www.abc.org/News-Media/News-Releases/abc-construction-industry-must-attract-439000-workers-in-2025)
remain unfilled in the United States, with
[40%](https://www.adp.com/spark/articles/2019/02/construction-grows-but-baby-boomers-retiring-leaves-gap.aspx?q1=ES_FY25_SparkSubscribePopup)
of the current workforce approaching retirement within the decade. These workforce limitations result in delayed projects, escalating costs, and deferred development plans. To address these constraints, organizations are developing autonomous systems that can perform tasks that fill capacity gaps, extend operational capabilities, and offer the added benefit of around-the-clock productivity.

Building autonomous systems requires large, annotated datasets to train AI models. Effective training determines whether these systems deliver business value. The bottleneck: the high cost of data preparation. Critically, the act of labeling video data—identifying information about equipment, tasks, and the environment—is required to make sure that the data is useful for model training. This step can impede model deployment, which slows down the delivery of AI-powered products and services to customers. For construction companies managing millions of hours of video, manual data preparation and annotation become impractical. Vision-language models (VLMs) help to address this by interpreting images and video, responding to natural language queries, and generating descriptions at a speed and scale that manual processes cannot match, providing a cost-effective alternative.

In this post, we examine how
[Bedrock Robotics](https://bedrockrobotics.com/)
tackles this challenge. By joining the
[AWS Physical AI Fellowship,](https://press.aboutamazon.com/aws/2025/9/massrobotics-aws-and-nvidia-launch-first-of-its-kind-physical-ai-fellowship)
the startup partnered with the
[AWS Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)
to apply vision-language models that analyze construction video footage, extract operational details, and generate labeled training datasets at scale, to improve data preparation for autonomous construction equipment.

## Bedrock Robotics: a case study in accelerating autonomous construction

Since 2024, Bedrock Robotics has been developing autonomous systems for construction equipment. The company’s product, Bedrock Operator, is a retrofit solution that combines hardware with AI models to enable excavators and other machinery to operate with minimal human intervention. These systems can perform tasks like digging, grading, and material handling with centimeter-level precision. Training these models requires massive volumes of video footage capturing equipment, tasks, and the surrounding environment – a highly resource-intensive process that limits scalability.

VLMs offer a solution by analyzing this image and video data and generating text descriptions. This makes them well-suited for annotation tasks, which is critical for teaching models how to associate visual patterns with human language. Bedrock Robotics used this technology to streamline data preparation for training AI models, enabling autonomous operations for equipment. Additionally, through proper model selection and prompt engineering, the company improved tool identification from 34% to 70%. This transformed a manual, time-intensive process into an automated, scalable data pipeline solution. The breakthrough accelerated deployment of autonomous equipment.

This approach provides a replicable framework for organizations facing similar data challenges and demonstrates how strategic investment in foundation models (FMs) can deliver measurable operational outcomes and a competitive advantage. Foundation models are models trained on massive amounts of data using self-supervised learning techniques that learn general representations that can be adapted to many downstream tasks. VLMs leverage these large-scale pretraining techniques to bridge visual and textual modalities, enabling them to understand, analyze, and generate content across both image and language.

In the following sections, we look at the process that Bedrock Robotics used to annotate millions of hours of video footage and accelerate innovation using a VLM-based solution.

### From unstructured video data to a strategic asset using VLMs

Enabling autonomous construction equipment requires extracting useful information from millions of hours of unstructured operational footage. Specifically, Bedrock Robotics needed to identify tool attachments, tasks, and worksite conditions across diverse scenarios. The following images are example video frames from this dataset.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/23/ML-2046.png)

Construction equipment operates with multiple tool attachments, each requiring accurate classification to train reliable AI models. Working with the Innovation Center, Bedrock Robotics focused their innovation efforts by addressing a few critical tool categories: lifting hooks for material handling, hammers for concrete demolition, grading beams for surface leveling, and trenching buckets for narrow excavation.

These labels allow Bedrock Robotics to select relevant video segments and assemble training datasets that represent a variety of equipment configurations and operating conditions.

### Accelerating AI deployment through strategic model optimization

Off-the-shelf VLMs (VLMs without prompt optimization) struggle with construction video data because they’re trained on web images, not operator footage from excavator cabins. They can’t handle unusual angles, equipment-specific visuals, or poor visibility from dust and weather. They also lack the domain knowledge to distinguish visually similar tools like digging buckets from trenching buckets.

Bedrock Robotics and the Innovation Center addressed this through targeted model selection and prompt optimization. The teams evaluated multiple VLMs—including open source options and FMs available in
[Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=572ae9ee-3a0d-4258-a24e-f5396ba81e9b&sc_channel=ps&trk=572ae9ee-3a0d-4258-a24e-f5396ba81e9b&sc_channel=ps&ef_id=CjwKCAiAv5bMBhAIEiwAqP9GuLw3dn1-30JXV1Gp_ZbUUc95xhhediy4hz5I7deWIDFZmlrYJlYNWRoChVkQAvD_BwE:G:s&s_kwcid=AL!4422!3!692006004850!e!!g!!amazon%20bedrock!21048268689!159639953975&gad_campaignid=21048268689&gbraid=0AAAAADjHtp-0RFjGQ8flyK5hf96Q2Fi6X&gclid=CjwKCAiAv5bMBhAIEiwAqP9GuLw3dn1-30JXV1Gp_ZbUUc95xhhediy4hz5I7deWIDFZmlrYJlYNWRoChVkQAvD_BwE)
—then refined prompts with detailed visual descriptions of each tool, guidance for commonly confused tool pairs, and step-by-step instructions for analyzing video frames.

These modifications enhanced the classification accuracy from 34% to 70% on a test set comprising 130 videos, at $10 per hour of video processing. These results demonstrate how prompt engineering adapts VLMs to specialized tasks. For Bedrock Robotics, this customization delivered faster training cycles, reduced time-to-deployment, and a cost-effective scalable annotation pipeline that evolves with operational needs.

## The path forward: addressing labor shortages through automation

**The Competitive Advantage.**
For Bedrock Robotics, vision-language systems enabled rapid identification and extraction of critical datasets, providing necessary insights from massive construction video footage. With an overall accuracy of 70%, this cost-effective approach provides a practical foundation for scaling data preparation for model training. It demonstrates how strategic AI innovation can transform workforce constraints and accelerate industry transformations. Organizations that streamline data preparation can accelerate autonomous system deployment, reduce operational costs, and explore new areas for growth in industries impacted by labor shortages. With this repeatable framework, manufacturing and industrial automation leaders facing similar challenges can apply these principles to drive competitive differentiation within their own domains.

To learn more, visit
[Bedrock Robotics](https://bedrockrobotics.com/)
or explore the physical AI resources on AWS.

---

### About the authors

### Laura Kulowski

**Laura Kulowski**
is a Senior Applied Scientist at the AWS Generative AI Innovation Center, where she works to develop physical AI solutions. Before joining Amazon, Laura completed her PhD at Harvard’s Department of Earth and Planetary Sciences and investigated Jupiter’s deep zonal flows and magnetic field using Juno data.

### Alla Simoneau

**Alla Simoneau**
is a technology and commercial leader with over 15 years of experience, currently serving as the Emerging Technology Physical AI Lead at Amazon Web Services (AWS), where she drives global innovation at the intersection of AI and real-world applications. With over a decade at Amazon, Alla is a recognized leader in strategy, team building, and operational excellence, specializing in turning cutting-edge technologies into real-world transformations for startups and enterprise customers.

### Parmida Atighehchian

**Parmida Atighehchian**
is a Senior Data Scientist at AWS Generative AI Innovation Center. With over 10 years of experience in Deep Learning and Generative AI, Parmida brings deep expertise in AI and customer focused solutions. Parmida has led and co-authored highly impactful scientific papers focused on domains such as computer vision, explainability, video and image generation. With a strong focus on scientific practices, Parmida helps customers with practical design of systems using generative AI in robust and scalable pipelines.

### Dan Volk

**Dan Volk**
is a Senior Data Scientist at the AWS Generative AI Innovation Center. He has 10 years of experience in machine learning, deep learning, and time series analysis, and holds a Master’s in Data Science from UC Berkeley. He is passionate about transforming complex business challenges into opportunities by leveraging cutting-edge AI technologies.

### Paul Amadeo

**Paul Amadeo**
is a seasoned technology leader with over 30 years of experience spanning artificial intelligence, machine learning, IoT systems, RF design, optics, semiconductor physics, and advanced engineering. As Technical Lead for Physical AI in the AWS Generative AI Innovation Center, Paul specializes in translating AI capabilities into tangible physical systems, guiding enterprise customers through complex implementations from concept to production. His diverse background includes architecting computer vision systems for edge environments, designing robotic smart card manufacturing technologies that have produced billions of devices globally, and leading cross-functional teams in both commercial and defense sectors. Paul holds an MS in Applied Physics from the University of California, San Diego, a BS in Applied Physics from Caltech, and holds six patents spanning optical systems, communication devices, and manufacturing technologies.

### Sri Elaprolu

**Sri Elaprolu**
is Director of the AWS Generative AI Innovation Center, where he leads a global team implementing cutting-edge AI solutions for enterprise and government organizations. During his 13-year tenure at AWS, he has led ML science teams partnering with global enterprises and public sector organizations. Prior to AWS, he spent 14 years at Northrop Grumman in product development and software engineering leadership roles. Sri holds a Master’s in Engineering Science and an MBA.