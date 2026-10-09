---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T03:01:47.694265+00:00'
exported_at: '2026-09-26T03:01:50.149466+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33264
structured_data:
  about: []
  author: ''
  description: 'Using Microsoft Graph and Powershell to Mine for Information - Stale
    Accounts and Licenses, Author: Rob VandenBrink'
  headline: Using Microsoft Graph and Powershell to Mine for Information - Stale Accounts
    and Licenses, (Thu, Aug 20th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33264
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Using Microsoft Graph and Powershell to Mine for Information - Stale Accounts
  and Licenses, (Thu, Aug 20th)
updated_at: '2026-09-26T03:01:47.694265+00:00'
url_hash: b34a5e308b80ef56a6145c88058cb8d2941c03fa
---

Microsoft Graph is a newer API that is meant to replace several others.  OK, it's at version 2.3.9, so it's not all that new, but it's new enough that lots of folks (and commercial tools) aren't using it yet.   It allows you to Get and Set info from/to M365, Entra Users and Entra managed machines for starters.  Let's dig in!

First, some preparation if you don't already have these modules installed:

Install-Module Microsoft.Graph -Repository PSGallery

# the beta likely isn't needed for most installs, but install it if desired

Install-Module Microsoft.Graph.Beta  -Repository PSGallery

Next, an import (again, if needed)



Import-Module Microsoft.Graph

Finally, you'll need to connect to your Entra account / directory



Connect-MgGraph -Scopes "User.Read.All

Let's start exploring just by dumping a user table:

$AllUsers = Get-MgUser -All -Property Id, DisplayName, UserPrincipalName, AccountEnabled, SignInActivity | Where-Object { $\_.AccountEnabled -eq $true }

Note the "-All" - this API has a default "first 100 objects" limit, if you are managing an actual domain you likely will always need a "-All" unless you are testing a script and want it to run faster.

If you want last password change included?  You'll need to ask for that in the initial get-mguser call, it's not in the default returned list of results:



Get-MgUser -All -Property DisplayName, UserPrincipalName, LastPasswordChangeDateTime | Select-Object DisplayName, UserPrincipalName, LastPasswordChangeDateTime

Cool, now you have a list of accounts and their last password change, that's worth a sort in Excel (or | Out-GridView) and a few emails.  Heck, since your in excel you could automate that right down to the email if you wanted.

What else?  Looking at $allusers | gm, we see a property called "assignedLicenses" - let's look at that:



Get-MgUser -UserId $u -Property AssignedLicenses | Select-Object -ExpandProperty AssignedLicenses

DisabledPlans SkuId

------------- -----

{}            05e9a617-0261-4cee-bb44-138d3ef5d965

{}            639dec6b-bb19-468b-871c-c5c441c4b0cb

{}            5b631642-bd26-49fe-bd20-1daaa972ef80

{}            a403ebcc-fae0-4ca2-8c8c-7a907fd6c235

{}            f30db892-07e9-47e9-837c-80727f46fd3d

hm, just the GUIDs (SkuId) for each license, that's not so useful.

For the real thing (that a human can read), we'll want a whole different command:



get-mguserlicensedetail -userid $u  | Select-Object SkuId, SkuPartNumber

SkuId                                SkuPartNumber

-----                                -------------

05e9a617-0261-4cee-bb44-138d3ef5d965 SPE\_E3

639dec6b-bb19-468b-871c-c5c441c4b0cb Microsoft\_365\_Copilot

5b631642-bd26-49fe-bd20-1daaa972ef80 POWERAPPS\_DEV

a403ebcc-fae0-4ca2-8c8c-7a907fd6c235 POWER\_BI\_STANDARD

f30db892-07e9-47e9-837c-80727f46fd3d FLOW\_FREE

So to add this to a regular one-liner without a powershell loop for each account, we'll need a
**join**
, we'll add this to our original get-mguser call (because if this is for a human to read, you don't want the SkuId normally):

@{N='License';E={(Get-MgUserLicenseDetail -All -UserId $\_.id).SkuPartNumber -join ';'}}

And to also, just for fun let's also pull the last interactive and non-interactive login dates:



@{N='LastInteractiveSignInDate';E={$\_.SignInActivity.LastSignInDateTime}}, `

@{N='LastNonInteractiveSignInDate';E={$\_.SignInActivity.LastNonInteractiveSignInDateTime}}

Also, let's pull the list of properties into a variable to make the call simpler (the computed statements are bolded):

$Properties = @('AccountEnabled','City','Country','Department','DisplayName','JobTitle','UserPrincipalName','CreatedDateTime','SignInActivity', 'LastPasswordChangeDateTime')

$Users = Get-MgUser -All -Property $Properties |

Select-Object @{N='AccountEnabled';E={$\_.AccountEnabled}}, `

@{N='City';E={$\_.City}}, `

@{N='Country';E={$\_.Country}},

@{N='Department';E={$\_.Department}},

@{N='DisplayName';E={$\_.DisplayName }}, `

@{N='JobTitle';E={$\_.JobTitle }}, `

@{N='UserPrincipalName';E={$\_.UserPrincipalName}}, `

@{N='CreatedDateTime';E={$\_.CreatedDateTime}}, `

**@{N='LastInteractiveSignInDate';E={$\_.SignInActivity.LastSignInDateTime}}, `

@{N='LastNonInteractiveSignInDate';E={$\_.SignInActivity.LastNonInteractiveSignInDateTime}},

@{N='License';E={(Get-MgUserLicenseDetail -UserId $\_.UserPrincipalName).SkuPartNumber -join '; '}}**

This can take a while - for each user, those last 3 lines add time.  The two "signindate" fields are an additional lookup, and the license detail line is a whole other command for each line.

So it's essentially another loop, but buried in standard syntax so you don't have to code a less efficient version ....

OK, so we have the last login dates so we can pick off inactive accounts, and license usage.  Also accounts that have been explicity disagbled (that firstr "AccountEnabled" field)  Dump the whole thing out to a CSV file with
**"| Out-CSV"**
, and you're an Excel sort away from a list of MS licenses you can stop paying for and a list of Entra accounts that you can likely disable or delete.  Or if you are philosphically opposed to spreadsheets or excel in particular, you can do the same with "
**| Out-GridView**
", except emailing your results can be a problem from there ...

![](https://isc.sans.edu/diaryimages/images/entra%20diary%201.png)

But what about a real security thing, something your SOC might alert on?  Stay tuned, that's next ...

===============

Rob VandenBrink

[[email protected]](/cdn-cgi/l/email-protection)