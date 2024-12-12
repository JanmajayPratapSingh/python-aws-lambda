import boto3

client = boto3.client('ec2')
response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp3'
            },
        },
    ],
    ImageId='ami-01b799c439fd5516a',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': True
    },
    SecurityGroupIds=[
        'sg-0f37394590d08f0e8',
    ],
    SubnetId='subnet-01fad936e7b524766',
    Placement={
        'AvailabilityZone': 'us-east-1a',
    },
    
)
instance_id=response['Instances'][0]['InstanceId']
client.get_waiter('instance_running').wait(InstanceIds=[instance_id])
#print instance information
instance=client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
print(instance)
print(f"{instance.get('PublicIpAddress','N/A')}")
print(f"{instance.get('PrivateIpAddress','N/A')}")
