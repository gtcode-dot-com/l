---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:43:33.939496+00:00'
exported_at: '2026-09-30T02:43:35.328648+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-feature-store-introduces-updaterecord-for-feature-level-writes
structured_data:
  about: []
  author: ''
  description: Amazon SageMaker Feature Store now supports feature-level writes. With
    the new UpdateRecord API, you can update one or more feature values in a single
    call without reading or rewriting the entire record. It is available for both
    the Standard (Amazon DynamoDB) and In-Memory (Amazon ElastiCache) online store
    tiers.
  headline: Amazon SageMaker Feature Store introduces UpdateRecord for feature-level
    writes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-feature-store-introduces-updaterecord-for-feature-level-writes
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Amazon SageMaker Feature Store introduces UpdateRecord for feature-level writes
updated_at: '2026-09-30T02:43:33.939496+00:00'
url_hash: e5760113b544149a2a51b9c52641efc51ea94402
---

We are excited to announce
[*feature-level writes*](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html)
for Amazon SageMaker Feature Store.
[Amazon SageMaker Feature Store](/sagemaker/ai/feature-store/)
is a fully managed, purpose-built repository to store, share, and manage machine learning (ML) features, the processed data used for training models and generating predictions. With the new UpdateRecord API, you can now update one or more feature values in a single call without reading or rewriting the entire record. This capability is available for both the
*Standard*
(
[Amazon DynamoDB](/dynamodb/?)
-backed) and
*In-Memory*
(
[Amazon ElastiCache](/elasticache/?)
-backed) online store tiers.

## The challenge: Full-record writes for every change

A Feature Group is a logical collection of features that are related, and are used by one or more ML models to either train a new model or generate inference predictions. Until now, updating even a single feature value in a feature group required a full read-modify-write cycle using
[PutRecord](https://docs.aws.amazon.com/boto3/latest/reference/services/sagemaker-featurestore-runtime/client/put_record.html)
. If your fraud-scoring pipeline needed to refresh a customer’s
`risk_score`
, your application had to:

1. **Read**
   the complete record (all features) by using
   [GetRecord](https://docs.aws.amazon.com/boto3/latest/reference/services/sagemaker-featurestore-runtime/client/get_record.html)
   .
2. **Merge**
   the new value in application code.
3. **Write**
   the entire record back with
   [PutRecord](https://docs.aws.amazon.com/boto3/latest/reference/services/sagemaker-featurestore-runtime/client/put_record.html)
   .

This pattern added extra latency per update, consumed unnecessary read capacity, and introduced race conditions when multiple pipelines concurrently updated different features in the same record. In the worst case, one pipeline’s write could silently overwrite another’s. This is a classic lost-update problem.

Beyond latency and correctness issues, the read-modify-write pattern also carries a cost overhead. The additional GetRecord calls required before each write generate extra
[Read Capacity Units (RCUs)](/sagemaker/ai/pricing/)
charges. For customers operating at scale with wide feature groups and high update frequencies, these costs add up quickly.

## Introducing UpdateRecord

The
[UpdateRecord API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html)
call removes the read-modify-write cycle. You provide only the features that you want to change, and Amazon SageMaker Feature Store applies the updates atomically to the existing record. Features you don’t include in the request are preserved as-is.

### UpdateRecord API data flow

The following diagram illustrates how the UpdateRecord API processes a partial write request and synchronizes with the offline store.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/09/03/Screenshot-2026-09-03-at-11.34.17%E2%80%AFAM.png)

Figure 1: UpdateRecord API data flow to the online and offline stores

The client application calls the UpdateRecord API with only the changed features. The Feature Store service validates AWS Identity and Access Management (IAM) permissions, checks EventTime ordering to reject stale writes, and performs an atomic merge. The blue arrow represents the single operation that writes only the changed features to the online store. Meanwhile, a full record snapshot is automatically replicated to the offline store to keep training datasets accurate. Multiple pipelines (clickstream, purchases, scoring) each write their own features independently to the same record. No coordination is needed.

### Request shape

```
POST /FeatureGroup/{FeatureGroupName}/Record

{
  "RecordIdentifierValueAsString": "user_123",
  "Features": [
    { "FeatureName": "risk_score", "ValueAsString": "0.87" },
    { "FeatureName": "last_login", "ValueAsString": "2026-07-21T08:15:00Z" }
  ],
  "TtlDuration": {  // optional
    "Unit": "Days",
    "Value": 30
  }
}
```

* **FeatureGroupName**
  — the target feature group.
* **RecordIdentifierValueAsString**
  — the primary key of the record to update. The record must already exist (UpdateRecord is not an upsert).
* **Features**
  — a list of one or more feature values to set. Up to 100 features per call.
* **TtlDuration**
  (optional) — override or set a per-record time-to-live (TTL). If provided, EventTime must also be present.

**Updating EventTime**
: To also update the EventTime (one of two required fields) stored with the record, provide a new value in the
*Features*
parameter list. For the update to persist, this EventTime must be newer (a later timestamp) than the existing EventTime stored for the record. Otherwise, the entire update record call is rejected with an HTTP 409 error.

For more Error details, refer to
[this documentation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html#API_feature_store_UpdateRecord_Errors)
.

## Things to know: New storage format Standard\_V2

The
[Amazon SageMaker Feature Store online storage](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations-online-store.html)
has traditionally offered two tiers, each with its own backend storage provider.
*Standard Tier*
is backed by Amazon DynamoDB, and the
*In-Memory Tier*
is backed by
[Amazon ElastiCache (Redis OSS).](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
There is now a new storage format for the Standard Tier named
[Standard\_V2](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations-online-store.html#feature-store-storage-configurations-online-store-standard-v2-tier)
. This represents a different serialization format that supports additional capabilities such as feature-level writes.

**Note:**
If using the In-Memory tier, no new storage type is needed and feature-level writes work on all existing In-Memory feature groups out of the box.

Using feature-level writes with the Standard Tier will require the new Standard\_V2 storage format. You opt in at feature group creation time with this syntax:

```
import boto3

sm = boto3.client("sagemaker")

sm.create_feature_group(
    FeatureGroupName="user-profile-fg",
    RecordIdentifierFeatureName="user_id",
    EventTimeFeatureName="event_time",
    OnlineStoreConfig={
        "EnableOnlineStore": True,
        "StorageType": "Standard_V2"  # enables feature-level writes
    },
    FeatureDefinitions=[
        {"FeatureName": "user_id", "FeatureType": "String"},
        {"FeatureName": "event_time", "FeatureType": "String"},
        {"FeatureName": "risk_score", "FeatureType": "Fractional"},
        {"FeatureName": "last_login", "FeatureType": "String"},
        {"FeatureName": "balance", "FeatureType": "Fractional"},
    ],
)
```

### Migrating existing feature groups from Standard to Standard\_V2

If you already have feature groups on the original Standard storage type, you can migrate to Standard\_V2 to benefit from feature-level writes and maintain the same capabilities from Standard tier. The following sections describe two migration strategies. Your choice depends on your sensitivity to downtime, your preferred migration timing, and whether you want the option to roll back.

**Strategy A: Bulk migration with Feature Processor**

* Use the
  [Feature Processor SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-sdk.html)
  to read records from the existing Standard feature group and re-ingest them into a new Standard\_V2 feature group.
* Pros: You control the timing. The original feature group stays intact during migration. Rollback is straightforward, because you switch back to the old feature group.
* Cons: This strategy requires a managed migration job. You pay the full read and write cost for the entire dataset upfront. You must update application clients to point to the new feature group name.

**Strategy B: In-place controlled switchover with UpdateFeatureGroup API**

Call UpdateFeatureGroup with OnlineStoreConfig.StorageType = “Standard\_V2” to flip the feature group’s storage format in place:

```
import boto3
sm = boto3.client("sagemaker")

sm.update_feature_group(
    FeatureGroupName="my-existing-fg",
    OnlineStoreConfig={"StorageType": "Standard_V2"}
)
```

Once the feature group is declared to be in Standard\_V2 format, Calls to PutRecord or BatchWriteRecord update the underlying format to Standard\_V2.

This approach requires zero downtime and charges migration cost only for records that are actually touched. It preserves existing application code, because the feature group name and API endpoints remain unchanged. The switch to Standard\_V2 is irreversible, and cold records that are never written linger in the legacy format until touched.

Recommendation: For most customers, Strategy B (in-place UpdateFeatureGroup) is the preferred approach because of zero downtime and pay-per-touch economics. Use Strategy A only if you require a fully reversible migration path or need to rename or restructure the feature group.

## EventTime: Temporal ordering built in

UpdateRecord supports the same EventTime-based ordering as PutRecord. When you include an EventTime in your request:

* If the provided EventTime is newer than or equal to the record’s current EventTime, the update is applied and the record’s EventTime advances.
* If the provided EventTime is earlier than the record’s current EventTime, the update is rejected with a 409 ConflictException. This helps prevent stale or out-of-order events from overwriting fresher data.

When EventTime is omitted, the update applies new feature changes while the existing EventTime on the record is left unchanged. This is ideal for multi-pipeline architectures where different pipelines own different features and don’t share a single event clock.

## Use cases

The following use cases demonstrate how UpdateRecord simplifies common feature engineering workflows.

### Streaming feature hydration

Real-time and streaming scenarios typically require data generated by multiple streams that occur at different frequencies.

**Scenario**
: A real-time clickstream pipeline receives
`page_views`
and
`session_duration`
data every few seconds, and a nightly batch pipeline refreshes
`lifetime_value`
and
`customer_segment`
data. With UpdateRecord, each pipeline submits only the features it owns to the core record, with no coordination and no lost updates.

### Backfilling new features

With Amazon SageMaker Feature Store, you can modify the table schema that backs the feature group to add new columns (features).

**Scenario**
: Your team adds
`preferred_language`
and
`notification_opt_in`
to an existing feature group. Instead of rewriting every record, you call UpdateRecord with only the new field values. Existing feature values remain untouched.

### Error correction at scale

When a data science or MLOps team discovers discrepancies in existing feature data, they can now take action to correct it efficiently.

**Scenario:**
A data-quality job discovers that
`customer_segment`
is miscategorized for 50,000 records. With UpdateRecord, you can fix one field across thousands of records without risking corruption of other feature values.

### High-velocity feature updates

Feature Groups often contain multiple fields of transactional data, even though these fields are generated or received at different times.

**Scenario**
: A fraud detection system receives
`transaction_velocity`
on every card swipe. With UpdateRecord, each write touches only the single feature that changed, which eliminates the overhead of full-record writes at scale.

### Multi-producer feature groups for enterprise entities

Large organizations often model their Feature Store around core business entities, one feature group per entity type, with dozens of independent producers contributing features to the same records.

**Scenario:**
An enterprise maintains a single feature group per business entity (for example, customer, policy, vehicle). The group holds millions of records and hundreds of features produced by different teams, batch extract, transform, and load (ETL) jobs, streaming analytics, and real-time scoring engines. Without UpdateRecord, each producer must read the full record, inject its subset, and write back the entire entity. This creates compaction jobs, race conditions, and monthly costs in read and write operations. With UpdateRecord, each producer writes only its own features atomically, which removes the need for custom compaction solutions.

## Fine-grained access control

UpdateRecord integrates with IAM so you can control exactly who can update which features. Two new IAM condition keys are available:

* **sagemaker:IsUpdateRecord**
  (Bool) — distinguish partial-update operations from full PutRecord writes.
* **sagemaker:UpdatableFeatures**
  (ArrayOfString) — restrict which feature names a principal is allowed to update.

### Example: Allow updates only to non-sensitive features

```
{
  "Effect": "Allow",
  "Action": "sagemaker:PutRecord",
  "Resource": "arn:aws:sagemaker:*:*:feature-group/user-profile-fg",
  "Condition": {
    "Bool": { "sagemaker:IsUpdateRecord": "true" },
    "ForAllValues:StringEquals": {
      "sagemaker:UpdatableFeatures": ["age", "score", "last_activity"]
    }
  }
}
```

This policy allows the principal to call UpdateRecord on
`age`
,
`score`
, and
`last_activity`
but blocks updates to any other features (for example,
`ssn`
or
`salary`
) and blocks direct PutRecord calls entirely.

### Backward compatibility

Existing IAM policies that deny sagemaker:PutRecord automatically block UpdateRecord as well. No customer migration is required for security controls to take effect.

## Offline store integration

Updates made through UpdateRecord flow to the offline store automatically through the same replication pipeline used by PutRecord. Each update emits a complete record snapshot to the offline store, helping you maintain accurate training datasets and historical analytics.

* **Record must exist.**
  UpdateRecord is strictly a modify operation. Call PutRecord first to create the record.
* **Feature names must be defined.**
  You can’t add features that aren’t in the feature group’s schema. Use PutRecord for schema-conformant full writes.
* **Record identifier is immutable.**
  The primary key can’t be modified by using UpdateRecord.
* **TTL requires EventTime.**
  If you specify a TtlDuration, you must also include EventTime in the request.

## Pricing

UpdateRecord follows the same pricing model as PutRecord. For the Standard tier, DynamoDB write capacity unit (WCU) charges are based on the item size after the update. However, you save on the read capacity that was previously required for the read-modify-write pattern. Consult the
[Amazon SageMaker Feature Store pricing page](/sagemaker/ai/pricing/)
for details.

## Getting started today

Feature-level writes with UpdateRecord is available today in all AWS Regions where Amazon SageMaker Feature Store is offered. To get started:

1. Create a feature group with StorageType: Standard\_V2 (Standard tier) or use any existing In-Memory feature group.
2. Ingest records using PutRecord as usual.
3. Call UpdateRecord to update individual features without rewriting the full record.

For more information, see the
[Amazon SageMaker Feature Store Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
and the
[UpdateRecord API Reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html)
.

## Conclusion

Feature-level writes with the UpdateRecord API to remove the read-modify-write cycle that previously added extra ms of latency to every partial update. UpdateRecord reduces latency, lowers data-transfer costs for single-feature updates, and helps minimize the risk of lost updates in multi-pipeline architectures.

Combined with fine-grained IAM controls and automatic offline store replication, teams can build more efficient and reliable feature engineering workflows. Whether refreshing a single risk score in real time or orchestrating dozens of independent producers writing to shared enterprise-wide feature groups, UpdateRecord simplifies the path from raw data to production-ready features.

To learn more, see the
[Amazon SageMaker Feature Store Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
, the
[UpdateRecord API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html)
Reference, or get started on the AWS Management Console.

---

## About the authors

### Mona Mona

Mona is a Specialist Solutions Architect at AWS, focused on machine learning infrastructure and AI/ML services. She helps customers design and optimize their ML pipelines using Amazon SageMaker.

### Ioan Catana

Ioan is a Senior Artificial Intelligence and Machine Learning Specialist Solutions Architect at AWS. He helps customers develop and scale their ML solutions and generative AI applications in the AWS Cloud. Ioan has over 25 years of experience, mostly in software architecture design and cloud engineering.

### Paul Hargis

Paul is a Principal Solutions Architect at AWS specializing in machine learning and data engineering. He works with enterprise customers to build scalable ML platforms.

### Romik Amipara

Romik is a software engineer on the SageMaker Feature Store team, passionate about building elegant, scalable systems that bring big data and machine learning to people’s fingertips. His interests lie at the intersection of distributed systems and the rapidly evolving world of AI, with a focus on building reliable infrastructure that enables intelligent applications at scale.

### Siamak Nariman

Siamak is a Senior Product Manager at AWS. He is focused on AI/ML technology, ML model management, and ML governance to improve overall organizational efficiency and productivity. He has extensive experience automating processes and deploying various technologies.