---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-02T03:16:28.518115+00:00'
exported_at: '2026-03-02T03:16:30.505916+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/nemotron-nano-9b-v2-japanese-ja
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: 'NVIDIA Nemotron 2 Nano 9B Japanese: 日本のソブリンAIを支える最先端小規模言語モデル'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/nemotron-nano-9b-v2-japanese-ja
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'NVIDIA Nemotron 2 Nano 9B Japanese: 日本のソブリンAIを支える最先端小規模言語モデル'
updated_at: '2026-03-02T03:16:28.518115+00:00'
url_hash: 5207df288bdf4dac920bba7536d53af62f23cc56
---

# NVIDIA Nemotron 2 Nano 9B Japanese: 日本のソブリンAIを支える最先端小規模言語モデル

[NVIDIA Nemotron](https://developer.nvidia.com/nemotron)

は、オープンモデルだけでなく、データセット、ライブラリ、レシピ、クックブックを提供し、開発者がモデルをカスタマイズし、多様なユースケースや言語に適応できるようにすることでソブリンAIを推進しています。

本日、NVIDIAは、
[Nejumi Leaderboard 4](https://wandb.ai/llm-leaderboard/nejumi-leaderboard4/reports/Nejumi-LLM-4--VmlldzoxMzc1OTk1MA)
のパラメータ数10B以下において、最先端の性能（SOTA）を達成した
[NVIDIA Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese)
を公開しました。

本モデルは、高度な日本語理解と強力なエージェント機能を、導入しやすい軽量なサイズで実現しており、日本のエンタープライズAI開発における重要なマイルストーンとなります。この成果は、実績ある
[Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2)
のアーキテクチャと、
[Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan)
によって実現された高品質な日本語合成データ生成（SDG）という、2つの重要な基盤の上に築かれています。

既に公開済みのNemotron 2 Nanoモデルを日本語向けにカスタマイズすることで、多様なユースケースや言語に対応したカスタム最先端モデルの開発・公開をコミュニティに促すことを目指しています。Nemotronチームは、このカスタマイズから得た知見を今後のNemotronリリースに反映し、日本語における推論能力の強化を図っています。

## **日本のエンタープライズにおけるSLM（小規模言語モデル）の重要性**

**日本のエンタープライズAIにおける重要なギャップ:**
現在の日本のエンタープライズAI環境には、「高度な日本語能力」と「エージェンティックAIとしてのタスク遂行能力」を兼ね備えたSLMがほとんど存在しないという課題があります。これにより、特に以下の点において導入の障壁が生じています。

**オンプレミスでのデプロイ要件:**
機密データを扱う企業では、プライベートネットワーク内でのモデル運用が不可欠です。10B（100億）パラメータ未満のモデルであれば、実用レベルの性能を維持しつつ、インフラ面の導入ハードルを大幅に下げることができます。

**カスタマイズの効率化:**
実証済みのエージェント能力を持つ強力な日本語ベースモデルから開始することで、ファインチューニングのサイクルを短縮できます。基礎能力の構築ではなく、特定のドメインへの適応に計算リソースを集中させることが可能になります。

**エージェント開発の加速:**
本モデルのアーキテクチャと性能により、大規模モデルのようなオーバーヘッドなしに、マルチエージェントシステムや複雑なワークフローの迅速なプロトタイピングが可能になります。

## **実績ある基盤の活用**

### Nemotron 2 Nano: 卓越したアーキテクチャ

Nemotron-Nano-9B-v2-Japanese は、英語ベンチマークにおいてサイズ対性能比で卓越した結果を示した NVIDIA Nemotron-Nano-9B-v2 をベースに構築されています。この効率的なアーキテクチャを基盤としてさらなるカスタマイズを実施し、日本語能力を強化しました。本アーキテクチャには以下の特長があります。

* 高度な推論能力を実現と最適化されたパラメータ効率
* 多言語適応のための強固な基盤
* 実証済みのエージェントタスク遂行能力

この検証済みのアーキテクチャを日本語に適応させることで、ベースモデルの強みを維持しつつ、優れた日本語能力を実現しています。

### Nemotron-Personas-Japan: 高品質な合成データ生成のシードセット

本モデルのデータ戦略は、オープンソース（CC BY 4.0）データセットである「
[Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan)
」を、合成データ生成（SDG）の高品質なシードとして活用することに焦点を当てています。このデータセットは、日本の実世界における人口統計、地理的分布、性格特性の分布に基づき合成生成されたペルソナで構成され、人口の多様性と豊かさを捉えています。こうした文化的に正確なペルソナを基盤として、高度に多様性があり、拡張性・堅牢性に優れたトレーニングパイプラインを構築しました。シードデータの豊富なペルソナ群により、多様なシナリオやニュアンスにわたる合成データセットを効率的に拡張できました。この手法により、拡張データは元のペルソナの厳密な文化的整合性を維持しつつ、最先端トレーニングに必要な規模を達成しています。

特にNemotron-Nano-9B-v2-Japaneseでは、これらのペルソナをツール呼び出しシナリオにおけるトレーニングデータの生成基盤として活用しました。これにより、モデルが獲得する能力が単なるツール呼び出し機能にとどまらず、文化的に適切な日本語の対話と現実世界のユースケースに根差したものであることが保証されます。

[Nemotron-Personas collection](https://huggingface.co/collections/nvidia/nemotron-personas)
には、米国、インド、シンガポール、ブラジルのデータセットも含まれており、同じ手法を地域を超えて再現することが可能となっています。

## **トレーニングパイプライン**

Nemotron-Nano-9B-v2-Japaneseは、継続事前学習、合成データ生成、事後学習に至るプロセスを日本語オープンソースコーパスとNVIDIAのNemotronスタックを組み合わせて構築されました。

[![training_diagram](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/uxrGpZ29BTHqQeD0_WQ5I.png)](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/uxrGpZ29BTHqQeD0_WQ5I.png)

### 継続事前学習

* Japanese OSS Corpus: Wikipedia, fineweb-2 Japanese, aozorabunko, sip3-ja-general-web-corpus
* Nemotron-CC-v2.1
* Nemotron-Pretraining-Specialized-v1

### SFT

* Nemotron-Personas-JapanをシードセットとしたTool Callingデータセット
* Nemotron-Post-Training-v3

### Nemotron-Nano-9B-v2-Japaneseに使用したソフトウェア

モデルの日本語能力を最大化するため、継続事前学習を実施しました。ここでは日本を代表するオープンソースLLMコミュニティである
[LLM-jp](https://llm-jp.nii.ac.jp/)
の資産を最大限に活用しています。同時に
[Nemotron Pre-training Datasets](https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets)
を活用し、モデルのエージェント機能を維持しました。

SFTに使用したNemotron-Personas-JapanをシードとしたTool Callingデータセットは非常に強力でした。性能向上はツール呼び出しに留まらず、日本語知識、QA、指示追従など多岐に渡りました。さらに、このシードセットが600万のペルソナに基づいて構築されているため、SDGを効果的にスケールさせることができました。これにより、重複を最小限に抑えながら、現実世界の多様なシナリオを網羅することに成功しました。
[Nemotron-Personas](https://huggingface.co/collections/nvidia/nemotron-personas)
コレクションは対象国を拡大しており、日本だけでなく他地域の開発者も同様のアプローチをとることができます。

モデルのトレーニングは、
[Nemotron Nano 2](https://arxiv.org/abs/2508.14444)
で確立されたトレーニングレシピを継承しています。これにより、トレーニングの不安定性を招くことなくスループットを向上させることができました。

このアプローチによって、ロバストなツール呼び出し機能とリーズニング能力を維持しながら強力な日本語言語モデルとしての性能を実現しています。

## **ベンチマークパフォーマンス**

[![leaderboard](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/5nuxnXClbAR3GI76KiG51.png)](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/5nuxnXClbAR3GI76KiG51.png)

Nemotron-Nano-9B-v2-Japanese は、日本で最も包括的なLLM評価プラットフォームである「Nejumi Leaderboard 4」において、10B未満のモデルカテゴリで1位を獲得しました。Nejumi Leaderboard は、以下の領域にわたる約40のベンチマークを通じてモデルを多角的に評価しています。

* 基礎的な言語能力: 日本語の理解と生成
* エージェント能力: コード生成、数学的推論、ツール利用など
* アライメント: 指示追従能力、バイアス、毒性、真実性、堅牢性など

これらの多次元的な評価により、Nejumi Leaderboard は、日本の環境においてカスタマイズや実運用のためのベースモデルを選定する開発者にとって、信頼できるリファレンスとなっています。

[![benchmark_summary](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/MfwBo6rVX4MrmsI_8kQpa.png)](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/MfwBo6rVX4MrmsI_8kQpa.png)

ベンチマークの結果は、Nemotron-Nano-9B-v2-Japanese がベースモデルである Nemotron-Nano-9B-v2 に強力な日本語能力を統合できたことを確認できます。これらの改善は、日本語の知識や質問応答能力にとどまらず、ツール呼び出し、コーディング、アライメントなど幅広いタスクに及びます。特筆すべきは、同等サイズの Qwen3-8B を上回り、優れたサイズ対性能比を実現している点です。

## **技術的優位性**

[![throughput](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/Jozble7RW6oSDRU9ietBv.png)](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/Jozble7RW6oSDRU9ietBv.png)

* 推論の効率性: Nemotron 2 Nano（Transformer-Mamba）のアーキテクチャを継承することで、エッジGPUにデプロイ可能でありながら、オープンソースの代替モデルと比較して最大6倍のスループット向上を実現します。上の図は、Nemotron 2 Nanoの
  [論文](https://arxiv.org/abs/2508.14444)
  で測定された結果を示しています。
* コンテキスト処理: 複数回（マルチターン）の会話やツール操作に最適化されています。
* ツール呼び出しの信頼性: API呼び出しや関数実行のために、強力な構造化データ生成能力を備えています。
* ファインチューニングの効率性: 手頃な計算インフラでもフルファインチューニングが可能なパラメータ数です。

## **デプロイのオプション**

#### 直接デプロイ

高い日本語理解とエージェンティックスキルを必要とするアプリケーションではモデルをそのままデプロイして活用できます。すでに学習済みの能力により、エージェントワークフローへの即時統合をサポートします。Nemotron 2 Nanoでサポートされている推論エンジンはシームレスに移行できます。

#### 独自ドメインへのカスタマイズ

特定のドメインに特化したファインチューニングのベースとして、Nemotron-Nano-9B-v2-Japaneseを利用できます。ベンチマークで実証された日本語およびエージェンティックタスクでの良い性能は、専門的なアプリケーション開発のための強固な開始点となります。カスタマイズにはNeMo Framework（
[NeMo Megatron-Bridge](https://github.com/NVIDIA-NeMo/Megatron-Bridge)
,
[NeMo AutoModel](https://github.com/NVIDIA-NeMo/Automodel)
, and
[NeMo-RL](https://github.com/NVIDIA-NeMo/RL)
）をご利用いただけます。

## **今すぐ使ってください**

日本のAIアプリケーション開発者の皆様は、今すぐ
[Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese)
をご利用いただけます。顧客対応エージェント、社内自動化ツール、あるいはドメイン特化型アシスタントなど、どのような用途であっても、本モデルは実運用へのデプロイに求められる優れたサイズ対性能比を提供します。

Nemotron 2 Nanoの実績あるアーキテクチャと、高品質なデータセットのシードとなる Nemotron-Personas-Japan の組み合わせは、日本のソブリンAI開発における効率的な出発点となるでしょう。

コミュニティの皆様に、Nemotronモデル、データセット、レシピ、ライブラリをぜひご活用いただき、さらに多くの言語やユースケース向けにNemotronモデルをカスタマイズしていただくことを歓迎します。皆様がどのようなものを構築されるか、楽しみにしています！

*Stay up to date on
[NVIDIA Nemotron](https://developer.nvidia.com/nemotron)
by subscribing to
[NVIDIA news](https://www.nvidia.com/en-us/ai-data-science/generative-ai/news/)
and following NVIDIA AI on
[LinkedIn](https://www.linkedin.com/showcase/nvidia-ai/posts/?feedView=all)
,
[X](https://x.com/NVIDIAAIDev)
,
[YouTube](https://www.youtube.com/@NVIDIADeveloper)*
,
*and the
[Nemotron channel](https://discord.com/channels/1019361803752456192/1407781691698708682)
on
[Discord](https://discord.com/invite/nvidiadeveloper)
.*

*Access open Nemotron Models on
[Hugging Face](https://huggingface.co/nvidia/collections?search=nemotron)
and a collection of
[NIM microservices](https://build.nvidia.com/models?filters=publisher%3Anvidia&q=Nemotron)
and Developer Examples on
[build.nvidia.com](http://build.nvidia.com)
.*