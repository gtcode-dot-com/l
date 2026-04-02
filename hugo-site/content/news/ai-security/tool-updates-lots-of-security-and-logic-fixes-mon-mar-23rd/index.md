---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T03:49:14.670916+00:00'
exported_at: '2026-04-02T03:49:17.719996+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32820
structured_data:
  about: []
  author: ''
  description: 'Tool updates: lots of security and logic fixes, Author: Jim Clausing'
  headline: 'Tool updates: lots of security and logic fixes, (Mon, Mar 23rd)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32820
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Tool updates: lots of security and logic fixes, (Mon, Mar 23rd)'
updated_at: '2026-04-02T03:49:14.670916+00:00'
url_hash: 5d0884b3d9fb57102b165fe96214bf76180cf035
---

So, I've been slow to get on the Claude Code/OpenCode/Codex/OpenClaw bandwagon, but I had some time last week so I asked Claude to review (
/security-review
) some of my python scripts. He found more than I'd like to admit, so I checked in a bunch of updates. In reviewing his suggestions, he was right, I made some stupid mistakes, some of which have been sitting in there for a long time. It was nothing earth-shattering and it took almost no time for Claude, it took longer for me to read through the updates he wanted to make, figure out what he was seeing, and decide whether to accept them or tweak them. Here are a few of them.

* a logic inversion error with the
  -f
  switch, and some unhandled errors in
  convert-ts-bash-history.py
* a TOCTOU (time of check/time of use) possible race condition, and a comment about some ambiguity with the
  -c
  switch when deciding which hash was used based solely on the length of the hash in
  sigs.py
* some overly permissive permissions, a possible symlink attack, and an encoding issue in
  ficheck.py
* a possible header injection issue via the
  -s
  switch with
  mail\_stuff.py

Most of these are issues I should have caught myself given how long I've been programming/scripting, but all of these started out as quick and dirty scripts to solve a problem I had, and then I made them available to the public through my github repo without taking any time to really ensure they were ready for public consumption. Taking a few minutes to setup Claude without much in the way of guidance (my CLAUDE.md is still very much a work-in-progress) and the one in my my scripts repo was one I asked Claude to create for me after some back and forth during this review which mostly covers a couple of personal preferences.

I guess the main point is I'm late to the game on using AI on a daily basis, but that needs to change. Even when I'm feeling my age and write my own scripts, I need to have that second pair of
*eyes*
give it a second look. Some of these scripts run as root out of cron or systemd timers on systems I administer and some of those issues could have been used for privilege escalation by an attacker who managed to get access. Even those of us with more grey than not in our beards need to be spending some time figuring out how to integrate this stuff into our daily routine.

**References**
:

[1]
<https://github.com/clausing/scripts>

---------------

Jim Clausing, GIAC GSE #26

jclausing --at-- isc [dot] sans (dot) edu