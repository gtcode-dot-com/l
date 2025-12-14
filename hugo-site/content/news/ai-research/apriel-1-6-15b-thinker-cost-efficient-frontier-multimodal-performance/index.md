---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-14T00:03:28.802239+00:00'
exported_at: '2025-12-14T00:03:32.172378+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/ServiceNow-AI/apriel-1p6-15b-thinker
structured_data:
  about: []
  author: ''
  description: A Blog post by ServiceNow-AI on Hugging Face
  headline: 'Apriel-1.6-15b-Thinker: Cost-efficient Frontier Multimodal Performance'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/ServiceNow-AI/apriel-1p6-15b-thinker
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Apriel-1.6-15b-Thinker: Cost-efficient Frontier Multimodal Performance'
updated_at: '2025-12-14T00:03:28.802239+00:00'
url_hash: 2458b809ec27770c6e780493b411ad15afe6674c
---

# Apriel-1.6-15b-Thinker: Cost-efficient Frontier Multimodal Performance

We release

[Apriel-1.6-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-1.6-15b-Thinker)

, a 15-billion parameter multimodal reasoning model in ServiceNow’s Apriel SLM series which achieves SOTA performance against models 10 times it's size. Apriel-1.6 builds on top of

[Apriel-1.5-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-1.5-15b-Thinker)

with an extensive focus on improving text and vision reasoning, while improving token efficiency. This version was trained on NVIDIA DGX™ Cloud with GB200 Grace™ Blackwell Superchips.

Apriel-1.6 scores 57 on the
[Artificial Analysis Index](https://artificialanalysis.ai/)
, outperforming models like Gemini 2.5 Flash, Claude Haiku 4.5 and GPT OSS 20b. It obtains a score on par with Qwen3 235B A22B, while being signficantly more efficient. This new release improves or maintains task performance in comparison with the previous Apriel-1.5-15B-Thinker [1], while reducing reasoning token usage by more than 30%.

[![Artificial Analysis Intelligence Index (30 Nov '25)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/liUuJ-2ZPz_xtHEgq4wN2.png)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/liUuJ-2ZPz_xtHEgq4wN2.png)

## Mid-Training

We follow the same overall training process used for Apriel-1.5-15B-Thinker, which includes a depth-upscaling phase followed by two Continual Pretraining (CPT) stages (detailed in [1]). The depth-upscaling corpus consists of 35% data from diverse sources, including high-quality web content, scientific and technical literature, mathematical problem sets, and programming code; 15% high-quality datasets from NVIDIA Nemotron™; and the remaining 50% pretraining-style data serving as replay.

For Apriel-1.6-15B-Thinker, we expand the Stage-1 CPT mixture, which focuses on strengthening textual reasoning and image understanding, with additional text-only samples and image-text pairs. The new text data is fully synthetic, covering general reasoning, knowledge, coding, and creative writing, while the multimodal portion spans document and chart understanding, OCR, visual-reasoning tasks, and SVG/web-code synthesis.

Following Stage-1, we perform a text-only CPT run at an extended 49K sequence length and then run Stage 2 to further refine the model’s visual-reasoning capabilities. This combination produced a strong base model that provided a solid foundation for subsequent post-training. Training for this mid-training pipeline required approximately 10,000 GPU hours on NVIDIA's GB200s, a small compute footprint enabled by their high throughput and aligned with our goal of building strong models with limited resources through careful data strategy and training methodology.

## Post-Training

Using the midtrained model, we perform post-training following a pipeline that consists of large scale Supervised Finetuning (SFT) and Reinforcement Learning (RL) targeting both vision and text abilities.

### Supervised Finetuning (SFT)

Our Supervised Fine-Tuning (SFT) stage focuses on improving the reasoning quality of Apriel-1.6 by training on a meticulously curated dataset of 2.4 million high-signal text samples. Each example includes explicit, step-by-step reasoning traces, enabling the model to internalize transparent reasoning processes rather than merely reproducing final answers.

To construct this dataset, we combined execution-verifiable synthetic samples for math, coding, and scientific problem-solving with a broad mix of instruction-following, conversational, API/function-calling, creative writing, safety, and other knowledge-intensive samples. Data quality was treated as a first-class priority: every sample passed through multi-stage de-duplication, content filtering, heuristic quality pruning, LLM-as-Judge validation, execution-based verification (where applicable), and strict decontamination against evaluation benchmarks.

SFT was carried out in two phases, both trained at a 32K context length. In the first phase, we ran a large-scale text-only training run on the 2.4M samples for 4 epochs. Compared to Apriel-1.5-15b-Thinker, we simplified the chat template by removing redundant tags and introduced four special tokens to the tokenizer (
`<tool_calls>`
,
`</tool_calls>`
,
`[BEGIN FINAL RESPONSE]`
,
`<|end|>`
) for easier output parsing.

The second phase was a lightweight, multimodal run trained for 3 epochs, using rejection-sampled data from Apriel-1.5-15b-Thinker to ensure the model maintained strong performance on image inputs after the introduction of these special tokens, while also preparing it for downstream RL stages.

This approach provided us with a robust, high-quality SFT foundation on top of which our RL pipeline could operate effectively. The resulting model exhibits strong multimodal understanding, improved text reasoning capabilities, and enhanced agentic behavior.

### Reinforcement Learning (RL)

We adopt a multi-stage RL setup that focuses on simultaneously improving reasoning capability and efficiency.
We train the model on image domains such as visual reasoning, general visual question answering (VQA) and optical character recognition (OCR). Our training data also consists of data across different domains, such as simple questions (to encourage short, direct answers on easy queries), math (numerical reasoning), STEM (multiple-choice scientific questions), and function calling (structured tool use).

Rewards are given for correctness of the response, along with penalties for undesirable behaviour, such as verbosity, incorrect formats, etc. Overall, our setup is designed to improve the model’s reasoning ability while using fewer reasoning tokens, encouraging it to avoid unnecessary intermediate steps, stop earlier when confident, and answer more directly for simpler queries.

Training is done with the Group Sequence Policy Optimization loss (GSPO) [2] using the
[VeRL](https://github.com/volcengine/verl)
framework and rule-based verification.

## Evaluation

### Text Evaluation

We evaluate Apriel-1.6 on various domains such as tool use, math, coding, instruction following and long context.

\* This score is with
[DCA](https://arxiv.org/pdf/2402.17463)
enabled. Without this, the model scores 36.

\*\* The average score is calculated using all benchmarks except BFCL v3 Only and DeepResearchBench, since some models do not have scores for these two benchmarks.

\*\*\* AA LCR score for o3-mini-high is projected score based on its AA Index score.

### Image Evaluation

We evaluate the Apriel-1.6 model on a representative set of evaluations with the prime focus on mathematical reasoning, visual question answering, logical reasoning, STEM related tasks and chart based reasoning. All evaluations are done using VLMEvalkit. Apriel-1.6 improves on its predecessor by
**4 points**
on the average of 13 benchmarks of the
**Image Index**
comprising of the following benchmarks: MathVision, MathVista, MMMU (validation), MMMU-Pro (10 choice COT), MMMU-Pro (Vision only COT), MathVerse (Vision Dominant), MathVerse (Text Dominant), MMStar, BLINK, LogicVista, CharXiV (descriptive), CharXiV (reasoning), AI2D (test).

[![Performance on the Image Index](https://cdn-uploads.huggingface.co/production/uploads/65036ffdb96045f918094fd6/B5PogpJIui7vGsZ7xx-jH.png)](https://cdn-uploads.huggingface.co/production/uploads/65036ffdb96045f918094fd6/B5PogpJIui7vGsZ7xx-jH.png)

## Cost-Efficient Frontier Performance

[![Intelligence vs Total Parameters (30 Nov '25)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/q2Y4Xjp9Sy5dma9wFt7Ny.png)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/q2Y4Xjp9Sy5dma9wFt7Ny.png)

Apriel-1.6-15B-Thinker sits in the sweet spot of the cost-efficient frontier. It delivers intelligence scores that rival or surpass much larger models while using only 15B parameters. On the chart, it’s firmly inside the
***most attractive***
quadrant, balancing efficiency with top-tier reasoning. In practice, this means Apriel-1.6-15B-Thinker offers strong performance and deep reasoning at a fraction of the compute and deployment cost of heavyweight competitors, making it an exceptionally efficient choice for the real-world, especially in enterprise applications.

[![Intelligence vs Output Tokens Used in Artificial Analysis Intelligence Index (30 Nov '25)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/QoymhuGcJf6lFAIruUQ2p.png)](https://cdn-uploads.huggingface.co/production/uploads/614cf0be2c0ca05fbc33a827/QoymhuGcJf6lFAIruUQ2p.png)

Our post-training focuses heavily on improving reasoning-token efficiency. The image above showing intelligence score against token usage highlights the effectiveness of our post-training. Apriel-1.6-15B-Thinker again lands in
***most attractive***
quadrant. The model reaches a high Artificial Analysis Intelligence Index score while using far fewer tokens than many similarly capable or larger models. In comparison to Apriel-1.5-15b-Thinker [1], we reduce token usage by over 30%.

Overall, Apriel-1.6 is a highly-capable reasoner, that maintains memory and efficiency characteristics required for enterprise deployment.

## Notes and Limitations

We are a small lab with big goals. While we are not GPU poor, our lab, in comparison has a tiny fraction of the compute available to other Frontier labs. Our goal with this work is to show that a SOTA model can be built with limited resources if you have the right data, design and solid methodology.

We set out to build a small but powerful model, aiming for capabilities on par with frontier models. Developing a 15B model with this level of performance requires tradeoffs, so we prioritized getting SOTA-level performance and improving reasoning token efficiency.

This model is trained to perform extensive reasoning for difficult questions and less reasoning effort for simpler questions. We are always actively working to make our models more efficient and concise in future releases.

The model has a few vision-related limitations to be aware of. Complex or low-quality images can reduce OCR accuracy, dense scenes (like crowds or many similar objects) can make subtle details and counting more challenging, and highly detailed or unusually formatted charts may occasionally lead to imperfect interpretations. It may also be less precise with fine-grained visual grounding, so bounding-box predictions can sometimes be approximate or inconsistent.

## References

[1] Radhakrishna, S., Tiwari, A., Shukla, A., Hashemi, M., Maheshwary, R., Malay, S.K.R., Mehta, J., Pattnaik, P., Mittal, S., Slimi, K., Ogueji, K., Oladipo, A., Parikh, S., Bamgbose, O., Liang, T., Masry, A., Mahajan, K., Mudumba, S.R., Yadav, V., Madhusudhan, S.T., Scholak, T., Davasam, S., Sunkara, S. and Chapados, N., 2025. Apriel-1.5-15b-Thinker. arXiv preprint arXiv:2510.01141.

[2] Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J. and Lin, J., 2025. Group Sequence Policy Optimization. arXiv preprint arXiv:2507.18071.

## Contributors

### Training

Shruthan Radhakrishna, Aman Tiwari, Jash Mehta, Toby Liang, Kelechi Ogueji, Akintunde Oladipo, Masoud Hashemi, Rishabh Maheshwary, Pulkit Pattnaik, Saloni Mittal, Khalil Slimi, Akshay Kalkunte, Shiva Krishna Reddy Malay

### Benchmarking & Evaluation

Aanjaneya Shukla, Oluwanifemi Bamgbose, Massimo Caccia, Dheeraj Vattikonda, Jishnu S Nair, Varun Pandey, Shashank Maiya, Dhruv Jhamb, Nicolas Gontier, Patrice Bechard, Tayfun Tuna, Kavya Sriram, Denis Akhiyarov, Hari Subramani, Tara Bogavelli

### Leads and Management

Sathwik Tejaswi Madhusudhan, Torsten Scholak, Sagar Davasam, Srinivas Sunkara