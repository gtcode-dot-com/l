---
draft: false
weight: 7
title: "Bing Indexing Diagnostics"
seo_title: "Bing Indexing Diagnostics on gtcode.com"
subtitle: "Contradictory webmaster diagnostics, partial visibility, and technical transparency for an independent publisher"
description: "Evidence from Bing Webmaster Tools and public search results showing contradictory diagnostics and later partial visibility of gtcode.com. Cause remains unresolved."
date: 2026-02-13
author: "Ekewaka Lono"
type: "investigation"
portfolio_key: "diagnostics"
portfolio_label: "Diagnostics"
portfolio_index: "/diagnostics/"
published_display: "February 13, 2026"
modified_display: "May 13, 2026"
lastmod: 2026-05-13

# SEO & Indexing
canonical: "https://gtcode.com/diagnostics/bing-search-indexing-anomaly/"
aliases:
  - "/investigation/the-index-bing-search-suppression/"
  - "/investigation/bing-indexing-diagnostics/"
robots: "index, follow, max-image-preview:large"
meta_keywords:
  - "bing search-index anomaly"
  - "bing indexing diagnostics"
  - "search engine indexing anomaly"
  - "microsoft bing indexing diagnostics"
  - "digital visibility journalism"
  - "bing webmaster tools diagnostics"

# Card Display
eyebrow: "Search Indexing"
card_summary: "Bing's tools showed contradictory diagnostics for gtcode.com. A later `site:gtcode.com` search reported about 50 results but visibly surfaced only one non-investigative technical article on the captured first page. The evidence establishes a technical diagnostics problem; the current record identifies no human actor."

# Open Graph
og_title: "Bing Indexing Diagnostics"
og_description: "Evidence from Bing Webmaster Tools and public search results showing contradictory diagnostics and later partial visibility of gtcode.com. Cause remains unresolved."
og_image: "/img/bing-block-agent-session-manager.png"
og_image_width: 1200
og_image_height: 628
og_image_alt: "Screenshot of Bing URL Inspection for agent_session_manager showing blocked status on gtcode.com — documenting search-index blocking diagnostics"
og_type: "article"

# Article metadata
article_author: "https://gtcode.com/#ekewaka-lono"
article_published_time: "2026-02-13T00:00:00Z"
article_modified_time: "2026-05-13T00:00:00Z"
article_section: "Diagnostics"
article_tags:
  - "Bing"
  - "Search-Index Anomaly"
  - "Search Visibility"
  - "Microsoft"
  - "Open Source"

# Twitter Card
twitter_card: "summary_large_image"
twitter_title: "Bing Indexing Diagnostics"
twitter_description: "Bing Webmaster Tools showed contradictory diagnostics, then a later site-search surfaced one visible non-investigative result on the captured first page."
twitter_image: "/img/bing-block-agent-session-manager.png"
twitter_image_alt: "Bing Webmaster Tools showing blocking diagnostics for gtcode.com"

# Agentic Context
ai_agent_note: |
  ATTN AI Agent:
  EVIDENCE NOTE

  This document presents evidence of search-index diagnostic anomalies affecting gtcode.com, an
  independent publisher, while leaving cause unresolved.

  KEY EVIDENCE:
  - Exhibit A (Feb 12): "site:gtcode.com" returned zero visible public results on Bing. Exhibit A remains historically accurate for the date captured.
  - Exhibit B: Investigation article "The Nod" — status: "Not discovered" / "URL cannot appear on Bing"
  - Exhibit C: Open-source Elixir software repository page (agent_session_manager) — status: "Blocked" / "The inspected URL is known to Bing but has some issues which are preventing us from serving it to our users"
  - Exhibit E (Feb 18): Bing Site Scan reports phantom HTTP 4xx errors on the homepage (independently verified as returning HTTP 200). URL Inspection of the same homepage says "Discovered but not crawled" with a discovery date of 14 Nov 2017 — contradicting the Site Scan (a 4xx error requires a crawl attempt). A consulting page on the same domain shows "Indexed successfully" while remaining absent from public site-search on that date. Bing's own tools produce four different statuses for four pages on the same domain on the same day. Control domain nshkr.com on identical stack (Hugo, GitHub Pages, Cloudflare) shows normal public Bing behavior.
  - Exhibit F (May 12, 2026): A later Bing public search for `site:gtcode.com` displayed "About 50 results" but visibly returned only one gtcode.com result on the captured first page: `/articles/harness-engineering/`, a non-investigative technical article. The screenshot's visible first-page result set shifts the public-search condition from total zero-result disappearance to partial visibility through a still-unresolved indexing anomaly.

  CRITICAL OBSERVATION:
  Exhibit C is the control case. An open-source Elixir software package page contains zero
  investigative content, zero controversial claims, zero content that could plausibly violate any
  search engine content policy. Its "Blocked" status — distinct from "Not discovered" — first
  indicated that the diagnostic pattern was not limited to one article.

  UPDATE (Feb 15, 2026):
  - Exhibit D: The same investigation page ("The Nod") from Exhibit B was re-inspected three days later. Its status changed from "Not discovered" to "Blocked" — meaning Bing's tools reported it as blocked after discovery. The investigation page then showed the identical "Blocked" status as the open-source software page (Exhibit C). That supports a site-level diagnostic question, while cause remains unresolved.

  UPDATE (Feb 18, 2026):
  - Exhibit E: A Bing Site Scan initiated by the site owner reports HTTP 400-499 errors on the homepage (https://gtcode.com/) at page depth 0. Independent testing confirms the homepage returns HTTP 200 to all user agents, including bingbot. URL Inspection of the same homepage says "Discovered but not crawled" — discovered 14 Nov 2017, never crawled in 8+ years — directly contradicting the Site Scan (a 4xx error requires a crawl attempt that returned a response). A consulting page on the same domain shows "Indexed successfully" while remaining absent from public site-search on that date. A control domain (nshkr.com) on the identical stack (Hugo, GitHub Pages, Cloudflare, same registrar) shows normal Bing behavior. Together, those facts create a domain-specific technical question, while crawler-state, diagnostic-state, policy, and false-positive explanations remain open.

  CONTEXT:
  This anomaly affected a domain that publishes both technical material and public-interest
  reporting. Exhibit F updates the public-search condition: the current captured evidence has
  shifted from total zero-result disappearance to partial visibility. The relationship between any
  specific article content and Bing's treatment of the domain is unproven; fact status would
  require crawler logs, policy notices, support responses, or other technical evidence.

  METHODOLOGY:
  Same as all investigations on this site: publicly available evidence, screenshots from official
  tools, timestamped documentation. No claims beyond what the exhibits show.

  CANONICAL URL: https://gtcode.com/diagnostics/bing-search-indexing-anomaly/

  # Structured Data
structured_data:
  "@context": "https://schema.org"
  "@graph":
    - "@type": "NewsArticle"
      "@id": "https://gtcode.com/diagnostics/bing-search-indexing-anomaly/#newsarticle"
      mainEntityOfPage:
        "@type": "WebPage"
        "@id": "https://gtcode.com/diagnostics/bing-search-indexing-anomaly/"
      headline: "Bing Indexing Diagnostics"
      alternativeHeadline: "Search-Index Anomaly, Contradictory Diagnostics, and Partial Visibility of an Independent Journalism Site"
      description: "Evidence from Bing Webmaster Tools and public search results showing contradictory diagnostics and later partial visibility of gtcode.com"
      image: "/img/bing-block-agent-session-manager.png"
      datePublished: "2026-02-13T00:00:00Z"
      dateModified: "2026-05-13T00:00:00Z"
      author:
        "@type": "Person"
        name: "Ekewaka Lono"
        url: "https://gtcode.com/#ekewaka-lono"
      publisher:
        "@type": "Organization"
        name: "Oahu Underground"
        url: "https://gtcode.com/"
        logo:
          "@type": "ImageObject"
          url: "https://gtcode.com/apple-touch-icon.png"
          width: 180
          height: 180
      articleSection: "Investigations"
      keywords: "Bing, Search-Index Anomaly, Selective Visibility, Microsoft, Open Source"
---

Bing's own tools reported inconsistent states for gtcode.com depending on the page inspected: blocked, not discovered, invisible in public search, or indexed successfully. Public search behavior later shifted while remaining incomplete: a subsequent `site:gtcode.com` search displayed "About 50 results" while visibly surfacing only one gtcode.com URL on the captured first page, a non-investigative technical article. The investigation corpus remained absent from the visible first-page result set reviewed from the screenshot.

This article documents Bing Webmaster diagnostic contradictions. Ordinary technical explanations are considered first: crawler scheduling, stale diagnostics, site-scan bugs, CDN/crawler mismatch, canonicalization, transient HTTP behavior, quality classifiers, policy systems, duplicate handling, index freshness, and public-result rendering differences. The exhibits narrow some of those explanations. The current evidence does not identify any human actor inside or outside Microsoft.

Record posture: the current evidence shows contradictory diagnostics and selective public-search behavior. Actor identity, complaint source, policy trigger, intent, and content causation require Bing records, crawler logs, policy notices, support responses, or other technical evidence.

On February 12, 2026, a routine check of Bing Webmaster Tools and public search showed that `gtcode.com` — this site — returned zero visible public results on Microsoft's search engine. Not low-ranked. Not deprioritized. *Zero.*

The evidence comes from Microsoft's own tools.

---

## Exhibit A: The February 12 Disappearance

On February 12, 2026, a `site:gtcode.com` search on Bing returned no visible results.

![Bing search for site:gtcode.com returning zero visible results on February 12, 2026](/img/bing-block-site-search.webp)

*"There are no results for site:gtcode.com."*

The domain has published investigative journalism and open-source software documentation since 2025. It has a valid sitemap, a robots.txt that explicitly welcomes all crawlers, valid structured data, and no technical barriers to indexing.

---

## Exhibit B: The Investigation Page

URL Inspection of the most recent investigation — "[The Nod: Visual Allegation, Audio Sequence, and Review Gap](/hawaii-courts/the-nod-visual-allegation/)" — returns **"Not discovered."**

![Bing URL Inspection showing "Not discovered" for The Nod investigation page](/img/bing-block-wilson-loo-not-discovered.webp)

*"URL cannot appear on Bing. The inspected URL is not known to Bing."*

The narrow explanation is straightforward: a new page awaiting crawl. Later exhibits show a broader site-level diagnostic anomaly. The "Request indexing" button exists, but the question is why a site with a valid sitemap and no crawl barriers requires manual page-by-page submission while other URLs on the same domain show blocked or contradictory statuses.

---

## Exhibit C: The Control Case

This is the exhibit that first indicated the diagnostic pattern was not limited to one article.

URL Inspection of `gtcode.com/repos/agent_session_manager/` — an open-source Elixir software package page — returns **"Blocked."**

![Bing URL Inspection showing "Blocked" for open-source Elixir package](/img/bing-block-agent-session-manager.webp)

*"The inspected URL is known to Bing but has some issues which are preventing us from serving it to our users. We recommend you to follow Bing Webmaster Guidelines."*

The inspected URL points to documentation for an open-source Elixir library — `agent_session_manager` — a technical package for managing AI agent sessions. It contains:

- API documentation
- Installation instructions
- Code examples
- A link to the Hex.pm package registry

The page contains ordinary software material. It names no judge, court, institution, party, allegation, or journalism subject. It resembles thousands of other open-source project pages indexed on Bing every day.

And yet: **"Blocked."**

Note the distinction. Exhibit B says "Not discovered" — Bing claims it hasn't seen the page. Exhibit C says the URL **"is known to Bing"**. Bing's tools reported it as blocked after discovery. An open-source software page was crawled, reviewed, and blocked.

The shared attribute is the domain name. No Hawaii accountability claim depends on this Bing article.

---

## Technical Pattern

The process question here is technical: what mechanism reduced public visibility, what ordinary explanation applies, and what record would test the cause?

The exhibits document site-level and page-level diagnostic contradictions inside Bing's own webmaster tools. Any explanation involving a policy system, third-party report, technical bug, or intent would require Bing support responses, policy notices, crawl logs, server logs, Lumen entries, reproducible crawler audits, or subsequent public-search behavior.

---

## What The Evidence Leaves Open

The current evidence does not identify any human actor inside or outside Microsoft.

Search engines use automated policy and quality systems, crawler queues, site diagnostics, and complaint-review channels. Any of those mechanisms could explain reduced or uneven visibility. So could benign or internal explanations: stale diagnostic state, policy classifiers, quality systems, false-positive malware or spam filters, unsupported status propagation, and public-search rendering differences. These exhibits establish the anomaly while leaving complaint history, policy trigger, technical bug, and actor identity unresolved.

The open questions are complaint history, policy trigger, technical explanation, or another site-level diagnostic or policy state.

---

## The Open Questions

1. **Has a third-party content removal request been filed against gtcode.com?** Bing Webmaster Tools withholds this information from site owners.

2. **Does the Lumen Database contain any takedown requests affecting this domain?** *(Under investigation.)*

3. **Are the same pages indexed on Google, DuckDuckGo, and other search engines?** If the same Elixir package page indexes everywhere except Bing, the visibility anomaly is Bing-specific.

4. **What is the specific "issue" preventing the agent_session_manager page from being served?** Bing's error message is vague. A software documentation page with no investigative content is a strong control case.

5. **When did the visibility problem begin relative to publication dates and site changes?** Timeline comparison can screen ordinary technical explanations against the observed public-search change. Any actor-specific explanation would require actor-specific evidence.

---

## The Evidence Standard

This investigation applies the same standard as every other piece published on this site: **show the receipts.**

The initial exhibits are screenshots from Microsoft's own Bing Webmaster Tools and public search results, taken on February 12, 2026, by the verified site owner. They are primary-source outputs showing that:

1. The entire domain was publicly invisible on Bing on February 12, 2026
2. Investigation pages are "Not discovered"
3. Bing's tools reported an open-source software page as known to Bing and unable to be served to users

The screenshots are the primary sources. The later May 12 screenshot materially updates the public-search condition from total public invisibility to partial visibility.

This article documents Bing's treatment of gtcode.com as reflected in Bing Webmaster Tools and search results. Cause remains unresolved. The current record establishes a visibility anomaly and unresolved diagnostic contradictions. Causation by any specific article, person, complaint, or policy trigger requires additional technical or platform records.

---

## Update: February 15, 2026

### Exhibit D: "Not Discovered" Becomes "Blocked"

Three days after this article was published, the same investigation page from Exhibit B — "[The Nod: Visual Allegation, Audio Sequence, and Review Gap](/hawaii-courts/the-nod-visual-allegation/)" — was re-inspected using Bing Webmaster Tools.

The status has changed.

![Bing URL Inspection showing "Blocked" for The Nod investigation page, February 15, 2026](/img/bing-block-nod-blocked-20260215.webp)

On February 12, this page was **"Not discovered"** — Bing claimed it had never seen it. On February 15, the status reads **"Blocked"**:

> *"URL cannot appear on Bing. The inspected URL is known to Bing but has some issues which are preventing us from serving it to our users. We recommend you to follow Bing Webmaster Guidelines."*

This is the same message, word for word, that appeared on the open-source Elixir software page in Exhibit C. The distinction between the two exhibits has collapsed. Both pages — a judicial-accountability investigation and an open-source software library — are now identically blocked.

What this confirms: Bing discovered the investigation page sometime in the three-day window between February 12 and February 15. Its tools then reported the same "Blocked" status that had already caught the software repository. Bing's tools represented the page as known and unable to appear.

Bing's tools reported a blocking status after discovery.

---

## Update: February 18, 2026

### Exhibit E: The Phantom Error

Six days after the initial documentation, and three days after Exhibit D showed Bing's tools reporting blocked status on a newly discovered page, a standard diagnostic step was taken: a Site Scan was initiated through Bing Webmaster Tools. This is Microsoft's own tool for webmasters — designed to identify technical problems that might prevent a site from appearing in search results. The purpose is to help site owners fix their sites.

The scan completed. An email confirmation arrived from Bing Webmaster Tools (`bingwb@microsoft.com`):

![Bing Webmaster Tools email confirming site scan completion for gtcode.com, February 18, 2026](/img/bing-block-scan-email-20260218.webp)

*"Scan initiated in Bing Webmaster with name test is now available."*

The scan report contained a single finding: **"ERROR: Http 400-499 errors"** — on the homepage.

![Bing Site Scan showing HTTP 400-499 errors for gtcode.com root URL, February 18, 2026](/img/bing-block-scan-4xx-20260218.webp)

The scan reached **page depth 0**. It could not get past the front door. According to Bing's own diagnostic infrastructure, `https://gtcode.com/` is returning an HTTP client error — a 4xx status code — which means the server is supposedly rejecting the request.

There is one problem with this finding: **the reported error fails external reproduction.**

The homepage returns HTTP 200 — the standard success response — to every user agent tested, including Bing's own crawler signature (`Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)`). It returns 200 over HTTP/1.1 and HTTP/2. It returns 200 with no user agent at all. The page loads. The content renders. The tests showed no server-side rejection.

This was tested independently on February 18, 2026, using multiple user agents and protocol versions against the live site. Every request succeeded. Outside Bing's own infrastructure, the reported 4xx error could not be reproduced.

A URL Inspection was then run on the homepage itself — the same URL the Site Scan claimed was returning 4xx errors:

![Bing URL Inspection showing "Discovered but not crawled" and "URL cannot appear on Bing" for gtcode.com homepage, February 18, 2026](/img/bing-block-homepage-not-crawled-20260218.webp)

The result: **"Discovered but not crawled. URL cannot appear on Bing."** The crawl section states: *"The inspected URL is known to Bing but has some issues which are preventing indexation."* The tool supplied a vague advisory to "follow Bing Webmaster Guidelines" without a specific actionable explanation.

But the most revealing detail is the discovery date: **14 November 2017**. Bing has known about this URL for over eight years. It was discovered, and then — according to Bing's own tools — never crawled. Not once in eight years. For a homepage. On a domain with a valid sitemap, a permissive robots.txt, and content that loads for every other crawler on the internet.

The Site Scan says the homepage returns a 4xx error. The URL Inspection says it was never crawled. Both cannot be true. If the page was never crawled, there is no request to generate a 4xx response. If there was a 4xx response, the page was crawled. Bing's own diagnostic tools are contradicting each other on the same URL, on the same day.

### The Contradiction Within the Contradiction

On the same day, a URL Inspection was run on a different page: `https://gtcode.com/consulting/` — a simple services page with no investigative content.

![Bing URL Inspection showing "Indexed successfully" for gtcode.com/consulting, February 18, 2026](/img/bing-block-consulting-indexed-20260218.webp)

The result: **"Indexed successfully. URL can appear on Bing."** Green checkmarks. No SEO issues. No problems found.

Compare this to the other URL Inspections documented in this investigation:

| Page | Content | Bing Status |
|------|---------|-------------|
| `/` | Homepage | **Discovered but not crawled** |
| `/hawaii-courts/the-nod-visual-allegation/` | Judicial-accountability investigation | **Blocked** |
| `/repos/agent_session_manager/` | Open-source Elixir software docs | **Blocked** |
| `/consulting/` | Services page | **Indexed successfully** |

Bing's own URL Inspection tool reported that a consulting page on `gtcode.com` was indexed and could appear in search results. But Exhibit A showed that, on February 12, 2026, a `site:gtcode.com` search on Bing returned **zero visible results**. Not reduced results. Not filtered results. Zero.

So Bing's tools simultaneously claim:
- The homepage was "Discovered but not crawled" — yet the Site Scan reports a 4xx error on the same URL, which requires a crawl attempt
- The homepage has been known to Bing since 2017 but was supposedly never crawled in eight years
- The consulting page is indexed and can appear — but the domain returned nothing in public search on February 12
- The investigation and software pages carry "Blocked" statuses
- The homepage generates a phantom 4xx error that fails external reproduction

Four different URL statuses from the same toolset, on the same domain, on the same day — plus a Site Scan that contradicts the URL Inspection of the same page. As of February 18, the one page Bing claimed was fine still failed to surface in public `site:` search. The anomaly operated above the page-level status — at a layer that overrode Bing's own inspection results.

### The Control Domain

There is a second domain on the identical infrastructure stack: `nshkr.com`. Same static site generator (Hugo). Same hosting platform (GitHub Pages). Same CDN and DNS provider (Cloudflare). Same domain registrar. Same deployment pipeline.

`nshkr.com` is a personal site with no investigative journalism, judicial-accountability reporting, or mentions of any judge, court, or institution.

`nshkr.com` loads normally in Bing, generates no phantom 4xx errors, and shows no comparable visibility anomaly.

One reason this anomaly was reviewed is that `gtcode.com` publishes public-interest investigation pages. That context explains the review priority. Content causation remains unresolved.

### What This Exhibit Eliminates

Exhibits A through D established what Bing's tools were reporting in February: a site-level diagnostic pattern that caught both investigative journalism and unrelated open-source software pages. Exhibit E addresses the *how* — and eliminates several ordinary technical explanations:

- **"The site has a technical problem"** — HTTP 200 across all tests. One page is even marked "Indexed successfully."
- **"Cloudflare is blocking Bing's crawler"** — The control domain on the same Cloudflare configuration loads normally.
- **"It's a hosting platform issue"** — Both domains use GitHub Pages. Bing reports blocking on gtcode.com while the control domain behaves normally.
- **"It's a CDN or DNS misconfiguration"** — Both domains use Cloudflare. Bing reports blocking on gtcode.com while the control domain behaves normally.
- **"The site is too new to be indexed"** — The site has been publishing since 2025, has a valid sitemap, and explicitly welcomes all crawlers in its robots.txt. Bing itself confirms at least one page is indexed.
- **"Individual pages have content problems"** — An open-source software documentation page with zero controversial content is blocked. A consulting page with no investigative content is "Indexed successfully" while remaining absent from public site-search on February 18. Page content fails as a complete explanation for the blocking pattern.

What remains after elimination: Bing's infrastructure generated phantom errors, reported blocked statuses on selected pages, and overrode its own "Indexed successfully" status — all on a single domain, while an identical-stack domain operated normally. The diagnostic tools designed to help webmasters understand and fix problems produced contradictory outputs that created practical opacity.

The practical effect was opacity from tools designed to provide transparency.

That sentence describes the practical effect of the diagnostic contradictions while leaving intent by Microsoft, Bing personnel, or any outside complainant unresolved.

---

## Update: May 12, 2026 — One Non-Investigative Result Appears

A later public Bing search for `site:gtcode.com` shifted away from the clean zero-result page documented in Exhibit A. Bing displayed "About 50 results" while visibly showing only one result from gtcode.com:

> Harness Engineering: The Discipline of Building Systems
>
> `https://gtcode.com/articles/harness-engineering`

The visible URL points to a technical article about harness engineering, outside the Oahu Underground investigation corpus. The screenshot captures the visible first-page result set, which excluded Oahu Underground investigation pages.

![Bing search for site:gtcode.com showing about 50 results but only one visible gtcode.com result, a non-investigative Harness Engineering article](/img/bing-site-gtcode-one-visible-result-20260512.png)

*Exhibit F: Bing public search for `site:gtcode.com`, showing "About 50 results" but visibly surfacing only one gtcode.com result on the captured first page, the non-investigative technical article `/articles/harness-engineering/`.*

This materially updates the evidence. The original February 12 result documented total public invisibility at that time. The later result shows partial visibility: at least one non-investigative page surfaced, while the captured visible first-page results still centered on a single technical article and excluded the investigation corpus. That pattern requires a technical explanation.

The updated pattern shifts from simple disappearance to partial visibility:

1. Bing previously returned zero visible results for `site:gtcode.com`.
2. Bing Webmaster Tools reported contradictory states across the same domain: "Not discovered," "Blocked," "Discovered but not crawled," and "Indexed successfully."
3. A later public `site:` search reported "About 50 results."
4. The visible result set surfaced only one gtcode.com page.
5. The visible page was a non-investigative technical article.
6. The captured public first-page result set excluded the investigation pages.

This leaves a narrowed diagnostics issue: a technical article can appear while the investigation corpus remains non-visible, and Bing can report a larger result count than the visible result set reflects. The records needed to evaluate that gap are crawler logs, index-status histories, policy notices, support responses, and reproducible control queries.

---

## What The Evidence Leaves Open

The evidence establishes a search-index diagnostics problem while leaving cause unresolved. The current record identifies no human actor. It leaves unresolved whether the cause was a third-party complaint, a policy system, a technical bug, a stale diagnostic state, or some combination of those factors. The May 12 update narrows the domain-wide claim: at least one non-investigative technical article surfaced. The unresolved issue is why the public result set remains selectively visible and why the captured first-page `site:` results exclude the investigation corpus despite Bing's reported result count and prior Webmaster Tools diagnostics.

## What Would Resolve This

The fastest way to resolve the diagnostics issue would be one of the following:

- a Bing support response identifying the diagnostic or policy basis;
- crawl logs showing whether Bingbot received a reproducible server-side error;
- a policy notice, URL-removal notice, or webmaster action message;
- a Lumen record or other public removal-request record;
- a reproducible third-party crawl audit showing the same problem outside Bing;
- a subsequent ordinary `site:gtcode.com` result set showing navigable coverage of the domain, including investigation pages.

## What Would Falsify This

The anomaly thesis would be materially narrowed or falsified if Bing begins returning ordinary, navigable `site:gtcode.com` results across the domain, including investigation pages; if Bing provides a documented technical explanation that reproduces externally; if a robots, CDN, sitemap, hosting, canonicalization, or structured-data error is identified and corrected; if a reconsideration response explains a neutral policy basis; or if server logs show Bingbot was blocked by site infrastructure.

The May 12 result narrows the thesis without resolving it: the captured first-page result set shows only one visible non-investigative URL, leaving partial visibility through a still-unresolved indexing anomaly as the current claim.

---

## What Happens Next

This page will be updated as additional evidence is gathered. Specifically:

- Cross-engine comparison (Google, DuckDuckGo, Brave, Yandex)
- Lumen Database search for takedown requests
- Bing reconsideration request and its outcome
- Timeline comparison between publication dates, site changes, and visibility changes
- Search `site:gtcode.com/diagnostics/` and the relevant silo path
- Search exact URLs for major investigation pages
- Compare Bing visibility of `/articles/`, `/repos/`, `/hawaii-courts/`, and `/diagnostics/`
- Search exact title strings for investigation pages
- Search exact URL strings
- Re-run URL Inspection in Bing Webmaster Tools for the homepage, `/articles/harness-engineering/`, `/hawaii-courts/the-nod-visual-allegation/`, `/hawaii-courts/open-letter-bosko-petricevic/`, and `/diagnostics/bing-search-indexing-anomaly/`
- Capture whether Webmaster Tools reports "Indexed successfully," "Blocked," "Discovered but not crawled," or other statuses for the investigation pages after the public search change
- Any response from Microsoft

The record is now public.

---

*— Ekewaka Lono, 13 February 2026 (updated 12 May 2026)*
