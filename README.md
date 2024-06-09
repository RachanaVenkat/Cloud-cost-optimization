# Cloud cost optimization using Boto3

### Introduction

What are the reasons for companies to migrate from on-premises servers to the Cloud? 
- Maintenance Overhead
- Highly Expensive
- Not very efficient

What if a company migrated to the Cloud and these problems still exist? What if the costs aren't being saved either?
Is it the cloud provider's fault? No. It is a shared responsibilty.
To explain it - cloud providers like AWS, Azure etc, provide you with numerous services for compute, storage, monitoring and many more, with least amount of effort on your end. This doesn't mean you can use the resources irresponsibly, it will incur additional charges and you won't benefit from the migration. So, it is a shared responsibility. Use resources responsibly, reap all the benefits.

As a DecOps Engineer, one of your responsibilities is to maintain all the created resources and ensure the deletion of stale resources

### Problem Explanation

Imagine you created an EC2 instance with an attached root EBS volume, to store the data related to your application hosted on that instance. You decided to take a backup of that EBS volume by taking a snapshot, to restore it as a new volume in a different AZ when a disaster strikes. But, you need the snapshots only as long as the application exists. If you decide to shut down your appliaction on the EC2 instance, there will be no need for the snapshot. In that scenario, the snapshots associated with the instance needs to be deleted to be financially efficient. 

If you just have one or two EC2 intances to manage, this won't be a big deal, and you can easily manage creation and deletion snapshots manually. But, companies usually have a lot of resources and EC2 instances to manage in various AWS regions. So the above task is almost impossible to be done manually.

This is when Lambda functions in AWS emerge.

### Description

A Lambda function is developed utilizing AWS Boto3 services to automate the identification and deletion of stale snapshots, thus optimizing cloud expenses. This function efficiently manages AWS resources by identifying snapshots that are no longer needed and removing them, thereby reducing unnecessary storage costs. Through proactive management of snapshots, the Lambda function contributes to cost optimization strategies within AWS environments.

