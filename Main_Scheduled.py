import requests
import pandas as pd
import time
from datetime import datetime
import schedule
from S3_Uploader import uploadToS3

def get_enrollment_data():
    try:
        # Enrollment by grade API
        url = 'https://educationdata.urban.org/api/v1/schools/ccd/enrollment/2021/grade-pk/'
               
        # Issuing the request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Convert JSON to DataFrame (Pandas)
            df = pd.DataFrame(data['results'])

            # set file name
            #filename = 'grade_pk_2021_data_' + date.today().strftime('%Y-%m-%d') + '.csv'
            filename = 'grade_pk_2021_data_' + time.strftime('%Y-%m-%d_%H-%M') + '.csv'
            
            # Save to CSV
            df.to_csv(filename, index=False)

            print("Data saved to " + filename)
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
            print("Error occured: {e}")

#Schedule 
#Ping API to get data and create a csv in current folder
schedule.every(1).minutes.do(get_enrollment_data)
#Push files from local to S3
schedule.every(2).minutes.do(uploadToS3)

while True:
     # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
    