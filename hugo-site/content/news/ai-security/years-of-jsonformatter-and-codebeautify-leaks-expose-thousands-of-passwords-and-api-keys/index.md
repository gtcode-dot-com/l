---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-26T00:00:07.586432+00:00'
exported_at: '2025-11-26T00:00:10.014597+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/years-of-jsonformatter-and-codebeautify.html
structured_data:
  about: []
  author: ''
  description: Researchers uncovered 5GB of leaked credentials from JSONFormatter
    and CodeBeautify, exposing sensitive data across critical sectors.
  headline: Years of JSONFormatter and CodeBeautify Leaks Expose Thousands of Passwords
    and API Keys
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/years-of-jsonformatter-and-codebeautify.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Years of JSONFormatter and CodeBeautify Leaks Expose Thousands of Passwords
  and API Keys
updated_at: '2025-11-26T00:00:07.586432+00:00'
url_hash: f9ad4ef37459df7aabc0d5eed6a9912654c28048
---

**

Nov 25, 2025
**

Ravie Lakshmanan

Data Exposure / Cloud Security

New research has found that organizations in various sensitive sectors, including governments, telecoms, and critical infrastructure, are pasting passwords and credentials into online tools like JSONformatter and CodeBeautify that are used to format and validate code.

Cybersecurity company watchTowr Labs
[said](https://labs.watchtowr.com/stop-putting-your-passwords-into-random-websites-yes-seriously-you-are-the-problem/)
it captured a dataset of over 80,000 files on these sites, uncovering thousands of usernames, passwords, repository authentication keys, Active Directory credentials, database credentials, FTP credentials, cloud environment keys, LDAP configuration information, helpdesk API keys, meeting room API keys, SSH session recordings, and all kinds of personal information.

This includes five years of historical JSONFormatter content and one year of historical CodeBeautify content, totalling over 5GB worth of enriched, annotated JSON data.

Organizations impacted by the leak span critical national infrastructure, government, finance, insurance, banking, technology, retail, aerospace, telecommunications, healthcare, education, travel, and, ironically, cybersecurity sectors.

"These tools are extremely popular, often appearing near the top of search results for terms like 'JSON beautify' and 'best place to paste secrets' (probably, unproven) -- and used by a wide variety of organizations, organisms, developers, and administrators in both enterprise environments and for personal projects," security researcher Jake Knott said in a report shared with The Hacker News.

Both tools also offer the ability to save a formatted JSON structure or code, turning it into a semi-permanent, shareable link with others – effectively allowing anyone with access to the URL to access the data.

As it happens, the sites not only provide a
[handy](https://jsonformatter.org/recentLinksPage/json)
[Recent Links page](https://codebeautify.org/recentLinksPage)
to list all recently saved links, but also follow a predictable URL format for the shareable link, thereby making it easier for a bad actor to retrieve all URLs using a simple crawler -

* https://jsonformatter.org/{id-here}
* https://jsonformatter.org/{formatter-type}/{id-here}
* https://codebeautify.org/{formatter-type}/{id-here}

Some examples of leaked information include Jenkins secrets, a cybersecurity company exposing encrypted credentials for sensitive configuration files, Know Your Customer (KYC) information associated with a bank, a major financial exchange's AWS credentials linked to Splunk, and Active Directory credentials for a bank.

To make matters worse, the company said it uploaded fake AWS access keys to one of these tools, and found bad actors attempting to abuse them 48 hours after it was saved. This indicates that valuable information exposed through these sources is being scraped by other parties and tested, posing severe risks.

"Mostly because someone is already exploiting it, and this is all really, really stupid," Knott said. "We don't need more AI-driven agentic agent platforms; we need fewer critical organizations pasting credentials into random websites."

When checked by The Hacker News, both JSONFormatter and CodeBeautify have temporarily disabled the save functionality, claiming they are "working on to make it better" and implementing "enhanced NSFW (Not Safe For Work) content prevention measures."

watchTowr said that the save functionality was disabled by these sites likely in response to the research. "We suspect this change occurred in September in response to communication from a number of the affected organizations we alerted," it added.