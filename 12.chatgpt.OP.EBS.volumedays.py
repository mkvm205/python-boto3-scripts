import boto3

def get_running_instances(region):
    ec2_client = boto3.client('ec2')

    # Describe running instances
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    running_instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_details = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'State': instance['State']['Name']
            }
            running_instances.append(instance_details)

    return running_instances

if __name__ == "__main__":
    region = 'your_aws_region'  # Replace with your AWS region, e.g., 'us-east-1'

    running_instances = get_running_instances(region)

    if running_instances:
        print("\nRunning Instances:")
        for instance in running_instances:
            print(f"Instance ID: {instance['InstanceId']}, Type: {instance['InstanceType']}, "
                  f"Public IP: {instance['PublicIpAddress']}, State: {instance['State']}")
    else:
        print("\nNo running instances found in the specified region.")
