---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-04T16:15:40.575097+00:00'
exported_at: '2026-05-04T16:15:43.666905+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/from-data-lake-to-ai-ready-analytics-introducing-direct-query-with-s3-tables-in-amazon-quick
structured_data:
  about: []
  author: ''
  description: Amazon Quick introduces Amazon S3 Tables (Apache Iceberg tables) as
    a new data source. With this feature, customers can directly query and visualize
    Apache Iceberg tables stored in an Amazon S3 table bucket without the need for
    intermediate data layers. In this post, we explored how Amazon Quick’s new Amazon
    S3 Tabl...
  headline: 'From data lake to AI-ready analytics: Introducing new data source with
    S3 Tables in Amazon Quick'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/from-data-lake-to-ai-ready-analytics-introducing-direct-query-with-s3-tables-in-amazon-quick
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'From data lake to AI-ready analytics: Introducing new data source with S3
  Tables in Amazon Quick'
updated_at: '2026-05-04T16:15:40.575097+00:00'
url_hash: b210398c71ba638f85cb0c35fab16c72d9a20c81
---

Organizations today are increasingly looking to combine analytics and AI to accelerate insights and decision-making.
[Amazon Quick](https://aws.amazon.com/quick/)
, a unified agentic AI-powered analytics and decision intelligence service, brings together data visualization, natural language interaction, and agent-driven automation in a single, governed experience. With this, business users can explore data, generate insights, and take action without requiring specialized machine learning (ML) expertise.

At the same time, modern data architectures are evolving toward scalable data lakes built on open table formats such as Apache Iceberg, which offer improved performance, cost efficiency, and governance. However, analyzing large-scale data often requires moving it into data warehouses or OLAP systems, introducing latency, added cost, and operational complexity. Although existing query modes—such as Direct Query and SPICE (
*Super-fast, Parallel, In-memory Calculation Engine*
) with data warehouses —address most analytics needs, customers continue to seek a more seamless way to analyze large, real-time datasets directly from their data lakes.

To address this, Amazon Quick introduces
[Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/)
(Apache Iceberg tables) as a new data source. With this feature, customers can directly query and visualize Apache Iceberg tables stored in an Amazon S3 table bucket without the need for intermediate data layers. This approach provides additional architectural choice especially when customers are requiring to reduce data movement, improve performance, and maintain a secure, governed single source of truth.

In this post, we explore how Amazon Quick and S3 Tables work together to enable near real-time analytics and streamline modern data architectures.

## Benefits of directly connecting with S3 Tables:

*Direct Query and SPICE modes for S3 Tables*
, a new Amazon Quick feature, enables direct consumption of Apache Iceberg tables in Amazon S3 table bucket without requiring intermediate query layers. This feature is beneficial for enterprise looking to implement modern data architecture using Apache Iceberg open table format to treat their data lake as a “central source of truth,” enabling high-performance analytics without complex data pipeline and the overhead of moving data between disparate systems.

Key benefits include:

* **Streamlined architecture**

  Removes the need for separate data warehouses or OLAP layers by enabling direct querying of data in the data lake, reducing operational complexity and infrastructure overhead.
* **Near real-time insights**

  Minimizes data movement and pipeline dependencies, ensuring dashboards and analytics reflect the most current data available.
* **Scalable performance**

  Supports querying large-scale datasets stored in Amazon S3 table bucket without requiring data curation, replication, or size constraints—enabling seamless scalability.

## Solution overview

With this new launch, Amazon Quick now supports querying data lakes using either SPICE or Direct Query mode. In this post, we focus on Direct Query mode, though you can choose SPICE mode when creating your dataset.

This solution enables near real-time analytics and decision-making for AnyCompany Corp., a global financial services organization handling card transactions across multiple regions. Transaction data is generated from diverse sources, including point-of-sale systems, mobile banking apps, IoT-enabled payment devices, and online gateways. To address the need for fraud detection, approval rate monitoring, and fast access to actionable insights, the solution uses a combination of streaming data ingestion, open table format data lakes, and AI-powered analytics.

Transaction events are streamed into Amazon Kinesis Data Streams and delivered using Amazon Data Firehose into an Amazon S3 table bucket. With the native S3 Tables connector of Quick, business users can query the data lake in near real-time and analyze data using natural language interactions, removing dependency on batch processing. You can use this unified approach to uncover insights such as regional fraud trends and approval rates instantly, improving operational visibility and supporting faster, data-driven decisions.

### Architecture overview

The architecture is composed of four core layers: data ingestion, storage, querying, and analytics. For this post, we focus on the
*query*
and
*analytics*
layer. Transaction events from distributed payment systems are ingested in real-time using Amazon Kinesis Data Streams, providing a scalable, low-latency streaming layer. These events are continuously delivered to an Amazon S3 table bucket in Apache Iceberg format, forming a high-performance data lake that supports both streaming and analytical workloads. While data could traditionally be queried through Amazon Athena, Amazon Quick allows direct, near real-time querying of S3 Tables and enables AI-powered, natural language analysis. Business users can explore live datasets, generate visualizations, and obtain insights—such as identifying regions with high fraud rates in the last hour—without technical expertise. This architecture keeps decisions informed by the most current data, supporting rapid and accurate business actions.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/23/ml-20936-arch.png)

## Prerequisites

To follow along with this post, ensure that you have the following in place:

* Your steaming pipeline including data ingestion and storage layers are already set up and your data is available in an Amazon S3 table bucket.
* An Amazon
  [Quick Enterprise](https://aws.amazon.com/quick/pricing/)
  subscription.

## Implementation steps

Here are the steps to give your business users access to your Apache Iceberg tables using Amazon Quick analytical and conversational workloads:

### Step 1: Enable S3 Tables data access for Amazon Quick

Let’s start by configuring Amazon Quick to access S3 Tables, so they can be automatically discovered when building the data source.

1. Select your account name in the top-right corner and select
   **Manage account**
   .
2. In the left navigation menu, under
   **Permissions**
   , choose
   **AWS Resources**
   .
3. In the
   **Allow access and auto discovery for these resources**
   section, select
   **Amazon S3 Tables**
   .
4. Choose
   **Select S3 table buckets**
   , then choose the relevant S3 table bucket containing the sample data for this blog and click
   **Finish**
   . (For this post, we use the
   **s3table-datasamples**
   bucket.)
5. Ensure that the
   **Amazon S3 bucket**
   option is selected, then choose
   **Save**
   .

This step adds required permission to your Amazon Quick role and allows your Amazon Quick instances to successfully discover the specific S3 table bucket data while creating a data source.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20936/ML-20936-2.gif)

### Step 2: Create an Amazon Quick data source using S3 Tables

Now, let’s create an Amazon Quick data source pointing to the
**s3table-datasamples**
bucket. This bucket contains two tables:
**customer**
dimension and
**transaction\_events**
. The
**customer**
dimension table is file-based and includes fictional bank customer information, while
**transaction\_events**
represents fictional streaming credit card transaction data associated with those customers.

1. Choose
   **Amazon Quick**
   in the top-left corner to navigate to the Quick home page.
2. From the menu, select
   **Datasets**
   , then go to the
   **Data sources**
   tab and choose
   **Create data source**
   .
3. On the next screen, select
   **Amazon S3 Tables (Apache Iceberg tables)**
   as the data source type, then choose
   **Next**
   .
4. Enter a data source name (for example,
   *CustomerTrxn-S3Tables*
   ) and provide the S3 table bucket ARN. In this example, it’s the ARN for the
   **s3table-datasamples**
   bucket.
5. Choose
   **Create data source**
   .

*Verify that the data source has been created successfully.*

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/22/ML-20936-3.gif)

### Step 3: Build a dataset in Amazon Quick

In this step, we use the data source created earlier to build a dataset.

1. Select the data source (
   *CustomerTrxn-S3Tables*
   ) created in the previous step and choose
   **Create dataset**
   .
2. Choose the namespace automatically populated for your data source, then select a table from the list and click
   **Edit/Preview data**
   .

   *In this example, the s3table-data namespace contains two tables. We begin with the customer dimension table.*
3. In the
   **Preview**
   tab, review the data pulled from S3 Tables.
4. To add another table, select
   **Add data**
   from the menu.
   *In this example, we will add the
   `transaction_events`
   table.*
5. In the
   **Add data**
   screen, select
   ***Data source***
   from the dropdown list.
6. Choose
   `CustomerTrxn-S3Tables`
   from the
   **Select a data source**
   list, and then choose
   **Select**
   .
7. From the list of tables, select
   `transaction_events`
   and choose
   **Select**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/22/ML-20936-4.gif)

8. Join the two tables by selecting the plus
   **(+)**
   icon next to the
   **customer\_master**
   table and selecting
   **Join**
   .
9. Configure the join using the
   **customer\_id**
   column:
   1. Select the
      **Inner Join**
      option.
   2. Choose
      **transaction\_events**
      as the right table.
   3. Select
      **customer\_id**
      from both the left and right tables as the join keys.
   4. Provide a name for the join (for example, TrxnJoin) to help identify it when working with multiple tables.
10. Name the dataset in the top-left corner (for example, CxTrxn\_S3TableData).
11. Ensure that
    **Direct Query mode**
    is selected in the top-right corner. This is important to fully use near real-time data access from S3 Tables. Alternatively, you can choose
    **SPICE mode**
    if you prefer scheduled data refreshes rather than near real-time access.
12. Choose
    **Save & Publish**
    .

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20936/ML-20936-5.gif)

### Step 4: Interact with the dataset using Amazon Quick chat

Now let’s start chatting with this dataset to gather insights using natural language. For this, we use the default chat named, “My Assistant.”

1. In the Amazon Quick home page, choose
   **Chat agents**
   on the left navigation panel and then
   **My Assistant**
   .
2. Choose
   ***Chat***
   next to the
   **My Assistant**
   .
3. From
   **All data and apps**
   , choose
   **Add**
   and select
   **Datasets**
   . Then select the
   ***CxTrxn\_S3TableData***
   dataset. Choose
   **Save.**
4. In the chat panel, enter “
   *Show the total number of transactions occurred so far in this month*
   ” and press
   **Send**
   .
5. Notice the chat response showing the total transaction count for the current month. Next, let’s ask the agent to break it down by day.
6. In the chat panel, enter “
   *break it down by day using ingestion timestamp*
   ” and press
   **Send**
   .
7. Review the daily breakdown provided by the agent. In our example, from April 1–April 17.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20936/ML-20936-6.gif)

### Step 5: Demonstrate real-time user interaction with streaming data

Next, we test the near real-time responsiveness of the chat by streaming new transaction data. In this demo, we use AWS Lambda as a producer for a Kinesis Data Stream and then store the incoming data in an S3 table bucket as S3 Tables – in Apache Iceberg format using Firehose. As new data is streamed in, the transaction counts will automatically update within the chat without the end user needing to take any action. This demonstrates seamless near real-time data access without manual intervention or complex architecture. We run this Lambda function a few times to stream new transactional events data.

If you’re interested in creating your own streaming source for this demo, you can refer to the official
[AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-firehose.html)
or relevant AWS
[posts](https://aws.amazon.com/blogs/storage/build-a-data-lake-for-streaming-data-with-amazon-s3-tables-and-amazon-data-firehose/)
for detailed guidance.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20936/ML-20936-7.gif)

Now let’s check the recently streamed data in our chat agent.

1. Navigate back to
   **My Assistant**
   in the same chat session
   *,*
   enter a new prompt
   *“Show the total number of transactions occurred so far in this month, include all recent streaming data and break it down by ingestion timestamp.”*
   and press
   **Send**
   *.*
2. **My Assistant**
   queries
   *the*
   ***CxTrxn\_S3TableData***

   dataset via Direct Query and returns the newly ingested records for April 18. This demonstrates that the recently streamed data is available without requiring a manual dataset refresh.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20936/ML-20936-8.gif)

## Cleanup

If you no longer need the resources deployed as part of this solution and want to avoid ongoing costs, we recommend that you clean up and remove the relevant components by deleting all Amazon Quick–related resources and unsubscribing from your Amazon Quick account.

## Conclusion

In this post, we explored how Amazon Quick’s new Amazon S3 Tables data source enables near real-time analytics while streamlining modern data architectures. By querying Apache Iceberg tables directly in Amazon S3, it removes intermediate layers, reduces data movement, and preserves a single, governed source of truth. Additionally, you can use natural language chat experiences, like
**My Assistant**
, to access up-to-date insights effortlessly, without manual refreshes or technical overhead.

The result is a unified, AI-powered analytics experience where data, insights, and actions come together seamlessly in near real-time. Organizations can move faster, make better decisions, and unlock the full value of their data—while keeping architectures simpler, more scalable, and cost-efficient. If your use case is a typical analytical scenario sourced from scheduled data refreshes and does not require near real-time access,
**SPICE mode**
remains a suitable option. For more details on this feature, see
[Creating a dataset using Amazon S3 Tables](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3-tables.html)
.

For additional discussions and help getting answers to your questions, check out the
[Amazon Quick Community](https://community.amazonquicksight.com/)
.

---

## About the authors

**Raji Sivasubramaniam**
is a Principal Solutions Architect at AWS, specializing in Agentic AI. She focuses on helping Fortune 100 and 500 organizations globally implement end-to-end enterprise solutions across Agentic AI, business intelligence, data management, and advanced analytics. Raji brings deep expertise in healthcare, with extensive experience navigating diverse datasets—including managed markets, physician targeting, and patient analytics—to drive high-impact, data-driven decision-making.

**Emily Zhu**
is a Senior Product Manager at Amazon Quick, responsible for the full structured data stack — spanning governed and enterprise-scale data architecture, high-performance analytical and conversational query engines, and the semantic and ontology layer that gives data real meaning at scale. She’s passionate about how a strong data strategy unlocks AI strategy, and is on a mission to make the structured data stack the foundation for conversational and analytical experiences across Quick Suite.

**Priya Kakarla**
is a Specialist Solutions Architect focused on modern analytics and AI-driven solutions, with experience across industries including healthcare, finance, and digital-native organizations. She is passionate about helping organizations unlock value from their data through scalable, intuitive, and agentic-driven approaches. Known for a strong customer-first mindset, Priya is dedicated to delivering tailored, innovative solutions that align with business goals and drive measurable outcomes. Outside of work, she enjoys traveling, exploring diverse cuisines, and spending time with family and friends.