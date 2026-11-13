{{- if site.Params.alternative_homepage -}}
{{ with site.GetPage "/homepage-alternative" }}# {{ .Title }}

{{ .RawContent }}{{ end }}
{{- else -}}
{{- $page := . -}}
{{- $active := partial "exception/resolve-active-page.html" $page -}}
{{- $isActiveException := and site.Params.enable_exceptions $page.Params.exception (ne $active.RelPermalink $page.RelPermalink) -}}
{{- $brandName := strings.TrimSpace ($active.Params.brand_name | default "Oahu Underground") -}}
{{- $tipsEmail := .Site.Params.tips_email | default "tips@gtcode.com" -}}
{{- $contactEmail := .Site.Params.contact_email | default "inquire@gtcode.com" -}}
{{- $investigationPagesAll := sort (where (where (where .Site.RegularPages "Type" "investigation") "Params.homepage_exclude" "ne" true) "Params.series" "ne" "The Architecture of Access") "Date" "desc" -}}
{{- $investigationPagesAll = where $investigationPagesAll "Title" "ne" "The Architecture of Access" -}}
{{- $investigationPagesAll = where $investigationPagesAll "Params.portfolio_key" "hawaii-courts" -}}
{{- $investigationPagesAll = partial "exception/filter-list-pages.html" $investigationPagesAll -}}
{{- $investigationPagesEn := where $investigationPagesAll "Params.language" "en" -}}
{{- $investigationPages := cond (gt (len $investigationPagesEn) 0) $investigationPagesEn $investigationPagesAll -}}
{{- $investigationsByUpdated := sort $investigationPages "Lastmod" "desc" -}}
{{- $latestUpdates := first 6 $investigationsByUpdated -}}
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
{{- if $isActiveException -}}
# {{ $active.Title }}

{{ with $active.Description }}{{ . }}

{{ end -}}
{{ (partial "repos-source.html" $active.RawContent) }}
{{- else -}}
{{ with site.GetPage "/homepage-fragments/adult-sequence" }}
# {{ .Title }}

*{{ .Description }}*

{{ .RawContent }}
{{ end }}

## Supporting records and reporting

Longer firsthand accounts:

- [Before the Tax Office](/disclosures/before-the-tax-office/)
- [Prior Law Enforcement Contact and Civic Overlap](/disclosures/prior-law-enforcement-contact/)
- [The Information Trail: open questions and records to obtain](/hawaii-courts/information-trail-2015-2022/)

Linked accounts are not independent corroboration.

The December 2, 2022 courtroom allegation has not been independently established. The sealed audio cannot show the reported gesture.

1. [The Nod](/hawaii-courts/the-nod-visual-allegation/)
2. [The Two Questions](/hawaii-courts/two-questions-wilson-loo/)
3. [The Reporting Duty](/hawaii-courts/reporting-duty-hrpc-8-3b/)

{{ with site.GetPage "/homepage-notice" }}
## {{ .Title }}

{{ .RawContent }}
{{ end }}

## Research portfolios

{{ range slice "/hawaii-courts" "/geopolitics" "/intelligence" "/diagnostics" "/disclosures" "/policy-essays" }}{{ with site.GetPage . }}
- [{{ .Title }}]({{ .RelPermalink }}): {{ .Description }}
{{ end }}{{ end }}

{{ with site.GetPage "/hawaii-courts/closed-loop-oversight-failure" }}
## {{ .Title }}

[Read the series]({{ .RelPermalink }})
{{ end }}

## Recently revised Hawaii Courts files

{{ range $latestUpdates }}
- [{{ .Title }}]({{ .RelPermalink }}) · {{ .Lastmod.Format "January 2, 2006" }}
{{ end }}

## Follow and contact

- [Site RSS](/index.xml)
- [News RSS]({{ $newsRSS }})
- [Reporter disclosures and methodology](/disclosures/)
- [Tips and responses](mailto:{{ $tipsEmail }})
- [AI consulting]({{ $consultingURL }})

## Latest news

{{ range $latestNews }}
- [{{ .Title }}]({{ .RelPermalink }})
{{ end }}
{{- end }}

Original content: all rights reserved. Linking is permitted. Republication requires prior written permission. [Content-use policy]({{ "policies/content-use/" | absURL }}).

{{- end -}}
