---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T03:01:46.286995+00:00'
exported_at: '2026-09-26T03:01:50.156204+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33268
structured_data:
  about: []
  author: ''
  description: 'Even MOAR Powershell, looking at Entra logins - the good, the bad
    and the password sprays, Author: Rob VandenBrink'
  headline: Even MOAR Powershell, looking at Entra logins - the good, the bad and
    the password sprays, (Fri, Aug 21st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33268
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Even MOAR Powershell, looking at Entra logins - the good, the bad and the password
  sprays, (Fri, Aug 21st)
updated_at: '2026-09-26T03:01:46.286995+00:00'
url_hash: 60ccb0cacb6d8d4c93736f3d3da002bfb7d428c2
---

One thing that folks never seem to do after "going to the CLOOOOUUUUD" is to look at their logs, logs that they would have checked daily when things were on premise.

One log that really bears looking at is the log of successful and failed logins.  the call for that is:

# import needed, if they're not already in place

Import-Module Microsoft.Graph.Reports

# connect with the correct scope

Connect-MgGraph -Scopes "AuditLog.Read.All", "Directory.Read.All"

$f = Get-MgAuditLogSignIn

Let's look at one object in the log:

![](https://isc.sans.edu/diaryimages/images/login%20fail%201.png)

This is an interactive login to OWA, which failed on a conditional access check

What is that under location though - that's likely why this failed.  How do we get the "where" from that?  And why does the status got a similar string in it instead of an actual status?

The command below shows us pulling only failed logins ("status/errorCode ne 0"), extracting the geo location info, and also the failure reason

Get-MgAuditLogSignIn -Filter "status/errorCode ne 0" -All | Select-Object `

CreatedDateTime,

UserPrincipalName,

IPAddress,

@{Name="City"; Expression={$\_.Location.City}},

@{Name="State"; Expression={$\_.Location.State}},

@{Name="Country"; Expression={$\_.Location.CountryOrRegion}},

@{Name="FailureReason"; Expression={$\_.Status.FailureReason}}

Aha!  Now we have that otherwise hidden information!  It's this sort of list where you'll see password sprays show up.  The list below shows part of such an attack, note that the last two lines show the account is locked.  The "IP address with malicious activity" alert generally means that this is a rotating proxy service, and the IP's in it have been fully or partially enumerated as "bad".

![](https://isc.sans.edu/diaryimages/images/failed%20login%202.png)

Or, looking for successful logins from unexpected countries, the command below.  Let's also remove the State / City info, normally it's just the country that matters, at least on the first pass through the data.

# set the array of "expected" Countries

$ExpectedCountries = @("CA", "US" )

#Get all successful logins

$f = Get-MgAuditLogSignIn -Filter "status/errorCode eq 0" -All | Select-Object `

CreatedDateTime,

UserPrincipalName,

UserDisplayName,

AppDisplayName,

ResourceDisplayName,

IsInteractive,

IPAddress,

@{Name="Country"; Expression={$\_.Location.CountryOrRegion}},

@{Name="FailureReason"; Expression={$\_.Status.FailureReason}}

# remove expected countries, and what is left is unexpected

# Just as Sherlock Holmes (or Occam) would say

$f | Where { $\_.Country -notin $ExpectedCountries } | out-gridview

![](https://isc.sans.edu/diaryimages/images/good%20logins%20from%20unexpected%20places.png)

It's interesting to see a few IPv6 addresses in the list.

In writing this diary, I found multiple password spray attacks.  This helped the client tighten up their conditional access policies, which was one of our goals going in.

Take a run at your Entra logs using the methods above.  Let us know in the comments if you found any unexpected (or expected) events or attacks, or if you were able to use your logs to effect a change in your configuration (in conditional access polices for instance)

===============

Rob VandenBrink

[[email protected]](/cdn-cgi/l/email-protection)