---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-04-07T23:53:56.098048+00:00'
exported_at: '2026-04-07T23:53:59.555914+00:00'
feed: https://www.bellingcat.com/feed/
language: en
source_url: https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf
structured_data:
  about: []
  author: ''
  description: Bellingcat is introducing an updated damage assessment tool — called
    the Iran Conflict Damage Proxy Map — focused on destruction in Iran and the Gulf
    .
  headline: 'When Satellite Imagery Goes Dark: New Tool Shows Damage in Iran and the
    Gulf'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'When Satellite Imagery Goes Dark: New Tool Shows Damage in Iran and the Gulf'
updated_at: '2026-04-07T23:53:56.098048+00:00'
url_hash: 3826ce7f7fbb3a3394623900acf81b5dcd02c44c
---

Access to open source visuals of the current Iran conflict, which has spread to many parts of the Middle East,
[continues to be sporadic](https://www.bloomberg.com/news/articles/2026-03-20/iran-war-internet-shutdown-limits-civilian-social-media-images?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc3NDAwNTA1MiwiZXhwIjoxNzc0NjA5ODUyLCJhcnRpY2xlSWQiOiJUQzZRMjRLSVAzSlQwMCIsImJjb25uZWN0SWQiOiI1MEU0OTBGQjhDNTM0MkREODAwRUEyNTQ1RjBCMThCOCJ9.wyxKGMZtga0S2Rgww9xGjYWTBB25bJi3MuhojVf5yWA&leadSource=uverify%20wall)
. Videos and photos from within Iran trickle out on social media as the
[Iranian internet blackout](https://bsky.app/profile/netblocks.org/post/3misqxvizzc2h)
hinders the flow of digital communication.

In past conflicts, satellite imagery has provided a vital overview of potential damage to both military and civilian infrastructure, especially when there are digital black spots or obstacles to on-the-ground reporting. But imagery from commercial providers is
[becoming](https://bsky.app/profile/eliothiggins.bsky.social/post/3miotfqqqqs2j)
[increasingly](https://bsky.app/profile/eliothiggins.bsky.social/post/3miotfqqqqs2j)
[restricted](https://www.reuters.com/business/aerospace-defense/satellite-firm-extends-middle-east-image-delay-prevent-use-by-us-adversaries-2026-03-10/)
, leaving even those who have access to the most expensive imagery in the dark.

Shortly after the war in Gaza began in 2023, Bellingcat
[introduced a free tool](https://www.bellingcat.com/resources/2023/11/15/a-new-tool-allows-researchers-to-track-damage-in-gaza/)
authored by University College London lecturer and Bellingcat contributor, Ollie Ballinger, that was able to estimate the number of damaged buildings in a given area. This helped monitor and map the scale of destruction across the territory as Israel’s military operation progressed.

Bellingcat is now introducing an updated version of the open source tool — called the Iran Conflict Damage Proxy Map — focused on destruction in Iran and the wider Gulf region.


It can be accessed
[here](https://bellingcat-ee.projects.earthengine.app/view/middle-east-change)
.

## How it Works

The tool works by conducting a statistical test on Synthetic Aperture Radar (SAR) imagery captured by the Sentinel-1 satellite which is part of the Copernicus mission developed and operated by the European Space Agency. SAR sends pulses of microwaves at the earth’s surface and uses their echo to capture textural information about what it detects.

The SAR data for the geographic area covered by the tool is put through the
[Pixel-Wise T-Test (PWTT)](https://www.sciencedirect.com/science/article/pii/S0034425725004298)
damage detection algorithm, which was also developed by Ollie Ballinger. It takes a reference period of one year’s worth of SAR imagery before the onset of the war and calculates a “normal” range within which 99% of the observations fall. It then conducts the same process for imagery in an inference period following the onset of the war, and compares it to the reference period. The core idea is that if a building has become damaged since the beginning of the war, then the “echo” (called backscatter) from that pixel will be consistently outside of the normal range of values for that particular area. Investigators can then further probe potential damage around this highlighted area.

The plot below shows how the process was applied to Gaza and several Syrian, Iraqi and Ukrainian cities. The bars represent the weekly total number of clashes in each place, sourced from the Armed Conflict Location Event (ACLED) dataset. The pre-war reference periods are shaded in blue, spanning one year before the onset of each conflict. The one month inference periods after the respective conflicts  began are shaded in orange. The blue and orange areas are what the tool compares.

The plot below shows an area with a number of warehouses in Tehran’s southwest. Some of the buildings show clear damage in optical Sentinel-2 imagery (something that has to be
[accessed outside](https://browser.dataspace.copernicus.eu/)
of the tool via the Copernicus Browser).

Clicking on the map within the
[tool](https://bellingcat-ee.projects.earthengine.app/view/middle-east-change)
generates a chart displaying that pixel’s historical backscatter; the red dotted lines denote a range within which 99% of the pre-war backscatter values fall. In this example, we can see that from March 14 onwards, the backscatter values over this warehouse begin to consistently fall outside of their historical normal range. This could signal that damage has been detected in the area.

Two important aspects of this workflow are that it utilises free and fully open access satellite data, as opposed to commercial satellite services; the second is that it overcomes some key limitations of AI in this domain, the most serious of which is called overfitting. This is where a model trained in one area is deployed in a new unseen area, and fails to generalise. Because we’re only ever comparing each pixel against its own historical baseline, we don’t run into that problem.

## Accuracy

The PWTT has been
[published in a scientific journal](https://www.sciencedirect.com/science/article/pii/S0034425725004298)
after two years of review.  Its accuracy was  assessed using an original dataset of over two million building footprints labeled by the United Nations, spanning 30 cities across Gaza, Ukraine, Sudan, Syria, and Iraq. Despite being simple and lightweight, the algorithm has been recorded achieving building-level accuracy statistics (AUC=0.87 in the full sample) rivaling state of the art
[methods](https://link.springer.com/article/10.1007/s13753-023-00526-6?utm_source=getftr&utm_medium=getftr&utm_campaign=getftr_pilot&getft_integrator=sciencedirect_contenthosting)
that use deep learning and high resolution imagery. The plot below compares building-level predictions from the PWTT against the UN damage annotations in Hostomel, Ukraine. True positives (PWTT and United Nations agree on damage) are shown in red, true negatives are shown in green, false positives in orange, and false negatives in purple. The graphic shows the accuracy of the tool, while also emphasising that further checks on what it highlights should be conducted to draw full conclusions.

It is important to note that just because the tool may show a high probability of a building or buildings being damaged or destroyed, that doesn’t make it definite.

It is best to check with any other available imagery — either open source photos and videos that’ve been geolocated by a group such as
[Geoconfirmed](https://geoconfirmed.org/iran)
or Sentinel-2 as well as other commercial satellite imagery if it’s up-to-date for the area. At time of publication, Sentinel-2 satellite imagery still offers coverage over the area that the tool focuses on. Other commercial satellite imagery providers have
[limited their coverage.](https://www.aljazeera.com/news/2026/4/5/us-satellite-firm-planet-labs-announces-blackout-on-war-on-iran-images)

What the tool excels at is highlighting and narrowing down areas so that further corroboration or further confirmation can be sought.

## Testing the Tool

Using the Iran Conflict Damage Proxy Map, we can spot some of the larger areas of potential damage or destruction that have occurred since the Iran war started.


Starting from a zoomed-out view of Tehran, there are a few spots that appear with large clusters of high damage probability. Cross-referencing these locations with open source map data from platforms like
[OpenStreetMap](https://www.openstreetmap.org/#map=12/35.6983/51.4078)
or
[Wikimapia](https://wikimapia.org/#lang=en&lat=35.670000&lon=51.430000)
, we can start finding sites that would make for likely targets – such as military sites.


One example of a potentially damaged site visible in the tool is the Valiasr Barracks in central Tehran, which
[was struck in the first week](https://www.reutersconnect.com/item/a-satellite-image-shows-the-valiasr-barracks-at-sepah-square-in-tehran/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX1JDMkxYSkFNSUUwSw)
of the war. By going to the Copernicus Browser and reviewing the area with optical Sentinel-2 imagery, we can see clear indications of damage at the barracks.

**IRGC Valiasr Barracks in Tehran:**

Below: Sentinel-2 comparison of February 20 and March 17.

A large Islamic Revolutionary Guard Corps (IRGC) compound near Isfahan is another example of military infrastructure that is readily visible in both the Iran Conflict Damage Proxy Map as well as Sentinel-2 imagery.

**IRGC Ashura Garrison in Isfahan:**

Below: Sentinel-2 comparison of February 20 and March 17.

Air bases have also been
[a frequent target](https://www.youtube.com/shorts/iOj8Vssogi0)
for U.S.-Israeli strikes in Iran. The Fath Air Base just outside of Tehran, near the city of Karaj, shows the signature of potential damage when using the tool. Checking Sentinel-2 imagery shows damage to multiple large buildings on the northern side of the base.

**Fath Air Base in Karaj:**

Below: Sentinel-2 comparison of February 20 and March 17.

The
[U.S. has stated](https://www.war.gov/News/News-Stories/Article/Article/4434312/hegseth-says-irans-defense-industrial-base-nearing-complete-destruction/)
that destroying Iran’s “defense industrial base” is also a goal, which makes large areas like the
[Khojir missile production complex](https://www.reuters.com/world/middle-east/satellite-photos-show-iran-expanding-missile-production-sources-say-2024-07-08/)
east of Tehran a good location to search with this tool. The tool suggests large clusters of damage on both the eastern and western sides of the complex — near areas where
[solid propellant is reportedly produced](https://x.com/sam_lair/status/2029980877577670782)
and where
[other fuel components are reportedly made](https://x.com/sam_lair/status/2028990704043868457)
.

**Khojir Missile Production Complex outside of Tehran:**

Below: Sentinel-2 comparison of February 20 and March 17.

## Usage in the Gulf Region

While useful for providing a sense of damaged areas in Iran, the Iran Conflict Damage Proxy Map can also be used to see damage outside
of Iran, particularly at sites in the region which Iran has been targeting with drones and missiles.


In the below example at Al Udeid Air Base in Qatar, which hosts U.S. Central Command’s
[Combined Air Operations Center](https://www.afcent.af.mil/About/Fact-Sheets/Display/Article/217803/combined-air-operations-center-caoc/)
, there is a notable indication of damage over a warehouse-like building at
[25.115647, 51.333125](https://www.google.com/maps/place/25%C2%B006'56.3%22N+51%C2%B019'59.3%22E/@25.1156484,51.3324818,345m/data=!3m2!1e3!4b1!4m4!3m3!8m2!3d25.1156472!4d51.3331255?entry=ttu&g_ep=EgoyMDI2MDMzMC4wIKXMDSoASAFQAw%3D%3D)
. Checking the same location in Sentinel-2 imagery shows that there does appear to be damage at that warehouse — represented by a large blackened area on the white roof.
[According to Qatar’s Ministry of Defense](https://x.com/MOD_Qatar/status/2028945288782635139)
, at least one Iranian ballistic missile struck the base in early March.

**Al Udeid Air Base in Qatar:**

Below: Sentinel-2 comparison of February 22 and March 14.

Civilian sites struck by Iranian drones or missiles are also visible in the tool — though the damage has to be fairly large in order to be picked up. Something like damage to the
[sides of high rise buildings](https://x.com/zarGEOINT/status/2031869962487214548)
from an Iranian drone attack doesn’t readily appear in the tool. Sites that
*do*
appear are places like oil refineries, such as
[a fuel tank at Fujairah port](https://www.bellingcat.com/news/2026/04/02/war-uae-iran-infuencer-dubai-conflict-drone-successful-strike-intercept-fire/)
in the United Arab Emirates.

**Fuel tanks at Fujairah Port, UAE:**

Below: Sentinel-2 comparison of March 3 and March 28.

## Accessing the Tool

It’s important to keep in mind that the data for the Iran Conflict Damage Proxy Map is updated approximately one or two times per week as new satellite data is collected by the Sentinel-1 satellite, so it’s not meant to be a representation of real-time damage to buildings.

Still, it can be useful for researchers to quickly gain an overview of damage throughout Iran and the Gulf where suspected strikes may have taken place and when there is no other open source information available.

You can access the Iran Conflict Damage Proxy Map
[here](https://bellingcat-ee.projects.earthengine.app/view/middle-east-change)
.


Similar tools using the same methodology to assess damage in Ukraine following Russia’s full-scale invasion and Turkey following the 2023 earthquake can be found
[here](https://oballinger.github.io/PWTT/)
. The Gaza Damage Proxy Map can be found
[here](https://ee-ollielballinger.projects.earthengine.app/view/gazadamage)
.

---

*Bellingcat’s Logan Williams contributed to this report.*

*This article was updated on April 7, 2026, to note that Sentinel-1 and Sentinel-2 are part of the Copernicus mission developed and operated by the European Space Agency.*

*Bellingcat is a non-profit and the ability to carry out our work is dependent on the kind support of individual donors. If you would like to support our work, you can do so*
[*here*](https://www.bellingcat.com/donate/)
*. You can also subscribe to our Patreon channel*
[*here*](https://www.patreon.com/bellingcat)
*. Subscribe to our*
[*Newsletter*](https://bellingcat.us14.list-manage.com/subscribe/post?u=c435f53a5568f7951404c8a38&id=4be345b082)
*and follow us on Bluesky*
[*here*](https://bsky.app/profile/bellingcat.com)
*, Instagram*
[*here*](https://www.instagram.com/bellingcatofficial/)
*, Reddit*
[*here*](https://www.reddit.com/r/bellingcat/)
*and YouTube*
[*here*](https://www.youtube.com/@bellingcatofficial/videos)
*.*