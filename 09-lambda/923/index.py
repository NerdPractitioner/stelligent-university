import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('s3log')

def lambda_handler(event, context):
    
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
       response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
       data.extend(response['Items'])
    
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }