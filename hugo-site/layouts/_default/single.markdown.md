{{- $page := . -}}
{{- $active := partial "exception/resolve-active-page.html" $page -}}
{{- with $active.Title }}# {{ . }}{{ "\n\n" }}{{ end -}}
{{- with $active.Params.subtitle }}## {{ . }}{{ "\n\n" }}{{ end -}}
{{- $raw := trim (partial "repos-source.html" $active.RawContent) "\n\r\t " -}}
{{- if gt (len (trim $raw "\n\r\t ")) 0 -}}
{{- $raw -}}
{{- else -}}
{{- with $active.Plain -}}
{{- . -}}
{{- end -}}
{{- end -}}
{{ with partial "content-use-notice.txt" . }}{{ "\n\n---\n\n" }}{{ . }}{{ "\n" }}{{ end }}
