import json


def lambda_handler(event, context):
    # TODO implement
    bodyString = json.dumps(event)
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": bodyString,
    }
