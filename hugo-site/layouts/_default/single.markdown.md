{{- $raw := .RawContent -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}
{{- else -}}
{{- with .Title -}}
# {{ . }}

{{- end -}}
{{- with .Plain -}}
{{- . -}}
{{- end -}}
{{- end -}}

