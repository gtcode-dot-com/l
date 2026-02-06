{{- with .Title -}}
# {{ . }}

{{ end -}}
{{ .RawContent }}

{{- $articles := first 5 (sort (where .Site.RegularPages "Section" "articles") "Date" "desc") -}}
{{- if gt (len $articles) 0 -}}
## Latest Articles

{{- range $articles }}
- [{{ .Title }}]({{ .RelPermalink }}){{- with .Date }} — {{ .Format "2006-01-02" }}{{- end }}{{- with .Params.meta_description }}
  {{ . }}{{- end }}
{{- end }}

{{ end -}}

{{- $sections := .Site.Sections -}}
{{- if gt (len $sections) 0 -}}
## Site Sections

{{- range sort $sections "Title" }}
- [{{ .Title }}]({{ .RelPermalink }}) — {{ len .Pages }} pages{{- with .Params.description }} · {{ . }}{{- end }}
{{- end }}

{{ end -}}

{{- $news := first 10 (sort (where .Site.RegularPages "Section" "news") "Date" "desc") -}}
{{- if gt (len $news) 0 -}}
## Latest News

{{- range $news }}
- [{{ .Title }}]({{ .RelPermalink }}){{- with .Date }} — {{ .Format "2006-01-02" }}{{- end }}
{{- end }}

{{ end -}}
