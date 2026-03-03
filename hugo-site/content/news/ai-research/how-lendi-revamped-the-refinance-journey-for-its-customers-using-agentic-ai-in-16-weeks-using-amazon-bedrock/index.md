---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T20:07:51.869668+00:00'
exported_at: '2026-03-03T20:07:56.041001+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-lendi-revamped-the-refinance-journey-for-its-customers-using-agentic-ai-in-12-weeks-using-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: This post details how Lendi Group built their AI-powered Home Loan
    Guardian using Amazon Bedrock, the challenges they faced, the architecture they
    implemented, and the significant business outcomes they’ve achieved. Their journey
    offers valuable insights for organizations that want to use generative AI to transform...
  headline: How Lendi revamped the refinance journey for its customers using agentic
    AI in 16 weeks using Amazon Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-lendi-revamped-the-refinance-journey-for-its-customers-using-agentic-ai-in-12-weeks-using-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Lendi revamped the refinance journey for its customers using agentic AI
  in 16 weeks using Amazon Bedrock
updated_at: '2026-03-03T20:07:51.869668+00:00'
url_hash: 46f120445ce73ff5bf4b79a717899db5ffdb4734
---

*This post was co-written with Davesh Maheshwari from Lendi Group and Samuel Casey from Mantel Group.*

Most Australians don’t know whether their home loan is still competitive. Rates shift, property values move, personal circumstances change—yet for the average homeowner, staying informed of these changes is difficult. It’s often their largest financial commitment, but it’s also the one they’re least equipped to monitor. And when they do decide to refinance, the process itself demands significant manual effort.

[Lendi Group](https://www.lendi.com.au/)
, one of Australia’s fastest growing FinTech companies, recognized this gap and set out to transform the home loan experience through innovative technology. By using the
[generative AI](https://aws.amazon.com/generative-ai/)
capabilities of
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
, Lendi Group has developed Guardian, an agentic AI-powered application that serves as an around-the-clock companion for homeowners, monitoring their loans, providing personalized insights, and simplifying the mortgage refinance process.

This post details how Lendi Group built their AI-powered Home Loan Guardian using Amazon Bedrock, the challenges they faced, the architecture they implemented, and the significant business outcomes they’ve achieved. Their journey offers valuable insights for organizations that want to use generative AI to transform customer experiences while maintaining the human touch that builds trust and loyalty.

## Challenges

Lendi Group identified several persistent challenges in the home loan journey that affected both customers and brokers:

* Customers struggled with limited visibility into their mortgage position. Most homeowners lacked real-time insights into whether their current rate remained competitive, how their equity position changed as property values fluctuated, or how their overall financial health impacted their mortgage options. This information gap often led to customers missing opportunities to save money or utilize their home equity effectively.
* The refinancing process was cumbersome and time-consuming. Even when customers identified better rates, the paperwork and administrative burden of refinancing deterred many from acting.
* Brokers spent significant time on administrative tasks rather than focusing on high-value client interactions. Post-call documentation, routine inquiries, and after-hours support diverted broker attention from complex client needs that required human expertise and empathy.
* Lendi Group faced the challenge of scaling personalized service across their extensive customer base. While their digital solution provided convenience, maintaining the human touch that builds trust in financial relationships proved difficult at scale, especially outside business hours.

These challenges led Lendi Group to explore how AI could transform the mortgage experience. Rather than viewing AI as merely an efficiency tool, Lendi envisioned a reinvention of the home loan journey—one where technology could anticipate customer needs, provide around-the-clock personalized guidance, and free human experts to focus on building meaningful relationships.

## Solution overview

Lendi’s Guardian represents a fundamental shift in how customers interact with their home loans. At its core, Guardian is designed to:

1. Monitor loan competitiveness by continuously scanning thousands of home loans daily and alerting customers when better deals become available
2. Track equity position in real time as property values and industry conditions change, giving customers visibility into their current financial standing
3. Streamline the refinancing process with journeys that adapt to the customer’s circumstances and auto populates forms based on internal and external data sources, removing friction points that previously deterred customers from taking action
4. Deliver personalized insights and recommendations based on each customer’s unique financial situation and goals

Lendi used Amazon Bedrock to accelerate the build of their agentic solution within 16 weeks.

The solution is built upon
[Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html)
and
[Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
. Lendi chose
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/)
(Amazon EKS) to deploy their AI agents at scale, facilitating the necessary infrastructure to meet consumer demand. By using the wide range of foundation models (FMs) available on Amazon Bedrock, Lendi was able to select task-appropriate models optimized for specific use cases.

A critical component of their solution is AI guardrails powered by Amazon Bedrock Guardrails, which help make sure that the customer communications remain aligned with regulatory requirements. Additionally, Lendi developed
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)
servers to enable AI agents to access institutional knowledge and interact with external services seamlessly.

The key components of the solution are as follows:

1. **UI layer**
   – Customers interact with Guardian through an intuitive chat led interface integrated directly into their Lendi dashboard, providing seamless access to AI-powered mortgage insights and recommendations.
2. **API layer**
   – A RESTful API in
   [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
   serves as the communication bridge between frontend applications and backend AI agents, handling request routing, authentication, and rate limiting to help maintain secure and reliable interactions.
3. **Compute layer**
   – Amazon EKS hosts and orchestrates the AI agents, providing auto-scaling capabilities to efficiently handle varying customer demand while maintaining consistent performance and availability.
4. **Intelligence layer**
   – The core AI capabilities are powered by multiple specialized agents built on Amazon Bedrock foundation models. Lendi used
   [Agno](https://github.com/agno-agi/agno)
   , an open-source agentic framework to develop these agents, with MCP servers providing integrations to internal systems, external data sources, and third-party services. Bedrock Guardrails help enforce compliance boundaries, verifying that the customer interactions adhere to Lendi’s communication guidelines and remain focused on relevant mortgage-related topics.
5. **Observability layer**
   – Langfuse captures comprehensive agent traces, including inputs, outputs, reasoning chains, and performance metrics, providing full visibility into agent behavior and enabling continuous optimization and debugging.
   [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/)
   logs are used to collect system level logs.
6. **Storage layer**
   – MongoDB serves as the persistent data store for user context, conversation history, and session state, enabling customers to resume conversations across sessions while providing agents with the customer-specific context needed for personalized recommendations.
   [Amazon S3](https://aws.amazon.com/s3/)
   is used to store documents and files provided by the customer.

The following diagram illustrates the solution architecture.

![architecture diagram](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/18/ML-19734-1.png)

This architecture pattern provides a robust and scalable system to deploy AI agents.

### Agent flow for mortgage refinance

Building upon this scalable architecture, Lendi designed a multi-agent orchestration system where specialized agents can collaborate to complete the mortgage refinance journey. This modular approach helps provide several key advantages: clear separation of concerns between agents, simplified development and maintenance of individual agent capabilities, faster response times through task-specific optimization, and straightforward troubleshooting when issues arise.

The mortgage refinance process flows through the following specialized agents, with seamless handovers preserving full context at each transition:

* **Mortgage Broker Associate Agent (initial engagement)**
  – This agent serves as the customer’s first point of contact, embodying a friendly, professional persona similar to a human mortgage broker. Its primary goal is to understand the customer’s current situation and assess their interest in refinancing.
* **Customer Information Collection Agent (data gathering)**
  – When a customer expresses interest in refinancing, this specialized agent systematically collects essential customer details including current loan information, employment status, income, and refinancing preferences. The agent uses conversational techniques to make data collection feel natural rather than interrogative and provides clarifications to the customer as required. The agent is context aware and asks for information not already provided by the customer.
* **Product Recommendation Agent (lender matching)**
  – With complete customer information in hand, this agent analyzes the customer’s profile against Lendi’s extensive database of lenders and products. It presents suitable options with clear explanations of benefits and potential savings.
* **Product-Specific Information Collection Agent (application preparation)**
  – After the customer selects their preferred product, this agent gathers the additional information required by that specific lender. Different lenders have varying requirements, and this agent adapts its questions accordingly.
* **Communication Agent (Linda)**
  – Linda is the off-system engagement and re-engagement agent that keeps customers connected to their refinance journey, even when they’re not actively using the Guardian system. Although the specialized agents manage in-system tasks from initial engagement to product selection and application preparation, Linda operates across channels such as SMS, email, WhatsApp, and push to bring customers back in at the right moment. She detects when progress has stalled, surfaces timely reminders or new opportunities, and reinvites customers to continue where they left off. Drawing on live data from the Aurora Digital Twin, Linda tailors messages to the customer’s specific context, tone, and goal, whether it’s encouraging them to reconnect their loan, review matched products, or complete their submission. In essence, Linda is the voice of Guardian beyond the app, helping keep customers informed, motivated, and moving forward throughout the refinance journey.

The following graphic illustrates this workflow.

![Workflow Diagram](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/18/ML-19734-2.png)

This agentic approach simplified the mortgage application process for customers by providing an intuitive, natural language interface to share information, ask clarifying questions, and receive guidance throughout their refinance journey. For brokers, it alleviated the burden of manual form filling and application submission, freeing them to focus their expertise on complex customer scenarios, relationship building, and providing strategic financial advice where human judgment and empathy are most valuable.

## Business outcomes and customer impact

Lendi’s Guardian application is already delivering measurable results, having settled millions in home loans with refinance cycle times considerably faster than Lendi Group’s baseline. Guardian extends this impact with its AI-powered Rate Radar, which scans thousands of home loans daily and enables refinancing in only 10 minutes, with no paperwork, no phone calls, only a single tap. By automating routine monitoring and alerting customers to better rates in real time, brokers can focus on negotiation, empathy, and complex structuring—the high-value, relationship-driven work that builds loyalty. Guardian launched in only 16 weeks following a more than 30,000-hour cross-functional sprint, demonstrating how an AI-first architecture accelerates both development velocity and customer outcomes.

## Lessons learned

Lendi Group’s 16-week journey to build and deploy the AI-powered Home Loan Guardian provided invaluable insights into implementing agentic AI at scale in a regulated financial services environment. Here are the critical lessons they learned:

* Prioritize early, iterative evaluation metrics to guide AI development systematically. Rely on data-driven metrics to make key decisions such as model choice. Use Amazon Bedrock prompt management for versioning prompts.
* Choose models strategically by using the diverse model options of Amazon Bedrock. Recognize that the most sophisticated model isn’t always the most effective solution for your specific use case. Equally important is incorporating domain knowledge from human experts into your prompts because this contextual expertise often determines success more than model selection alone.
* Take advantage of using Amazon Bedrock
  [batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
  on tasks that don’t require immediate results to reduce cost.
* Treat AI as a transformative technology requiring bold vision and rapid, strategic implementation. Use the generative AI capabilities of Amazon Bedrock and the scalable cloud infrastructure of AWS to accelerate AI-driven innovation.
* Prioritize responsible AI governance in regulated environments. Use Amazon Bedrock Guardrails to help enforce content policies, filter inappropriate responses, and maintain compliance alignment requirements throughout the AI lifecycle.
* Balance automation with human expertise. Design AI systems that augment—rather than replace—human judgment, maintaining a customer-centric approach where human oversight remains central to critical decisions.

## Future roadmap

Lendi Group’s implementation of the AI-powered Home Loan Guardian represents only the first step in their ambitious journey to become a fully AI-based organization by June 2026. With the foundation now in place, Lendi Group aims to use agentic AI to rethink the whole mortgage and finance journey.

To support this strategic initiative, Lendi is exploring new AWS services, including
[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
, which enables the deployment of agents in a scalable and secure manner without the overhead of infrastructure management. This approach will further help accelerate Lendi’s pace of innovation.

*“We’ve built our platform so that refinancing happens at the speed of life, not at the speed of paperwork,”*
says Devesh Maheshwari – CTO at Lendi.
*“A customer can receive a Rate Radar alert about a sharper rate or a shift in property value during their morning commute. They tap to engage with it and provide information to our Agentic platform “Guardian” and by the time they’re heading home, their refinance loan application can be lodged. That’s not magic. It’s what happens when you invest properly in intelligent automation, real-time decisioning APIs and a micro-services architecture that coordinates everything from document verification through to settlement, without manual handoffs. The real challenge wasn’t just speed. It was removing every point of friction while still meeting the highest standards of compliance and risk control. When your infrastructure can support life-changing financial decisions in minutes rather than weeks, you’re not just improving the experience. You’re resetting what customers expect from financial services.”*

## Conclusion

Lendi Group’s AI-powered Home Loan Guardian represents a significant leap forward in how Australians manage their home loans. By using the generative AI capabilities of Amazon Bedrock, Lendi has created a solution that helps transform the mortgage experience from a periodic, transaction-based interaction to an ongoing, proactive relationship that delivers continuous value to customers. Looking ahead, Lendi’s journey to become a fully AI-based organization by June 2026 positions them at the forefront of innovation in the Australian mortgage industry. Their vision of AI integrated into “every workflow, every decision, every customer experience, and every broker experience” presents a fundamental reimagining of how mortgage services can be delivered.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/18/pic-100x115.jpg)
Deepak Dalakoti**
, PhD, is a Deep Learning Architect at the Generative AI Innovation Centre in Sydney, Australia. With expertise in AI, he partners with clients to accelerate their generative AI adoption through customized, innovative solutions. Outside the world of AI, he enjoys exploring new activities and experiences.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/23/image-10-1-100x100.png)
**James Hardman**
James is a Senior Account Manager at AWS, partnering with Australia’s fintech and financial services organisations to navigate complex technology challenges. He works backwards from what matters most to his customers, connecting them with the right investment, tools, and specialist teams to help them move faster. James is particularly focused on helping customers explore emerging technologies like agentic AI – not for the sake of innovation, but to drive real business outcomes and better serve their end customers.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/23/igor_avatar1-aws-100x133.jpg)
**Igor Londero Gentil**
is a Solutions Architect at AWS, based in Sydney, helping customers design and build on the cloud with a focus on serverless and event-driven architectures. With a background spanning infrastructure engineering, cloud architecture, and AI, he brings a practitioner’s perspective to solving real-world problems — grounded in years of hands-on experience before joining AWS. Igor is a regular speaker on topics like event-driven architectures and AWS Lambda, and an active open-source contributor.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/18/39763-100x67.jpeg)
Devesh Maheshwari**
is the Chief Technology Officer at Lendi Group Services in Sydney, Australia, where he’s driving the company’s transition to an AI-native business. With more than 18 years of experience leading technology strategy, digital transformation and engineering teams, Dev has a strong track record in fintech and highly regulated sectors, shaping platforms that scale and deliver real business value. Before Lendi and he has held senior leadership positions at DataMesh, Tyro Payments, Tabcorp & ThoughtWorks. He’s also a trusted advisor and mentor in tech, and he’s shared his insights on AI and innovation at industry events.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/23/image-52-1-100x122.png)
**Samuel Casey**
began his career in the startup ecosystem as the co-founder of a specialised AI consultancy. After successfully spinning out a proprietary AI product and overseeing its acquisition by Mantel Group, Samuel joined Mantel four years ago to lead high-stakes digital transformations. As an AI partner in Mantel, he has spearheaded a variety of complex projects for a broad range of enterprise and government clients. Most recently, Samuel has been at the forefront of the Generative/Agentic AI movement, dedicated to helping organisations integrate AI Solutions into their core operations as these technologies have materialised in the global market.