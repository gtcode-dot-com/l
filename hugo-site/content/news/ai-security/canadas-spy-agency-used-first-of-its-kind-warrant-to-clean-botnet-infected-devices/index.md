---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:54:00.839444+00:00'
exported_at: '2026-06-23T03:54:03.330168+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/canadas-spy-agency-used-first-of-its.html
structured_data:
  about: []
  author: ''
  description: Canada’s spy agency used a court-approved warrant to neutralize two
    foreign-run botnets abusing routers, servers, and IoT devices.
  headline: Canada’s Spy Agency Used First-of-Its-Kind Warrant to Clean Botnet-Infected
    Devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/canadas-spy-agency-used-first-of-its.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Canada’s Spy Agency Used First-of-Its-Kind Warrant to Clean Botnet-Infected
  Devices
updated_at: '2026-06-23T03:54:00.839444+00:00'
url_hash: e34b04d248816badef317a3d5815af26b9eaf753
---

Canada's spy service got a judge's permission to reach into infected servers, home routers, and IoT gear sitting on Canadian soil and neutralize two foreign-run botnets.

The Federal Court released a
[public version](https://www.fct-cf.ca/en/pages/media/news-bulletins/file-c-6-24)
of the ruling on June 15. It is the first time the Canadian Security Intelligence Service has used its threat reduction warrant powers this way.

The warrant let CSIS alter, degrade, and destroy botnet data on the infected machines and cut the devices loose from the networks.

The targets were Canada-based servers, small office and home office (SOHO) routers, and Internet of Things devices: Ring doorbells, security cameras, TVs, and other Wi-Fi-enabled appliances.

Justice Catherine Kane granted the warrant on May 1, 2024, renewed it that August, and issued the confidential reasons in February 2026. The warrant stayed out of public view for more than two years, until this month's redacted release.

CSIS needed the order because the cleanup would likely have been a crime without it. Reaching into someone else's device and wiping data is computer mischief under the Criminal Code, so the Service needed a judge's sign-off before touching the machines.

The court found the threat to Canada clearly established and imminent, and the measures necessary, reasonable, and proportional. It stressed the operation went after devices, not people: no user identities sought, no content intercepted, any personal data swept up incidentally destroyed.

The two botnets ran the standard relay playbook. A command tier issued the orders; a layer of infected devices relayed the traffic. By routing through hijacked Canadian hardware, a foreign state can look like an ordinary connection, a home worker, or an ISP customer, while it probes critical infrastructure, government, and military networks.

The owner of the infected doorbell gets left looking responsible for traffic they never sent. The court flagged the energy sector among the targets and warned that the
[adversaries could direct the botnets](https://www.narcity.com/csis-got-judges-ok-to-neutralize-infected-devices)
to probe and potentially disrupt Canadian infrastructure.

The public ruling settles the what: two foreign adversaries, a threat to Canada's security, the court found clearly made out. What it strips is the who. The timing and the technique match a specific moment in early 2024, but The Bureau, which
[surfaced the ruling](https://www.todayville.com/canadas-spy-service-won-permission-to-hack-two-state-linked-botnets-assessed-to-likely-include-china-hiding-inside-canadian-homes/)
, says it cannot tell from the redacted reasons whether Canada's two botnets were both Chinese, both Russian, or one of each. The foreign-state hand is a finding. The flag is the redaction.

## Same Tactic, a Different Authority

That moment was a run of court-ordered botnet cleanups in the United States. In a December 2023 operation, the FBI used the botnet's own command channel to delete the
[KV-botnet malware](https://thehackernews.com/2024/02/us-feds-shut-down-china-linked-kv.html)
from hundreds of U.S. SOHO routers, mostly end-of-life Cisco and NetGear boxes that the China-linked Volt Typhoon was using to hide access it had planted ahead of a possible crisis inside American communications, energy, water, and transportation systems.

Weeks later, it ran a near-identical operation against a separate network of Ubiquiti routers that Russia's GRU, the
[APT28 group](https://thehackernews.com/2024/02/us-government-disrupts-russian-linked.html)
, had turned into an espionage relay.

Canada's cyber centre had joined the allied warnings about state actors abusing SOHO and IoT gear. Same court-ordered shape both times: neglected consumer gear, a state operator, a judge signing off on remote disinfection.

The difference is who holds the warrant. The U.S. operations were law enforcement, FBI, and DOJ acting under search-and-seizure authority.

Canada's is an intelligence service using threat reduction measures, the CSIS's power to actively disrupt a threat rather than just collect intelligence on it, written into the CSIS Act years ago and reworked in the
[National Security Act, 2017](https://www.canada.ca/en/security-intelligence-service/news/2020/06/amendments-to-the-csis-act---threat-reduction-measures.html)
, which took effect in 2019. CSIS had never reached for it like this until now.

## It Still Comes Down to Old Routers

The lesson for defenders is the boring one. The botnets feed on the gear nobody maintains: end-of-life routers still wired into the network, IoT kits that never took their last firmware update, anything sitting on default credentials with a management panel facing the internet.

A government cleanup does not touch that. In the U.S. operations, the malware came off, but the weaknesses stayed, and a reboot or factory reset could undo the fix and reopen the door to reinfection. Retiring the dead hardware and locking down what stays is on the owner, not the agency that cleaned up after them.

One loose end the public ruling does not close: the application, by The Bureau's account, leaned on IP addresses CSIS had collected without a warrant, weeks after the Supreme Court of Canada held in
[R. v. Bykovets](https://www.scc-csc.ca/judgments-jugements/cb/2024/40269/)
that an IP address carries a reasonable expectation of privacy.

Whether that squares with CSIS's collection authorities, and whether the owners of the disinfected devices were ever told, stay open.