import json
import boto3
import pymysql
import os

def lambda_handler(event, context):
    # SecretManagerからAurora接続情報を取得
    secret_name = os.environ['AURORA_SECRET_NAME']
    region_name = os.environ['AWS_REGION']

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    secret = json.loads(client.get_secret_value(SecretId=secret_name)['SecretString'])

    # SSM Parameter StoreからSQL文を取得
    ssm = boto3.client('ssm')
    sql_parameter = ssm.get_parameter(Name=os.environ['SQL_PARAMETER_NAME'])
    sql = json.loads(sql_parameter['Parameter']['Value'])

    # Auroraに接続
    conn = pymysql.connect(
        host=secret['host'],
        user=secret['username'],
        password=secret['password'],
        db=secret['dbname'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        # 結果をS3に保存
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=os.environ['S3_BUCKET_NAME'],
            Key=os.environ['S3_OUTPUT_KEY'],
            Body=json.dumps(result)
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Query executed and results saved to S3 successfully')
        }
    finally:
        conn.close()
