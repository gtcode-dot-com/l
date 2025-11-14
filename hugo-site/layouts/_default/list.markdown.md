{{- $raw := .RawContent -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}
{{- else -}}
{{- with .Title -}}
# {{ . }}

{{- end -}}
{{- with .Params.description -}}
{{ . }}

{{- end -}}
{{- end -}}

{{- $pages := .Pages -}}
{{- if gt (len $pages) 0 -}}

## Entries

{{- range $pages.ByDate.Reverse }}
- [{{ .Title }}]({{ .RelPermalink }}){{- with .Params.author }} — {{ . }}{{- end }}{{- with .Date }} ({{ .Format "2006-01-02" }}){{- end }}{{- with .Params.description }} — {{ . }}{{- else }}{{- with .Summary }} — {{ truncate 240 (plainify .) }}{{- end }}{{- end }}
{{- end -}}
{{- else -}}

_No entries available in this section._

{{- end -}}
