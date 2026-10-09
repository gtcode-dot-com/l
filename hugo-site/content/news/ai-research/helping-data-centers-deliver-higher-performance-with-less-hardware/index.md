---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-08T00:15:45.990168+00:00'
exported_at: '2026-04-08T00:15:48.937556+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/helping-data-centers-deliver-higher-performance-less-hardware-0407
structured_data:
  about: []
  author: ''
  description: MIT researchers developed an intelligent system for balancing the tasks
    of storage devices inside a data center, which can extend the longevity of storage
    hardware and help a data center operate more efficiently.
  headline: Helping data centers deliver higher performance with less hardware
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/helping-data-centers-deliver-higher-performance-less-hardware-0407
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Helping data centers deliver higher performance with less hardware
updated_at: '2026-04-08T00:15:45.990168+00:00'
url_hash: 2260a8ab08f14630cb52c10077a51550e4dd64b6
---

To improve data center efficiency, multiple storage devices are often pooled together over a network so many applications can share them. But even with pooling, significant device capacity remains underutilized due to performance variability across the devices.

MIT researchers have now developed a system that boosts the performance of storage devices by handling three major sources of variability simultaneously. Their approach delivers significant speed improvements over traditional methods that tackle only one source of variability at a time.

The system uses a two-tier architecture, with a central controller that makes big-picture decisions about which tasks each storage device performs, and local controllers for each machine that rapidly reroute data if that device is struggling.

The method, which can adapt in real-time to shifting workloads, does not require specialized hardware. When the researchers tested this system on realistic tasks like AI model training and image compression, it nearly doubled the performance delivered by traditional approaches. By intelligently balancing the workloads of multiple storage devices, the system can increase overall data center efficiency.

“There is a tendency to want to throw more resources at a problem to solve it, but that is not sustainable in many ways. We want to be able to maximize the longevity of these very expensive and carbon-intensive resources,” says Gohar Chaudhry, an electrical engineering and computer science (EECS) graduate student and lead author of a
[paper on this technique](https://goharirfan.me/publications/sandook_nsdi_2026.pdf)
. “With our adaptive software solution, you can still squeeze a lot of performance out of your existing devices before you need to throw them away and buy new ones.”

Chaudhry is joined on the paper by Ankit Bhardwaj, an assistant professor at Tufts University; Zhenyuan Ruan PhD ’24; and senior author Adam Belay, an associate professor of EECS and a member of the MIT Computer Science and Artificial Intelligence Laboratory. The research will be presented at the USENIX Symposium on Networked Systems Design and Implementation.

**Leveraging untapped performance**

Solid-state drives (SSDs) are high-performance digital storage devices that allow applications to read and write data. For instance, an SSD can store vast datasets and rapidly send data to a processor for machine-learning model training.

Pooling multiple SSDs together so many applications can share them improves efficiency, since not every application needs to use the entire capacity of an SSD at a given time. But not all SSDs perform equally, and the slowest device can limit the overall performance of the pool.

These inefficiencies arise from variability in SSD hardware and the tasks they perform.

To utilize this untapped SSD performance, the researchers developed Sandook, a software-based system that tackles three major forms of performance-hampering variability simultaneously. “Sandook” is an Urdu word that means “box,” to signify “storage.”

One type of variability is caused by differences in the age, amount of wear, and capacity of SSDs that may have been purchased at different times from multiple vendors.

The second type of variability is due to the mismatch between read and write operations occurring on the same SSD. To write new data to the device, the SSD must erase some existing data. This process can slow down data reads, or retrievals, happening at the same time.

The third source of variability is garbage collection, a process of gathering and removing outdated data to free up space. This process, which slows SSD operations, is triggered at random intervals that a data center operator cannot control.

“I can’t assume all SSDs will behave identically through my entire deployment cycle. Even if I give them all the same workload, some of them will be stragglers, which hurts the net throughput I can achieve,” Chaudhry explains.

**Plan globally, react locally**

To handle all three sources of variability, Sandook utilizes a two-tier structure. A global schedular optimizes the distribution of tasks for the overall pool, while faster schedulers on each SSD react to urgent events and shift operations away from congested devices.

The system overcomes delays from read-write interference by rotating which SSDs an application can use for reads and writes. This reduces the chance reads and writes happen simultaneously on the same machine.

Sandook also profiles the typical performance of each SSD. It uses this information to detect when garbage collection is likely slowing operations down. Once detected, Sandook reduces the workload on that SSD by diverting some tasks until garbage collection is finished.

“If that SSD is doing garbage collection and can’t handle the same workload anymore, I want to give it a smaller workload and slowly ramp things back up. We want to find the sweet spot where it is still doing some work, and tap into that performance,” Chaudhry says.

The SSD profiles also allow Sandook’s global controller to assign workloads in a weighted fashion that considers the characteristics and capacity of each device.

Because the global controller sees the overall picture and the local controllers react on the fly, Sandook can simultaneously manage forms of variability that happen over different time scales. For instance, delays from garbage collection occur suddenly, while latency caused by wear and tear builds up over many months.

The researchers tested Sandook on a pool of 10 SSDs and evaluated the system on four tasks: running a database, training a machine-learning model, compressing images, and storing user data. Sandook boosted the throughput of each application between 12 and 94 percent when compared to static methods, and improved the overall utilization of SSD capacity by 23 percent.

The system enabled SSDs to achieve 95 percent of their theoretical maximum performance, without the need for specialized hardware or application-specific updates.

“Our dynamic solution can unlock more performance for all the SSDs and really push them to the limit. Every bit of capacity you can save really counts at this scale,” Chaudhry says.

In the future, the researchers want to incorporate new protocols available on the latest SSDs that give operators more control over data placement. They also want to leverage the predictability in AI workloads to increase the efficiency of SSD operations.

“Flash storage is a powerful technology that underpins modern datacenter applications, but sharing this resource across workloads with widely varying performance demands remains an outstanding challenge. This work moves the needle meaningfully forward with an elegant and practical solution ready for deployment, bringing flash storage closer to its full potential in production clouds,” says Josh Fried, a software engineer at Google and incoming assistant professor at the University of Pennsylvania, who was not involved with this work.

This research was funded, in part, by the National Science Foundation, the U.S. Defense Advanced Research Projects Agency, and the Semiconductor Research Corporation.