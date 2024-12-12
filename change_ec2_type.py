import boto3


# Initialize the EC2 client
client = boto3.client('ec2')

def lambda_handler(event, context):
    # print json
    print(event)
    # Extract the instance ID from the event
    instance_id = event['detail']['instance-id']
    # Describe the instance to get current instance type
    response = client.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    current_instance_type = instance['InstanceType']
    
    # Check if instance type is not in the allowed list
    allowed_instance_types = ['t2.medium', 't2.nano', 't2.small', 't2.micro']
    if current_instance_type not in allowed_instance_types:
        # Change instance type to t2.micro
        print(f"Changing instance {instance_id} type from {current_instance_type} to t2.micro")
        
        # Stop the instance
        client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}")
        
        # Wait until the instance is stopped
        waiter = client.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])
        print(f"Instance {instance_id} has stopped")

        # Modify the instance type
        client.modify_instance_attribute(
            InstanceId=instance_id,
            InstanceType={'Value': 't2.micro'}
        )
        print(f"Modified instance {instance_id} to type t2.micro")

        # Start the instance
        client.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}")

        # Wait until the instance is running
        waiter = client.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is running")

    