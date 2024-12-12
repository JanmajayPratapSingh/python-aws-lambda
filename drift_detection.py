import json
import boto3

def lambda_handler(event, context):
    # Initialize clients
    cloudtrail_client = boto3.client('cloudtrail')
    sns_client = boto3.client('sns')
    drift_client = boto3.client('resourcegroupstaggingapi')
    
    # Define SNS topic ARN for alerts
    sns_topic_arn = 'arn:aws:sns:us-west-2:123456789012:TerraformDriftAlerts'
    
    # Get the latest drift detection result
    response = drift_client.get_resources(ResourceTypeFilters=['aws:cloudformation:stack'])
    
    # Check for drift in the response
    drift_detected = False
    changes = []
    
    for resource in response['ResourceTagMappingList']:
        drift_status = resource['Tags']['DriftStatus']
        if drift_status != 'IN_SYNC':
            drift_detected = True
            changes.append(resource)
    
    if drift_detected:
        # Find the user who made the change via CloudTrail
        event_response = cloudtrail_client.lookup_events(
            LookupAttributes=[
                {'AttributeKey': 'ResourceName', 'AttributeValue': 'YourResourceName'}
            ],
            MaxResults=1
        )
        user_id = event_response['Events'][0]['Username']
        
        # Create alert message
        message = {
            'Drift Detected': True,
            'UserId': user_id,
            'Changes': changes
        }
        
        # Send alert via SNS
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps({'default': json.dumps(message)}),
            Subject='Terraform Drift Detected',
            MessageStructure='json'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Drift detected and alert sent')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No drift detected')
        }
# create a python program that execcreate a lambda function that 
# detects drift detection for manual changes made via AWS console for 
# the infrastructure managed by terraform. Sends out an alert with the user
# id of the user who has made the manual changes and also the change that was made.