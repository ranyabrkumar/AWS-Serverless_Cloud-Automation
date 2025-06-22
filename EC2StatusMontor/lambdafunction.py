import boto3
import os
import logging

sns = boto3.client('sns')
TOPIC_ARN = os.environ['TOPIC_ARN']  # from environment variable


def lambda_handler(event, context):
    detail = event['detail']
    instance_id = detail['instance-id']
    state = detail['state']

    message = f"EC2 Instance {instance_id} changed state to: {state}"
    subject = f"EC2 State Change: {state.upper()}"

    print(f"Sending notification:", {message})
    logging.info(f"Sending notification: {message}")
    

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject=subject,
        Message=message
    )

    return {
        'statusCode': 200,
        'body': 'Notification sent successfully.'
    }
