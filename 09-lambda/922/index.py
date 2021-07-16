
import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('holmes-log-data')

    print(f"Writing item with: {event}")
    response = table.put_item(
        Item={
            'source': event["source"],
            'region': event["region"],
            'detail': event["detail"]
        }
    )

    response = {'statusCode': 200,
    'body': json.dumps(response)}

    return response