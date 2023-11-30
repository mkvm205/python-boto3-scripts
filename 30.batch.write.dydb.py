import boto3
dynamodb  = boto3.resource('dynamodb')
table = dynamodb.Table('emp')

with table.batch_writer() as batch:
    for x in range(100):
        batch.put_item(
            Item={
                'id': str(x),
                 'name': 'Name-{}'.format(x)
            }
        )
