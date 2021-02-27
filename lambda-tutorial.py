import json

print('loading')

def lambda_handler(event, context):
    orderId = event['queryStringParameters']['orderId']
    orderDate = event['queryStringParameters']['date']
    orderAmount = event['queryStringParameters']['amount']

    print('orderId='+ orderId)
    print('orderDate=' + orderDate)
    print('orderAmount=' + orderAmount)

    orderResponse = {}
    orderResponse['orderID'] = orderId
    orderResponse['date'] = orderDate
    orderResponse['amount'] = orderAmount
    orderResponse['message'] = 'This is a response message'

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-type'] = 'application/json'
    responseObject['body']: json.dumps(orderResponse)

    return responseObject



