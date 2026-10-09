---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-20T16:15:13.582468+00:00'
exported_at: '2026-01-20T16:15:15.997727+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html
structured_data:
  about: []
  author: ''
  description: Three vulnerabilities in Anthropic’s MCP Git server allow prompt injection
    attacks that can read or delete files and, in some cases, lead to RCE.
  headline: Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution
updated_at: '2026-01-20T16:15:13.582468+00:00'
url_hash: c3941ab0886b398417d0d637992314565daff457
---

**

Ravie Lakshmanan
**

Jan 20, 2026

Vulnerability / Artificial Intelligence

A set of three security vulnerabilities has been disclosed in
[mcp-server-git](https://pypi.org/project/mcp-server-git/)
, the official Git Model Context Protocol (
[MCP](https://github.com/modelcontextprotocol/servers)
) server maintained by Anthropic, that could be exploited to read or delete arbitrary files and execute code under certain conditions.

"These flaws can be exploited through prompt injection, meaning an attacker who can influence what an AI assistant reads (a malicious README, a poisoned issue description, a compromised webpage) can weaponize these vulnerabilities without any direct access to the victim's system," Cyata researcher Yarden Porat
[said](https://cyata.ai/blog/cyata-research-breaking-anthropics-official-mcp-server/)
in a report shared with The Hacker News.

Mcp-server-git is a Python package and an MCP server that provides a set of built-in tools to read, search, and manipulate Git repositories programmatically via large language models (LLMs).

The security issues, which have been addressed in versions 2025.9.25 and 2025.12.18 following responsible disclosure in June 2025, are listed below -

* **[CVE-2025-68143](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-5cgr-j3jf-jw3v)**
  (CVSS score: 8.8 [v3] / 6.5 [v4]) - A path traversal vulnerability arising as a result of the git\_init tool accepting arbitrary file system paths during repository creation without validation (Fixed in version 2025.9.25)
* **[CVE-2025-68144](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-9xwc-hfwc-8w59)**
  (CVSS score: 8.1 [v3] / 6.4 [v4]) - An argument injection vulnerability arising as a result of git\_diff and git\_checkout functions passing user-controlled arguments directly to git CLI commands without sanitization (Fixed in version 2025.12.18)
* **[CVE-2025-68145](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-j22h-9j4x-23w5)**
  (CVSS score: 7.1 [v3] / 6.3 [v4]) - A path traversal vulnerability arising as a result of a missing path validation when using the --repository flag to limit operations to a specific repository path (Fixed in version 2025.12.18)

Successful exploitation of the above vulnerabilities could allow an attacker to turn any directory on the system into a Git repository, overwrite any file with an empty diff, and access any repository on the server.

In an attack scenario documented by Cyata, the three vulnerabilities could be chained with the
[Filesystem MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
to write to a ".git/config" file (typically located within the hidden .git directory) and achieve remote code execution by triggering a call to git\_init by means of a prompt injection.

* Use git\_init to create a repo in a writable directory
* Use the Filesystem MCP server to write a malicious .git/config with a clean filter
* Write a .gitattributes file to apply the filter to certain files
* Write a shell script with the payload
* Write a file that triggers the filter
* Call git\_add, which executes the clean filter, running the payload

In response to the findings, the git\_init tool has been removed from the package and adds extra validation to prevent path traversal primitives. Users of the Python package are recommended to update to the latest version for optimal protection.

"This is the canonical Git MCP server, the one developers are expected to copy," Shahar Tal, CEO and co-founder of Agentic AI security company Cyata, said. "If security boundaries break down even in the reference implementation, it's a signal that the entire MCP ecosystem needs deeper scrutiny. These are not edge cases or exotic configurations, they work out of the box."