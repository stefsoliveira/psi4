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








# orders?orderId=5&date=25032020&amount=125



#
#
# //event object
# //TransactionHandler
#
# {
#
# "parameters": {
# 	"transactionId": 100
#
# }
#
# /transactions GET
#
# {
# 	"transactionId": 101,
# 	"type": "PURCHASE".
# 	"amount": 500
#
# }









































# import random
# # f = open("teste.txt", "w")
# # # for i in range(40):
# # #     for j in range(40):
# # #         f.write(".")
# # #     f.write("\n")
# # # print("foi")
# #
# # for i in range(100000):
# #     x = random.randint(0, 8)
# #     f.write(str(x))
#
#
# str= ['1', '2', '3']
#
# conc = int(str[0]+str[1]+str[2])
#
#
# print(conc=='123')

