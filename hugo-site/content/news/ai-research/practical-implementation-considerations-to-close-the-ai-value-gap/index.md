---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:00:18.609707+00:00'
exported_at: '2025-11-26T00:00:22.029804+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/practical-implementation-considerations-to-close-the-ai-value-gap
structured_data:
  about: []
  author: ''
  description: 'The AWS Customer Success Center of Excellence (CS COE) helps customers
    get tangible value from their AWS investments. We''ve seen a pattern: customers
    who build AI strategies that address people, process, and technology together
    succeed more often. In this post, we share practical considerations that can help
    close the AI value gap.'
  headline: Practical implementation considerations to close the AI value gap
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/practical-implementation-considerations-to-close-the-ai-value-gap
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Practical implementation considerations to close the AI value gap
updated_at: '2025-11-26T00:00:18.609707+00:00'
url_hash: 53020272e15d03d83433013c3c43a47865363bc7
---

Artificial Intelligence (AI) is changing how businesses operate.
[Gartner® predicts](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
at least 15% of day-to-day work decisions will be made autonomously through agentic AI by 2028. And 92% of companies are boosting their AI spending,
[according to McKinsey](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work&ved=2ahUKEwi-hMWWnPmQAxUxF1kFHaksFcAQFnoECBoQAQ&usg=AOvVaw0j7oHUfqwwBiNIkGYkckSh)
.

But here’s the problem: most companies are yet to realize a positive impact of AI on their profit and loss (P&L). According to analysis from
[S&P Global Market Intelligence](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/)
,

> *“The share of companies abandoning most of their AI initiatives jumped to 42%, up from 17% last year [2024]” in the first half of 2025.*

[According to Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
,

> *“Over 40% of agentic AI projects will be canceled by the end of 2027.”*

The gap between spending and results is clear. To make AI work, companies need to stop running scattered experiments and start building enterprise-wide programs.
[As McKinsey puts it](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf)
:

> *“The organizations that are building a genuine and lasting competitive advantage from their AI efforts are the ones that are thinking in terms of holistic transformative change that stands to alter their business models, cost structures, and revenue streams—rather than proceeding incrementally.”*

The AWS Customer Success Center of Excellence (CS COE) helps customers get tangible value from their AWS investments. We’ve seen a pattern: customers who build AI strategies that address people, process, and technology together succeed more often.

In this post, we share practical considerations that can help close the AI value gap.

## Implementation considerations

The following sections include practical implementation considerations for aligning leadership, redesigning incentives, building governance frameworks, and measuring outcomes—all grounded in real-world examples from organizations that have successfully closed their AI value gap. These practical insights can help you avoid common pitfalls and accelerate your path from AI investment to measurable business impact.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20094/ML-20094-image-1.gif)

*Figure 1: Six considerations for successful AI transformation and sustained value realization*

### **Business leaders — not just tech leaders — need to drive your AI agenda**

AI transformation requires translating vision into specific business outcomes with clear tracking mechanisms—and this demands broad cross-functional leadership from day one.

Roles like Chief Revenue Officers and line-of-business leaders need a seat at the decision-making table alongside technology leaders right from the start. These leaders have typically joined digital or cloud transformations much later in the process, but AI is different. The most impactful AI use cases come from two sources: line-of-business leaders who understand customer pain points and industry opportunities intimately, and employees across business functions who are willing to change their mindsets and fundamentally alter their operating models. Consider a large global institutional investment organization that embarked on an AI transformation program. They started by defining and creating relevant data and AI technical and business professions. Then, the organization designed and implemented the mechanisms and operating model needed to create data and AI products. Ultimately, they launched a new data and AI organization that helps them create new products, better serve customers, and monetize data assets by addressing new business opportunities. While engineering and product management remained at its core, their entire leadership team treated this as a business development initiative and partnered to make it possible.

### **Redesign incentives to reward AI-first operations**

Transform organizational behavior to reward actual AI adoption, not just theoretical interest. Restructure career pathways to create advancement opportunities tied to effective AI use and measurable business outcomes. Critical to success is defining what outcomes matter. AI can generate voluminous output with little business impact, making measurement of outcomes essential.

One organization introduced standardized definitions for business processes and automation levels. They then redesigned their performance management framework to incorporate automation achievement as a key metric for Product Managers. This approach shifted focus from traditional input metrics toward measurable automation outcomes. It encouraged leaders to prioritize AI-augmented structures and intelligent process redesign over manual operations.

This alignment demonstrates how organizations must clearly define and measure desired outcomes—and tie individual rewards directly to tangible AI-driven business results.

### **Put people first and have HR lead the change as a strategic partner**

HR serves as the cornerstone for aligning culture, talent, and incentives with AI transformation goals. Success requires HR to partner with executives in communicating the rationale for AI initiatives, addressing employee concerns, and fostering organizational buy-in through coaching and thought leadership.

Build AI fluency through tailored learning pathways. Provide focused training with practical tools like pre-populated prompt catalogs and quick-start demonstrations. Strengthen employee engagement through continuous feedback loops, celebrate AI learning participation across teams, and invest in retention strategies that value AI-skilled talent. HR champions adoption by collaborating with business and operations teams to develop role-based “What’s in it for me” content and current versus future process comparisons. For example, HR at a global financial institution took a leadership role to accelerate adoption of a reimagined product operating model. After the institution had invested significantly in a bottom-up transformation, HR designed and led—in partnership with AWS—a top-down approach. They empowered business leaders from lines of business, operations, and technology with extensive executive-level training to help them lead product teams, not just operate them. These leaders worked with technology teams to build mechanisms that helped accelerate adoption of their product operating model. The resulting mechanisms enabled them to create AI solutions focused on industry opportunities and customer needs.

HR support is key to transforming resistance into enthusiasm by embedding AI-first behaviors into the cultural DNA.

### **Set guardrails that help protect—without slowing down**

Establish AI governance frameworks from day one that balance centralization and federation. This facilitates compliance alignment and integration while enabling rapid innovation at the edge. Pure centralization offers simpler governance but slows innovation. Complete federation creates integration challenges and compliance gaps.

For both centralized and federated models, create cross-functional AI governance councils with representation from legal, risk, IT, and business units. Define clear guardrails, approval thresholds, and escalation paths. This approach accelerates AI delivery by creating clear paths to production and reducing bureaucratic friction while maintaining enterprise-wide coherence and risk management.

One financial services customer implemented a three-layered AI governance approach. At the enterprise level, they automated security and compliance policies through
[policy as code](https://aws.amazon.com/blogs/opensource/cloud-governance-and-compliance-on-aws-with-policy-as-code/)
. At the line-of-business level, they created data policies that support AI solutions within the value stream. At the solution level, they addressed individual AI model risks and performance thresholds. This approach facilitated necessary guardrails and policy adherence while allowing builders to focus on value-added AI solution features. It unlocked true innovation at the edge while maintaining compliance alignment with critical policies.

### **Work with the right partners to move faster on AI**

[According to Gartner](https://www.gartner.com/document-reader/document/6570102?ref=ABABYRDocConvEmail&pos=BYR_RR_DT-1_RN_119102)
,

> *“Scaling AI solutions across the enterprise is challenging and requires intentional plans to address AI skills, infrastructure, governance policies and forums to facilitate collaboration, integration, and shared best practices.”*

Organizations achieve higher success rates when working with partners who provide AI innovation, cloud expertise, and industry-specific knowledge at the right time. Effective AI transformation partners serve three roles: industry advisors who reimagine existing value streams and workflows to uncover high-value use cases, technical experts who bring leading experience building scalable AI solutions and change champions who manage cultural shifts through training and governance frameworks.

A global insurance company engaged an AI transformation partner for a long-term engagement focused on building durable capabilities. The partner established business case frameworks and assets to prioritize use cases and baseline KPIs. They developed detailed adoption strategies using train-the-trainer methodologies. They implemented measurement systems to continuously track productivity impact. Together, they established governance models for ongoing
[AI agent](https://aws.amazon.com/what-is/agentic-ai/)
creation and enterprise-wide deployment. This “teach to fish” model meant the insurance company could independently sustain and expand their AI transformation beyond the partnership engagement.

### **Track results that matter—not just what AI costs**

Traditional cost prediction models struggle with AI’s continuously changing pricing and capabilities. Success requires anchoring to one or two measurable business outcomes that can be baselined and tracked—such as customer conversations handled entirely by AI agents or revenue uplift per recommendation accepted.

Build adaptive ROI frameworks that can be seamlessly adjusted to changes in token pricing, inference efficiency, and model capabilities rather than fixed cost projections. Focus on outcome-based metrics that demonstrate clear business value as use cases scale. With these metrics executives can make informed investment decisions despite technological uncertainty. This approach transforms AI economics from unpredictable cost centers into measurable value drivers, providing the financial clarity needed for confident scaling decisions. A marketing team implemented generative AI for long-form content creation and quality assurance. They analyzed their end-to-end process to determine the distribution of their production capacity and identify the costliest failure point: localization errors. They anchored against measurable baselines of 150+ annual localization errors and 300 monthly QA hours across 150 assets. The solution delivered immediate impact by catching errors earlier, minimizing costly localization rework while accelerating production speed. Return on investment in the solution was measured through localization cost savings and top-line value through increased content output, providing a clear path to assess the impact of scaling the solution.

## Conclusion

Becoming an AI-first organization requires synchronized transformation across seven critical dimensions: Data and AI Vision and Strategy that establishes a data-driven foundation while embedding AI into core business objectives; Business Process Redesign to optimize human-AI collaboration; Culture & Change Management to drive adoption top-down and bottom-up change; Infrastructure and Operations for scalable, self-healing systems; AI Skills and Talent development with continuous learning to build core AI capabilities beyond basic awareness; Security, Governance, and Ethics to facilitate responsible AI deployment; and AI Industrialization for seamless integration and automation.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/7-dim-112525-1-1.png)

*Figure 2: Seven dimensions of AI-First organizational transformation*

These dimensions provide a framework for systematically evaluating and implementing AI transformation. But here’s what matters most: technology alone delivers marginal gains. When orchestrated with organizational change and process redesign, it creates measurable business value. Organizations that have success, compared to those that do not, see dramatic results—45% more in cost savings and 60% more in revenue growth,
[according to the Boston Consulting Group (BCG)](https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap)
.

The AWS Customer Success Center of Excellence collaborates with AWS partners to define programmatic implementation plans that can help customers embed AI into their operations, product development, business processes, and go-to-market strategies. Because becoming AI-first isn’t about isolated technology initiatives—it requires synchronized evolution across people, process, and technology, with comprehensive change management as the enabler.

For more information about becoming an AI-first company, contact your AWS account team. For more information on delivering agents see the
[AWS Artificial Intelligence blog](https://aws.amazon.com/blogs/machine-learning/enabling-customers-to-deliver-production-ready-ai-agents-at-scale/)
.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/23/sbhargs.jpeg)
**Bhargs Srivathsan**
leads the Customer Success Center of Excellence for Amazon Web Services (AWS), where she is responsible for defining and executing on the strategic vision for customer success across AWS’ services. In this role, she focuses on ensuring AWS customers and partners realize maximum value from their technology investments, particularly as the pace of innovation accelerates with AI and other emerging technologies. She works closely with the field, specialist GTM leaders, and partners across AWS to build and scale customer success capabilities that drive adoption and business outcomes for customers.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/20210717-SK-AWS-Badge.jpg)
**Sergio Klarreich**
is a Senior Manager of Customer Success at AWS, within the Customer Success Center of Excellence. Sergio leads a team focused on enabling enterprises to realize tangible business outcomes from AI investments. With hands-on experience leading Fortune 500 companies through successful AI-first transformation journeys and over 20 years driving technology innovation across global markets. He specializes in bridging the gap between AI strategy and measurable business results.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/23/badaljos.jpeg)
**Joseph Badalamenti**
is a Senior Customer Success AI Specialist at AWS, within the Customer Success Center of Excellence. As a Customer Success Specialist, he partners with enterprise customers to accelerate their AI transformation journeys. Joseph specializes in Generative AI and Agentic AI implementations, helping organizations realize measurable business value through strategic AI adoption. Joseph has 20+ years experience supporting customers with Digital, Cloud, and AI Transformation journeys.