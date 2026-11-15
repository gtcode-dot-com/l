---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:13:59.550862+00:00'
exported_at: '2026-11-15T07:14:01.559955+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
structured_data:
  about: []
  author: ''
  description: PostgreSQL fixes 52 security flaws, including CVE-2026-6460, which
    allows users with object creation privileges to execute server code.
  headline: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated
    RCE
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated
  RCE
updated_at: '2026-11-15T07:13:59.550862+00:00'
url_hash: e05f7a78ce38d83c34d2054e4262b63dc4863494
---

**

Swati Khandelwal
**

Nov 13, 2026

Vulnerability / Database Security

A type confusion flaw in
**PostgreSQL**
lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server.

The flaw, tracked as
**CVE-2026-6460**
, has a CVSS score of 8.8. Any code run this way has the rights of the operating system user that runs PostgreSQL. All versions before 18.7, 17.12, 16.16, 15.20, and 14.25 are affected.

The PostgreSQL Global Development Group, which publishes the database's releases, has not reported any attacks using the flaw. CISA's assessment in the CVE record also lists exploitation as none.

The flaw involves composite types, which are types built from named fields, each with its own data type. A field's type can be changed while older values of that type are still held in other parts of the server.

The server could then read an old value as if it had the new type. The fix, described in the project's
[release notes](https://www.postgresql.org/docs/18/release-18-7.html)
, adds version checks so the server can detect a value that no longer matches its type.

Security researcher
**Mehmet Ince**
described a working exploit for the flaw, demonstrated on PostgreSQL 18.6, in a
[technical writeup](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/)
published this week.

His method is to prepare a query that holds a value, change the type of one of the value's fields, and then run the query. The writeup includes the SQL that crashes an unpatched server this way and a second step that leaks memory addresses. It does not include the SQL for the final step, which makes the server run a command.

He wrote that he could "trigger this crash as a lowest-privileged login role." The project's
[security advisory](https://www.postgresql.org/support/security/CVE-2026-6460/)
describes the attacker only as someone who can create objects, without saying which privileges that takes.

Red Hat, which ships PostgreSQL packages, says in its
[CVE assessment](https://access.redhat.com/security/cve/cve-2026-6460)
that an attacker needs a database login with the ability to create or modify objects. None of these sources says whether an account with only default privileges can go beyond the crash to run code.

Ince traces the root of the flaw to May 5, 2004, when PostgreSQL gained the ability to change a column's type. His technique for running code relies on a later change made on May 14, 2015.

He also adapted the exploit for managed PostgreSQL services and privately shared proofs of concept with their security teams in August. The providers he worked with include AWS (Aurora and RDS), Microsoft (Azure PostgreSQL), Google (AlloyDB), Supabase, Databricks, and Ubicloud. The writeup does not give each service's current patch status.

The project credits more than a dozen reporters for
**CVE-2026-6460**
, including the researcher, and credits him on five other flaws in the same release.

The project rates 32 of the 52 flaws at 8.8, the highest score in the release. Based on the scores in its
[vulnerability index](https://www.postgresql.org/support/security/)
, only one flaw in the server requires neither a login nor any user action. That flaw,
**CVE-2026-116322**
, lets an unauthenticated client trigger a restart of PostgreSQL 18 servers.

Several other fixes are in client tools. A crafted archive can make pg\_restore run code as the user running it. A compromised source server can make psql run code through the restore script in pg\_dump's tar output.

### What Administrators Should Do

1. Update the server to 18.7, 17.12, 16.16, 15.20, or 14.25, matching your major version.
2. Rebuild or update every C-language extension at the same time as the server. Extensions built against older releases still load, but they "may not be protected from the vulnerabilities fixed in this release," according to a
   [repository notice](https://yum.postgresql.org/news/extensions-require-minor-release/)
   from the project's RPM package maintainers. Some extensions will also need source-code changes.
3. Extensions rebuilt for the new releases can fail to load on older servers. Extension packages in the project's RPM repositories now require the new minor release.
4. If PostgreSQL runs outside its package's own service unit, for example under Patroni, restart it right after updating, a maintainer of the RPM packages says in a
   [packaging blog post](https://people.planetpostgresql.org/devrim/index.php?/archives/138-PostgreSQL-November-2026-minor-releases-update-the-server-and-extensions-together.html)
   .
5. Update client tools such as pg\_dump, pg\_restore, reindexdb and vacuumdb on every machine that runs them.
6. Do not use the new composite\_type\_mismatch setting to turn off the checks. The project says doing so carries security risks.
7. The project's advisory and release notes offer no workaround for servers that cannot be updated yet.
8. PostgreSQL 14 is now end-of-life, and 14.25 is its last release. Older major versions are also affected and received no update.
9. After updating, follow the reindexing steps in the
   [release announcement](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)
   . If you use incremental backups, take a new full backup and base later incremental backups on it.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.