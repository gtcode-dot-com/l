---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-01T19:24:28.455859+00:00'
exported_at: '2026-10-01T19:24:31.363606+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33306
structured_data:
  about: []
  author: ''
  description: 'Honeypot-Omaha and batch.py [Guest Diary], Author: Guy Bruneau'
  headline: Honeypot-Omaha and batch.py &#x5b;Guest Diary&#x5d;, (Wed, Sep 2nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33306
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Honeypot-Omaha and batch.py &#x5b;Guest Diary&#x5d;, (Wed, Sep 2nd)
updated_at: '2026-10-01T19:24:28.455859+00:00'
url_hash: 1fa23c3492c69dbc742df1900934707ee06167c0
---

[This is a Guest Diary by Frank Igbokwe, an ISC intern as part of the SANS.edu BACS program]

Honeypot-Omaha is a DShied Sensor located at the Internet Storm Center (ISC) that is set up as a decoy for the original target and deployed over the internet. It is a flawed and very vulnerable system that was intentionally designed to attract threat actors with malicious intents. I view it as a massive log aggregator that collects data that an analyst like myself can then analyse, hypothesize, synthesize and then generate a cohesive and coherent report.

DShield Sensor uses a collective of tools to track internet threat actors, one of those packaged tools is called “cowrie”. It emulates port twenty-two and twenty-three, which are secure shell and telnet. Automation is at its rise and almost everything has been or would be automated at some point in time. From botnets to password brute force attacks to credentials scraping and gathering of data, we observe more automated activities.

Tools like hashcat and jack the ripper make credential collection easy. So, cowrie waits and listens on the decoy ports set up for DShield Sensor. It exposes these ports to the public facing internet and relays the data to a centralized station (ISC). Which logs every information about that threat actor and its activities. “DShield.org” and the Internet Storm Center—founded by Dr. Johannes Ullrich in November 2000 out of the precursor site Incidents.org—provide valuable threat intelligence.

When a potential threat actor infiltrates the sensor, cowrie records their activities. Questions begin to arise like methods used to access the system, what vulnerability was exploited, did they succeed or fail at their attempts, what commands were used, where it was used, what was exfiltrated. With this valuable intel an analyst can build a time frame of when the activity started and ended. Answers to most of these questions asked would be revealed as we proceed.

The next question is how do I correlate and gather all these data of interest, types, and structure. There are web logs, firewall logs, cowrie logs with credentials and other valuable information. I tried using tools like zeek for data behaviour correlation, carving, and analysis, rwfilter for metadata carving of specific fields of interest and converting to silk then my favorite tool, tcpdump for parsing network traffic packets.

All these tools are excellent tools but they are multiple tools that perform specific functions. I needed one tool that could consolidate all my logs of data, filter out the relevant data of interest and use those filtered consolidated data to answer all the questions asked on my internship template. For example, an analyst may want to get more information about a specific internet address, and all the activities engaged by that address.

An analyst has to have a way to input an internet address or fully qualified domain name (FQDN) and it recursively gathers different data of interest related to that address, by searching and querying different “APIs” application programming interfaces for data.

Then converts the data into a tab separated value format, analyzes, correlates, gathers threat intelligence, common vulnerabilities and exposure (CVE), mitre, exploits, threat score, session id, hash and fingerprints, port numbers, geolocation, internet service and cloud service  providers (ISPs or CSP) and a way to mitigate the threat actors activities.

This tool should be able to implement hashing mechanisms using any of the secure algorithms, for example using a combination of symmetric-asymmetric ciphers, and consolidating relevant data across a given directory into one view. Nothing complicated, just a simple script that synthesizes, consolidates data and brings all that into a focused, comprehensive, cohesive functionality and possibly more. Now you see where I am going with this delima.

All data are important but which ones are  relevant to solving my internship questions. After a long research, I had an “Aha!” moment, you can call it an epiphany or what I call my “eureka” moment. That's where the idea of a “batch” process was formulated. I use my recently gained knowledge and skills of the python programming language to write a script called “batch.py”.

Batch is a script based on the python programming language, I wrote to assist me do most of what I described above. Here is the step by step breakdown of what it does. It is composed of “Four” integrated phases of the analysis processing pipeline. The fidelity of “batch.py” is based on the raw logs it parses. For now the logs must be located in the same directory as batch.py. I use secure copy (scp) to download my logs located on my amazon web services to a local directory on my computer.


As a security conscious analyst, persistence security of data should be a priority. This is the start of “batch”, you can either log in as full admin or grant access to guests. To use the
batch.py
program you start by running a bash script on your local terminal window to generate a master password, I use a mac. It uses the secure hashing algorithm(SHA-256) to generate a master and a guest token.You have to generate a master password first by executing the bash script below.

**Start:**

Generating master password or guest passcode.


![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic1.png)


Authentication and verification are used to prevent unauthorized access to sensitive data. The principle of least privilege (POLP) is a necessary requirement for accountability, monitoring, and data loss prevention.

Select an option for the authentication process.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic2.png)

If option two is chosen and an analyst does not have a guest passcode, a message will be generated notifying the analyst that they need to have a guest passcode for them to access the program.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic3.png)

Select option 3 to generate a guest passcode and login.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic4.png)

**Phase 1**

After an analyst authenticates and is verified, the phase one process starts by gathering and feeding relevant data through the analysis pipeline, then converts the .json, .log, .gz, and any other relevant data to a .tsv file format. “TSV” stands for tab separated values.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic5.png)

The gathered intelligence data from querying
ip-api.com
,
cve.org
and
paloaltonetworks.com
are broken down into sections and fields to delineate the processing stages. With the integrated unified analysis pipeline design, batch.py is engineered for efficiency, low latency, and the rapid parsing of large volumes of logs.

**Phase 2**

**Stage: 1**

This displays on your screen showing a summary of the top 10 unique internet addresses that made contact with honeypot\_omaha.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic6.png)

**Stage: 2**

As you can observe on what is displayed on the screen. I only have two cowrie protocols shown. There are more but on this stage I am focusing on just a few of the protocols used by cowrie.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic7.png)

**Stage: 3**

This displays on your screen the top 10 correlation of usernames to their respective internet address.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic8.png)

**Stage: 4**

This shows the top 10 correlation of passwords to their respective internet addresses.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic9.png)

**Stage: 5**

This displays the top 10 talkers with possible threat intelligence, attempts, geolocation, and their respective internet service and cloud providers. Not all top talkers are threat actors or have malicious intents. This requires the know-how and expertise of trained analysts to dissect and discern relevant data from noise.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic10.png)

**Stage: 6**

As an analyst, a long tail analysis of the data of interest will give you an idea of where to start your analysis. Sometimes threat actors use beaconing and command and control to relay data back and forth. Check for specific time intervals.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic11.png)

**Stage: 7**

Batch aggregates all the data it has parsed and gives a summary of how many attempts were made by the threat actors to an endpoint.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic12.png)

**Phase 3**

Generates a summary report and visual pie chart compilation.

**Stage: 8**

Compilation and summarization of data, using matplotlib to create the pie charts in a png file format and generating text document reports.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic13.png)

**Phase 4**

This phase displays an interactive menu an analyst can use to further examine and analyze data. It comprises six numbered menu points. Let's start with the first menu.

**Stage: 9**

An easy navigation menu for an analyst to access detailed information on a given threat actor's internet address and activities.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic14.png)

**Menu 1**

Any artifacts found or indication of compromise will be displayed here using the program "less". Instead of having my data clutter and flood my screen, less seems like a better option.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic15.png)

**Menu 2**

This is a cumulation of all the exploits used by the malicious actors. It is a lot and it is sorted by the highest threat rating score.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic16.png)

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic17.png)

**Menu 3**

Option menu three is used to navigate the pie chart options. An analyst has the choice of generating an individual chart or both.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic18.png)

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic19.png)

It is always good practice to provide error feedback if the program fails to execute seamlessly.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic20.png)

The pie chart is dynamically generated once the pipeline is initiated. An analyst can choose any of the options to initiate the process of populating the pie chart with the data of interest, and displaying it on the monitor.  Below is an example of a dynamically generated pie chart with all information.

The pie chart below shows the top talkers, protocols, usernames, and passwords.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic21.png)

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic22.png)

Made using matplotlib.

**Menu 4**

This menu option is a quick console overview of what was found when batch executed and initiated the unified processing pipeline.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic23.png)

There are over four hundred file artifacts discovered. The data is viewed using the “ less” program, an analyst can use the built-in sort functionality to sort the data.

**Menu 5**

An analyst can query an internet address or fully qualified domain name and search for more data related to that internet address. A "

honeypot\_Omaha\_query\_reoprt.txt
"  is generated.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic24.png)

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic25.png)

After some analysis I observed that the threat actor made twenty-eight attempts and it shows a lot of the malicious actors' detailed activities. An analyst can use this consolidated view to analyze the data all in one screen. It displays the behavior analysis, pattern, utc timestamps, a count of how many attempts were made, the threat actors credentials and more.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic26.png)

Attempt number five displays the malicious actor’s secure shell client hash fingerprint:
2ec37a7cc8daf20b10e1ad6221061ca5
showing an established session. Attempt number 6 shows a failed login.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic27.png)

At attempt number eight, the threat actor used a different password. Attempt number nine shows the secure shell version used. An analyst can track session id, there are five recorded sessions made by the threat actor.

A new connection and login were successfully established at attempt number ten and eleven, batch displays the fingerprint and login details

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic28.png)

The malicious actor has gained access to the system. I observed multiple commands executed on attempt number thirteen, such as exporting of the “usr/local/sbin”. This is the location that contains the system administration program tools and daemons installed locally by the owner of the system. “uname” and "Busybox” are visible, this threat actor gained and exfiltrated a wealth of information about the compromised system. The threat actor is covering up its activities by using this command “rm -rf filter”. This command recursively deletes any file or folder that is named filter. The rm removes any shell commands used in a Linux operating system, -r stands for recursive, which is used to perform a deep granular deletion of data forcefully. I am going to make an educated guess\*\*—\*\*Basically, the threat actor is probing, gathering data, and cleaning up their tracks.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic29.png)

Connection lost on attempt number fifteen.

The malicious actor is now using a different password as displayed on attempt number sixteen.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic30.png)

A failed attempt was logged on attempt number nineteen and the connection was lost at attempt number twenty. Another attempt to re-establish a connection was successful as observed on attempt number twenty-four.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic31.png)

As an analyst, you are a step behind the threat actor and must follow whatever digital breadcrumbs they leave behind to understand their movements. Every action creates a pattern—often captured by the acronym “RIPLE” (Reconnaissance, Initial exploitation, Persistence-privilege escalation, Lateral movement, and Exfiltration of data). As I often say, if you throw a rock into a pond, it produces a ripple effect.

The relentless, defenseless assault on honeypot\_omaha continued, as shown on attempt number twenty-six.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic32.png)

Connection lost again and the threat actor exited as displayed on the screen at attempt number twenty-eight. A summary report of the threat actors’ activities is generated below.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic33.png)

Reflecting back to the original questions at the beginning of the diary. How did the threat actor gain access to the system, what was exfiltrated, and how do I as an analyst go about gathering more data for further investigation?

Recalling from the previous discussions, cowrie is designed to be vulnerable, so the malicious actor was able to guess the username and password.

Summary report on the shell commands executed on honeypot\_omaha is generated and displayed on the screen.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic34.png)

The batch.py script performed a detailed query on the application programming interfaces of  cve.org, paloaltonetworks.com and ip-api.com to generate and correlate intelligence data related to a suspected system compromise. It displays the threat rating score, status code, associated exploits, attack intent, and mitigation strategies. The targeted endpoints are sorted by their threat rating score and displayed below.

![](https://isc.sans.edu/diaryimages/images/Frank_Igbokwe_pic35.png)

Reconnaissance and script profiling reveal the behavioral fingerprints of automated malware, botnets, or exploit payloads when they first gain access to a compromised shell\*\*—in this case,\*\* captured by honeypot\_omaha as a “cowrie.command.input” event. Always practice persistence defense in depth, principle of least privilege’ and continuous diagnostics and mitigation.

As an analyst, I was inquisitive about the data and conducted Google research on the internet service provider called “Pptechnology limited” and the executed commands. Below is a description of the internet service provider and a breakdown of what each section of the command does:

PPTECHNOLOGY LIMITED
: Often associated with the brand/network name PTechnology) is a corporate entity and network infrastructure holder that has appeared in cybersecurity research, threat intelligence reports, and UK corporate registries.

Corporate Profile &amp; UK Registration

Company Status: According to UK Companies House records, PPTECHNOLOGY LIMITED (Company Number: 12176225) was incorporated on August 27, 2019, and was officially dissolved on December 23, 2025.

Registered Address: It was registered at a mass-registration virtual office address in London (35 Firs Avenue)—a location known for hosting thousands of distinct corporate entities.

Registered Nature of Business: Officially classified under SIC code 96090 (Other service activities not elsewhere classified).

**Threat Intelligence Context**

In cybersecurity investigations (such as threat-hunting reports tracking offshore or "bulletproof-style" hosting infrastructure—notably research by firms like
[Team Cymru](https://www.team-cymru.com/)
examining networks associated with anonymous hosting, ignore-DMCA setups, and malicious campaigns like Jingle Shells), PPTECHNOLOGY LIMITED has surfaced in analyses of proxy infrastructure:

Shell/Paper Companies: Security researchers have identified that shell and dormant UK entities like PPTECHNOLOGY LIMITED are frequently used as corporate facades or administrative holders for IP space and backend infrastructure associated with high-privacy or quasi-anonymous hosting environments.

Fraud Risk Scoring: Due to the nature of the IP blocks assigned to or historically associated with it, security scoring engines (like Scamalytics or VirusTotal) often flag traffic originating from these ranges as carrying higher risk or anonymity traits.

Note: The analysis above was performed by the analyst, using Google.com solely to research the internet service provider and executed commands.

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu