import boto3
dynamodb  = boto3.resource('dynamodb')
table = dynamodb.Table('emp')
resp = table.put_item(
        Item={
        'id': '2',
        'name': 'Sreelaja',
        'salary': 250000
    }
)
