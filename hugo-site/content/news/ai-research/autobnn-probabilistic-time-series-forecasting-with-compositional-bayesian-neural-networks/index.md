---
ai_agent_meta:
  content_digest: d38951e36495f47697cbdb2cbf6c6d98e45e31ec
  generated_at: '2025-11-10T02:34:22.628184+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
ai_agent_note: 'ATTN AI Agent: Ensure JSON conforms to the specified schema, preserve
  key terminology (compositional kernels, Sequential Monte Carlo, probabilistic forecasting),
  and maintain concise, professional prose.'
ai_commentary:
- body: The framework emphasizes interpretable model structures that domain experts
    can reason about, supported by discrete search over a small, human-understandable
    space of components and operators.
  title: Interpretability and domain expertise
- body: Builds on a decade of GP kernel-learning work (e.g., Duvenaud 2013; Saad 2023)
    while migrating to Bayesian neural networks to retain probabilistic forecasting
    and uncertainty quantification.
  title: Relation to prior kernel-learning work
- body: Discrete structure search via Sequential Monte Carlo enables tractable exploration
    of compositional components and operators, yielding transparent, candidate models
    for domain experts to compare and validate.
  title: Methodology and search strategy
ai_commentary_meta:
  content_digest: d38951e36495f47697cbdb2cbf6c6d98e45e31ec
  generated_at: '2025-11-10T02:34:22.628149+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
category: ai-research
date: '2025-11-09T05:13:21.724722+00:00'
exported_at: '2025-11-09T05:30:20.828859+00:00'
feed: http://feeds.feedburner.com/blogspot/gJZg
meta_description: AutoBNN introduces Bayesian neural networks for probabilistic time-series
  forecasting with compositional, kernel-inspired components and structure-search
  via Sequential Monte Carlo, extending learned-kernel ideas beyond Gaussian Processes.
meta_keywords:
- AutoBNN
- Bayesian neural networks
- time-series forecasting
- compositional kernels
- kernel learning
- Gaussian processes
- Sequential Monte Carlo
- ChangePoint
- Periodic
- interpretable models
source_url: http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html
structured_data:
  about: &id001
  - Gaussian Processes with learned, compositional kernels for time-series modeling
  - 'Base kernels and composite operators: Linear, Quadratic, Periodic, Matérn, ExponentiatedQuadratic;
    Addition, Multiplication, ChangePoint'
  - Interpretability through priors and discrete structure search (e.g., Sequential
    Monte Carlo)
  - AutoBNN replaces GP with Bayesian neural networks for probabilistic forecasting
  description: AutoBNN extends the GP-based approach of learning compositional kernels
    for time-series forecasting by substituting the Gaussian Process with Bayesian
    neural networks. Building on a decade of work showing improved predictive accuracy
    from learned kernel structures, AutoBNN maintains probabilistic forecasting and
    interpretable structure through compositional components built from base kernels
    (e.g., Linear, Quadratic, Periodic, Matérn, ExponentiatedQuadratic) and their
    combinations via Addition, Multiplication, or ChangePoint. The framework also
    leverages discrete structure-search techniques, such as Sequential Monte Carlo,
    to yield interpretable results for users with domain expertise.
  headline: 'AutoBNN: Probabilistic time series forecasting with compositional Bayesian
    neural networks'
  keywords: *id001
title: 'AutoBNN: Probabilistic time series forecasting with compositional bayesian
  neural networks'
updated_at: '2025-11-09T05:13:21.724722+00:00'
url_hash: 7a1c5d502bbd270b0fc1b2a17b132fe7c11fa535
---

AutoBNN is based on a
[line](https://proceedings.mlr.press/v28/duvenaud13.html)
[of](https://royalsocietypublishing.org/doi/10.1098/rsta.2011.0550)
[research](https://proceedings.mlr.press/v202/saad23a.html)
that over the past decade has yielded improved predictive accuracy by modeling time series using GPs with learned
[kernel](https://www.cs.toronto.edu/~duvenaud/cookbook/)
structures. The kernel function of a GP encodes assumptions about the function being modeled, such as the presence of trends, periodicity or noise. With learned GP kernels, the kernel function is defined compositionally: it is either a base kernel (such as
Linear
,
Quadratic
,
Periodic
,
[Matérn](https://en.wikipedia.org/wiki/Mat%C3%A9rn_covariance_function)
or
ExponentiatedQuadratic
) or a composite that combines two or more kernel functions using operators such as
Addition
,
Multiplication
, or
[ChangePoint](https://icml.cc/Conferences/2010/papers/170.pdf)
. This compositional kernel structure serves two related purposes. First, it is simple enough that a user who is an expert about their data, but not necessarily about GPs, can construct a reasonable prior for their time series. Second, techniques like
[Sequential Monte Carlo](https://www.stats.ox.ac.uk/~doucet/doucet_defreitas_gordon_smcbookintro.pdf)
can be used for discrete searches over small structures and can output interpretable results.

AutoBNN improves upon these ideas, replacing the GP with
[Bayesian neural networks](https://www.cs.toronto.edu/~duvenaud/distill_bayes_net/public/)
(BNNs) while retaining the compositional kernel structure. A BNN is a neural network with a probability distribution over weights rather than a fixed set of weights. This induces a distribution over outputs, capturing uncertainty in the predictions. BNNs bring the following advantages over GPs: First, training large GPs is computationally expensive, and traditional training algorithms scale as the cube of the number of data points in the time series. In contrast, for a fixed width, training a BNN will often be approximately linear in the number of data points. Second, BNNs lend themselves better to GPU and
[TPU](https://cloud.google.com/tpu?hl=en)
hardware acceleration than GP training operations. Third, compositional BNNs can be easily combined with
[traditional deep BNNs](https://arxiv.org/abs/2007.06823)
, which have the ability to do feature discovery. One could imagine "hybrid" architectures, in which users specify a top-level structure of
Add
(
Linear
,
Periodic
,
Deep
), and the deep BNN is left to learn the contributions from potentially high-dimensional covariate information.

How might one translate a GP with compositional kernels into a BNN then? A single layer neural network will typically converge to a GP as the number of neurons (or "width")
[goes to infinity](https://link.springer.com/chapter/10.1007/978-1-4612-0745-0_2)
. More recently, researchers have
[discovered](https://openreview.net/forum?id=gRwh5HkdaTm)
a correspondence in the other direction — many popular GP
[kernels](https://www.cs.toronto.edu/~duvenaud/cookbook/)
(such as
Matern
,
Exponentiated

Quadratic
,
Polynomial
or
Periodic
) can be obtained as infinite-width BNNs with appropriately chosen activation functions and weight distributions. Furthermore, these BNNs remain close to the corresponding GP even when the width is very much less than infinite. For example, the figures below show the difference in the
[covariance](https://en.wikipedia.org/wiki/Covariance_matrix#:~:text=In%20probability%20theory%20and%20statistics,of%20a%20given%20random%20vector)
between pairs of observations, and
[regression](https://en.wikipedia.org/wiki/Kriging)
results of the true GPs and their corresponding width-10 neural network versions.