---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:16:10.107372+00:00'
exported_at: '2026-10-07T01:16:12.019204+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html
structured_data:
  about: []
  author: ''
  description: MCP Python SDK flaw can let malicious servers redirect OAuth exchanges
    and steal credentials; fixes are in 1.30.0 and 2.2.0.
  headline: Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials
updated_at: '2026-10-07T01:16:10.107372+00:00'
url_hash: 70b35ed4cc7c633acdcb0313efdf823a57a6227c
---

**

Swati Khandelwal
**

Sep 29, 2026

Identity Security / Artificial Intelligence

A malicious MCP server could trick an application built on the official
[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-qx49-fqc8-xw99)
into handing over the OAuth credentials it uses to log in to a real service, the SDK's maintainers said in a security advisory.

Affected versions sent the client secret, the authorization code, and the PKCE proof key to a token endpoint the attacker controlled. The fix is in versions 1.30.0 and 2.2.0.

The Model Context Protocol (MCP) is an open standard for connecting AI applications to outside tools and data, and this package is its official Python SDK for building MCP servers and clients.

With the stolen credentials, the attacker can request a valid access token from the real login service. Cycode, the security firm that
[reported the flaw](https://cycode.com/blog/mcp-python-sdk-oauth-account-takeover/)
, demonstrated that full exchange in a test and says the resulting token carries whatever permissions the app was granted. The client secret is long-lived, so it keeps working until it is changed.

The flaw is rated high (7.5) for the two providers that run without a person present. Scored for the interactive provider, where someone has to start the sign-in, it is 6.5. No CVE had been assigned as of September 29.

### How a server steals the credentials

When an MCP client needs to log in, it asks the server it is connecting to where its login service, called the authorization server, can be found. On the affected versions, the SDK did not always check that answer. A malicious server could point it at a login service of the attacker's choosing, either by naming the attacker's own server or by serving login details that name the user's real service while sending the credentials elsewhere.

The client then sends its secret, its authorization code, and its PKCE proof key to the attacker instead of the real service. The proof key is a one-time value designed to prevent a stolen authorization code from being reused, so handing it over defeats that protection as well.

With the interactive provider, the person still has to approve a sign-in. Cycode says the page they approve is the genuine login page, so nothing looks wrong. The two machine-to-machine providers need no sign-in and no person at all.

### Who is affected

An application is affected if it uses the SDK as an MCP client over HTTP with one of the OAuth providers OAuthClientProvider, ClientCredentialsOAuthProvider, PrivateKeyJWTOAuthProvider, or the deprecated 1.x RFC7523OAuthClientProvider, and it can connect to a server it does not fully control while holding credentials for a real login service. MCP servers built with the SDK, local (stdio) clients, and clients that attach their own tokens are not affected.

| Line | Affected | Fixed in |
| --- | --- | --- |
| 1.x | 1.9.1 through 1.29.1 | 1.30.0 |
| 2.x | 2.0.0 through 2.1.1 | 2.2.0 |

### What to do

Upgrade to
[1.30.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0)
on the 1.x line or
[2.2.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0)
on the 2.x line. In the fixed versions, the client works out which login service it expects before fetching any details and refuses any that name a different one.

Upgrading is not the whole fix for two of the providers. If you use ClientCredentialsOAuthProvider or PrivateKeyJWTOAuthProvider, the advisory says
["upgrading changes nothing until you also pass issuer="](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-qx49-fqc8-xw99)
to name the login service those credentials belong to. Without it, they still follow whichever server the MCP server points them at.

On 1.30.0, the warning about this is a standard deprecation warning, which Python hides by default, so it is easy to miss. The deprecated RFC7523OAuthClientProvider has no issuer= option at all, so move to one of the other two providers.

After upgrading, clear any stored OAuth client registrations once, because older ones are not tied to a login service and stay that way. If a client may already have connected to an untrusted server, rotate its client secret and revoke its tokens at the login service. On older versions, there is no workaround other than connecting only to MCP servers you trust.

### Disclosure

The issuer checks shipped in the 1.30.0 and 2.2.0 release notes on September 7, listed under behavior changes rather than as a security fix. The advisory followed on September 28, the same day Cycode published its writeup. The advisory credits eight reporters, including Cycode's researcher.

Neither the advisory nor Cycode reports any attacks using the flaw, and none has been reported elsewhere.