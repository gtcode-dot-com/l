---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-21T00:00:19.105330+00:00'
exported_at: '2025-11-21T00:00:23.239058+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/msd-explores-applying-generative-al-to-improve-the-deviation-management-process-using-aws-services
structured_data:
  about: []
  author: ''
  description: This blog post has explores how MSD is harnessing the power of generative
    AI and databases to optimize and transform its manufacturing deviation management
    process. By creating an accurate and multifaceted knowledge base of past events,
    deviations, and findings, the company aims to significantly reduce the time and
    effort required for each new case while maintaining the highest standards of quality
    and compliance.
  headline: MSD explores applying generative Al to improve the deviation management
    process using AWS services
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/msd-explores-applying-generative-al-to-improve-the-deviation-management-process-using-aws-services
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MSD explores applying generative Al to improve the deviation management process
  using AWS services
updated_at: '2025-11-21T00:00:19.105330+00:00'
url_hash: c6a1cf6f05444ee99665def35cb9ffc7f2e075b8
---

*This post is co-written with Hossein Salami and Jwalant Vyas from MSD.*

In the biopharmaceutical industry, deviations in the manufacturing process are rigorously addressed. Each deviation is thoroughly documented, and its various aspects and potential impacts are closely examined to help ensure drug product quality, patient safety, and compliance. For leading pharmaceutical companies, managing these deviations robustly and efficiently is crucial to maintaining high standards and minimizing disruptions.

Recently, the Digital Manufacturing Data Science team at Merck & Co., Inc., Rahway, NJ, USA (MSD) recognized an opportunity to streamline aspects of their deviation management process using emerging technologies including vector databases and generative AI, powered by AWS services such as
[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
and
[Amazon OpenSearch](https://docs.aws.amazon.com/opensearch-service/)
. This innovative approach aims to use the organization’s past deviations as a vast, diverse, and reliable knowledge source. Such knowledge can potentially help reduce the time and resources required for—and increase the efficiency of—researching and addressing each new deviation by using learnings from similar cases across the manufacturing network, while maintaining the rigorous standards demanded by
[Good Manufacturing Practices (GMP)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q7a-good-manufacturing-practice-guidance-active-pharmaceutical-ingredients)
requirements.

## Industry trends: AI in pharmaceutical manufacturing

The pharmaceutical industry has been increasingly turning to advanced technologies to enhance various aspects of their operations, from early drug discovery to manufacturing and quality control. The application of AI, particularly generative AI, in streamlining complex processes is a growing trend. Many companies are exploring how these technologies can be applied to areas that traditionally require significant human expertise and time investment, including the above-mentioned deviation management. This shift towards AI-assisted processes is not only about improving efficiency, but also about enhancing the quality and consistency of outcomes in critical areas.

## Innovative solution: Generative AI for deviation management

To address some of the major challenges in deviation management, the Digital Manufacturing Data Science team at MSD devised an innovative solution using generative AI (see
[How can language models assist with pharmaceuticals manufacturing deviations and investigations?](https://www.sciencedirect.com/science/article/pii/S0378517324013346)
). The approach involves first, creating a comprehensive knowledge base from past deviation reports, which can be intelligently queried to provide various insights including helpful information for addressing new cases. In addition to the routine metadata, the knowledge base includes important unstructured data such as observations, analysis processes, and conclusions, typically recorded as natural language text. The solution is designed to facilitate the interaction of different users in manufacturing sites, with different personas and roles, with this knowledge sources. For example, users can quickly and accurately identify and access information about similar past incidents and use that information to hypothesize about the potential root causes and define resolutions for a current case. This is facilitated by a hybrid and domain-specific search mechanism implemented through Amazon OpenSearch Service. Subsequently, the information is processed by a large language model (LLM) and is presented to the user based on their persona and need. This functionality not only saves time but also uses the wealth of experience and knowledge from previous deviations.

## Solution overview: Goals, risks, and opportunities

Deviation investigations have traditionally been a time-consuming, manual process that requires significant human effort and expertise. Investigation teams often spend extensive hours collecting, analyzing, and documenting information, sifting through historical records, and drawing conclusions—a workflow that is not only labor-intensive but also prone to potential human error and inconsistency. The solution aims to achieve several key goals:

* Significantly reduce the time and effort required for investigation and closure of a deviation
* Provide users with easy access to relevant knowledge, historical information, and data with high accuracy and flexibility based on user persona
* Make sure that the information used to derive conclusions is traceable and verifiable

The team is also mindful of potential risks, such as over-reliance on AI-generated suggestions or the possibility of outdated information influencing current investigations. To mitigate these risks, the solution mostly limits the generative AI content creation to low-risk areas and incorporates human oversight and other guardrails. An automated data pipeline helps the knowledge base remain up-to-date with the most recent information and data. To protect proprietary and sensitive manufacturing information, the solution includes data encryption and access controls on different elements.

Additionally, the team sees opportunities for incorporating new elements in the architecture, particularly in the form of agents that can handle specific requests common to certain user personas such as high-level statistics and visualizations for site managers.

## Technical architecture: RAG approach with AWS services

The solution architecture uses a Retrieval-Augmented Generation (RAG) approach to enhance the efficiency, relevance, and traceability of deviation investigations. This architecture integrates multiple AWS managed services to build a scalable, secure, and domain-aware AI-driven system.

At the core of the solution is a
**hybrid retrieval module**
(leveraging the hybrid search capabilities of Amazon OpenSearch Service) that combines both semantic (vector-based) and keyword (lexical) search for high-accuracy information retrieval. This module is built on
**Amazon OpenSearch Service**
, which functions as the
**vector store**
. OpenSearch indexes embeddings generated from past deviation reports and related documents, enriched with domain-specific metadata such as deviation type, resolution date, impacted product lines, and root cause classification. This is for both deep semantic search and efficient filtering based on structured fields.

To support structured data storage and management, the system uses
**Amazon Relational Database Service (Amazon RDS)**
. RDS stores normalized tabular information associated with each deviation case, such as investigation timelines, responsible personnel, and other operational metadata. With RDS you can make complex queries across structured dimensions and supports reporting, compliance audits, and trend analysis.

A
**RAG pipeline**
orchestrates the flow between the retrieval module and a
**large language model (LLM)**
hosted in
**Amazon Bedrock**
. When a user issues a query, the system first retrieves relevant documents from OpenSearch and structured case data from RDS. These results are then passed as context to the LLM, which generates grounded, contextualized outputs such as:

* Summarized investigation histories
* Root cause patterns
* Comparable past incidents
* Suggested next steps or knowledge gaps

![AWS generative AI deviation management workflow showing data flow between services, security, and storage components](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/17/msd-blog-image.png)

High-level architecture of the solution. Domain-specific deviation data are located on Amazon RDS and OpenSearch. Text vector embeddings along with relevant metadata are located on OpenSearch to support a variety of search functionalities.

## Conclusion and next steps

This blog post has explored how MSD is harnessing the power of generative AI and databases to optimize and transform its manufacturing deviation management process. By creating an accurate and multifaceted knowledge base of past events, deviations, and findings, the company aims to significantly reduce the time and effort required for each new case while maintaining the highest standards of quality and compliance.

As next steps, the company plans to conduct a comprehensive review of use cases in the pharma quality domain and build a generative AI-driven enterprise scale product by integrating structured and unstructured sources using methods from this innovation. Some of the key capabilities coming from this innovation include data architecture, data modeling, including metadata curation, and generative AI-related components. Looking ahead, we plan to use the capabilities of
[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases)
, which will provide more advanced semantic search and retrieval capabilities while maintaining seamless integration within the AWS environment. If successful, this approach could set a new standard for not only deviation management at MSD, but also pave the way for more efficient, integrated, and knowledge-driven manufacturing quality processes including complaints, audits, and so on.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/06/ML-17659-Hossein-1-100x100.jpeg)
**Hossein Salami**
is a Senior Data Scientist at the Digital Manufacturing organization at MSD. As a Chemical Engineering Ph.D. with a background of more than 9 years of laboratory and process R&D experience, he takes part in leveraging advanced technologies to build data science and AI/ML solutions that address core business problems and applications.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/17/Vyas_photo-100x100.jpg)
Jwalant (JD) Vyas**
is the Digital Product Line Lead for the Investigations Digital Product Portfolio at MSD, bringing 25+ years of biopharmaceutical experience across Quality Operations, QMS, Plant Operations, Manufacturing, Supply Chain, and Pharmaceutical Product Development. He leads the digitization of Quality Operations to improve efficiency, strengthen compliance, and enhance decision-making. With deep business domain and technology expertise, he bridges technical depth with strategic leadership.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/06/ML-17659-Duverney-1-100x100.jpeg)
Duverney Tavares**
is a Senior Solutions Architect at Amazon Web Services (AWS), specializing in guiding Life Sciences companies through their digital transformation journeys. With over two decades of experience in Data Warehousing, Big Data & Analytics, and Database Management, he uses his expertise to help organizations harness the power of data to drive business growth and innovation.