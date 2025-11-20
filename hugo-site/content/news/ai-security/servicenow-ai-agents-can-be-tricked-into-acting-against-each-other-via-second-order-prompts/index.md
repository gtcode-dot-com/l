---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-19T12:00:06.666464+00:00'
exported_at: '2025-11-19T12:00:09.071631+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html
structured_data:
  about: []
  author: ''
  description: Second-order prompt injection exploits ServiceNow agent discovery,
    enabling unauthorized actions unless configurations and monitoring are tightened.
  headline: ServiceNow AI Agents Can Be Tricked Into Acting Against Each Other via
    Second-Order Prompts
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: ServiceNow AI Agents Can Be Tricked Into Acting Against Each Other via Second-Order
  Prompts
updated_at: '2025-11-19T12:00:06.666464+00:00'
url_hash: 9c0468e498e6215abcad032432cab72d19723574
---

**

Nov 19, 2025
**

Ravie Lakshmanan

AI Security / SaaS Security

Malicious actors can exploit default configurations in ServiceNow's Now Assist generative artificial intelligence (AI) platform and leverage its agentic capabilities to conduct prompt injection attacks.

The second-order prompt injection, according to AppOmni, makes use of Now Assist's agent-to-agent discovery to execute unauthorized actions, enabling attackers to copy and exfiltrate sensitive corporate data, modify records, and escalate privileges.

"This discovery is alarming because it isn't a bug in the AI; it's expected behavior as defined by certain default configuration options,"
[said](https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection)
Aaron Costello, chief of SaaS Security Research at AppOmni.

"When agents can discover and recruit each other, a harmless request can quietly turn into an attack, with criminals stealing sensitive data or gaining more access to internal company systems. These settings are easy to overlook."

The attack is made possible because of agent discovery and agent-to-agent collaboration capabilities within ServiceNow's Now Assist. With Now Assist offering the ability to automate functions such as help-desk operations, the scenario opens the door to possible security risks.

For instance, a benign agent can parse specially crafted prompts embedded into content it's allowed access to and recruit a more potent agent to read or change records, copy sensitive data, or send emails, even when built-in prompt injection protections are enabled.

The most significant aspect of this attack is that the actions unfold behind the scenes, unbeknownst to the victim organization. At its core, the cross-agent communication is enabled by controllable configuration settings, including the default LLM to use, tool setup options, and channel-specific defaults where the agents are deployed -

* The underlying large language model (LLM) must support agent discovery (both Azure OpenAI LLM and Now LLM, which is the default choice, support the feature)
* Now Assist agents are automatically grouped into the same team by default to invoke each other
* An agent is marked as being discoverable by default when published

While these defaults can be useful to facilitate communication between agents, the architecture can be susceptible to prompt injections when an agent whose main task is to read data that's not inserted by the user invoking the agent.

"Through second-order prompt injection, an attacker can redirect a benign task assigned to an innocuous agent into something far more harmful by employing the utility and functionality of other agents on its team," AppOmni said.

"Critically, Now Assist agents run with the privilege of the user who started the interaction unless otherwise configured, and not the privilege of the user who created the malicious prompt and inserted it into a field."

Following responsible disclosure, ServiceNow said the behavior is intended to be this way, but the company has since updated its documentation to provide more clarity on the matter. The findings demonstrate the need for strengthening AI agent protection, as enterprises increasingly incorporate AI capabilities into their workflows.

To mitigate such prompt injection threats, it's advised to configure supervised execution mode for privileged agents, disable the autonomous override property ("sn\_aia.enable\_usecase\_tool\_execution\_mode\_override"), segment agent duties by team, and monitor AI agents for suspicious behavior.

"If organizations using Now Assist's AI agents aren't closely examining their configurations, they're likely already at risk," Costello added.