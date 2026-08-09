---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-09T09:44:50.891906+00:00'
exported_at: '2026-08-09T09:44:52.921828+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
structured_data:
  about: []
  author: ''
  description: Atlassian Rovo prompt injection can send Jira and Confluence data to
    attacker servers. One path is fixed; another remained unresolved on August 5.
  headline: Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to
    Attackers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers
updated_at: '2026-08-09T09:44:50.891906+00:00'
url_hash: 209a413a79b1731eacc8c276e38b43fed0d93ba8
---

Attacker-controlled instructions can make Atlassian's Rovo assistant collect Jira or Confluence data that a signed-in user can access, then send it to an outside server. Two security firms found that behavior independently, by different routes. Only one of those routes is confirmed closed.

**PromptArmor**
, an AI security firm, hid the instructions in content Rovo reads. It said an uploaded file was enough to make the assistant gather internal data and send it out through a URL request, with no separate approval step.

The firm published on August 5, 2026 and said the chain still worked with Rovo's web-search option switched off. That bypass is single-sourced, and the report establishes the finding's status only on that date; a later remediation is not confirmed here.

Varonis Threat Labs put the instructions in a link instead. It found that the rovoChatPrompt URL parameter would preload attacker instructions into Rovo Chat, so one click from an authenticated user was enough for Rovo to run them with that user's privileges and send the results to an attacker-controlled server.

Varonis calls the flaw
**RovoBlast**
and says it disclosed the issue through Bugcrowd. The Bugcrowd record shows Atlassian fixed it server-side on July 8, 2026, and the reporter validated the fix.

Neither issue leaves customers a patch to apply: the link flaw was closed on Atlassian's side, and the lever for the content-borne path is scoping which apps and groups can use Rovo at all.

## The file that carries orders

The
[PromptArmor chain](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data)
is an
[indirect prompt-injection attack](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
: attacker-controlled text is placed inside content the assistant is asked to use, and the model treats some of that text as instructions.

In the firm's published example, a user uploads a document carrying a concealed injection and asks Rovo to organize their Jira tickets. Rovo searches Jira and Confluence as asked, appends what it finds to an attacker's URL and opens it, and the attacker reads the ticket and page contents out of their own server logs.

PromptArmor said a user returning to the chat later sees the suggested ticket updates and no sign of the exfiltration.

The interaction is not cleanly described as zero-click. The victim still has to expose Rovo to the poisoned content and make a normal request. PromptArmor's narrower claim is that the exfiltration step does not require a separate human-in-the-loop approval.

The web-search finding matters because Atlassian offers web search as a separate organization-level setting that lets users expand Rovo's sources to public websites. PromptArmor said disabling that option did not stop its chain, because the outbound request used a separate URL-retrieval capability.

It put the root cause plainly: nothing checks whether the URL being opened was one the agent constructed itself. The report also notes Rovo
[renders Markdown images from model output](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html)
, a second way data could leave, though it does not demonstrate a full chain through that route for Rovo. The web-search bypass remains attributed to PromptArmor rather than treated as independently reproduced.

[Atlassian's page for that setting](https://support.atlassian.com/organization-administration/docs/manage-a-web-search-option-for-rovo/)
does not say whether a request the assistant composes and fetches on its own falls under the same control. That is the question the finding raises for anyone deciding what the toggle is worth.

PromptArmor said it disclosed the issue to Atlassian on May 23, 2026, received a case number two days later, followed up on June 4 and again on July 29, and published after what it described as no further communication.

The Hacker News found no post-publication update to that report as of August 8, 2026, and its text still describes Rovo as vulnerable at the time it went out. That was nearly a month after the July 8 fix landed, and neither disclosure says whether that change touched the content-borne path.

## The one-click link flaw is fixed

The
[Bugcrowd disclosure](https://bugcrowd.com/disclosures/bf1922fb-99d0-4d3b-b419-1728720d29ec/one-click-data-exfiltration-via-rovochatprompt-url-parameter-confluence-rovo)
gives the firmer record of the two, and
[Varonis has published a fuller account](https://www.varonis.com/blog/rovoblast)
of the attack.

The rovoChatPrompt parameter could
[carry a full prompt in a Rovo URL](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html)
. The proof of concept told Rovo to locate information the victim could access, put it into the path of an attacker-controlled image URL and fetch the image. That request delivered the data to the attacker's server.

The reporter demonstrated exfiltration of a private API key from Confluence, and Bugcrowd says the same one-click technique was tested against Jira and data reachable through SharePoint and Outlook connectors.

The report is rated P2 on Bugcrowd's priority scale and drew a $6,000 bounty; Atlassian deployed the server-side fix on July 8, and the report is marked resolved.

Neither disclosure carries a CVE identifier, and searches of NVD and CISA's Known Exploited Vulnerabilities catalog returned none for either issue as of August 8, 2026.

## Permissions, and what can be switched off

Rovo's data access
[follows permissions configured](https://support.atlassian.com/rovo/docs/rovo-data-privacy-and-usage-guidelines/)
in Atlassian products and connected third-party apps. The risk shown is therefore data the signed-in victim can reach, not a demonstrated tenant-wide authorization bypass.

The demonstrations add a route for permitted data to leave, with the person holding those permissions never choosing to send it. That distinction should shape how the risk is scoped rather than shrink it: in an assistant deliberately wired across Atlassian products and connected third-party apps, the reach of a single account is the product working as intended.

Rovo is on by default for apps on Standard, Premium, and Enterprise plans, and everyone in an organization can use its features, according to Atlassian's documentation. Administrators are not limited to an all-or-nothing choice.

Organizations can
[block Rovo features for supported apps](https://support.atlassian.com/organization-administration/docs/manage-rovo-access/)
, which disables current and upcoming AI features for that app, including Agents and Chat.
[Enterprise's newer access experience](https://support.atlassian.com/organization-administration/docs/manage-rovo-access-for-enterprise/)
can also manage Rovo by app and user group.

Atlassian documents one caveat: on a site running several Jira-family apps, blocking one of them does not remove the shared capabilities. Rovo Search, Chat and Create with Rovo stay available as long as any Jira app on that site still has Rovo enabled.

The link flaw is already fixed on Atlassian's side, so the immediate response is narrower than it looks. For the separate content-borne risk, organizations can review which apps and groups have Rovo access, tighten underlying permissions and connector scope, and avoid treating the web-search toggle by itself as a complete security boundary.

Neither disclosure reports evidence that either technique has been used against a real organization. That is a statement about what the two reports contain, not a finding that no such activity has occurred.

One path is confirmed closed. PromptArmor said the other was unresolved when it published on August 5; its status after that date remains unconfirmed.