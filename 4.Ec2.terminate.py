import boto3
client = boto3.client('ec2')
resp = client.terminate_instances(InstanceIds=['i-0db186cb62e2f5ab4','i-049ec9d6eacac572c','i-0079fa1cca3693be2' ])

for instance in resp['TerminatingInstances']: 
    print("The Instances with id {} Terminated".format(instance['InstanceId']))