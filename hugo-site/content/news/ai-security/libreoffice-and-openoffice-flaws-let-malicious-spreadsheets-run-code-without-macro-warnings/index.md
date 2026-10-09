---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T21:15:15.379922+00:00'
exported_at: '2026-10-07T21:15:17.464632+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html
structured_data:
  about: []
  author: ''
  description: Malicious spreadsheets can make LibreOffice and OpenOffice run Java
    code with Java enabled; LibreOffice has fixed the flaw.
  headline: LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without
    Macro Warnings
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without
  Macro Warnings
updated_at: '2026-10-07T21:15:15.379922+00:00'
url_hash: 893051a996ecd889df4b893632e47b6bb32fcb7a
---

**

Swati Khandelwal
**

Oct 06, 2026

Vulnerability / Open Source

A malicious spreadsheet can make LibreOffice and Apache OpenOffice run an attacker's code as soon as the file is opened, security researchers have shown. There is no warning first, of the kind either program shows before it runs a macro.

The attack works only when the program's Java support is enabled. So far, it has only been shown as a proof of concept, and there are no reports of its use in real attacks.

LibreOffice has already
[fixed the flaw](https://www.libreoffice.org/security/)
, which it tracks as CVE-2026-63277, in updates released on October 5. It recommends that users move to version 26.2.5 or 26.8.0. Versions before those are affected.

Apache OpenOffice has not fixed the matching flaw, which it tracks as CVE-2026-59265. Every version up to and including its current release, 4.1.16, is affected, and the project
[says a fix is expected](https://www.openwall.com/lists/oss-security/2026/10/02/2)
in version 4.1.17, which is still being tested.

Until then, Apache OpenOffice users can block the attack by turning off Java in the program's settings, or by not opening spreadsheets they do not trust.

The attack combines features that each work as intended on their own. A LibreOffice or Apache OpenOffice Calc spreadsheet can hold a "database range", a block of cells that pulls in data from an outside source and refreshes it by itself. That outside source can be a separate database file, called an ODB, named by a web address written into the spreadsheet.

When the spreadsheet is opened, the range refreshes and the program downloads the ODB from that web address. The ODB can name a Java database driver, known as a JDBC driver, and point to where the driver's code lives, which can be a JAR file, a bundle of Java code, or on a remote server. The program then downloads the JAR and starts the driver, which is the attacker's code, inside the program itself.

Each of these is a normal feature. The security problem, the researchers say, is that together they reach code execution without ever asking the user to trust the document, the way the program asks before it runs a macro.

In the
[proof of concept](https://github.com/v12-security/pocs/tree/main/office_jdbc_bugs)
, the driver simply opens the Calculator app, a harmless stand-in, but the same path can run any Java code the attacker chooses. The researchers tested the attack on Windows and Linux and say it is not tied to one operating system.

In their
[demonstration](https://x.com/v12sec/status/2107142692853469503)
, the malicious files sat on the same machine for convenience. The researchers say a real attack would instead place the database file and the code on an attacker-controlled server.

The flaw in LibreOffice was reported independently by Rick de Jager of the V12 security team and by Thomas Rinsma and Edoardo Geraci of Codean Labs. Apache credits Codean Labs for the matching flaw in OpenOffice. The V12 team has published a proof of concept for both programs, and Caolán McNamara of Collabora Productivity wrote the fix for LibreOffice.

The Hacker News has contacted The Document Foundation, which develops LibreOffice, and the Apache OpenOffice project for comment.