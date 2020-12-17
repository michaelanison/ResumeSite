import json
import boto3


def handler(event, context):

    dynamodb = boto3.client('dynamodb')

    # Get Visits
    response = dynamodb.get_item(
        TableName='resumecounter', Key={'Site': {'N': '0'}})

    visits = int(response["Item"]["Visits"]["N"]) + 1

    # Store Visits
    dynamodb.put_item(TableName='resumecounter', Item={
        'Site': {'N': '0'},
        'Visits': {'N': str(visits)}
    })
    return visits