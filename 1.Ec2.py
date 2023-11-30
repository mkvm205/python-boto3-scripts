import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-06aa3f7caf3a30282',InstanceType='t2.micro',MaxCount=1,MinCount=1 )

for instance in resp['Instances']:
    print(instance['InstanceId'])