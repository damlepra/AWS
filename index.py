import json
import boto3
import pandas as pd

s3_bucket = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    obj = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(f'New file : {obj} has been added to {bucket}')

    csv_obj = s3_bucket.get_object(Bucket=bucket, Key=obj)
    df = pd.read_csv(csv_obj.get("Body"))
    print(df)
    return {
        'statusCode': 200,
        'body': json.dumps(f'New file : {obj} has been added to {bucket}')
    }