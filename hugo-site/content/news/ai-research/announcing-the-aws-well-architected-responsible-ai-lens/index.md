---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-20T00:00:18.535221+00:00'
exported_at: '2025-11-20T00:00:21.583095+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-the-aws-well-architected-responsible-ai-lens
structured_data:
  about: []
  author: ''
  description: Today, we're announcing the AWS Well-Architected Responsible AI Lens—a
    set of thoughtful questions and corresponding best practices that help builders
    address responsible AI concerns throughout development and operation.
  headline: Announcing the AWS Well-Architected Responsible AI Lens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/announcing-the-aws-well-architected-responsible-ai-lens
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Announcing the AWS Well-Architected Responsible AI Lens
updated_at: '2025-11-20T00:00:18.535221+00:00'
url_hash: ed8201241e297105ff8835bc44f93fbb18cd663e
---

As AI applications grow more complex, many builders struggle to appropriately and responsibly balance AI benefits and risks. Few resources exist that help non-experts articulate and resolve the key design decisions they must make. However, it doesn’t have to be this way. Today, we’re announcing the
[AWS Well-Architected Responsible AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/responsible-ai-lens.html)
—a set of thoughtful questions and corresponding best practices that help builders address responsible AI concerns throughout development and operation. Based on our experience helping customers run hundreds of thousands of AI workloads and on the experience of responsible AI scientists, this lens provides clear, actionable guidance throughout the AI lifecycle. By systematically addressing responsible AI considerations early in development, teams can reduce costly late-stage changes and accelerate their path to trusted production systems.

## What is the Responsible AI Lens?

The
[Responsible AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/responsible-ai-lens.html)
guides builders through the end-to-end lifecycle of building a targeted AI application (not a frontier model). It is designed to help builders make informed decisions that balance business and technical requirements and speed up the deployment of trusted AI systems.

The Responsible AI Lens is based on three design principles:

* **Responsible by design**
  : Consider
  [responsible AI dimensions](https://aws.amazon.com/ai/responsible-ai/)
  throughout the AI lifecycle from design through operations, while emphasizing identifying and resolving potential issues as early as possible in the lifecycle.
* **Scope use cases narrowly**
  : Develop the specifications of an AI system by working backwards from the AI use case (in other words, the problem to be solved). The narrower the scope of the use case, the simpler the time you will have identifying, mitigating, and testing risks that the AI use case and its solution might pose to stakeholders.
* **Follow the science**
  : Use practical, science-backed guidance to assess and mitigate risks and support evidence-based release decisions.

The graphic below shows the high-level Design, Develop, Operate phases and their sub-categories.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/ml-19968.png)

## How to use the Responsible AI Lens

The Responsible AI Lens is organized into eight focus areas covering different steps in the AI lifecycle. Each focus area offers key questions to consider and provides best practices that can help you resolve the questions. The best practices for a given question cover relevant responsible AI dimensions such as fairness, explainability, privacy, security, safety, controllability, veracity, robustness, and transparency. Each best practice includes guidance, implementation considerations, and resources.

The eight focus areas help to:

* **Describe use case**
  – Define the specific problem being solved, validate the need for AI, and identify stakeholders.
* **Assess benefits and risks**
  – Identify the potential benefits and risks of the use case across stakeholder groups.
* **Define release criteria**
  – Set clear, testable criteria for AI system readiness.
* **Design datasets**
  – Create high-quality datasets for training, evaluation, and operations.
* **Design the AI system**
  – Implement responsible behavior directly into system design.
* **Make an evidence-based release**
  **decision**
  – Assess actual benefits and residual risks to make informed release decisions based on evidence.
* **Provide downstream guidance and transparency**
  – Support users and other downstream stakeholders with clear explanations of intended usage and limitations.
* **Manage post-release monitoring and decommissioning**
  – Monitor system performance and respond to issues.

Since AI development is often iterative and nonlinear, you don’t need to work through the focus areas sequentially. However, we recommend you first review the guidance in total, then work through the areas in whatever order fits your situation.

## Who should use the Responsible AI Lens?

The Responsible AI Lens serves three audiences who play complementary roles in developing and deploying responsible AI systems:

* **AI builders**
  , including engineers, product managers, and scientists, who develop and deploy AI systems. Builders get guidance on how to structure their work to identify and optimize benefit and risk tradeoffs specific to AI applications.
* **AI technical leaders**
  who oversee teams building AI systems and implement enterprise-wide responsible AI practices. Leaders get a framework they can use to standardize their approaches to balancing portfolio risk and earning their own customers’ trust.
* **Responsible AI specialists**
  who establish the specific policies needed by their organizations to comply with applicable regulations and industry standards, and work with builder teams to meet the policies. Specialists benefit from having a science-based best practice framework to help them set and implement their own organization’s AI-related policies.

## Getting started

To get started with the Responsible AI Lens, implement the best practice guidance provided using the
[GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens)
. Create or select an AI workload, add the Responsible AI Lens from the available custom lenses, and begin working through the focus areas relevant to your development stage.

Use this lens for new AI projects or to help enhance existing systems. Contact your AWS Solutions Architect or account representative for guidance on applying these practices to your specific use cases.

The launch of the
[AWS Well-Architected Responsible AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/responsible-ai-lens.html)
represents a significant step in our long-standing commitment to help organizations innovate responsibly with AI. The structured guidance and practical tools will help you navigate AI development complexities, improve benefits, reduce risks, and avoid costly late-stage changes.

The Responsible AI Lens reflects collaboration across AWS teams—from responsible AI scientists who brought deep expertise in evidence-based practices to solution architects who contributed insights from working with customers across industries. Their combined perspectives helped shape practical guidance that addresses real-world AI development challenges.

For related reading, you can explore the AWS Well-Architected Framework and other lens documents, including the AWS Well-Architected
[Generative AI Lens](https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/)
and
[Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html)
, which offer complementary guidance for AI implementations.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/04/25/rachna-new.png)
**Rachna Chadha**
is a Principal Technologist at AWS, where she helps customers leverage generative AI solutions to drive business value. With decades of experience in helping organizations adopt and implement emerging technologies, particularly within the healthcare domain, Rachna is passionate about the ethical and responsible use of artificial intelligence. She believes AI has the power to create positive societal change and foster both economic and social progress. Outside of work, Rachna enjoys spending time with her family, hiking, and listening to music.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/hallinan.jpeg)
Peter Hallinan**
is the Director of Responsible AI at AWS, where he leads an organization that advances the science and practice of Responsible AI at AWS. He has deep expertise in AI (PhD, Harvard) and entrepreneurship (Blindsight, sold to Amazon). His volunteer activities have included serving as a consulting professor at the Stanford University School of Medicine, and as the president of the American Chamber of Commerce in Madagascar.