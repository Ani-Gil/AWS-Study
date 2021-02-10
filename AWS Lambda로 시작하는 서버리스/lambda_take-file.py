import json
import boto3
import botocore

def lambda_handler(event, context):
    bucket_name = 'kumpacloudskills01'
    key = 'hello.txt'

    s3_client = boto3.client('s3')

    data = s3_client.get_object(Bucket=bucket_name, Key= key)
    file_text = data['Body'].read()

    return json.dumps(file_txt.decode('UTF-8'))