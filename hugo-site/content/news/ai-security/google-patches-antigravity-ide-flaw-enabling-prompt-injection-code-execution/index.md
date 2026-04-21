---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-21T12:15:14.436120+00:00'
exported_at: '2026-04-21T12:15:16.718417+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
structured_data:
  about: []
  author: ''
  description: Antigravity Strict Mode bypass disclosed Jan 7, 2026, patched Feb 28,
    enables arbitrary code execution via fd -X flag.
  headline: Google Patches Antigravity IDE Flaw Enabling Prompt Injection Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Patches Antigravity IDE Flaw Enabling Prompt Injection Code Execution
updated_at: '2026-04-21T12:15:14.436120+00:00'
url_hash: 4b2b714d047c3622e6e663ccd6ee8cfa4a9a437d
---

**

Ravie Lakshmanan
**

Apr 21, 2026

Vulnerability / Artificial Intelligence

Cybersecurity researchers have discovered a vulnerability in Google's agentic integrated development environment (IDE), Antigravity, that could be exploited to achieve code execution.

The flaw, since patched, combines Antigravity's permitted file-creation capabilities with an insufficient input sanitization in Antigravity's native file-searching tool, find\_by\_name, to bypass the program's
[Strict Mode](https://antigravity.google/docs/strict-mode)
, a restrictive security configuration that limits network access, prevents out-of-workspace writes, and ensures all commands are being run within a
[sandbox context](https://antigravity.google/docs/sandbox-mode)
.

"By injecting the -X (exec-batch) flag through the Pattern parameter [in the find\_by\_name tool], an attacker can force fd to execute arbitrary binaries against workspace files," Pillar Security researcher Dan Lisichkin
[said](https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity)
in an analysis.

"Combined with Antigravity's ability to create files as a permitted action, this enables a full attack chain: stage a malicious script, then trigger it through a seemingly legitimate search, all without additional user interaction once the prompt injection lands."

The attack takes advantage of the fact that the find\_by\_name tool call is executed before any of the constraints associated with Strict Mode are enforced and is instead interpreted as a native tool invocation, leading to arbitrary code execution. While the Pattern parameter is designed to accept a filename search pattern to trigger a file and directory search using fd through find\_by\_name, it's undermined by a lack of strict validation, passing the input directly to the underlying fd command.

An attacker could, therefore, leverage this behavior to stage a malicious file and inject malicious commands into the Pattern parameter to trigger the execution of the payload.

"The critical flag here is -X (exec-batch). When passed to fd, this flag executes a specified binary against each matched file," Pillar explained. "By crafting a Pattern value of -Xsh, an attacker causes fd to pass matched files to sh for execution as shell scripts."

Alternatively, the attack can be initiated via an indirect prompt injection without having to compromise a user's account. In this approach, an unsuspecting user pulls a seemingly harmless file from an untrusted source that contains hidden attacker-controlled comments instructing the artificial intelligence (AI) agent to stage and trigger the exploit.

Following responsible disclosure on January 7, 2026, Google addressed the shortcoming as of February 28.

"Tools designed for constrained operations become attack vectors when their inputs are not strictly validated," Lisichkin said. "The trust model underpinning security assumptions, that a human will catch something suspicious, does not hold when autonomous agents follow instructions from external content."

The findings coincide with the discovery of a number of now-patched security flaws in various AI-powered tools -

* Anthropic Claude Code Security Review, Google Gemini CLI Action, and GitHub Copilot Agent have been found vulnerable to prompt injection via GitHub comments, allowing an attacker to turn pull request (PR) titles, issue bodies, and issue comments into attack vectors for API key and token theft. The prompt injection attack has been codenamed
  [Comment and Control](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/)
  , as it weaponizes an AI agent's
  [elevated access](https://www.manifold.security/blog/gateway-gap-ai-agent-security)
  and its ability to process untrusted user input to execute malicious instructions.
* "The pattern likely applies to any AI agent that ingests untrusted GitHub data and has access to execution tools in the same runtime as production secrets -- and beyond GitHub Actions, to any agent that processes untrusted input with access to tools and secrets: Slack bots, Jira agents, email agents, deployment automation," security researcher Aonan Guan said. "The injection surface changes, but the pattern is the same."
* Another vulnerability in Claude Code,
  [discovered by Cisco](https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code)
  , is capable of poisoning the coding agent's memory and maintaining persistence across every project and every session, even after a system reboot. The attack essentially utilizes a
  [software supply chain attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)
  as an initial access vector to launch a malicious payload that can tamper with the model's memory files for malicious purposes (e.g., framing insecure practices as necessary architectural requirements) and appends a shell alias to the user's shell configuration.
* AI code editor Cursor has been found susceptible to a critical living-off-the-land (LotL) vulnerability chain dubbed
  [NomShub](https://www.straiker.ai/blog/nomshub-cursor-remote-tunneling-sandbox-breakout)
  that makes it possible for a malicious repository to clandestinely hijack a developer's machine by leveraging a mix of indirect prompt injection, a command parser sandbox escape via shell builtins like export and cd, and Cursor's built-in remote tunnel, granting the attacker persistent, undetected shell access simply upon opening the repository in the IDE.
* Once persistent access is obtained, the attacker can connect to the machine without triggering the prompt injection again or raising any security alerts. Because Cursor is a legitimate binary that's signed and notarized, the adversary has unfettered access to the underlying host, gaining full file system access and command execution capabilities.
* "A human attacker would need to chain together multiple exploits and maintain persistent access," Straiker researchers Karpagarajan Vikkii and Amanda Rousseau said. "The AI agent does this autonomously, following the injected instructions as if they were legitimate development tasks."
* A novel attack called
  [ToolJack](https://www.preamble.com/blogs/tooljack-hijacking-an-ai-agents-perception-through-bridge-protocol-exploitation)
  has been found to allow a local attacker to manipulate an AI agent's perception of its environment and corrupts the tool's ground truth to produce unintended downstream effects, including poisoned data, fabricated business intelligence, and bogus recommendations.
* "Where MCP Tool Shadowing poisons tool descriptions to influence agent behavior across servers and ConfusedPilot contaminates a RAG retrieval pool, ToolJack operates as a real-time infrastructure attack on the communication conduit itself," Preamble researcher Jeremy McHugh said. "It does not wait for the agent to organically encounter poisoned data. It synthesizes a fabricated reality mid-execution, demonstrating that compromising the protocol boundary yields control over the agent's entire perception."
* Severe indirect prompt injection vulnerabilities have been identified in Microsoft Copilot Studio (aka
  [ShareLeak](https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520)
  or CVE-2026-21520, CVSS score: 7.5) and Salesforce Agentforce (aka
  [PipeLeak](https://www.capsulesecurity.io/blog-post/pipeleak-the-lead-that-stole-your-database-exploiting-salesforce-agentforce-with-indirect-prompt-injection)
  ) that could enable attackers to exfiltrate sensitive data through an external SharePoint form or a simple lead from a form submission, respectively.
* "The attack exploits the lack of input sanitization and inadequate separation between system instructions and user-supplied data," Capsule Security researcher Bar Kaduri said about CVE-2026-21520. PipeLeak is similar to
  [ForcedLeak](https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html)
  in that the system processes public-facing lead form inputs as trusted instructions, thus allowing an attacker to embed malicious prompts that override the agent's intended behavior.
* A trio of vulnerabilities have been identified in Claude that, when chained together in an attack codenamed
  [Claudy Day](https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability)
  , allow an attacker to silently hijack a user's chat session and exfiltrate sensitive data with a single click. The attack pipeline requires no additional integrations, tools, or Model Context Protocol (MCP) servers.
* The attack works by embedding hidden instructions in a crafted Claude URL ("claude[.]ai/new?q=..."), encapsulating it in an open redirect on claude[.]com to make it appear legitimate, and then running it as a benign-looking Google ad that, when clicked, triggers the attack by silently redirecting the victim to the crafted "claude[.]ai/new?q=..." URL containing the invisible prompt injection.
* "Combined with Google Ads, which validates URLs by hostname, this allowed an attacker to place a search ad displaying a trusted claude.com URL that, when clicked, silently redirected the victim to the injection URL. Not a phishing email. A Google search result, indistinguishable from the real thing," Oasis Security said.

In research published last week, Manifold Security also
[revealed](https://www.manifold.security/blog/spoofed-git-identity-ai-code-reviewer)
how a Claude-powered GitHub Actions workflow ("claude-code-action") can be tricked into approving and merging a pull request containing malicious code with just two
[Git configuration commands](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
by spoofing a trusted developer's identity.

At its core, the attack entails setting Git's
[user.name and user.email properties](https://git-scm.com/docs/git-config)
to those of a well-known developer (in this case, AI researcher Andrej Karpathy). This metadata trickery becomes a problem when an AI system treats it as a signal of trust. An attacker could exploit this unverified metadata to deceive the AI agent into executing unintended actions.

"On the first submission, Claude flagged the PR for manual review, noting that author reputation alone wasn't sufficient justification," researchers Ax Sharma and Oleksandr Yaremchuk said. "Reopening and resubmitting the same PR led to its approval. The AI overrode its own better judgment on retry. This non-determinism is the point. You cannot build a security control on a system that changes its mind."