import json

def lambda_handler(event, context):
    # Your logic goes here
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from the updated Lambda!')
    }