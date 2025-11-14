{{- with .Title -}}
# {{ . }}

{{- end -}}

{{- $raw := .RawContent -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}

{{- end -}}

{{- $sections := .Site.Sections -}}
{{- if gt (len $sections) 0 -}}
## Site Sections

{{- range sort $sections "Title" }}
- [{{ .Title }}]({{ .RelPermalink }}) — {{ len .Pages }} pages{{- with .Params.description }} · {{ . }}{{- end }}
{{- end }}

{{- end -}}

{{- $news := first 10 (sort (where .Site.RegularPages "Section" "news") "Date" "desc") -}}
{{- if gt (len $news) 0 -}}
## Latest News

{{- range $news }}
- [{{ .Title }}]({{ .RelPermalink }}){{- with .Date }} — {{ .Format "2006-01-02" }}{{- end }}
{{- end }}

{{- end -}}

