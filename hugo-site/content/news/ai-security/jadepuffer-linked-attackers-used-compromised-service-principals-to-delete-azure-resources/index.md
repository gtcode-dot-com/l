---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T00:49:29.804721+00:00'
exported_at: '2026-10-06T00:49:33.965589+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
structured_data:
  about: []
  author: ''
  description: JADEPUFFER used compromised Azure service principals to delete most
    targeted storage accounts in an 18-hour intrusion, Microsoft says.
  headline: JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete
    Azure Resources
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure
  Resources
updated_at: '2026-10-06T00:49:29.804721+00:00'
url_hash: b2d877fcb67a5cac43e6e2ca4f9095f4215eb60d
---

The threat actor known as JADEPUFFER has been observed orchestrating destructive actions within a Microsoft Azure environment using compromised service principals.

Microsoft, which is tracking the activity under the name
**Storm-3168**
, has called it an evolution of the threat actor's tradecraft. The attack took place in early June 2026 over a period of about 18 hours.

"The destructive operations were facilitated by compromising service principals and targeted Azure Storage Accounts, SQL databases, Key Vaults, Function Apps, recovery protection locks, Virtual Machines, and App Services," researchers Yossi Weizman and Tushar Mudi, along with the Microsoft Security Research team,
[said](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
.

JADEPUFFER was
[first documented](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html)
by Sysdig, describing it as the first-ever ransomware operation run end-to-end with the help of a large language model (LLM). The agentic attack exploited a known security flaw in Langflow (CVE-2025-3248) to break in, harvested credentials, burrowed deeper into the network, encrypted Nacos service configuration files, dropped the original database tables, and left a ransom note demanding a Bitcoin payment.

While the attack was found to have leveraged MySQL's built-in AES\_ENCRYPT() function to perform the encryption step,  the same Langflow instance was subsequently targeted by the threat actor a second time using a compiled Go-based ransomware strain codenamed
[ENCFORGE](https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html)
.

ENCFORGE is specifically built for the artificial intelligence (AI) infrastructure, scanning for nearly 180 file extensions spanning model checkpoints, vector databases, training datasets, and embedding indices, along with macOS-centric files like Keychain stores, Xcode project files, and Apple Pages and Numbers documents.

"An autonomous agent reasoned about its targets, harvested and reused credentials, moved laterally, established persistence, and destroyed a database, narrating its own intent the entire way," Sysdig noted at the time. "None of the individual techniques were novel or sophisticated. What is notable, however, is that an AI model strung them together into a complete ransomware operation against neglected internet-facing infrastructure."

Microsoft, in its analysis, said it observed two compromised service principals linked to the same tenant, with one used for reconnaissance and resource discovery and the second for destructive operations and credential collection.

The enumeration activity targeted Azure Virtual Machines, subscriptions, resource groups, and resources for close to 16 hours, carrying out over 300 read operations during the time period. The second compromised service principal also engaged in some discovery operation of its own 90 minutes later, enumerating virtual machines and resource groups across two subscriptions within five seconds.

After 16 hours, the second service principal also successfully enumerated Azure App Service configuration stores, likely in an attempt to look for exposed credentials. Soon after, the service principal is said to have conducted more than 150 destructive or credential collection-related operations in 35 minutes.

In all, the destructive sequence lasted for about seven minutes and involved over 100 storage account deletion attempts. Also targeted were an Azure Key Vault, Function App, and App Service plan, as well as multiple Azure SQL databases. However, each of the database deletion attempts ended up in failure due to the use of an unsupported API version for the Azure SQL database resource type.

"Most Azure Storage accounts targeted by the threat actor were successfully deleted," Microsoft said. "However, Azure resource locks and storage account-level deletion protection blocked deletion attempts for few of the storage accounts, demonstrating the value of independent safeguards that remain effective even when a compromised identity has broad administrative permissions."

It's unclear how the service principal was compromised, but Microsoft said it observed its client ID, client secret, and tenant ID had been previously exposed in plaintext in a public GitHub issue by an employee of the impacted organization. Although the secret was removed, it remained accessible through the public edit history.

Microsoft said it has also detected repeated probing from Storm-3168 linked infrastructure against several Azure App services for different customers, adding that the attacks are likely automated or scripted given the division of work using multiple service principals and the timing between the different operations.

The end goal of the attack is assessed to be ransomware-aligned, as it led to the deletion of numerous Azure resources in addition to backup and recovery-related resources, suggesting the threat actor was looking to impair the victim's ability to recover from the destructive activity. However, no ransom note or successful data exfiltration was observed in connection with the intrusion.

"This activity highlights a broader shift toward AI-orchestrated attacks, where threat actors can coordinate complex post-compromise operations across cloud environments with greater speed and scale," Microsoft said. "As these capabilities evolve, defenders must similarly use AI to investigate and respond across large environments."