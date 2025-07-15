import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"Bucket: {bucket}")
        print(f"Key: {key}")

        obj = s3.get_object(Bucket=bucket, Key=key)
        content = obj['Body'].read().decode('utf-8')

        if 'confidential' in content.lower():
            print("Sensitive data detected!")
        else:
            print("File content safe.")

        return {
            'statusCode': 200,
            'body': f'File {key} scanned successfully.'
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise
