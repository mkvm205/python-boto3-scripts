import boto3
from pprint import pprint
aws_mgmt_console = boto3.session.Session(profile_name="default")
iam_console = aws_mgmt_console.client(service_name='iam')
result = iam_console.list_users()
pprint(result['Users'])