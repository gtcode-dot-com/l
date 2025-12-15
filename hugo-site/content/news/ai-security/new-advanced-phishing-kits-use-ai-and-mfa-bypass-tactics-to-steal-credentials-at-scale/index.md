---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-15T00:03:12.594846+00:00'
exported_at: '2025-12-15T00:03:15.203272+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html
structured_data:
  about: []
  author: ''
  description: Researchers detail new AI and phishing kits that steal credentials,
    bypass MFA, and scale attacks across major services.
  headline: New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials
    at Scale
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials
  at Scale
updated_at: '2025-12-15T00:03:12.594846+00:00'
url_hash: b5618c11e1275aa8e5f9e09bcea6d908b31af59f
---

Cybersecurity researchers have documented four new phishing kits named
**BlackForce, GhostFrame, InboxPrime AI, and Spiderman**
that are capable of facilitating credential theft at scale.

BlackForce, first detected in August 2025, is designed to steal credentials and perform Man-in-the-Browser (
[MitB](https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html)
) attacks to capture one-time passwords (OTPs) and bypass multi-factor authentication (MFA). The kit is sold on Telegram forums for anywhere between €200 ($234) and €300 ($351).

The kit, according to
[Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/technical-analysis-blackforce-phishing-kit)
researchers Gladis Brinda R and Ashwathi Sasi, has been used to impersonate over 11 brands, including Disney, Netflix, DHL, and UPS. It's said to be in active development.

"BlackForce features several evasion techniques with a blocklist that filters out security vendors, web crawlers, and scanners," the company said. "BlackForce remains under active development. Version 3 was widely used until early August, with versions 4 and 5 being released in subsequent months."

Phishing pages connected to the kit have been found to use JavaScript files with what has been described as "
[cache busting](https://www.keycdn.com/support/what-is-cache-busting)
" hashes in their names (e.g., "index-[hash].js"), thereby forcing the victim's web browser to download the latest version of the malicious script instead of using a cached version.

In a typical attack using the kit, victims who click on a link are redirected to a malicious phishing page, after which a server-side check filters out crawlers and bots, before serving them a page that's designed to mimic a legitimate website. Once the credentials are entered on the page, the details are captured and sent to a Telegram bot and a command-and-control (C2) panel in real-time using an HTTP client called
[Axios](https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html)
.

When the attacker attempts to log in with the stolen credentials on the legitimate website, an MFA prompt is triggered. At this stage, the MitB techniques are used to display a fake MFA authentication page to the victim's browser through the C2 panel. Should the victim enter the MFA code on the bogus page, it's collected and used by the threat actor to gain unauthorized access to their account.

"Once the attack is complete, the victim is redirected to the homepage of the legitimate website, hiding evidence of the compromise and ensuring the victim remains unaware of the attack," Zscaler said.

### GhostFrame Fuels 1M+ Stealth Phishing Attacks

Another nascent phishing kit that has gained traction since its discovery in September 2025 is GhostFrame. At the heart of the kit's architecture is a simple HTML file that appears harmless while hiding its malicious behavior within an embedded iframe, which leads victims to a phishing login page to steal Microsoft 365 or Google account credentials.

"The iframe design also allows attackers to easily switch out the phishing content, try new tricks or target specific regions, all without changing the main web page that distributes the kit," Barracuda security researcher Sreyas Shetty
[said](https://blog.barracuda.com/2025/12/04/threat-spotlight-ghostframe-phishing-kit)
. "Further, by simply updating where the iframe points, the kit can avoid being detected by security tools that only check the outer page."

Attacks using the GhostFrame kit commence with typical phishing emails that claim to be about business contracts, invoices, and password reset requests, but are designed to take recipients to the fake page. The kit uses anti-analysis and anti-debugging to prevent attempts to inspect it using browser developer tools, and generates a random subdomain each time someone visits the site.

The visible outer pages come with a loader script that's responsible for setting up the iframe and responding to any messages from the HTML element. This can include changing the parent page's title to impersonate trusted services, modifying the site favicon, or redirecting the top-level browser window to another domain.

In the final stage, the victim is sent to a secondary page containing the actual phishing components through the iframe delivered via the constantly changing subdomain, thereby making it harder to block the threat. The kit also incorporates a fallback mechanism in the form of a backup iframe appended at the bottom of the page in the event the loader JavaScript fails or is blocked.

### InboxPrime AI Phishing Kit Automates Email Attacks

If BlackForce follows the same playbook as other traditional phishing kits, InboxPrime AI goes a step further by leveraging artificial intelligence (AI) to automate mass mailing campaigns. It's advertised on a 1,300-member-strong Telegram channel under a malware-as-a-service (MaaS) subscription model for $1,000, granting purchasers a perpetual license and full access to the source code.

"It is designed to mimic real human emailing behavior and even leverages Gmail's web interface to evade traditional filtering mechanisms," Abnormal researchers Callie Baron and Piotr Wojtyla
[said](https://abnormal.ai/blog/inboxprime-ai-phishing-kit)
.

"InboxPrime AI blends artificial intelligence with operational evasion techniques and promises cybercriminals near-perfect deliverability, automated campaign generation, and a polished, professional interface that mirrors legitimate email marketing software."

The platform employs a user-friendly interface that allows customers to manage accounts, proxies, templates, and campaigns, mirroring commercial email automation tools. One of its core features is a built-in AI-powered email generator, which can produce entire phishing emails, including the subject lines, in a manner that mimics legitimate business communication.

In doing so, these services further lower the barrier to entry for cybercrime, effectively eliminating the manual work that goes into drafting such emails. In its place, attackers can configure parameters, such as language, topic, or industry, email length, and desired tone, which the toolkit uses as inputs to generate convincing lures that match the chosen theme.

What's more, the dashboard enables users to save the produced email as a reusable template, complete with support for spintax to create variations of the email messages by substituting certain template variables. This ensures that no two phishing emails look identical and helps them bypass signature-based filters that look for similar content patterns.

Some of the other supported features in InboxPrime AI are listed below -

* A real-time spam diagnostic module that can analyze a generated email for common spam-filter triggers and suggest precise corrections
* Sender identity randomization and spoofing, enabling attackers to customize display names for each Gmail session

"This industrialization of phishing has direct implications for defenders: more attackers can now launch more campaigns with more volume, without any corresponding increase in defender bandwidth or resources," Abnormal said. "This not only accelerates campaign launch time but also ensures consistent message quality, enables scalable, thematic targeting across industries, and empowers attackers to run professional-looking phishing operations without copywriting expertise."

### Spiderman Creates Pixel-Perfect Replicas of European Banks

The third phishing kit that has come under the cybersecurity radar is Spiderman, which permits attackers to target customers of dozens of European banks and online financial services providers, such as Blau, CaixaBank, Comdirect, Commerzbank, Deutsche Bank, ING, O2, Volksbank, Klarna, and PayPal.

"Spiderman is a full-stack phishing framework that replicates dozens of European banking login pages, and even some government portals," Varonis researcher Daniel Kelley
[said](https://www.varonis.com/blog/spiderman-phishing-kit)
. "Its organized interface provides cybercriminals with an all-in-one platform to launch phishing campaigns, capture credentials, and manage stolen session data in real-time."

What's notable about the modular kit is that its seller is marketing the solution in a Signal messenger group that has about 750 members, marking a departure from Telegram. Germany, Austria, Switzerland, and Belgium are the primary targets of the phishing service.

Like in the case of BlackForce, Spiderman utilizes various techniques like ISP allowlisting, geofencing, and device filtering to ascertain that only the intended targets can access the phishing pages. The toolkit is also equipped to capture cryptocurrency wallet seed phrases, intercept OTP and
[PhotoTAN](https://thehackernews.com/2024/06/moreeggs-malware-disguised-as-resumes.html)
codes, and trigger prompts to gather credit card data.

"This flexible, multi-step approach is particularly effective in European banking fraud, where login credentials alone often aren't enough to authorize transactions," Kelley explained. "After capturing credentials, Spiderman logs each session with a unique identifier so the attacker can maintain continuity through the entire phishing workflow."

### Hybrid Salty-Tycoon 2FA Attacks Spotted

BlackForce, GhostFrame, InboxPrime AI, and Spiderman are the latest additions to a long list of phishing kits like
[Tycoon 2FA](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html)
,
[Salty 2FA](https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html)
,
[Sneaky 2FA](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html)
,
[Whisper 2FA](https://thehackernews.com/2025/10/threatsday-bulletin-15b-crypto-bust.html)
,
[Cephas](https://blog.barracuda.com/2025/11/12/email-threat-radar-november-2025)
, and
[Astaroth](https://cybersecsentinel.com/astaroth-phishing-kit-exploits-2fa-weaknesses-in-gmail-and-o365/)
(not to be confused with a
[Windows banking trojan](https://thehackernews.com/2024/10/astaroth-banking-malware-resurfaces-in.html)
of the same name) that have emerged over the past year.

In a report published earlier this month, ANY.RUN said it observed a new Salty-Tycoon hybrid that's already bypassing detection rules tuned to either of them. The new attack wave coincides with a sharp drop in Salty 2FA activity in late October 2025, with early stages matching Salty2FA, while later stages load code that reproduces Tycoon 2FA's execution chain.

"This overlap marks a meaningful shift; one that weakens kit-specific rules, complicates attribution, and gives threat actors more room to slip past early detection," the company
[said](https://any.run/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
.

"Taken together, this provides clear evidence that a single phishing campaign, and, more interestingly, a single sample, contains traces of both Salty 2FA and Tycoon, with Tycoon serving as a fallback payload once the Salty infrastructure stopped working for reasons that are still unclear."