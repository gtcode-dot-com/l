---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-24T00:03:26.737680+00:00'
exported_at: '2025-12-24T00:03:29.985248+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/aws-ai-league-model-customization-and-agentic-showdown
structured_data:
  about: []
  author: ''
  description: In this post, we explore the new AWS AI League challenges and how they
    are transforming how organizations approach AI development. The grand finale at
    AWS re:Invent 2025 was an exciting showcase of their ingenuity and skills.
  headline: 'AWS AI League: Model customization and agentic showdown'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/aws-ai-league-model-customization-and-agentic-showdown
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'AWS AI League: Model customization and agentic showdown'
updated_at: '2025-12-24T00:03:26.737680+00:00'
url_hash: 3fa9f46012d13feafe0ffb4a71b379ec1a2834cc
---

Building intelligent agents to handle complex, real-world tasks can be daunting. Additionally, rather than relying solely on large, pre-trained foundation models, organizations often need to fine-tune and customize smaller, more specialized models to outperform them for their specific use cases. The AWS AI League provides an innovative program to help enterprises overcome the challenges of building advanced AI capabilities through exciting competitions that drive innovation in agentic AI and model customization.

In 2025, the first
[AWS AI League competition](https://aws.amazon.com/about-aws/whats-new/2025/07/introducing-aws-ai-league/)
captured the attention of developers, data scientists, and business leaders globally. They came together to solve pressing problems using the latest AI tools and techniques. The grand finale at AWS re:Invent 2025 was an exciting showcase of their ingenuity and skills. Cross-functional teams from leading organizations competed head-to-head, demonstrating their ability to craft effective prompts, fine-tune models, and build powerful AI agents.

Congratulations to our 2025 AWS AI League Champions! After intense competition among these three exceptional builders emerged victorious, sharing a $25,000 prize pool:

* 1st Place: Hemanth Vediyera from Cisco
* 2nd Place: Ross Williams from Aqfer
* 3rd Place: Deepesh Khanna from Capital One

![Figure 1: Left to right: Ross, Hemanth, Deepesh](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-1.png)

Figure 1: Left to right: Ross, Hemanth, Deepesh

This post explores how the AWS AI League program can be used to host AI competitions that can help participants experience model customization and agent building concepts, apply these to tackle real-world business challenges, and showcase their innovative solutions through engaging, game-style formats. We highlight the new agentic AI and model customization challenges, where enterprises can apply to host internal tournaments using AWS credits, and developers can compete at AWS events.

To get started, visit the
[AWS AI League product page.](https://aws.amazon.com/ai/aileague/)

## What is the AWS AI League Championship?

The AWS AI League experience begins with a hands-on, 2-hour workshop led by AWS experts, followed by self-paced experimentation. The journey culminates in a captivating, gameshow-style grand finale, where you showcase your AI creations and solutions to address pressing business challenges. The following figure shows these three steps.

![Figure 2: AWS AI League Championship steps](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-3.png)

Figure 2: AWS AI League Championship steps

Building on the success of the 2025 program, we are excited to announce the launch of the
[AWS AI League 2026 Championship](https://aws.amazon.com/about-aws/whats-new/2025/11/ai-league-2026-championship/)
. This year, the competition features two new challenges that allow participants to really put their AI skills to the test:

1. The agentic AI Challenge allows you to build intelligent agents using
   [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
   . Competitors craft customized agent architectures to tackle real-world business problems.
2. Complementing the agentic AI Challenge, the model customization Challenge now uses the latest fine-tuning recipes in
   [SageMaker Studio](https://aws.amazon.com/sagemaker/?trk=31926bd3-3ed0-43f3-a835-1801081fa158&sc_channel=ps&ef_id=CjwKCAiAw9vIBhBBEiwAraSAToSPObQDY9iSwn6WtYvlutKgvOLnITJRt9h2Y2dgGYgzPmeCJjYOGxoCyYkQAvD_BwE:G:s&s_kwcid=AL!4422!3!651751060695!e!!g!!sagemaker%20studio!23162970444!188078569355&gad_campaignid=23162970444&gbraid=0AAAAADjHtp833bIFJ4GBoL7HaTuA1ZZE-&gclid=CjwKCAiAw9vIBhBBEiwAraSAToSPObQDY9iSwn6WtYvlutKgvOLnITJRt9h2Y2dgGYgzPmeCJjYOGxoCyYkQAvD_BwE)
   . Here you customize models for specific use cases.

For the
[2026 AI League championship](https://aws.amazon.com/about-aws/whats-new/2025/11/ai-league-2026-championship/)
, the prize pool doubles to $50,000, with tracks catering to developers at different skill levels – from beginners to advanced practitioners.

### Build intelligent agents with the agentic AI challenge

The AWS AI League now features an exciting agentic AI challenge, where you build intelligent agents using Amazon Bedrock AgentCore to solve complex problems in a dynamic, game-style competition. In this challenge, agents navigate through a maze-like grid environment, encountering various challenges while seeking a treasure chest. These challenges map to real-world use cases, testing the agents’ ability to handle inappropriate content, execute code, use a browser, and more.

Agents have a time limit to traverse the map, collect points, and overcome the obstacles before reaching the treasure chest. The more points they earn, the higher they rank on the leaderboard. You can fully customize your agents using Amazon Bedrock AgentCore primitives, which enables you to more securely scale and manage production-grade agents. You can also select specific models for supervisor and sub-agents, as well as create custom tools such as
[Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
,
[AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
, and
[AWS Lambda](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-lambda.html)
functions to help your agents navigate the challenges. The following figure depicts the obstacles the agent must overcome while traveling to reach the treasure chest.

![Figure 3: AWS AI League Agentic Challenge](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-5.png)

Figure 3: AWS AI League Agentic Challenge

AWS AI League provides a full user interface (UI) for users to build their intelligent agent solutions. You can use this no-code UI to construct multi-agent architectures and tools, integrating various components such as
[Amazon SageMaker Studio CodeEditor](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html)
for interactive coding of custom Lambda functions and tools. This allows you to fully develop and customize your agent-based solutions within the AWS AI League website, without needing to leave the environment.

The following screenshots showcase the agent building experience all within the AWS AI League website.

![Figure 4: AWS AI League agent tools](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-8.png)

Figure 4: AWS AI League agent tools

![Figure 5: AWS AI League multi agent architecture ](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-10.png)

Figure 5: AWS AI League multi agent architecture

Throughout the competition, users receive real-time agent performance feedback, with a large language model (LLM) evaluator providing assessment to help with iteration. The following image showcases how the agent is evaluated during challenges.

![Figure 6: AWS AI League agent challenge evaluation](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-6.jpg)

Figure 6: AWS AI League agent challenge evaluation

At the grand finale, the top finalists take the stage to showcase their agents’ capabilities in a live, game-show format, demonstrating the power and versatility of agentic AI in solving complex, multi-step problems. The evaluation criteria include time efficiency, accuracy in solving challenges, agent planning, and token consumption efficiency. The following snapshot shows the final round of the Grand Finale at re:Invent 2025.

![Figure 7: AWS AI League re:Invent 2025 Grand Finale](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-13.png)

Figure 7: AWS AI League re:Invent 2025 Grand Finale

### Customize models to outperform larger models

AWS AI League is expanding the scope of its
[model customization challenge](https://aws.amazon.com/blogs/aws/aws-ai-league-learn-innovate-and-compete-in-our-new-ultimate-ai-showdown/)
, allowing you to use the latest advancements in fine-tuning techniques.

You can access the new model customization experience within
[Amazon SageMaker Studio,](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html)
where you can use powerful new training recipes. The goal is to develop highly effective, domain-specific models that can outperform the performance of larger, reference models.

The challenge begins with you honing in on your model customization skills. Using the tools and techniques you have learned, you apply advanced fine-tuning methods to help enhance your model’s performance. After your models are customized, the true test begins. The models are submitted to a leaderboard for performance assessment against a reference model. The model earns points each time the automated judge deems your customized model’s response to be more accurate and comprehensive than the reference model’s output. You can showcase your advanced skills, rise to the top of the leaderboard, and potentially unlock new opportunities for your organizations.

During the challenge, you receive real-time feedback on your model’s performance from an automated evaluator when you submit to the leaderboard. The leaderboard evaluates submissions against a reference dataset throughout the competition, providing immediate feedback on accuracy to help you iterate and improve your solutions. The following image showcases how an AI critique is used to evaluate the customized model.

![Figure 8: AWS AI League model customization evaluation](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-15.jpg)

Figure 8: AWS AI League model customization evaluation

At the grand finale, the top finalists demonstrate their models’ capabilities in a live, game-show format, showcasing their prompt engineering abilities. During the gameshow, the scoring includes expert evaluation where domain experts and a live audience participate in real-time voting to determine which AI solutions best solve real business challenges. The following image showcases the participant prompt engineering view during a Grand Finale.

![Figure 9: AWS AI League model customization Grand Finale participant view](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/ML-20061-image-17.jpg)

Figure 9: AWS AI League model customization Grand Finale participant view

## Conclusion

In this post, we explored the new AWS AI League challenges and how they are transforming how organizations approach AI development. At AWS, we’ve learned that the fastest way to spark innovation is through competition. With AWS AI League, builders can now showcase their AI skills, compete and unlock innovation.

To learn more about hosting an AWS AI League within your organization visit the
[AWS AI League](https://aws.amazon.com/ai/aileague/)
and to dive deeper into building intelligent agents and customizing AI models explore
[AWS AI training catalog](https://skillbuilder.aws/category/domain/artificial-intelligence/?trk=805ba28f-db17-442f-9f1a-252060a9709c&sc_channel=el)
on
[AWS Skill Builder](https://skillbuilder.aws/)
.

---

### About the authors

**![Marc Karp](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/11/27/ml-17555-karpmar.jpg)
Marc Karp**
is an ML Architect with the Amazon SageMaker Service team. He focuses on helping customers design, deploy, and manage ML workloads at scale. In his spare time, he enjoys traveling and exploring new places.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/22/natasya.png)
Natasya K. Idries**
is the Product Marketing Manager for AWS AI/ML Gamified Learning Programs. She is passionate about democratizing AI/ML skills through engaging and hands-on educational initiatives that bridge the gap between advanced technology and practical business implementation. Her expertise in building learning communities and driving digital innovation continues to shape her approach to creating impactful AI education programs. Outside of work, Natasya enjoys traveling, cooking Southeast Asian cuisines and exploring nature trails.