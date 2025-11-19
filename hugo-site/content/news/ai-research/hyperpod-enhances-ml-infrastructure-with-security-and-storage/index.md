---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-19T01:01:35.906918+00:00'
exported_at: '2025-11-19T01:01:39.217877+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/hyperpod-enhances-ml-infrastructure-with-security-and-storage
structured_data:
  about: []
  author: ''
  description: This blog post introduces two major enhancements to Amazon SageMaker
    HyperPod that strengthen security and storage capabilities for large-scale machine
    learning infrastructure. The new features include customer managed key (CMK) support
    for encrypting EBS volumes with organization-controlled encryption keys, and Amazon
    EBS CSI driver integration that enables dynamic storage management for Kubernetes
    volumes in AI workloads.
  headline: HyperPod enhances ML infrastructure with security and storage
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/hyperpod-enhances-ml-infrastructure-with-security-and-storage
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: HyperPod enhances ML infrastructure with security and storage
updated_at: '2025-11-19T01:01:35.906918+00:00'
url_hash: 8dd0957365b0f70c32cca6a4e733c2261c942676
---

[Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/)
is a purpose-built infrastructure for optimizing foundation model training and inference at scale. SageMaker HyperPod removes the undifferentiated heavy lifting involved in building and optimizing machine learning (ML) infrastructure for training foundation models (FMs).

As AI moves towards deployment adopting to a multitude of domains and use cases, the need for security and multiple storage options is becoming more pertinent. Large enterprises want to make sure that the GPU clusters follow the organization wide policies and security rules. Two new features in SageMaker HyperPod EKS enhance this control and flexibility for production deployment of large-scale machine learning workloads. These features include support for continuous scaling, custom Amazon Machine Images, and customer managed key (CMK) integration.

* [Customer managed keys (CMK) support](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-cmk.html)
  : HyperPod EKS now allows customers to encrypt primary and secondary
  [EBS](https://aws.amazon.com/ebs/)
  volumes attached to HyperPod instances or their custom AMI with their own encryption keys. To learn more about creating a custom AMI for your HyperPod cluster, please see our
  [blog post](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-enhances-ml-infrastructure-with-scalability-and-customizability/)
  and
  [documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-custom-ami-support.html)
  .
* [Amazon EBS CSI support](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-ebs.html)
  : HyperPod EKS now supports the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver, which manages the lifecycle of Amazon EBS volumes as storage for the Kubernetes volumes that you create.

## Prerequisites

In order to use these features verify you have the following prerequisites:

## Customer managed key support

With CMK support you control the encryption capabilities required for compliance and security governance, ultimately helping to resolve the critical business risk of unmet regulatory and organizational security requirements, such as HIPAA and FIPS compliance. CMK support allows customers to encrypt EBS volumes attached to their HyperPod instances using their own encryption keys. When creating a cluster, updating a cluster, or adding new instance groups, customers can specify a CMK for both root and secondary EBS volumes. Additionally, customers can encrypt their custom AMIs with CMK, providing comprehensive data-at-rest protection with customer-controlled keys throughout the instance lifecycle.

Here are the key points about CMK configuration:

**For EBS volumes:**

* CMK is optional – if not specified, volumes will be encrypted with AWS managed keys
* You cannot update/change the CMK for existing volumes (CMK is immutable)
* Each instance group can have:
  + One root volume configuration with CMK
  + One secondary volume configuration with CMK
* Root volume configurations cannot specify volume size
* Secondary volume configurations must specify volume size
* You can specify different CMKs for root and secondary volumes

**For custom AMIs:**

* You can encrypt custom AMIs with CMK independently of volume encryption
* Unlike volume CMK, custom AMI CMK is mutable – customers can patch clusters using AMIs encrypted with different CMKs

**Important**
: When using customer managed keys, we strongly recommend that you use different KMS keys for each instance group in your cluster. Using the same customer managed key across multiple instance groups might lead to unintentional continued permissions even if you try to revoke a grant. For example:

* If you revoke an AWS KMS grant for one instance group’s volumes, that instance group might still allow scaling and patching operations due to grants existing on other instance groups using the same key
* To help prevent this issue, make sure that you assign unique KMS keys to each instance group in your cluster

### Configuring CMK on HyperPod

In this section, we will demonstrate how to set up CMK for your HyperPod cluster. As a prerequisite, make sure you have the following:

1. Verify that the AWS IAM execution role that you’re using for your CMK-enabled instance group has the following permissions for AWS KMS added. The
   [`kms:CreateGrant`](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)
   permission allows HyperPod to take the following actions using permissions to your KMS key:
   1. Scaling out your instance count (
      `UpdateCluster`
      operations)
   2. Adding cluster nodes (
      `BatchAddClusterNodes`
      operations)
   3. Patching software (
      `UpdateClusterSoftware`
      operations)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        }
    ]
}
```

2. Include this in your KMS key policy:

You can modify your key policy following the
[Change a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html)
documentation. Replace variables
`<iam-hp-execution-role>`
,
`<region>`
,
`<account-id>`
, and
`<key-id>`
with your HyperPod execution role (the role that is linked to your instance group using CMKs), AWS Region your HyperPod cluster is deployed in, your account ID, and your KMS key ID, respectively.

```
{
    "Version": "2012-10-17",
    "Id": "hyperpod-key-policy",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account-id>:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account-id>:role/<iam-hp-execution-role>"
            },
            "Action": "kms:CreateGrant",
            "Resource": "arn:aws:kms:<region>:<account-id>:key/<key-id>",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "sagemaker.<region>.amazonaws.com"
                },
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account-id>:role/<iam-hp-execution-role>"
            },
            "Action": "kms:DescribeKey",
            "Resource": "arn:aws:kms:<region>:<account-id>:key/<key-id>",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "sagemaker.<region>.amazonaws.com"
                }
            }
        }
    ]
}
```

Now, let’s use the CMK.

You can specify your customer managed keys when creating or updating a cluster using the
[CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html)
and
[UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html)
API operations. The
`InstanceStorageConfigs`
structure allows up to two
`EbsVolumeConfig`
configurations, in which you can configure the root Amazon EBS volume and, optionally, a secondary volume. You can use the same KMS key or a different KMS key for each volume, depending on your needs.

When you are configuring the root volume, the following requirements apply:

* `RootVolume`
  must be set to
  `True`
  . The default value is
  `False`
  , which configures the secondary volume instead.
* The
  `VolumeKmsKeyId`
  field is required and you must specify your customer managed key. This is because the root volume must be encrypted with either an AWS owned key or a customer managed key (if you don’t specify your own, then an AWS owned key is used).
* You can’t specify the
  `VolumeSizeInGB`
  field for root volumes since HyperPod determines the size of the root volume for you.

When configuring the secondary volume, the following requirements apply:

* `RootVolume`
  must be
  `False`
  (the default value of this field is
  `False`
  ).
* The
  `VolumeKmsKeyId`
  field is optional. You can use the same customer managed key you specified for the root volume, or you can use a different key.
* The
  `VolumeSizeInGB`
  field is required, since you must specify your desired size for the secondary volume.

Example of creating cluster with CMK support:

```
aws sagemaker create-cluster \
  --cluster-name <your-hyperpod-cluster> \
  --instance-groups '[{
    "ExecutionRole": "arn:aws:iam::<account-id>:role/<your-SageMaker-Execution-Role>",
    "InstanceCount": 2,
    "InstanceGroupName": "<your-ig-name>",
    "InstanceStorageConfigs": [
            {
                "EbsVolumeConfig": {
                    "RootVolume": True,
                    "VolumeKmsKeyId": "arn:aws:kms:<region>:<account-id>:key/<root-volume-key-id>"
                }
            },
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:<region>:<account-id>:key/<secondary-volume-key-id>"
                }
            }
    ],
    "InstanceType": "<desired-instance-type>"
  }]' \
  --vpc-config '{
    "SecurityGroupIds": ["<sg-id>"],
    "Subnets": ["<subnet-id>"]
  }'
```

Example of updating a cluster with CMK support:

```
aws sagemaker update-cluster \
  --cluster-name <your-hyperpod-cluster> \
  --instance-groups '[{
    "InstanceGroupName": "<your-ig-name>",
    "InstanceStorageConfigs": [
            {
                "EbsVolumeConfig": {
                    "RootVolume": true,
                    "VolumeKmsKeyId": "arn:aws:kms:<region>:<account-id>:key/<root-volume-key-id>"
                }
            },
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:<region>:<account-id>:key/<secondary-volume-key-id>"
                }
            }
    ]
  }]'
```

To use a custom AMI with CMK encryption, you would first have to build your custom AMI with your CMK. You can do this with the following tools, but note that these commands are sample snippets. Follow the linked documentation to generate the AMI.

```
aws imagebuilder create-image-recipe \
    --name "hyperpod-custom-recipe" \
    --version "1.0.0" \
    --parent-image "<hyperpod-base-image-id>" \
    --components "componentArn=<component-arn>" \
    --block-device-mappings DeviceName="/dev/xvda",Ebs={VolumeSize=100,VolumeType=gp3,Encrypted=true,KmsKeyId=arn:aws:kms:us-east-1:111122223333:key/key-id,DeleteOnTermination=true}
```

* [Amazon EC2 Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
  :
  1. Right-click on your customized Amazon EC2 instance and choose
     **Create Image**
     .
  2. In the
     **Encryption**
     section, select
     **Encrypt snapshots**
     .
  3. Select your KMS key from the dropdown. For example:
     `arn:aws:kms:us-east-2:111122223333:key/<your-kms-key-id>`
     or use the key alias:
     `alias/<your-hyperpod-key>`
     .

```
aws ec2 create-image \
    --instance-id "<instance-id>" \
    --name "MyCustomHyperPodAMI" \
    --description "Custom HyperPod AMI" \
    --block-device-mappings '[
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "Encrypted": true,
                "KmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/<key-id>",
                "VolumeType": "gp2"
            }
        }
    ]'
```

To use this encrypted custom AMI, please follow our
[blog](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-enhances-ml-infrastructure-with-scalability-and-customizability/)
or
[documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-custom-ami-support.html)
on using your custom AMI on HyperPod.

## Amazon EBS CSI driver support

With Amazon Elastic Block Storage (EBS) Container Storage Interface (CSI) support in HyperPod you can manage the lifecycle of Amazon EBS volumes as storage for the Kubernetes Volumes created for your EKS clusters. Supporting both
[ephemeral](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/)
and
[persistent](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
volumes, this enhancement addresses the need for dynamic storage management in large-scale AI workloads, efficiently handling the massive datasets and model artifacts for foundation model training and inference.

HyperPod now offers two flexible approaches for provisioning and mounting additional Amazon EBS volumes on nodes. The first method, which isn’t new, uses
`InstanceStorageConfigs`
for cluster-level volume provisioning when creating or updating instance groups, requiring users to set the local path to
`/opt/sagemaker`
in their Pod configuration file. Alternatively, users can implement the Amazon EBS CSI driver for dynamic Pod-level volume management, providing greater control over storage allocation.

This feature was previously supported exclusively only on Amazon EKS clusters, now it unlocks new storage capabilities for the SageMaker HyperPod too. To read more about the capabilities yourself, follow the official
[documentation page](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-ebs.html)
.

### Demo of the Amazon EBS CSI driver on SageMaker HyperPod

In this section, we will demo one of the capabilities of Amazon EBS CSI, such as
**volume resizing**
.

#### Setup EBS CSI Driver

In the following sections we will ask you to substitute some parameters with the values unique to your demo. When we refer to
`<eks-cluster-name>`
, that’s the name of the underlying Amazon EKS cluster, not the SageMaker HyperPod cluster. Configure your kubernetes config to add a new context, so the utils will interact with your new EKS cluster. Run the following:

```
aws eks update-kubeconfig \
        --region <region> \
        --name <eks-cluster-name>
```

Secondly, we need to create a IAM Service Account with an appropriate policy to work with Amazon EBS CSI. The IAM Service Account is the IAM entity for Amazon EKS to interact with other AWS services. We chose
[eksctl](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html"%20\l%20"csi-iam-role)
to create the policy and attach the required policy in a single command, however there are other ways to do the same.

```
eksctl create iamserviceaccount \
        --name ebs-csi-controller-sa \
        --namespace kube-system \
        --cluster <eks-cluster-name> \
        --role-name DemoRole \
        --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
        --approve
```

After the successful execution of the command, we should expect three outcomes:

* IAM Service account with the name
  **ebs-csi-controller-sa**
  is created
* IAM role named
  **DemoRole**
  is created with policy
  **arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy**
  attached
* The
  **ebs-csi-controller-sa**
  service account consumes the
  **DemoRole**

During this demo you should see an output to the previous command, for example:

```
2025-08-19 12:44:17 [ℹ]  3 existing iamserviceaccount(s) (kube-system/aws-load-balancer-controller,kube-system/fsx-csi-controller-sa,kube-system/s3-csi-driver-sa) will be excluded
2025-08-19 12:44:17 [ℹ]  1 iamserviceaccount (kube-system/ebs-csi-controller-sa) was included (based on the include/exclude rules)
2025-08-19 12:44:17 [!]  serviceaccounts that exist in Kubernetes will be excluded, use --override-existing-serviceaccounts to override
2025-08-19 12:44:17 [ℹ]  1 task: {
    2 sequential sub-tasks: {
        create IAM role for serviceaccount "kube-system/ebs-csi-controller-sa",
        create serviceaccount "kube-system/ebs-csi-controller-sa",
    } }2025-08-19 12:44:17 [ℹ]  building iamserviceaccount stack "eksctl-sagemaker-hyperpod-eks-cluster-b94d57bb-eks-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2025-08-19 12:44:17 [ℹ]  deploying stack "eksctl-sagemaker-hyperpod-eks-cluster-b94d57bb-eks-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2025-08-19 12:44:17 [ℹ]  waiting for CloudFormation stack "eksctl-sagemaker-hyperpod-eks-cluster-b94d57bb-eks-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2025-08-19 12:44:48 [ℹ]  waiting for CloudFormation stack "eksctl-sagemaker-hyperpod-eks-cluster-b94d57bb-eks-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2025-08-19 12:44:49 [ℹ]  created serviceaccount "kube-system/ebs-csi-controller-sa"
```

The final step of the IAM Service Account configuration is to attach extra policies required for the interaction between Amazon EKS and SageMaker HyperPod, mentioned in the feature’s
[documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-ebs.html#sagemaker-hyperpod-eks-ebs-setup)
. We will do this with an inline policy, created from the terminal.

The following code snippet creates a temporary file and attaches it to the newly created policy, where you need to put in three values, related to your demo process:

* <region>
* <account-id>
* <eks-cluster-name>

```
cat > inline_policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "sagemaker:AttachClusterNodeVolume",
                "sagemaker:DetachClusterNodeVolume"
            ],
            "Resource": "arn:aws:sagemaker:*:*:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "eks:DescribeCluster"
            ],
            "Resource": "arn:aws:eks:<region>:<account-id>:cluster/<eks-cluster-name>"
        }
    ]
}
EOF
```

Once the file is configured with your parameters, apply the policy to the DemoRole created before using eksctl:

```
aws iam put-role-policy \
        --role-name DemoRole \
        --policy-name HyperPodEBS \
        --policy-document file://inline_policy.json
```

To observe the results of the creation, we can use kubectl to inspect the service account’s state and an IAM role consumed by it:

```
kubectl get sa ebs-csi-controller-sa -n kube-system -o json
{
    "apiVersion": "v1",
    "kind": "ServiceAccount",
    "metadata": {
        "annotations": {
            "eks.amazonaws.com/role-arn": "arn:aws:iam::<account-id>:role/DemoRole"
        },
        "creationTimestamp": "2025-08-19T12:10:05Z",
        "labels": {
            "app.kubernetes.io/managed-by": "eksctl"
        },
        "name": "ebs-csi-controller-sa",
        "namespace": "kube-system",
        "resourceVersion": "17982",
        "uid": "679cc698-88dd-4934-a11f-0b8edee5277c"
    }
}
```

To observe the role, we can check both attached managed policies and inline policies.For the attached managed:

```
$ aws iam list-attached-role-policies --role-name DemoRole
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonEBSCSIDriverPolicy",
            "PolicyArn": "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
        }
    ]
}
```

For the inline policies:

```
aws iam list-role-policies —role-name DemoRole
{
    "PolicyNames": [
        "HyperPodEBS"
    ]
}
```

Now, we are ready to
[create and install the Amazon EBS CSI add-on](https://docs.aws.amazon.com/eks/latest/userguide/creating-an-add-on.html)
on the EKS cluster. For this example, use the following command:

```
eksctl create addon \
        --cluster <eks-cluster-name>
        --name aws-ebs-csi-driver \
        --version latest \
        --service-account-role-arn arn:aws:iam::<account-id>:role/DemoRole \
        --force
```

You will see an output indicating that the creation has started, for example:

```
:27:47 [ℹ] Kubernetes version "1.31" in use by cluster "sagemaker-hyperpod-eks-cluster-b94d57bb-eks"
:27:48 [ℹ] IRSA is set for "aws-ebs-csi-driver" addon; will use this to configure IAM permissions
2025-08-19 13:27:48 [!] the recommended way to provide IAM permissions for "aws-ebs-csi-driver" addon is via pod identity associations; after addon creation is completed, run
:27:48 [ℹ] using provided ServiceAccountRoleARN "arn:aws:iam::000182341198:role/DemoRole"
:27:48 [ℹ] creating addon: aws-ebs-csi-driver
```

To track the status of add-on creation, you can use the
**watch**
utility from the terminal.

**Note**
: If the status is stuck on
`CREATING`
for more than 5 minutes, you should debug the state of your cluster to see whether the pods are running. If the status isn’t changing, you might not have a sufficient number of instances or the instance type is too small. If you observe that many pods of the cluster are in the
`PENDING`
state that might be an indicator of one of these issues.

```
watch -n 5 aws eks describe-addon \
        --cluster-name <eks-cluster-name> \
        --addon-name aws-ebs-csi-driver \
        --query 'addon.status'

# wait until you see this:
"ACTIVE"
```

#### Running the volume resize demo

Now we’re ready for the demo, all the components are installed and ready to interact with each other. On your local machine, download the
[repository of AWS EBS CSI driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
, then navigate to the folder of the resizing example.

```
$ git clone git@github.com:kubernetes-sigs/aws-ebs-csi-driver.git
Cloning into 'aws-ebs-csi-driver'...
remote: Enumerating objects: 35200, done.
remote: Counting objects: 100% (146/146), done.
remote: Compressing objects: 100% (81/81), done.
remote: Total 35200 (delta 99), reused 67 (delta 61), pack-reused 35054 (from 2)
Receiving objects: 100% (35200/35200), 29.61 MiB | 14.56 MiB/s, done.
Resolving deltas: 100% (20351/20351), done.

$ cd aws-ebs-csi-driver/examples/kubernetes/resizing
```

Within this folder, we will utilize the provided example, which you can study yourself a bit more by reading the
[readme file](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/tree/master/examples/kubernetes/resizing)
.

Quoting the readme file, we are going to:

1. Deploy the provided pod on your cluster along with the
   `StorageClass`
   and
   `PersistentVolumeClaim`
   :

```
kubectl apply -f manifests
persistentvolumeclaim/ebs-claim created
pod/app created
storageclass.storage.k8s.io/resize-sc created
```

2. Wait for the
   `PersistentVolumeClaim`
   to bind and the pod to reach the
   `Running`
   state.

```
kubectl get pvc/ebs-claim pod/app
NAME                              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/ebs-claim       pvc-404555ec-d4a8-4fb0-bfbb-782619b1f815   4Gi        RWO            resize-sc      <unset>                 55s

NAME      READY   STATUS    RESTARTS   AGE
pod/app   1/1        0          55s
```

3. Expand the volume size by increasing the capacity specification in the
   **PersistentVolumeClaim**
   using the editor, we use vim but you can use other editors. The following example is the content of the file with extra comments pointing to the places where you should change the capacity. Be attentive, as there are two places with storage volume – one is the specification, while the other is only a status. Changing the status will result in no changes.

```
$ KUBE_EDITOR="vim" && kubectl edit pvc ebs-claim

  1 # Please edit the object below. Lines beginning with a '#' will be ignored,
  2 # and an empty file will abort the edit. If an error occurs while saving this file will be
  3 # reopened with the relevant failures.
  4 #
  5 apiVersion: v1
  6 kind: PersistentVolumeClaim
  7 metadata:
  8   annotations:
  9     kubectl.kubernetes.io/last-applied-configuration: |
 10       {"apiVersion":"v1","kind":"PersistentVolumeClaim","metadata":{"annotations":{},"name":"ebs-claim","namespace":"default"},"spec":{"accessMod>
 11     pv.kubernetes.io/bind-completed: "yes"
 12     pv.kubernetes.io/bound-by-controller: "yes"
 13     volume.beta.kubernetes.io/storage-provisioner: ebs.csi.aws.com
 14     volume.kubernetes.io/storage-provisioner: ebs.csi.aws.com
 15   creationTimestamp: "2025-08-19T13:14:42Z"
 16   finalizers:
 17   - kubernetes.io/pvc-protection
 18   name: ebs-claim
 19   namespace: default
 20   resourceVersion: "45457"
 21   uid: 404555ec-d4a8-4fb0-bfbb-782619b1f815
 22 spec:
 23   accessModes:
 24   - ReadWriteOnce
 25   resources:
 26     requests:
 27       storage: 4Gi # <----------- CHANGE THE VALUE HERE
 28   storageClassName: resize-sc
 29   volumeMode: Filesystem
 30   volumeName: pvc-404555ec-d4a8-4fb0-bfbb-782619b1f815
 31 status:
 32   accessModes:
 33   - ReadWriteOnce
 34   capacity:
 35     storage: 4Gi # <------------- NOT HERE. THIS IS ONLY STATUS
 36   phase: Bound
```

4. Wait a few minutes and verify that both the persistence volume and persistence volume claim have been appropriately resized. To do so, first, check the claim
   **ebs-claim**
   and use the
   **VOLUME**
   from the output to check the volume itself. In both outputs we now see the
   **Capacity**
   changed to 8Gi form initial 4Gi

```
kubectl get pvc/ebs-claim
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
ebs-claim   Bound               RWO            resize-sc      <unset>                 10m

kubectl get pv/
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-404555ec-d4a8-4fb0-bfbb-782619b1f815           RWO            Delete           Bound    default/ebs-claim   resize-sc      <unset>                          11m
```

Clean up the example:

```
kubectl delete -f manifests
persistentvolumeclaim "ebs-claim" deleted
pod "app" deleted
storageclass.storage.k8s.io "resize-sc" deleted
```

We are done with the demo of the feature on the resize example, congratulations! Explore other examples in the same repository, like dynamic provisioning or block volume.

## Clean up

To clean up your resources to avoid incurring more charges, complete the following steps:

1. [Delete your SageMaker HyperPod cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-delete-cluster.html)
   .
2. If you created the networking stack from the
   [SageMaker HyperPod workshop](https://catalog.workshops.aws/sagemaker-hyperpod-eks/en-US)
   , delete the stack as well to clean up the virtual private cloud (VPC) resources and the FSx for Lustre volume.

## Conclusion

The new features in Amazon SageMaker HyperPod Customer Managed Key (CMK) support and Amazon EBS CSI driver support enhance system security and storage capabilities.The Amazon EBS CSI driver support within SageMaker HyperPod EKS clusters supports the use of Amazon EBS volumes for flexible and dynamic storage management options for large-scale AI workloads. In addition to other storage services already available with SageMaker HyperPod clusters, such as Amazon FSx or Amazon S3, you can build efficient and high performing AI solutions. By combining Amazon EBS volumes with Customer Managed Keys support, you can maintain compliance and security governance by controlling their own encryption keys.Together, these features make SageMaker HyperPod a more robust and enterprise-ready environment for training and deploying foundation models at scale, allowing organizations to meet both their security requirements and storage needs efficiently.

For more information, please see,
[Customer managed AWS KMS key encryption for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-cmk.html)
and
[Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-ebs.html)
.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/15/mvincig-100x133.jpg)
**Mark Vinciguerra**
is an Associate Specialist Solutions Architect at Amazon Web Services (AWS) based in New York. He focuses on Generative AI training and inference, with the goal of helping customers architect, optimize, and scale their workloads across various AWS services. Prior to AWS, he went to Boston University and graduated with a degree in Computer Engineering. You can connect with him on
[LinkedIn](https://www.linkedin.com/in/mark-vinciguerra/)
.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/13/rpovelik-100x133.jpg)
Rostislav (Ross) Povelikin**
is a Senior Specialist Solutions Architect at AWS focusing on systems performance for distributed training and inference. Prior to this, he focused on datacenter network and software performance optimisations at NVIDIA.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/15/jhakunal-100x133.jpg)
Kunal Jha**
is a Principal Product Manager at AWS, where he focuses on building Amazon SageMaker HyperPod to enable scalable distributed training and fine-tuning of foundation models. In his spare time, Kunal enjoys skiing and exploring the Pacific Northwest. You can connect with him on
[LinkedIn](https://www.linkedin.com/in/kunal-j/)
.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/11/Takuma-Yoshitani.jpeg)
Takuma Yoshitani**
is a Senior Software Development Engineer at AWS, where he focuses on improving the experience of the SageMaker HyperPod service. Prior to SageMaker, he has contributed to Amazon Go / Just Walk-Out tech.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/11/koppv.jpeg)
**Vivek Koppuru**
is an engineering leader on the Amazon SageMaker HyperPod team helping provide infrastructure solutions for ML training and inference. He has years of experience in AWS and compute as an engineer, working on core services like EC2 and EKS. He is passionate about building customer-focused solutions and navigating through complex technical challenges in distributed systems with the team.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/13/mahajay-100x133.jpg)
Ajay Mahendru**
is an engineering leader at AWS, working in the SageMaker HyperPod team. Bringing in nearly 15+ years of software development experience, Ajay has contributed to multiple AWS SageMaker Services inlcuding SageMaker Inference, Training, Processing and HyperPod. With an expertise in building distributed systems, he focuses on building reliable, customer-focused and scalable solutions across teams.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/13/sengers-100x133.jpg)
Siddharth Senger**
currently serves as a Senior Software Development Engineer at Amazon Web Services (AWS), specifically within the SageMaker HyperPod team. Bringing nearly a decade of software development experience, Siddharth has contributed to several across Amazon, including Retail, Amazon Rekognition, Amazon Textract and AWS SageMaker. He is passionate about building reliable, scalable, and efficient distributed systems that empower customers to accelerate large-scale machine learning and AI innovation.