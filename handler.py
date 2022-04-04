import json, requests


def call_telegram(event, context):

    qsp = event['queryStringParameters']

    message = json.dumps(qsp)
    url = f'https://api.telegram.org/bot281761192:AAE7h61HIio8eviXggpssYHrJJ58nHWT32A/sendMessage?chat_id=173075344&text={message}'
    r = requests.get(url)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "r": r.json()
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
    call_telegram('', '')
