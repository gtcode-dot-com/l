---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-30T12:15:13.543990+00:00'
exported_at: '2025-12-30T12:15:16.151633+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/how-to-integrate-ai-into-modern-soc.html
structured_data:
  about: []
  author: ''
  description: The 2025 SANS SOC Survey shows AI use is rising, but many SOCs lack
    integration, customization, and clear validation processes.
  headline: How to Integrate AI into Modern SOC Workflows
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/how-to-integrate-ai-into-modern-soc.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How to Integrate AI into Modern SOC Workflows
updated_at: '2025-12-30T12:15:13.543990+00:00'
url_hash: 6b5194b0e4e6b89b4bd4a51dd6ff461683a948ca
---

Artificial intelligence (AI) is making its way into security operations quickly, but many practitioners are still struggling to turn early experimentation into consistent operational value. This is because SOCs are adopting AI without an intentional approach to operational integration. Some teams treat it as a shortcut for broken processes. Others attempt to apply machine learning to problems that are not well defined.

[Findings from](https://www.sans.org/white-papers/sans-2025-soc-survey?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_Central26_Dec_CC_Organic_Article_SOC_Survey1&utm_campaign=SANS_Security_Central_2026)
[our 2025 SANS SOC Survey](https://www.sans.org/white-papers/sans-2025-soc-survey?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_Central26_Dec_CC_Organic_Article_SOC_Survey1&utm_campaign=SANS_Security_Central_2026)
reinforce that disconnect. A significant portion of organizations are already experimenting with AI, yet 40 percent of SOCs use AI or ML tools without making them a defined part of operations, and 42 percent rely on AI/ML tools "out of the box" with no customization at all. The result is a familiar pattern. AI is present inside the SOC but not operationalized. Analysts use it informally, often with mixed reliability, while leadership has not yet established a consistent model for where AI belongs, how its output should be validated, or which workflows are mature enough to benefit from augmentation.

AI can realistically improve SOC capability, maturity, process repeatability, as well as staff capacity and satisfaction. It only works when teams narrow the scope of the problem, validate their logic, and treat the output with the same rigor they expect from any engineering effort. The opportunity isn't in creating new categories of work, but in refining the ones that already exist and enabling testing, development, and experimentation for expansion of existing capabilities. When AI is applied to a specific, well-bounded task and paired with a clear review process, its impact becomes both more predictable and more useful.

Here are five areas where AI can provide reliable support for your SOC.

## **1. Detection Engineering**

Detection engineering is fundamentally about building a high-quality alert that can be placed into a SIEM, an MDR pipeline, or another operational system. To be viable, the logic needs to be developed, tested, refined, and operationalized with a level of confidence that leaves little room for ambiguity. This is where AI tends to be ineffectively applied.

Unless it's the targeted outcome, don't assume AI will fix deficiencies in DevSecOps or resolve issues in the alerting pipeline. AI can be useful when applied to a well-defined problem that can support ongoing operational validation and tuning. One clear example from the
*[SANS SEC595: Applied Data Science and AI/ML for Cybersecurity](https://www.sans.org/cyber-security-courses/applied-data-science-machine-learning?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_Central26_Dec_CC_Organic_Article_595&utm_campaign=SANS_Security_Central_2026)*
course is a machine learning exercise that examines the first eight bytes of a packet's stream to determine whether traffic reconstructs as DNS. If the reconstruction does not match anything previously seen for DNS, the system raises a high-fidelity alert. The value comes from the precision of the task and the quality of the training process, not from broad automation. The anticipated implementation is to inspect all flows on UDP/53 (and TCP/53) and assess the reconstruction loss from a machine learning tuned autoencoder. Threshold-violating streams are flagged as anomalous.

This granular example demonstrates an implementable, AI-engineered detection. By examining the first eight bytes of a packet stream and checking whether they reconstruct as DNS based on learned patterns in historical traffic, we create a clear, testable classification problem. When those bytes do not match what DNS normally looks like, the system alerts. AI helps here because the scope is narrow and the evaluation criteria are objective. It may be more effective than a heuristic, rule-driven detection because it learns to encode/decode what is familiar. Things that are not familiar (in this case, DNS) cannot be encoded/decoded properly. What AI cannot do is fix vaguely defined alerting problems or compensate for a missing engineering discipline.

## **2. Threat Hunting**

Threat hunting is often portrayed as a place where AI might "discover" threats automatically, but that misses the purpose of the workflow. Hunting is not production detection engineering. It should be a research and development capability of the SOC, where analysts explore ideas, test assumptions, and evaluate signals that are not yet strong enough for an operationalized detection. This is needed because the vulnerability and threat landscape is rapidly shifting, and security operations must constantly adapt to the volatility and uncertainty of the information assurance universe.

AI fits here because the work is exploratory. Analysts can use it to pilot an approach, compare patterns, or check whether a hypothesis is worth investigating. It speeds up the early stages of analysis, but it does not decide what matters. The model is a useful tool, not the final authority.

Hunting also feeds directly into detection engineering. AI can help generate candidate logic or highlight unusual patterns, but analysts are still responsible for interpreting the environment and deciding what a signal means. If they cannot evaluate AI output or explain why something is important, the hunt may not produce anything useful. The benefit of AI here is in speed and breadth of exploration rather than certainty or judgment. We caution you to use operational security (OpSec) and protection of information. Please only provide hunting-relevant information to authorized systems, AI, or otherwise.

## **3. Software Development and Analysis**

Modern SOCs run on code. Analysts write Python to automate investigations, build PowerShell tooling for host interrogation, and craft SIEM queries tailored to their environment. This constant programming need makes AI a natural fit for software development and analysis. It can produce draft code, refine existing snippets, or accelerate logic construction that analysts previously built by hand.

But AI does not understand the underlying problem. Analysts must interpret and validate everything the model generates. If an analyst lacks depth in a domain, the AI's output can sound correct even when it is wrong, and the analyst may have no way to tell the difference. This creates a unique risk: analysts may ship or rely on code they do not fully understand and haven't been adequately tested.

AI is most effective here when it reduces mechanical overhead. It helps teams get to a usable starting point faster. It supports code creation in Python, PowerShell, or SIEM query languages. But the responsibility for correctness stays with the human who understands the system, the data, and the operational consequences of running that code in production.

The author suggests that the team develop appropriate style guidelines for code and only use authorized (meaning tested and approved) libraries and packages. Include the guidelines and dependency requirements as part of every prompt, or use an AI/ML development tool that enables configuration of these specifications.

## **4. Automation and Orchestration**

Automation has long been part of SOC operations, but AI is reshaping how teams design these workflows. Instead of manually stitching together action sequences or translating runbooks into automation logic, analysts can now use AI to draft the scaffolding. AI can outline the steps, propose branching logic, and even convert a plain-language description into the structured format that orchestration platforms require.

However, AI cannot decide when automation should run. The central question in orchestration remains unchanged: should the automated action execute immediately, or should it present information for an analyst to review first? That choice depends on organizational risk tolerance, the sensitivity of the environment, and the specific action under consideration.

Whether the platform is a SOAR, MCP, or any other orchestration system, the responsibility for initiating an action must rest with people, not the model. AI can help build and refine the workflow, but it should never be the authority that activates it. Clear boundaries keep automation predictable, explainable, and aligned with the SOC's risk posture.

There will be a threshold where the organization's comfort level with automations enables rapid action taken in an automated way. That level of comfort comes from extensive testing and people responding to the actions taken by the automation system in a timely manner.

## **5. Reporting and Communication**

Reporting is one of the most persistent challenges in security operations, not because teams lack technical skill but because translating that skill into clear, actionable communication is difficult to scale. The
[2025 SANS SOC Survey](https://www.sans.org/white-papers/sans-2025-soc-survey?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_Central26_Dec_CC_Organic_Article_SOC_Survey2&utm_campaign=SANS_Security_Central_2026)
highlights just how far behind this area remains:
**69 percent of SOCs still rely on manual or mostly manual processes to report metrics**
. This gap matters. When reporting is inconsistent, leadership loses visibility, context is diluted, and operational decisions slow down.

AI provides an immediate and low-risk way to enhance the SOC's reporting performance. It can smooth out the mechanical parts of reporting by standardizing structure, improving clarity, and helping analysts move from raw notes to well-formed summaries. Instead of each analyst writing in a different style or burying the lead in technical detail, AI helps produce consistent, readable outputs that leadership can interpret quickly. Including moving averages, boundaries of standard deviation, and highlighting the overall consistency of the SOC is a story worth telling to your management.

The value isn't in making reports sound polished. It's in making them
**coherent and comparable**
. When every incident summary, weekly roll-up, or metrics report follows a predictable structure, leaders can recognize trends faster and prioritize more effectively. Analysts also gain back the time they would have spent wrestling with wording, formatting, or repetitive explanations.

## **Are You a Taker, Shaper, or Maker? Let's Talk at SANS Security Central 2026**

As teams begin experimenting with AI across these workflows, it is important to recognize that there is no single path for adoption. SOC AI utilization can be described via three convenient categories. A
**taker**
uses AI tools as delivered. A
**shaper**
adjusts or customizes those tools to fit the workflow. A
**maker**
builds something new, such as the tightly scoped machine learning detection example described earlier.

All of these example use cases can be in one or more of the categories. You might be both a taker and a maker in detection engineering, implementing the AI rules from your SIEM vendor, as well as crafting your own detections. Most teams are manual makers as well as takers (just using out-of-the-box ticketing system reports) in reporting. You might be a shaper in automation, partially customizing the vendor-provided SOAR runbooks. Hopefully, you're at least using vendor-provided IOC-driven hunts; that's something every SOC needs to do. Aspiring to internally-driven hunting moves you into that maker category.

What matters is that each workflow has clear expectations for where AI can be used, how output is validated, that updates are done on an ongoing basis, and that analysts ultimately remain accountable for the protection of information systems.

I'll be exploring these themes in more depth during my keynote session at
[SANS Security Central 2026](https://www.sans.org/cyber-security-training-events/security-central-2026)
in New Orleans. You will learn how to evaluate where your SOC sits today and design an AI adoption model that strengthens the expertise of your team. I hope to see you there!

[Register for SANS Security Central 2026 here.](https://www.sans.org/cyber-security-training-events/security-central-2026)

**Note:**
*This article was expertly written and contributed by Christopher Crowley, SANS Senior Instructor.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.