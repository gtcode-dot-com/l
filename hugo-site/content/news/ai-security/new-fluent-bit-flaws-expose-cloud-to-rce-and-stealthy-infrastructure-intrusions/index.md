---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-25T00:00:08.384641+00:00'
exported_at: '2025-11-25T00:00:11.216190+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/new-fluent-bit-flaws-expose-cloud-to.html
structured_data:
  about: []
  author: ''
  description: Fluent Bit, deployed in billions of containers, has five new flaws
    enabling log tampering, remote code execution, and cloud takeover paths.
  headline: New Fluent Bit Flaws Expose Cloud to RCE and Stealthy Infrastructure Intrusions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/new-fluent-bit-flaws-expose-cloud-to.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Fluent Bit Flaws Expose Cloud to RCE and Stealthy Infrastructure Intrusions
updated_at: '2025-11-25T00:00:08.384641+00:00'
url_hash: 986240f8d00887196960dfdc38187890e41bcc13
---

**

Nov 24, 2025
**

Ravie Lakshmanan

Vulnerability / Container Security

Cybersecurity researchers have discovered five vulnerabilities in
[Fluent Bit](https://github.com/fluent/fluent-bit)
, an open-source and lightweight telemetry agent, that could be chained to compromise and take over cloud infrastructures.

The security defects "allow attackers to bypass authentication, perform path traversal, achieve remote code execution, cause denial-of-service conditions, and manipulate tags," Oligo Security said in a
[report](https://www.oligo.security/blog/critical-vulnerabilities-in-fluent-bit-expose-cloud-environments-to-remote-takeover)
shared with The Hacker News.

Successful exploitation of the flaws could enable attackers to disrupt cloud services, manipulate data, and burrow deeper into cloud and Kubernetes infrastructure. The list of identified vulnerabilities is as follows -

* **CVE-2025-12972**
  - A path traversal vulnerability stemming from the use of unsanitized
  [tag values](https://docs.fluentbit.io/manual/concepts/key-concepts#tag)
  to generate output filenames, making it possible to write or overwrite arbitrary files on disk, enabling log tampering and remote code execution.
* **CVE-2025-12970**
  - A stack buffer overflow vulnerability in the Docker Metrics input plugin (in\_docker) that could allow attackers to trigger code execution or crash the agent by creating containers with excessively long names.
* **CVE-2025-12978**
  - A vulnerability in the tag-matching logic lets attackers spoof trusted tags – which are assigned to every event ingested by Fluent Bit – by guessing only the first character of a Tag\_Key, allowing an attacker to reroute logs, bypass filters, and inject malicious or misleading records under trusted tags.
* **CVE-2025-12977**
  - An improper input validation of tags derived from user-controlled fields, allowing an attacker to inject newlines, traversal sequences, and control characters that can corrupt downstream logs.
* **CVE-2025-12969**
  - A missing security.users authentication in the
  [in\_forward plugin](https://docs.fluentbit.io/manual/data-pipeline/outputs/forward)
  that's used to receive logs from other Fluent Bit instances using the
  [Forward protocol](https://docs.fluentd.org/input/forward)
  , allowing attackers to send logs, inject false telemetry, and flood a security product's logs with false events.

"The amount of control enabled by this class of vulnerabilities could allow an attacker to breach deeper into a cloud environment to execute malicious code through Fluent Bit, while dictating which events are recorded, erasing or rewriting incriminating entries to hide their tracks after an attack, injecting fake telemetry, and injecting plausible fake events to mislead responders," researchers said.

The CERT Coordination Center (CERT/CC), in an independent advisory,
[said](https://kb.cert.org/vuls/id/761751)
many of these vulnerabilities require an attacker to have network access to a Fluent Bit instance, adding they could be used for authentication bypass, remote code execution, service disruption, and tag manipulation.

Following responsible disclosure, the issues have been addressed in
[versions 4.1.1](https://github.com/fluent/fluent-bit/releases/tag/v4.1.1)
and 4.0.12 released last month. Amazon Web Services (AWS), which also engaged in coordinated disclosure, has urged customers running Fluentbit to update to the latest version for optimal protection.

Given Fluent Bit's popularity within enterprise environments, the shortcomings have the potential to impair access to cloud services, allow data tampering, and seize control of the logging service itself.

Other recommended actions include avoiding use of dynamic tags for routing, locking down output paths and destinations to prevent tag-based path expansion or traversal, mounting /fluent-bit/etc/ and configuration files as read-only to block runtime tampering, and running the service as non-root users.

The development comes more than a year after Tenable detailed a flaw in Fluent Bit's built-in HTTP server (
[CVE-2024-4323](https://thehackernews.com/2024/05/linguistic-lumberjack-vulnerability.html)
aka Linguistic Lumberjack) that could be exploited to achieve denial-of-service (DoS), information disclosure, or remote code execution.