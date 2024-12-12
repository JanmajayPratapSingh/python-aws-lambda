import boto3
client = boto3.client('s3')
response=client.download_file('shivalikaa-testing-123','xy.py', 'xy.py')
print(response)