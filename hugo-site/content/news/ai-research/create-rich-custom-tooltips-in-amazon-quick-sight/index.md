---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-15T16:15:43.265281+00:00'
exported_at: '2026-04-15T16:15:47.989009+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/create-rich-custom-tooltips-in-amazon-quick-sight
structured_data:
  about: []
  author: ''
  description: Today, we're announcing sheet tooltips in Amazon Quick Sight. Dashboard
    authors can now design custom tooltip layouts using free-form layout sheets. These
    layouts combine charts, key performance indicator (KPI) metrics, text, and other
    visuals into a single tooltip that renders dynamically when readers hover over
    da...
  headline: Create rich, custom tooltips in Amazon Quick Sight
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/create-rich-custom-tooltips-in-amazon-quick-sight
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Create rich, custom tooltips in Amazon Quick Sight
updated_at: '2026-04-15T16:15:43.265281+00:00'
url_hash: 1b6b6a5d7818ab6cda080e4af2079ea8305910d0
---

Amazon Quick Sight, the business intelligence (BI) capability of Amazon Quick, is a unified BI service. It provides modern interactive dashboards, natural language querying, pixel-perfect reports, machine learning (ML) insights, and embedded analytics at scale. Amazon Quick brings together AI agents for business insights, research, and automation in one integrated experience, helping you work smarter and faster while maintaining security and access policies.

Today, we’re announcing sheet tooltips in Amazon Quick Sight. Dashboard authors can now design custom tooltip layouts using free-form layout sheets. These layouts combine charts, key performance indicator (KPI) metrics, text, and other visuals into a single tooltip that renders dynamically when readers hover over data points. Sheet tooltips work with most chart types, including tables and pivot tables, and authors can reuse the same tooltip sheet across multiple visuals for a consistent experience. With this feature, you have more control over how contextual information appears, and you can create richer data storytelling without requiring readers to navigate away from the visual they’re exploring.

## Solution overview

With sheet tooltips, you can now:

* Design custom tooltip layouts using the free-form sheet editor
* Include multiple visual types within a single tooltip, such as line charts, bar charts, and text boxes
* Display dynamic, real-time data that updates as readers hover over different data points
* Add contextual metrics like revenue, units sold, and total orders alongside trend visualizations
* Create visually rich tooltip experiences that go beyond text-based data labels
* Enhance data storytelling by surfacing supplementary insights on hover

This feature uses a dedicated tooltip sheet type with a free-form layout, giving you the flexibility to arrange visual components exactly how you want. The tooltip sheet supports up to 5 visuals and filters data dynamically based on the data point you hover over.

## Prerequisites

Before you begin, make sure you have the following:

* An active AWS account with permissions to access Amazon Quick Sight
* Quick Sight Enterprise Edition enabled in your account
* Author or Author Pro access to create and manage analyses and dashboards
* Basic familiarity with Quick Sight concepts such as analyses, dashboards, sheets, and visual types

## Getting started with sheet tooltips

The following walkthrough demonstrates how to set up a sheet tooltip using a sales dashboard as an example. You can apply the same approach to any use case. Simply substitute the visuals and metrics that are relevant to your data.

Complete the following steps to create a sheet tooltip for your Quick Sight visuals:

### Step 1: Navigate to the Interactions tab

1. In the Amazon Quick console, in the left pane, under Quick Sight, choose an analysis
   **.**
2. Choose any visual on your dashboard sheet, such as a bar chart or table, and choose Edit visual.
3. In the
   **Properties**
   panel on the right, navigate to the Interactions tab.
4. Under the
   **Tooltip**
   configuration, select
   **Sheet tooltip**
   as shown in the following example.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-1.jpg)

5. Choose
   **Create sheet tooltip**
   to build one for your use case.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-2.jpg)

### Step 2: Design and publish your tooltip sheet

1. Quick Sight analysis opens a new
   **tooltip**
   sheet with a free-form layout, providing a blank canvas for your tooltip design. Add up to 5 visuals to the tooltip sheet. Resize and format them to fit your layout

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-3.jpg)

2. After configuring the settings, navigate back to your main dashboard sheet by choosing the
   `<`
   button on the top menu bar.
3. Hover over any data point on your visual to see the sheet tooltip rendered with your custom layout.
4. As you move across different data points, the tooltip dynamically updates all visuals, text boxes, and metrics in real time, providing rich contextual information at a glance.
5. To edit an existing tooltip sheet, select the sheet from the tooltip drop-down list and choose the pencil icon to make any changes.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-4.jpg)

6. Finally, publish the dashboard so that your readers can use the tooltips.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-5.jpg)

### Use case

Let’s take an example to create a sales-focused sheet tooltip with three visuals. You can replace these with any visuals and metrics that suit your use case.

1. From the Visuals section, drag a visual onto the canvas and resize it to fit your layout.
2. Rename the sheet tooltip to
   **Model Sales**
   .
3. Add a gauge chart to measure sales against target and display the comparison percentage.
4. Add a line chart to show monthly trend for sales.
5. Now add a table and select the model image. Edit the field settings and set the field to
   **show URLs as images.**
6. Adjust the size and position of each visual element on the canvas. The free-form layout allows you to drag and rearrange elements freely to create your preferred tooltip composition. Format the visuals to see the results as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-6.jpg)

The following video shows an example of the Automotive Sales Performance dashboard sheet tooltip displaying Sales vs. Target, Monthly Sales trend and image of selected model when hovering over a model data point. Your tooltip content will vary based on the visuals and metrics you choose for your specific use case.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20785/tooltip1.gif)

## **Features supported by sheet tooltips**

You can add a sheet tooltip to most visual types in Quick Sight. The following list shows the supported visual types.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Visual types can have sheet tooltips** | | | | |
| Gauge | Donut chart | Pie chart | Historical pie chart | Vertical bar chart |
| Historical stacked bar chart | Vertical stacked bar chart | Historical stacked 100% bar chart | Vertical stacked 100% bar chart | Line chart |
| Area line chart | Stacked area line chart | Clustered bar combo chart | Stacked bar combo chart | Box plot |
| Pivot table | Table | Heat map | Tree map | Scatter plot |
| Histogram | Funnel chart | Points on map | Filled map | Layered map |

You can also add sheet tooltips to visuals that use
[small multiples](https://docs.aws.amazon.com/quick/latest/userguide/small-multiples.html)
. The small multiples feature allows you to compare data across many values of a specific dimension. The following screenshot shows a sheet tooltip displaying sales by quarter over a pie chart with small multiples. This view helps readers gain deeper insights, such as comparison of vehicle type across regions along with the quarterly sales trends.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-8.jpg)

You can also use
[parameters](https://docs.aws.amazon.com/quick/latest/userguide/parameters-in-quicksight.html)
to let readers dynamically change the visuals shown in a sheet tooltip. In the following example, readers can choose whether they want to view Sales by quarter or Sales by vehicle make in the sheet tooltip.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-9.jpg)

A dashboard author can configure the preceding sheet tooltip option by using a parameter to show or hide a visual in Quick Sight. See
[Using Quick Sight parameters and controls to drive interactivity in your dashboards](https://aws.amazon.com/blogs/big-data/using-quicksight-parameters-and-controls-to-drive-interactivity-in-your-dashboards/)
and
[Hiding a visual by default](https://docs.aws.amazon.com/quick/latest/userguide/hiding-a-visual-by-default.title.html)
to learn more.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/14/ml-20785-image-10.jpg)

The following video demonstrates how to configure Quick Sight to allow dashboard readers to switch visuals in a sheet tooltip.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20785/tooltip2.gif)

## Limitations in sheet tooltips

As you explore the sheet tooltip feature, note the following current limitations:

* Certain visual types cannot have sheet tooltips added to them. See the following list.

|  |  |  |  |
| --- | --- | --- | --- |
| **Visual types cannot have sheet tooltips** | | | |
| KPI | Waterfall chart | Sankey diagram | Radar chart |
| Wordcloud | Custom visual | Highcharts visual | Insight |

* Each tooltip sheet supports up to 5 visuals, 5 images, and 5 text boxes.
* Each analysis supports up to 50 tooltip sheets. This limit is separate from the interactive and pixel-perfect report sheet limits.
* An analysis must contain at least one interactive or paginated report sheet. Tooltip sheets cannot be the only sheet type in an analysis.
* Sheet tooltips are not supported on pixel-perfect report sheets because reports are static PDF output.
* Layer map visuals aren’t supported on tooltip sheets.
* Sheet title and description are not available on tooltip sheets.
* Cross-sheet filtering is not supported on tooltip sheets.
* Sheet tooltips use free-form layout and support up to 640px width and 720px height.
* [Import visual feature](https://docs.aws.amazon.com/quick/latest/userguide/import-visuals.html)
  cannot import sheet tooltip from another analysis.
* You cannot add custom actions on visuals in a tooltip sheet.

## Conclusion

Sheet tooltips in Amazon Quick Sight enhance the dashboard authoring experience, giving authors the creative freedom to design rich, multi-visual tooltip layouts that display detailed data on hover. By combining dynamic charts, real-time metrics, and flexible free-form layouts, sheet tooltips transform hover interactions into interactive data exploration experiences. Whether you’re building executive dashboards, sales reports, or operational monitoring views, sheet tooltips help you deliver deeper insights without requiring readers to navigate away from their current context.

To learn more about sheet tooltips and other new features, visit the
[Amazon Quick community](https://community.amazonquicksight.com/)
What’s New section. We look forward to seeing the creative tooltip experiences you build!

---

## About the authors

### Meshan Khosla

**Meshan Khosla**
is a Software Development Engineer working on Amazon Quick Sight. He enjoys building great software and solving challenging technical problems. Outside of work, he enjoys watching football and working on soon-to-be abandoned side projects.bio

### Neeraj Kumar

**Neeraj Kumar**
is a Senior Worldwide Solutions Architect at AWS, architecting enterprise-scale solutions that transform how organizations use data. With over two decades in data and analytics across automotive, manufacturing, and telecom sectors, he guides global customers to gain deeper insights using Amazon Quick and AI-powered analytics, helping them modernize their Unified AI/BI landscape and accelerate their data-driven initiatives.

### Will Tsao

**Will Tsao**
is a Software Engineer on Amazon’s Quick Sight Visualization team, where he specializes in building intuitive and powerful table and pivot table experiences. He is passionate about solving complex problems and delivering creative, elegant solutions that enhance how users explore and understand data. Outside of work, William dedicates much of his time to kickboxing, continuously challenging himself both physically and mentally.bio.

### Ying Wang

**Ying Wang**
is a Senior Specialist Solutions Architect in the Generative AI organization at AWS, specializing in Amazon Quick Sight and Amazon Q to support large enterprise and ISV customers. She brings 16 years of experience in data analytics and data science, with a strong background as a data architect and software development engineering manager. As a data architect, Ying helped customers design and scale enterprise data architecture solutions in the cloud. In her role as an engineering manager, she enabled customers to make the most of their data through Quick Sight by delivering new features and driving product innovation from both engineering and product perspectives.

### Roy Yung

**Roy Yung**
is a Senior Specialist Solutions Architect for Amazon Quick Sight. Roy has over 10 years of experience implementing enterprise business intelligence (BI) solutions. Prior to AWS, Roy delivered BI and data platform solutions in the insurance, banking, aviation, and retail industries.