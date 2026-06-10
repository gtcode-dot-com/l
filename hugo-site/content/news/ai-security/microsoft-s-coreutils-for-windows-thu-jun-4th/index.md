---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T22:15:16.386033+00:00'
exported_at: '2026-06-10T22:15:20.193422+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33048
structured_data:
  about: []
  author: ''
  description: 'Microsoft''s Coreutils for Windows, Author: Didier Stevens'
  headline: Microsoft's Coreutils for Windows, (Thu, Jun 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33048
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft's Coreutils for Windows, (Thu, Jun 4th)
updated_at: '2026-06-10T22:15:16.386033+00:00'
url_hash: a34210168419a19b79a03ea972cb4dfff768303f
---

I've been using the GnuWin32 CoreUtils for Windows for many years now (it gives you many \*nix core commands on Windows).

Microsoft has just
[released](https://github.com/microsoft/coreutils)
their coreutils version for Windows.

You can install them with a winget command (winget install Microsoft.Coreutils) or with the
[installer released on GitHub](https://github.com/microsoft/coreutils/releases)
.

It takes just a few clicks:

![](https://isc.sans.edu/diaryimages/images/20260604-074226.png)

![](https://isc.sans.edu/diaryimages/images/20260604-074240.png)

![](https://isc.sans.edu/diaryimages/images/20260604-074312.png)

It installs a single executable compiled with Rust (coreutils.exe) in the program files folder:

![](https://isc.sans.edu/diaryimages/images/20260604-074636.png)

And each individual command is a hard link to this executable:

![](https://isc.sans.edu/diaryimages/images/20260604-074703.png)

Here is the full list of commands:

```
arch.cmd
b2sum.cmd
base32.cmd
base64.cmd
basename.cmd
basenc.cmd
cat.cmd
cksum.cmd
comm.cmd
cp.cmd
csplit.cmd
cut.cmd
date.cmd
df.cmd
dirname.cmd
du.cmd
echo.cmd
env.cmd
expr.cmd
factor.cmd
false.cmd
find.cmd
fmt.cmd
fold.cmd
grep.cmd
head.cmd
hostname.cmd
join.cmd
link.cmd
ln.cmd
ls.cmd
md5sum.cmd
mkdir.cmd
mktemp.cmd
mv.cmd
nl.cmd
nproc.cmd
numfmt.cmd
od.cmd
pathchk.cmd
pr.cmd
printenv.cmd
printf.cmd
ptx.cmd
pwd.cmd
readlink.cmd
realpath.cmd
rm.cmd
rmdir.cmd
seq.cmd
sha1sum.cmd
sha224sum.cmd
sha256sum.cmd
sha384sum.cmd
sha512sum.cmd
shuf.cmd
sleep.cmd
sort.cmd
split.cmd
stat.cmd
sum.cmd
tac.cmd
tail.cmd
tee.cmd
test.cmd
touch.cmd
tr.cmd
true.cmd
truncate.cmd
tsort.cmd
unexpand.cmd
uniq.cmd
unlink.cmd
uptime.cmd
wc.cmd
xargs.cmd
yes.cmd
```

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)