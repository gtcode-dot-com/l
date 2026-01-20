---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-20T04:15:26.517154+00:00'
exported_at: '2026-01-20T04:15:28.807770+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/microsoft/diff-attn-v2
structured_data:
  about: []
  author: ''
  description: A Blog post by Microsoft on Hugging Face
  headline: Differential Transformer V2
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/microsoft/diff-attn-v2
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Differential Transformer V2
updated_at: '2026-01-20T04:15:26.517154+00:00'
url_hash: d6ae64ab3b5d77bb0b930512f4fc3844bf66a7ba
---

# Differential Transformer V2

Tianzhu Ye, Li Dong, Yutao Sun, Furu Wei

[Github Link](https://github.com/microsoft/unilm/blob/master/Diff-Transformer/Diff-Transformer-V2)

## Abstract

We introduce
**Differential Transformer V2**
(DIFF V2), an improved version of
[Differential Transformer](https://arxiv.org/abs/2410.05258)
(DIFF V1). This revision focuses on inference efficiency, training stability for production-level LLMs, and architectural elegance.

Key improvements:

1. **Faster Inference & No Need of Custom Attention Kernels**
   Instead of forcing the attention parameter count to match the baseline
   [Transformer](https://arxiv.org/abs/1706.03762)
   (as in DIFF V1), we introduce additional parameters (borrowed from other parts of the model) for $Q\_2$.
   This design allows DIFF V2 to match the baseline Transformer’s decoding speed and directly use
   [FlashAttention](https://github.com/Dao-AILab/flash-attention)
   without custom kernels.
2. **Improved Training Stability**
   We remove the per-head RMSNorm after differential attention. We find the per-head RMSNorm can lead to instability in later stages of large-scale pretraining of LLM.
3. **Simpler Parameterization & Initialization**
   We replace the globally shared $\lambda$ with a token-specific, head-wise projected $\lambda$. \*\*\*\*This eliminates the exponential re-parameterization and initialization of $\lambda$.

We conduct pretraining experiments on production-scale LLMs, including dense models and a 30A3 MoE on trillions of tokens using large learning rate of 6e-4 to 1e-3. Experimental observations:

* **Notably lower language modeling loss**
  compared to Transformer.
* **Reduced loss and gradient spikes during training**
  , particularly under large learning rate settings where the Transformer baseline becomes unstable.
* **Reduced activation outliers magnitude.**

The experiments are still running. We expect to explore in later stages of training:

* If learning efficiency is improved in mid- and post-training.
* If performance on downstream long-context benchmarks improves (alleviating context rot).

After the experiments complete and we evaluate the results, we will prepare a more formal report.

## Code

We compare DIFF V2 with DIFF V1 below:

(For simplicity, we omit the batch dimension and assume that both the input and output of the following
`flash_attn_func`
are three-dimensional tensors
`(tokens, heads, head dimension)`
. Heads belonging to the same GQA group are arranged contiguously in the output)

```
def DiffAttnV1(
        layer_index, q1, q2, k1, k2, v,
        lam_q1, lam_k1, lam_q2, lam_k2,
):
        """
      q1, q2: (N, h/2, d)
      k1, k2: (N, h_kv/2, d)
      v:      (N, h_kv/2, 2d)
      lam_*: (d,)
      """
      attn1 = flash_attn_func(q1, k1, v)
        attn2 = flash_attn_func(q2, k2, v)

        lam_init = 0.8 - 0.6 * \
            exp(-0.3 * layer_index)
        lam1 = exp(sum(lam_q1 * lam_k1)
    lam2 = exp(sum(lam_q2 * lam_k2)
    lam = lam1 - lam2 + lam_init
    attn = attn1 - lam * attn2

    attn = rmsnorm(attn)
    attn = attn * (1 - lam_init)
    return attn
```

```
def DiffAttnV2(
        q, k, v, lam
):
        """
      q:   (N, 2h, d)
      k:   (N, h_kv, d)
      v:   (N, h_kv, d)
      lam: (N, h, 1)
      """

        attn = flash_attn_func(q, k, v)
        attn1, attn2 = (attn[:, 0::2],
                        attn[:, 1::2])

        lam_val = sigmoid(lam)
        attn = attn1 - lam_val * attn2
    return attn
```

Full code at:
[unilm/Diff-Transformer/Diff-Transformer-V2 at master · microsoft/unilm](https://github.com/microsoft/unilm/tree/master/Diff-Transformer/Diff-Transformer-V2)
In the script,
`h`
represents number of query heads,
`h_kv`
represents number of key-value heads, and
`d`
means head dimension. The $\lambda$ in DIFF V2 is projected from $X$ for each token each head.

DIFF V2 doubles number of query heads while maintaining number of key value heads, and the extra dimension is reduced back to
`h*d`
after the differential operation so the $W\_O$ projection remains the same as baseline Transformer.

## Motivation

### **Faster Decoding & No Custom Kernels**

DIFF V2 introduces additional query heads compared to the baseline Transformer,
**but does not increase the number of key-value (KV) heads**
. Since LLM decoding is typically memory-bound, this design allows DIFF V2 to achieve decoding speeds on par with standard Transformer.
**Besides, since head dimension is aligned between query, key and value, there is no need for custom attention kernels for DIFF V2**
. In contrast, DIFF V1 can be slower during decoding because the value cache must be loaded twice, and a custom attention kernel is needed. DIFF V2 can also increase the arithmetic intensity of the attention module during decoding.

**During pretraining**
, when using cutting-edge FlashAttention kernels on H-series and B-series GPUs, the throughput reduction introduced by DIFF V2 is negligible.
**For long-sequence prefilling**
, we recommend combining DIFF V2 with techniques such as
[YOCO](https://arxiv.org/abs/2405.05254)
(also used in
[Gemma 3n](https://github.com/huggingface/transformers/blob/main/src/transformers/models/gemma3n/modeling_gemma3n.py)
), which already reduces prefilling complexity to linear time with respect to sequence length.

**An alternative perspective is to compare DIFF V2 with a Transformer that has the same query dimension**
`2h*d`
. Under this comparison, both models exhibit same attention kernel speed, while DIFF V2 has less parameters and flops in output projection.

### **Softmax Magnitude Constraint**

In the standard Scaled Dot-Product Attention (SDPA), let $Q, K, V \in \mathbb{R}^{n \times d}$ be the queries, keys, and values. The context vector $C$ is defined as:

C

=

Softmax


(



Q


K

T


d

)

V

=

A

V
C = \text{Softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V = AV





C



=






Softmax





(




















d


​












Q


K









T

​



)



V



=





A

V

Where $A \in \mathbb{R}^{n \times n}$ is the attention weight matrix. Let’s focus on a single row of $C$, denoted as $\mathbf{c}\_i$, which is a weighted sum of value vectors $\mathbf{v}\_j$:

c

i

=


∑


j

=

1

n


a


i

j


v

j
\mathbf{c}\_i = \sum\_{j=1}^{n} a\_{ij} \mathbf{v}\_j






c









i

​




=














j

=

1





∑






n

​





a










ij

​



v









j

​

We define the
**Context RMS**
(Root Mean Square) to represent the magnitude of this output:

RMS

(


c

i

)

=




1

d

∥


c

i


∥

2
\text{RMS}(\mathbf{c}\_i) = \sqrt{\frac{1}{d} \|\mathbf{c}\_i\|^2}






RMS

(


c









i

​


)



=
























d











1

​


∥


c









i

​



∥









2


​

The weights $a\_{ij}$ are non-negative and sum to 1 ($\sum\_{j=1}^{n} a\_{ij} = 1$). Assume the value vectors $\mathbf{v}\_j$ are uncorrelated and have an RMS of 1,
**the Context RMS is strictly bounded in range $[\frac{1}{\sqrt{n}},1)$ however the attention distribution changes**
:

* If the attention is focused entirely on one token, the Context RMS is $1$.
* If the attention is spread equally across all tokens ($a\_{ij} = \frac{1}{n}$), the Context RMS drops to $\frac{1}{\sqrt{n}}$.
* In other situations, the Context RMS is between $\frac{1}{\sqrt{n}}$ and $1$.

In DIFF V1 we add a per-head RMSNorm on context vectors:

c

^

i

=



c

i


RMS

(


c

i

)
\mathbf{\hat{c}}\_i = \frac{\mathbf{c}\_i}{\text{RMS}(\mathbf{c}\_i)}













c





^









i

​




=

















RMS

(


c









i

​


)












c









i

​


​

If the model learns a uniform attention distribution in a head, the Context RMS is approximately $1/\sqrt{n}$. To normalize this back to $1$, RMSNorm must multiply the vector by a scale of $\sqrt{n}$. For $n = 8192$, $\sqrt{n} \approx 90.5$. This means the RMSNorm layer applies a
**100x**
magnification to the output. In large-scale pretraining, we find this leads to massive gradients and numerical instability.

A typical phenomenon is that when DIFF V1 is pre-trained at a large learning rate, the gradient norm experiences a larger increase compared to Transformer in the later stages, along with higher variance.
**In DIFF V2, after removing the per-head RMSNorm, the gradient norm scale becomes comparable to that of Transformer, and the gradient norm spike is reduced**
(will be discussed further below).

We adopted the per-head RMSNorm design in DIFF V1 primarily because of the doubled value head dimension and the globally shared $\lambda$ across all tokens. Given the modifications made to these two aspects in DIFF V2, we found that removing RMSNorm is now safe.

### **Beyond Softmax Constraint & Elimination of Attention Sinks**

We demonstrate DIFF V2 can overcome the constraint of Softmax mentioned above. It can also help eliminate
[attention sinks](https://arxiv.org/abs/2309.17453)
.

* In original Softmax attention:

a


i

j

=

Softmax

(


z


i

j

)

=



exp

⁡

(


z


i

j

)



∑


k

=

1

n

exp

⁡

(


z


i

k

)




c

i

=


∑


j

=

1

n


a


i

j


v

j

=


∑


j

=

1

n

Softmax

(


z


i

j

)


v

j



RMS

(


c

i

)

∈


[


1


n

,

1

)
a\_{ij} = \text{Softmax}(z\_{ij}) = \frac{\exp(z\_{ij})}{\sum\_{k=1}^{n} \exp(z\_{ik})} \\
\mathbf{c}\_i = \sum\_{j=1}^{n} a\_{ij} \mathbf{v}\_j = \sum\_{j=1}^{n} \text{Softmax}(z\_{ij}) \mathbf{v}\_j \\
\text{RMS}(\mathbf{c}\_i) \in \left[\frac{1}{\sqrt{n}},1\right)






a










ij

​




=






Softmax

(


z










ij

​


)



=

















∑










k

=

1






n

​




exp

(


z










ik

​


)











exp

(


z










ij

​


)

​








c









i

​




=














j

=

1





∑






n

​





a










ij

​



v









j

​




=














j

=

1





∑






n

​





Softmax

(


z










ij

​


)


v









j

​








RMS

(


c









i

​


)



∈







[




















n


​












1

​


,



1


)

* In DIFF V2 we introduce a projected $\lambda$ for each token and each head:

c

i

=


∑


j

=

1

n


(

Softmax

(


z


i

j

1

)

−

sigmoid

(


λ

i

)

⋅

Softmax

(


z


i

j

2

)

)


v

j



RMS

(


c

i

)

∈


(

0

,


2

)
\mathbf{c}\_i = \sum\_{j=1}^{n} \left( \text{Softmax}(z\_{ij}^\text{1}) - \text{sigmoid}(\lambda\_i) \cdot \text{Softmax}(z\_{ij}^\text{2}) \right) \mathbf{v}\_j \\
\text{RMS}(\mathbf{c}\_i) \in \left(0, \sqrt{2}\right)






c









i

​




=














j

=

1





∑






n

​






(


Softmax

(


z










ij






1

​


)



−




sigmoid

(


λ









i

​


)



⋅




Softmax

(


z










ij






2

​


)


)




v









j

​








RMS

(


c









i

​


)



∈







(

0

,











2


​



)

The projected $\lambda\_i$ helps to control the context RMS. We observe that
**lowering the lower bound of the context RMS to zero is particularly important**
.
**It can help eliminate attention sinks and improve training stability**
. The upper bound only needs to remain bounded.

Note that our analysis here consider RMS before output projection $W\_O$. Although the RMS can be recovered and adjusted after the output projection, the lack of freedom at Softmax still affects the learning performance.

Other recent works alleviate this constraint as well:

a


i

j

off

=



exp

⁡

(


z


i

j

)


1

+


∑


k

=

1

n

exp

⁡

(


z


i

k

)








c

i

=


∑


j

=

1

n


a


i

j

off


v

j

=




∑


k

=

1

n

exp

⁡

(


z


i

k

)


1

+


∑


k

=

1

n

exp

⁡

(


z


i

k

)


∑


j

=

1

n

Softmax

(


z


i

j

)


v

j







RMS

(


c

i

)

∈


(

0

,

1

)
a\_{ij}^{\text{off}} = \frac{\exp(z\_{ij})}{1 + \sum\_{k=1}^{n} \exp(z\_{ik})} \\
\ \\
\mathbf{c}\_i = \sum\_{j=1}^{n} a\_{ij}^{\text{off}} \mathbf{v}\_j = \frac{\sum\_{k=1}^{n} \exp(z\_{ik})}{1 + \sum\_{k=1}^{n} \exp(z\_{ik})} \sum\_{j=1}^{n} \text{Softmax}(z\_{ij}) \mathbf{v}\_j \\
\ \\
\text{RMS}(\mathbf{c}\_i) \in \left(0, 1\right)






a










ij







off

​




=
















1



+




∑










k

=

1






n

​




exp

(


z










ik

​


)











exp

(


z










ij

​


)

​
















c









i

​




=














j

=

1





∑






n

​





a










ij







off

​



v









j

​




=
















1



+




∑










k

=

1






n

​




exp

(


z










ik

​


)












∑










k

=

1






n

​




exp

(


z










ik

​


)

​













j

=

1





∑






n

​





Softmax

(


z










ij

​


)


v









j

​
















RMS

(


c









i

​


)



∈






(

0

,



1

)

* In
  [gpt-oss](https://openai.com/index/introducing-gpt-oss/)
  , a learnable scalar $s$ is introduced for each head:

a


i

j

oss

=



exp

⁡

(


z


i

j

)


exp

⁡

(

s

)

+


∑


k

=

1

n

exp

⁡

(


z


i

k

)








c

i

=


∑


j

=

1

n


a


i

j

oss


v

j

=




∑


k

=

1

n

exp

⁡

(


z


i

k

)


exp

⁡

(

s

)

+


∑


k

=

1

n

exp

⁡

(


z


i

k

)


∑


j

=

1

n

Softmax

(


z


i

j

)


v

j







RMS

(


c

i

)

∈


(

0

,

1

)
a\_{ij}^{\text{oss}} = \frac{\exp(z\_{ij})}{\exp(s) + \sum\_{k=1}^{n} \exp(z\_{ik})} \\
\ \\
\mathbf{c}\_i = \sum\_{j=1}^{n} a\_{ij}^{\text{oss}} \mathbf{v}\_j = \frac{\sum\_{k=1}^{n} \exp(z\_{ik})}{\exp(s) + \sum\_{k=1}^{n} \exp(z\_{ik})} \sum\_{j=1}^{n} \text{Softmax}(z\_{ij}) \mathbf{v}\_j \\
\ \\
\text{RMS}(\mathbf{c}\_i) \in \left(0, 1\right)






a










ij







oss

​




=
















exp

(

s

)



+




∑










k

=

1






n

​




exp

(


z










ik

​


)











exp

(


z










ij

​


)

​
















c









i

​




=














j

=

1





∑






n

​





a










ij







oss

​



v









j

​




=
















exp

(

s

)



+




∑










k

=

1






n

​




exp

(


z










ik

​


)












∑










k

=

1






n

​




exp

(


z










ik

​


)

​













j

=

1





∑






n

​





Softmax

(


z










ij

​


)


v









j

​
















RMS

(


c









i

​


)



∈






(

0

,



1

)

c

i

=

sigmoid

(


g

i

)

⊙


∑


j

=

1

n

Softmax

(


z


i

j

)


v

j



RMS

(


c

i

)

∈


(

0

,

1

)
\mathbf{c}\_i = \text{sigmoid} (\mathbf{g}\_i) \odot \sum\_{j=1}^{n} \text{Softmax}(z\_{ij}) \mathbf{v}\_j \\
\text{RMS}(\mathbf{c}\_i) \in \left(0, 1\right)






c









i

​




=






sigmoid

(


g









i

​


)



⊙














j

=

1





∑






n

​





Softmax

(


z










ij

​


)


v









j

​








RMS

(


c









i

​


)



∈






(

0

,



1

)

## Experimental Observations

We conduct pretraining experiments on production-scale LLMs, including dense models and a 30A3 MoE on trillions of tokens using large learning rate of 6e-4 to 1e-3.

The experiments are still running. What we have observed now:

* **Notably lower language modeling loss**
  compared to Transformer (a gap of 0.02 to 0.03).
* **Reduced loss and gradient spikes during training**
  , particularly under large learning rate settings where the Transformer baseline becomes unstable.
* **Reduced activation outliers magnitude.**

We expect to explore in later stages of training:

* Learning efficiency in mid- and post-training.
* Performance on downstream long-context benchmarks (alleviating context rot).

## Discussions

### Construction of Differential Operation

In theory, a standard Transformer with $2h$ attention heads can learn the differential operation by learning $W\_O^{2i}=-W\_O^{2i+1}, i=0,1,\ldots,h-1$, where $W\_O^{i}$ denotes the output projection of head $i$, and head $2i$ and $2i+1$ belong to the same GQA group.

**Assumption 1.**
In practice, such a solution is difficult to learn through optimization, as it requires two sets of parameters to converge to exact negatives of each other.

**Assumption 2.**
The differential operation can be learned by the model and the model chooses to learn it in the training.
**Then explicitly constructing it before the output projection as in DIFF V2 can save half of the $W\_O$ parameters**
. The number of saved parameters is also non-trivial. Under the current GQA setting, the parameters in the attention module are dominated by $W\_Q$ and $W\_O$; Therefore, approximately
**25% of the attention-module parameters can be saved.**
The saved parameter budget can then be reallocated to other parts of the model.

Even if DIFF V2, after reallocating parameters, does not achieve a lower loss than the baseline but merely matches it,
**the method is still worthwhile if it provides additional benefits**
such as improved training stability, better control of outliers, or higher training efficiency. This is analogous to
[GQA](https://arxiv.org/abs/2305.13245)
, which matches the loss of MHA while reducing KV-cache as an additional benefit. So the key question becomes empirical performance.

### Design Ablations

1. Subtracting two heads that are
   **not**
   in the same GQA group, which means they
   **do not**
   share the same key and value.

(For simplicity, we omit the batch dimension and assume that both the input and output of the following
`flash_attn_func`
are three-dimensional tensors
`(tokens, heads, head dimension)`
. Heads belonging to the same GQA group are arranged contiguously in the output)

```
...
attn = flash_attn_func(q, k, v)
nh = attn.size(1)
attn1, attn2 = (attn[:, :nh//2],
                    attn[:, nh//2:])
...
```

```
...
attn = flash_attn_func(q, k, v)

attn1, attn2 = (attn[:, 0::2],
                    attn[:, 1::2])
...
```

In our large learning rate setting, the ablation 1 setting exhibits obvious training instability (much more loss and gradient spikes) and higher loss comparing to DIFF V2. The value should be shared in the two subtraction heads to construct differential operation, as discussed in DIFF V1 paper.

1. Subtracting two attention maps without $\lambda$ scaling factor, i.e.,
   `attn1 - attn2`
   instead of
   `attn1 - lam_val * attn2`
   . This results in an excessively small context RMS at initialization.
2. Directly using projected $\lambda$ without applying
   `sigmoid`
   operation. The context RMS is unbounded from above.

Both ablation 2 and ablation 3 lead to higher language modeling loss than DIFF V2. Ablation 2 maintains training stability similar to DIFF V2, whereas ablation 3 is less stable (still more stable than ablation 1).

### Miscellaneous

* In DIFF, the outliers in qk logits can be smaller than those in the baseline. This was already analyzed in DIFF V1: DIFF can achieve attention sparsity comparable to the baseline while using smaller qk logits. We further propose that DIFF’s differential mechanism, which cancels out small attention values,
  **may help mitigate the attention rounding error issue discussed in this
  [blog](https://spaces.ac.cn/archives/11371)
  and
  [paper](https://arxiv.org/abs/2510.04212)**
  .
* **DIFF V2 is compatible with sparse attention**
  . In many existing sparse attention frameworks, query heads within the same GQA group are required to attend to the same key-value blocks in order to maximize speedup. A common strategy is to select key-value blocks based on the average attention logits across heads.
  For DIFF V2, the problem shifts to designing an effective block-selection strategy for a larger GQA group that contains pairs of differential heads. This may require handling the two types of differential heads separately during selection, or maybe a simple average of attention logits might already be sufficient in practice. Conceptually, this does not introduce any fundamental differences compared to block sparse attention of standard Transformers.