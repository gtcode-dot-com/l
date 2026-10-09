---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-07T03:17:12.527787+00:00'
exported_at: '2026-10-07T03:17:14.106731+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/algorithmic-monoculture-effects-depend-on-details-0929
structured_data:
  about: []
  author: ''
  description: The use of a single hiring algorithm by multiple firms, known as algorithmic
    monoculture, is less problematic for job seekers than past research has shown,
    and may even be a good thing depending on the approach used, according to a study
    by MIT researchers.
  headline: The effects of an “algorithmic monoculture” depend on the details
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/algorithmic-monoculture-effects-depend-on-details-0929
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The effects of an “algorithmic monoculture” depend on the details
updated_at: '2026-10-07T03:17:12.527787+00:00'
url_hash: 7912342139f3efcb3d77f66f0be61767cdebccf1
---

AI tools are increasingly replacing human judgements in some settings. For instance, resume screening algorithms are often used in hiring, where they may improve efficiency and consistency in decision-making.

But some scholars have
[raised concerns](https://www.pnas.org/doi/10.1073/pnas.2018340118)
that the adoption of automated systems could eventually result in one algorithm being used to make all decisions in a particular industry. They worry so-called algorithmic monoculture could have negative consequences.

For example, in hiring, the thinking goes that algorithmic monoculture might result in systematic exclusion — a situation in which a job candidate rejected by one firm’s algorithm would likely also be rejected by every other firm’s algorithm.

However, MIT researchers now argue that algorithmic monoculture may not always be as bad as some scientists have suggested.

They systematically evaluated major objections to algorithmic monoculture, including systematic exclusion, and concluded this and many other arguments either fail or aren’t decisive against all forms of monoculture.

Instead, they mathematically prove that monoculture tends to create informational echo chambers that can hinder exploration. In hiring, this could make it less likely that the best candidates would get jobs — however, bundling various hiring algorithms into a single “ensemble” can overcome this limitation, the researchers show. This could sometimes enable monoculture to perform as well as, if not better than, a polyculture where different firms use different algorithms.

“A trend toward algorithmic monoculture is a realistic scenario, and a really important issue that is being brought about by the use of AI, but it is hard to say in the abstract whether monoculture would be a bad thing. It depends on the details, like the domain we are talking about and the accuracy of the algorithm itself,” says study co-author Brian Hedden, a professor in the Department of Linguistics and Philosophy, who holds an MIT Schwarzman College of Computing shared position with the Department of Electrical Engineering and Computer Science (EECS) and is also a principal investigator in the Laboratory for Information and Decision Systems (LIDS).

Hedden is joined on the paper by co-author Manish Raghavan, the Drew Houston (2005) Career Development Professor at the MIT Sloan School of Management and in EECS, as well as a LIDS principal investigator. The research
[appears in
*Philosophical Perspectives*](https://onlinelibrary.wiley.com/doi/10.1111/phpe.70018)
*.*

**The move toward monoculture**

Algorithmic monoculture, in which all decisions across a certain domain are made using the same algorithm, is not a new phenomenon.

For instance, lending decisions were once made by independent bankers at individual banks, but now all bankers use the same information based on a borrower’s standardized credit scores, which are derived from the Fair Isaac Corporation (FICO) algorithm.

Similarly, a handful of resume screening algorithms are commonly used by many Fortune 500 companies.

“The worry is that, as more people use AI and algorithms to get information and make decisions, there is more of a vehicle for this kind of correlation to occur,” Raghavan says.

To better understand this issue, he and Hedden joined forces to systematically assess the promises and pitfalls of algorithmic monoculture. They focused on hiring, but their approach could apply to other domains, such as lending. (They note, however, that other domains, like generative AI content creation or AI-guided scientific research, may work differently, and that monoculture in some of these domains may be more problematic.)

The researchers began by exploring one common objection to algorithmic monoculture: that reliance on the same algorithm will systematically exclude certain people from opportunities.

This could occur in hiring because, if one firm screens out an individual’s resume, that applicant will likely face the same bad luck at each firm.

But after systematically evaluating this argument using a series of models that capture multiple situations, the researchers argue it isn’t compelling since the overall number of people hired is not affected by the fact that firms use the same algorithm.

Rather, algorithmic monoculture could improve bargaining power of job candidates.

“All the jobs get filled and the same number of people have jobs, but the firms are fighting over the same pool of candidates, which actually drives up wages,” Raghavan says.

They also explored objections related to agency. For instance, if a job candidate applies for a job and their resume is forwarded to every firm using the hiring algorithm, the candidate never gets a chance to adjust their resume to improve their chances.

“This seems like a good objection to bad forms of monoculture. But if you have a monoculture where you get to revise your resume and resubmit your materials, then this doesn’t hold up,” Hedden says.

On the flip side, monoculture could enable individuals to game the system. For instance, if having one’s resume in a certain format leads to a better outcome, job candidates could simply reformat their resumes to improve their chances.

“But it is not obvious that having one algorithm would incentivize this kind of gaming more than having a bunch of different algorithms used by different firms,” Hedden says. “In the latter scenario, you might just target a couple of firms’ algorithms and try to game them, giving yourself a bit of advantage with a few employers.”

**The wisdom of crowds**

They also considered a less-explored objection: that monoculture can increase homogenization of information.

Based on the “wisdom of crowds,” a theory from social psychology, a diverse group of independent decision makers can outperform a single person, Hedden explains.

In hiring, this means that having firms with diverse hiring algorithms can lead to a higher-quality pool of new hires.

Algorithmic monoculture could also cause candidates with the same characteristics and credentials to be hired every time by every firm. This may prevent firms from discovering candidates who may be better alternatives.

“Monoculture might inhibit the amount of discovery that happens overall. It is not clear if that is a bad thing, but it is definitely a worry when we think about designing AI for applications like science, art, or writing,” Raghavan says.

This problem could be mitigated by building randomness into a monocultural platform, which could induce a higher level of exploration, he adds.

In addition, the performance of monoculture depends on the algorithm. If a single algorithm is much more accurate than the many algorithms used by different firms, monoculture may be better system.

One way to boost performance may be to package multiple firms’ hiring algorithms into one “ensemble algorithm” that could assign each job candidate a score based on the average.

By conducting a series of simulations of different hiring situations, the researchers confirmed that such an “ensemble algorithm” could sometimes outperform the use of multiple algorithms.

However, it remains to be explored how feasible this kind of algorithmic “ensembling” would be in practice, Hedden says.

“A lot of the answers around the promises and pitfalls of algorithmic monoculture are going to be contextual. Even from a research perspective, there is still a lot of work to be done to figure out how we can approach these concerns from an empirical perspective,” Raghavan says.

Ultimately, the researchers hope this work inspires additional research about the long-term consequences of algorithmic monoculture, as well as studies that focus on the real-world complexities involved in a complex system like a job market.