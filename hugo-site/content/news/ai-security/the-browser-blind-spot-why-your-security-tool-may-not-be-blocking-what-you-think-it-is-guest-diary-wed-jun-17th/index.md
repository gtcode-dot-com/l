---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T04:33:40.864054+00:00'
exported_at: '2026-06-23T04:33:42.910185+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33084
structured_data:
  about: []
  author: ''
  description: 'The browser blind spot: Why your security tool may not be blocking
    what you think it is [Guest Diary], Author: Johannes Ullrich'
  headline: 'The browser blind spot: Why your security tool may not be blocking what
    you think it is &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33084
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'The browser blind spot: Why your security tool may not be blocking what you
  think it is &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)'
updated_at: '2026-06-23T04:33:40.864054+00:00'
url_hash: f36b1f64253eeb66de0d9552b78b558af83446f6
---

[This is a guest diary submitted by Varun Murdula]

### SUMMARY

CASB block policies rely on inspecting TCP traffic. QUIC, the protocol powering HTTP/3, runs over UDP, a protocol most CASBs cannot inspect. The result: Chrome can reach a destination your CASB is supposed to block, and nothing in the logs shows it happened. This article explains the gap, how to test for it, and what to do about it.

When a security team blocks access to a website or cloud service, the assumption is simple: the block is in place, so users cannot reach that destination. The rule is configured. The tool is running.

&gt; "Job done. Time for coffee."

That assumption is often wrong. When it is, there is nothing in the logs to tell you.

I ran a test across five browsers on a managed endpoint with an active CASB policy. What I found is what this article describes. There is a real enforcement gap in how CASBs handle browser traffic. It is documented by the security vendors themselves, including published guidance from Palo Alto Networks, Forcepoint, and Cloudflare. But many security teams have never tested for it and do not know it applies to them. The tools are doing what they were designed to do. The way CASBs were built predates how browsers behave today. A block policy can look completely fine in every log and dashboard while traffic to the blocked destination flows freely through a different browser on the same machine.

### First, what is a CASB?

A Cloud Access Security Broker (CASB, pronounced “cazz-bee”) is a security tool that sits between an organization’s users and the internet. Gartner, which coined the term in 2012, defines it as “on-premises, or cloud-based security policy enforcement points, placed between cloud service consumers and cloud service providers to combine and interject enterprise security policies as the cloud-based resources are accessed.”10 In plain terms: it sits in the path of every internet connection and decides what gets through.

Proxy mode is the most common deployment for web traffic inspection. In this mode, every time a browser connects to a website or service, the CASB intercepts the request, checks it against policy rules, and either allows it or blocks it. It acts like a security checkpoint on every outbound internet connection.

CASBs are used to stop employees from sending sensitive data to places their organization does not permit: personal cloud storage, unauthorized file sharing tools, and generative AI chatbots where organizational policies may prohibit data sharing.

To inspect web traffic, a CASB needs to read the content of the connection, including encrypted ones. The vast majority of web traffic today is encrypted using Transport Layer Security (TLS). A protocol is a set of rules for how data travels across a network. TLS encrypts data in transit so only the sender and recipient can read it. It is the technology behind the padlock icon in your browser’s address bar.

To inspect TLS-encrypted traffic, a CASB performs SSL/TLS inspection (SSL stands for Secure Sockets Layer, TLS’s older predecessor). The CASB intercepts the connection and decrypts it. It then inspects the content, applies its policy, re-encrypts the traffic, and forwards it on. From the user’s side, nothing looks different. The padlock is still in the address bar.

For this to work, the CASB needs the browser to trust its re-signed certificates. It does that by installing a root Certificate Authority (CA) certificate into the device’s trusted certificate store, a list of credentials the device recognizes as legitimate. Once that certificate is there, the browser trusts the CASB’s re-signed traffic and continues normally.

This works fine, but not every browser on the device handles that certificate the same way.

### How QUIC creates a gap in your CASB coverage

Two things explain this gap.

The first is QUIC, a modern transport protocol developed by Google and standardized by the IETF.1 It was designed to make web connections faster and more reliable. It was not designed to circumvent enterprise security controls. This gap exists because proxy-based inspection tools were built around TCP, not because QUIC has a flaw. The name is not an acronym. Google just called it QUIC.

The second is the difference between TCP and UDP, the two transport mechanisms that determine whether your CASB ever sees the traffic.

TCP (Transmission Control Protocol) is the traditional protocol behind most internet traffic. Ordered, reliable, and what CASB SSL/TLS inspection is built around.

UDP (User Datagram Protocol) is a faster, lower-overhead alternative. It trades some of TCP’s reliability for speed and does not require the same connection handshake.

QUIC runs over UDP, not TCP. CASB inspection only works on TCP, so it never sees QUIC traffic.

&gt; "Chrome took the side door. The CASB was watching the front."

QUIC is the transport behind HTTP/3 (the third version of the Hypertext Transfer Protocol, the language of the web). Chrome learns which servers support QUIC through previous connections, Alt-Svc headers, or DNS HTTPS records (RFC 9460), which let servers signal QUIC support before a connection even starts.9 Once Chrome knows a server supports QUIC, it tries it automatically. When that happens, the traffic goes over UDP. The CASB only monitors TCP, so it never sees the connection. No block fires and nothing is logged.

&gt; KEY FINDING:  A user on a managed laptop can reach a destination the CASB is supposed to block, simply because Chrome used QUIC over UDP instead of TCP. The tool is running. The policy is active. The block does not fire.

These are not hypothetical concerns. Palo Alto Networks explicitly recommends blocking QUIC in their internet gateway security best practices.2 Forcepoint published a dedicated advisory documenting that QUIC traffic from Chrome, Edge, Brave, Firefox, and Safari may not be intercepted by their proxy.3 Cloudflare’s gateway documentation states directly: if the UDP proxy or TLS decryption is off, HTTP/3 traffic from Chrome bypasses inspection entirely. [4]

### The broader problem: Browsers do not all behave the same way

QUIC is the clearest example, but it is not the only way enforcement can fail across browsers.

When a CASB policy is set up and tested, it is usually tested once, from a single browser, and signed off as working. Most teams never verify whether the policy is enforced consistently across every browser on managed devices.

&gt; "One browser tested. Zero browsers questioned. Ticket closed."

Keep Aware’s 2026 Browser Security Report makes the point clearly: DLP and CASB tools were built for a different era of computing, one defined by email attachments, file transfers, and endpoint storage.5 They were never designed for what people actually do in a browser today: typing sensitive data into a web form, pasting content into an AI chatbot, uploading files through a browser interface.

Some DLP tools enforce policy through a browser extension rather than a network proxy. That extension only works in browsers where it was deployed.6 Use a different browser on the same machine and the enforcement is gone entirely.

### Why this is invisible in standard log review

That missing coverage does not generate an alert. It leaves no trace.

When QUIC bypasses the proxy, the traffic never touches the inspection pipeline. The CASB sees nothing. No failed block, no error, no anomaly. When one browser is enforced and another is not, the CASB log looks clean. Block events from the enforced browser are there. The uninspected traffic from the other browser generates no entries at all.

&gt; "The logs are not lying. They reported exactly what they saw. The problem is they only saw the traffic that came through TCP."

CASB block event counts get used to assess how much traffic reached a blocked destination. But block events only count traffic that entered the inspection pipeline, not all traffic that actually arrived. Where QUIC is unblocked, the real number is higher. Sometimes significantly. In an investigation, that gap means you underestimated how much data actually moved — you scoped the incident wrong.

### Why this gap matters now

Generative AI has changed where sensitive data goes. Industry research consistently shows that employees are sharing internal documents, reports, and confidential data with AI tools at significant scale.[7] Most of it on managed devices, through Chromium-based browsers, reaching destinations that CASB policies are meant to block.

&gt; 223  avg GenAI policy violations per org per month (Netskope 2026)
&gt;
&gt; 2x  sensitive data incidents sent to AI platforms, year over year (Netskope 2026)
&gt;
&gt; 86%  security leaders who believe employees are sharing sensitive data with AI tools without authorization (Code42 2024)

Blocking AI destinations at the CASB layer is the right call. But if QUIC is unblocked and HTTP/3 connections are being established over UDP to those destinations, the block may not be firing for a significant portion of actual traffic. The policy says blocked. The network says otherwise.

For organizations subject to GDPR, HIPAA, PCI DSS, or SOC 2, an undetected enforcement gap like this one is not just a security problem. It is a compliance risk. Regulators do not distinguish between a policy that was misconfigured and one that was never enforced — the outcome is the same.

### How to test whether this gap exists in your environment

Run this on a test device configured the same as production. You need three things. First, the CASB agent active with a block policy targeting a specific URL. Second, all five browsers installed on that device: Safari, Chrome, Brave, Firefox, and Edge. Third, access to your CASB’s log console. URL stands for Uniform Resource Locator, which is just a web address.

&gt; "Takes about twenty minutes. Less time than the average security vendor webinar."

1. Confirm the CASB agent is running and the block policy is active on the test device.
2. Open Safari and navigate to the blocked destination. Verify the block fires and a log event appears in the CASB console.
3. Open Chrome and navigate to the same destination. Does the block fire, or does the page load?
4. Repeat with Brave, Firefox, and Edge separately. Record each result.
5. In Chrome, type chrome://net-export into the address bar. That is Chrome’s built-in network log. Use it to check whether Chrome negotiated a QUIC connection to the destination.
6. At the firewall or proxy, check whether UDP port 443 is being explicitly dropped. If it is allowed through, QUIC bypass is possible.
7. Compare CASB log entries against what you observed in each browser.

What to look for if the gap exists:

| Browser | Engine | Expected result |
| --- | --- | --- |
| **Safari** | WebKit | Block fires. Log event generated. |
| **Chrome** | Chromium / Blink | Page loads. No block. No log entry. |
| **Brave** | Chromium / Blink | Page loads. No block. No log entry. |
| **Firefox** | Gecko | Varies by proxy vendor. Test independently. |
| **Edge** | Chromium / Blink | Chromium-based. Behavior similar to Chrome. |

NOTE ON FIREFOX  Cloudflare’s documentation shows Firefox HTTP/3 inspection can work when the UDP proxy is properly enabled. Behavior varies by CASB vendor. Do not assume Firefox is safe or vulnerable. Test it in your specific environment.

What to do about it

01  Block QUIC at the network layer

Ask your network team to drop UDP/443 traffic at the proxy, Secure Web Gateway (SWG), or firewall. Chromium-based browsers fall back to TCP when QUIC is blocked, and the CASB inspection pipeline takes over. Most platforms handle this gracefully, though some may see a brief delay on the first connection as the browser falls back to TCP. Recommended by Palo Alto Networks, Forcepoint, and Cloudflare. Verify it is actually enforced, not just documented somewhere.

02  Test every browser, not just one

Testing a single browser and calling the control validated is not enough. Safari, Chrome, Brave, Firefox, and Edge each have different protocol behaviors. Every browser in the environment needs to be tested independently, starting at initial deployment and again after any policy changes.

03  Compare CASB logs against what your endpoint actually recorded

Endpoint telemetry shows what programs are running and what connections they are making. A pattern where Safari generates block events for a destination while Chrome generates none on the same device in the same time window is worth investigating. It means the block is not reaching Chrome, not that the user was inactive.

04  Look at controls that live inside the browser, not outside it

Proxy-based enforcement intercepts traffic from the outside. It was designed before QUIC existed and before users spent most of their working day inside a browser. There are tools that work differently: browser-native DLP products, endpoint agents that monitor at the process level, and secure enterprise browsers such as Island or Talon that apply policy from within the browser itself. None of them replaces a CASB, but each one covers gaps that a CASB cannot.

05  Treat CASB event counts as a floor, not a ceiling

In any investigation or data loss review, CASB block event volume is the minimum known traffic, the fraction that entered the inspection pipeline. Actual traffic may be higher. Cross-check against your endpoint logs before you call the scope final.

Conclusion

Nobody wants to find out their block policy was not working by reviewing an incident report. But that is exactly how this gap tends to surface. The logs looked fine. The dashboard was clean. The policy was active. Meanwhile, QUIC connections were going straight to the destination that was supposed to be blocked.

This is not a cutting-edge attack technique. It is a protocol mismatch that has been sitting in enterprise environments for years. Nobody talks about it because the logs never show anything wrong. No alert. No error. Just traffic moving where it should not be, with no corresponding log entry to show for it.

If you take one thing from this: ask your network team to block UDP port 443 at the firewall or proxy, then test every browser in your environment against a blocked destination. Twenty minutes. You might be surprised what you find.

If you are sharing this with leadership: ask your security team to run the test in the section above and report back. The answer will tell you whether your current enforcement is doing what you think it is.

Assume nothing. Test everything.

Glossary of key terms

CASB  Cloud Access Security Broker. A security tool that monitors and controls traffic between users and cloud services. In proxy mode, it acts as a checkpoint on every outbound internet connection.

SSL / TLS  Secure Sockets Layer / Transport Layer Security. Encryption protocols that protect data in transit. The padlock in your browser’s address bar means TLS is active.

CA  Certificate Authority. Issues digital credentials called certificates. In the context of this article, a CASB uses a CA certificate so browsers trust its re-signed traffic during SSL inspection.

TCP  Transmission Control Protocol. The traditional, reliable internet transport protocol. CASB inspection tools are built to intercept TCP traffic.

UDP  User Datagram Protocol. A faster, lower-overhead protocol. QUIC runs over UDP, which is why CASB tools built around TCP cannot inspect it.

QUIC  A modern transport protocol from Google, standardized by the IETF. Runs over UDP and powers HTTP/3. Not an acronym, just a name. Designed for performance, not to bypass security controls.

HTTP/3  The third major version of the Hypertext Transfer Protocol, the language of the web. Uses QUIC as its transport. Supported by most large platforms.

SWG  Secure Web Gateway. A network-level security tool that filters internet traffic, often deployed alongside a CASB.

DLP  Data Loss Prevention. Tools and policies designed to stop sensitive data from leaving an organization without authorization.

SaaS  Software as a Service. Cloud-based software accessed through a browser: email, productivity tools, AI services.

Endpoint  Any device (laptop, desktop, phone) connected to a corporate network or running corporate security software.

Telemetry  Detailed data automatically collected from systems about their activity and connections. Used by security teams to investigate incidents.

URL  Uniform Resource Locator. A web address, what you type into a browser’s address bar.

DNS  Domain Name System. The internet’s directory. Translates web addresses into numeric IP addresses computers use to find servers. Modern DNS records can also signal which protocols a server supports, including QUIC.

Protocol  A set of rules for how data travels across a network. TCP and UDP are both transport protocols, but they work very differently.

References

1.  Internet Engineering Task Force. QUIC: A UDP-Based Multiplexed and Secure Transport. RFC 9000. May 2021.  rfc-editor.org/rfc/rfc9000

2.  Palo Alto Networks. Create the Application Block Rules: Block QUIC. Internet Gateway Best Practices.  docs.paloaltonetworks.com

3.  Forcepoint. QUIC (UDP) Protocol Traffic Can Bypass Forcepoint Cloud and On-Premises Proxies. Support Advisory.  support.forcepoint.com/s/article/000015410

4.  Cloudflare. HTTP/3 Inspection, Cloudflare One Documentation. Accessed June 2026.  developers.cloudflare.com

5.  Keep Aware. 2026 Browser Security Report: Enterprise Blind Spots and AI Risk. March 2026. Coverage via BleepingComputer.  bleepingcomputer.com

6.  Endpoint Protector. Why Browser-Based Workflows Break Traditional DLP. February 2026.  endpointprotector.com

7.  Netskope Threat Labs. Cloud and Threat Report: 2026. January 2026.  netskope.com

8.  Code42 Software. 2024 Data Exposure Report. March 2024.  globenewswire.com

9.  Internet Engineering Task Force. Service Binding and Parameter Specification via the DNS (SVCB and HTTPS Resource Records). RFC 9460. November 2023.  rfc-editor.org/info/rfc9460

10.  Gartner. Definition of Cloud Access Security Brokers (CASBs). Gartner IT Glossary.  gartner.com