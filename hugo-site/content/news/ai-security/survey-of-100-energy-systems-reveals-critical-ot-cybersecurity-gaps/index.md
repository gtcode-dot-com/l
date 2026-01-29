---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T12:15:13.383667+00:00'
exported_at: '2026-01-29T12:15:16.954707+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/survey-of-100-energy-systems-reveals.html
structured_data:
  about: []
  author: ''
  description: Study of 100+ energy OT sites reveals unpatched devices, flat networks,
    and hidden assets, with critical issues detected within minutes.
  headline: Survey of 100+ Energy Systems Reveals Critical OT Cybersecurity Gaps
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/survey-of-100-energy-systems-reveals.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Survey of 100+ Energy Systems Reveals Critical OT Cybersecurity Gaps
updated_at: '2026-01-29T12:15:13.383667+00:00'
url_hash: 64622d20179a1dc3eb5c8cd24801d44cd89b1cd1
---

A study by
[OMICRON](https://www.omicroncybersecurity.com/en/?utm_medium=cpc&utm_source=article&utm_campaign=2601-bdopuc-hackernews&utm_content=link)
has revealed widespread cybersecurity gaps in the operational technology (OT) networks of substations, power plants, and control centers worldwide. Drawing on data from more than 100 installations, the analysis highlights recurring technical, organizational, and functional issues that leave critical energy infrastructure vulnerable to cyber threats.

The findings are based on several years of deploying
[OMICRON's intrusion detection system (IDS) StationGuard](https://www.omicroncybersecurity.com/en/products?utm_medium=cpc&utm_source=article&utm_campaign=2601-bdopuc-hackernews&utm_content=link)
in protection, automation, and control (PAC) systems. The technology, which monitors network traffic passively, has provided deep visibility into real-world OT environments. The results underscore the growing attack surface in energy systems and the challenges operators face in securing aging infrastructure and complex network architectures.

|  |
| --- |
|  |
| Connection of an IDS in PAC systems (circles indicate mirror ports) |

StationGuard deployments, often carried out during security assessments, revealed vulnerabilities such as unpatched devices, insecure external connections, weak network segmentation, and incomplete asset inventories. In many cases, these security weaknesses were identified within the first 30 minutes of connecting to the network. Beyond security risks, the assessments also uncovered operational issues like VLAN misconfigurations, time synchronization errors, and network redundancy problems.

In addition to technical shortcomings, the findings point to organizational factors that contribute to these risks — including unclear responsibilities for OT security, limited resources, and departmental silos. These findings reflect a growing trend across the energy sector: IT and OT environments are converging rapidly, yet security measures often fail to keep pace. How are utilities adapting to these complex risks, and what gaps remain that could leave critical systems exposed?

## **Why OT Networks Need Intrusion Detection**

The ability to detect security incidents is an integral part of most security frameworks and guidelines, including the NIST Cybersecurity Framework, IEC 62443, and the ISO 27000 standard series. In substations, power plant control systems, and control centers, many devices operate without standard operating systems, making it impossible to install endpoint detection software. In such environments, detection capabilities must be implemented at the network level.

OMICRON's StationGuard deployments typically use network mirror ports or Ethernet TAPs to passively monitor communication. Besides detecting intrusions and cyber threats, the IDS technology provides key benefits, including:

* Visualization of network communication
* Identification of unnecessary services and risky network connections
* Automatic asset inventory creation
* Detection of device vulnerabilities based on this inventory

## **Assessing Risks: Methodology Behind the Findings**

The report is based on years of IDS installations. The first installation dates back to 2018. Since then, several hundred installations and security assessments have been conducted at substations, power plants, and control centers in dozens of countries. The findings are grouped into three categories:

1. Technical security risks
2. Organizational security issues
3. Operational and functional problems

In most cases, critical security and operational issues were detected within minutes of connecting the IDS to the network.

Typically, sensors were connected to mirror ports on OT networks, often at gateways and other critical network entry points, to capture key communication flows. In many substations, bay-level monitoring was not required, as multicast propagation made the traffic visible elsewhere in the network.

## **Hidden Devices and Asset Blind Spots**

Accurate asset inventories are essential for securing complex energy systems. Creating and maintaining such directories manually is time-consuming and error-prone. To address this, OMICRON used both passive and active methods for automated asset discovery.

**Passive asset identification**
relies on existing system configuration description (SCD) files, standardized under IEC 61850-6, which contain detailed device information. However, passive monitoring alone proved insufficient in many cases, as essential data such as firmware versions are not transmitted in normal PAC communication.

**Active querying of device information**
, on the other hand, leverages the MMS protocol to retrieve nameplate data such as device names, manufacturers, model numbers, firmware versions, and sometimes even hardware identifiers. This combination of passive and active techniques provided a comprehensive asset inventory across installations.

|  |
| --- |
|  |
| Example of device information retrievable via SCL and MMS active querying |

## **Which Technical Cybersecurity Risks Are Most Common?**

OMICRON's analysis identified several recurring technical issues across energy OT networks:

* **Vulnerable PAC devices:**

  Many PAC devices were found to be operating with outdated firmware containing known vulnerabilities. A notable example is the CVE-2015-5374 vulnerability, which allows a denial-of-service attack on protective relays with a single UDP packet. Although patches have been available since 2015, numerous devices remain unpatched. Similar vulnerabilities in GOOSE implementations and MMS protocol stacks pose additional risks.
* **Risky external connections:**

  In several installations, undocumented external TCP/IP connections were found, in some cases exceeding 50 persistent connections to external IP addresses in a single substation.
* **Unnecessary insecure services:**

  Common findings included unused Windows file sharing services (NetBIOS), IPv6 services, license management services running with elevated privileges, and unsecured PLC debugging functions.
* **Weak network segmentation:**

  Many facilities operated as a single large flat network, allowing unrestricted communication between hundreds of devices. In some cases, even office IT networks were reachable from remote substations. Such architectures significantly increase the impact radius of cyber incidents.
* **Unexpected devices:**

  Untracked IP cameras, printers, and even automation devices frequently appeared on networks without being documented in asset inventories, creating serious blind spots for defenders.

## **The Human Factor: Organizational Weaknesses in OT Security**

Beyond technical flaws, OMICRON also observed recurring organizational challenges that exacerbate cyber risk. These include:

* Departmental boundaries between IT and OT teams
* Lack of dedicated OT security personnel
* Resource constraints are limiting the implementation of security controls

In many organizations, IT departments remain responsible for OT security — a model that often struggles to address the unique requirements of energy infrastructure.

## **When Operations Fail: Functional Risks in Substations**

The IDS deployments also revealed a range of operational problems unrelated to direct cyber threats but still affecting system reliability. The most common were:

* **VLAN issues**
  were by far the most frequent, often involving inconsistent VLAN tagging of GOOSE messages across the network.
* **RTU and SCD mismatches**
  led to broken communication between devices, preventing SCADA updates in several cases.
* **Time synchronization errors**
  ranged from simple misconfigurations to devices operating with incorrect time zones or default timestamps.
* **Network redundancy issues**
  involving RSTP loops and misconfigured switch chips caused severe performance degradation in some installations.

These operational weaknesses not only impact availability but can also amplify the consequences of cyber incidents.

|  |
| --- |
|  |
| Functional monitoring related alert messages |

## **What Can Utilities Learn from These Findings?**

The analysis of over 100 energy facilities highlights the urgent need for robust, purpose-built security solutions that are designed for the unique challenges of operational technology environments.

With its deep protocol understanding and asset visibility, the
**StationGuard**
**Solution**
provides security teams with the transparency and control needed to protect critical infrastructure. Its built-in allowlisting detects even subtle deviations from expected behavior, while its signature-based detection identifies known threats in real time.

The system's ability to monitor both IT and OT protocols — including IEC 104, MMS, GOOSE, and more — allows utilities to detect and respond to threats at every layer of their substation network. Combined with features like automated asset inventories, role-based access control, and seamless integration into existing security workflows,
**StationGuard**
enables organizations to strengthen resilience without disrupting operations.

To learn more about how
**StationGuard**
supports utilities in closing these critical security gaps, visit
[our website](https://www.omicroncybersecurity.com/en/products?utm_medium=cpc&utm_source=article&utm_campaign=2601-bdopuc-hackernews&utm_content=link)
.

|  |
| --- |
|  |
| StationGuard Solution |

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.