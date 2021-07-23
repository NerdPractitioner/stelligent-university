import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    data = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('holmes-demo-data')

    print(f"Getting item with filter: {data}")

    response = table.query(
        KeyConditionExpression=Key('event_source').eq(data["event_source"]))["Items"]

    response = {'statusCode': 200,
    'body': json.dumps(response)}

    return response