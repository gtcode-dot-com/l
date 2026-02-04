{{- with .Title -}}
# {{ . }}

{{- end -}}
{{- $raw := .RawContent -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}
{{- else -}}
{{- with .Plain -}}
{{- . -}}
{{- end -}}
{{- end -}}

