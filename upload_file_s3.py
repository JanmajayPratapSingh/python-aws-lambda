import boto3
client = boto3.client('s3')
response=client.upload_file('lambda.md', 'shivalikaa-bucket-ultimate', 'lambda.md')
print(response)
# import boto3
# client = boto3.client('s3')
# response=client.upload_file('tmp/xy.py', 'shivalikaa-testing-123', 'xy.py')
# print(response)