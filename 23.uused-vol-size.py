import boto3
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')
volumes = ec2_client.describe_volumes()
sns_arn = 'arn:aws:sns:us-east-1:685164813512:unused-volume-alerts-krish'

def lambda_handler(event, context):
    unused_vols = []
    size = 0
    for volume in volumes['Volumes']:
        if len(volume['Attachments']) == 0:
            unused_vols.append(volume['VolumeId'])
            size = size + volume['Size']
            print(volume)
            print("-----"*5)
    
    email_body = '###################### Krish Unused Volumes ############ \n'
    
    for vol in unused_vols:
        email_body = email_body + "VolumeId = {}\n".format(vol)
    
    #Send Email 
    email_body = email_body + "\n\n Total Unused Volume Size = {}".format(size)
    sns_client.publish(
        TopicArn = sns_arn,
        Subject = 'Krishn Unused Volumes' ,
        Message = email_body
    )