---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2025-12-01T12:03:29.697153+00:00'
exported_at: '2025-12-01T12:03:34.150967+00:00'
feed: https://reason.com/feed/
language: en
source_url: https://reason.com/2025/12/01/our-obsession-with-statistical-significance-is-ruining-science
structured_data:
  about: []
  author: ''
  description: From medicine to economics, significance testing misleads. Estimation
    offers a clearer way forward.
  headline: Our Obsession With Statistical Significance Is Ruining Science
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://reason.com/2025/12/01/our-obsession-with-statistical-significance-is-ruining-science
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Our Obsession With Statistical Significance Is Ruining Science
updated_at: '2025-12-01T12:03:29.697153+00:00'
url_hash: 31f33d7e2146ee0d0aa5283272d75bb65b929ff4
---

A century ago, two oddly domestic puzzles helped set the rules for what modern science treats as "real": a Guinness brewer charged with quality control and a British lady insisting she can taste whether milk or tea was poured first.

Those stories sound quaint, but the machinery they inspired now decides which findings get published, promoted, and believed—and which get waved away as "not significant." Instead of recognizing the limitations of statistical significance, fields including economics and medicine ossified around it, with dire consequences for science. In the 21st century, an obsession with statistical significance led to overprescription of both antidepressant drugs and a headache remedy with lethal side effects. There was another path we could have taken.

Sir Ronald Fisher succeeded 100 years ago in making statistical significance central to scientific investigation. Some scientists have argued for decades that blindly following his approach has led the scientific method down the wrong path. Today, statistical significance has brought many branches of science to a crisis of false-positive findings and bias.

At the beginning of the 20th century, the young science of statistics was blooming. One of the key innovations at this time was small-sample statistics—a toolkit for working with data that contain only a small number of observations. That method was championed by the great data scientist William S. Gosset. His ideas were largely ignored in favor of Fisher's, and our ability to reach accurate and useful conclusions from data was harmed. It's time to revive Gosset's approach to experimentation and estimation.

Fisher's approach, "statistical significance," is a simple method for drawing conclusions from data. Researchers gather data to test a hypothesis. They compute the p-value under the null hypothesis—that's the probability of observing their data if the effect they are testing is absent. They compare that p-value to a cutoff, usually 0.05. If the p-value is below the cutoff—in other words, the data we observe are unlikely under the null hypothesis—then the effect is present.

Fisher pioneered many statistical tools still in use today. But writing in the early 20th century, when science was carried out with fountain pens and slide rules, he could not have anticipated how those tools would be misused in an era of big data and limitless computing power.

Fisher was able to attend Cambridge only by virtue of winning a scholarship in mathematics. In 1919 he was offered a job as a statistician at the Rothamsted Agricultural Experiment Station, the oldest scientific research farm in England. At Rothamsted, then at University College London and Cambridge, Fisher grew into an awesomely productive polymath. He invented p-values, significance testing, maximum likelihood estimation, analysis of variance, and even linkage analysis in genetics.
[The Simply Statistics blog estimates](https://simplystatistics.tumblr.com/post/18903448428/ra-fisher-is-the-most-influential-scientist-ever)
that if every paper that used a Fisherian tool cited him by 2012 he would have amassed over 6 million citations, making him the most influential scientist ever.

In 1925 Fisher published his first textbook,
*Statistical Methods for Research Workers,*
which defined the field of statistics for much of the 20th century. Before its publication, a researcher who wished to draw conclusions from data would make use of a large-sample formula such as the normal distribution. Discovered a hundred years earlier by Carl Friedrich Gauss, the normal distribution is the standard "bell curve" formula for an entire population of observations around a central mean. Fisher's textbook provided tools to analyze more limited samples of data.

**How Beer Led to a Breakthrough**

The most important small-sample formula in
*Statistical Methods*
was discovered by a correspondent of Fisher's, William Sealy Gosset, who studied mathematics and chemistry at Oxford. Instead of staying in academia, Gosset moved to Dublin to work for Guinness.

Guinness was expanding rapidly and shipping its product worldwide. By 1900 it was the largest beer maker in the world, producing over a million gallons of stout porter each year. At such scale, it no longer made sense to test each batch by taste and feel. Guinness set up an experimental lab within its giant brewery in St. James's Gate, Dublin, to systematically improve quality and yield, and staffed it with talented young university graduates. Gosset and his colleagues were among the first industrial data scientists.

Gosset's interest in small-sample statistics flowed from his everyday work. Beer takes three ingredients: yeast, hops, and grain. The grain in Guinness is malted barley. To prepare the barley, you steep it in water, allow it to germinate, and then dry and roast it, which malts the starch into sugar that the yeast can digest. The amount of sugar in a batch of malt affects the taste of the beer, its shelf life, and its alcohol content, and was measured at that time in "degrees saccharine."

Guinness had established that 133 degrees saccharine per barrel was the ideal level, and was willing to tolerate a margin of error of 0.5 degrees on either side. The brewer could take spoonfuls from a barrel of malt, test each spoonful, then take the average. But how accurate would that average be—should he take five spoonfuls or 10? Gosset verified that small-sample estimates are more spread out than a normal distribution, because you might draw a spoonful that is unusually high or unusually low in sugar, and in a small sample such outliers will have outsize influence.

Gosset was unable to mathematically solve the distribution of a small sample. Impressively, he wrote out a formula based solely on his intuition. To check his work, Gosset made use of a set of physical measurements taken by the British police from 3,000 prisoners. He wrote each prisoner's height and finger length on a card, then shuffled the cards and divided them into groups of four. The averages of the four-card samples had a distribution that matched closely with his formula.

That formula was immediately useful in his job of industrial quality control. Guinness now had an exact formula for the number of samples that would yield a desired level of accuracy. Guinness scientists were allowed to publish their work in academic journals on two conditions: The paper must not mention Guinness or any beer-related topics, and it must use a pseudonym. Under the name "Student"—he kept his laboratory notes in a notebook whose cover read "The Student's Science Notebook"—Gosset
[published his small-sample formula in 1908](https://www.jstor.org/stable/2331554)
.

The height of plants and prisoners, the degrees saccharine of a batch of malt, the test scores of college applicants, and many other real-world examples are approximately normally distributed. Thus, knowing the distribution of a small sample drawn from such a population would be useful in many areas of science. Ronald Fisher, then a Cambridge undergraduate, recognized the potential of Student's distribution, and in 1912 he mathematically proved the formula that Gosset had guessed.

Gosset's formula was a product of his work at Guinness. But the formal proof was all Fisher, as was the organization of
*Statistical Methods for Research Workers*
. One of the reasons Fisher's textbook was so influential was an innovative feature: It included a set of statistical tables. The researcher could pick the distribution that corresponded to their data and look up the p-value in the corresponding table.

Gosset was unimpressed with this emphasis on p-values. In a 1937 letter, talking about a comparison of crop yields at different farm stations, he wrote that "the important thing in such is to have a low real error, not to have a 'significant' result at a particular station. The latter seems to me to be nearly valueless in itself." Gosset was not interested in statistical significance, and he had no null hypothesis to test. His interest was in accurately measuring the yield. The economists
[Aaron Edlin and Michael Love](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4195779)
call this philosophy "estimation culture."

**The Flaws in Fisher**

In his 1936 textbook,
*The Design of Experiments*
, Fisher formally laid the foundation of significance testing. On page 6, Fisher describes an acquaintance, a British lady who claims that she can distinguish by taste whether the milk or the tea was poured first. Fisher is skeptical. He proposes having the lady drink eight cups of tea, four milk-first and four tea-first, in random order, and try to guess which was which. How, he asks, should we evaluate the data from this experiment?

Fisher advised calculating the probability of observing your data under the null hypothesis that the lady has no tea-tasting ability. If she is picking at random, she might get all eight cups of tea correct by chance, but the probability of that happening is one in 72—a p-value of 0.014. Fisher then proposes that a p-value under 5 percent is "statistically significant," while a p-value greater than 5 percent is not.

The Fisherian approach flows from the specifics of the tea-tasting example. The binary, yes-or-no approach arises because the fundamental question is "Does the lady have tea-tasting ability, or does she not?" We are not trying to estimate how much tea-tasting ability she has. This feature of the tea-tasting experiment—the binary yes-or-no question—is critical to the Fisherian approach. Without it, statistical significance is unhelpful at best, actively misleading at worst.

The original sin of statistical significance is that it sets up an artificial yes-or-no dichotomy in how we learn from data. Fisher himself would agree that his 0.05 threshold for significance is arbitrary. But this arbitrary cutoff leads us to discard useful information. Imagine you run an expensive randomized trial of a new drug and find that it miraculously cures patients of pancreatic cancer—but only in a few rare cases, so that p = 0.06 and the result is statistically insignificant. Hopefully, we would not toss the project. Put differently, experiments do not exist merely to test the null hypothesis. Their purpose is to advance human knowledge, such as finding cancer cures.

Many important scientific experiments are completely outside of the Fisherian statistical significance model. For one sterling example, 16 years before the publication of
*The Design of Experiments,*
Robert Millikan and his graduate student, Harvey Fletcher, performed their oil-drop experiment at the University of Chicago. Millikan and Fletcher set up a mechanism that sprayed droplets of oil past an X-ray tube and then between two metal plates wired with an electric current.

As the droplets passed the X-ray tube, they became ionized—that is, they absorbed one or more extra electrons and gained a negative charge. By gently varying the voltage between the metal plates, Millikan and Fletcher could see when the oil drops floated in midair, precisely balancing the electrical force with the pull of gravity. That level of electrical current, plus the weight of the average oil drop, let them estimate the charge of the electron.

The oil-drop experiment was such a tour de force that Millikan received the Nobel Prize in physics just 14 years later, in 1923—two years before the publication of
*The Design of Experiments*
. But what null hypothesis were they testing? Nobody thought that the charge of an electron might be zero. Instead, the oil-drop experiment is a towering example of estimation culture: an experiment to measure the world we live in.

**How Statistical Significance Causes Publication Bias**

Significance culture versus estimation culture might seem like a minor technical debate. If you're not a tenure-track academic, you may find it hard to believe how much one's career depends on getting "significant" publishable results. In my own field of economics,
[Isaiah Andrews and Maximilian Kasy estimated](https://www.aeaweb.org/articles?id=10.1257/aer.20180310)
that a statistically significant result is 30 times more likely to be published than a nonsignificant result. In the prestigious
*American Economic Review*
in 1983, the economist
[Ed Leamer wrote,](https://www.jstor.org/stable/1803924)
"This is a sad and decidedly unscientific state of affairs…hardly anyone takes anyone else's data analysis seriously. Like elaborately plumed birds who have long since lost the ability to procreate but not the desire, we preen and strut and display our [p]-values."

We might imagine that medical studies are held to a higher standard. But in a
[2008 study](https://www.nejm.org/doi/full/10.1056/NEJMsa065779)
in the
*New England Journal of Medicine,*
researchers gathered data from 74 preregistered studies of antidepressant medications. Of the 38 studies that found a statistically and medically positive result, 37 were ultimately published. Of the 36 that found negative or insignificant results, 33 were either not published or published in a way the researchers considered misleading.

If a doctor relied on the published literature, then, they would see 94 percent of studies yielding a positive outcome. In reality, only 51 percent of studies found a positive outcome—no better than a coin flip.

Individual findings are also distorted by significance culture. Vioxx is a nonsteroidal anti-inflammatory drug (or NSAID) similar to aspirin. In the year 2000,
[a clinical trial](https://www.nejm.org/doi/full/10.1056/NEJM200011233432103)
funded by its producer—the pharmaceutical firm Merck—reported that the difference between the treated and control groups in the rate of cardiac complications "did not reach statistical significance."

But heart issues were quite rare in their patient population. One patient out of 2,772 in the control group had cardiac complications. In the treated group, five patients out of 2,785 had cardiac complications. The risk of the deadly side effect was five times higher among treated patients. But because one and five out of 2,800 are both very low numbers, the p-value of the difference is above 0.05. As a result, it was reported and marketed as having no significant difference.

Less than a year later, Merck pulled Vioxx from the market; follow-up studies had found the NSAID led to an increased risk of heart attack and stroke. In the meantime,
[millions of prescriptions were handed out](https://www.nejm.org/doi/full/10.1056/NEJMp048286)
.

Statistical significance had a doubly malign effect on the Vioxx study. First, it caused the researchers, editors, and reviewers to ignore the higher rate of cardiac complications because the difference was not statistically significant. Second, and more insidiously, statistical significance meant that they did not think about the relative costs and benefits. We already have aspirin, Tylenol, Advil, and other NSAID drugs, so the contribution to human well-being of Vioxx's ability to alleviate aches and pains was always going to be modest. By contrast, an increase in the risk of cardiac complications is deadly serious. But statistical significance does not consider the importance of the outcome; all that matters is the p-value.

The false-positive problem is getting worse, not better, in the world of big data. As we run more and more studies, we sieve down to smaller and less important effects. At the same time, we increase our sample sizes and run more and more significance tests. As a result, the flood of nonsense findings is rising over time—as predicted in a 2005
*PLoS Medicine*
article by John Ioannidis titled "
[Why Most Published Research Findings Are False](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124)
."

**Can "Estimation Culture" Improve Practical Science?**

Gosset disliked statistical significance. He was interested in estimating useful quantities in the real world, quantifying his confidence around that estimate, and adding up the costs and benefits involved. His
[1908
*Biometrika*
paper on the small-sample formula](https://www.jstor.org/stable/2331554)
states that "any series of experiments is only of value in so far as it enables us to form a judgment as to the statistical constants of the population." That's estimation culture.

Could we shift the norms and practices of entire fields (social science and medicine, for starters) toward estimation culture? More than 100 years later, we can still look to industry for inspiration. In recent years, there's been a flood of quantitative researchers into software and marketing jobs analyzing the oceans of data collected by companies such as Google and Microsoft.

A
[2025
*Information Research Studies*
paper](https://pubsonline.informs.org/doi/abs/10.1287/isre.2024.0872)
examined over 16,000 statistical tests run by e-commerce data scientists. The researchers found no evidence of p-hacking or selective publication. Unlike academics, data scientists in industry don't need to publish or perish, so they have no incentive to distort their findings; they are paid for accuracy. Just like their forebear at the Guinness brewery, they naturally cleave to estimation culture.

Academics and journalists should do likewise. Start with the estimate itself and our confidence in that estimate. Put the number in context, evaluate its relevance and plausibility, and try to add up the potential costs and benefits on each side. Finally, recognize that the scientific record in many fields presents a severely distorted picture. When reading the academic literature—to say nothing of the media coverage—keep in mind that we see all the positive and significant findings, and far fewer of the negative or insignificant findings.

There is a better way, and it was there in the Guinness brewery with William Gosset 100 years ago. It starts with dethroning statistical significance, moving away from all-or-none frequentist thinking and toward estimation culture.