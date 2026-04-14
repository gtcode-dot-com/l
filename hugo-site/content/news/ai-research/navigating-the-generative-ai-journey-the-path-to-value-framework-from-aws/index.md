---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-14T20:15:36.271757+00:00'
exported_at: '2026-04-14T20:15:38.459646+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/navigating-the-generative-ai-journey-the-path-to-value-framework-from-aws
structured_data:
  about: []
  author: ''
  description: In this post, we introduce the Generative AI Path-to-Value (P2V) framework,
    a structured approach to help you move generative AI initiatives from concept
    to production and sustained value creation.
  headline: 'Navigating the generative AI journey: The Path-to-Value framework from
    AWS'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/navigating-the-generative-ai-journey-the-path-to-value-framework-from-aws
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Navigating the generative AI journey: The Path-to-Value framework from AWS'
updated_at: '2026-04-14T20:15:36.271757+00:00'
url_hash: ed5f08c348f7fa2a70843387790ce8ebe4d95de5
---

Generative AI is reshaping how organizations approach productivity, customer experiences, and operational capabilities. Across industries, teams are experimenting with generative AI to unlock new ways of working. Many of these efforts produce compelling proofs of concept (POC) that demonstrate technical feasibility. The real challenge begins after those early wins. Although POCs frequently demonstrate technical feasibility, organizations often struggle to translate them into production-ready systems that deliver measurable business value. The journey from concept to production, and from production to sustained value creation, introduces challenges across technical, organizational, and governance dimensions.

The
**Generative AI Path-to-Value (P2V) framework**
was created to address this gap. It provides a mental model and practical guide to help organizations systematically move generative AI initiatives from ideation and experimentation to production at scale. The goal is to create durable business value.

## The fundamental challenge

The core challenge with generative AI adoption is not innovation velocity. Initial pilots frequently show strong promise and generate enthusiasm across teams. However, when organizations attempt to operationalize these solutions, progress slows. Data access becomes constrained by security and privacy requirements. Integration with existing enterprise systems introduces unexpected complexity. Governance, compliance, and approval processes add friction. At the same time, teams struggle to define consistent success metrics that connect generative AI capabilities to business outcomes. Without a structured approach, these challenges compound. Many initiatives stall between prototype, production readiness, and value realization. What organizations need is a framework that addresses these issues deliberately and holistically. The right framework reduces friction while accelerating time to value.

## Four major categories of barriers

When organizations move generative AI from experimentation toward production and value creation, challenges consistently fall into four major categories.

* **Value:**
  Many generative AI initiatives lack clearly defined ROI or measurable business outcomes. Without concrete success criteria, it becomes difficult to justify continued investment or prioritize efforts.
* **Risk:**
  Concerns around legal exposure, data privacy, security vulnerabilities, and reputational impact create resistance. The evolving regulatory landscape for AI further increases uncertainty around compliance requirements.
* **Technology:**
  Productionizing generative AI introduces technical challenges beyond model selection. Integration with existing systems, infrastructure requirements, data quality issues, and operational complexity (observability, scalability, resilience) are often underestimated. Additionally, evaluation and validation remain critical challenges before production. Deployment teams must establish metrics, build test datasets, measure performance across scenarios, and implement continuous monitoring to maintain quality. FinOps considerations for cost optimization and resource management further compound these technical complexities.
* **People:**
  Adoption is slowed by resistance to change, skill gaps within teams, uncertainty around how generative AI affects roles and responsibilities, and challenges in finding or developing the right expertise.

These barriers rarely appear in isolation. Addressing one without the others often shifts the problem rather than solving it.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/09/ML-18780-1.png)

## The Generative AI Path-to-Value framework

The
**Generative AI Path-to-Value (P2V) framework**
serves as a shared mental model and roadmap for both technical and non-technical stakeholders. It provides lifecycle guidance for generative AI workloads from early ideation, through production-ready implementation, to sustained value realization. Rather than treating production as the end goal, the framework positions production readiness as a milestone on the path to business impact. Its purpose is to help organizations remove the most common blockers that prevent generative AI initiatives from scaling successfully.

### Framework structure

The framework translates real-world implementation experience into practical guidance through three core components:

* **Pillars**
  , which represent the key areas that must be addressed
* **Checkpoints**
  , which clarify what readiness looks like at different stages
* **Guidance and artifacts**
  , which provide concrete tools to support execution

This structure helps organizations move beyond understanding challenges and toward consistently resolving them as they progress from concept to value.

## An interconnected system, not a linear process

The P2V framework is not intended to be applied as a linear, step-by-step process. Generative AI adoption rarely progresses in a straight line. Instead, organizations should apply the framework flexibly and asynchronously, with multiple pillars addressed in parallel. For example, teams can simultaneously build technical capabilities while establishing governance guardrails and developing business cases for different use cases. This parallel approach can significantly accelerate the overall path to production and value. At the center of the framework is the end-to-end generative AI journey, guiding organizations from initial concept through production deployment and ultimately to measurable value realization. The P2V journey relies on interconnected pillars that require continuous attention across all stages of generative AI adoption. Organizations often engage multiple pillars in parallel, depending on their maturity and constraints. This flexible, holistic approach helps make sure that the critical aspects of generative AI implementation are addressed. Organizations can adapt the framework to their context. However, they should prioritize foundational pillars (business case, data strategy, security, and legal compliance) before advancing to PoC or MVP stages.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/09/ML-18780-2.png)

## Key pillars of the P2V framework

The P2V framework organizes the journey into a set of foundational pillars. Each pillar defines a critical dimension that must be addressed to move generative AI initiatives from experimentation to production and into sustained business value. Each pillar combines intent with execution by explaining why the area matters and outlining the key focus areas that teams must address. Organizations should work through each pillar systematically even if some require only a brief assessment, reviewing each through its specific lens helps make sure critical gaps aren’t overlooked. Future posts will explore each pillar in greater depth.

### Business case and value creation

In a competitive landscape, generative AI investments must demonstrate clear returns. This pillar focuses on defining and measuring business outcomes so initiatives move beyond proofs of concept and into production solutions that deliver quantifiable value. The emphasis is on making success measurable and helping make sure that investments yield meaningful results.

**Key focus areas:**

* **Business value template**
  – Create a structured template to document the value proposition and expected outcomes
* **Cost decision matrix**
  – Establish a framework to evaluate implementation costs against potential returns. Apply cost optimization techniques including prompt caching, knowledge distillation, context management, model tiering via intelligent routing, batch inference for non-urgent workloads (available at reduced cost), and provisioned throughput for production traffic.
* **Business KPIs and impact quantification**
  – Define metrics to measure business impact and performance
* **Benefits and success ROI metrics**
  – Track return on investment and validate realized benefits
* **Measurable business outcomes**
  – Define and monitor concrete business results over time

### Resources

1. [Why model choice matters: Flexible AI unlocks freedom to innovate](https://aws.amazon.com/blogs/aws-insights/why-model-choice-matters-flexible-ai-unlocks-freedom-to-innovate/)
2. [Transformative AI starts with clear use cases](https://aws.amazon.com/ai/generative-ai/use-cases/)
3. [Generative AI ATLAS – Business Value and use cases](https://awslabs.github.io/generative-ai-atlas/topics/1_0_generative_ai_fundamentals/1_2_business_value_and_use_cases/1_2_business_value_and_use_cases.html)
4. [Delivering Business Value through Generative AI: Use Cases and Insights for CxOs](https://aws.amazon.com/blogs/apn/delivering-business-value-through-generative-ai-use-cases-and-insights-for-cxos/)
5. [Optimize for cost, latency, and accuracy](https://aws.amazon.com/bedrock/cost-optimization/)
6. [Lower cost and latency for AI using Amazon ElastiCache as a semantic cache with Amazon Bedrock](https://aws.amazon.com/blogs/database/lower-cost-and-latency-for-ai-using-amazon-elasticache-as-a-semantic-cache-with-amazon-bedrock/)
7. [Build a read-through semantic cache with Amazon OpenSearch Serverless and Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/build-a-read-through-semantic-cache-with-amazon-opensearch-serverless-and-amazon-bedrock/)
8. [Effective cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock)
9. [Optimize LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)

### Data strategy

Quality data is the foundation of successful AI. This pillar emphasizes integrating high-quality data from enterprise knowledge systems, rather than relying on increasingly complex models. By focusing on data quality, governance, and integration, organizations can often achieve better outcomes with lower technical complexity, augmented by synthetic data where it meaningfully extends existing information assets.

**Key focus areas:**

* **Data collection and preparation**
  – Establish guidelines for gathering and preprocessing relevant data
* **Data quality and integrity**
  – Define standards to support data accuracy and reliability
* **Data foundations and governance**
  – Create frameworks for managing and governing data assets
* **Golden datasets**
  – Define criteria for benchmark datasets used for training and evaluation
* **Data pipelines**
  – Build efficient data processing workflows
* **Enterprise knowledge integration**
  – Connect generative AI systems to organizational knowledge sources
* **Synthetic data generation**
  – Apply techniques to augment training data where appropriate
* **Data-centric pipelines**
  – Maintain data quality throughout the AI lifecycle

### Resources

1. [Data security, lifecycle, and strategy for generative AI applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/introduction.html)
2. [Your data, your generative AI differentiator](https://aws.amazon.com/ai/generative-ai/data/)

### Security, compliance, and governance

As generative AI becomes mission-critical to business operations, responsible implementation is essential. This pillar establishes the guardrails required to scale generative AI confidently, so that organizations can build security, compliance, and governance from the start rather than adding them after deployment. The focus is on enabling progress while helping organizations navigate evolving regulatory and enterprise requirements.

**Key focus areas:**

* **Access control**
  – Define protocols for managing system and data access permissions
* **Guardrails**
  – Implement safety mechanisms to help avoid misuse or unintended consequences
* **Authorization patterns**
  – Apply consistent patterns to secure models, endpoints, and data
* **Security scaling**
  – Upgrade POC-level controls to production-level security protocols
* **Industry-specific considerations**
  – Help address sector-specific regulatory factors and standards
* **AI ethics council framework**
  – Establish structured oversight and review committees
* **Self-governance frameworks**
  – Define internal policies for responsible AI development
* **Automated AI risk management**
  – Continuously monitor and mitigate security and compliance risks

### Resources

1. [AWS Security Reference Architecture for AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html)
2. [Security for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html)
3. [The Agentic AI Security Scoping Matrix: A framework for securing autonomous AI systems](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/)

### Choice evaluation

Selecting the right generative AI approach requires more than comparing technical specifications. This pillar aligns technology decisions with business objectives, providing clear guidance on implementation strategies and resource optimization to maximize return on AI investments at enterprise scale.

**Key focus areas:**

* **Model overview and comparison**
  – Evaluate different model architectures using consistent criteria
* **Decision trees**
  – Apply structured approaches to technology selection decisions
* **Migration strategy**
  – Plan transitions between generative AI approaches as requirements evolve
* **Multimodal architecture**
  – Assess considerations for systems that handle multiple data types
* **Fine-tuning vs. RAG decision matrix**
  – Select the appropriate customization approach based on use case needs

### Resources

1. [Beyond the basics: A comprehensive foundation model selection framework for generative AI](https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/)

### Building trust in AI: Responsible foundations and implementations

Responsible AI is now a core requirement for enterprise adoption. This pillar establishes guardrails that address regulatory compliance while building trust with stakeholders. Organizations that operationalize responsible AI early can help accelerate approvals and strengthen their competitive position through disciplined, transparent practices.

**Key focus areas:**

* **Model considerations**
  – Evaluate implications of model sourcing and ownership
* **Privacy patterns**
  – Implement privacy-preserving techniques across data and inference workflows
* **Responsible use considerations**
  – Identify and address responsible AI implications of generative AI use cases
* **Bias mitigation**
  – Detect and reduce algorithmic bias in data and models
* **Transparency and interpretability**
  – Support the ability to understand and explain AI-driven decisions
* **Guidelines and policies**
  – Define standards for responsible AI usage
* **AI governance council and framework**
  – Provide governance and oversight structures
* **Automated AI risk management**
  – Continuously monitor responsible use and compliance risks

Resources

1. [Transform responsible AI from theory into practice](https://aws.amazon.com/ai/responsible-ai/)
2. [Announcing the AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/responsible-ai-lens.html)

### Development lifecycle

Delivering generative AI successfully in production requires selecting the right technical approach without getting lost in complexity. This pillar provides clear guidance for evaluation, architecture, and implementation so that technical decisions remain aligned with business outcomes and cost efficiency as systems scale. The emphasis is on disciplined development practices that allow teams to adopt advanced capabilities while maintaining control, repeatability, and measurable impact.

**Key focus areas:**

* **Evaluation metrics and testing**
  – Define standards for measuring model performance and validating behavior
  + **Evaluation process**
    – Establish structured testing and validation approaches
  + **Online and offline evaluation**
    – Apply different evaluation methods for pre-production testing versus live usage
  + **LLM-assisted evaluation**
    – Use techniques such as
    *LLMs acting as evaluators*
    to assess response quality at scale
  + **Application-specific metrics**
    – Define metrics aligned to the use case, such as task completion or answer accuracy
  + **Human-in-the-loop:**
    Integrate human judgment across the AI lifecycle to help improve accuracy, safety, and alignment.
* **Model architecture selection**
  – Apply decision frameworks to guide technical implementation choices
  + **Task and output modality**
    – Select architectures based on target outputs, such as text-only or multimodal responses
  + **Task type and pre-training data**
    – Choose approaches based on the nature of the task and available data
  + **Domain-specific considerations**
    – Account for industry-specific requirements and constraints
  + **Infrastructure and resources**
    – Plan infrastructure and optimize resource usage for cost and latency
  + **Multimodal architecture**
    – Support scenarios involving multiple input or output types, such as text and images
* **Implementation guidelines**
  – Establish best practices for deploying generative AI systems
  + **Integration approaches**
    – Connect generative AI components with existing enterprise systems and workflows
  + **Model development**
    – Apply consistent standards for model building and refinement
  + **Optimization considerations**
    – Improve performance and efficiency without increasing operational cost

### Resources

1. [Agentic AI development from prototype to production](https://kiro.dev/"%20\t%20"_blank)
2. [Customize your applications](https://aws.amazon.com/bedrock/customize/)
3. [Announcing the AWS Well-Architected Generative AI Lens](https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/)

### Operational excellence

The difference between successful generative AI deployments and stalled experiments comes down to operational execution. This pillar focuses on running generative AI systems reliably in production through continuous optimization, KPI monitoring, and disciplined cost management. Strong feedback mechanisms help systems improve over time while maintaining predictable performance. The emphasis is on treating generative AI as a long-running production workload rather than a one-time deployment.

**Key focus areas:**

* **Operations**
  – Establish guidelines for day-to-day production management
  + **Load distribution and elasticity**
    – Handle variable demand, such as spikes in inference traffic
  + **Monitoring and logging**
    – Maintain visibility into system behavior and failures
  + **Automated deployment**
    – Streamline updates to models, prompts, and configurations
  + **Infrastructure management**
    – Administer and optimize runtime resources
  + **Performance and scalability**
    – Maintain consistent latency and throughput at scale
* **Hallucination detection and mitigation**
  – Employ mathematically sound verification and lifecycle management to move beyond simple guardrails, helping improve factual accuracy and long-term model reliability.
* **Model maintenance and improvement**
  – Continuously refine models based on production signals
* **Resilience and recovery**
  – Define protocols for handling failures and service disruptions
* **Continuous optimization**
  – Iteratively improve performance, quality, and efficiency
* **Observability**
  – Maintain end-to-end visibility across data, models, and applications
* **Production KPI monitoring**
  – Track operational metrics that reflect system health and usage
* **Feedback loop implementation**
  – Incorporate user and system feedback into ongoing improvements
* **FinOps and cost management**
  – Monitor and optimize operational expenses to control run costs

### Resources

1. [Generative AI Lifecycle Operational Excellence framework on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/introduction.html)
2. [Move your AI agents from proof of concept to production with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/move-your-ai-agents-from-proof-of-concept-to-production-with-amazon-bedrock-agentcore/)
3. [Announcing the AWS Well-Architected Generative AI Lens](https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/)
4. [Reducing hallucinations in LLM agents with a verified semantic cache using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/reducing-hallucinations-in-llm-agents-with-a-verified-semantic-cache-using-amazon-bedrock-knowledge-bases/)
5. [Minimize AI hallucinations and deliver up to 99% verification accuracy with Automated Reasoning checks](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/)
6. [Zero-knowledge LLM hallucination detection and mitigation through fine-grained cross-model consistency](https://www.amazon.science/publications/zero-knowledge-llm-hallucination-detection-and-mitigation-through-fine-grained-cross-model-consistency)

### Upskilling and training

Sustained generative AI success depends on people as much as technology. This pillar focuses on building the skills and organizational readiness required to adopt, operate, and scale generative AI effectively. The goal is to help make sure that technical capabilities translate directly into business value. By aligning training with real use cases and measuring impact, organizations can drive adoption while maintaining a clear link between enablement efforts and outcomes.

**Key focus areas:**

* **Skill-building self-training courses**
  – Develop structured curricula to build generative AI competencies
* **Industry- and use-case-specific guidance**
  – Tailor training to relevant business and technical contexts
* **Business value realization methodologies**
  – Connect newly acquired skills to measurable outcomes
* **ROI measurement frameworks**
  – Quantify the impact of training investments
* **Change management strategies**
  – Drive adoption and embed generative AI into daily workflows

### Resources

1. [Generative AI ATLAS](https://awslabs.github.io/generative-ai-atlas/index.html"%20\t%20"_blank)
   – ATLAS is a comprehensive knowledge hub providing verified technical content and guidance for generative AI implementation, spanning from basics to advanced deployment strategies.

## The Generative AI adoption journey

The
**Generative AI Path-to-Value (P2V) framework**
, as a mental model, simplifies the generative AI adoption journey. It provides a flexible and interconnected system that guides organizations through critical phases, from initial concept development through production-ready implementation to sustainable value creation. As an industry-agnostic, use-case-agnostic, and technology-agnostic framework, it can be applied across diverse organizational contexts and scenarios.

Rather than optimizing for a single stage, the framework systematically addresses the dimensions that determine long-term success: value creation, risk management, technical rigor, and people transformation. Organizations can enter the journey when they choose and progress at their own pace while maintaining alignment with business objectives and responsible AI practices.

The P2V framework is intentionally not a rigid, waterfall-style approach. It serves as both a proactive guide and a diagnostic tool helping organizations struggling with production deployment or value realization to quickly identify gaps and develop customized paths forward. Through its pillars, the framework offers prescriptive guidance that allows teams to focus on the areas most relevant to their current state. Whether an organization is discovering new use cases, reassessing prioritization, hardening production deployments, or scaling adoption, the framework emphasizes outcomes and provides clear direction at each stage.

The adoption journey visualization reinforces this approach by highlighting the framework’s interconnected elements and the significance of outcomes at every phase. By making these dependencies explicit, the model helps teams navigate complexity without losing sight of what ultimately matters: delivering sustained business value.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/09/ML-18780-3.png)

## Meet Amazon Bedrock

[Amazon Bedrock](https://aws.amazon.com/bedrock/)
(the service for building generative AI applications and agents at production scale) helps organizations execute the Path-to-Value journey by streamlining the transition from concept to production. It provides a unified environment for generative AI implementation that addresses key P2V elements such as model access, security, and scalability.

By offering managed infrastructure, built-in governance controls, and enterprise integration capabilities, Amazon Bedrock can reduce operational friction and accelerate production readiness. This allows teams to focus less on undifferentiated infrastructure concerns and more on applying the P2V framework to deliver measurable business outcomes.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/09/ML-18780-4.png)

## Reimagining how generative AI applications are built

The P2V framework addresses what organizations need to get right across the generative AI journey, but the speed of that journey depends heavily on how teams build. Traditional software development practices, designed for human-driven sequential processes, often become the hidden bottleneck that stalls initiatives between proof of concept and production. The
[AI-Driven Development Lifecycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
(AI-DLC) addresses this by positioning AI as a central collaborator rather than just a coding assistant, reimagining the entire lifecycle around a powerful pattern: AI helps create plans, seeks clarification, and supports implementation, while humans make the critical decisions. AI-DLC’s three phases (Inception, Construction, and Operations) mirror the P2V journey from concept through production to sustained value, with the potential to compress development cycles from weeks to hours while keeping technical work aligned with business outcomes and governance requirements. Each phase builds persistent context that carries forward, helping reduce the information loss and rework that commonly stall initiatives between stages. Organizations applying the P2V framework can adopt AI-DLC as the execution engine for their development lifecycle, helping turn framework guidance into faster, higher-quality delivery without compromising the human oversight that production-scale generative AI requires. To dive deeper, watch the full session from AWS re:Invent
[Introducing AI-Driven Development Lifecycle (AI-DLC)](https://www.youtube.com/watch?v=1HNUH6j5t4A)

## Conclusion

The Generative AI Path-to-Value framework offers a comprehensive mental model for navigating the complexities of generative AI adoption. By providing guidance across the complete journey, from concept to production-ready to value creation, the framework helps organizations address common challenges at each stage. For organizations with stalled generative AI initiatives, the framework offers targeted guidance to diagnose blockers and tailor a path forward. It helps make sure the many aspects of successful implementation are considered. As generative AI continues to evolve, this mental model can serve as a resource for organizations seeking to use this technology at scale.

To learn more about implementing generative AI with the Path-to-Value framework, contact your AWS account team or explore the following resources.

---

## About the authors

### Nitin Eusebius

Nitin Eusebius is a Principal Solutions Architect and Generative AI Tech Lead at Amazon Web Services (AWS). He works with executive and technology leaders on enterprise transformation, cloud strategy, and AI Engineering, including the adoption of Generative and Agentic AI. With over 20 years of experience across enterprise technology, cloud architecture, and large-scale digital platforms, Nitin helps organizations design secure, resilient, and production-ready systems. He leads strategic initiatives, contributes to AWS thought leadership and blogs, and is a frequent speaker at AWS re:Invent, reInforce, and global AWS Summits. What differentiates him is the combination of deep hands-on architecture, AI systems thinking, executive engagement, and the ability to turn fast-moving technology into practical, production-ready systems.

### Akash Bhatia

Akash Bhatia is a Principal Solutions Architect at Amazon Web Services (AWS), where he partners with executive and technology leaders on cloud strategy, advanced architecture, and AI engineering. With over 20 years of experience spanning enterprise and digital-native organizations across both private and public sectors, Akash has helped Fortune 100 companies and high-growth startups navigate complex challenges and accelerate their cloud journeys through large-scale enterprise transformation. His current focus includes model development, customization, and the adoption of Generative and Agentic AI. Prior to AWS, Akash held leadership roles at Hyundai and Toyota, driving strategy and technology efforts in advanced mobility, autonomous systems, and new market development. That foundation in product leadership and building at-scale scale systems gives him a distinctive perspective in his current role.

### Nipun Chagari

Nipun Chagari is a Sr Manager, Solutions Architecture based in the Bay Area, CA. Nipun leads next generation cloud architectures and generative AI initiatives, providing technical advisory to enterprise customers. He helps organizations adopt Serverless technology to modernize applications and achieve business objectives. Apart from work, he enjoys pickleball and traveling.

### Kiran Lakkireddy

Kiran Lakkireddy is a Sr. SA Manager at AWS specializing in Enterprise Architecture and AI Strategy & Governance. He has deep expertise in Financial Services, Benefits Management, and HR Services, leading teams that guide enterprise customers through complex business and technology transformations. Kiran regularly advises customer security leaders on responsible AI strategies, helping organizations safely adopt Generative and Agentic AI while maintaining the highest standards of security, compliance, and governance.

### Vasile Balan

Vasile Balan is the Head of Solutions Architecture for Advertising & Marketing and Travel & Hospitality at AWS, bringing over 25 years of global technology leadership. He built one of the earliest enterprise public clouds in 2009 and has since championed cloud-driven transformation across multiple industries. At AWS, he developed the GenAI Path-to-Value framework, helping enterprise customers accelerate ROI from generative AI investments, and leads Agentic AI initiatives driving adoption across key industry verticals. Vasile is a passionate car enthusiast – when he’s not geeking out over the latest AI innovations, you’ll find him in the garage tinkering with his cars or on the track extracting maximum performance from every corner. He is based in Palm Beach, FL.