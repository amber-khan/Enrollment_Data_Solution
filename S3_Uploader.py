#This will read all the .csv file in this given directory and upload to S3 bucket
from Secrets import access_key, secret_access_key
import boto3
import os

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key )

def uploadToS3():
    try:
        for file in os.listdir():
            if '.csv' in file:
                upload_file_bucket = 'education-data-bucket'
                upload_file_key = 'enrollment_2021/' + str(file)
                client.upload_file(file, upload_file_bucket,upload_file_key)
    except Exception as e:
            print("Error occured: {e}")