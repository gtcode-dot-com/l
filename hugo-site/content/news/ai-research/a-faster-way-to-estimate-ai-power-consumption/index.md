---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-27T04:15:37.036210+00:00'
exported_at: '2026-04-27T04:15:39.219910+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/faster-way-to-estimate-ai-power-consumption-0427
structured_data:
  about: []
  author: ''
  description: The EnergAIzer technique can predict how much power a certain AI workload
    will consume when run on a particular processor. This method could help data center
    operators and algorithm developers improve the sustainability of AI workloads.
  headline: A faster way to estimate AI power consumption
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/faster-way-to-estimate-ai-power-consumption-0427
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A faster way to estimate AI power consumption
updated_at: '2026-04-27T04:15:37.036210+00:00'
url_hash: 0c12c016ef1eefe60bd2246ce3e5cd949bd83ae3
---

Due to the explosive growth of artificial intelligence, it is estimated that data centers will consume
[up to 12 percent of total U.S. electricity by 2028](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/)
, according to the Lawrence Berkeley National Laboratory. Improving data center energy efficiency is one way scientists are striving to make AI more sustainable.

Toward that goal, researchers from MIT and the MIT-IBM Watson AI Lab developed a rapid prediction tool that tells data center operators how much power will be consumed by running a particular AI workload on a certain processor or AI accelerator chip.

Their method produces reliable power estimates in a few seconds, unlike traditional modeling techniques that can take hours or even days to yield results. Moreover, their prediction tool can be applied to a wide range of hardware configurations — even emerging designs that haven’t been deployed yet.

Data center operators could use these estimates to effectively allocate limited resources across multiple AI models and processors, improving energy efficiency. In addition, this tool could allow algorithm developers and model providers to assess potential energy consumption of a new model before they deploy it.

“The AI sustainability challenge is a pressing question we have to answer. Because our estimation method is fast, convenient, and provides direct feedback, we hope it makes algorithm developers and data center operators more likely to think about reducing energy consumption,” says Kyungmi Lee, an MIT postdoc and lead author of a
[paper on this technique](https://arxiv.org/pdf/2604.20105)
.

She is joined on the paper by Zhiye Song, an electrical engineering and computer science (EECS) graduate student; Eun Kyung Lee and Xin Zhang, research managers at IBM Research and the MIT-IBM Watson AI Lab; Tamar Eilam, IBM Fellow, chief scientist of sustainable computing at IBM Research, and a member of the MIT-IBM Watson AI Lab; and senior author Anantha P. Chandrakasan, MIT provost, Vannevar Bush Professor of Electrical Engineering and Computer Science, and a member of the MIT-IBM Watson AI Lab. The research is being presented this week at the IEEE International Symposium on Performance Analysis of Systems and Software.

**Expediting energy estimation**

Inside a data center, thousands of powerful graphics processing units (GPUs) perform operations to train and deploy AI models. The power consumption of a particular GPU will vary based on its configuration and the workload it is handling.

Many traditional methods used to predict energy consumption involve breaking a workload into individual steps and emulating how each module inside the GPU is being utilized one step at a time. But AI workloads like model training and data preprocessing are extremely large and can take hours or even days to simulate in this manner.

“As an operator, if I want to compare different algorithms or configurations to find the most energy-efficient manner to proceed, if a single emulation is going to take days, that is going to become very impractical,” Lee says.

To speed up the prediction process, the MIT researchers sought to use less-detailed information that could be estimated faster. They found that AI workloads often have many repeatable patterns. They could use these patterns to generate the information needed for reliable but quick power estimation.

In many cases, algorithm developers write programs to run as efficiently as possible on a GPU. For instance, they use well-structured optimizations to distribute the work across parallel processing cores and move chunks of data around in the most efficient manner.

“These optimizations that software developers use create a regular structure, and that is what we are trying to leverage,” explains Lee.

The researchers developed a lightweight estimation model, called EnergAIzer, that captures the power usage pattern of a GPU from those optimizations.

**An accurate assessment**

But while their estimation was fast, the researchers found that it didn’t take all energy costs into account. For instance, every time a GPU runs a program, there is a fixed energy cost required for setting up and configurating that program. Then each time the GPU runs an operation on a chunk of data, an additional energy cost must be paid.

Due to fluctuations in the hardware or conflicts in accessing or moving data, a GPU might not be able to use all available bandwidth, slowing operations down and drawing more energy over time.

To include these additional costs and variances, the researchers gathered real measurements from GPUs to generate correction terms they applied to their estimation model.

“This way, we can get a fast estimation that is also very accurate,” she says.

In the end, a user can provide their workload information, like the AI model they want to run and the number and length of user inputs to process, and EnergAIzer will output an energy consumption estimation in a matter of seconds.

The user can also change the GPU configuration or adjust the operating speed to see how such design choices impact the overall power consumption.

When the researchers tested EnergAIzer using real AI workload information from actual GPUs, it could estimate the power consumption with only about 8 percent error, which is comparable to traditional methods that can take hours to produce results.

Their method could also be used to predict the power consumption of future GPUs and emerging device configurations, as long as the hardware doesn’t change drastically in a short amount of time.

In the future, the researchers want to test EnergAIzer on the newest GPU configurations and scale the model up so it can be applied to many GPUs that are collaborating to run a workload.

“To really make an impact on sustainability, we need a tool that can provide a fast energy estimation solution across the stack, for hardware designers, data center operators, and algorithm developers, so they can all be more aware of power consumption. With this tool, we’ve taken one step toward that goal,” Lee says.

This research was funded, in part, by the MIT-IBM Watson AI Lab.