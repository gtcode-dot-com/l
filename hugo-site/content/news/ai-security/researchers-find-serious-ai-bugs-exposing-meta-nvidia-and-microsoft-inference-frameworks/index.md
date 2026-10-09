---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-14T16:15:52.617080+00:00'
exported_at: '2025-11-14T16:15:55.482821+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/researchers-find-serious-ai-bugs.html
structured_data:
  about: []
  author: ''
  description: Researchers reveal RCE flaws in AI inference engines and Cursor IDE
    from unsafe code reuse.
  headline: Researchers Find Serious AI Bugs Exposing Meta, Nvidia, and Microsoft
    Inference Frameworks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/researchers-find-serious-ai-bugs.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Find Serious AI Bugs Exposing Meta, Nvidia, and Microsoft Inference
  Frameworks
updated_at: '2025-11-14T16:15:52.617080+00:00'
url_hash: 9546a7d948ce431cb6104d527b7eb2b4bec71204
---

Cybersecurity researchers have uncovered critical remote code execution vulnerabilities impacting major artificial intelligence (AI) inference engines, including those from Meta, Nvidia, Microsoft, and open-source PyTorch projects such as vLLM and SGLang.

"These vulnerabilities all traced back to the same root cause: the overlooked unsafe use of ZeroMQ (ZMQ) and Python's pickle deserialization," Oligo Security researcher Avi Lumelsky
[said](https://www.oligo.security/blog/shadowmq-how-code-reuse-spread-critical-vulnerabilities-across-the-ai-ecosystem)
in a report published Thursday.

At its core, the issue stems from what has been described as a pattern called
**ShadowMQ**
, in which the insecure deserialization logic has propagated to several projects as a result of code reuse.

The root cause is a vulnerability in Meta's Llama large language model (LLM) framework (
[CVE-2024-50050](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html)
, CVSS score: 6.3/9.3) that was patched by the company last October. Specifically, it involved the use of ZeroMQ's recv\_pyobj() method to deserialize incoming data using Python's pickle module.

This, coupled with the fact that the framework exposed the ZeroMQ socket over the network, opened the door to a scenario where an attacker can execute arbitrary code by sending malicious data for deserialization. The issue has also been addressed in the pyzmq Python library.

Oligo has since discovered the same pattern recurring in other inference frameworks, such as NVIDIA TensorRT-LLM, Microsoft Sarathi-Serve, Modular Max Server, vLLM, and SGLang.

"All contained nearly identical unsafe patterns: pickle deserialization over unauthenticated ZMQ TCP sockets," Lumelsky said. "Different maintainers and projects maintained by different companies – all made the same mistake."

Tracing the origins of the problem, Oligo found that in at least a few cases, it was the result of a direct copy-paste of code. For example, the vulnerable file in SGLang says it's adapted by vLLM, while Modular Max Server has borrowed the same logic from both vLLM and SGLang, effectively perpetuating the same flaw across codebases.

The issues have been assigned the following identifiers -

* **[CVE-2025-30165](https://github.com/vllm-project/vllm/security/advisories/GHSA-9pcc-gvx5-r5wm)**
  (CVSS score: 8.0) - vLLM (While the issue is not fixed, it has been addressed by switching to the V1 engine by default)
* **[CVE-2025-23254](https://nvidia.custhelp.com/app/answers/detail/a_id/5648/~/security-bulletin%3A-nvidia-tensorrt-llm---april-2025)**
  (CVSS score: 8.8) - NVIDIA TensorRT-LLM (Fixed in version 0.18.2)
* **[CVE-2025-60455](https://github.com/modular/modular/commit/10620059fb5c47fb0c30e5d21a8ff3b8d622fba4)**
  (CVSS score: N/A) - Modular Max Server (Fixed)
* Sarathi-Serve (Remains unpatched)
* SGLang (Implemented
  [incomplete fixes](https://github.com/sgl-project/sglang/issues/5569)
  )

With inference engines acting as a crucial component within AI infrastructures, a successful compromise of a single node could permit an attacker to execute arbitrary code on the cluster, escalate privileges, conduct model theft, and even drop malicious payloads like cryptocurrency miners for financial gain.

"Projects are moving at incredible speed, and it's common to borrow architectural components from peers," Lumelsky said. "But when code reuse includes unsafe patterns, the consequences ripple outward fast."

The disclosure comes as a new report from AI security platform Knostic has found that it's possible to compromise Cursor's new
[built-in browser](https://cursor.com/docs/agent/browser)
via JavaScript injection techniques, not to mention leverage a malicious extension to facilitate JavaScript injection in order to take control of the developer workstation.

The first attack involves registering a rogue local Model Context Protocol (
[MCP](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)
) server that bypasses Cursor's controls to allow an attacker to replace the login pages within the browser with a bogus page that harvests credentials and exfiltrates them to a remote server under their control.

"Once a user downloaded the MCP server and ran it, using an mcp.json file within Cursor, it injected code into Cursor's browser that led the user to a fake login page, which stole their credentials and sent them to a remote server," security researcher Dor Munis
[said](https://www.knostic.ai/blog/mcp-hijacked-cursor-browser)
.

Given that the AI-powered source code editor is essentially a fork of Visual Studio Code, a bad actor could also craft a malicious extension to inject JavaScript into the running IDE to execute arbitrary actions, including marking harmless Open VSX extensions as "malicious."

"JavaScript running inside the Node.js interpreter, whether introduced by an extension, an MCP server, or a poisoned prompt or rule, immediately inherits the IDE's privileges: full file-system access, the ability to modify or replace IDE functions (including installed extensions), and the ability to persist code that reattaches after a restart," the company
[said](https://www.knostic.ai/blog/demonstrating-code-injection-vscode-cursor)
.

"Once interpreter-level execution is available, an attacker can turn the IDE into a malware distribution and exfiltration platform."

To counter these risks, it's essential that users disable Auto-Run features in their IDEs, vet extensions, install MCP servers from trusted developers and repositories, check what data and APIs the servers access, use API keys with minimal required permissions, and audit MCP server source code for critical integrations.