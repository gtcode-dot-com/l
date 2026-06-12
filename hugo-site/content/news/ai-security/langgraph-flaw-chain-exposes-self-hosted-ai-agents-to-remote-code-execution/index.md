---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:44:11.492617+00:00'
exported_at: '2026-06-12T21:44:12.815515+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html
structured_data:
  about: []
  author: ''
  description: Three patched LangGraph flaws could let attackers chain SQL injection
    and unsafe deserialization for RCE in self-hosted deployments.
  headline: LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution
updated_at: '2026-06-12T21:44:11.492617+00:00'
url_hash: 850f08119b5ca30c78593822d867cb25671c9e4b
---

**

Ravie Lakshmanan
**

Jun 12, 2026

Vulnerability / AI Security

Cybersecurity researchers have disclosed details of three now-patched security flaws impacting
[LangGraph](https://www.langchain.com/langgraph)
, including a critical vulnerability chain that could result in remote code execution.

LangGraph is an open-source framework created by LangChain to build complex, stateful, and multi-agent artificial intelligence (AI) agentic applications.

"An SQL injection in LangGraph's function could allow attackers to gain full control via remote code execution of a server by exploiting weaknesses in how the system processes and handles data," Check Point
[said](https://blog.checkpoint.com/research/when-your-ai-agents-memory-becomes-a-security-liability/)
.

The list of identified vulnerabilities is as follows -

* **[CVE-2025-67644](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-9rwj-6rc7-p77c)**
  (CVSS score: 7.3) - A SQL injection vulnerability exists in LangGraph's SQLite checkpoint implementation that allows attackers to manipulate SQL queries through metadata filter keys. (Affects langgraph-checkpoint-sqlite versions before 3.0.1)
* **[CVE-2026-28277](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-g48c-2wqr-h844)**
  (CVSS score: 6.8) - An unsafe
  [msgpack](https://msgpack.org/index.html)
  deserialization vulnerability in LangGraph that could be used to trigger object reconstruction when a checkpoint is loaded by an attacker who can modify checkpoint data. (Affects langgraph versions before 1.0.10)
* **[CVE-2026-27022](https://github.com/langchain-ai/langgraphjs/security/advisories/GHSA-5mx2-w598-339m)**
  (CVSS score: 6.5) - A RediSearch Query Injection in @langchain/langgraph-checkpoint-redis that can be used to bypass access controls. (Affects @langchain/langgraph-checkpoint-redis versions before 1.0.1)

"The vulnerability chain is exploitable in self-hosted deployments using the SQLite or Redis checkpointer with user-controlled filter input," Check Point said. "LangChain's managed platform (LangSmith Deployment), is not affected."

Security researcher Yarden Porat, who is credited with discovering and reporting all three flaws,
[said](https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/)
CVE-2025-67644 and CVE-2026-28277 could be chained to achieve remote code execution.

Specifically, the attack chain hinges on the application exposing the
[get\_state\_history()](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state_history)
endpoint, which then allows an attacker to retrieve historical checkpoints based on their metadata. It requires the following steps -

* The attacker prepares a msgpack payload containing instructions to execute arbitrary code.
* The attacker sends a malicious filter parameter that exploits the SQL injection vulnerability to return a fake checkpoint row to the database query results, where the checkpoint column contains attacker-controlled serialized data.
* When the application processes the query results, it deserializes the malicious checkpoint's BLOB.
* The attacker exploits the unsafe deserialization vulnerability to execute the attacker's payload, giving them remote code execution on the server.

LangGraph has described CVE-2026-28277 as a post-exploitation issue, where successful exploitation requires the ability to write attacker-controlled checkpoint data and turn that into code execution in the application runtime, and it does not pose any risks to existing LangSmith-hosted deployments.

In such a scenario, this escalation from write access to checkpoint store" to code execution may "expose runtime secrets or provide access to other systems the runtime can reach," LangGraph maintainers said. "The described threat model requires an attacker to tamper with the checkpoint persistence layer used by the deployment; typical hosted configurations are designed to prevent such access."

Check Point said the findings illustrate how classic vulnerability classes like SQL injection can become more potent when they manifest inside AI agent frameworks that carry elevated access and trust, thereby opening the door to sensitive data exposure.

Users are advised to apply the latest fixes, implement authentication for self-hosted LangGraph servers, avoid long-lived static secrets, enforce network segmentation, treat AI agents as privileged identities, and apply the principle of least privilege (PoLP) to limit the agent's access footprint.