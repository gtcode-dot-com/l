---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T03:53:08.569336+00:00'
exported_at: '2026-10-08T03:53:10.965500+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
structured_data:
  about: []
  author: ''
  description: LMCache CVE-2026-105192 lets unauthenticated attackers run code when
    the multiprocess server is bound to a routable address; no fix exists.
  headline: Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code
    Remotely
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely
updated_at: '2026-10-08T03:53:08.569336+00:00'
url_hash: 35545ae5e825d85466ebcf359204116a54b9c5de
---

**

Swati Khandelwal
**

Oct 07, 2026

Vulnerability / Artificial Intelligence

A critical vulnerability in
**LMCache**
, open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available.

The flaw is in LMCache's
[multiprocess mode](https://docs.lmcache.ai/mp/index.html)
, where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network message to that server can run commands as the user the LMCache process runs as.

The server can be reached from another machine only when an operator sets it to listen on a routable address, rather than the localhost it uses by default.

[JFrog disclosed the flaw](https://research.jfrog.com/vulnerabilities/lmcache-is-vulnerable-to-unauthenticated-remote-code-execution-via-pickle-deserialization-on-the-multiprocess-zmq-transport-cve-2026-105192-jfsa-2026-001694382/)
on October 7 and assigned it a severity score of 9.8 out of 10, in the critical range, the rating it gives a server bound to a routable address.

The vulnerability, tracked as
[CVE-2026-105192](https://www.cve.org/CVERecord?id=CVE-2026-105192)
, affects LMCache from version 0.3.9, released in October 2025, through 0.5.5, the latest stable release, and is also present in the 0.5.6 release candidates and the development branch. No fixed version exists.

Whether a server is exposed comes down to one setting. By default, the multiprocess server listens only on the local machine, so another host cannot reach it. It becomes reachable when an operator starts it with a routable address, much like multi-node deployments share a cache across machines.

LMCache's own
[example Kubernetes deployment](https://github.com/LMCache/LMCache/blob/v0.5.5/examples/multi_process/lmcache-daemonset.yaml)
starts the server that way, listening on every network interface. A copy of LMCache running inside a single vLLM process does not open the port at all.

The ZeroMQ socket the multiprocess server opens for worker processes to register and share cached data has no authentication. One type of message is
[unpacked with pickle](https://github.com/LMCache/LMCache/blob/v0.5.5/lmcache/v1/platform/base/ipc_wrapper.py)
, a Python format that can carry code and run it as the data is decoded. The server unpacks it while still reading the message's arguments, before any check of the message's type, so a crafted message can run the sender's code.

The code runs with the privileges of the LMCache process. On the project's official container images, that process runs as root, according to JFrog. The flaw was found by Yuval Moravchick of JFrog's security research team.

There is no patched release. Until one ships, JFrog advises operators not to assign the multiprocess server a routable address and to keep its port on the local machine or on a trusted cluster network. A firewall that limits who can reach the port lowers the risk but does not remove it, because any host that can still open a connection can run code.

LMCache has
[not published a security advisory](https://github.com/LMCache/LMCache/security/advisories)
for the flaw. JFrog's advisory does not provide operators with a way to determine whether a server has already been attacked.

### Other Reports and a Related vLLM Fix

Separately, a GitHub user opened six additional LMCache security reports on October 6, the day before CVE-2026-105192 was made public. They allege
[unauthenticated access to cached data](https://github.com/LMCache/LMCache/issues/5507)
belonging to different tenants, as well as to
[several network services](https://github.com/LMCache/LMCache/issues/5508)
that execute commands without a login.

The reports come from one account, rest on proof-of-concept claims, and have no CVE, no confirmation from the maintainers, and no fix. One points to a default LMCache that has since changed: an admin HTTP server that listened on every network interface in 0.5.5 listens only on the local host in the 0.5.6 release candidates.

A related flaw in vLLM is already fixed. Before version 0.30.0, released September 22, a single request carrying a malformed cache\_salt value could crash the engine on deployments that use the LMCache multiprocess connector, a denial-of-service bug tracked as
[CVE-2026-105756](https://github.com/vllm-project/vllm/security/advisories/GHSA-2823-qmq8-rwvj)
. It is rated 6.5 and does not allow code execution.

The core mistake, handing data from an unauthenticated network socket to pickle, is the same one researchers found across other AI inference frameworks in November 2025, in a group of flaws they called
[ShadowMQ](https://thehackernews.com/2025/11/researchers-find-serious-ai-bugs.html)
. Whether LMCache's code shares a common source with those projects has not been established.