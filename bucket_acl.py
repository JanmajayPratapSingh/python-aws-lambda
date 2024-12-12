import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='shivalikaa-testing-123',
)
print(response['Owner']['DisplayName'])
print(response['Grants'][0])

