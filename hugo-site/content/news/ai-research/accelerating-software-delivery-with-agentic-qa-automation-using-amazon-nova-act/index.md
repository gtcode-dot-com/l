---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T06:15:37.594708+00:00'
exported_at: '2026-04-02T06:15:40.470623+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate how to implement agentic QA automation
    through QA Studio, a reference solution built with Amazon Nova Act. You will see
    how to define tests in natural language that adapt automatically to UI changes,
    explore the serverless architecture that executes tests reliably at scale, and
    get step-...
  headline: Accelerating software delivery with agentic QA automation using Amazon
    Nova Act
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Accelerating software delivery with agentic QA automation using Amazon Nova
  Act
updated_at: '2026-04-02T06:15:37.594708+00:00'
url_hash: e5407911a91059b41c86c456f006cff24bc7036d
---

Quality assurance (QA) automation is critical for modern software delivery. It catches regressions before production, validates user journeys at scale, and enables confident feature releases. But traditional QA automation solutions are brittle and demand specialized programming knowledge, decelerating software delivery.

Automation frameworks rely on implementation details including UI selectors, element identifiers, and structural references to navigate applications. When developers refactor UI code or designers adjust layouts, tests break even though functionality remains intact. This maintenance burden stems from a mismatch in how teams work. Product managers define acceptance criteria in the business language, development teams implement features, then developers write automation code. This puts distance between testing and those who understand user needs, forcing software teams to maintain tests instead of delivering features.

These challenges are addressed by Amazon Nova Act, an AWS service to build fleets of reliable agents that automate production UI workflows at scale. Its custom computer use model interacts with applications the same way that users do: through natural language and visual understanding, rather than code inspection. This removes code-dependent selectors and technical barriers, enabling agentic QA automation that reduces test maintenance overhead, democratizes test management, and accelerates software delivery cycles.

In this post, we demonstrate how to implement agentic QA automation through QA Studio, a reference solution built with Amazon Nova Act. You will see how to define tests in natural language that adapt automatically to UI changes, explore the serverless architecture that executes tests reliably at scale, and get step-by-step deployment guidance for your AWS environment.

### **QA Studio overview**

QA Studio provides a web frontend, API, and CLI for managing QA automation, built on serverless AWS infrastructure and powered by Amazon Nova Act for agentic UI automation. Run tests on demand, schedule them automatically, or trigger them as part of your continuous integration and delivery CI/CD pipeline.

![Figure 1 - Nova QA Studio Test Case Execution Demo](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/26/output.gif)

Figure 1 – Nova QA Studio Test Case Execution Demo

### **Natural language test management**

Amazon Nova Act translates natural language instructions into browser interactions including navigation, data extraction, and assertions. Teams can use this to define tests in the same language that they use to describe product requirements, creating unified specifications where requirement changes flow directly into test definitions.

Teams can use QA Studio to create and execute tests using natural language to define test steps. Users create test suites through live browser preview powered by
[Amazon Bedrock AgentCore Browser,](https://aws.amazon.com/bedrock/agentcore/)
test generation from user journey descriptions using
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
, secure data entry through
[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
, and other capabilities. Amazon Nova Act translates these test definitions into browser actions, while QA Studio provides the interface, so test authors can create and manage tests without writing or maintaining code.

![Figure 2 – Test creation with the User Journey Wizard](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/26/image-qa-studio2.gif)

Figure 2 – Test creation with the User Journey Wizard

### **Visual navigation that adapts to change**

The computer use model of Amazon Nova Act navigates applications using their visual appearance and context rather than relying on code dependent selectors. When designers adjust button placement or developers refactor component structure, tests adapt automatically. This removes the brittleness that creates maintenance overhead in traditional frameworks so that test authors can focus on what the application should do rather than how to locate elements in code.QA Studio provides an interface for users to execute and monitor tests, using the visual navigation of Amazon Nova Act for UI automation, data extraction, and state validation. Teams can use this to focus on delivering features rather than maintaining test infrastructure.

![Figure 3 – A test in the QA Studio vs the equivalent traditional test automation code](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/26/image-qa-studio3.png)

Figure 3 – A test in the QA Studio vs the equivalent traditional test automation code

### **End-to-End test visibility**

Amazon Nova Act provides trajectory logs that capture its visual reasoning and decision making at each step, showing exactly what the agent saw and why it took specific actions. This transparency transforms debugging from parsing technical stack traces into understanding test behavior through natural language descriptions and visual context.

QA Studio surfaces these insights throughout the testing lifecycle. During test creation, users preview steps with the live browser. When tests execute, teams receive real-time status updates and can monitor progress across test suites. After tests complete, QA Studio provides test recordings, results, and Nova Act trajectory logs with screenshots so that teams can identify issues without debugging code level errors.

## **Technical architecture**

QA Studio uses the following AWS services:

![Figure 4 - QA Studio AWS architecture](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/26/image-qa-studio4.png)

Figure 4 – QA Studio AWS architecture

This serverless architecture provides automatic scaling and consumption-based economics with pay-per-use pricing across all AWS services. You maintain control over security policies, compliance requirements, and customization needs.

## **Getting started with QA Studio**

QA Studio is available as a
[GitHub repository](https://github.com/aws-samples/sample-qa-studio)
that you deploy in your own AWS account using the
[AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
. This gives you complete control over your testing infrastructure, security policies, and compliance requirements—all test data, recordings, and logs remain within your security boundary. You can configure VPC settings and access controls according to your organization’s requirements.

To deploy the QA Studio in your AWS Account:

1. Clone the
   [GitHub repository](https://github.com/aws-samples/sample-qa-studio)
   .
2. Follow the README guide to deploy the infrastructure using the AWS CDK.
3. Configure notifications and CI/CD integration (optional).

For complete deployment instructions, refer to the
[QA Studio GitHub repository](https://github.com/aws-samples/sample-qa-studio)
. The repository includes AWS CDK templates and all necessary components, guides, and documentation to deploy the QA Studio in your own AWS environment.

## **Cleaning Up**

If you deployed QA Studio for evaluation purposes, remember to delete the AWS resources to avoid incurring future costs. Refer to the GitHub repository README for complete deletion instructions.

Have questions about implementing QA Studio in your environment? Leave a comment, we’d love to hear about your testing challenges and how you’re planning to use AI-powered testing to accelerate your software delivery.

## **Conclusion**

In this post, we showed how agentic QA automation with Amazon Nova Act accelerates software delivery through natural language test management and visual navigation. QA Studio is a reference solution that removes technical barriers to QA automation and removes brittleness through visual understanding so that teams can focus on delivering features rather than maintaining test infrastructure.

---

## About the authors

### Vinicius Pedroni

[Vinicius Pedroni](https://www.linkedin.com/in/vinicius-pedroni-63ab9023/)
is a Senior Solutions Architect at AWS for the Travel and Hospitality Industry, with focus on Edge Services and Generative AI. Vinicius is also passionate about assisting customers on their Cloud Journey, allowing them to adopt the right strategies at the right moment.

### Jan Wiemers

[Jan Wiemers](https://www.linkedin.com/in/janwiemers/)
is a Senior Solutions Architect at AWS, working with customers in the Travel, Transportation & Logistics industry. With over 20 years of experience in the software industry, he focuses on the AI Product Development Lifecycle and Test Automation, helping customers accelerate how they build, test, and deploy AI-driven solutions.

### Ryan Canty

[Ryan Canty](https://www.linkedin.com/in/ryan-canty/)
is a Solutions Architect at Amazon AGI Labs with deep expertise in designing and scaling enterprise software systems. He works with customers to build and deploy fleets of reliable AI agents using Amazon Nova Act, an AWS service that automates UI workflows at scale.