---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:41:29.172833+00:00'
exported_at: '2026-10-07T04:41:31.015697+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/the-credential-layer-is-expanding.html
structured_data:
  about: []
  author: ''
  description: GitGuardian found 28.65 million new hardcoded secrets in public GitHub
    commits in 2025, up 34% year over year.
  headline: The Credential Layer Is Expanding Faster Than Security Teams Can See It
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/the-credential-layer-is-expanding.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Credential Layer Is Expanding Faster Than Security Teams Can See It
updated_at: '2026-10-07T04:41:29.172833+00:00'
url_hash: 20616b5d110d0e27ee0a3b17b56f1029a3e1eed6
---

Every modern enterprise depends on credentials. This is how humans, systems, and now AI, all connect to data, services, and each other securely. GitGuardian helps secure that credential layer through three connected capabilities: Detect, Remediate, and Prevent. The journey starts with detection, because organizations first need to understand what credentials exist, where they live, and what they can access. This is the first of three articles we are releasing that explain the reason behind our mission.

—

Software production is accelerating beyond the growth assumptions that shaped many of today's security controls. GitHub COO Kyle Daigle said the platform had gone from roughly 1 billion commits during all of
[2025 to 2.9 billion commits in August 2026,](https://thenewstack.io/github-2-9b-monthly-commits/)
an annualized pace of over 14 billion for the 2026 reporting year. GitHub's own engineering team has gone further in its capacity planning, saying it moved from preparing for 10x scale to designing for a future that requires 30x today's scale as agentic development accelerated.

All of this code prodiction means more infrastructure and more secrets. More applications, new types of integrations, automations, and now agents, mean more systems need to authenticate to something else. Credential exposure has already been a problem of increasing scale.
[GitGuardian detected 28.65 million new hardcoded secrets in public GitHub commits in 2025](https://www.gitguardian.com/state-of-secrets-sprawl-report-2026)
, up 34% year over year. Leaked credentials associated with AI services increased 81%.

Security teams need to establish visibility into that expanding credential layer right now.

GitGuardian approaches credential-layer security through three connected stages: Detect, Remediate, and Prevent. Detection comes first because every action that follows depends on knowing which credentials actually exist, where they have spread, and what access they represent.

## **The credential layer has no convenient perimeter**

The credential layer is the collection of credentials connecting people, applications, infrastructure, and services across an enterprise.

Its perimeter follows the credentials themselves.

A developer will create a secret inside a sanctioned cloud account and later that same key, in plaintext, will appear in a repository or in a shared knowledgebase. Other secrets will be stored in an approved vault while a plaintext copies remain on the developer's laptop. More may be created outside security's normal vantage point through a personal project or a newly adopted AI service, especially by an increasingly growing number fo 'citizen developers' who now have access to coding agents.

The result is an attack surface that crosses all technology and ownership boundaries.

The same GitGuardian State of Secrets Sprawl 2026 research we referenced earlier shows how wide this surface has become. Internal repositories were roughly six times more likely than public repositories to contain at least one secret. Around 28% of secrets incidents originated entirely outside source-code repositories in collaboration and productivity systems.

That leaves security teams with a basic discovery challenge. Each scanner, vault, repository, or endpoint can describe the part of the credential layer it sees. The organization still needs a way to understand the combined population.

## **Every discovery source provides a partial picture**

Source control remains essential because hardcoded credentials leave durable evidence.

A credential removed from the current version of a file can remain in Git history. Copies can spread into other branches or repositories. Public exposure can put the value beyond the organization's control, making it extremely challenging for anyone to immediately notice.

Internal repositories reveal another large population. They contain the credentials developers and applications use during normal work, including access to cloud environments and internal services.

Collaboration systems expose a different part of the credential layer. Credentials get pasted into tickets while troubleshooting. They move through chat during handoffs. They can remain searchable long after the work that required them is finished.

## Developer laptops are holding all the credentials

Developers are at the heart of all of this creation, use and placement of secrets. Until recently it was considered normal form to use local local environment files to hold application secrets using command-line tools cache credentials used to reach cloud services. The danger of an unscrubbed local shell history, which can preserve values long after someone has forgotten they were entered, seemed rather low.

Then the attackers shifted.  The end of 2025 brought new waves of infostealer attacks like Shai-Hulud and S1ingularity, which turned the developer laptop into a target and an entry point into the supply chain.

Every laptop is part of the credential layer and the secrets they hold need to be mapped.

Repository scanning shows credentials that reached source control. Public monitoring reveals exposures outside corporate repositories. Endpoint discovery identifies secrets that may never have entered a centrally monitored system.

The credential layer only becomes visible when those perspectives are connected.

## **Attackers already search across those boundaries**

Attackers have already adapted to the fact that credentials exist across managed and unmanaged environments.

Compromised credentials already accounted for 22% of initial access according to the the
[2026 Verizon Data Breach Investigations Report](https://blog.gitguardian.com/initial-access-changed-the-attack-path-did-not-findinds-from-the-verizon-2026-dbir/)
. Their data also found corporate credentials on unmanaged devices, which drove a significant number of the breaches they researched. Enterprise access can quickly cross a boundary that security teams consider meaningful.

And their data reporting period ended before the information stealer worms became as wide spread as we saw in early 2026.

This self propagating malware running on an endpoint can search browser data, local files, and application storage. It can collect whatever authentication material is available without caring which team created it or which security product was supposed to govern it.

Developer systems offer an especially valuable targets. A developer machine may authenticate to source control and cloud infrastructure. It can also hold local credentials for applications under development. Compromising that endpoint can expose access that spans several otherwise separate parts of the enterprise.

Security teams need to perform that inventory before an attacker does.

## **The developer laptop is being shared with a new type of user**

The developer endpoint has always accumulated credentials because building software requires connecting systems. But now there is a new type of internal actor that has access to that same machine, AI agents.

Coding agents can read files, execute commands, and interact with external services. Model Context Protocol connections can give those agents access to additional tools. Each connection introduces another place where authentication and authorization need to be established.

GitGuardian's analysis of systems compromised during the Shai-Hulud 2 supply-chain campaign provides a rare view into the density of credentials on these machines. Across 6,943 compromised systems, researchers identified 33,185 unique secrets. Forty-four percent of compromised machines held more than 10 secrets, while 5% contained more than 100.

At the same time, how we are authenticating AI agents have introduced a new security hole. In the same report we saw 24,008 unique secrets in public MCP configuration files during 2025, of which, 2,117 could be verified as valid.

A security team that scans repositories can know a great deal about repositories. It still has limited visibility into credentials living on the machines where code is created, tested, and connected to external systems.

AI agents can do unexpected things with this access. It can be abused by attackers, but just as likely it can result in negative outcomes from the AI taking a surprising move, like deleting a production database.

Security teams need to understand what exactly these agents can access to understand the risk.

## **Discovery needs context around every credential**

Finding a secret provides the first coordinate. Security teams need the surrounding context to understand the risk it represents.

### Validity is one of the most immediate signals.

Unfortunately, most secrets stay valid far longer than they should. Ideally, any credential would be made just in time, and expire after use, but GitGuardian retested credentials that had been confirmed valid in 2022 and found that 64% were still valid in January 2026.

A credential can therefore remain useful to an attacker years after the original exposure.

### A secret's location adds another dimension to risk assessment.

A credential found once in an internal repository has one exposure history. The same credential appearing on a laptop and later in a public repository has traveled much farther. Every occurrence expands the set of people and systems that may have had access to it.

Credential fingerprinting can connect those appearances while preserving a single credential record. Seven detections of the same secret represent one credential with seven known exposures. Treating it that way produces a more accurate inventory and a clearer picture of how far it has spread.

### Ownership provides another layer.

Security teams need to know which user, workload, or application relies on the credential. Ownership connects the finding to the team responsible for managing the access, not just who created it, but what policy or governance does this fall under.

### The scope of permissions shows what the credential can do and the danger it brings.

A credential limited to a development service presents one scope of risk. A production credential with broad administrative permissions presents another. Validity and permission context together reveal which findings deserve the fastest attention.

### Dependencies complete more of the picture.

A credential can be highly exposed while still supporting critical workloads. Understanding those relationships gives the organization the information it will eventually need to rotate or revoke the credential safely.

Discovery should produce a credential record enriched with this context.

## **Security teams need a real denominator for their coverage metrics**

Many enterprises already have strong secrets-management programs.

Those systems provide valuable information about credentials already under management. They can show what is stored, who has access, and how the secret is being used.

The larger credential layer mapping determines how complete that coverage really is.

For example, a company might have 50,000 credentials stored in approved vaults while thousands more sit in plaintext in repositories, developer endpoints, or collaboration systems. But from their reporting, they show how the secrets they know about are accounted for, blind to the ones created outside of their planned paved paths. Some of those credentials may correspond to values already held in the vault. Others may exist completely outside any approved manager.

Security teams need to know how much of the credential population has an identified owner. They need to know how many active credentials can be connected to permissions and dependent workloads. They also need visibility into which credentials have crossed into public environments.

Those measurements depend on discovering the population first.

## **Everything is speeding up, including attackers**

Security programs built around periodic discovery will face increasing pressure as software production accelerates. This historic growth represents more than additional code.

GitGuardian's reports show, that over the time they have been researching this area, secret exposure has increased 1.6 times faster than the number of active developers.

Attackers are leveraging this while also accelerating their attack speeds.

CrowdStrike reported an average eCrime breakout time of
[29 minutes in 2025, with the fastest observed case reaching lateral movement in 27 seconds](https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/)
. Defenders need to react in terms of machine speed, as the days of a human executing an attack are now past us. The time available to respond will only continue to shrink.

The answer can not just be faster reaction, but a shift towards prevention. And that is not possible until you understand what you are trying to prevent, which in turn requires knowledge of what is surfaces you currently even have for credentials to leak into.

## **Detection builds the map for everything that follows**

The first step in controlling credential risk is understanding the credential layer the organization actually has.

That requires discovery across repositories, public exposure, and developer endpoints. It also requires context around every credential, including validity, ownership, permissions, and dependencies.

Vault coverage becomes one measurement inside that larger picture. Repository findings become another. Endpoint discoveries add credentials that may have remained invisible to central security systems.

Together, they create a usable inventory of the credential layer.

The approach of "detect, remediate, and prevent" starts with that inventory because remediation and prevention depend on it. Security teams need to know what exists before they can systematically remove risky credentials or stop new exposure from spreading.

The growth already underway raises the cost of waiting.

GitHub's move from 1 billion annual commits to a pace measured in hundreds of millions per week provides a glimpse of the software volume ahead. GitHub itself is preparing infrastructure for a future measured at 30 times today's scale. Every new application, agent, and integration can extend the credential layer further.

Security teams need
[visibility capable of expanding at the same pace](https://www.gitguardian.com/)
.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.