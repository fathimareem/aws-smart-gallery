# AWS AI-Powered Image Recognition Pipeline

A cloud-native, serverless application that automates image analysis and real-time alerting using AWS AI services.

## 🌟 Project Impact
As a fresher, I built this to demonstrate a deep understanding of **Event-Driven Architecture (EDA)**. Instead of a server running 24/7, this system only runs when an image is uploaded, making it highly cost-effective and scalable.

## 🛠️ Tech Stack
- **Compute:** AWS Lambda (Python 3.12)
- **Storage:** Amazon S3
- **AI/ML:** Amazon Rekognition
- **Database:** Amazon DynamoDB (NoSQL)
- **Messaging:** Amazon SNS (Simple Notification Service)
- **Monitoring:** AWS CloudWatch

## 📋 Architecture
The system follows a 5-step automated workflow:
1. **Trigger:** Image is uploaded to an S3 bucket.
2. **Process:** S3 triggers a Lambda function via an Event Notification.
3. **Analyze:** Lambda sends the image bytes to Rekognition for object detection.
4. **Persist:** Detected labels (tags) and confidence scores are saved to DynamoDB.
5. **Alert:** If a specific object (e.g., "Person") is detected, an email alert is sent via SNS.

## 🚀 Key Learning Milestones
- **IAM Best Practices:** Implemented "Least Privilege" by attaching specific policies to Lambda execution roles.
- **Boto3 Mastery:** Used the AWS SDK for Python to orchestrate multiple services.
- **NoSQL Schema:** Designed a simple DynamoDB table for fast metadata retrieval.
- **Cloud Monitoring:** Utilized CloudWatch Logs to debug and verify event triggers.

## 🔧 Setup
1. Clone this repository.
2. Deploy the Lambda function using the code provided in `lambda_function.py`.
3. Create an S3 bucket and set up a trigger for the Lambda.
4. Configure an SNS topic with your email for notifications.
