---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-24T00:03:27.449660+00:00'
exported_at: '2025-12-24T00:03:29.979882+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-dlocal-automated-compliance-reviews-using-amazon-quick-automate
structured_data:
  about: []
  author: ''
  description: In this post, we share how dLocal worked closely with the AWS team
    to help shape the product roadmap, reinforce its role as an industry innovator,
    and set new benchmarks for operational excellence in the global fintech landscape.
  headline: How dLocal automated compliance reviews using Amazon Quick Automate
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-dlocal-automated-compliance-reviews-using-amazon-quick-automate
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How dLocal automated compliance reviews using Amazon Quick Automate
updated_at: '2025-12-24T00:03:27.449660+00:00'
url_hash: 0e0c6db91ee236d8d42d58d78b5564b549e74288
---

[dLocal](https://www.dlocal.com/)
, Uruguay’s first unicorn, has established itself as a pioneer in cross-border payments since its founding in 2016. Today, the company operates in over 40 emerging countries, connecting more than two billion consumers with global technology leaders.

Operating at this scale requires strict and consistent compliance processes. Each month, thousands of merchant ecommerce websites are reviewed to verify alignment with dLocal’s policies. These merchants have already onboarded dLocal as a payment service provider or are in the process of onboarding. The compliance process includes verifying that merchants are not selling prohibited or non-compliant goods or services, and confirming that domains are valid and sites remain accessible. However, the compliance challenge extends beyond initial onboarding. Merchant websites can change their offerings or practices at any time, requiring ongoing monitoring to detect policy violations.

In 2023, dLocal developed a proprietary generative AI solution to help streamline the website review process. However, as the company expanded across more countries and onboarded thousands of new merchants monthly, the growing complexity challenged the continued evolution of the solution. A significant portion of cases still required manual review to validate compliance decisions, creating a bottleneck that limited scalability as transaction volumes and merchant growth accelerated. The manual review of merchant websites included examining their full product catalogs to identify items violating the company’s prohibited product policies. These covered a wide range of illegal or unethical categories with over 15 major categories and more than 100 subcategories. This made the review process highly cumbersome.

To address this, dLocal sought to automate the review process to reduce manual effort, minimize human error, and facilitate compliance alignment. Additionally, because onboarded websites must be periodically reevaluated to confirm continued adherence to policies, automation would also help streamline these recurring compliance checks for existing merchants.

dLocal decided to partner with AWS to implement
[Amazon Quick Automate](https://aws.amazon.com/quicksuite/automate/)
, a capability of
[Amazon Quick Suite](https://aws.amazon.com/quicksuite/)
, as one of the service’s earliest adopters. Quick Automate helps enterprises build, deploy and maintain resilient automations at scale.

Using Quick Automate, dLocal automated its merchant compliance website review process, enabling large-scale, efficient, and consistent policy enforcement. With an advanced multi-agent automation architecture engineered for enterprise-scale deployment, Quick Automate combines UI automation, API integrations, and automation orchestration in a single, fully managed solution. Quick Automate uses generative AI to analyze inputs from the user and suggests an automation that can be modified and extended to take action across business systems and UIs, engaging a human when needed. Through specialized AI agents, Quick Automate helps organizations automate complex processes across applications and departments while reducing operational costs through usage-based pricing.

In this post, we share how dLocal worked closely with the AWS team to help shape the product roadmap, reinforce its role as an industry innovator, and set new benchmarks for operational excellence in the global fintech landscape.

## Solution overview

dLocal required a process automation solution capable of navigating multiple product pages in websites and reviewing each product against their policy to determine if the website is compliance-aligned. The solution needed to be highly reliable, accurate, and scalable to thousands of websites. Given the high compliance risk associated with allowing websites that sell prohibited products on its system, the accuracy bar for the automation solution was high.

The automation was built using Quick Automate, designed for automating complex enterprise-scale business processes. A key component of the solution is a UI Agent, configured to autonomously perform website navigation and data extraction. The UI Agent is part of Quick Automate, enabling complex browser-based tasks.

The UI Agent takes natural language input, navigates websites, and performs tasks on the websites based on the inputs. The automation was configured to navigate and evaluate merchant website product pages to identify prohibited items, helping dLocal maintain their compliance posture. The AWS team collaborated closely with the dLocal team to design and refine prompts, helping the automation perform optimally for the customer’s needs. The following architecture diagram illustrates the automation.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Flow-1-779x1024.png)

The workflow consists of the following steps:

1. The case management feature retrieves merchant cases from a processing queue for evaluation, with each case containing essential data, including the website URL that needs to be navigated and assessed. This feature enables parallel automation execution, allowing multiple cases from the queue to be processed simultaneously, with each automation handling a designated number of cases to optimize efficiency and reduce overall processing time.
2. The UI Agent is designed to navigate websites across various languages. This agent uses specially crafted prompts to identify prohibited products and counterfeit items according to local regulations and country-specific requirements. It autonomously browses websites to collect product information and assess compliance with dLocal’s policies.
3. When websites are inaccessible, the system marks them as Non Compliant and evaluates the accessible sites against prohibited categories.
4. The system classifies each case as Approved, Rejected, or Website Inaccessible, generating detailed reasoning for the decision and marking rejected cases for human in the loop (HILO) review.
5. Each case is updated with its compliance status and reasoning, and the results are saved to the case management system for tracking and future reference.
6. The compliance results are stored in
   [Amazon Simple Storage Service](http://aws.amazon.com/s3)
   (Amazon S3) to maintain compliance with regulatory standards and facilitate proper documentation of the merchant evaluations.

## Core automation components

In this section, we discuss the core automation components used in the solution.

### Case processing

The solution processes merchant websites using its case management feature. This feature treats each recurring entity (in this case, every website) as an individual case, providing enhanced observability. Users can track metrics (such as success rate) and review logs at the case level rather than across the entire automation.

The feature handles multiple merchant evaluations concurrently using parallel batch processing, and provides real-time status updates and maintains comprehensive records for the case data.

### Automated website analysis using the UI Agent

The UI Agent is a feature in Quick Automate to automate complex browser-based actions based on natural language instructions. It handles inaccessible websites, timeouts, and technical failures. The agent is able to navigate multiple pages and reason over the content of the pages to determine if a website is selling prohibited products. It provides a standardized data format for downstream business systems.

The UI Agent reasons with the websites against more than 15 prohibited categories.

### Human in the loop

For the few cases that remain ambiguous, Quick Automate can route exceptions to human operators, enabling manual review of critical steps. Reviewers receive structured evidence site data, flagged issues, and screenshots so they can make quick, well-informed decisions.

The UI agent provides detailed reasoning for the decisions, which can be included in the human-in-the-loop review steps to give reviewers additional context.

### Integration

The solution securely stores compliance documents using its integration with Amazon S3. The solution enables users to create, modify, and analyze structured data directly within the automation.

### Reliability and compliance

The solution logs actions for compliance records. Built-in exception handling automatically detects and manages system errors and business logic exceptions, facilitating automation continuity and enabling intelligent error recovery without manual intervention.

## Results and impact

With Quick Automate, dLocal achieved a breakthrough in compliance automation, with up to 75% of merchant website reviews completed fully automatically in the universe rolled out for the controlled evaluations, with no human intervention required. Compliance specialists who once spent hours on routine website checks now focus exclusively on complex cases and making nuanced judgment calls that require deep regulatory expertise, leading to higher-quality risk decisions where it matters most.

Beyond improving onboarding efficiency, the automation helps identify instances of policy drift where previously compliant merchants introduce prohibited products. This automation enhances dLocal’s compliance process by providing continuous, real-time monitoring across the entire merchant portfolio.

dLocal is now positioned to scale merchant onboarding in line with business growth, with a clear path to push automation rates even higher. The goal is to expand automated coverage to encompass the majority of compliance cases, helping the team focus human expertise on high-risk merchants, complex regulatory scenarios, and cases requiring deep investigative judgment.

As Mauricio Clausen, VP of AI at dLocal, explains:”With Amazon Quick Automate, we’ve accelerated the evolution of one of our advanced AI assisted solutions: scaling merchant due diligence for cross-border marketplace payments in emerging markets. We integrated Amazon Quick Automate into our due diligence workflows to augment our compliance team’s capabilities. Our initial AI deployment streamlined processing across many cases, and we continue to apply expert review where needed. By leveraging Amazon Quick Automate, we’ve substantially reduced routine manual steps, allowing our compliance experts to focus on the most complex cases while maintaining accuracy and scalability.”

## Conclusion

dLocal’s implementation of Quick Automate illustrates how fintech companies can maintain rigorous compliance standards while scaling across emerging countries. The results dLocal achieved demonstrate how compliance can shift from a growth constraint to a strategic enabler.As an early adopter actively shaping the development of Quick Automate, dLocal has reinforced its position as an industry innovator. Their approach to automating routine decisions while reserving human expertise for complex, high-risk scenarios offers a model for compliance organizations navigating similar challenges at scale. In an industry where regulatory demands intensify as companies expand, this combination of AI-powered automation and strategic human oversight shows how technology can enhance rather than replace expert judgment.

To learn more about how Quick Automate is helping enterprises reimagine operations and automation, refer to the following additional resources:

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Tincho-100x119.jpeg)
**Martín Da Rosa**
is a Senior Software Architect at dLocal, bringing more than 13 years of experience to the software industry. Based in Uruguay and part of the dLocal team since 2016. Martin plays a key role in the AI R&D division. His work focuses on bridging the gap between solid architecture and applied AI to deliver high-impact technology solutions.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Chethan-100x120.png)
Chethan Shriyan**
is a Principal Product Manager – Technical at AWS, based in Seattle, WA. He brings nearly 12 years of experience in product and business management, including over 6 years at Amazon. He is passionate about building and delivering technology products that create meaningful impact in customer’s lives.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Guillermo-100x123.png)
Guillermo Spallina**
is a Sr. Customer Solutions Manager at AWS based in Buenos Aires, Argentina, with more than 25 years of experience in IT and product management, currently helping DNB/ISV customers achieve their business goals.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Reagan-100x109.png)
Reagan Rosario**
brings over a decade of technical expertise to his role as a Sr. Specialist Solutions Architect in Generative AI at AWS. Reagan transforms enterprise systems through strategic implementation of AI-powered cloud solutions, automated workflows, and innovative architecture design. His specialty lies in guiding organizations through digital evolution, preserving core business value while implementing cutting-edge generative AI capabilities that dramatically enhance operations and create new possibilities.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/ML-19345-Natalia-100x117.png)
Natalia Mayorga Prieto**
is an Associate Scale CSM at AWS based in Bogotá, Colombia, helping customers as a Migration Success Lead for MAP 2.0 migrations across LATAM. With a passion for technology and dance, she is dedicated to making her mark as a young woman in the tech world, inspiring others girls.