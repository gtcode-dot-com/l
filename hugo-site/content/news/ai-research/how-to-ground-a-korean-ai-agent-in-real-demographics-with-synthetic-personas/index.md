---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-21T02:15:46.516595+00:00'
exported_at: '2026-04-21T02:15:48.829004+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/build-korean-agents-with-nemotron-personas
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: How to Ground a Korean AI Agent in Real Demographics with Synthetic Personas
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/build-korean-agents-with-nemotron-personas
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How to Ground a Korean AI Agent in Real Demographics with Synthetic Personas
updated_at: '2026-04-21T02:15:46.516595+00:00'
url_hash: b806a278ca173d77a50b0ccc564f22229c9cca56
---

# How to Ground a Korean AI Agent in Real Demographics with Synthetic Personas

The models powering most

[AI agents](https://www.nvidia.com/en-us/glossary/ai-agents/)

today were trained primarily on English web data. They miss Korean honorific structures, regional occupation patterns, and the cultural context that Korean users expect. An agent that applies U.S. healthcare workflows to the Korean public health system isn't ready for production.

[Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)
fixes this. The dataset provides 6 million fully synthetic personas grounded in official statistics and seed data from the
[Korean Statistical Information Service (KOSIS)](https://kosis.kr/index/index.do)
, the
[Supreme Court of Korea](https://scourt.go.kr/scourt/index.html)
, the
[National Health Insurance Service](https://www.nhis.or.kr/)
, and the
[Korea Rural Economic Institute](https://www.krei.re.kr/krei/index.do)
.
[NAVER Cloud](https://www.navercloudcorp.com/)
contributed seed data and domain expertise during design.

Every persona is demographically accurate but contains zero personally identifiable information (PII). It’s designed with Korea's Personal Information Protection Act (PIPA) in mind. South Korea is also one of the few countries to publish an
[official Synthetic Data Generation guide](https://www.pipc.go.kr/np/default/page.do?mCode=D010010000)
, establishing governance for grounding models with synthetic versions of sensitive data. This dataset follows that approach.

In this tutorial, we'll turn a synthetic persona into a deployed Korean agent — from filtering the dataset to inference — in about 20 minutes using hosted APIs.

## A Sovereign Dataset for South Korea

[![Screenshot 2026-04-20 at 5.16.08 PM](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/P0Kad_kEoA0ZmaMc-tlay.png)](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/P0Kad_kEoA0ZmaMc-tlay.png)

| Attribute | Detail |
| --- | --- |
| Total personas | 7 million (1 million records × 7 personas each) |
| Persona fields | 26 fields: 7 persona fields, 6 persona attribute fields, 12 demographic & geographic contextual fields, and 1 unique identifier |
| Geographic coverage | All 17 Korean provinces, and 25 districts |
| Names | ~209K unique names (118 surnames, ~21.4K given names) |
| Occupations | 2K+ categories reflecting tech, manufacturing, public sector, etc. |
| Persona types | Professional, family, sports, arts, travel, culinary, concise |
| Life stages | Student, military service, employed, unemployed, retired |
| Language | Natural Korean |
| License | CC BY 4.0 |

Nemotron-Personas-Korea was generated using
[NeMo Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner)
, NVIDIA's open-source compound AI system for synthetic data. The pipeline pairs a Probabilistic Graphical Model (Apache-2.0) for statistical grounding with Gemma-4-31B for Korean-language narrative generation. Population data comes from KOSIS (2020–2026 releases); name distributions come from the Supreme Court of Korea.

[![title_diagram](https://cdn-uploads.huggingface.co/production/uploads/627a8c1793d0b645835e65f0/K8sQATx_CPk4p3h0ECIuF.png)](https://cdn-uploads.huggingface.co/production/uploads/627a8c1793d0b645835e65f0/K8sQATx_CPk4p3h0ECIuF.png)

Nemotron-Personas-Korea is the latest addition to the
[Nemotron-Personas Collection](https://huggingface.co/collections/nvidia/nemotron-personas)
, which also covers the USA, Japan, India, Singapore (with
AI Singapore
), Brazil (with
[WideLabs](https://valor.globo.com/empresas/noticia/2026/01/26/nvidia-e-widelabs-lancam-personas-de-ia-que-refletem-a-populacao-brasileira.ghtml)
), and France (with
[Pleias](https://pleias.fr/)
). If you're building a multilingual agent that serves Korean users alongside other markets, you can blend personas across countries in the same pipeline.

## Why This Matters for Autonomous Agents

Most agents today are identity-blind. They follow instructions without any grounding in who they're serving. For example, an agent that books a Korean hospital appointment using US scheduling conventions, or addresses a 60-year-old patient in 반말 (“banmal,” informal language), doesn't just feel wrong. It fails.

Nemotron-Personas-Korea changes this by giving your agent a Korean operating context. Load a persona into the system prompt and the agent inherits that persona's region, occupation, communication norms, and domain expertise.

This works across any agent framework. Deploy with
[NemoClaw](https://github.com/NVIDIA/NemoClaw)
(NVIDIA's open-source reference stack for always-on agents running in
[NVIDIA OpenShell](https://build.nvidia.com/spark/openclaw/overview)
sandboxes, on anything from RTX PCs to DGX Spark), serve through NVIDIA NIM for production inference, or call the NVIDIA API directly. The persona layer is framework-agnostic, acting as a well-structured system prompt grounded in real Korean demographics.

## Tutorial: From Synthetic Persona to Sovereign Agent

🔗 Resources

### Step 1: Load and Explore the Dataset

Load the dataset and explore what's available. Each record contains structured demographic fields alongside rich, natural-language persona narratives.

```
from datasets import load_dataset


dataset = load_dataset("nvidia/Nemotron-Personas-Korea")


print(dataset["train"].column_names)


print(dataset["train"][0])
```

### Step 2: Filter and Select a Persona

Filter the dataset by occupation, region, age, or any combination of fields to find personas that match your target domain. Here we'll build a Korean public health agent.

```
health_personas = dataset["train"].filter(
    lambda x: "보건" in x["occupation"] or "간호" in x["occupation"] or "의료" in x["occupation"]
)

print(f"Found {len(health_personas)} health personas")


persona = health_personas[0]
print(persona)
```

You can refine further by region (e.g., only Jeju-based health workers), education level, or life stage. The dataset is large enough to find highly specific slices.

### Step 3: Define Your Agent Behavior

This is where persona data becomes agent behavior. The structured fields — name, region, occupation, skills — become the agent's identity. You layer behavioral instructions and task scope on top. The result is an agent that reasons like a Korean professional in a specific role and region.

```
system_prompt = f"""당신은 한국의 공중보건 상담 AI 에이전트입니다.

[신원]                              # Identity
- 이름: {persona['name']}           # Name
- 지역: {persona['region']}         # Region
- 직업: {persona['occupation']}     # Occupation
- 전문분야: {persona['skills']}      # Specialization

[행동 지침]                           # Behavior guidelines
- 한국어 존댓말을 사용하여 응답하세요.      # Use formal Korean
- 지역 보건소 및 공공 의료 체계에 대한 안내를 제공하세요.  # Guide on local clinics
- 한국 공중보건 정책과 절차를 기반으로 정확한 정보를 제공하세요.  # Follow KR health policy
- 문화적 맥락을 고려하여 상담하세요.        # Consider cultural context

[업무 범위]                           # Task scope
- 예방접종 일정 안내                    # Vaccination scheduling
- 건강검진 절차 설명                    # Health screening procedures
- 지역 보건 자원 연결                   # Connect to local health resources
- 공중보건 관련 일반 상담                # General public health consultation

"""
```

### Step 4: Deploy Your Agent

Connect your persona-grounded prompt to a model for inference. You have three options depending on your setup:

* [NVIDIA API catalog](https://build.nvidia.com/)
  — fastest way to test (shown below)
* [NVIDIA NIM](https://developer.nvidia.com/nim)
  — self-hosted inference for production deployments
* [NemoClaw](https://github.com/NVIDIA/NemoClaw)
  — reference stack for deploying always-on agents, runs anywhere, including on RTX PCs through DGX Spark

```
from openai import OpenAI


client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="nvapi-YOUR_KEY"
)

response = client.chat.completions.create(
    model="nvidia/nemotron-nano-8b-v1",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "독감 예방접종은 언제 맞아야 하나요?"}
    ],
    temperature=0.7,
    max_tokens=512
)

print(response.choices[0].message.content)
```

The same workflow applies to any domain. Swap the persona filter and task scope, and you have a new agent: a 금융 ("geum-yung," finance) persona becomes a retail banking advisor, a 교육 ("gyoyug," education) persona becomes a tutoring assistant, a 공무원 ("gongmuwon," civil servant) persona becomes a government health services agent.

## What Grounding Changes

Here's the same question — "독감 예방접종은 언제 맞아야 하나요?" (When should I get a flu shot?) — answered with and without persona grounding.

|  | Without Personas | With Korean Health Worker Personas |
| --- | --- | --- |
| **Language** | Responds in English/generic Korean | Natural 존댓말 appropriate for health consultation |
| **Content** | References CDC/global guidance | References Korean 보건소 schedule, national vaccination program |
| **Specificity** | "Visit your local clinic" | "가까운 보건소에서 무료 접종이 가능합니다" with regional context |
| **Trust** | None | Cites Korean public health policy, uses professional medical Korean |

The persona goes beyond translation — it contextualizes and results in an agent your users will trust.

## Come Build with Us in Seoul

[NVIDIA Nemotron Developer Days](https://www.digitaltoday.co.kr/en/view/47483/nvidia-to-hold-nemotron-developer-days-seoul-2026-first-event-in-south-korea)
comes to Seoul today and tomorrow, April 21–22, 2026 — the first time the event has been held outside GTC. Two days of activities, including technical sessions on sovereign AI and open models, plus a hands-on hackathon where you'll have an opportunity to use Nemotron-Personas-Korea to build domain-specific Korean agents and a claw. 🦞

Join in person or via
[livestream](https://evt.to/w7654jbq79dq)
. Share what you build for a chance to be featured in a future NVIDIA tutorial.