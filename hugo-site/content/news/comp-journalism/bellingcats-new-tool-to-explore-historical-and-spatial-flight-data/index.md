---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-03-06T22:15:48.503336+00:00'
exported_at: '2026-03-06T22:15:54.307142+00:00'
feed: https://www.bellingcat.com/feed/
language: en
source_url: https://www.bellingcat.com/resources/2026/03/05/turnstone-flight-tracking-tool
structured_data:
  about: []
  author: ''
  description: Turnstone can visualise historical trends in flight data or filter
    them by geography, aircraft type and other parameters.
  headline: Using Bellingcat’s New Open Source Tool to Explore Historical and Spatial
    Flight Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.bellingcat.com/resources/2026/03/05/turnstone-flight-tracking-tool
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Using Bellingcat’s New Open Source Tool to Explore Historical and Spatial Flight
  Data
updated_at: '2026-03-06T22:15:48.503336+00:00'
url_hash: 205087a1f9cdce4ef7e29b63e8868b02ee643755
---

Flight tracking data is
[an important tool](https://www.bellingcat.com/resources/how-tos/2019/10/15/a-beginners-guide-to-flight-tracking/)
in open source research, but with
[100,000 daily flights](https://easbcn.com/en/how-many-planes-fly-per-day-around-the-world/)
, it can be difficult to contextualise what a particular aircraft’s movements indicate.

Bellingcat has developed a tool called Turnstone to make it easier to visualise historical trends in flight data and spot unusual patterns. It also allows users to filter by parameters such as aircraft type or a geographic region of interest.

*Source: ZUMA Press Wire via Reuters Connect; overlays of Turnstone by Bellingcat*

This tool primarily uses Automatic Dependent Surveillance–Broadcast (ADS-B) data, the technology that enables open source investigators and enthusiasts to track flights.

Most aircraft are equipped with transmitters that broadcast ADS-B data to comply with global aviation regulations, though regulations
[vary by jurisdiction](https://www.aopa.org/go-fly/aircraft-and-ownership/ads-b/where-is-ads-b-out-required)
, and military aircraft
[might not always transmit](https://nbaa.org/aircraft-operations/communications-navigation-surveillance-cns/ads-b/faa-permits-ads-b-off-military-sensitive-flights/)
. ADS-B data includes information about an aircraft’s identity and type, as well as its precise position, speed and altitude.

Popular flight-tracking websites such as
[Flightradar24](https://www.flightradar24.com/)
and
[ADS-B Exchange](https://globe.adsbexchange.com/)
typically display historical data for a particular time or aircraft. However, Turnstone aggregates ADS-B data for multiple aircraft over time, and allows users to search for flights across two areas of interest at once. These features provide additional context for open source investigators to better understand flight behaviour.

*Watch the video for a demonstration of how the tool works, using the example of*
[*Black Hawk helicopter patrols*](https://www.cbc.ca/news/canada/british-columbia/black-hawk-patrols-1.7454474)
*near one of the borders between the US and Canada:*

VIDEO

You can view Turnstone’s source code and information about hosting it yourself on Bellingcat’s
[GitHub](https://github.com/bellingcat/adsb-history)
.

We also have a web-based instance of the tool that journalists and academics can access. Due to data hosting and processing costs, we can only grant access on a selective basis. If you would like to apply, please fill in
[this form](https://docs.google.com/forms/d/e/1FAIpQLSct-l5hl7OiLJ65bIaAYub5uGrDziHFnry6wxVshSP8r2e_JA/viewform?usp=preview)
. Priority will be given to researchers conducting open source investigations
[aligned with Bellingcat’s goals](https://www.bellingcat.com/about/who-we-are/)
.

Read on for more examples of how Turnstone can be used for investigations, as well as some limitations of the tool.

## Spotting Unusually High US Tanker Activity Before Iran Strikes

The US and Israel launched
[joint air strikes](https://www.cbsnews.com/live-updates/iran-war-us-israel-day-4-trump-gives-no-timeline-as-gulf-states-attacked/)
across Iran on Feb. 28, 2026,
[reportedly](https://www.aljazeera.com/news/2026/3/4/death-toll-in-iran-surpasses-1000-as-israel-us-strikes-continue)
killing
[more than 1,000 people](https://www.cbc.ca/news/world/tracking-deaths-iran-israel-united-states-middle-east-9.7114340)
, including
[members of the Iranian leadership](https://edition.cnn.com/2026/02/28/middleeast/maps-iran-tehran-attack-vis-intl)
, in five days.

This marked a dramatic escalation since the US and Israel
[bombed three Iranian nuclear sites](https://news.un.org/en/story/2025/06/1164741)
in June 2025.

Flight data before both the
[June 2025](https://www.airnavradar.com/blog/massive-us-tanker-deployment-spotted-over-atlantic-likely-supporting-middle-east-troop-movement)
and
[February 2026](https://x.com/vcdgf555/status/2027421469421310432)
strikes showed a large number of American
[aerial tankers](https://simpleflying.com/top-tanker-aircraft-list/)
leaving the US and crossing the Atlantic towards Iran. Aerial tankers such as the
[KC-135](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/1529736/kc-135-stratotanker/)
and
[KC-46A](https://www.boeing.com/defense/tankers-and-transports/kc-46-pegasus)
can refuel military aircraft in-flight, making them
[essential](https://simpleflying.com/roles-kc-135-stratotanker-us-military-missions/)
for most long-range combat missions.



With Turnstone, it is possible to interrogate the baseline level of movement and see how unusual this activity is.

To do this, three filters are set on the search: a geographic region of interest, set to the North Atlantic, a filter on the aircraft type, to search only for tankers, and a filter on the aircraft heading, to search only for eastbound traffic.

**Filtering a search by aircraft type, region of interest, and heading range that captures eastbound traffic. Source: Turnstone/Bellingcat**

[Note: For the aircraft category designations,
[Bellingcat used](https://github.com/bellingcat/adsb-history?tab=readme-ov-file#augmenting-tar1090-db)
a custom-prompted large language model (LLM),
[Claude Sonnet 4.0](https://www.anthropic.com/news/claude-4)
, to assign a category label using aircraft type code data. There may be some inaccuracies in the classifications, as LLMs are prone to hallucinations. We discuss this further in the “Limitations of the Data” section of this piece.]

This search finds over 40,000 aircraft locations that match these filter queries. However, a look at the summary table shows that this data includes non-American tankers as well.

*Results from a filtered search, showing tankers owned by the French Air Force and the United States Air Force. Source: Turnstone/Bellingcat*

We can filter this data to include only aircraft associated with the US by typing “United States” into the search box in the table. Note that ownership data is not 100 percent accurate – it may be out of date, especially for privately owned aircraft, and new aircraft might not have any data at all. However, especially when comparing trends over time or searching for research leads, this data can still be useful.

The graph of matching detections over time now shows that while there is a large baseline level of transatlantic movement for American tankers, there was a notably higher number of American tankers heading eastward from the US across the North Atlantic detected in the week of June 15, 2025, as well as in the last two weeks of February 2026.

**The weekly graph view on Turnstone shows a noticeable spike in eastbound American tankers crossing the North Atlantic per day from June 15 to June 21, 2025 and from Feb. 15 to Feb. 28, 2026. Source: Turnstone/Bellingcat**

A week after the increased eastbound traffic in June 2025, early in the morning on June 22, the
[US struck](https://www.npr.org/2025/06/21/nx-s1-5441127/iran-us-strike-nuclear-trump)
several nuclear sites in Iran. And on Feb. 28, 2026, the
[US and Israel launched over 900 strikes against Iran](https://understandingwar.org/research/middle-east/iran-update-evening-special-report-february-28-2026/)
.

Altering the search query to look for westbound tankers instead of eastbound tankers, we can also see a larger-than-normal number of American tankers heading in the direction of the US during the week of July 13, 2025, bookending the summer airstrikes in Iran. No such return movement is yet visible following the recent strikes.

*The number of American tankers heading westward across the North Atlantic, towards the US, appeared higher than usual from July 13 to July 19, 2025. Source: Turnstone/Bellingcat*

## Finding Deportation Flights to Guantanamo Bay

Turnstone also allows you to search for aircraft detected across two different geographic regions of interest (ROIs).

Shortly after US President Donald Trump
[announced](https://www.theguardian.com/us-news/2025/jan/29/trump-guantanamo-detention-center)
the opening of a migrant detention centre at Guantanamo Bay in Cuba at the end of January 2025, the US military reportedly flew about 100 immigrants from El Paso, Texas,
[to the US naval base](https://www.texastribune.org/2025/02/13/immigration-flights-elpaso-guantanamo/)
to await deportation. By selecting the areas around both Guantanamo Bay and El Paso, we can find flights between these cities that broadcast ADS-B data.

*When you select two regions of interest, a filter for the time difference between them also appears. Source: Turnstone/Bellingcat*

When two ROIs are selected, you can also enter the maximum time difference between an aircraft’s presence in the two regions.

In the example below, we have entered 36,000 seconds (10 hours), meaning that the aircraft must have crossed through both regions within 10 hours of each other. We have also set the maximum altitude to 15,000 ft (4.57km) to look for planes landing and taking off. This limit is set relatively high as there are no ADS-B receivers at Guantanamo Bay, and only the initial approach is captured.

*Search panel settings for finding aircraft that have been in both Guantanamo Bay and El Paso, Texas, with inputs under the “Maximum Altitude” and “Maximum Time Difference” fields, and selection areas drawn around both areas on the map (in blue). Source: Turnstone/Bellingcat*

After five months with no tracked flights between the two locations, this search shows an uptick in flights in the few months from February 2025.

*The results from Turnstone come with a bar graph that shows the average aircraft per day by week or by month, which can be further filtered by aircraft hex code (the unique identifier for specific aircraft) or the*
[*aircraft type code*](https://www.avcodes.co.uk/acrtypes.asp)
*. Source: Turnstone/Bellingcat*

Results for this search query from Jan. 26, 2026, include several passenger aircraft operated by companies
[known to run deportation flights](https://www.opensecrets.org/news/2025/05/which-air-carriers-are-positioned-to-benefit-from-increased-deportations/)
from the US, such as Omni Air International and Global Crossing Airlines.

*Results from a search of flights of up to 10 hours between Guantanamo Bay and El Paso, Texas, conducted on Jan. 26, 2026 show flights owned by Omni Air International and Global Crossing Airlines, both carriers*
[*known to operate*](https://www.opensecrets.org/news/2025/05/which-air-carriers-are-positioned-to-benefit-from-increased-deportations/)
*deportation flights. Source: Turnstone/Bellingcat*

## Mapping US Customs and Border Patrol Aircraft

Turnstone also supports uploading a list of International Civil Aviation Organization (ICAO) addresses, informally referred to as aircraft “hex codes”, which are unique identifiers assigned to aircraft by ICAO member states.

For example, to explore data related to Department of Homeland Security (DHS) activity and look for patterns related to the
[US immigration enforcement and border security operations](https://www.bellingcat.com/news/2025/07/08/masked-armed-and-forceful-finding-patterns-in-los-angeles-immigration-raids/)
, we can copy and paste the hex codes from a
[list of US Customs and Border Patrol (CBP) aircraft](https://wiki.radioreference.com/index.php/CBP_Office_of_Air_and_Marine)
(used across the DHS) into a text file, and upload that file. Now, we can search among these aircraft with any of the same filters demonstrated in the earlier case studies. Alternatively, we can also deselect all of the filters to track the most recent activity by those aircraft.

Let’s try that with the CBP list, this time with a very large number of results selected: 500,000. Note that increasing the number of results increases the search time and requires more browser memory.

*With the list of hex codes provided, the search interface shows “216 hex codes loaded”. No other filters have been selected and the result limit is set to 500,000. Source: Turnstone/Bellingcat*

When many points are displayed, the map is simplified, and hover features are disabled.

*The results map shows a large number of CBP flights over the US without any filters, from a search of historical data on Jan. 26, 2026. Source: Turnstone/Bellingcat*

By the California-Mexico border, Eurocopter AS350 (type “AS50”) can be seen on frequent patrol missions over the land border. Over the Pacific Ocean, Black Hawk helicopters (“H60”) can be seen patrolling the international waters boundary off the Mexican coast, while CBP Dash-8s (“DH8B” and “DH8C”) travel farther offshore.

*Zooming in on the area near the California-Mexico border shows an obvious concentration of certain aircraft types in this search of historical data on Jan. 26. 2026. Source: Turnstone/Bellingcat*

In contrast, by the Minnesota-Canada border, CBP makes more active use of one of its MQ-9 Reaper drones, as seen from the prevalence of red dots that correspond to “Q9”, the type code of these drones, in the results map.

*The dots around the Minnesota-Canada border mainly show activity by MQ-9 Reaper drones in this search of historical data on Jan. 26, 2026. Source: Turnstone/Bellingcat*

Let’s take a closer look at these drones by filtering the results with the text “Q9”. Now the displayed aircraft only include MQ-9 Reaper drones.

*Results can be filtered by typing into the search field on the top right of the “Aircraft Summary” table. Source: Turnstone/Bellingcat*

Now we can take a closer look at the patterns of drones, specifically among the search results.

*Left: A very large number of MQ-9 Reaper flights south of San Angelo, Texas. They are coloured by altitude, with green symbols indicating lower flights and red showing those at higher altitudes. Right: The flight pattern of a known Aug. 13, 2025 MQ-9 Reaper*
[*mission into Mexico*](https://www.twz.com/air/u-s-mq-9-drone-just-flew-a-mission-deep-into-mexico)
*, as shown on Turnstone. Source: Turnstone/Bellingcat*

While overall CBP flight activity was relatively stable, drone flights seem to have intensified in December 2025 and January 2026, compared with previous weeks.

*The bar graph by week shows a higher average number of MQ-9 Reaper drone flights in December 2025 and January 2026 than in previous weeks. Source: Turnstone/Bellingcat*

## Limitations of the Data

In open source research, it is always important to be alert to the limitations of a particular data source, and ADS-B data is no exception.

For example, some aircraft
[do not have ADS-B transponders](https://www.flightradar24.com/blog/inside-flightradar24/how-we-track-flights-with-mlat/)
and use older transponders to transmit flight information, which can result in tracking tools such as Turnstone showing inaccurate position data.

In the previous case study of CBP aircraft, the Turnstone results appeared to show an MQ-9 Reaper drone in Canada on Jan. 20, 2026.

*Search results for CBP MQ-9 Reaper drones on Jan. 20, 2026, which appeared to show four instances (circled) of a drone in Canadian airspace. Source: Turnstone/Bellingcat*

Is this evidence of covert DHS missions in Canadian airspace? Likely not: a cross-check of the drone’s hex code on that date
[with ADS-B Exchange](https://globe.adsbexchange.com/?icao=ae4dde&lat=49.034&lon=-97.567&zoom=8.3&showTrace=2026-01-20)
shows that the aircraft’s position track is not smooth, but jumps back and forth between a line in the US and several points many kilometres away in Canada.

*Screenshot from flight tracking website ADS-B Exchange, appearing to show a CBP drone flying within US airspace but jumping suddenly to the circled points in Canada, several kilometres away. Source: ADS-B Exchange; annotations by Bellingcat*

This happens because when ADS-B position data is not available, flight trackers often use
[multilateration (MLAT)](https://www.flightradar24.com/blog/inside-flightradar24/how-we-track-flights-with-mlat/)
, which estimates the location of the aircraft using the time differences between signals transmitted from known sites, as a substitute. The flight tracking information
[on ADS-B Exchange](https://globe.adsbexchange.com/?icao=ae4dde&lat=49.034&lon=-97.567&zoom=8.3&showTrace=2026-01-20&trackLabels)
shows that the position was calculated using MLAT, which is less accurate than position data directly transmitted through ADS-B.
[ADSB.lol](https://github.com/adsblol)
, which is the data source used by Turnstone, uses MLAT when ADS-B position data is not available.

ADS-B data is also limited by where ground antennas are available to receive radio signals from aircraft and by when aircraft choose to transmit the data.

Other datasets which Bellingcat has used to enable the filters available on Turnstone each have their own limitations.

There is no single source of data on aircraft ownership. ADS-B data identifies an aircraft only using its ICAO address or hex codes, but does not contain other information that directly specifies the type of aircraft or its registration.

Instead, flight-tracking websites reference aircraft registration databases, such as those
[maintained by the US Federal Aviation Administration](https://registry.faa.gov/aircraftinquiry/search/nnumberinquiry)
, to correlate ICAO addresses with registration information. The ownership data displayed on Turnstone is from
[tar1090-db](https://github.com/wiedehopf/tar1090)
, a community-maintained project which has produced the most comprehensive freely available global aircraft registration database. However, since ownership data is collected from many jurisdictions, with different privacy and disclosure requirements, it may sometimes be out-of-date or misleading.

Ownership information displayed in Turnstone or any other flight-tracking software should still be verified independently using multiple sources.

For example, one of the aircraft that came up in the search for flights between El Paso and Guantanamo Bay had a hex code of a6b0f5. This showed up in Turnstone’s results as being owned by Bank of Utah Trustee, which matches the operator listed for this flight on
[ADS-B Exchange](https://globe.adsbexchange.com/?icao=a6b0f5)
. But some of the flight codes used by this aircraft, starting with “GXA”, are
[used by Global Crossing Airlines](https://www.iata.org/en/about/members/airline-list/globalx/585/)
(GlobalX). The Bank of Utah is
[known to](https://www.bankofutah.com/corporate/trust/aircraft-owner-trust-frequently-asked-questions)
legally own aircraft under a trust relationship, while
[leasing the aircraft](https://www.hef.ru.nl/~pfk/aircraft/operator-BankOfUtah.php)
and operational control to third parties such as GlobalX.

*Screenshot from Turnstone showing aircraft flying between Guantanamo Bay and El Paso, from a historical flight data search on Jan. 26, 2026.*

The “Category” label and “Military” flag, which provide a convenient way to filter aircraft, are pre-generated by a custom-prompted large language model,
[Claude Sonnet 4.0](https://www.anthropic.com/news/claude-4)
, based on the make and model of an aircraft.

For example, the LLM may take a type code of A321, which refers to an Airbus A321 passenger jet, as input and assign the corresponding aircraft the category of “airliner”.

Bellingcat manually verified over 80 per cent of aircraft, corresponding to the most common aircraft types. But as we know, LLMs are
[prone to hallucinations](https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/)
, and categorisation may be inaccurate for more obscure aircraft. Additionally, some aircraft, such as the
[V-22 Osprey](https://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey)
, fall between categories and are inherently ambiguous.

To prevent errors caused by the potential miscategorisation of aircraft, you may want to search by type code, which will draw from the raw tar1090-db data, rather than category. All aircraft registration, type, and owner information should be independently verified.

## Suggestions and Further Information

As we’ve seen in this guide, Turnstone searches historical ADS-B data to allow researchers to explore flight patterns over time and in specific locations. While flight-tracking data has inherent limitations, Turnstone can provide useful leads for researchers looking to incorporate flight tracking in their investigations.

If you have suggestions for improving the tool, you can
[submit a pull request](https://github.com/bellingcat/adsb-history?tab=contributing-ov-file#submitting-a-pull-request-bulb)
on Bellingcat’s GitHub. More technical information can also be found in the tool’s
[README](https://github.com/bellingcat/adsb-history)
.

*For more demos and information about the history of this tool, watch a talk that Bellingcat gave about it at the What Hackers Yearn (WHY) 2025 hacker camp:*

VIDEO



---

*Bellingcat is a non-profit and the ability to carry out our work is dependent on the kind support of individual donors. If you would like to support our work, you can do so*
[*here*](https://www.bellingcat.com/donate/)
*. You can also subscribe to our Patreon channel*
[*here*](https://www.patreon.com/bellingcat)
*. Subscribe to our*
[*Newsletter*](https://bellingcat.us14.list-manage.com/subscribe/post?u=c435f53a5568f7951404c8a38&id=4be345b082)
*and follow us on Bluesky*
[*here*](https://bsky.app/profile/bellingcat.com)
*and Mastodon*
[*here*](https://mstdn.social/@Bellingcat)
*.*