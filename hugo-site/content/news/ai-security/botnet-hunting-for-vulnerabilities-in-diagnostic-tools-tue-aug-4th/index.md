---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-10T00:59:23.506019+00:00'
exported_at: '2026-09-10T00:59:22.989195+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33214
structured_data:
  about: []
  author: ''
  description: 'Botnet Hunting for Vulnerabilities in Diagnostic Tools, Author: Johannes
    Ullrich'
  headline: Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33214
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)
updated_at: '2026-09-10T00:59:23.506019+00:00'
url_hash: d8604fbc4f65184f87cb905d2b4e583295a97023
---

This morning, I noticed specific sources "hunting" for vulnerabilities in URLs that I haven't noticed before. All of these URLs appear to be associated with diagnostic tools:

The naming of these URLs points to diagnostic tools. I was unable to find any specific vulnerabilities associated with many of the URLs, but the table above reflects those I found. But diagnostic tools often suffer from file inclusion and code execution vulnerabilities.

These tools will often call operating system commands directly, without properly separating user-provided arguments. Here is a sample vulnerability in a ping utility:

&gt; response = os.system("ping -c 1 -w2 " + hostname )

The above example is in Python. But most (all?) languages have something equivalent to "os.system" (often called "exec", "shell\_exec", "process" ...) Often, proper input validation and output encoding are used to prevent this vulnerability, but, in my opinion, there is a better approach that should always be used in addition to input validation, and I do not see it used much.

As with many other vulnerabilities, the root cause of command injection is the concatenation of user data and commands. Mixing control plane and data plane has been an issue since blue boxing and continues today with prompt injection. The real fix is to avoid this comingling of data and commands and instead properly separate them. Prepared statements in SQL are probably the best-known approach following this principle.

For OS command execution, we do have a very similar solution. The "system" command in your language will typically call the standard C function "exec" [1]. This family of function implements some meant to pass command line arguments: execv ("exec vector"). In addition to the command, it accepts an array of command-line arguments that are then passed to the command, properly separating the command from the arguments.

Python implements execv as part of the subprocess module:

&gt; response = subprocess.run("ping", "-c", 1, "-w", 2, hostname )

Using "subprocess.run" eliminates the possibility of command injection in this example.

For example, if you are using "google.com; ls" as a hostname, you get:

&gt; `ping: cannot resolve google.com; ls: Unknown host`

The entire string "google.com; ls" was used as a hostname, and the ";" no longer acted as a separator. Give it a try with other command injection strings, and you will see similar results.

There are a few cases where "execv" is not sufficient. Some operating system commands may execute additional commands passed on the command line. For example, tcpdump offers the "-z" option to execute a "postrotate command". But these cases are rare, and if you are running into them, you are back to proper input validation to use these specific command line options. In most cases, users cannot specify the command-line option itself but only the parameter; using the "execv" API will help.

A while ago, I also made a brief video with more details on preventing OS command injection:
&lt;https://www.youtube.com/watch?v=7QDO3pZbum8&gt;
. It also covers some of the issues around Windows, which implements different APIs.

[1] https://man7.org/linux/man-pages/man3/exec.3.html

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|