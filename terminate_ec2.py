import boto3
client=boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-0d97e9d8b513c70ea','i-0557bf2745439a944','i-0204819ecf17a3629'
    ],
    
)