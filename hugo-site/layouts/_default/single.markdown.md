{{- with .Title }}# {{ . }}{{ "\n\n" }}{{ end -}}
{{- with .Params.subtitle }}## {{ . }}{{ "\n\n" }}{{ end -}}
{{- $raw := trim .RawContent "\n\r\t " -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}
{{- else -}}
{{- with .Plain -}}
{{- . -}}
{{- end -}}
{{- end -}}
