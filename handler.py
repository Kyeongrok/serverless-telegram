import json
import numpy as np


def hello(event, context):
    a = np.arange(15).reshape(3, 5)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "a": str(a),
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json; charset=utf-8'
        },
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


if __name__ == "__main__":
    hello('', '')
