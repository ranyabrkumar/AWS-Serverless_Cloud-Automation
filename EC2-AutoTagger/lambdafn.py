import boto3
from datetime import datetime
import logging

ec2 = boto3.client('ec2')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Extract instance ID from the event
        instance_id = event['detail']['instance-id']
        logger.info(f"New instance launched: {instance_id}")
        
        # Create tags
        launch_date = datetime.utcnow().strftime('%Y-%m-%d')
        tags = [
            {'Key': 'LaunchDate', 'Value': launch_date},
            {'Key': 'CreatedBy', 'Value': 'AutoTagger'}
        ]
        
        # Apply tags to instance
        ec2.create_tags(Resources=[instance_id], Tags=tags)
        logger.info(f"Successfully tagged instance {instance_id} with tag : {tags}")
        
    except Exception as e:
        logger.error(f"Error tagging instance: {str(e)}")
        raise
