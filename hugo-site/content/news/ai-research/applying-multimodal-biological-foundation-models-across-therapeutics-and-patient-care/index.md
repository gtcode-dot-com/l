---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-23T18:15:37.422110+00:00'
exported_at: '2026-04-23T18:15:39.653448+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/applying-multimodal-biological-foundation-models-across-therapeutics-and-patient-care
structured_data:
  about: []
  author: ''
  description: In this post, we'll explore how multimodal BioFMs work, showcase real-world
    applications in drug discovery and clinical development, and contextualize how
    AWS enables organizations to build and deploy multimodal BioFMs.
  headline: Applying multimodal biological foundation models across therapeutics and
    patient care
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/applying-multimodal-biological-foundation-models-across-therapeutics-and-patient-care
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Applying multimodal biological foundation models across therapeutics and patient
  care
updated_at: '2026-04-23T18:15:37.422110+00:00'
url_hash: 17fbd044ef6ef3de09ca9e815438e59e2aad3052
---

Healthcare and life sciences decision making increasingly relies on multimodal data to diagnose diseases, prescribe medicine and predict treatment outcomes, develop and optimize innovative therapies accurately. Traditional approaches analyze fragmented data, such as ‘omics for drug discovery, medical images for diagnostics, clinical trial reports for validation, and electronic health records (EHR) for patient treatment. As a result, decision makers (CxOs, VPs, Directors) often miss critical insights hidden in the relationships between data types. Recent advancements in AI enable you to integrate and analyze these fragmented data streams efficiently to support a more complete understanding of therapeutics and patient care.

AWS provides a unified environment for multimodal biological foundation models (BioFMs), enabling you to make more confident, timely decision-making in personalized medicine. This AI system combines biological data, model development, scalable compute, and partner tools to support the drug development life cycle. In this post, we’ll explore how multimodal BioFMs work, showcase real-world applications in drug discovery and clinical development, and contextualize how AWS enables organizations to build and deploy multimodal BioFMs.

## **Multimodal biological foundation models**

Biological foundation models (BioFMs) are AI models pre-trained on large biological datasets. BioFMs demonstrate advanced capabilities on specific healthcare and life sciences tasks. The commonly used BioFMs span drug discovery and clinical development domains, particularly in protein structure and molecule design (~20%), omics data analysis including DNA, epigenetic, and RNA (~30%), medical imaging (15%), and clinical documentation (~35%) (
[Delile et al. 2025](https://www.sciencedirect.com/science/article/pii/S1359644625002314?via%3Dihub)
).

Unimodal BioFMs are trained exclusively on a single data modality (for example, amino acid sequences) for relevant downstream applications like predicting protein structures; this breakthrough earned the
[2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)
. Multimodal BioFMs train across multiple data types (text, audio, image, and video, hereafter “modalities”) and can simultaneously infer across different streams in a single model (for example, text prompts to generate new images or match images to captions).

Notable multimodal BioFM examples include:

1. Latent Labs’
   [Latent-X1](https://www.latentlabs.com/latent-x/)
   and
   [Latent-X2](https://www.latentlabs.com/latent-x2/)
   not only predict 3D structures of proteins, but also generate novel binders like antibodies, macrocyclic peptides, and miniproteins and predict how they interact with targets.
2. Arc Institute’s
   [Evo 2](https://aws.amazon.com/marketplace/pp/prodview-daikatl6hfzqe)
   maps the
   [central dogma of biology](https://www.genome.gov/genetics-glossary/Central-Dogma)
   to interpret and predict the structure and function of DNA, RNA, and proteins.
3. Insilco Medicine’s
   [Nach01](https://aws.amazon.com/marketplace/pp/prodview-aq32kfu5ifjgw)
   integrates natural language, chemical intelligence, and 3D molecular structure data to accelerate drug discovery.
4. Bioptimus’
   [M-Optimus](https://www.bioptimus.com/m-optimus)
   decodes histology and clinical data for rich biological insights, supporting multiple stages from research to patient care.
5. Harvard and AstraZeneca’s
   [MADRIGAL](https://arxiv.org/html/2503.02781v1)
   integrates structural, pathway, cell viability, and transcriptomic data to predict drug combination clinical outcome, identify adverse interactions, and optimize polypharmacy management.
6. John Snow Lab’s vision language model
   [Medical VLM-24B](https://aws.amazon.com/marketplace/pp/prodview-sagwxj5hcox4o?sr=0-1&ref_=beagle&applicationId=AWSMPContessa)
   processes clinical notes, lab reports, and imaging (X‑ray, MRI, CT) for unified, context‑aware diagnostics.
7. GEHC’s
   [3D magnetic resonance imaging (MRI) foundation model](https://www.gehealthcare.com/insights/article/ge-healthcare-unveils-firstofitskind-mri-foundation-model?srsltid=AfmBOoqbiT-XIGGDwFwJgHm21T_IQIJC1shSBq9tLteuZTzAkcy4MLRL)
   , designed to enable developers to build applications for tasks such as image retrieval, classification, image segmentation, and report generation.

## **The multimodal advantage**

The current frontier of models pushes the boundary of multimodal understanding and generation capabilities. General-purpose models like
[Amazon Nova 2 Omni](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-nova-2-omni-preview/)
can process text, images, video, and speech inputs while generating both text and images. This multimodality trend extends to BioFMs, where combining multiple data types like medical images and clinical documentation achieves higher predictive accuracy and broader applicability across diverse clinical outcomes (
[Siam et al. 2025](https://www.mdpi.com/2078-2489/16/11/971)
).

Integrating diverse biological data types yields measurable performance gains:

* **Enhanced diagnostic accuracy:**
  Models integrating genomics, imaging, and clinical data yield 4-7% average gains in area under the curve (AUC) over unimodal baselines for diagnoses (e.g., Alzheimer’s, brain cancer) and phenotypes (
  [Sun et al. 2024](https://www.nature.com/articles/s44172-024-00245-w)
  ). Moreover, models integrating lab data, patient exercise metrics, and clinical notes during patient screening achieve 92.74% accuracy with 93.21 AUC in cardiovascular risk prediction (
  [Guo and Wu, 2025](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1693823/full)
  ).
* **Targeted therapeutic strategies**
  : You can use models integrating genomic profiles, medical images, and clinical histories to guide selection of effective interventions for individual patients (
  [Parvin et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12195918/)
  ). This proves especially impactful for cancer patients where tumor genomics and radiological imaging can facilitate therapeutic decisions like chemotherapy regimens (
  [Restrepo et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10340640/)
  ).
* **New disease mechanisms:**
  Single-cell multi-omics models show how cancer cells grow and resist treatments inside blood diseases like leukemia, helping physicians improve survival rates by spotting hidden cancer cells, tracking how mutations drive disease progression, and selecting personalized treatments for patients
  [(Kim and Takahashi, 2025](https://haematologica.org/article/view/11928)
  ).
* **Accurate risk prediction:**
  You can use models integrating lab results, medications, clinical notes, and discharge summaries and other clinical data to predict 30-day hospital readmission risk with 76% accuracy—delivering ~$3.4 million in net savings per hospital annually while improving overall clinical outcomes for high-risk heart failure patients through targeted interventions (
  [Golas et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6013959/)
  ).
* **Predictive, Preventative, Personalized, Participatory (P4) medicine:**
  Models combining wearable health technologies with patient health data can extract target signals with 96-97% accuracy for diabetes and heart disease diagnosis (
  [Mansour et al. 2021](https://ieeexplore.ieee.org/document/9380633)
  ).

## **BioFMs in action at AWS customers**

These performance gains explain why leading biopharma organizations are increasingly adopting multimodal BioFMs. Leading biopharma organizations invest in BioFMs for analyzing biologic (
[Merck](https://www.youtube.com/watch?v=f5Bmf_axRNw)
and
[Novo Nordisk](https://aws.amazon.com/blogs/hpc/how-novo-nordisk-columbia-university-and-aws-collaborated-to-create-openfold3/)
), genomic (
[AstraZeneca)](https://aws.amazon.com/blogs/industries/astrazeneca-fine-tunes-genomics-foundation-models-with-amazon-sagemaker/)
, pathology (
[Bayer](https://aws.amazon.com/blogs/industries/bayer-imaging-fm-classifies-drug-targets-using-amazon-sagemaker-hyperpod/)
), and clinical (
[Roche](https://www.johnsnowlabs.com/spark-nlp-how-roche-automates-knowledge-extraction-from-pathology-reports/)
) data. You can realize up to 50% in cost and time savings for drug development and up to 90% in time savings for medical image diagnosis when using these specialized AI models (
[State of the Art-ificial Intelligence 2025,](https://www.tdsecurities.com/ca/en/state-of-the-art-ificial-intelligence)
[Jeong et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11813001/)
). Multimodal BioFMs show promise in multiple stages of the healthcare and life sciences value chain (
**Figure 1**
).

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/21/ML-20310-image-1-new.png)

Figure 1. Multimodal BioFMs integrate various biological data types (for example, protein, small molecule, omics, imaging, sensors, clinical documentation) to power applications across the drug development lifecycle (research, clinical development, manufacturing, commercial).

For a deeper dive, we’ve selected two use cases: drug discovery and clinical development.

* **Designing therapeutic proteins for undruggable disease targets.**
  Multimodal BioFMs integrating computational predictions, structural biology, and biophysical validation enable new approaches to previously inaccessible protein targets (
  **Figure 2**
  ). Early applications predicted 3D structures but struggled with multidomain targets featuring discontinuous epitopes. Advanced drug discovery now integrates iterative design-make-test-analyze (DMTA) loops that span structural, computational, and biophysical data. The 3D protein structural data captured through cryo-electron microscopy (Cryo-EM) is evaluated alongside computational metrics like interface predicted template modeling score (iPTM), interface predicted aligned error (iPAE), and root mean square deviation (RMSD) then validated against biophysical measurements such as dose-response curves, biolayer interferometry (BLI), and enzyme-linked immunosorbent assay (ELISA) to accelerate and de-risk drug discovery. For example,
  [Onava’s](https://onava.ai/)
  integrated “AI-human-wet lab” loop represents a step forward in this space by combining generative AI for de novo protein design with rapid experimental validation through an “epitope expansion” strategy, compressing design-to-validation timelines from months to weeks (
  [Calman et al. bioRxiv 2025](https://www.biorxiv.org/content/10.64898/2025.12.27.696647v1)
  ). You may develop next-generation biologics using multimodal BioFMs like Latent Labs Latent-X2 and Chai Discovery Chai-2 through AWS services including Amazon Bio Discovery, Amazon SageMaker AI for training generative models, Amazon Elastic Compute Cloud (EC2) for model inference, Amazon Simple Storage Service (Amazon S3) for storing structural and experimental data, Amazon Elastic File System (EFS) for shared design libraries, and Amazon Virtual Private Cloud (VPC) for secure infrastructure.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/21/ML-20310-image-2-new.png)

Figure 2. Multimodal BioFMs integrate 3D protein structure, computational metrics, and biophysical measurements through iterative design-validation loops to accelerate therapeutic protein discovery for undruggable multidomain disease targets.

* **Predicting immunotherapy resistance in cancer patients during clinical development.**
  Multimodal BioFM developers work towards addressing oncology’s 90% clinical trial failure rate. Today’s multimodal BioFMs simulate tumor microenvironments by integrating sequencing, single-cell data, spatial biology, and patient records to discover resistance mechanisms that reduce patient drop-offs from ineffective treatments and discover new therapeutic targets for previously untreatable patient subgroups (
  **Figure 3**
  ). For example,
  [Noetik’s](https://aws.amazon.com/startups/learn/noetik-powers-precision-cancer-therapies-with-machine-learning?lang=en-US)
  Oncology Counterfactual Therapeutics Oracle (OCTO) simulated 873,000 virtual immune cells across 1,399 patient tumors and revealed why lung cancer patients with KRAS and STK11 gene mutations develop “immune cold” environments blocking immunotherapy effectiveness (
  [Xie et al. Poster presented at SITC 2025](https://www.noetik.ai/sitc-2025)
  ). Notably,
  [Noetik](https://aws.amazon.com/startups/learn/noetik-powers-precision-cancer-therapies-with-machine-learning#overview)
  achieved 40% faster training time and doubled processing speed through
  [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
  ’s fault-tolerant infrastructure on AWS with NVIDIA H100 GPUs. You can build your own multimodal BioFMs can take a similar approach using
  [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
  for distributed AI training across GPUs,
  [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)
  for compute capacity,
  [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
  for data storage, and
  [Amazon Athena](https://aws.amazon.com/athena/)
  for analyzing petabytes of patient data.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/21/ML-20310-image-3-new.png)

Figure 3. Multimodal BioFM approach combines sequencing, spatial transcriptomics, pathology, and patient records to simulate tumor microenvironments and prioritize patient subpopulations, potentially reducing early-phase trial failures

## **Solution: AWS environment for multimodal BioFMs**

AWS provides a unified environment for building, training, and deploying multimodal BioFMs that help you convert healthcare and life science data into actionable insights. This environment comprises four layers: an AI solution for model development, a unified data foundation for biological data management, scalable infrastructure for compute and storage, and partner integrations that extend capabilities across the drug development lifecycle.

* **AI System**
  + [Amazon Bio Discovery](https://aws.amazon.com/biodiscovery/)
    provides scientists direct access AI agents selecting the right BioFMs, optimizing inputs, evaluating candidates, sending to lab partners for testing, and automatically returning results for refinement in a lab-in-the-loop cycle that builds institutional knowledge.
  + [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
    delivers distributed training infrastructure for large-scale models.
    [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
    compliments this with built-in explainability tools, bias detection, and comprehensive audit trails to support regulatory confidence needed from model development through production deployment.
  + [Amazon Nova Forge,](https://aws.amazon.com/nova/forge/)
    [released at AWS re:Invent 2025,](https://aws.amazon.com/nova/forge/)
    uses the Amazon Nova model family as a starting point to train at optimal points to maximize proprietary data set learning while minimizing training and continued pretraining.
  + [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
    includes the
    [Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
    service to host long-running deep research agents and the
    [Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
    service to securely connect agents to BioFM models and other domain-specific tools.
* **Unified Data Foundation**
  + [AWS HealthOmics](https://aws.amazon.com/healthomics/)
    can orchestrate multi-step AI workflows and handle omics data (DNA, RNA, proteomics) at the petabyte scale, serving as a biological data backbone that powers multimodal BioFM workflows.
  + [AWS HealthLake](https://aws.amazon.com/healthlake/)
    and
    [AWS HealthImaging](https://aws.amazon.com/healthimaging/)
    aggregate heterogeneous data into governed lakehouses, automating harmonization across clinical records and medical imaging (radiology, pathology).
  + [AWS Data Exchange](https://aws.amazon.com/data-exchange/)
    and
    [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
    provide “search, shop, serve” access to federated datasets from Epic, Snowflake, and proprietary sources – revealing disease mechanisms across cancer, rare diseases, and clinical trials without manual integration.
    [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)
    enable federated learning while maintaining data sovereignty.
* **Scalable Infrastructure**

## **AWS Partner solutions and implementation support**

You can deploy pre-built
[multimodal BioFMs from partners like NVIDIA](https://blogs.nvidia.com/blog/open-models-data-tools-accelerate-ai/)
directly through AWS. Combine these production-ready
[NVIDIA NIM microservices with AWS](https://blogs.nvidia.com/blog/nim-ai-microservices-for-healthcare-integrate-with-aws/)
HIPAA-eligible imaging services, multimodal reasoning capabilities, and parallel genomics pipelines to build end-to-end discovery-to-clinic applications. Example partner multimodal BioFMs include:

* [MONAI Multimodal](https://developer.nvidia.com/blog/monai-integrates-advanced-agentic-architectures-to-establish-multimodal-medical-ai-ecosystem/)
  : Models combine diverse healthcare data—including CT, MRI, X-ray, ultrasound, EHRs, clinical documentation, DICOM standards, video streams, and whole slide imaging—to enable multimodal analysis for researchers and developers.
* [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
  : Large Multimodal Models for Science and Medicine. Models like
  [NVIDIA Cosmos Reason-1-7B](https://aws.amazon.com/marketplace/pp/prodview-e6loqk6jyzssy)
  could be used for surgical robotics training by generating synthetic datasets that combine 3D anatomical models, physics-based sensor data (ultrasound/RGB cameras), and procedural variation.
* [La-Proteina](https://research.nvidia.com/labs/genair/la-proteina/)
  : Uses both protein sequence and atom-level 3D structural information to design large, precise proteins, so it can reasonably be described as a multimodal protein model (sequence + structure).

You can consult with implementation partners like
[Loka](https://aws.amazon.com/marketplace/seller-profile?id=a185d876-660d-4b27-a582-cf30ce37f670)
,
[Deloitte](https://aws.amazon.com/marketplace/seller-profile?id=c2b4f9de-b920-4d33-abff-5f27d81d35c1)
, and
[Accenture](https://aws.amazon.com/marketplace/seller-profile?id=4fe793cb-71be-4e10-894c-037dd798e603)
on transitioning from proof-of-concept to production deployment for multimodal BioFMs use cases. These partners bring specialized expertise in bioinformatics, cloud architecture, and regulatory compliance to accelerate time-to-value.
[Visit the AWS Partner Network](https://aws.amazon.com/partners/)
to explore additional qualified partners with healthcare and life sciences competencies.

## **Conclusion**

Multimodal BioFMs are reimagining what we can discover about disease, treatment, and human health. By integrating omics data, medical imaging, and clinical information, these models reveal hidden insights that were previously difficult to detect through traditional methods. Decision makers can now make more accurate, confident decisions across disease diagnosis, treatment prediction, and therapeutic optimization.

AWS provides a unified environment to overcome the technical barriers of building and deploying multimodal BioFMs at scale. Rather than investing in fragmented, single-use AI solutions for each therapeutic area or clinical application, you can leverage reusable foundation models that adapt across therapeutics and patient care. This system reduces time-to-value while preserving the flexibility to adapt as new data sources and use cases emerge for multimodal BioFMs across therapeutics and patient care.

To learn more about using AWS for BioFM training or inference in a therapeutic or medical context, please contact an
[AWS Life Sciences](https://pages.awscloud.com/global-ln-gc-a4hcls-biopharma-contact-us-interest.html?languages=english)
representative.

### **Further reading**

---

## About the authors

### Kristin Ambrosini

Kristin Ambrosini is a Generative AI Specialist in Healthcare and Life Sciences at Amazon Web Services. She leads go-to-market for BioFMs to accelerate drug discovery and improve patient care. She combines scientific expertise, technical fluency, and strategic insight to drive innovation across healthcare and life sciences. Kristin holds a Ph.D. in Biological Sciences and brings hands-on experience in DNA sequencing, cancer therapeutics, and viral diagnostics – giving her a unique lens into the challenges and opportunities multimodal BioFMs are built to solve.

### Brian Loyal

Brian Loyal is a Principal AI/ML Solutions Architect in the Global Healthcare and Life Sciences team at Amazon Web Services. He has more than 20 years’ experience in biotechnology and machine learning and is passionate about using AI to improve human health and well-being.

### Mike Tarselli

Mike Tarselli is a Specialist Leader in Healthcare and Life Sciences Data and AI at Amazon Web Services. He has spent more than 25 years in the biopharma industry. As a leader in AI and data strategy, he works with scientific and technical teams to help them realize their vision, while embracing the fast pace and enormity of AI.

### Zheng Yang

Zheng Yang is the global Head of AI/ML Strategy for Healthcare and Life Sciences at AWS. He brings more than 25 years experience in AI/ML solution development across the life sciences value chain. Before AWS, Zheng architected holistic data solutions to accelerate new medicine launches and championed technology adoption in pharmaceutical research. He is passionate about using technology to transform patient care.