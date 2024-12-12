# create a lambda function that gets triggered whenever an ebs volume is created and Cloudwatch Events helps to monitor 
# and respond to ebs volumes of type gp2  and converts them to gp3. Thereby maintaining organizational policies.

import boto3
client= boto3.client('ec2')

def get_volume_id_from_arn(volume_arn):
    volume_split = volume_arn.split('/')
    volume_id = volume_split[1]
    return volume_id
    

def lambda_handler(event, context):
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    response = client.modify_volume(
    VolumeId = volume_id,
    VolumeType ='gp3',
)