---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-27T18:35:32.577248+00:00'
exported_at: '2026-09-27T18:35:35.412043+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
structured_data:
  about: []
  author: ''
  description: A DeepSeek Harness flaw let attacker-supplied text push AI agents to
    disable the file sandbox; fixed npm releases start at 0.1.2-alpha.2.
  headline: DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without
    Approval
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without
  Approval
updated_at: '2026-09-27T18:35:32.577248+00:00'
url_hash: 6546338aa1f2b8220a857bfd74a6fb5763c10cd0
---

A flaw in
**DeepSeek Harness**
, DeepSeek's open-source tool for running AI coding agents on a developer's machine, let a sandboxed agent turn off its own sandbox with a single command.

The tool runs an agent's commands inside an operating-system sandbox, so that an agent working on untrusted files cannot write outside its workspace. The agent could remove that limit by calling the tool's own web interface on the same machine, and its commands would then run outside the sandbox without an approval prompt.

It worked on a default installation until DeepSeek fixed the tool on August 27, and it required attacker-supplied text that the agent read to prompt it to make the call.

The flaw is tracked as
**CVE-2026-82533**
. VulnCheck, which assigned the identifier,
[published the record](https://www.vulncheck.com/advisories/deepseek-harness-alpha-1-authentication-bypass-via-host-header-spoofing)
on September 8 and rated the flaw 9.4 out of 10.

[OX Research](https://www.ox.security/blog/cve-2026-82533-deepseek-harness-ai-agent-sandbox-escape/)
, the security firm that reported the flaw, said one shell command was enough. The command invoked the tool's local interface and set the agent's session to a mode called danger-full-access, which turns off the sandbox and stops approval prompts.

Ordinary commands did not need approval to begin with. Approval was applied only when a command requested broader access than the session already had, and this call did not request it. It changed the session's setting instead.

OX said it checked that the sandbox had been working before the escape. It ran two sessions from the same default settings and gave both the same command. The session that had made the call wrote to a folder outside its workspace, and the other was blocked.

The sandbox only covers files. The
[command-line reference for the affected release](https://github.com/deepseek-ai/deepseek-harness/blob/dsh-v0.1.1-rc.2/apps/cli/reference/README.md)
says that under the default setting, writes stay inside the workspace and temporary folders, while "reads and network access are not confined."

That left the tool's own interface reachable from inside the sandbox. The tool also provides the agent's shell with the address of that interface and the current session's identifier, so the agent does not have to look for them.

The interface had no authentication. In the affected release, the
[check that determined whether a request could reach it](https://github.com/deepseek-ai/deepseek-harness/blob/dsh-v0.1.1-rc.2/packages/client/connection/src/api-request-trust.ts)
read the request's Host header and never looked at where the connection originated. A comment in that file says the check "is not an auth layer."

That check is what the CVE record describes. Because it trusted a header the client supplies, a machine outside could claim to be local and drive the agent. The tool's command line refused to listen on all network interfaces, so reaching it from outside needed the user to have forwarded or proxied the port through a tunnel, an SSH forward, or an editor.

The same interface served a request to download a session's entire log. VulnCheck's advisory states that a caller who reaches the interface could retrieve all stored conversations without a key.

### Affected Versions and What to Install

Versions 0.1.1-rc.2 and earlier are affected. The record names 0.1.2-alpha.1 as the fixed version, but that version was never published to the npm registry, which is where the project's own instructions send users.

| Version | Status | Released |
| --- | --- | --- |
| 0.1.1-rc.2 and earlier | Affected | 0.1.1-rc.2 published August 21 |
| 0.1.2-alpha.1 | Fixed, on GitHub only | August 27, not on npm |
| 0.1.2-alpha.2 | First fixed release on npm | August 30 |
| 0.1.2-rc.1 | Current npm release, carries the fix | September 3 |

The Hacker News checked
[the npm registry](https://registry.npmjs.org/@deepseek-ai/dsh)
on September 9 and found that the first published release with the authentication change is 0.1.2-alpha.2, three days after the fix was pushed to GitHub.

1. Install 0.1.2-alpha.2 or later. The registry's current release is 0.1.2-rc.1.
2. If you installed through a third-party desktop app, check which version of the harness it ships.
3. If you cannot upgrade, stop the web interface when you are not using it, and remove any tunnel, proxy, or port forward that reaches it.

No source reviewed for this article offers a way to stop the escape from inside the sandbox on a default local installation while the tool is running. The August 13 report says limiting the address the tool listens on does not help, because the agent is already on the same machine.

The fix gives the interface an identity check. The tool now prints a one-time token at its startup address; the browser exchanges that token for a signed cookie, and
[every call to the interface requires the cookie](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/implemented/architecture/2026-08-24-browser-token-authentication.md)
.

What the fix does not change is the sandbox. In 0.1.2-rc.1, the same reference still says that reads and network access are not confined, and the agent's shell still receives the interface address. No source addresses whether an agent running inside its workspace can still obtain a valid session under the new scheme.

Third-party desktop builds ship their own copy of the harness, and which copy they ship is the wrapper maintainer's choice. One Windows build pinned 0.1.1-rc.2 in late August and moved to 0.1.3-alpha.1, which carries the fix, on
[September 6](https://github.com/Links2008/DeepSeek-Harness-Desktop/releases)
. Anyone who installed the harness through a wrapper should check which version it ships.

A coding-agent harness is worth attacking because it holds a shell. DeepSeek Harness runs an agent's commands under the account that started it.

The project's own
[safety notice](https://github.com/deepseek-ai/deepseek-harness/blob/master/SAFETY.md)
states that the software has not undergone a security audit and that sandboxing and approval prompts "do not guarantee isolation or prevent damage." It tells users not to rely on the tool as their only security control for untrusted work.

The repository had more than 216,000 stars on September 9, a count of accounts that bookmarked it rather than installations.

Researchers have repeatedly found coding agents escaping their sandboxes this year, including
[a set of flaws](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html)
in which a repository's own configuration caused agents to run attacker code outside their sandboxes.

### Community Reports Described the Same Escape in August

Two developers described the same escape on DeepSeek's own discussion board before the CVE existed. On August 13, one posted
[a report](https://github.com/deepseek-ai/deepseek-harness/discussions/250)
showing a process still held by the sandbox reaching the local interface and then switching the session to danger-full-access, with test output.

On August 14, another posted
[a report](https://github.com/deepseek-ai/deepseek-harness/discussions/853)
on the same interface, listing the requests it accepted without any credentials.

That second report also noted that the project had no security policy file and no private way to report a flaw. The project still has no security policy file.

OX Research reported the flaw to VulnCheck on August 24, by its own timeline, and VulnCheck credits Nir Zadok and Moshe Siman Tov Bustan. OX's post does not mention the earlier reports.

The Hacker News checked the repository's advisory list on September 9 and found no security advisory published.
[The release that carried the fix](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.2-alpha.1)
lists it among routine changes, as removing an old transport and requiring "one-time-token authentication for network access," with no security notice and no mention of the CVE.