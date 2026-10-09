---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-21T10:15:13.679130+00:00'
exported_at: '2026-01-21T10:15:15.933841+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32644
structured_data:
  about: []
  author: ''
  description: 'Automatic Script Execution In Visual Studio Code, Author: Xavier Mertens'
  headline: Automatic Script Execution In Visual Studio Code, (Wed, Jan 21st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32644
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Automatic Script Execution In Visual Studio Code, (Wed, Jan 21st)
updated_at: '2026-01-21T10:15:13.679130+00:00'
url_hash: 159e88d295dfe35fa5035c680e12d66e38d60d9a
---

Visual Studio Code is a popular open-source code editor[
[1](https://code.visualstudio.com)
]. But it’s much more than a simple editor, it’s a complete development platform that supports many languages and it is available on multiple platforms. Used by developers worldwide, it’s a juicy target for threat actors because it can be extended with extensions.

Of course, it became a new playground for bad guys and malicious extensions were already discovered multiple times, like the 'Dracula Official' theme[
[2](https://www.bleepingcomputer.com/news/security/malicious-vscode-extensions-with-millions-of-installs-discovered/)
]. Their modus-operandi is always the same: they take the legitimate extension and include scripts that perform malicious actions.

VSCode has also many features that help developers in their day to day job. One of them is the execution of automatic tasks on specific events. Think about the automatic macro execution in Microsoft Office.

With VSCode, it’s easy to implement and it’s based on a simple JSON file. Create in your project directory a sub-directory ".vscode" and, inside this one, create a “tasks.json”. Here is an example:

```
PS C:\temp\MyProject> cat .\.vscode\tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": “ISC PoC,
      "type": "shell",
      "command": "powershell",
      "args": [
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-EncodedCommand",
      "QQBkAGQALQBUAHkAcABlACAALQBBAHMAcwBlAG0AYgBsAHkATgBhAG0AZQAgAFAAcgBlAHMAZQBuAHQAYQB0AGkAbwBuAEYAcgBhAG0AZQB3AG8AcgBrADsAIABbAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAE0AZQBzAHMAYQBnAGUAQgBvAHgAXQA6ADoAUwBoAG8AdwAoACcASQAgAGEAbQAgAG4AbwB0ACAAbQBhAGwAaQBjAGkAbwB1AHMAIQAgAH0AOgAtAD4AJwAsACAAJwBJAFMAQwAgAFAAbwBDACcAKQAgAHwAIABPAHUAdAAtAE4AdQBsAGwA"
      ],
      "problemMatcher": [],
      "runOptions": {
        "runOn": "folderOpen"
      },
    }
  ]
}
```

The key element in this JSON file is the "runOn" method: The script will be triggered when the folder will be opened by VSCode.

If you see some Base64 encode stuff, you can imagine that some obfuscation is in place. Now, launch VSCode from the project directory and you should see this:

![](https://isc.sans.edu/diaryimages/images/isc-20260121-1.png)

The Base64 data is just this code:

```
Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('I am not malicious! }:->', 'ISC PoC') | Out-Null
```

This technique has already been implemented by some threat actors![
[3](https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure)
]!

Be careful if you see some unexpected ".vscode" directories!

[1]
<https://code.visualstudio.com>

[2]
<https://www.bleepingcomputer.com/news/security/malicious-vscode-extensions-with-millions-of-installs-discovered/>

[3]
<https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)