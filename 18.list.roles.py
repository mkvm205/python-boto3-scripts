import boto3
from pprint import pprint
aws_mgmt_console = boto3.session.Session(profile_name="default")
iam_console = aws_mgmt_console.client(service_name='iam')

roles = iam_console.list_roles()
for each_roles in roles['Roles']:
    print(each_roles['RoleName'] )  
    print(each_roles['Arn'] )  
    
