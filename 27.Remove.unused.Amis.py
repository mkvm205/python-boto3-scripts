import boto3
client = boto3.client('ec2')
# use descibre instance from boto3 ec2 documentation 

instances = client.describe_instances()
used_amis = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])
        
print(used_amis)

# Remove Duplicate AMIS 
def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis
unique_amis = remove_duplicates(used_amis)

print(unique_amis)
        
# Get all the AMIS in the account 
#Get Custom AMIS from the account 

custom_images = client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': ['available']
        },
      ],
    Owners= ['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

#Delete Unused AMIS
# First needs to Derigster the image 
for custom_ami in custom_amis_list:
    if custom_ami not in used_amis:
       print("deregistering_ami {}".format(custom_ami))
       client.deregister_image(ImageId=image['ImageId']) 