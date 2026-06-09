---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T02:58:24.338728+00:00'
exported_at: '2026-06-09T02:58:26.314867+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html
structured_data:
  about: []
  author: ''
  description: VS Code flaw exposes GitHub OAuth tokens via one-click attack on GitHub.dev,
    enabling private repo access and token theft.
  headline: One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens
updated_at: '2026-06-09T02:58:24.338728+00:00'
url_hash: 73d3eedfbf67e6b3e6eed2965b69e33523e32ce9
---

**

Ravie Lakshmanan
**

Jun 03, 2026

Vulnerability / Software Development

Cybersecurity researchers have disclosed a one-click attack via Microsoft Visual Studio Code (VS Code) that makes it possible to steal a user's GitHub token.

"Just by clicking a link, it's possible for an attacker to steal a GitHub token that can read and write to your repos, including private ones," security researcher Ammar Askar
[said](https://blog.ammaraskar.com/github-token-stealing/)
.

GitHub supports a feature called
[GitHub.dev](https://github.com/github/dev)
that runs as a
[lightweight web-based source code editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)
in the web browser's sandbox by launching a VS Code environment. It allows users to send pull requests and make commits.

"This functionality is achieved by github.com POSTing over an OAuth token to github.dev that allows it to interact with GitHub on your behalf," Askar said. "The token is not scoped to the particular repo you interacted with, meaning it has full access to every other repo that you have access to."

In a nutshell, the vulnerability allows attackers to install malicious VS Code extensions that steal GitHub OAuth tokens when they are passed to GitHub.dev by exploiting a
[message-passing mechanism](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
between the main VS Code window and
[webviews](https://code.visualstudio.com/api/extension-guides/webview)
. Webviews are used to render Markdown previews or edit Jupyter notebooks.

Specifically, the exploit runs malicious JavaScript inside an untrusted webview to simulate keypresses (aka keydown events) in the main editor window, open the Command Palette by triggering "Ctrl+Shift+P," and install an attacker-controlled extension that extracts the GitHub OAuth token sent to GitHub.dev and queries the GitHub API to enumerate all private repositories the victim can access.

It's worth noting the approach also leverages a VS Code feature called
[local workspace extensions](https://code.visualstudio.com/updates/v1_89#_local-workspace-extensions)
that allows an extension to be directly installed without presenting any additional
[trust dialog prompt](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security#_extension-publisher-trust)
as long as it's placed in the ".vscode/extensions" folder within that workspace, effectively bypassing the publisher trust check.

"This is just a small hiccup though, one of the things that extensions can do as part of their package.json is to contribute extra keybindings to VS Code," the researcher explained. "Since we can reliably trigger keybindings, we can just add a keybind for whatever VS Code command we want, such as installing an extension while skipping the trusted publisher check."

The researcher also noted GitHub was
[notified](https://github.com/microsoft/vscode/issues/319593)
of the vulnerability on June 2, 2026, an hour after which details of the issue were made public knowledge, citing Microsoft's
[handling](https://blog.ammaraskar.com/vscode-rce/)
of
[VS Code-related bugs](https://starlabs.sg/blog/2025/05-breaking-out-of-restricted-mode-xss-to-rce-in-visual-studio-code/)
in the past. As of writing, Microsoft has acknowledged the vulnerability and noted that it's working on a fix.

"To clarify, this issue does not affect VS Code Desktop," Alexandru Dima, a partner software engineering manager at Microsoft, said.

### Update

Following the publication of the story, Microsoft told The Hacker News that the vulnerability was addressed on June 3, 2026, at 7:30 a.m. PST. "This issue has been mitigated for our services and no customer action is required," a Microsoft spokesperson said.

*(The story was updated after publication to include a response from Microsoft.)*