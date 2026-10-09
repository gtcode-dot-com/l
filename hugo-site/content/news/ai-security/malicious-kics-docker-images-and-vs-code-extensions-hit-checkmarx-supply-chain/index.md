---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-22T20:15:13.493911+00:00'
exported_at: '2026-04-22T20:15:15.712963+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html
structured_data:
  about: []
  author: ''
  description: Malicious KICS Docker tags and VS Code versions 1.17.0, 1.19.0 enabled
    data exfiltration, risking exposed infrastructure secrets.
  headline: Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply
    Chain
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply Chain
updated_at: '2026-04-22T20:15:13.493911+00:00'
url_hash: f9be8dd752ca1e2022c3ec1aee6bf8272f02eaca
---

**

Ravie Lakshmanan
**

Apr 22, 2026

Cloud Security / Software Security

Cybersecurity researchers have warned of malicious images pushed to the official "
[checkmarx/kics](https://hub.docker.com/r/checkmarx/kics)
" Docker Hub repository.

In an alert published today, software supply chain security company Socket
[revealed](https://socket.dev/blog/checkmarx-supply-chain-compromise)
that unknown threat actors managed to have overwritten existing tags, including v2.1.20 and alpine, while also introducing a new v2.1.21 tag that does not correspond to an official release. The Docker repository has been archived as of writing.

"Analysis of the poisoned image indicates that the bundled KICS binary was modified to include data collection and exfiltration capabilities not present in the legitimate version," Socket said.

"The malware could generate an uncensored scan report, encrypt it, and send it to an external endpoint, creating a serious risk for teams using KICS to scan infrastructure-as-code files that may contain credentials or other sensitive configuration data."

Further analysis of the incident has uncovered that related Checkmarx developer tooling may also have been affected, such as recent Microsoft Visual Studio Code extension releases that come with malicious code to download and run a remote addon through the Bun runtime.

"The behavior appeared in versions 1.17.0 and 1.19.0, was removed in 1.18.0, and relied on a hardcoded GitHub URL to fetch and run additional JavaScript without user confirmation or integrity verification," Socket added.

Organizations that may have used the affected KICS image to scan Terraform, CloudFormation, or Kubernetes configurations should treat any secrets or credentials exposed to those scans as likely compromised.

"The evidence suggests this is not an isolated Docker Hub incident, but part of a broader supply chain compromise affecting multiple Checkmarx distribution channels," the company noted.

The Hacker News has contacted Checkmarx for further information, and we will update the story if we hear back.

*(This is a developing story. Please check back for more details.)*