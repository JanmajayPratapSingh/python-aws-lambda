import json
import boto3

s3_client = boto3.client('s3')

def check_bucket_acl(bucket_name):
    try:
        response = s3_client.get_bucket_acl(Bucket=bucket_name)
        for grant in response['Grants']:
            if 'URI' in grant.get('Grantee', {}):
                if 'AllUsers' in grant['Grantee']['URI'] or 'AuthenticatedUsers' in grant['Grantee']['URI']:
                    return True
    except Exception as e:
        print(f"Error getting ACL for bucket {bucket_name}: {e}")
    return False

def check_bucket_policy(bucket_name):
    try:
        response = s3_client.get_bucket_policy_status(Bucket=bucket_name)
        if response.get('PolicyStatus', {}).get('IsPublic', False):
            return True
    except Exception as e:
        print(f"Error getting policy for bucket {bucket_name}: {e}")
    return False

def lambda_handler(event, context):
    public_buckets = []
    
    try:
        # List all buckets
        response = s3_client.list_buckets()
        buckets = response.get('Buckets', [])
        
        for bucket in buckets:
            bucket_name = bucket['Name']
            print(f"Checking bucket: {bucket_name}")
            
            # Check ACL and Policy
            if check_bucket_acl(bucket_name) or check_bucket_policy(bucket_name):
                public_buckets.append(bucket_name)
    
    except Exception as e:
        print(f"Error listing buckets: {e}")
    
    if public_buckets:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Public buckets found!',
                'public_buckets': public_buckets
            })
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'No public buckets found.'
            })
        }
