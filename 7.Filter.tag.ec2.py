import boto3
client = boto3.client('ec2')
resp = client.describe_instances(Filters = [{
    'Name': 'tag:ENV',
    'Values' : ['Prod', 'dev']
}])
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {}".format(instance['InstanceId']))