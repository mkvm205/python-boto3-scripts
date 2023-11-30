import boto3
client = boto3.client('ec2')
client.start_instances(InstanceIds=['i-0079fa1cca3693be2'])