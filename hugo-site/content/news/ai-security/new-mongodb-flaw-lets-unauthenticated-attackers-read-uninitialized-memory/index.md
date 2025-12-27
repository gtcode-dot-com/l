---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-27T12:03:13.091999+00:00'
exported_at: '2025-12-27T12:03:15.314401+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-mongodb-flaw-lets-unauthenticated.html
structured_data:
  about: []
  author: ''
  description: High-severity CVE-2025-14847 allows unauthenticated attackers to read
    uninitialized heap memory in MongoDB due to a zlib compression handling flaw.
  headline: New MongoDB Flaw Lets Unauthenticated Attackers Read Uninitialized Memory
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-mongodb-flaw-lets-unauthenticated.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New MongoDB Flaw Lets Unauthenticated Attackers Read Uninitialized Memory
updated_at: '2025-12-27T12:03:13.091999+00:00'
url_hash: 01b9dbf5d844b52f11d9b3058cfdd50caa3da0c8
---

**

Dec 27, 2025
**

Ravie Lakshmanan

Database Security / Vulnerability

A high-severity security flaw has been disclosed in MongoDB that could allow unauthenticated users to read uninitialized heap memory.

The vulnerability, tracked as
**CVE-2025-14847**
(CVSS score: 8.7), has been described as a case of
[improper handling of length parameter inconsistency](https://cwe.mitre.org/data/definitions/130.html)
, which arises when a program fails to appropriately tackle scenarios where a length field is inconsistent with the actual length of the associated data.

"Mismatched length fields in Zlib compressed protocol headers may allow a read of uninitialized heap memory by an unauthenticated client," according to a
[description](https://www.cve.org/CVERecord?id=CVE-2025-14847)
of the flaw in CVE.org.

The flaw impacts the following versions of the database -

* MongoDB 8.2.0 through 8.2.3
* MongoDB 8.0.0 through 8.0.16
* MongoDB 7.0.0 through 7.0.26
* MongoDB 6.0.0 through 6.0.26
* MongoDB 5.0.0 through 5.0.31
* MongoDB 4.4.0 through 4.4.29
* All MongoDB Server v4.2 versions
* All MongoDB Server v4.0 versions
* All MongoDB Server v3.6 versions

The issue has been addressed in MongoDB versions 8.2.3, 8.0.17, 7.0.28, 6.0.27, 5.0.32, and 4.4.30.

"An client-side exploit of the Server's zlib implementation can return uninitialized heap memory without authenticating to the server," MongoDB
[said](https://jira.mongodb.org/browse/SERVER-115508)
. "We strongly recommend upgrading to a fixed version as soon as possible."

If immediate update is not an option, it's recommended to
[disable zlib compression](https://www.mongodb.com/docs/drivers/node/current/connect/connection-options/network-compression/)
on the MongoDB Server by starting mongod or mongos with a
[networkMessageCompressors](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--networkMessageCompressors)
or a
[net.compression.compressors](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-net.compression.compressors)
option that explicitly omits zlib. The other compressor options supported by MongoDB are snappy and zstd.

"CVE-2025-14847 allows a remote, unauthenticated attacker to trigger a condition in which the MongoDB server may return uninitialized memory from its heap," OP Innovate
[said](https://op-c.net/blog/mongodb-zlib-protocol-vulnerability-cve-2025-14847/)
. "This could result in the disclosure of sensitive in-memory data, including internal state information, pointers, or other data that may assist an attacker in further exploitation."