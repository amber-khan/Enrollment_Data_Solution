# education-bezos

Main_Scheduled.py:
This will call the API, create a CSV file and Schedule the ping for every minute.
Followed by uploading the file from local to S3

S3_Uploader.py:
This code establishes a connection to AWS using the IAM role credentials. It also defines the function responsible for uploading the file to an S3 bucket.

Secrets.py:
The Access Key and Secret Access Key are stored here, and are used by the S3_Uploader function to authenticate and establish a connection to AWS.

Snowflake_Scripting.sql:
All the queries that are required to setup the environment in Snowflake. This include Database, Schema, Table, Storage Integration, Stage and Snow Pipe

User_Query.sql:
This is the query that will answer "which 10 states had the highest number of children enroller in Pre-K?"

Snowflake_IAM_Policies.json:
This policy allows the IAM role to upload, read, and list objects within the specified S3 bucket.