---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-22T04:26:07.162601+00:00'
exported_at: '2026-09-22T04:26:08.977125+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33272
structured_data:
  about: []
  author: ''
  description: 'Who Got Missed in the MFA Rollout? More Powershell + Graph + Entra
    scripting!, Author: Rob VandenBrink'
  headline: Who Got Missed in the MFA Rollout&#x3f; More Powershell &#x2b; Graph &#x2b;
    Entra scripting&#x21;, (Fri, Aug 21st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33272
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Who Got Missed in the MFA Rollout&#x3f; More Powershell &#x2b; Graph &#x2b;
  Entra scripting&#x21;, (Fri, Aug 21st)
updated_at: '2026-09-22T04:26:07.162601+00:00'
url_hash: 71733a0355c0ddf750eece7cbc44c3a6d371720c
---

In every MFA rollout, there will come a time where you think you are closing in on "done", and some automation to list what's left would be handy.  Something quicker than scrolling through the web interface through thousands of accounts ...

This is that method.

Also, remember when we discussed yesterday about the beta graph commands in the
Microsoft.Graph.Beta
library?  We'll use one of those beta commands here!

# import, if it's not already there

Import-Module -Name Microsoft.Graph.Beta.Reports

# with the necessary auditing scope

Connect-MgGraph -Scopes "AuditLog.Read.All", "User.Read.All"

$AllMFADetails = Get-MgBetaReportAuthenticationMethodUserRegistrationDetail -All

# We're only interested in users who are NOT yet registered for MFA

$NonMFAUsers = $AllMFAdetails | Where-Object { $\_.IsMfaRegistered -eq $false }

$t = foreach ($User in $NonMFAUsers) {

# user by user, collect account details (primary if it's enabled)

# then construct the userobj record

# note the join adds the object to the list

$UserObj = Get-MgUser -UserId $User.Id -Select Id, AccountEnabled

[PSCustomObject]@{

"UserPrincipalName"   = $User.UserPrincipalName

"DisplayName"         = $User.UserDisplayName

"AccountEnabled"      = $UserObj.AccountEnabled

"MethodsRegistered"   = ($User.UserPreferredMethodForSignIn -join ", ")

}

}

$t | Out-GridView -Title "NON-MFA Users"

Note that the last two columns are for MFA methods, so they'll be blank, but we'll use those in a sec.

I'm not displaying the output in this case, as it's essentially a list of actual user accounts.

You can also modify this a bit, for instance if you were tightening up your MFA setup, because your auditor told you to root out folks using SMS for MFA for instance, this is definitely the command set to use.  You'd want
$\_.IsMfaRegistered -eq $true
, but then look for "SMS" in the Methods registered or Default MFA columns.  Surprisingly in this last check I saw a number of folks with "voiceMobile" (ie a voice callback) as their primary MFA.

Give this a try, let us know in the comments if you find some unexpected folks who skated by the MFA login policy requirements ....

===============

Rob VandenBrink

[[email protected]](/cdn-cgi/l/email-protection)