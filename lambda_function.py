import boto3
import json

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# PASTE YOUR TOPIC ARN HERE
SNS_TOPIC_ARN = "arn:aws:sns:REGION:ACCOUNT_ID:ImageDetectionAlert"
table = dynamodb.Table('ImageLabels')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    
    # 1. AI Analysis
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
        MaxLabels=10,
        MinConfidence=90
    )

    labels = [label['Name'] for label in response['Labels']]
    
    # 2. Save to DynamoDB
    table.put_item(Item={'ImageID': image_name, 'Labels': labels})
    
    # 3. Logic: If a "Person" is detected, send an email
    if "Person" in labels:
        message = f"Security Alert! A person was detected in the uploaded image: {image_name}"
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Object Detection Alert"
        )
        print("Alert sent via SNS!")

    return {'statusCode': 200}