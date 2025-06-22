import boto3
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# EC2 resource gives a nicer interface than the client
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    try:
        # Find and stop instances tagged with Action=Auto-Stop
        auto_stop_instances = get_instances_by_tag('Auto-Stop')
        instances_to_stop = [i.id for i in auto_stop_instances if i.state['Name'] != 'stopped']

        if instances_to_stop:
            logger.info(f"Stopping instances: {instances_to_stop}")
            print(f"Stopping instances: {instances_to_stop}")
            ec2.instances.filter(InstanceIds=instances_to_stop).stop()
        else:
            logger.info("No instances need stopping.")

        # Find and start instances tagged with Action=Auto-Start
        auto_start_instances = get_instances_by_tag('Auto-Start')
        instances_to_start = [i.id for i in auto_start_instances if i.state['Name'] != 'running']

        if instances_to_start:
            logger.info(f"Starting instances: {instances_to_start}")
            print(f"Starting instances: {instances_to_start}")
            ec2.instances.filter(InstanceIds=instances_to_start).start()
        else:
            logger.info("No instances need starting.")

    except Exception as e:
        logger.error(f"Something went wrong: {str(e)}")
        raise


def get_instances_by_tag(tag_value):
    """
    Returns all EC2 instances with the tag Action=<tag_value>
    across all states (running, stopped, etc).
    """
    return ec2.instances.filter(
        Filters=[
            {'Name': 'tag:Action', 'Values': [tag_value]},
            {'Name': 'instance-state-name', 'Values': ['pending', 'running', 'stopping', 'stopped']}
        ]
    )
