import boto3
client=boto3.client('s3')
response=client.get_object(
    Bucket='shivalikaa-testing-123',
    
    Key='xy.py',
    
)