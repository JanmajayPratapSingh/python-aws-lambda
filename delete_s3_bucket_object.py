import boto3
client= boto3.client('s3')
response = client.delete_objects(
    Bucket='shivalikaa-testing-123',
    Delete={
        'Objects': [
            {
                'Key': 'ec2.py',
            
            },
            {
                'Key': 'xy.py',
            
            },
        ],
        'Quiet': True
    },
    
)