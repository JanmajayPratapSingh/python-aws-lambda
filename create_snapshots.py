import boto3
client=boto3.client('ec2')
response = client.create_snapshots(
    Description='string',
    InstanceSpecification={
        'InstanceId': 'string',
        'ExcludeBootVolume': True|False,
        'ExcludeDataVolumeIds': [
            'string',
        ]
    },
    
    
    
    CopyTagsFromSource='volume'
)