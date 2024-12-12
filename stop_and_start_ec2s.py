import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    client = boto3.client('ec2')

    # Define the instance IDs you want to start or stop
    instance_ids = [
        'i-0123456789abcdef0',  # Replace with your instance IDs
        'i-0abcdef1234567890'
    ]
    
    # Example action to start instances
    action = event.get('action', 'start')  # Default to 'start' if no action is specified
    
    if action == 'start':
        response = client.start_instances(InstanceIds=instance_ids)
        status_message = 'Starting instances'
    elif action == 'stop':
        response = client.stop_instances(InstanceIds=instance_ids)
        status_message = 'Stopping instances'
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid action. Use "start" or "stop".'
        }
    
    # Log the response from AWS EC2
    print(f"{status_message}: {response}")
    
    return {
        'statusCode': 200,
        'body': f'{status_message.capitalize()} request sent successfully!'
    }


# 2. Create a CloudWatch Event Rule
# CloudWatch Event to Trigger Lambda

# Go to the Amazon CloudWatch Console.
# Click on “Rules” in the left-hand menu.
# Click on “Create rule.”
# For the event source, choose “Event Source” and then “Schedule.”
# Define your schedule expression. For example, cron(0 8 ? * MON-FRI *) will trigger the rule at 8 AM (UTC) Monday through Friday.
# In the “Targets” section, click “Add target.”
# Choose “Lambda function” from the target type dropdown.
# Select your Lambda function (e.g., ManageEC2Instances).
# Click “Create a new role for this specific resource” or choose an existing role with the appropriate permissions.
# Optionally, click “Configure details” and enter a name and description for your rule.
# Click “Create rule.”
# 3. Test the Setup
# To test your setup:

# Manually Invoke Lambda Function:

# Go to the AWS Lambda Console.
# Select your function and click on “Test.”
# Configure a test event with an action parameter, for example:
# json
# Copy code
# {
#   "action": "start"
# }
# Click “Test” to manually invoke the function and verify it works.
# Check CloudWatch Events:

# Verify the CloudWatch Events rule is active and correctly configured by checking the rule details in the CloudWatch console.
# This setup allows you to manage EC2 instances automatically based on a schedule defined in CloudWatch Events, making your operations more efficient and automated.




