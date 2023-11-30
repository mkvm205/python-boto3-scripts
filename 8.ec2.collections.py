import boto3
ec2 = boto3.resource('ec2')
for server in ec2.instances.all():
    print('Instance id is {} and Instance type is {}'.format(server.instance_id,server.instance_type))