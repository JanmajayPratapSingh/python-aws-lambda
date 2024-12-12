import boto3
import logging
from datetime import datetime

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = 'your-primary-bucket'
    backup_bucket = 'your-backup-bucket'
    
    try:
        # List objects in the source bucket
        response = s3_client.list_objects_v2(Bucket=source_bucket)
        
        if 'Contents' not in response:
            logger.info('No files to back up')
            return {
                'statusCode': 200,
                'body': 'No files to back up'
            }
        
        for obj in response['Contents']:
            file_key = obj['Key']
            timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
            backup_key = f'backup/{timestamp}/{file_key}'
            
            # Copy the file to the backup bucket
            copy_source = {'Bucket': source_bucket, 'Key': file_key}
            s3_client.copy_object(CopySource=copy_source, Bucket=backup_bucket, Key=backup_key)
            logger.info(f'Backed up {file_key} to {backup_key}')
        
        return {
            'statusCode': 200,
            'body': 'Backup completed successfully'
        }
    
    except Exception as e:
        logger.error(f'Error during backup: {e}')
        return {
            'statusCode': 500,
            'body': f'Error during backup: {e}'
        }


# A real-life use case for a Python AWS Lambda function that performs routine system backups could be for a company managing critical application data in AWS S3. Here's a detailed scenario:

# Use Case: E-Commerce Platform Backup
# Scenario:

# An e-commerce company uses AWS S3 to store critical application data, including product information, user data, and transaction logs. The company needs to ensure that this data is backed up regularly to safeguard against accidental deletion, data corruption, or system failures.

# Solution:

# The company implements an AWS Lambda function to automate the backup process. Here's how it fits into their operational workflow:

# Routine Backup:

# The Lambda function is scheduled to run daily using an Amazon CloudWatch Events rule.
# It automatically backs up all files from the primary S3 bucket (where current data is stored) to a backup S3 bucket.
# Versioning and Compliance:

# The Lambda function creates timestamped backups in a dedicated "backup" directory within the backup S3 bucket.
# This versioning helps the company maintain compliance with data retention policies by preserving historical snapshots of the data.
# Data Integrity:

# The function ensures that every file in the primary bucket is copied to the backup bucket, maintaining data integrity and providing a reliable recovery point.
# Automated Error Handling:

# If a backup operation fails (e.g., due to permission issues or network problems), the Lambda function logs the error details in Amazon CloudWatch Logs.
# Alerts can be configured using Amazon SNS to notify the IT team immediately if any issues are detected.
# Disaster Recovery:

# In the event of a data loss or corruption scenario, the backup data can be quickly restored from the backup S3 bucket.
# This minimizes downtime and ensures business continuity.
