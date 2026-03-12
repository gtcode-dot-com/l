---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-12T22:15:48.488305+00:00'
exported_at: '2026-03-12T22:15:51.124045+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/multimodal-embeddings-at-scale-ai-data-lake-for-media-and-entertainment-workloads
structured_data:
  about: []
  author: ''
  description: This post shows you how to build a scalable multimodal video search
    system that enables natural language search across large video datasets using
    Amazon Nova models and Amazon OpenSearch Service. You will learn how to move beyond
    manual tagging and keyword-based searches to enable semantic search that captures
    the f...
  headline: 'Multimodal embeddings at scale: AI data lake for media and entertainment
    workloads'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/multimodal-embeddings-at-scale-ai-data-lake-for-media-and-entertainment-workloads
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Multimodal embeddings at scale: AI data lake for media and entertainment workloads'
updated_at: '2026-03-12T22:15:48.488305+00:00'
url_hash: da712e678deb38e91aa4db556343b7bc09eddc47
---

This post shows you how to build a scalable multimodal video search system that enables natural language search across large video datasets using
[Amazon Nova](https://aws.amazon.com/nova/)
models and
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
. You will learn how to move beyond manual tagging and keyword-based searches to enable semantic search that captures the full richness of video content.

We demonstrate this at scale by processing 792,270 videos from two
[AWS Open Data Registry](https://registry.opendata.aws/)
datasets:
[Multimedia Commons](https://registry.opendata.aws/multimedia-commons/)
(787,479 videos, 37-second average) and
[MEVA](https://registry.opendata.aws/mevadata/)
(4,791 videos, 5-minute average). Processing 8,480 hours of video content (30.5M seconds) took 41 hours. First-year total cost: $27,328 (with OpenSearch on-demand) or $23,632 (with OpenSearch Service Reserved Instances). The cost consisted of one-time ingestion ($18,088) and annual Amazon OpenSearch Service ($9,240 on-demand or $5,544 Reserved).

The ingestion breakdown is as follows:

* Amazon Elastic Compute Cloud (Amazon EC2) compute (4× c7i.48xlarge spot at $2.57/hour × 41 hours): $421
* [Amazon Bedrock](https://aws.amazon.com/bedrock/)
  Nova Multimodal Embeddings (30.5M seconds × $0.00056/second batch pricing): $17,096
* Nova Pro tagging (792K videos × 600 tokens(avg.)): $571

The solution generates audio-visual embeddings using
`AUDIO_VIDEO_COMBINED`
mode (see
[Nova Multimodal Embeddings API schema](https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html)
), stores them in OpenSearch Service, and supports text-to-video, video-to-video, and hybrid search.

## Solution overview

The architecture consists of two main workflows—ingestion and search—that work together to enable multimodal video search at scale:

**Video ingestion pipeline:**

The ingestion pipeline uses four
[Amazon EC2](https://aws.amazon.com/ec2/)
c7i.48xlarge instances with 600 parallel workers to process 19,400 videos per hour. The async API has a concurrency limit of 30 concurrent jobs per account (see
[Amazon Bedrock quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
), so the pipeline implements a job queue with polling. Workers submit jobs up to the concurrency limit, poll for completion, and submit new jobs as slots become available.
[Amazon Nova Multimodal Embeddings](https://docs.aws.amazon.com/nova/latest/userguide/nova-embeddings.html)
handles video processing asynchronously, segmenting videos into 15-second chunks (optimized for capturing scene changes while keeping embedding counts manageable) and generating 1024-dimensional embeddings. Those embeddings were chosen over 3072-dimensional for 3x cost savings from the storage point of view with minimal accuracy impact. The embedding generation cost is agnostic to embedding dimensions.
[Amazon Nova Pro](https://docs.aws.amazon.com/nova/latest/userguide/prompting-video-understanding.html)
adds 10-15 descriptive tags per video from a predefined taxonomy.

Note:
[Amazon Nova 2 Lite](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/)
offers improved accuracy at lower cost for tagging tasks. We recommend that you consider it for new deployments. The system stores embeddings in an
[OpenSearch k-NN index](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
for semantic search and metadata tags in a separate text index for keyword matching. For search, you can query videos three ways: convert natural language to embeddings for text-to-video search, compare video embeddings directly for video-to-video search, or combine both approaches in hybrid search.

**Types of searches enabled by this solution:**

1. **Text-to-video Search**
   – Natural language queries converted to embeddings for semantic similarity matching
2. **Video-to-video Search**
   – Find similar content by comparing video embeddings directly
3. **Hybrid search**
   – Combines vector similarity (70% weight) with keyword matching (30% weight) for maximum accuracy

### Video ingestion pipeline

The following diagram illustrates the video ingestion and processing pipeline:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/l-ml-200121.png)

*Figure 1: Video ingestion pipeline showing the flow from S3 video storage through Nova Multimodal Embeddings and Nova Pro to dual OpenSearch indexes*

The video processing workflow is as follows:

1. Upload videos to
   [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
   .
2. Process videos using
   [Nova Multimodal Embeddings async API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_StartAsyncInvoke.html)
   , which automatically segments videos and generates embeddings. An orchestrator polls for job completion (async API has a 30 concurrent job limit per account, see
   [Amazon Bedrock quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
   ) and retrieves results from Amazon S3.
3. Generate descriptive tags using
   [Nova Pro](https://docs.aws.amazon.com/nova/latest/userguide/prompting-video-understanding.html)
   (or
   [Nova Lite](https://docs.aws.amazon.com/ai/responsible-ai/nova-2-lite/overview.html)
   for better accuracy at lower cost) from a predefined taxonomy for enhanced search capabilities.
4. Index embeddings in
   [OpenSearch k-NN index](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
   and tags in text index.

### Video search architecture

The following diagram shows the complete search architecture:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/l-ml-200122.png)

*Figure 2: Video search architecture demonstrating three search modes – text-to-video, video-to-video, and hybrid search combining k-NN and BM25*

The search architecture enables three modes:

1. **Text-to-video –**
   Natural language queries
2. **Video-to-video**
   – Similar content discovery
3. **Hybrid**
   – Combined semantic and keyword matching

## Prerequisites

Before you begin, you will need:

1. An
   [AWS account](https://aws.amazon.com/free/)
   with access to
   [Amazon Bedrock](https://aws.amazon.com/bedrock/)
   in
   `us-east-1`
   (Nova models are enabled by default with appropriate IAM permissions)
2. [Python](https://www.python.org/downloads/)
   3.9 or later installed
3. [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/)
   configured with appropriate credentials
4. An Amazon OpenSearch Service domain (r6g.large or larger recommended)
5. An
   [Amazon S3](https://aws.amazon.com/s3/)
   bucket for video storage and embedding outputs
6. [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
   for Amazon Bedrock, OpenSearch Service, and Amazon S3

The solution uses:

7. Amazon Bedrock with
   [Nova Multimodal Embeddings](https://docs.aws.amazon.com/nova/latest/userguide/nova-embeddings.html)
   (amazon.nova-2-multimodal-embeddings-v1:0)
8. Amazon Bedrock with
   [Nova Pro](https://docs.aws.amazon.com/nova/latest/userguide/prompting-video-understanding.html)
   (us.amazon.nova-pro-v1:0) or
   [Nova Lite](https://docs.aws.amazon.com/ai/responsible-ai/nova-2-lite/overview.html)
   (us.amazon.nova-2-lite-v1:0) for tagging
9. Amazon OpenSearch Service 2.11 or later with
   [k-NN plugin](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
10. Amazon S3 for video and embedding storage

## Walkthrough

### Step 1: Create IAM roles and policies

Create an
[IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
with permissions to invoke Amazon Bedrock models, write to OpenSearch indexes, and read/write S3 objects.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:StartAsyncInvoke",
        "bedrock:GetAsyncInvoke",
        "bedrock:ListAsyncInvoke"
      ],
      "Resource": [
        "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-2-multimodal-embeddings-v1:0",
        "arn:aws:bedrock:us-east-1::foundation-model/us.amazon.nova-pro-v1:0"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "es:ESHttpPost",
        "es:ESHttpPut",
        "es:ESHttpGet"
      ],
      "Resource": "arn:aws:es:us-east-1:ACCOUNT_ID:domain/DOMAIN_NAME/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-video-bucket/*",
        "arn:aws:s3:::amzn-s3-demo-embedding-bucket/*"
      ]
    }
  ]
}
```

### Step 2: Set up OpenSearch Service indexes

Create two
[OpenSearch Service indexes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdateindex.html)
: one for vector embeddings (
[k-NN](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
) and one for text metadata. This architecture supports semantic search and hybrid queries.

```
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

session = boto3.Session()
credentials = session.get_credentials()
awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    session.region_name,
    'es',
    session_token=credentials.token
)

opensearch_client = OpenSearch(
    hosts=[{'host': 'YOUR_OPENSEARCH_ENDPOINT', 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# Create k-Nearest Neighbors (k-NN) index for embeddings
knn_index_body = {
    "settings": {
        "index.knn": True,
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "video_id": {"type": "keyword"},
            "segment_index": {"type": "integer"},
            "timestamp": {"type": "float"},
            "embedding": {
                "type": "knn_vector",
                "dimension": 1024,
                "method": {
                    "name": "hnsw",
                    "space_type": "cosinesimilarity",
                    "engine": "faiss"
                }
            },
            "s3_uri": {"type": "keyword"}
        }
    }
}

opensearch_client.indices.create(
    index="video-embeddings-knn",
    body=knn_index_body
)

# Create text index for metadata
text_index_body = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "video_id": {"type": "keyword"},
            "segment_index": {"type": "integer"},
            "tags": {"type": "text", "analyzer": "standard"}
        }
    }
}

opensearch_client.indices.create(
    index="video-embeddings-text",
    body=text_index_body
)
```

### Step 3: Process videos with Nova Multimodal Embeddings

The
[Amazon Bedrock async API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_StartAsyncInvoke.html)
processes videos and generates embeddings. It segments videos into 15-second chunks and combines audio and visual information.

```
import boto3
import json
import time

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def generate_video_embeddings(video_s3_uri, output_s3_uri):
    """Generate embeddings for a video using Nova MME async API."""

    # Start async job
    response = bedrock.start_async_invoke(
        modelId="amazon.nova-2-multimodal-embeddings-v1:0",
        modelInput={
            "taskType": "SEGMENTED_EMBEDDING",
            "segmentedEmbeddingParams": {
                "embeddingPurpose": "GENERIC_INDEX",
                "embeddingDimension": 1024,
                "video": {
                    "format": "mp4",
                    "embeddingMode": "AUDIO_VIDEO_COMBINED",
                    "source": {"s3Location": {"uri": video_s3_uri}},
                    "segmentationConfig": {"durationSeconds": 15}
                }
            }
        },
        outputDataConfig={"s3OutputDataConfig": {"s3Uri": output_s3_uri}}
    )

    # Poll for completion
    invocation_arn = response["invocationArn"]
    while True:
        job = bedrock.get_async_invoke(invocationArn=invocation_arn)
        if job["status"] == "Completed":
            return read_embeddings_from_s3(job["outputDataConfig"]["s3OutputDataConfig"]["s3Uri"])
        elif job["status"] in ["Failed", "Expired"]:
            raise RuntimeError(f"Job failed: {job.get('failureMessage')}")
        time.sleep(10)

def manage_concurrent_jobs(bedrock_client, video_queue, max_concurrent=30):
    """Manage 30 concurrent async jobs within quota limits."""
    active_jobs = {}

    while video_queue or active_jobs:
        # Submit new jobs up to limit (uses same start_async_invoke call as above)
        while len(active_jobs) < max_concurrent and video_queue:
            video_info = video_queue.pop(0)
            response = bedrock_client.start_async_invoke(
                modelId="amazon.nova-2-multimodal-embeddings-v1:0",
                modelInput={...},  # Same model_input structure as generate_video_embeddings()
                outputDataConfig={"s3OutputDataConfig": {"s3Uri": video_info['output_uri']}}
            )
            active_jobs[response["invocationArn"]] = video_info

        # Poll all active jobs
        for arn in list(active_jobs.keys()):
            job = bedrock_client.get_async_invoke(invocationArn=arn)
            if job["status"] == "Completed":
                video_info = active_jobs.pop(arn)
                embeddings = read_embeddings_from_s3(job["outputDataConfig"]["s3OutputDataConfig"]["s3Uri"])
                # Process embeddings...
            elif job["status"] in ["Failed", "Expired"]:
                active_jobs.pop(arn)

        if active_jobs:
            time.sleep(10)

def read_embeddings_from_s3(s3_uri):
    """Read JSONL embeddings from S3. Returns list of {startTime, endTime, embedding} dicts."""
    # Download and parse JSONL from s3_uri (standard S3 GetObject + json.loads per line)
```

### Step 4: Generate metadata tags with Nova Pro or Nova Lite

Generate descriptive tags for videos using Nova Pro (or
[Nova Lite](https://docs.aws.amazon.com/ai/responsible-ai/nova-2-lite/overview.html)
for better accuracy at lower cost) to enable hybrid search that combines semantic and keyword matching.

```
VALID_TAGS = [
    "person", "vehicle", "animal", "building", "nature", "indoor", "outdoor",
    "walking", "running", "sitting", "standing", "talking", "driving",
    "day", "night", "sunny", "cloudy", "urban", "rural", "beach", "forest",
    "sports", "music", "food", "technology", "crowd", "solo"
]

def generate_tags(video_s3_uri, sample_frame_count=3):
    """Generate descriptive tags using Nova Pro or Nova Lite."""

    prompt = f"""Analyze this video and select 10-15 tags from this predefined list that best describe the content:
{', '.join(VALID_TAGS)}

Only return tags from this list as a comma-separated list. Do not invent new tags."""

    response = bedrock.converse(
        modelId="us.amazon.nova-pro-v1:0",  # Or use us.amazon.nova-2-lite-v1:0
        messages=[{
            "role": "user",
            "content": [{
                "video": {
                    "format": "mp4",
                    "source": {"s3Location": {"uri": video_s3_uri}}
                }
            }, {
                "text": prompt
            }]
        }]
    )

    # Parse tags from response and validate against taxonomy
    tags_text = response['output']['message']['content'][0]['text']
    tags = [tag.strip().lower() for tag in tags_text.split(',')]

    # Filter to only valid tags from our taxonomy
    valid_tags = [tag for tag in tags if tag in VALID_TAGS]

    return valid_tags
```

### Step 5: Index embeddings and tags in OpenSearch Service

Store the generated embeddings and tags in OpenSearch Service using
[bulk indexing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/indexing.html)
for efficiency.

```
from opensearchpy import helpers

def index_video_data(video_id, s3_uri, embeddings, tags):
    """Index embeddings and tags in OpenSearch."""

    # Prepare bulk actions for k-NN index
    knn_actions = []
    for idx, emb in enumerate(embeddings):
        doc_id = f"{video_id}_{idx}"
        knn_actions.append({
            "_index": "video-embeddings-knn",
            "_id": doc_id,
            "_source": {
                "video_id": video_id,
                "segment_index": idx,
                "timestamp": emb['start_time'],
                "embedding": emb['embedding'],
                "s3_uri": s3_uri
            }
        })

    # Bulk index embeddings
    helpers.bulk(opensearch_client, knn_actions)

    # Prepare bulk actions for text index
    text_actions = []
    for idx in range(len(embeddings)):
        doc_id = f"{video_id}_{idx}"
        text_actions.append({
            "_index": "video-embeddings-text",
            "_id": doc_id,
            "_source": {
                "video_id": video_id,
                "segment_index": idx,
                "tags": " ".join(tags)
            }
        })

    # Bulk index tags
    helpers.bulk(opensearch_client, text_actions)

    print(f"Indexed {len(embeddings)} segments for video {video_id}")
```

### Step 6: Implement search functionality

After ingestion completes, search the indexed videos three ways. The implementation targets low-latency queries.

#### Initialize OpenSearch Service client for search

First, create the OpenSearch Service client for search operations:

```
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

def create_opensearch_client():
    """Create OpenSearch client with AWS authentication."""
    session = boto3.Session(region_name='us-east-1')
    credentials = session.get_credentials()
    awsauth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        'us-east-1',
        'es',
        session_token=credentials.token
    )

    return OpenSearch(
        hosts=[{'host': 'YOUR_OPENSEARCH_ENDPOINT', 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=30
    )

# Create client
opensearch_client = create_opensearch_client()
```

#### Text-to-video semantic search

Convert natural language queries to embeddings using the sync API, then perform a k-NN similarity search:

```
def search_text_to_video(query_text, opensearch_client, k=10):
    """Search videos using natural language query converted to embedding."""

    bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

    # Use SINGLE_EMBEDDING task type for text-to-embedding conversion
    # VIDEO_RETRIEVAL purpose optimizes embeddings for searching video content
    request_body = {
        "taskType": "SINGLE_EMBEDDING",
        "singleEmbeddingParams": {
            "embeddingPurpose": "VIDEO_RETRIEVAL",
            "embeddingDimension": 1024,
            "text": {
                "truncationMode": "END",
                "value": query_text
            }
        }
    }

    response = bedrock_client.invoke_model(
        modelId='amazon.nova-2-multimodal-embeddings-v1:0',
        body=json.dumps(request_body),
        accept='application/json',
        contentType='application/json'
    )

    response_body = json.loads(response['body'].read())
    # Response structure: {"embeddings": [{"embeddingType": "TEXT", "embedding": [...]}]}
    query_embedding = response_body['embeddings'][0]['embedding']

    # Perform k-NN search against video embeddings
    search_body = {
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_embedding,
                    "k": k
                }
            }
        },
        "size": k,
        "_source": ["video_id", "segment_index", "timestamp", "s3_uri"]
    }

    response = opensearch_client.search(
        index="video-embeddings-knn",
        body=search_body
    )

    # Extract results
    return [{'score': hit['_score'],
             'video_id': hit['_source']['video_id'],
             'segment_index': hit['_source']['segment_index'],
             'timestamp': hit['_source'].get('timestamp', 0)}
            for hit in response['hits']['hits']]
```

#### Text search with BM25 (keyword matching)

Use the OpenSearch BM25 scoring for keyword matching on tags without generating embeddings:

```
def search_text_bm25(search_term, opensearch_client, k=10):
    """Search videos using BM25 keyword matching on tags field."""

    # Search text index using match query on tags
    search_body = {
        "query": {
            "match": {
                "tags": search_term
            }
        },
        "size": k,
        "_source": ["video_id", "segment_index", "tags"]
    }

    response = opensearch_client.search(
        index="video-embeddings-text",
        body=search_body
    )

    return response['hits']['hits']  # Extract results (same pattern as above)
```

#### Video-to-video search

Retrieve an existing video’s embedding from OpenSearch Service and search for similar content—no Amazon Bedrock API call needed:

```
def search_video_to_video(query_video_id, query_segment_index, opensearch_client, k=10):
    """Find similar videos using a reference video segment."""

    # Get the embedding from the reference video segment
    sample_query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"video_id": query_video_id}},
                    {"term": {"segment_index": query_segment_index}}
                ]
            }
        },
        "_source": ["video_id", "segment_index", "embedding"]
    }

    sample_response = opensearch_client.search(
        index="video-embeddings-knn",
        body=sample_query
    )

    if not sample_response['hits']['hits']:
        return []

    sample_doc = sample_response['hits']['hits'][0]['_source']
    query_embedding = sample_doc.get('embedding')

    # Perform k-NN search with the embedding
    search_body = {
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_embedding,
                    "k": k
                }
            }
        },
        "size": k,
        "_source": ["video_id", "segment_index", "timestamp"]
    }

    response = opensearch_client.search(
        index="video-embeddings-knn",
        body=search_body
    )

    return response['hits']['hits']  # Extract results as needed
```

#### Hybrid search

Combine semantic k-NN and BM25 keyword matching by retrieving results from both indexes and merging with weighted scoring:

```
def search_hybrid(query_text, opensearch_client, k=10, vector_weight=0.7, text_weight=0.3):
    """Hybrid search combining k-NN semantic search and BM25 text matching."""

    # Generate query embedding (use same code as search_text_to_video above)
    query_embedding = generate_query_embedding(query_text)  # See text-to-video example

    # Get k-NN results (same query as search_text_to_video)
    knn_response = opensearch_client.search(
        index="video-embeddings-knn",
        body={"query": {"knn": {"embedding": {"vector": query_embedding, "k": 20}}}, "size": 20}
    )

    # Get BM25 text results (same query as search_text_bm25)
    text_response = opensearch_client.search(
        index="video-embeddings-text",
        body={"query": {"match": {"tags": query_text}}, "size": 20}
    )

    # Combine results with weighted scoring
    knn_hits = knn_response['hits']['hits']
    text_hits = text_response['hits']['hits']

    combined = {}

    for hit in knn_hits:
        vid = hit['_source']['video_id']
        seg = hit['_source']['segment_index']
        key = f"{vid}_{seg}"
        combined[key] = {
            'video_id': vid,
            'segment_index': seg,
            'tags': hit['_source'].get('tags', ''),
            'vector_score': hit['_score'],
            'text_score': 0,
            'combined_score': hit['_score'] * vector_weight
        }

    for hit in text_hits:
        vid = hit['_source']['video_id']
        seg = hit['_source']['segment_index']
        key = f"{vid}_{seg}"
        if key in combined:
            combined[key]['text_score'] = hit['_score']
            combined[key]['combined_score'] += hit['_score'] * text_weight
        else:
            combined[key] = {
                'video_id': vid,
                'segment_index': seg,
                'tags': hit['_source'].get('tags', ''),
                'vector_score': 0,
                'text_score': hit['_score'],
                'combined_score': hit['_score'] * text_weight
            }

    # Sort by combined score and return top k
    sorted_results = sorted(combined.values(), key=lambda x: x['combined_score'], reverse=True)[:k]

    return sorted_results

# Usage example - search with natural language query
query = "person walking on beach at sunset"
hybrid_results = search_hybrid(query, opensearch_client, k=10)

for r in hybrid_results:
    print(f"Combined: {r['combined_score']:.4f} (Vector: {r['vector_score']:.4f}, Text: {r['text_score']:.4f})")
    print(f"  Video: {r['video_id']}, Segment: {r['segment_index']}")
    print(f"  Tags: {r['tags']}\n")
```

### Search performance at scale

After indexing all 792,218 videos, we measured search performance across all three methods.

**The measured query latencies at 792,218 videos are as follows:**

* Semantic k-NN search: ~76ms (using
  [HNSW](https://aws.amazon.com/blogs/big-data/choose-the-k-nn-algorithm-for-your-billion-scale-use-case-with-opensearch/)
  logarithmic scaling)
* [BM25](https://docs.opensearch.org/latest/im-plugin/similarity/)
  text search: ~30ms
* Hybrid search: ~106ms

After indexing and storing all 792,218 videos and generating embeddings, the storage requirements are as follows:

* k-NN index: 28.8 GB for 792K videos
* Text index: 1.0 GB for 792K videos
* Total: 29.8 GB (manageable on modern OpenSearch clusters)

The Hierarchical Navigable Small World (HNSW) algorithm used for k-NN search provides logarithmic time complexity, which means search times grow slowly as the dataset increases. All three search methods maintain sub-200 ms response times even at 792K video scale, meeting production requirements for interactive search applications.

## Things to know

### Performance and cost considerations

Video processing time depends on video length. In our testing, a 45-second video took approximately 70 seconds to process using the async API. The processing includes automatic segmentation, embedding generation for each segment, and output to Amazon S3. Search operations scale efficiently—our testing shows that even at 792K videos, semantic search completes in under 80 ms, text search in under 30 ms, and hybrid search in under 11 0ms.Use 1024-dimensional embeddings instead of 3072 to reduce storage costs while maintaining accuracy. Nova Multimodal Embeddings charges per second of video input ($0.00056/second batch), so video duration—not embedding dimension or segmentation—determines processing cost. The async API is more cost-effective than processing frames individually. For OpenSearch Service, using r6g instances provides better price-performance than earlier instance types, and you can implement tiering to move cold data to Amazon S3 for additional savings.

### Scaling to production

For production deployments with large video libraries, consider using
[AWS Batch](https://aws.amazon.com/batch/)
to process videos in parallel across multiple compute instances. You can partition your video dataset and assign subsets to different workers. Monitor
[OpenSearch Service cluster health](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html)
and scale data nodes as your index grows. The two-index architecture scales well because k-NN and text searches can be optimized independently.

### Search accuracy tuning

Tune hybrid search weights based on your use case. The default 0.7/0.3 split (vector/text) favors semantic similarity for most scenarios. If you have high-quality metadata tags, increasing the text weight to 0.5 can improve results. We recommend that you test different configurations with your specific content to find a balance.

## Cleanup

To avoid ongoing charges, delete the resources that you created:

1. Delete the
   [OpenSearch Service domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/delete-domain.html)
   from the Amazon OpenSearch Service console
2. Empty and delete the
   [S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)
   used for videos and embeddings
3. Delete any
   [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html)
   created specifically for this solution

Note that Amazon Bedrock charges are based on usage, so no cleanup is needed for the Amazon Bedrock models themselves.

## Conclusion

This walkthrough covered building a multimodal video search system for natural language queries across video content. The solution uses Amazon Bedrock Nova models to generate embeddings. These embeddings capture both audio and visual information, stores them efficiently in OpenSearch Service using a two-index architecture, and provides three search modes for different use cases.The async processing approach scales to handle large video libraries, and the hybrid search capability combines semantic and keyword-based matching for maximum accuracy. You can extend this foundation by adding features like video-to-video similarity search, implementing caching for frequently searched queries, or integrating with AWS Batch for parallel processing of large datasets.

To learn more about the technologies used in this solution, see
[Amazon Nova Multimodal Embeddings](https://aws.amazon.com/blogs/aws/amazon-nova-multimodal-embeddings-now-available-in-amazon-bedrock/)
and
[Hybrid Search with Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/hybrid-search-with-amazon-opensearch-service/)
.

---

## About the authors