---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-16T02:47:13.406224+00:00'
exported_at: '2025-11-16T02:47:14.734348+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/s3-compatible-ai-storage
structured_data:
  about: []
  author: ''
  description: RDMA for S3-compatible storage, optimized for NVIDIA networking and
    accelerated computing, delivers faster, more efficient object storage access.
  headline: How to Unlock Accelerated AI Storage Performance With RDMA for S3-Compatible
    Storage
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/s3-compatible-ai-storage
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How to Unlock Accelerated AI Storage Performance With RDMA for S3-Compatible
  Storage
updated_at: '2025-11-16T02:47:13.406224+00:00'
url_hash: a65ef4f0d3d93cf15b318cec658805158f9ffb24
---

Today’s AI workloads are data-intensive, requiring more scalable and affordable storage than ever. By 2028, enterprises are projected to generate nearly 400 zettabytes of data annually, with 90% of new data being unstructured, comprising audio, video, PDFs, images and more.

This massive scale, combined with the need for data portability between on-premises infrastructure and the cloud, is pushing the AI industry to evaluate new storage options.

Enter RDMA for S3-compatible storage — which uses remote direct memory access (RDMA) to accelerate the S3-application programming interface (API)-based storage protocol and is optimized for AI data and workloads.

Object storage has long been used as a lower-cost storage option for applications, such as archive, backups, data lakes and activity logs, that didn’t require the fastest performance. While some customers are already using object storage for AI training, they want more performance for the fast-paced world of AI.

This solution, which incorporates
[NVIDIA networking](https://www.nvidia.com/en-us/networking/)
, delivers faster and more efficient object storage by using RDMA for object data transfers.

For customers, this means higher throughput per terabyte of storage, higher throughput per watt, lower cost per terabyte and significantly lower latencies compared with TCP, the traditional network transport protocol for object storage.

Other benefits include:

* **Lower Cost:**
  End users can lower the cost of their AI storage, which can also speed up project approval and implementation.
* **Workload Portability:**
  Customers can run their AI workloads unmodified in both on premises and in cloud service provider and neocloud environments, using a common storage API.
* **Accelerated Storage:**
  Faster data access and performance for AI training and inference — including vector databases and key-value cache storage for inference in AI factories.
* [**AI data platform**](https://www.nvidia.com/en-us/data-center/ai-data-platform/)
  solutions gain faster storage object storage access and more metadata for content indexing and retrieval.
* **Reduced CPU Utilization:**
  RDMA for S3-compatible storage doesn’t use the host CPU for data transfer, meaning this critical resource is available to deliver AI value for customers.

NVIDIA has developed RDMA client and server libraries to accelerate object storage. Storage partners have integrated these server libraries into their storage solutions to enable RDMA data transfer for S3-API-based object storage, leading to faster data transfers and higher efficiency for AI workloads.

Client libraries for RDMA for S3-compatible storage run on AI GPU compute nodes. This allows AI workloads to access object storage data much faster than traditional TCP access — improving AI workload performance and GPU utilization.

While the initial libraries are optimized for NVIDIA GPUs and networking, the architecture itself is open, because other vendors and customers can contribute to the client libraries and incorporate them into their software. They can also write their own software to support and use the RDMA for S3-compatible storage APIs.

## **Standardization, Availability and Adoption**

NVIDIA is working with partners to standardize RDMA for S3-compatible storage.

Several key object storage partners are already adopting the new technology.
[Cloudian](https://cloudian.com/blog/supercharging-vector-database-indexing-8x-faster-with-cloudian-s3-rdma-and-nvidia/)
, Dell Technologies and HPE are all incorporating RDMA for S3-compatible libraries into their high-performance object storage products: Cloudian
[HyperStore](https://cloudian.com/products/hyperstore/)
, Dell
[ObjectScale](https://www.dell.com/en-us/shop/storage-servers-and-networking-for-business/sf/objectscale)
and the HPE
[Alletra Storage MP X10000](https://www.hpe.com/us/en/alletra-storage-mp-x10000.html)
.

“Object storage is the future of scalable data management for AI,” said Jon Toor, chief marketing officer at Cloudian. “Cloudian is leading efforts with NVIDIA to standardize RDMA for S3-compatible storage, which enables faster, more efficient object storage that helps scale AI solutions and reduce storage costs. Standardization and Cloudian’s S3-API compatibility will seamlessly bring scalability and performance to thousands of existing S3-based applications and tools, both on premises and in the cloud.”

“AI workloads demand storage performance at scale with thousands of GPUs reading or writing data concurrently, and enterprise customers, with multiple AI factories — on premises and in the cloud — desire AI workload portability for objects,” said Rajesh Rajaraman, chief technology officer and vice president of Dell Technologies Storage, Data and Cyber Resilience. “Dell Technologies has collaborated with NVIDIA to integrate RDMA for S3-compatible storage acceleration into Dell ObjectScale, object storage that delivers unmatched scalability, performance and dramatically lower latency with end-to-end RDMA. The latest Dell ObjectScale software update will provide an excellent storage foundation for AI factories and AI data platforms.”

“As AI workloads continue to grow in scale and intensity, NVIDIA’s innovations in RDMA for S3-compatible storage APIs and libraries are redefining how data moves at massive scale,” said Jim O’Dorisio, senior vice president and general manager of storage at HPE. “Working closely with NVIDIA, HPE has built a solution that accelerates throughput, reduces latency and lowers total cost of ownership. With RDMA for S3-compatible storage capabilities now integrated into HPE Alletra Storage MP X10000, we are extending our leadership in intelligent, scalable storage for unstructured and AI-driven workloads.”

*NVIDIA’s RDMA for S3-compatible storage libraries are now available to select partners and are expected to be generally available via the*
[*NVIDIA CUDA Toolkit*](https://developer.nvidia.com/cuda-toolkit)
*in January. Plus, learn more about a new NVIDIA Object Storage Certification, part of the*
[*NVIDIA-Certified Storage program*](https://blogs.nvidia.com/blog/nvidia-certified-enterprise-storage/)
*.*