---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-10T00:03:19.156482+00:00'
exported_at: '2025-12-10T00:03:21.481060+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/create-ai-powered-chat-assistants-for-your-enterprise-with-amazon-quick-suite
structured_data:
  about: []
  author: ''
  description: In this post, we show how to build chat agents in Amazon Quick Suite.
    We walk through a three-layer framework—identity, instructions, and knowledge—that
    transforms Quick Suite chat agents into intelligent enterprise AI assistants.
    In our example, we demonstrate how our chat agent guides feature discovery, use
    enterprise data to inform recommendations, and tailors solutions based on potential
    to impact and your team’s adoption readiness.
  headline: Create AI-powered chat assistants for your enterprise with Amazon Quick
    Suite
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/create-ai-powered-chat-assistants-for-your-enterprise-with-amazon-quick-suite
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Create AI-powered chat assistants for your enterprise with Amazon Quick Suite
updated_at: '2025-12-10T00:03:19.156482+00:00'
url_hash: 35d716a0f33a7b091b0b82949caa621198fe8a56
---

Teams need instant access to enterprise data and intelligent guidance on how to use it. Instead, they get scattered information across multiple systems. This results in employees spending valuable time searching for answers instead of making decisions.

In this post, we show how to build chat agents in
[Amazon Quick Suite](https://aws.amazon.com/quicksuite/)
to address this problem. We walk through a three-layer framework—identity, instructions, and knowledge—that transforms Quick Suite chat agents into intelligent enterprise AI assistants. In our example, we demonstrate how our chat agent guides feature discovery, use enterprise data to inform recommendations, and tailors solutions based on potential to impact and your team’s adoption readiness.

## Benefits of Quick Suite chat agents

Quick Suite chat agents make advanced AI capabilities accessible to non-technical business users. Sales representatives, analysts, and domain experts can create sophisticated AI assistants without requiring deep technical expertise in machine learning or cloud infrastructure.

Quick Suite instances come with their own default
[system chat agent](https://docs.aws.amazon.com/quicksuite/latest/userguide/default-assistant.html)
(My Assistant). Administrators can enable the ability to create
[custom chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-agents.html)
for the users. Many users begin their Quick Suite journey by experimenting with My Assistant, discovering its AI capabilities through hands-on exploration. Users can enhance their interactions with contextual configuration: you can point the agent to specific Spaces to filter conversation scope, so responses draw from relevant organizational knowledge. You can also upload response templates or process documents directly into chat sessions to modify how the agent structures its outputs or approaches specific tasks.

Although these approaches offer immediate value and flexibility for individual users and one-off tasks, each conversation requires manual setup—selecting the right Spaces, uploading relevant templates, and providing context-specific instructions. With custom chat agents, you can capture these successful patterns into permanent, shareable solutions. You can preserve the contextual knowledge and behavioral guidelines in the agent’s persona, as well as the resource selections that make individual conversations successful, and package them into consistent, reusable agents that teams can deploy at scale. With this systematic deployment solution, individual insights become organizational assets that drive productivity gains. The solution reduces the cognitive load on users who no longer need to remember specific prompting techniques or locate the right resources for each interaction.

## The three-layer foundation: Identity, instructions, and knowledge

Effective chat agents are built on three essential components that work together to create consistent, reliable AI assistants:

* **Identity**
  – Defines who the agent is and what role it serves
* **Instructions**
  – Specifies how the agent should think and respond
* **Knowledge**
  – Provides the information the agent can access to search for answers and content generation

Understanding these three layers is crucial because they determine your agent’s behavior, including its communication style and the information it can retrieve.

### Identity

Identity defines who your agent is and what role it plays, which shapes how it responds to every request. You can configure an identity through the
**Agent identity**
configuration field.

### Instructions

Instructions function as behavioral directives that provide granular control over agent response generation, with specificity and consistency being crucial for effectiveness. Effective
[prompt engineering](https://aws.amazon.com/what-is/prompt-engineering/)
skills become essential when crafting both identity and instructions, because the precision and clarity of these elements directly impact the agent’s ability to understand context, follow behavioral directives, and maintain consistent, persona-driven responses. You can configure your Quick Suite chat agent with instructions in the
**Persona instructions, Communication style,**
and
**Reference documents**
fields. Reference documents refer to more specific or detailed instructions, or information attached as files that you require the agent to always have and follow exactly, like templates and process documents.

### Knowledge

[Large language models](https://aws.amazon.com/what-is/large-language-model)
(LLMs) power the agents. The custom chat agent provides required
[context](https://docs.aws.amazon.com/quicksuite/latest/userguide/agent-knowledge-sources-best-practices.html#knowledge-source-types)
to LLMs through two distinct means: instructions as discussed in previous section, and searchable knowledge. Quick
[Spaces](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-spaces.html)
provides the ability to pool searchable knowledge for the chat agent in different forms:

Spaces function as dynamic, searchable knowledge repositories that facilitate real-time access to teams’ information in structured or unstructured form, while maintaining security boundaries and supporting collaborative workflows. These are ideal for enabling semantic search capabilities over evolving knowledge bases like current business data and collaborative knowledge.

## Solution overview

The Quick Suite Product Specialist is a custom chat agent to help users identify the right Quick Suite features for their specific needs. My Assistant can answer any questions related to Quick Suite; the Product Specialist chat agent takes a product specialist’s approach to support user questions and requirements. This agent acts as an intelligent advisor that matches business challenges with appropriate Quick Suite capabilities.

The Product Specialist chat agent is configured to follow a three-phased methodology: discovery, analysis, and solution recommendations. This showcases how modern AI agents should balance comprehensive platform knowledge with practical wisdom about right-sizing solutions. It can recommend simple prompts to be used with My Assistant to serve individual users, or architect complex multi-capability workflows for enterprise-wide deployment, it exemplifies the principle of matching solution complexity to actual impact potential while fostering GenAI adoption across organizations and projecting potential ROI for recommended solutions.

In the following sections, we demonstrate how to build a knowledge Space consisting of the Quick Suite User Guide documentation and then configure the Quick Suite Product Specialist chat agent.

## Prerequisites

To build a custom chat agent in Quick Suite, you must have the following:

* An active Quick Suite instance
* A Quick Suite subscription for the required capabilities:
  + **Professional**
    – Create, configure, and share, spaces and custom chat agents
  + **Enterprise**
    **(includes Professional capabilities)**
    – Create knowledge bases

For more information about Quick Suite’s subscription tiers, see
[Amazon Quick Suite pricing](https://aws.amazon.com/quicksuite/pricing/)
.

## Create Space with knowledge base

We first set up a Quick Space as part of the context component of the three-layered foundation we discussed previously. This Space contains a searchable knowledge base for the
[Amazon Quick Suite User Guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/)
.

This step is for reference on how to create indexed searchable content for specific documentation. Quick Suite chat agents are self-aware of all the Quick Suite capabilities and associated implementation practices.

We can choose from two options to create our Space: a static file or a live web-crawled knowledge base.

### Use a static file

This option is a static snapshot of the official Quick Suite User Guide and must be updated occasionally to incorporate latest changes and additions to the platform documentation. Complete the following steps:

1. Go to
   [Amazon Quick Suite User Guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/)
   .
2. Choose the PDF download option under the page header to download the User Guide as a PDF file to your local machine.

![Downloading Amazon Quick Suite user guide](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/ml-20069-1-download-user-guide.gif)

3. On the Quick Suite console, choose
   **Spaces**
   in the navigation pane.
4. Choose
   **Create space**
   to create a new Space:
   1. For
      **Title**
      , enter a title, such as the following:

      ```
      Amazon Quick Suite Documentation Space
      ```
   2. For
      **Description**
      , enter a description, such as the following:

      ```
      This Quick Space contains Amazon Quick Suite User Guide file.
      ```
   3. Choose
      **Add knowledge**
      and choose
      **File uploads**
      .
   4. Upload the User Guide PDF.
   5. Choose
      **Share**
      to manage Viewer/Owner access to the created Space.

Files uploaded to a Space use the same access permissions as the Space.

![Creating Quick Space with the downloaded user guide](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/ml-20069-2-create-qs-with-pdf.gif)

### Use a live web-crawled knowledge base

This represents a near real-time option in which you set up a direct connection between the documentation site and Quick Suite through a web crawler integration, and indexing the documentation, with an automatic refresh configuration set on the default schedule.

1. On the Quick Suite console, choose
   **Integrations**
   in the navigation pane.
2. Choose
   **Add**
   and choose
   **Webcrawler**
   to add a webcrawler.
   1. For
      **Name**
      , use the default name.
   2. Select
      **No authentication**
      .
   3. Choose
      **Create and continue**
      .
3. Configure the knowledge base:
   1. For
      **Name**
      , enter a name, such as the following:

      ```
      Amazon Quick Suite User Guide Documentation KB
      ```
   2. For
      **Add URLs**
      , enter the main documentation URL:

      ```
      https://docs.aws.amazon.com/quicksuite/latest/userguide/
      ```
   3. Choose
      **Add**
      .
   4. Choose
      **Create**
      .
   5. On the
      **Knowledge bases**
      tab, choose the knowledge base you created. The knowledge base refresh is initiated automatically.
   6. To manage access to Knowledge base
      **,**
      choose Add Users & groups on the
      **Permissions**
      tab to search and add people or groups for Viewer access.

![Create a webcrawler knowledge base](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/ml-20069-3-create-webcrawler-kb.gif)

4. Choose
   **Spaces**
   in the navigation pane.
5. Choose
   **Create space**
   to create a new Space:
   1. For
      **Title**
      , enter a title, such as the following:

      ```
      Amazon Quick Suite Documentation Space
      ```
   2. For
      **Description**
      , enter a description, such as the following:

      ```
      This Quick Space consists of connection to the web-crawled knowledge base for Amazon Quick Suite’s User Guide from AWS Documentation website.
      ```
   3. Choose
      **Add knowledge**
      , then choose
      **Knowledge bases**
      .
   4. Locate the knowledge base you created and choose
      **Add**
      .
   5. Choose
      **Share**
      to manage Viewer/Owner access to the created Space.

Knowledge base permission settings are honored by Quick Suite over Space sharing settings.

The Space is now created and should be syncing the latest Quick Suite User Guide.

![Creating Quick Space with knowledge base](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/ml-20069-4-create-qs-with-kb.gif)

## Create chat agent

Complete the following steps to build your own Quick Suite Product Specialist:

1. On the Quick Suite console, choose
   **Chat agents**
   in the navigation pane.
2. Choose
   **Create chat agent**
3. Choose
   **Skip**
   to enter Builder view to create a custom chat agent, because we know exactly what instructions and assets the chat agent needs.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/08/ml-20069-5-create-chat-agent-1.png)

4. For
   **Title**
   , enter a title, such as the following:

   ```
   Quick Suite Product Specialist
   ```
5. For
   **Description**
   , enter a description, such as the following:

   ```
   A comprehensive expert agent that combines Amazon Quick Suite expertise with GenAI evangelism and prompt engineering mastery. DISCOVERS users' productivity challenges, GenAI readiness, and solution scalability needs, ANALYZES their competency and impact potential, and provides optimal SOLUTION RECOMMENDATIONS based on Amazon Quick Suite capabilities including Custom Chat Agents, Flows, Automate, Integrations, Extensions, Spaces, Research, and Quick Sight with detailed implementation guidance and projected ROI analysis.
   ```
6. Update the
   **AGENT PERSONA**
   configuration:
   1. For
      **Agent identity**
      , enter details such as the following:

      ```
      You are a seasoned expert in Amazon Quick Suite's capabilities with deep knowledge of how its features can solve various internal use cases. You also serve as a GenAI Evangelist, passionate about democratizing AI adoption across organizations, and an expert Prompt Engineer with mastery in crafting effective prompts for various AI systems. You specialize in use case discovery, analyzing productivity challenges, automation opportunities, GenAI solution design, and simple to complex workflow orchestration to recommend optimal Quick Suite solutions with detailed implementation guidance and projected ROI analysis.
      ```

      The
      **Agent identity**
      field defines the agent’s internal persona, which shapes the decisions it makes. Using the keywords “seasoned expert” establishes authority that influences response confidence and depth, while the multi-role design (“GenAI Evangelist,” “expert Prompt Engineer”) makes sure the agent can pivot between technical guidance, strategic adoption advice, and educational support. The emphasis on “use case discovery” programs the agent to prioritize understanding before recommending, establishing a consultative rather than transactional interaction pattern. The phrase “democratizing AI adoption” internally calibrates the agent to serve users at different skill levels, preventing it from defaulting to overly technical responses that might intimidate beginners. These identity choices program how it interprets queries and structures responses.
   2. For
      **Persona instructions**
      , enter instructions such as the following:

      ```
      For each user problem follow this 3-phased approach:
      A. DISCOVERY
      1. Analyze the initial use case details provided
      2. Before providing any recommendations, ask clarifying questions to understand:
      -Knowledge base platforms and scale of use case relevant to identifying suitable Quick Suite capability
      -User's current experience level with GenAI solutions (Beginner/Intermediate/Advanced)
      -Number of potential users who would benefit from this solution (Individual/Team/Department/Organization-wide)
      -Available metrics around the problem/challenge (e.g., "it takes 8 hours to do this manually today")
      -Current AI/automation tools in use and satisfaction level
      -Team's technical capabilities and change management readiness
      -Wait for user confirmation before proceeding
      B. ANALYSIS
      1. Analyze all the user provided information including their GenAI maturity, and scalability requirements
      2. Assess impact potential: High impact = high user count + significant time/effort savings; Low impact = limited users + minimal savings
      3. Right sizing the solution:
      -Low impact = Consider simple prompt-based solutions using default Chat Agent (My Assistant)
      -High impact = Recommend dedicated Quick Suite capabilities
      -Avoid unnecessary complexity when simple solutions suffice
      4. Calculate potential ROI in terms of as time savings by user count
      5. CAPABILITY VERIFICATION PROTOCOL:
      - Before recommending any specific Quick Suite feature, verify the exact capability exists in available documentation
      - Clearly distinguish between Quick Flows (interactive, on-demand workflows) and Quick Automate (scheduled automation with triggers)
      - If uncertain about a capability, explicitly state limitations and provide documented alternatives
      - Never assume features exist without documentation confirmation
      - When correcting previous errors, acknowledge the mistake and provide accurate information based on verified documentation
      - Use the documentation knowledgebase available through the attached Space to validate capabilities before making recommendations
      C. SOLUTION RECOMMENDATIONS
      1. List appropriate Quick Suite capabilities with scalability-matched options:
      -For low impact: Start with optimized prompts for default chat agent (My Assistant) or basic Quick Sight BI functionalities as suitable for the use case
      -For moderate-high impact: assess and recommend dedicated scalable solutions (aligning with the use case) built as custom chat agent, Flows, Automation projects, required Integrations, Extensions for web browser/Slack/Teams/Outlook/Word specific use cases, relevant Spaces, Research, Quick Sight
      -Present multiple options when applicable, prioritizing simplicity when impact doesn't justify complexity
      2. Provide clear reasoning for each suggested capability including:
      -Impact-to-complexity analysis
      -Scalability considerations (user adoption, maintenance, governance)
      -Pros & Cons with emphasis on right-sizing the solution
      -Detailed ROI projections including potential time savings multiplied by user count and estimated implementation costs (e.g., "suggested solution would save 7 hours per person across 50 users = 350 hours total weekly savings, equivalent to $X in productivity gains")
      -GenAI adoption benefits and change management considerations
      -Prompt engineering best practices for Chat Agents when applicable
      3. Ask if they want prescriptive implementation guidance, if they do, then provide detailed solution building pathways including:
      -Step-by-step implementation approach starting with minimum viable solution
      -Scaling pathway from simple to complex as adoption grows
      -Prompt engineering templates and best practices
      -GenAI adoption strategies and success metrics
      -ROI tracking and measurement recommendations
      -Change management recommendations
      ```

      The three-phase methodology (discovery, analysis, solution recommendations) gives the agent best practices and guidelines on the kind of information it needs to collect to inform its recommendations, so its ability to get data about these features is augmented by user-specified context that is relevant to the recommended solutions.
   3. For
      **Tone**
      , enter a description to calibrate emotional intelligence and approachability:

      ```
      Professional, consultative, thorough, and evangelistic about GenAI potential while emphasizing practical, right-sized solutions. Ask clarifying questions to ensure accurate recommendations while inspiring confidence in AI adoption without over-engineering.
      ```
   4. For
      **Response format**
      , configure the structural patterns (conversational vs. prescriptive, lists vs. paragraphs) that match different interaction phases:

      ```
      Conversational in DISCOVERY phase with competency and scalability assessment questions. Always ask follow-up questions for clarity before concluding suggestions. Prescriptive in SOLUTION RECOMMENDATIONS phase: Provide structured recommendations with clear reasoning, impact analysis, prompt engineering guidance, and GenAI adoption strategies. Use numbered lists for capabilities and bullet points for implementation details.
      ```
   5. For
      **Length**
      , set phase-appropriate boundaries to prevent both overwhelming verbosity and insufficient detail:

      ```
      Succinct and to-the-point in DISCOVERY phase. For SOLUTION RECOMMENDATIONS phase: Comprehensive enough to cover all relevant Quick Suite capabilities with detailed reasoning, scalability analysis, prompt engineering best practices, and GenAI evangelism insights, but organized for easy scanning.
      ```
   6. For
      **Reference documents**
      , you can provide reference documents that give additional guidance to the agent on enterprise considerations and guardrails to keep in mind while recommending solutions, as well as additional nuances about the different features to factor for solution complexity. For this example, we don’t upload additional documents.
7. For
   **KNOWLEDGE SOURCES**
   :
   1. Choose
      **Link spaces**
   2. Choose the Space you created earlier and choose
      **Link.**

Linking the Space makes sure the agent can verify capabilities against actual product documentation. The Space architecture maintains enterprise security by honoring underlying data source permissions, allowing AI deployment without compromising existing security permissions. The web crawler option for live documentation makes sure the agent’s knowledge stays current as the platform evolves.

8. For
   **ACTIONS**
   , set up relevant third-party platform integrations. For example, add one of your enterprise collaboration tools, such as Slack or Teams, for sharing the implementation recommendations from this agent with your team.

Action integrations extend capabilities beyond conversation to actual workflow execution. This dynamic knowledge approach configures an adaptive assistant that validates recommendations against current information, accesses real business data, and executes actions, all while respecting organizational security boundaries.

9. Update
   **CUSTOMIZATION**
   1. For
      **Welcome Message**
      , enter a message such as the following:

      ```
      Hello! I'm your Quick Suite Product Specialist, GenAI Evangelist, and Pro Prompt Engineer. Let's DISCOVER your productivity challenge, assess its scalability potential and your GenAI readiness, and I'll recommend the right-sized SOLUTION that maximizes impact, complete with projected ROI analysis.
      ```
   2. For
      **Suggested prompts**
      , enter suggestions that end-users of this chat might use as quick start prompts to talk to the agent:

      ```
      "What Quick Suite capability can help me with my productivity/automation use case?"
      "How can I maximize impact with the simplest possible GenAI solution for my use case?”
      “I'm new to GenAI - what's the best Quick Suite solution to start with for my use case?”
      ```
10. Choose
    **Update preview**
    , test the chat agent, and make adjustments as necessary.
11. Choose
    **Launch chat agent**
    to publish the agent.
12. Choose
    **Share**
    to share access to the chat agent as necessary.

![Option 2 Create Quick chat agent](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/05/ml-20069-5-create-chat-agent-2.png)

## Test the chat agent

Let’s demonstrate the capabilities of the Quick Suite Product Specialist that you created:

1. On the Quick Suite console, choose
   **Chat agents**
   in the navigation pane.
2. Select the Quick Suite Product Specialist chat agent you created.
3. On the
   **Actions**
   menu, choose the
   **Chat**
   link.
4. Send the following request to the agent: “I want to get help in formatting my weekly status emails.”

![QS Product Specialist agent response 1](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/05/ml-20069-6-review-response-1-1024x886.png)

The agent takes the initial prompts and returns with detailed discovery questionnaire to better understand your use case, without jumping to recommendations. You will notice some differences from run to run, and might not see the same questionnaire, and chat agent responses as shown in the example in this post.

5. Review and respond to the questionnaire.

![QS Product Specialist agent response 2](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/05/ml-20069-6-review-response-2.png)

The agent returns a comprehensive response including assessment of impact, multiple solution recommendations with reasoning, and high-level implementation pathway options, letting you choose your solution options, and receive prescriptive implementation guidance.

6. Continue interacting with the agent to get detailed implementation guidance. Try out the chat agent on your own use cases, build out recommended solutions, and learn from your interactions.

## Clean up

When you are ready to remove the custom chat agent from your Quick Suite setup, clean up the resources to avoid potential additional indexing costs:

1. Delete the knowledge base:
   1. On the Quick Suite console, choose
      **Integrations**
      in the navigation pane, then choose
      **Knowledge bases**
      .
   2. Choose the options menu (three dots) next to the knowledge base you created.
   3. Choose
      **Delete knowledge base**
      and follow the prompts to delete the knowledge base.
2. Delete the Space:
   1. On the Quick Suite console, choose
      **Spaces**
      in the navigation pane.
   2. Choose the options menu (three dots) next to the Space you created.
   3. Choose
      **Delete**
      and follow the prompts to delete the Space.
3. Delete the chat agent:
   1. On the Quick Suite console, choose
      **Chat agents**
      in the navigation pane.
   2. Choose the options menu (three dots) next to the chat agent you created.
   3. Choose
      **Delete**
      and follow the prompts to delete the chat agent.

## Key takeaways

Building effective chat agents requires intentional design across three foundational layers. The Quick Suite Product Specialist demonstrates these principles in action:

* **Specificity drives consistency**
  – Rather than hoping the LLM will determine the right approach, you can provide explicit identity definitions, behavioral constraints, decision frameworks, and output formats to transform generic AI into reliable expert assistants.
* **Structure prevents common failures**
  – The three-phase methodology (discovery, analysis, solution recommendations) shows how systematic approaches guide users to right-size solutions, only after understanding the problem.
* **Dynamic knowledge maintains relevance**
  – Linking live documentation and permission-aware Spaces makes sure agents validate recommendations against current information while respecting organizational security boundaries.

## Conclusion

Custom chat agents in Quick Suite can transform how teams access and use enterprise knowledge. By applying the three-layer framework—identity, instructions, and knowledge—you can create AI assistants that deliver instant, accurate answers while maintaining enterprise security and compliance. The Quick Suite Product Specialist example demonstrates how structured methodologies and careful configuration turn generic AI into specialized experts that guide users to the right solutions for their specific needs.

Start with a focused use case that demonstrates clear ROI, then expand as adoption grows. Custom chat agents can deliver measurable productivity gains, helping teams find information faster, automating repetitive workflows, or providing expert guidance at scale. To learn more about creating and deploying Quick Suite chat agents, see
[Create, customize, and deploy AI-powered chat agents in Amazon Quick Suite](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)
.

---

### About the authors

![Author-Nitish Chaudhari](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/ml-20069-7-nidacha-100x100.jpeg)
**Nitish Chaudhari**
is a Senior Customer Solutions Manager at AWS, where he partners with customers to architect and implement generative AI solutions. He specializes in building collaborating agents, chat agents, and automation flows with Amazon Quick Suite and Amazon Bedrock that help teams solve real-world productivity challenges at scale. Before joining AWS, Nitish led product teams in the energy sector, and he now works closely with customers and AWS service teams to shape the next generation of generative AI capabilities.

**![Author-Sindhu Santhanakrishnan](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/image-8-100x100.jpeg)
Sindhu Santhanakrishnan**
is a Senior Product Manager at AWS, where she leads the development of custom agent capabilities in Amazon Quick Suite. She has played a key role in AWS’s automation journey, being part of the Q Apps launch, leading Q Actions in Q Business, and most recently driving the successful launch of chat agents in Quick Suite. She specializes in building business-focused automation solutions, with a background in launching zero-to-one products and customer data platforms. Sindhu holds a Master’s in Product Management from Carnegie Mellon University.

**![Author-Vinayak Datar](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/image-9-100x133.jpeg)
Vinayak Datar**
is a Senior Solutions Manager based in Bay Area, helping enterprise customers accelerate their AWS Cloud journey. He’s focusing on helping customers to convert ideas from concepts to working prototypes to production using AWS generative AI services.