---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-12T22:51:26.336724+00:00'
exported_at: '2025-11-12T22:54:41.544712+00:00'
feed: http://feeds.feedburner.com/blogspot/gJZg
language: en
source_url: http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html
structured_data:
  about: []
  author: ''
  description: 'AutoBNN: Probabilistic time series forecasting with compositional
    bayesian neural networks'
  headline: 'AutoBNN: Probabilistic time series forecasting with compositional bayesian
    neural networks'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'AutoBNN: Probabilistic time series forecasting with compositional bayesian
  neural networks'
updated_at: '2025-11-12T22:51:26.336724+00:00'
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