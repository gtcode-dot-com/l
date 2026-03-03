---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T00:14:15.441764+00:00'
exported_at: '2026-03-03T00:14:17.744020+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-quick-suite-now-supports-key-pair-authentication-to-snowflake-data-source
structured_data:
  about: []
  author: ''
  description: In this blog post, we will guide you through establishing data source
    connectivity between Amazon Quick Sight and Snowflake through secure key pair
    authentication.
  headline: Amazon Quick now supports key pair authentication to Snowflake data source
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/amazon-quick-suite-now-supports-key-pair-authentication-to-snowflake-data-source
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Amazon Quick now supports key pair authentication to Snowflake data source
updated_at: '2026-03-03T00:14:15.441764+00:00'
url_hash: a7cdf4ae74f3f1c6321e3de9661b2a94dc05650a
---

Modern enterprises face significant challenges connecting business intelligence platforms to cloud data warehouses while maintaining automation. Password-based authentication introduces security vulnerabilities, operational friction, and compliance gaps—especially critical as Snowflake is deprecating username password.

[Amazon Quick Sight](https://aws.amazon.com/quick/quicksight/)
(a capability of Amazon Quick) now supports key pair authentication for Snowflake integrations, using asymmetric cryptography where RSA key pairs replace traditional passwords. This enhancement addresses a critical need as Snowflake moves toward deprecating password-based authentication, which requires more secure authentication methods. With this new capability, Amazon Quick users can establish secure, passwordless connections to Snowflake data sources using RSA key pairs, providing a seamless and secure integration experience that meets enterprise security standards.

In this blog post, we will guide you through establishing data source connectivity between Amazon Quick Sight and Snowflake through secure key pair authentication.

## **Prerequisites**

Before configuring key pair authentication between Amazon Quick and Snowflake, ensure that you have the following:

* An active
  [Amazon Quick account](https://docs.aws.amazon.com/quicksuite/latest/userguide/signing-up.html)
  with appropriate permissions – You need administrative access to create and manage data sources, configure authentication settings, and grant permissions to users. Amazon Quick Enterprise license or Author role in Amazon Quick Enterprise Sight Edition typically provide sufficient access.
* A
  [Snowflake account](https://app.snowflake.com/)
  with ACCOUNTADMIN, SECURITYADMIN, or USERADMIN role – These elevated permissions are essential for modifying user accounts, assigning public keys using ALTER USER commands, and granting warehouse and database permissions. If you don’t have access to these roles, contact your Snowflake administrator for assistance.
* [OpenSSL](https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl5-install.html)
  installed (for key generation) – This cryptographic toolkit generates RSA key pairs in PKCS#8 format. Most Linux and macOS systems include OpenSSL pre-installed. Windows users can use Windows Subsystem Linux (WSL) or download OpenSSL separately.
* **(Optional)**
  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
  access (for API-based setup) – Required for programmatic configurations, you will need
  [IAM](https://aws.amazon.com/iam/identity-center/)
  permissions to create and manage secrets, and Amazon Quick Sight API access for automated deployments and infrastructure as code (IaC) implementations.

## **Solution walkthrough**

We will guide you through the following essential steps to establish secure key pair authentication between Amazon Quick Sight and Snowflake:

1. Generate RSA Key Pair – Create public and private keys using OpenSSL with proper encryption standards
2. Configure Snowflake User – Assign the public key to your Snowflake user account and verify the setup
3. Establish Data Source Connectivity – Create your connection through either the Amazon Quick UI for interactive setup or AWS Command Line Interface (AWS CLI) for programmatic deployment

Let’s explore each step in detail and secure your Amazon Quick Sight-Snowflake connection with key pair authentication!

### **Generate RSA key pair:**

1. Navigate to AWS CloudShell in
   [AWS Management Console](https://aws.amazon.com/console/)
   and execute the following command to generate the RSA private key. You will be prompted to enter an encryption passphrase. Choose a strong passphrase and store it securely—you will need this later when generating the public key.

```
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-1.png)

2. Run the following commands to create a public key pair. You will be prompted to enter the phrase that you used in the previous step.

```
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-2.png)

3. Extract the private key content (including header and footer):

This displays your private key in the format:

`-----BEGIN PRIVATE KEY-----[key content]-----END PRIVATE KEY-----`

**Note**
: Copy the entire output including the
`-----BEGIN PRIVATE KEY-----`
and
`-----END PRIVATE KEY-----`
lines. You will use this complete private key (with headers and footers) when creating your Snowflake data source connection.

4. Snowflake requires the public key in a specific format without headers or line breaks. Run these commands to extract and format the key properly.

```
grep -v KEY rsa_key.pub | tr -d '\n' | awk '{print $1}' > pub.Key
cat pub.Key
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/BI-8236-image-3-new.png)

This will display your formatted public key string. Copy this output—you will use it in the next step to configure your Snowflake user account.

### **Assign public key to Snowflake user:**

1. Log in to Snowflake and execute the following SQL commands to assign the public key to your user:

```
ALTER USER <username> SET RSA_PUBLIC_KEY='<public_key_content>';
```

2. Verify the key assignment: Look for the
   `RSA_PUBLIC_KEY`
   property to confirm if the public key is set.

```
DESCRIBE USER <username>;
```

### **Establish your Snowflake connection in Amazon Quick UI:**

3. Navigate to Amazon Quick in AWS Management Console and select
   **Datasets**
   . Then select the
   **Data sources**
   tab and choose
   **Create data source**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-4.png)

4. In the
   **Create data source**
   pane, enter “snowflake” in
   **Search datasets**
   , select
   **Snowflake,**
   and then choose
   **Next**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-5.png)

5. In the New Snowflake data source pane, enter the data source name, then enter the connection type as Public Network or a Private VPC Connection. If you need a VPC connection, see
   [configure the VPC connection in Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/vpc-creating-a-connection-in-quicksight.html)
   .
6. Then, enter the database server hostname, database name, and warehouse name.
7. Select
   **Authentication Type**
   as
   **KeyPair**
   and then enter the username of the Snowflake user.
8. In the
   **Private Key**
   field, paste the complete output from
   `cat rsa_key.p8`
   (including the BEGIN and END headers). If you have configured a passphrase during key generation, provide it in the optional Passphrase field.
9. After all the fields are entered, select the
   **Validate connection**
   button.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/BI-8236-image-6-1.png)

10. After the connection is validated, select the
    **Create data source**
    button.
11. Then in the Data sources list, find the snowflake data source that you created.
12. From the
    **Action**
    menu, select the
    **Create dataset**
    option.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-7.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-14-1.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-13.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/BI-8236-image-8.png)

### **Establish your Snowflake Connection using the Amazon Quick Sight API:**

Using AWS CLI, create the Amazon Quick data source connection to Snowflake by executing the following command:

```
aws quicksight create-data-source \
  --aws-account-id 123456789 \
  --data-source-id awsclikeypairtest \
  --name "awsclikeypairtest" \
  --type SNOWFLAKE \
  --data-source-parameters '{
    "SnowflakeParameters": {
      "Host": "hostname.snowflakecomputing.com",
      "Database": "DB_NAME",
      "Warehouse": "WH_NAME",
      "AuthenticationType": "KEYPAIR"
    }
  }' \
  --credentials '{
    "KeyPairCredentials": {
      "KeyPairUsername": "SNOWFLAKE_USERNAME",
      "PrivateKey": "-----BEGIN ENCRYPTED PRIVATE KEY-----\nPRIVATE_KEY\n-----END ENCRYPTED PRIVATE KEY-----",
      "PrivateKeyPassphrase": "******"
    }
  }' \
    --permissions '[
    {
      "Principal": "arn:aws:quicksight:us-east-1: 123456789:user/default/Admin/username,
      "Actions": [
        "quicksight:DescribeDataSource",
        "quicksight:DescribeDataSourcePermissions",
        "quicksight:PassDataSource",
        "quicksight:UpdateDataSource",
        "quicksight:DeleteDataSource",
        "quicksight:UpdateDataSourcePermissions"
      ]
    }
  ]' \
  --region us-east-1
```

Use the following command to check the status of creation:

```
aws quicksight describe-data-source --region us-east-1 --aws-account-id 123456789 --data-source-id awsclikeypairtest
```

Initially, the status returned from the describe-data-source command will be
`CREATION_IN_PROGRESS`
. The status will change to
`CREATION_SUCCESSFUL`
if the new data source is ready for use.

Alternatively, when creating the data source programmatically via
`CreateDataSource`
, you can store the username, key and passphrase in AWS Secrets Manager and reference them using the Secret ARN.

After the data source is successfully created, you can navigate to the Quick console. In the
**Create a Dataset**
page, you can view the newly created data source connection
`awsclikeypairtest`
under the data sources list. You can then continue to create the datasets.

## **Cleanup**

To clean up your resources to avoid incurring additional charges, follow these steps:

1. [Delete the secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)
   created in the AWS Secrets Manager Console.
2. [Delete the data source connection](https://docs.aws.amazon.com/quicksuite/latest/userguide/delete-a-data-source.html)
   created in Amazon Quick.

## **Conclusion**

Key pair authentication represents a transformative advancement in securing data connectivity between Amazon Quick and Snowflake. By removing password-based vulnerabilities and embracing cryptographic authentication, organizations can achieve superior security posture while maintaining seamless automated workflows. This implementation addresses critical enterprise requirements, such as enhanced security through asymmetric encryption, streamlined service account management, and compliance with evolving authentication standards as Snowflake transitions away from traditional password methods.

Whether deploying through the intuitive Amazon Quick UI or using AWS CLI for Infrastructure as Code implementations, key pair authentication provides flexibility without compromising security. The integration with AWS Secrets Manager helps protect the private keys, while the straightforward setup process enables rapid deployment across development, staging, and production environments.

As data security continues to evolve, adopting key pair authentication positions your organization at the forefront of best practices. Business intelligence teams can now focus on extracting actionable insights from Snowflake data rather than managing authentication complexities, ultimately accelerating time-to-insight and improving operational efficiency.

For further reading, see
[Snowflake Key-Pair Authentication.](https://docs.snowflake.com/en/user-guide/key-pair-auth)

---

## **About the authors**

### Vignessh Baskaran

Vignessh Baskaran is a Sr. Technical Product Manager in the structured DATA domain in Amazon Quick powering BI and GenAI initiatives. He has 9+ years of experience in developing large-scale data and analytics solutions. Prior to this role, he worked as a Sr. Analytics Lead in AWS building comprehensive BI solutions using Quick which were globally adopted across AWS Worldwide Specialist Sales teams. Outside of work, he enjoys watching Cricket, playing Racquetball and exploring different cuisines in Seattle.

### Chinnakanu Sai Janakiram

Chinnakanu Sai Janakiram is a Software Development Engineer in Amazon Quick, working on cloud infrastructure automation and feature development using AWS technologies. He has 2+ years of experience building scalable systems across AWS, CI/CD pipelines, CloudFormation, React, and Spring Boot. Prior to this role, he contributed to data and analytics solutions on AWS, improving deployment reliability and scalability across regions. Outside of work, he enjoys following Formula 1 and staying up to date with emerging technologies.

### Nithyashree Alwarsamy

Nithyashree Alwarsamy is a Partner Solutions Architect at Amazon Web Services, specializing in data and analytics solutions with a focus on streaming and event-driven architecture. Leveraging deep expertise in modern data architectures, Nithyashree helps organizations unlock the full potential of their data by integrating Snowflake’s cloud-native data platform with the breadth of AWS services.

### Andries Engelbrecht

[Andries Engelbrecht](https://www.linkedin.com/in/andries-engelbrecht-427b8b1/)
is a Principal Partner Solutions Engineer at Snowflake working with AWS. He supports product and service integrations, as well as the development of joint solutions with AWS. Andries has over 25 years of experience in the field of data and analytics.