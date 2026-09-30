---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-30T02:44:09.836426+00:00'
exported_at: '2026-09-30T02:44:11.098832+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/prince-kohli-president-and-ceo-of-sauce-labs-interview-series
structured_data:
  about: []
  author: ''
  description: Prince Kohli, President and CEO of Sauce Labs, is a veteran technology
    executive with extensive experience spanning artificial intelligence, enterprise
    software, cloud computing, automation, networking, and cybersecurity...
  headline: Prince Kohli, President and CEO of Sauce Labs – Interview Series
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/prince-kohli-president-and-ceo-of-sauce-labs-interview-series
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Prince Kohli, President and CEO of Sauce Labs – Interview Series
updated_at: '2026-09-30T02:44:09.836426+00:00'
url_hash: 02cd02d4db67c28df577ef00a050c88a7c065707
---

[Prince Kohli](https://www.linkedin.com/in/princekohli/)
, President and CEO of Sauce Labs, is a veteran technology executive with extensive experience spanning artificial intelligence, enterprise software, cloud computing, automation, networking, and cybersecurity. Before joining Sauce Labs in February 2025, he spent more than six years as Chief Technology Officer of Automation Anywhere, where he helped advance AI-driven automation technologies for large enterprises. Earlier, Kohli served as Senior Vice President of Engineering at ThoughtSpot and held senior leadership roles at Ericsson, including overseeing global R&amp;D organizations comprising more than 10,000 engineers. He also spent nearly a decade at Citrix leading platform, cloud networking, engineering, and operations initiatives. Earlier in his career, he co-founded application security company Teros and worked as a technical lead at SGI. Alongside his executive roles, Kohli has contributed to technology governance initiatives through the Ethical AI Governance Group and previously participated in the World Economic Forum’s Safe Systems and Technologies working group.

[Sauce Labs](https://saucelabs.com/)
is a software quality and continuous testing company that provides enterprises with infrastructure and tools for testing web and mobile applications across browsers, operating systems, virtual environments, and real devices. Its platform supports capabilities including automated and manual testing, visual testing, mobile app distribution, error reporting, and AI-powered test authoring and analytics, while integrating with common continuous integration and delivery workflows. Sauce Labs is increasingly positioning its technology around AURA, its AI-Unified Release Assurance platform, which uses AI agents to help generate, execute, and analyze tests while retaining human oversight throughout the software release process. The company says its infrastructure has supported more than 8.7 billion test executions and over 300,000 enterprise users, drawing on nearly two decades of cross-platform testing data.

**Before
[joining Sauce Labs](https://saucelabs.com/company/news/sauce-labs-appoints-prince-kohli-as-chief-executive-officer)
, you led AI-driven automation at Automation Anywhere and managed major cloud and engineering organizations at companies including Ericsson and Citrix. How have those experiences shaped your view of the software-quality problem, and what convinced you to make AI-native release assurance a central priority at Sauce Labs?**

At Ericsson and Citrix, I saw how quickly a software defect can spread and affect worldwide infrastructure, creating major impacts on security, customer operations and trust, and revenue. Automation Anywhere showed me how AI changes the speed and structure of work, and it became clear that testing had to be rebuilt for the pace of AI-generated software. Sauce Labs pioneered test automation, so AI-native release assurance is the next major problem we are built to solve.

**Sauce Labs’**
[**research**](https://qz.com/ai-coding-tools-code-volume-releases-gap-nber-study-061126)
**found that 80% of organizations have traced a production incident, outage, or customer-impacting defect to AI-generated code. Does this point primarily to weaknesses in the code produced by AI, or to enterprises adopting AI coding tools without updating their testing and governance processes?**

The 80% figure points to a problem across the full software delivery system. The AI industry has attracted more than a trillion dollars in private capital, much of it predicated on AI making businesses dramatically more productive. But generating more code only creates value if companies can be confident about its quality and security before they get it into production.

AI-generated code can introduce subtle bugs and security issues and enterprises are being forced to push that code through testing and governance processes that were already struggling to keep pace. That creates a trillion-dollar execution problem: AI can accelerate software creation, but without modernized release assurance, it just as easily accelerates defects. Every bug will eventually be run into, so companies need to make sure they find it before a customer or attacker does.

**The report states that developers are producing 741% more code while release velocity has increased by less than 20%. What is preventing validation systems from keeping pace, and where does the largest bottleneck typically emerge within the software development lifecycle?**

Code generation has moved far ahead of test creation, maintenance, and analysis. The biggest bottlenecks usually appear after the code is written and needs to be verified in the context of the user journey. That can often be very complex, often more complex than the code itself, as it must account for end-to-end paths that span code functions and objects, with seemingly minor changes in semantics in one place creating large downstream effects. Authoring these tests in a way that they capture the intent of the application correctly and fully has traditionally been almost impossible, plus it requires a very significant amount of manual work and maintenance. Moreover, after tests run and something fails, teams have to understand and diagnose the issue including deciding whether a failure comes from the product or an outdated test. That work still depends heavily on manual review and engineering context.

**More than half of the surveyed enterprises acknowledged knowingly releasing software with critical defects, while 66% said they had compromised quality or testing standards to meet a deadline. Why are organizations accepting this level of risk, and what would need to change for software quality to become a business-level priority rather than a final engineering checkpoint?**

Organizations accept the risk because release targets are tied to immediate customer, revenue, and product commitments, and defect costs often appear later across several teams. Quality becomes a business priority only when leaders measure production incidents, customer impact, security exposure, rework costs, and delayed revenue alongside release speed.

**Sauce Labs is positioning
[AURA](https://www.businesswire.com/news/home/20260722320853/en/Sauce-Labs-Launches-AURA-to-Close-the-AI-Code-Verification-Gap)
as a closed-loop platform that authors, executes, and analyzes tests while learning from each release. How does this differ technically and operationally from AI-assisted test generation, self-healing test scripts, or other automation tools already used by engineering teams?**

Most AI testing tools address a specific task, such as generating a test or repairing a broken locator. AURA connects the full process by understanding application intent, authoring and executing tests, analyzing failures, and feeding production behavior back into development. It can automatically handle many changes and bring a person into the process when the application’s meaning or expected behavior has changed. In addition, the tests it generates are stable, meaning they do not need to be modified when changes that do not impact semantics occur in applications, browsers, devices and the like. Finally, since AURA embeds within itself a test execution cloud, it is able to offload the entire process from a developer or quality engineering team.

**AURA is designed to verify software against “business intent.” How is that intent defined and translated into testable requirements, who is responsible for approving it, and how does the platform handle requirements that are ambiguous, incomplete, or open to interpretation?**

Business intent comes from product requirements, acceptance criteria, business rules, user journeys, and the way customers actually use the application. Product leaders define the expected outcome, and engineering and quality teams translate that outcome into behavior the system can verify. When requirements are incomplete or ambiguous, AURA should surface the uncertainty and ask for human approval before changing the expected result.

**Sauce Labs reports that enterprises using AURA have experienced 90% fewer production incidents, 47% faster release cycles, and reclaimed 38% of engineering capacity. How were these outcomes measured, over what deployment periods, and what independent validation was used to distinguish AURA’s impact from other organizational or engineering changes?**

Across enterprise deployments, we measured changes in production incidents, release-cycle speed, and engineering capacity after teams implemented AURA. Those deployments saw more than 90% fewer production incidents, 47% faster release cycles, and 38% of engineering capacity reclaimed, with the results independently validated. Customers such as Walmart and Keller Williams have also reported significant gains in release frequency, test coverage and cycle time.

**The research found that 64% of organizations increased quality assurance headcount even as incidents continued to rise. Why can’t enterprises solve the verification gap simply by hiring more testers, and how do you expect the responsibilities of developers, quality engineers, and site reliability teams to change as testing becomes more autonomous?**

AI can increase code volume much faster than a company can increase its testing headcount, and adding people also creates more handoffs and coordination. Developers will need to define intent clearly, quality engineers will focus more on risk, coverage, and governance, and site reliability teams will feed production behavior back into the release process. Agents can handle repetitive execution and analysis at the scale this new development model requires.

**As AI agents gain responsibility for authoring, running, and interpreting tests, where must humans retain decision-making authority? What types of uncertainty, security risk, or potential customer impact should automatically stop a release or trigger human review?**

Humans must retain final authority over release decisions, particularly when judgment, customer impact, or business risk is involved. AI agents can automate tedious, repeatable, and clearly defined testing tasks, but humans should approve production releases whenever code or test results cannot be fully understood, explained, or reproduced. Review should also be mandatory when requirements are unclear, security vulnerabilities are possible, third-party components have not been adequately validated, or failures could affect revenue, sensitive data, customer experience, or mission-critical operations.

In those situations, unexplained behavior, inconsistent test results or insufficient evidence of release readiness should automatically stop the release.

We have seen cases in our customers where a test that appeared “flaky,” passing inconsistently without an apparent failure pattern, would in many cases be ignored. But well-governed processes in certain of these customers required due diligence and with the help from our platform, they were able to track the failure to a subtle but critical timing-based defect that could have led to major impacts if released, with a very high cost.

**You have also worked with the Ethical AI Governance Group and the World Economic Forum’s Safe Systems and Technologies working group. As AI-generated code and autonomous testing become more deeply connected, what governance standards will enterprises need to ensure that faster software creation does not introduce new systemic, security, or accountability risks?**

The faster AI can create software, the stronger the verification and governance layer has to become. This layer has many parts.  Enterprises must have clear boundaries around what agents can decide autonomously, with human review required when there is uncertainty around business intent, security, compliance, or meaningful semantic change. They also need traceability into what an agent changed, why it changed it, and what evidence supported the release decision. Ultimately, governance should be measured by the quality and predictability of what reaches production, such as specifically tracking how frequently generated code causes incidents within 90 days of release, not by how much faster AI can generate code.

*Thank you for the great interview, readers who wish to learn more should visit
[Sauce Labs](https://saucelabs.com/)
.*