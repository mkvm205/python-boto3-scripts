import boto3
dynamodb  = boto3.resource('dynamodb')
table = dynamodb.Table('emp')
resp =table.get_item(
    Key={
        'id':'2'
    }
)
print(resp['Item'])
# Delete Item 
table.delete_item(
    Key={
        'id': '2'
    }
)

