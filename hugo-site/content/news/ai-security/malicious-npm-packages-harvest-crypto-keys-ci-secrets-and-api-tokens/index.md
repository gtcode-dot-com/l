---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-23T12:15:14.653845+00:00'
exported_at: '2026-02-23T12:15:17.034040+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html
structured_data:
  about: []
  author: ''
  description: 19 npm packages spread SANDWORM_MODE worm, stealing tokens, crypto
    keys, CI secrets, and AI API keys via MCP injection
  headline: Malicious npm Packages Harvest Crypto Keys, CI Secrets, and API Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious npm Packages Harvest Crypto Keys, CI Secrets, and API Tokens
updated_at: '2026-02-23T12:15:14.653845+00:00'
url_hash: ed2362663afc23ebb8b5a22a5bd606e29dc01daf
---

Cybersecurity researchers have disclosed what they say is an active "Shai-Hulud-like" supply chain worm campaign that has leveraged a cluster of at least 19 malicious npm packages to enable credential harvesting and cryptocurrency key theft.

The campaign has been codenamed
**SANDWORM\_MODE**
by supply chain security company Socket. As with prior
[Shai-Hulud attack waves](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html)
, the malicious code embedded into the packages comes with capabilities to siphon system information, access tokens, environment secrets, and API keys from developer environments and automatically propagate by abusing stolen npm and GitHub identities to extend its reach.

"The sample retains Shai-Hulud hallmarks and adds GitHub API exfiltration with DNS fallback, hook-based persistence, SSH propagation fallback, MCP server injection with embedded prompt injection targeting AI coding assistants, and LLM API Key harvesting," the company
[said](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning)
.

The packages, published to npm by two npm publisher aliases, official334 and javaorg, are listed below -

* claud-code@0.2.1
* cloude-code@0.2.1
* cloude@0.3.0
* crypto-locale@1.0.0
* crypto-reader-info@1.0.0
* detect-cache@1.0.0
* format-defaults@1.0.0
* hardhta@1.0.0
* locale-loader-pro@1.0.0
* naniod@1.0.0
* node-native-bridge@1.0.0
* opencraw@2026.2.17
* parse-compat@1.0.0
* rimarf@1.0.0
* scan-store@1.0.0
* secp256@1.0.0
* suport-color@1.0.1
* veim@2.46.2
* yarsg@18.0.1

Also identified are four sleeper packages that do not incorporate any malicious features -

* ethres
* iru-caches
* iruchache
* uudi

The packages go beyond npm-based propagation by including a weaponized GitHub Action that harvests CI/CD secrets and exfiltrates them via HTTPS with DNS fallback. They also feature a destructive routine that acts as a kill switch by triggering home directory wiping should it lose access to GitHub and npm. The wiper functionality is currently off by default.

Another significant component of the malware is an "McpInject" module that specifically targets AI coding assistants by deploying a malicious model context protocol (
[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
) server and injecting it into their tool configurations. The MCP server masquerades as a legitimate tool provider and registers three seemingly-harmless
[tools](https://modelcontextprotocol.io/legacy/concepts/tools)
, each of which embeds a prompt injection to read the contents of ~/.ssh/id\_rsa, ~/.ssh/id\_ed25519, ~/.aws/credentials, ~/.npmrc, and .env files, stage them in a local directory for later exfiltration.

The module targets Claude Code, Claude Desktop, Cursor, Microsoft Visual Studio Code (VS Code) Continue, and Windsurf. It also harvests API keys for nine large language models (LLM) providers: Anthropic, Cohere, Fireworks AI, Google, Grok, Mistral, OpenAI, Replicate, and Together.

What's more, the payload contains a polymorphic engine that's configured to call a local
[Ollama](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html)
instance with the
[DeepSeek Coder](https://deepseekcoder.github.io/)
model to rename variables, rewrite control flow, insert junk code, and encode strings to evade detection. While the engine is turned off in the currently detected packages, the inclusion of the feature suggests that the operators are looking to release more iterations of the malware in the future.

The entire attack chain unfolds over two stages: a first-stage component that captures credentials and cryptocurrency keys and then loads a secondary stage that subsequently performs deeper harvesting of credentials from password managers, worm-like propagation, MCP injection, and full exfiltration. The second stage is not activated until 48 hours (along with a per-machine jitter of up to 48 additional hours) have elapsed.

Users who have installed any of the aforementioned packages are advised to remove them with immediate effect, rotate npm/GitHub tokens and CI secrets, and review any package.json, lockfiles, and .github/workflows/ for any unexpected changes.

"Several feature flags and guardrails still suggest the threat actor is iterating on capabilities (for example, toggles that disable destructive routines or polymorphic rewriting in some builds)," Socket said. "However, the same worm code appearing across multiple typosquatting packages and publisher aliases indicates intentional distribution rather than an accidental release."

"The destructive and propagation behaviors remain real and high-risk, and defenders should treat these packages as active compromise risks rather than benign test artifacts."

The disclosure comes as
[Veracode](https://www.veracode.com/blog/malicious-npm-package-hiding-in-plain-pixels/)
and
[JFrog](https://research.jfrog.com/post/three-stages-deep-a-malicious-npm-package/)
detailed two other malicious npm packages named "buildrunner-dev" and "eslint-verify-plugin," respectively, that are designed to deliver a remote access trojan (RAT) targeting Windows, macOS, and Linux systems. The .NET malware deployed by buildrunner-dev is
[Pulsar RAT](https://thehackernews.com/2025/06/malicious-pypi-package-masquerades-as.html)
, an open-source RAT delivered via a PNG image hosted on i.ibb[.]co.

Eslint-verify-plugin, on the other hand, "masquerades as a legitimate ESLint utility while deploying a sophisticated, multi-stage infection chain targeting macOS and Linux environments," JFrog said.

On Linux, the package deploys a
[Poseidon](https://github.com/MythicAgents/poseidon)
agent for the Mythic C2 framework. It facilitates a wide range of post-exploitation capabilities, including file operations, credential harvesting, and lateral movement. The macOS infection sequence executes
[Apfell](https://github.com/MythicAgents/apfell)
, a JavaScript for Automation (JXA) agent for macOS, to conduct extensive data collection and create a new macOS user with admin privileges.

Some of the data stolen by the agent are as follows -

* System information
* System credentials via a fake password dialog
* Google Chrome browser bookmarks
* Clipboard contents
* Files associated with iCloud Keychain and Chrome cookies, login data, and bookmarks
* Screenshots
* File metadata

"The eslint-verify-plugin package is a direct example of how a malicious npm package can escalate from a simple installation hook to a full-system compromise," JFrog said. "By masquerading as a legitimate utility, the attackers successfully concealed a multi-stage infection chain."

The findings also follow a report from Checkmarx, which flagged a rogue VS Code extension known as "solid281" that impersonates the official Solidity extension, but harbors covert features to execute a heavily obfuscated loader automatically upon
[application startup](https://code.visualstudio.com/api/references/activation-events#onStartupFinished)
and drop ScreenConnect on Windows and a Python reverse shell on macOS and Linux machines.

"This mirrors broader patterns reported by other teams: Solidity developers appear to be targeted specifically, including campaigns that used fake Solidity extensions to install ScreenConnect and then deploy follow-on payloads," Checkmarx
[noted](https://checkmarx.com/zero-post/solidity-devs-targeted-again-malicious-vs-code-extension-drops-screenconnect-based-remote-access-trojan-rat/)
.