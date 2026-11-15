---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T03:51:22.280586+00:00'
exported_at: '2026-11-15T03:51:25.248608+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33488
structured_data:
  about: []
  author: ''
  description: 'The Classics Return: Vulnerable E-Mail Scripts, Author: Johannes Ullrich'
  headline: 'The Classics Return: Vulnerable E-Mail Scripts, (Wed, Nov 4th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33488
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'The Classics Return: Vulnerable E-Mail Scripts, (Wed, Nov 4th)'
updated_at: '2026-11-15T03:51:22.280586+00:00'
url_hash: 7dcd83260d7cc003d17e6a5a8c76c7ae51a9039c
---

One of the early web application vulnerabilities I remember was CVE-2000-0411 [CVE]. This was a simple vulnerability in a CGI-bin script used to send e-mail. The vulnerability was pretty straightforward: Adding additional parameters to the URL leaked environment variables. Other vulnerabilities allowed setting the "To" address and were heavily abused by spammers. And if parameters were passed directly to the sendmail binary, similar vulnerabilities could allow arbitrary code execution.

Today, I noticed a slight resurgence in scans targeting e-mail scripts on our honeypots. Today, there are numerous scripts like the old "formail" scripts, and it is hard to link a specific vulnerability to any of these scans. But my main suspect is spammers looking for webforms that allow setting arbitrary "To" headers. The URLs I am seeing:

&gt; `"/sendmail.php"
&gt;
&gt; "/test-mail.php"
&gt;
&gt; "/testemail.php"
&gt;
&gt; "/config/mail_config.php"
&gt;
&gt; "/mail_config.php"
&gt;
&gt; "/email-test.php"
&gt;
&gt; "/mailtest.php"`

In particular, the "Test" part of the filename suggests that the attacker is not looking for production scripts, but for test scripts left behind during development. This, along with the requests for credential/secret files that top our "Leaderboard," points to a more fundamental issue: Code hygiene. Do not leave behind development artifacts that should never have reached a live website.

For example, some excerpts from a random "mailtest.php" script that came back in a Google search [mailtest]:

&gt; `&lt;?php`
&gt;
&gt; `/*
&gt;
&gt; DONT FORGET TO DELETE THIS SCRIPT WHEN FINISHED!
&gt;
&gt; */`
&gt;
&gt; `$server = array(
&gt;
&gt; 'HTTP_HOST', 'SERVER_NAME', 'SERVER_ADDR', 'SERVER_PORT',
&gt;
&gt; 'SERVER_ADMIN', 'SERVER_SIGNATURE', 'SERVER_SOFTWARE',
&gt;
&gt; 'REMOTE_ADDR', 'DOCUMENT_ROOT', 'REQUEST_URI',
&gt;
&gt; 'SCRIPT_NAME', 'SCRIPT_FILENAME',
&gt;
&gt; );
&gt;
&gt;
&gt; $to      = ( isset( $_GET['email'] ) ? $_GET['email'] : FALSE );
&gt;
&gt; $subject = 'Mail Test Successful for ' . $_SERVER['HTTP_HOST'];
&gt;
&gt; $message = '';`
&gt;
&gt; `![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-11-04%20at%208_22_06%E2%80%AFAM.png)
&gt; ???????    foreach ( $server as $s )
&gt;
&gt; {
&gt;
&gt; $message .= sprintf( '%s: %s', $s, $_SERVER[$s] ) . PHP_EOL;
&gt;
&gt; };`
&gt;
&gt; `$success = mail( $to, $subject, $message, $headers );`

The comment at the top says it all: This is not meant for production use, and even on a development site, it should likely be deployed only briefly for debugging. The script takes any "To" address from the "email" GET parameter and exfiltrates/displays part of the server configuration. It can be useful to scan your own hosts for some of these URLs as an additional control, but you really want to catch these issues during application deployment.

[CVE] https://nvd.nist.gov/vuln/detail/cve-2000-0411

[mailtest] https://gist.github.com/Porrapat/60ed7411d933122fc481

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|