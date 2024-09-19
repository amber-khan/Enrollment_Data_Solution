USE ROLE SYSADMIN;
--Create a new database
CREATE OR REPLACE DATABASE EDUCATION;

--Create a schema
CREATE OR REPLACE SCHEMA EDUCATION_URBAN;

--Create a table to store data
CREATE OR REPLACE TABLE GRADES (
YEAR INTEGER,
NCESSCH INTEGER,
NCESSCH_NUM INTEGER,
GRADE INTEGER,
RACE INTEGER,
SEX INTEGER,
ENROLLMENT INTEGER,
FIPS INTEGER,
LEAID INTEGER

);

--Create a Storage Integration for S3
CREATE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::213083243868:role/mySnowflakeRole'
  STORAGE_ALLOWED_LOCATIONS = ('*')
  ;
--Create an external stage pointing to AWS S3
--url = 's3://education-data-bucket/';
CREATE STAGE mySnowflakeStage
  URL = 's3://education-data-bucket/'
  STORAGE_INTEGRATION = s3_int;

--List files in stage
list @mySnowflakeStage;

--Create a SnowPipe to copy data from S3 into Stage into destination table

CREATE OR REPLACE PIPE myPipe
  AUTO_INGEST = TRUE
  AS
    COPY INTO EDUCATION.EDUCATION_URBAN.GRADES
      FROM @mySnowflakeStage
      FILE_FORMAT = (type = 'csv')
      ON_ERROR = 'CONTINUE';
