---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T03:16:50.986402+00:00'
exported_at: '2026-10-07T03:16:52.908480+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html
structured_data:
  about: []
  author: ''
  description: Dell fixes six CSM flaws enabling authentication bypass, storage credential
    access, and cluster-wide privilege escalation.
  headline: Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes
    Nodes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes
updated_at: '2026-10-07T03:16:50.986402+00:00'
url_hash: 0214f46e5aeb5bf71898c1e290c3c42e43f8fd0c
---

**

Ravie Lakshmanan
**

Oct 02, 2026

Vulnerability / Cloud Security

Dell has
[released](https://www.dell.com/support/kbdoc/en-us/000515771/dsa-2026-448-security-update-for-dell-container-storage-modules-multiple-vulnerabilities)
security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems.

The vulnerabilities are listed below -

* **CVE-2026-63688**
  (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server that an unauthenticated remote attacker could exploit to obtain unauthorized access to storage backend administrator credentials for all registered storage arrays.
* **CVE-2026-63692**
  (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the authorization proxy and tenant service that an unauthenticated network attacker could exploit to bypass authentication controls and gain administrative-level privileges.
* **CVE-2026-67269**
  (CVSS score: 9.9) - An improper privilege management vulnerability in the ContainerStorageModule Custom Resource reconciler that a low-privilege remote attacker could exploit to escalate privileges and gain root-level access on cluster nodes.
* **CVE-2026-54472**
  (CVSS score: 9.8) - A use of hard-coded credentials vulnerability in the CSM Authorization module that a remote unauthenticated attacker could exploit to forge cryptographically valid administrative tokens and gain unauthorized administrative access to the CSM Authorization proxy.
* **CVE-2026-61421**
  (CVSS score: 9.8) - A use of hard-coded cryptographic key vulnerability in the JWT authentication component of karavi-authorization that a remote unauthenticated attacker with knowledge of this publicly available signing secret could exploit to forge authentication tokens and gain administrative privileges.
* **CVE-2026-67273**
  (CVSS score: 9.6) - An improper neutralization of special elements used in a template engine vulnerability that a low-privilege attacker with remote access could exploit to escalate privileges, access sensitive information, and carry out unauthorized RBAC tampering.

"This vulnerability is considered critical as it enables a complete bypass of the csm-authorization security model, allowing an attacker to gain full administrative control over the storage infrastructure spanning all five supported Dell storage product families," Dell said about CVE-2026-63688.

As for CVE-2026-63692, Dell noted that successful exploitation could enable an unauthenticated attacker to gain complete administrative control over the authorization service, and allow them to access or manipulate storage resources across all tenants.

The PC maker also noted that an attacker can exploit CVE-2026-67269 to compromise all nodes in a Kubernetes cluster through a single custom resource submission. CVE-2026-54472, on the other hand, can be weaponized to sidestep authentication controls for the CSM Authorization proxy and enable unauthorized management of storage access policies across all connected tenants. Dell is recommending that customers apply the updates and rotate any JWT signing secrets.

"Successful exploitation grants the attacker cluster-wide read access to Kubernetes Secrets and the ability to create cluster-scoped RBAC resources, effectively bypassing the intended Kubernetes access controls," Dell said in its advisory for CVE-2026-67273.

The flaws, which affect all versions of CSM prior to 1.17.0, have been addressed in 1.18.0. There are no workarounds or mitigations other than updating to the latest version. With vulnerabilities in Dell products (
[CVE-2021-21551](https://thehackernews.com/2022/10/hackers-exploiting-dell-driver.html)
and
[CVE-2026-22769](https://thehackernews.com/2026/02/dell-recoverpoint-for-vms-zero-day-cve.html)
) having come under active exploitation in recent years, it's essential to apply the necessary fixes for optimal protection.