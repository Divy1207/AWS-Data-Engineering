import json
import boto3
import os

def lambda_handler(event, context):
    glue_client = boto3.client('glue')
    
    # Use the provided job name
    job_name = "Status Check"  

    # Log the incoming event
    print("Received event: ", json.dumps(event))

    # Start the Glue job
    try:
        response = glue_client.start_job_run(JobName=job_name)
        print(f"Glue job invoked successfully: {response['JobRunId']}")
    except Exception as e:
        print(f"Error starting Glue job: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error starting Glue job')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f'Glue job invoked successfully: {response["JobRunId"]}')
    }
