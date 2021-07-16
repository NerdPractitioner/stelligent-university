import json
import boto3

def lambda_handler(event, context):

    data = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('People')

    print(f"Writing item: {data}")
    response = table.put_item(
        Item={
            'user_id': data["user_id"],
            'first_name': data["first_name"],
            'age': data["age"]
        }
    )

    response = {'statusCode': 200,
    'body': json.dumps(response)}

    return response