{{- $brandName := strings.TrimSpace (.Params.brand_name | default "Oahu Underground") -}}
{{- $tipsEmail := .Site.Params.tips_email | default "tips@gtcode.com" -}}
{{- $contactEmail := .Site.Params.contact_email | default "inquire@gtcode.com" -}}
{{- $investigationPagesAll := sort (where (where (where .Site.RegularPages "Section" "investigation") "Params.homepage_exclude" "ne" true) "Params.series" "ne" "The Architecture of Access") "Date" "desc" -}}
{{- $investigationPagesAll = where $investigationPagesAll "Title" "ne" "The Architecture of Access" -}}
{{- $investigationPagesEn := where $investigationPagesAll "Params.language" "en" -}}
{{- $investigationPages := cond (gt (len $investigationPagesEn) 0) $investigationPagesEn $investigationPagesAll -}}
{{- $investigationsByUpdated := sort $investigationPages "Lastmod" "desc" -}}
{{- $latestUpdates := first 6 $investigationsByUpdated -}}
{{- $lead := .Site.GetPage "/investigation/the-nod-wilson-loo-silent-felony" -}}
{{- if and (not $lead) (gt (len $investigationPages) 0) -}}
  {{- $lead = index $investigationPages 0 -}}
{{- end -}}
{{- $carto := .Site.GetPage "/investigation/cartography-for-guppies" -}}
{{- $zoneOfPoliteness := .Site.GetPage "/investigation/zone-of-politeness-hawaii-media-blackout" -}}
{{- $twoQuestions := .Site.GetPage "/investigation/the-two-questions" -}}
{{- $consultingPage := .Site.GetPage "section" "consulting" -}}
{{- $consultingURL := "/consulting/" -}}
{{- if $consultingPage }}{{ $consultingURL = $consultingPage.RelPermalink }}{{ end -}}
{{- $newsSection := .Site.GetPage "section" "news" -}}
{{- $newsPagesAll := sort (where .Site.RegularPages "Section" "news") "Date" "desc" -}}
{{- $newsPagesEn := where $newsPagesAll "Params.language" "en" -}}
{{- $newsPages := cond (gt (len $newsPagesEn) 0) $newsPagesEn $newsPagesAll -}}
{{- $latestNews := first 10 $newsPages -}}
{{- $newsRSS := "/news/index.xml" -}}
{{- if $newsSection -}}
  {{- with $newsSection.OutputFormats.Get "RSS" -}}
    {{- $newsRSS = .RelPermalink -}}
  {{- end -}}
{{- end -}}
{{- $data := .Site.Data.neutralization_stack -}}
# {{ .Title }}

{{ .Params.hero_kicker | default "Prosecution Roadmap" }}

## {{ .Params.hero_headline | default "The Two Questions" }}

{{ .Params.hero_subtitle | default "One Witness. Two Questions. ~1.8 Years on the Clock." }}

[{{ .Params.hero_primary_cta_label | default "Read the Roadmap" }}]({{ .Params.hero_primary_cta_url | default "/investigation/the-two-questions/" }})
[{{ .Params.hero_secondary_cta_label | default "Browse All Files" }}]({{ .Params.hero_secondary_cta_url | default "/investigation/" }})

---

## Investigation Architecture

### The Seven-Layer Neutralization Stack

*How one network produces silence without coordination*

Each layer is independently sufficient to suppress a claim. Together, they form a defense-in-depth architecture: if one layer fails, the next catches the signal and attenuates it. No single point of failure. No coordination required. Each actor follows institutional incentives. The aggregate output is silence.

{{ range $data.layers }}{{ if eq .status "live" }}> **LAYER {{ .num }} ACTIVATED** — {{ .live_detail }}

{{ end }}{{ end -}}
| Layer | Code | Name | Status |
|-------|------|------|--------|
{{ range $data.layers -}}
| {{ .num }} | {{ .code }} | [{{ .name }}]({{ .url }}) | {{ if eq .status "live" }}LIVE{{ else if eq .status "forthcoming" }}FORTHCOMING{{ else }}PUBLISHED{{ end }} |
{{ end }}
{{ range $data.layers }}
**Layer {{ .num }}: {{ .code }}** — {{ .name }}
- **Mechanism:** {{ .mechanism }}
- *{{ .one_liner }}*
- Status: {{ if eq .status "live" }}LIVE{{ else if eq .status "forthcoming" }}FORTHCOMING{{ else }}PUBLISHED{{ end }} · {{ .published }}{{ if and (ne .status "forthcoming") (ne .status "live") }} · [Read the investigation →]({{ .url }}){{ else if eq .status "live" }} · Investigation in progress{{ else }} · [Have information? →](mailto:tips@gtcode.com){{ end }}
{{ end }}
**Aggregate output: Silence**

### Related Series & Methodology
{{ range $data.series_hubs }}
- [{{ .name }}]({{ .url }}) — {{ .desc }}
{{- end }}

### For the CI Reform Audience

The SECURE Act, signed into law in December 2025, broadened U.S. counterintelligence from a protective function to one that includes deterrence, disruption, and exploitation, and directed information-sharing with state, local, and tribal partners to counter foreign influence operations. This site shows what that mandate looks like in practice at the state level: one network, seventeen investigations, primary-source records. Coordination is only possible once the operating environment has been mapped.

gtcode.com/investigation/ · CC-BY-4.0 · GitHub-archived · Wayback Machine indexed

---

## GTCode Consulting

### AI engineering support for real deployments

Consulting work focuses on shipping reliable systems: architecture choices, evaluation gates, observability, and operational hardening.

**Architecture and Risk Review**
Rapid assessment of model, data, and integration risks before you commit to implementation paths.

**Build and Hardening**
Hands-on delivery for agent workflows, retrieval systems, and production inference pipelines.

**Fractional Technical Leadership**
Advisory support for roadmap decisions, engineering execution, and AI governance boundaries.

[Open the consulting brief →]({{ $consultingURL }})
[Email Inquire@GTCode.com →](mailto:{{ $contactEmail }})

---

## Featured Investigations
{{ if $lead }}
{{ $leadUpdated := $lead.Lastmod -}}
{{ if $leadUpdated.IsZero }}{{ $leadUpdated = $lead.Date }}{{ end -}}
{{ $leadSummary := $lead.Params.card_summary | default $lead.Description -}}
{{ if eq (strings.TrimSpace $leadSummary) "" }}{{ $leadSummary = $lead.Summary | plainify | truncate 260 }}{{ end -}}
### Lead Investigation

**[{{ $lead.Title }}]({{ $lead.RelPermalink }})**
{{ with $lead.Params.subtitle }}*{{ . }}*
{{ end }}
{{ $leadSummary }}

Published {{ $lead.Date.Format "January 2, 2006" }} · Updated {{ $leadUpdated.Format "January 2, 2006" }}

[Read the investigation →]({{ $lead.RelPermalink }})
{{ end -}}

{{ if $zoneOfPoliteness -}}
{{ $zopSummary := $zoneOfPoliteness.Params.card_summary | default $zoneOfPoliteness.Description -}}
{{ if eq (strings.TrimSpace $zopSummary) "" }}{{ $zopSummary = $zoneOfPoliteness.Summary | plainify | truncate 220 }}{{ end -}}
### {{ $zoneOfPoliteness.Params.eyebrow | default "Media Capture" }}

**[{{ $zoneOfPoliteness.Title }}]({{ $zoneOfPoliteness.RelPermalink }})**
{{ with $zoneOfPoliteness.Params.subtitle }}*{{ . }}*
{{ end }}
{{ $zopSummary }}

[Read the investigation →]({{ $zoneOfPoliteness.RelPermalink }})
{{ end -}}

{{ if $carto -}}
{{ $cartoSummary := $carto.Params.card_summary | default $carto.Description -}}
{{ if eq (strings.TrimSpace $cartoSummary) "" }}{{ $cartoSummary = $carto.Summary | plainify | truncate 220 }}{{ end -}}
### Publisher's Note

**[{{ $carto.Title }}]({{ $carto.RelPermalink }})**
{{ with $carto.Params.subtitle }}*{{ . }}*
{{ end }}
{{ $cartoSummary }}

[Read the full note →]({{ $carto.RelPermalink }})
{{ end -}}

---

## Investigations
{{- $featuredPaths := slice -}}
{{- if $lead }}{{ $featuredPaths = $featuredPaths | append $lead.RelPermalink }}{{ end -}}
{{- if $zoneOfPoliteness }}{{ $featuredPaths = $featuredPaths | append $zoneOfPoliteness.RelPermalink }}{{ end -}}
{{- if $twoQuestions }}{{ $featuredPaths = $featuredPaths | append $twoQuestions.RelPermalink }}{{ end -}}
{{- if $carto }}{{ $featuredPaths = $featuredPaths | append $carto.RelPermalink }}{{ end -}}

{{- $closedLoopSeries := .Site.GetPage "/investigation/the-closed-loop" -}}
{{- $closedLoopMembers := slice -}}
{{- if $closedLoopSeries -}}
  {{- $featuredPaths = $featuredPaths | append $closedLoopSeries.RelPermalink -}}
  {{- range where $.Site.RegularPages "Params.series" "The Closed Loop" -}}
    {{- $closedLoopMembers = $closedLoopMembers | append . -}}
    {{- $featuredPaths = $featuredPaths | append .RelPermalink -}}
  {{- end -}}
  {{- $closedLoopMembers = sort $closedLoopMembers "Params.series_part" "asc" -}}
{{- end -}}

{{ if $closedLoopSeries }}
### Series: {{ $closedLoopSeries.Title }}

{{ with $closedLoopSeries.Params.card_summary }}{{ . }}{{ end }}

{{ range $closedLoopMembers -}}
- **{{ .Params.series_part }}:** [{{ .Title }}]({{ .RelPermalink }})
{{ end }}
[Read series →]({{ $closedLoopSeries.RelPermalink }})
{{ end }}

{{- $archivePages := where $investigationPages ".RelPermalink" "not in" $featuredPaths -}}
### Investigation Archive
{{ range first 8 $archivePages }}
{{ $updated := .Lastmod -}}
{{ if $updated.IsZero }}{{ $updated = .Date }}{{ end -}}
{{ $summary := .Params.card_summary | default .Description -}}
{{ if eq (strings.TrimSpace $summary) "" }}{{ $summary = .Summary | plainify | truncate 210 }}{{ end -}}
**[{{ .Title }}]({{ .RelPermalink }})** — {{ .Params.eyebrow | default "Investigative File" }}
{{ $summary }}
Published {{ .Date.Format "Jan 2, 2006" }} · Updated {{ $updated.Format "Jan 2, 2006" }}
[Read the file →]({{ .RelPermalink }})
{{ end }}
[View the full investigation archive →](/investigation/)

---

{{ if gt (len $latestUpdates) 0 -}}
## Latest Updates

New filings and recently updated files
{{ range $latestUpdates }}
{{ $updated := .Lastmod -}}
{{ if $updated.IsZero }}{{ $updated = .Date }}{{ end -}}
- {{ $updated.Format "Jan 2, 2006" }} · {{ .Params.eyebrow | default "Update" }} · [{{ .Title | htmlUnescape }}]({{ .RelPermalink }})
{{- end }}

[View all investigative updates →](/investigation/)

---

{{ end -}}

## Subscribe

Track new investigations and the broader AI/news wire through RSS.

- [Subscribe: Site RSS →](/index.xml)
- [Subscribe: News RSS →]({{ $newsRSS }})

---

## About the Reporter

### Ekewaka Lono

Ekewaka Lono is an independent investigative reporter based in Hawaii, focused on judicial accountability, institutional capture, and public-interest documentation within Hawaii's court system.

Methodology is evidence-first: public records, primary-source documents, and clearly labeled firsthand testimony. Each claim is linked to source material where possible.

**Reporting Method**

- Map verifiable public records before narrative claims
- Label firsthand testimony explicitly
- Publish dates, revisions, and source context
- Keep tip channels confidential and secure
{{ if $carto }}
[Read full methodology →]({{ $carto.RelPermalink }})
{{ end }}
---

## Get in Touch

### Have information?

If you have documents, first-hand knowledge, or information relevant to institutional misconduct in Hawaii, we want to hear from you. All inquiries are treated as confidential.

**Contact:** [tips@GTCode.com](mailto:{{ $tipsEmail }})

*Send only a brief, non-sensitive introduction. Encrypted channels are arranged for follow-up.*

---

{{ if gt (len $latestNews) 0 -}}
## News Wire

### Latest News Feed
{{ range $latestNews }}
- {{ .Date.Format "Jan 2, 2006" }} · {{ .Params.category | default "News" }} · [{{ .Title | htmlUnescape }}]({{ .RelPermalink }})
{{- end }}

[View full news feed →](/news/)

---

{{ end -}}

## Latest Articles
{{ $articles := first 5 (sort (where .Site.RegularPages "Section" "articles") "Date" "desc") -}}
{{ range $articles }}
- [{{ .Title }}]({{ .RelPermalink }}){{- with .Date }} — {{ .Format "2006-01-02" }}{{- end }}{{- with .Params.meta_description }}
  {{ . }}{{- end }}
{{- end }}

## Site Sections
{{ range sort .Site.Sections "Title" }}
- [{{ .Title }}]({{ .RelPermalink }}) — {{ len .Pages }} pages{{- with .Params.description }} · {{ . }}{{- end }}
{{- end }}
