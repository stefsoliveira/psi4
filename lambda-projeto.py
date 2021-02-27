import json
import requests
import boto3


def lambda_handler(event, context):
        response = requests.get('https://apitempo.inmet.gov.br/estacao/diaria/2019-10-01/2019-10-31/A301')
        formatted_response = response.json()       
        client = boto3.client('kinesis')
        for response in formatted_response:
                client.put_record(
                        StreamName = 'stationData',
                        Data=json.dumps(formatted_response),
                        PartitionKey='part_key')
        return {
                'statusCode': 200,
                'body': json.dumps(formatted_response),
                # 'body': json.dumps(response.json())
        }
        
