---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-17T18:15:42.857180+00:00'
exported_at: '2026-04-17T18:15:45.471700+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/nemotron-ocr-v2
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: Building a Fast Multilingual OCR Model with Synthetic Data
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/nemotron-ocr-v2
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Building a Fast Multilingual OCR Model with Synthetic Data
updated_at: '2026-04-17T18:15:42.857180+00:00'
url_hash: a51525335ebcd3126ced5af03bd6b19ba50febdd
---

# Building a Fast Multilingual OCR Model with Synthetic Data

Training a high-quality OCR model requires a large quantity of annotated image-text pairs: images with precise bounding boxes, transcriptions, and ideally reading order information at the word, line, and paragraph level. Every approach to curating this data comes with tradeoffs. Existing benchmark datasets like ICDAR and Total-Text have clean labels but limited scale, typically tens of thousands of images skewed toward English and Chinese. Manual annotation produces the highest quality labels but is expensive and slow, making it impractical at the millions-of-images scale needed for robust multilingual models. Web-scraped PDFs offer enormous quantity, but the embedded text is often noisy: characters recorded as individual strokes instead of words, text baked into images with no extractable layer, or scanned pages where a weak OCR model was applied and the resulting text layer is unreliable. You can extract usable signal from web PDFs, but it takes significant filtering effort and the result is never perfectly clean.

Synthetic data generation offers a way out of these tradeoffs. By rendering text onto images programmatically, we get both the scale of web scraping and the label purity of hand annotation. Every bounding box, transcription, and reading order relationship is known exactly because we placed it there, and we have full control over which layouts, font styles, and edge cases appear in the training set. The challenge is realism. Simulating diverse layouts and realistic document scenarios is difficult, but with the right rendering engine and strong randomization across fonts, colors, backgrounds, augmentations, and layout structures, it is possible to build enough invariance that models trained on synthetic data generalize well to real-world documents.

Using this approach, we built
[**Nemotron OCR v2**](https://huggingface.co/nvidia/nemotron-ocr-v2)
, a multilingual OCR model that is both accurate and fast. Accuracy is driven by data: 12 million synthetic training images across six languages brought NED scores from 0.56–0.92 down to 0.035–0.069 on non-English languages. Speed is driven by architecture: a shared detection backbone whose features are reused by both the recognizer and relational model, eliminating redundant computation and enabling 34.7 pages/second on a single A100 GPU. The synthetic data pipeline is generic enough to extend to any language for which fonts and source text exist.

The dataset is publicly available at
[nvidia/OCR-Synthetic-Multilingual-v1](https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1)
and the model at
[nvidia/nemotron-ocr-v2](https://huggingface.co/nvidia/nemotron-ocr-v2)
. You can try the model directly in the browser at the
[Nemotron OCR v2 demo](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2)
.

[![Nemotron OCR v2 HuggingFace Space demo showing detected text regions and extracted text](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/Screenshot%202026-04-09%20at%202.59.12%E2%80%AFPM.png)](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/Screenshot%202026-04-09%20at%202.59.12%E2%80%AFPM.png)

---

## The Problem: Data, Not Architecture

Nemotron OCR v1 was a strong English OCR model, but it was not trained for multilingual purposes so when exposed to other languages it failed to read the documents accurately. On our SynthDoG benchmark, v1 produced Normalized Edit Distance (NED) scores between 0.56 and 0.92 for Japanese, Korean, Russian, and Chinese. At these error rates, the model output bears little resemblance to the ground truth.

| Language | Nemotron OCR v1 NED |
| --- | --- |
| Japanese | 0.723 |
| Korean | 0.923 |
| Russian | 0.564 |
| Chinese (Simplified) | 0.784 |
| Chinese (Traditional) | 0.700 |

Part of the issue was the character set. The v1 model supported only 855 characters, which simply did not cover CJK (Chinese, Japanese, Korean) or Cyrillic scripts. We ran an experiment where we expanded the character set to 14,244 characters to cover all the target languages. This helped slightly, but without sufficient training data actually containing those characters, the improvement was marginal. The model could theoretically output the right characters, but it had never learned what they looked like. The bottleneck was data, not architecture.

Collecting and annotating millions of real-world images across six languages with word-, line-, and paragraph-level bounding boxes plus reading order graphs would be prohibitively expensive. We needed a different approach.

---

## A Generic Synthetic Data Pipeline

Our key insight is that the recipe for multilingual OCR training data is fundamentally
**language-agnostic**
. You need two ingredients:

1. **Source text**
   in the target language, drawn from a realistic distribution
2. **Fonts**
   that can render that language's script

Given those, a synthetic renderer can produce unlimited annotated training images with pixel-perfect ground truth at every level of granularity for free.

### Text: mOSCAR

For source text, we use
[mOSCAR](https://huggingface.co/datasets/oscar-corpus/mOSCAR)
, a large-scale multilingual web corpus covering
**163 language subsets**
across dozens of scripts including Latin, CJK, Cyrillic, Arabic, Devanagari, and Thai. Sampling from mOSCAR gives us text that follows a realistic distribution of vocabulary, sentence length, and character frequency for each language. This is far more representative than dictionary word lists or machine-generated text.

### Rendering: Modified SynthDoG

We built our pipeline on a heavily modified version of
[SynthDoG](https://github.com/clovaai/donut/tree/master/synthdog)
(Synthetic Document Generator) from the Donut project. The original SynthDoG generates document-like images with page-level text labels. We extended it in several important ways.

**Multi-level bounding boxes.**
Vanilla SynthDoG provides only page-level text. Our pipeline generates pixel-precise annotations at three levels simultaneously: word, line, and paragraph. Each level includes both axis-aligned bounding boxes and 4-point quads, with indices linking words to their parent lines and paragraphs.

**Relation graph for reading order.**
Most publicly available OCR datasets do not include reading order annotations. This makes it hard to train models that understand document structure beyond just detecting text. We took inspiration from the
[HierText](https://github.com/google-research-datasets/hiertext)
dataset, which pioneered hierarchical (word, line, paragraph) annotations with structural relationships. Our synthetic pipeline generates a relation graph for every sample, encoding which words compose each line, which lines compose each paragraph, and in what order they should be read. This is what powers the relational model component of Nemotron OCR v2, which handles multi-column layouts, tables, and other structures where a simple top-to-bottom, left-to-right merge would produce garbled output.

**Diverse layout modes.**
We created a set of layout templates that cover a range of real-world document scenarios: flowing multi-column text, scattered scene-text-like words, vertical text columns (important for Japanese and Chinese), tables with headers and borders, table-of-contents pages with dot leaders, PowerPoint-style slides, and Word-document-style pages with headings and body text. Each generation run randomly selects a layout mode, so the model sees a wide variety of structures during training.

**Line-level recognition for CJK.**
An important design decision for the multilingual variant was moving from word-level to line-level text recognition. Languages like Chinese and Japanese do not use spaces between words, so there is no natural word boundary to segment on. Korean uses spaces inconsistently. By operating at the line level, the recognizer handles these languages naturally without needing a separate word segmentation step. The English variant continues to use word-level recognition where it makes sense.

**Open-source font pool.**
We assembled 165 to 1,258 unique fonts per language from open-source collections including Google Fonts and the Noto family, covering serif, sans-serif, handwritten, decorative, and variable-weight styles.

**Augmentations.**
Each rendered page goes through a stack of randomized augmentations to improve generalization. At the text level, these include border/outline effects, drop shadows, extrusion, and sprinkle noise on glyph edges. Custom effects modulate stroke opacity and stroke width variation across text using random fields. At the image level, we apply morphological operations (dilation, erosion), median blur, and elastic distortion, gated by a minimum text height to avoid destroying small text. At the full-page level, the pipeline applies contrast and brightness jitter, Gaussian and motion blur, color shifting, shadow overlays, and additive Gaussian noise. Backgrounds are either image textures or solid colors, with optional semi-transparent tinted rectangles behind individual words or lines.

---

## What the Data Looks Like

Here is a sample of raw synthetic images across all six languages. Each image is generated with a random layout mode, font selection, background, and augmentation stack:

[![Mosaic of synthetic training images across all languages](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/mosaic_raw.jpg)](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/mosaic_raw.jpg)

Below is an annotated example showing the hierarchical structure. Dashed outlines indicate paragraph boundaries, shaded regions show line-level groupings (colored by paragraph), and arrows trace the reading order between lines within each paragraph.

[![English paragraph layout with reading order annotations](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/en_5078_full_annotation.png)](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/en_5078_full_annotation.png)

Here are more annotated examples across languages showing the range of layouts, scripts, and augmentation styles the pipeline produces. Each subtitle describes what the example highlights:

[![Annotated examples across languages and layout types](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/examples_collage.jpg)](https://huggingface.co/spaces/nvidia/nemotron-ocr-v2/resolve/main/examples_collage.jpg)

---

## Dataset at a Glance

The full dataset contains
**12.2 million samples**
across six languages:

| Language | Total Samples | Train | Test | Validation |
| --- | --- | --- | --- | --- |
| English | 1,825,089 | 1,460,304 | 183,629 | 181,156 |
| Japanese | 1,889,137 | 1,502,712 | 193,779 | 192,646 |
| Korean | 2,269,540 | 1,814,994 | 227,091 | 227,455 |
| Russian | 1,724,733 | 1,380,404 | 171,678 | 172,651 |
| Chinese (Simplified) | 2,335,343 | 1,914,948 | 210,143 | 210,252 |
| Chinese (Traditional) | 2,214,304 | 1,772,280 | 221,867 | 220,157 |
| **Total** | **12,258,146** | **9,845,642** | **1,208,187** | **1,204,317** |

Download:
[nvidia/OCR-Synthetic-Multilingual-v1](https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1)

---

## Extensibility

The pipeline we have described is deliberately generic. We chose six languages for this release, but adding a new language only requires source text and fonts that cover the script. No changes to the model architecture or manual annotation are needed. The rendering pipeline can generate millions of annotated pages per day on a single machine, making it practical to produce large-scale training sets for new languages quickly. With mOSCAR covering 163 language subsets and the Noto font family supporting virtually every Unicode script in active use, there is a clear path to scaling this approach broadly.

---

## The Model: Nemotron OCR v2

[Nemotron OCR v2](https://huggingface.co/nvidia/nemotron-ocr-v2)
is a production-ready, commercially usable OCR model trained on this synthetic data along with approximately 680K real-world images. It uses a three-component end-to-end architecture:

* **Text Detector**
  (RegNetX-8GF backbone): localizes text regions in the image
* **Text Recognizer**
  (pre-norm Transformer): transcribes detected regions
* **Relational Model**
  : predicts logical groupings, reading order, and layout relationships

Two variants are available:

|  | v2\_english | v2\_multilingual |
| --- | --- | --- |
| Languages | English | EN, ZH, JA, KO, RU |
| Region level | Word | Line |
| Recognizer layers | 3 | 6 |
| Character set | 855 | 14,244 |
| Parameters | 54M | 84M |

An important distinction from other OCR pipelines:
**Nemotron OCR v2 multilingual is a single unified model**
that handles all five languages simultaneously. You do not need to know the document language ahead of time or select a language-specific variant. By contrast, pipeline tools like PP-OCR v5 (PaddleOCR) and OpenOCR offer specialized per-language models that perform well on their target language but require you to either detect the language first or fall back to a base variant that is less capable across the board.

### Why the Model Is Fast

## The architecture is based on the [FOTS](https://arxiv.org/abs/1801.01671) (Fast Oriented Text Spotting) design, which unifies detection and recognition into a single network with a shared convolutional backbone. The detection backbone (RegNetX-8GF) processes the input image once and produces feature maps that are reused by all three components. The text recognizer receives rectified feature crops from detected regions and decodes them with a small Transformer. The relational model reasons over per-region embeddings derived from the same feature maps using a compact Transformer encoder. Because the expensive convolutional pass happens only once, the downstream components add minimal overhead. This feature reuse is what drives the model's efficiency, enabling 34.7 pages/second on a single A100 GPU.

## Results: What Synthetic Data Buys You

### Multilingual Benchmark (SynthDoG)

Normalized Edit Distance on SynthDoG-generated pages (lower is better). The v2 multilingual model, trained on our synthetic data, brings NED scores from unusable levels down to near-zero across all target languages:

| Language | PaddleOCR (base) | PaddleOCR (specialized) | OpenOCR (server) | Nemotron OCR v1 | **Nemotron OCR v2 (multi)** |
| --- | --- | --- | --- | --- | --- |
| English | 0.117 | 0.096 | 0.105 | 0.078 | **0.069** |
| Japanese | 0.201 | 0.201 | 0.586 | 0.723 | **0.046** |
| Korean | 0.943 | 0.133 | 0.837 | 0.923 | **0.047** |
| Russian | 0.959 | 0.163 | 0.950 | 0.564 | **0.043** |
| Chinese (Simplified) | 0.054 | 0.054 | 0.061 | 0.784 | **0.035** |
| Chinese (Traditional) | 0.094 | 0.094 | 0.127 | 0.700 | **0.065** |

Note that the "PaddleOCR (specialized)" column uses language-specific models (e.g., the Korean model for Korean), which is the best-case scenario when you already know the language. Nemotron OCR v2 multilingual achieves better results on this synthetic data than even these specialized variants across all languages, using a single model.

### Real-World Benchmark (OmniDocBench)

On OmniDocBench, a real-world document OCR benchmark with English, Chinese, and mixed-language content, Nemotron OCR v2 multilingual achieves competitive accuracy at
**34.7 pages/second**
, over 28x faster than PaddleOCR v5:

| Model | pages/s | EN | ZH | Mixed |
| --- | --- | --- | --- | --- |
| PaddleOCR v5 (server) | 1.2 | 0.027 | 0.037 | 0.041 |
| OpenOCR (server) | 1.5 | 0.024 | 0.033 | 0.049 |
| **Nemotron OCR v2 (multi)** | **34.7** | **0.048** | **0.072** | **0.142** |
| *Nemotron OCR v2 (EN)* | *40.7* | *0.038* | *0.830* | *0.437* |
| EasyOCR | 0.4 | 0.095 | 0.117 | 0.326 |
| Nemotron OCR v1 | 39.3 | 0.038 | 0.876 | 0.436 |

NED scores (lower is better). Speed measured on a single A100 GPU with the v2 batched pipeline. All comparison models were benchmarked using their default detector + recognizer pipeline with optional extras disabled.

A note on the speed differences between variants: v1 and v2 English are faster than v2 multilingual because the multilingual recognizer is larger (6 Transformer layers with a 14,244-token vocabulary vs 3 layers with 855 tokens). The recognizer processes every detected text region, so a heavier recognizer directly impacts throughput on text-dense pages. The v2 english model is slightly faster than v1 because the backbone has been swapped from RegNetY to RegNetX.

---

## Links

## Acknowledgments

Thank you to Bo Liu, Théo Viel and Mike Ranzinger for contributing code, strategy and additional validation to this work.