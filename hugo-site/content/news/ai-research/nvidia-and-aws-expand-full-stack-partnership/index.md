---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-03T00:03:20.197254+00:00'
exported_at: '2025-12-03T00:03:22.801967+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/aws-partnership-expansion-reinvent
structured_data:
  about: []
  author: ''
  description: At AWS re:Invent, NVIDIA and AWS expanded their strategic collaboration
    with new technology integrations across interconnect technology, cloud infrastructure,
    open models and physical AI.
  headline: NVIDIA and AWS Expand Full-Stack Partnership, Providing the Secure, High-Performance
    Compute Platform Vital for Future Innovation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/aws-partnership-expansion-reinvent
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: NVIDIA and AWS Expand Full-Stack Partnership, Providing the Secure, High-Performance
  Compute Platform Vital for Future Innovation
updated_at: '2025-12-03T00:03:20.197254+00:00'
url_hash: bbc2a328a5c45183cb4a49e863ba6082bfa0ba5c
---

At AWS re:Invent, NVIDIA and Amazon Web Services expanded their strategic collaboration with new technology integrations across interconnect technology, cloud infrastructure, open models and physical AI.

As part of this expansion, AWS will support
[NVIDIA NVLink Fusion](https://www.nvidia.com/en-us/data-center/nvlink-fusion/)
— a platform for custom AI infrastructure — for deploying its custom-designed silicon, including next-generation Trainium4 chips for inference and agentic AI model training, Graviton CPUs for a broad range of workloads and the Nitro System virtualization infrastructure.

Using NVIDIA NVLink Fusion,
[AWS will combine](https://developer.nvidia.com/blog/aws-integrates-ai-infrastructure-with-nvidia-nvlink-fusion-for-trainium4-deployment/)
NVIDIA NVLink scale-up interconnect and the NVIDIA MGX rack architecture with AWS custom silicon to increase performance and accelerate time to market for its next-generation cloud-scale AI capabilities.

AWS is designing Trainium4 to integrate with NVLink and NVIDIA MGX, the first of a multigenerational collaboration between NVIDIA and AWS for NVLink Fusion.

AWS has already deployed MGX racks at scale with NVIDIA GPUs. Integrating NVLink Fusion will allow AWS to further simplify deployment and systems management across its platforms.

AWS can also harness the NVLink Fusion supplier ecosystem, which provides all the components required for full rack-scale deployment, from the rack and chassis, to power-delivery and cooling systems.

By supporting AWS’s Elastic Fabric Adapter and Nitro System, the NVIDIA Vera Rubin architecture on AWS will give customers robust networking choices while maintaining full compatibility with AWS’s cloud infrastructure and accelerating new AI service rollout.

“GPU compute demand is skyrocketing — more compute makes smarter AI, smarter AI drives broader use and broader use creates demand for even more compute. The virtuous cycle of AI has arrived,” said Jensen Huang, founder and CEO of NVIDIA. “With NVIDIA NVLink Fusion coming to AWS Trainium4, we’re unifying our scale-up architecture with AWS’s custom silicon to build a new generation of accelerated platforms. Together, NVIDIA and AWS are creating the compute fabric for the AI industrial revolution — bringing advanced AI to every company, in every country, and accelerating the world’s path to intelligence.”

“AWS and NVIDIA have worked side by side for more than 15 years, and today marks a new milestone in that journey,” said Matt Garman, CEO of AWS. “With NVIDIA, we’re advancing our large-scale AI infrastructure to deliver customers the highest performance, efficiency and scalability. The upcoming support of NVIDIA NVLink Fusion in AWS Trainium4, Graviton and the Nitro System will bring new capabilities to customers so they can innovate faster than ever before.”

## **Convergence of Scale and Sovereignty**

AWS has expanded its accelerated computing portfolio with the NVIDIA Blackwell architecture, including NVIDIA HGX B300 and NVIDIA GB300 NVL72 GPUs, giving customers immediate access to the industry’s most advanced GPUs for training and inference. Availability of NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs, designed for visual applications, on AWS is expected in the coming weeks.

These GPUs form part of the AWS infrastructure backbone powering AWS AI Factories, a new AI cloud offering that will provide customers around the world with the dedicated infrastructure they need to harness advanced AI services and capabilities in their own data centers, operated by AWS, while also letting customers maintain control of their data and comply with local regulations.

NVIDIA and AWS are committing to deploy sovereign AI clouds globally and bring the best of AI innovation to the world. With the launch of AWS AI Factories, the companies are providing secure, sovereign AI infrastructure to deliver unprecedented computing capabilities for organizations around the world while meeting increasingly rigorous sovereign AI requirements.

For public sector organizations, AWS AI Factories will transform the federal supercomputing and AI landscape. AWS AI Factories customers will be able to seamlessly integrate AWS’s industry-leading cloud infrastructure and services — known for its reliability, security and scalability — with NVIDIA Blackwell GPUs and the full-stack NVIDIA accelerated computing platform, including
[NVIDIA Spectrum-X](https://www.nvidia.com/en-us/networking/spectrumx/)
Ethernet switches.

The unified architecture will ensure customers can access advanced AI services and capabilities, as well as train and deploy massive models, while maintaining absolute control of proprietary data and full compliance with local regulatory frameworks.

## **NVIDIA Nemotron Integration With Amazon Bedrock Expands Software Optimizations**

Beyond hardware, the partnership expands integration of NVIDIA’s software stack with the AWS AI ecosystem.
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
open models are now integrated with
[Amazon Bedrock](https://aws.amazon.com/blogs/aws/amazon-bedrock-adds-fully-managed-open-weight-models)
, enabling customers to build generative AI applications and agents at production scale. Developers can access Nemotron Nano 2 and Nemotron Nano 2 VL to build specialized agentic AI applications that process text, code, images and video with high efficiency and accuracy.

The integration makes high-performance, open NVIDIA models instantly accessible via Amazon Bedrock’s serverless platform where customers can rely on proven scalability and zero infrastructure management. Industry leaders
[CrowdStrike](https://www.crowdstrike.com/en-us/blog/crowdstrike-uses-nvidia-nemotron-aws-power-agentic-security/)
and
[BridgeWise](https://bridgewise.com/press/nvidia-amazon)
are the first to use the service to deploy specialized AI agents.

## **NVIDIA Software on AWS Simplifies Developer Experience**

NVIDIA and AWS are also co-engineering at the software layer to accelerate the data backbone of every enterprise.
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
now offers serverless GPU acceleration for vector index building, powered by
[NVIDIA cuVS](https://developer.nvidia.com/cuvs?sortBy=developer_learning_library%2Fsort%2Ftitle%3Aasc)
, an open-source library for GPU-accelerated vector search and data clustering. This milestone represents a fundamental shift to using GPUs for unstructured data processing, with early adopters seeing up to 10x faster vector indexing at a quarter of the cost.

These dramatic gains reduce search latency, accelerate writes and unlock faster productivity for dynamic AI techniques like retrieval-augmented generation by delivering the right amount of GPU power precisely when it’s needed. AWS is the first major cloud provider to offer serverless vector indexing with NVIDIA GPUs.

Production-ready AI agents require performance visibility, optimization and scalable infrastructure. By combining
[Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)
for agent development and orchestration, the
[NVIDIA NeMo Agent Toolkit](https://developer.nvidia.com/nemo-agent-toolkit)
for deep profiling and performance tuning, and
[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
for secure, scalable agent infrastructure, organizations can empower developers with a complete, predictable path from prototype to production.

This expanded support builds on AWS’s existing integrations with NVIDIA technologies — including
[NVIDIA NIM](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)
microservices and frameworks like
[NVIDIA Riva](https://www.nvidia.com/en-us/ai-data-science/products/riva/)
and
[NVIDIA BioNeMo](https://www.nvidia.com/en-us/clara/biopharma/)
, as well as model development tools integrated with Amazon SageMaker and Amazon Bedrock — that enable organizations to deploy agentic AI, speech AI and scientific applications faster than ever.

## **Accelerating Physical AI With AWS**

Developing
[physical AI](https://www.nvidia.com/en-us/glossary/generative-physical-ai/)
demands high-quality and diverse datasets for training robot models, as well as frameworks for testing and validation in simulation before real-world deployment.

[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
world foundation models (WFMs) are now available as
[NVIDIA NIM microservices on Amazon EKS](https://aws.amazon.com/blogs/hpc/running-nvidia-cosmos-world-foundation-models-on-aws/)
, enabling real-time
[robotics control and simulation workloads](https://nvidia-cosmos.github.io/cosmos-cookbook/index.html)
with seamless reliability and cloud-native efficiency. For batch-based tasks and offline workloads such as large-scale
[synthetic data generation](https://www.nvidia.com/en-us/use-cases/synthetic-data/)
, Cosmos WFMs are also available on AWS Batch as containers.

Cosmos-generated world states can then be used to train and validate robots using open-source simulation and learning frameworks such as
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)
and
[Isaac Lab](https://developer.nvidia.com/isaac/lab)
.

Leading robotics companies such as Agility Robotics, Agile Robots, ANYbotics, Diligent Robotics, Dyna Robotics, Field AI, Haply Robotics, Lightwheel, RIVR and Skild AI are using the NVIDIA Isaac platform with AWS for use cases ranging from collecting, storing and processing robot-generated data to training and simulation for scaling robotics development.

## **Sustained Collaboration**

Underscoring years of continued collaboration, NVIDIA earned the AWS Global GenAI Infrastructure and Data Partner of the Year award, which recognizes top technology partners with the Generative AI Competency that support vector embeddings, data storage and management or synthetic data generation in multiple types and formats.

*Learn more about NVIDIA and AWS’s collaboration and join sessions at*
[*AWS re:Invent*](https://www.nvidia.com/en-us/events/aws-reinvent/)
*, running through Friday, Dec. 5, in Las Vegas.*