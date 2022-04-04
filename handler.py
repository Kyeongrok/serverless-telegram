import json, requests, os
from urllib import parse


def call_telegram(event:dict, context):

    r = ''
    status_code = 200
    if isinstance(event, dict) and event.get('queryStringParameters') != None:
        try:
            qsp = event['queryStringParameters']
            message = {k: parse.unquote(str(v)) for k, v in qsp.items()}
            url = f'https://api.telegram.org/bot281761192:{os.getenv("TELEGRAM_ACCESS_TOKEN")}/sendMessage?chat_id=173075344&text={message}'
            r = requests.get(url).json()

        except Exception as e:
            r = e
            status_code = 400

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "r": str(r)
    }

    response = {
        "statusCode": status_code,
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
    call_telegram('', '')
