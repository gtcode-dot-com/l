---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-22T04:26:05.154189+00:00'
exported_at: '2026-09-22T04:26:08.984793+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats
structured_data:
  about: []
  author: ''
  description: Signal recently launched Automatic Key Verification, a feature that
    helps validate that your chats are secure without requiring direct safety number
    comparison. Trail of Bits built and operates one of the three auditors that make
    this system trustworthy.
  headline: How Trail of Bits helps verify the integrity of your Signal chats
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Trail of Bits helps verify the integrity of your Signal chats
updated_at: '2026-09-22T04:26:05.154189+00:00'
url_hash: d4a6d4fc3b3e1e2f4243909a7b84eaf2ecb45b19
---

Every Signal chat starts the same way: the client asks the Signal server for the public key associated with your contact’s phone number. But how do you know the server gave you the right key? A compromised server could provide a false public key, allowing the client to encrypt messages to an attacker rather than the intended recipient.

Until now, the only way to detect such malfeasance was to verify safety numbers with your contact in person or over a trusted channel. Signal recently launched an alternative:
[Automatic Key Verification](https://signal.org/blog/automatic-key-verification)
, a feature that helps validate that your chats are secure without requiring direct
[safety number comparison](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed)
. Trail of Bits built and operates one of the three auditors that make this system trustworthy. Our auditor, which is an independent implementation written from scratch, continuously checks that the Automatic Key Verification system behaves honestly.

## How key verification works

Automatic Key Verification is a form of “key transparency” that makes mismatch attacks harder to hide by creating a globally consistent view of the set of public keys associated with each phone number. The Signal app now performs a periodic self-check to ensure that all keys stored in the global map for your account belong to your devices. If the app is unable to verify the log, or finds that not all keys are expected, the user is presented with a warning that “Automatic Key Verification is currently unavailable for your device.” Automatic Key Verification may also be unavailable for other reasons, as outlined in
[Signal’s documentation](https://support.signal.org/hc/en-us/articles/10223569377562-Automatic-Key-Verification)
.

## What our auditor does

Automatic Key Verification depends on external auditors. Trail of Bits helps this system function by providing external verification that the user ↔ public key map is globally consistent and well formed, and does not hide any entries. Each time a new entry is added, we update our local copy of the map, stored as a Merkle tree. Periodically, we sign the head of the tree using a signing key that only we know. Because we commit to only ever signing one consistent lineage of Merkle trees, clients know that they are seeing the same set of public keys as everyone else in the system. Clients currently require signatures from each of three auditors: one operated by Signal, one operated by Cloudflare, and one operated by Trail of Bits.

When Automatic Key Verification is turned on, the Signal client periodically fetches Merkle tree heads from the Signal key transparency server. The client
[requires](https://github.com/signalapp/libsignal/blob/main/rust/keytrans/src/verify.rs#L136-L268)
that each tree head belong to a lineage endorsed by all
[registered auditors](https://github.com/signalapp/libsignal/blob/622d0d52471f3cc9215fe4e9abaac1970018f79c/rust/net/src/env.rs#L392)
within the last seven days. If the server does not present valid auditor signatures, the client will raise a warning and Automatic Key Verification will fail. A fully malicious server may therefore maintain a split view of the system for at most one week before client applications start to display warning messages.

We chose to implement our auditor from scratch, based on the
[specification](https://github.com/trailofbits/signal-auditor/blob/main/docs/Key_Transparency_Auditor_Spec.pdf)
, to provide independent verification; the code is
[open source](https://github.com/trailofbits/signal-auditor)
. Signal also publishes a
[reference implementation](https://github.com/signalapp/key-transparency-auditor)
.

We will provide updates to this blog post if we need to make substantive changes to our signing policy, such as resetting the state of our auditor or rotating our signing key. Our current public key is:

```
7fe5d91de235188486d8fb836a6da37e625e2b10eb6d144185b9364cc83cbbb6
```

## How to use Automatic Key Verification

You can enable Automatic Key Verification in Signal by going to “Settings &gt; Privacy &gt; Advanced” and enabling Automatic Key Verification. In supported chats, you can verify the public key of your counterparty by visiting the safety number verification screen and clicking “Verify Automatically.” Automatic Key Verification often does not support chats where you started the conversation by searching for a recipient’s username. See Signal’s
[help page](https://support.signal.org/hc/en-us/articles/10223569377562-Automatic-Key-Verification)
for more information. If automatic verification fails, users should fall back on safety number comparison.

## Why we’re doing this

We believe that free and private communication is a critical public good. We are not paid by Signal or any other party for this service; we operate it in the interest of users and the community broadly.

Some form of public key integrity is an important component of any full end-to-end encryption system. If you would like to implement key transparency or end-to-end encryption generally,
[contact us](https://trailofbits.com/contact/)
.