import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='murali-1cloud123',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)


