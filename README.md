![Updated_AWS4](https://github.com/user-attachments/assets/a61f663c-c3cf-4096-9d97-eaee311294a5)



# Data Engineering on AWS
Data Engineering Project on AWS

## Project Overview
This project establishes an end-to-end data pipeline using AWS for ingesting, validating, and transforming data from IoT sensors and websites. The pipeline is designed to handle real-time data, perform quality checks, and aggregate insights, enabling downstream analytics and machine learning.

## Architecture Workflow 

### Data Ingestion:
Data from IoT sensors and websites is stored in the S3 Bronze Layer (Landing Zone).
Data arrives in the S3 bucket with a pre-configured prefix and file path.

### Event Detection:
AWS Lambda is triggered upon data arrival, detecting events based on the specified prefix and file path patterns.

### Data Validation and Quality Checks:
Lambda invokes an AWS Glue job that performs data quality checks on the new data.
Quality checks are defined in SQL queries to validate data integrity.
Example check: Orders with statuses outside the approved list are filtered out as invalid and sent to a discard folder.

### Data Transformation and Aggregation:
Valid data is moved to the Silver Layer in S3 for further processing.
Aggregations and insights are then developed on validated data to enable meaningful analysis.

### Serving Layer:
Aggregated data is loaded into the S3 Gold Layer (Serving Zone) to support BI dashboards and machine learning models.

## Components
1. S3 Buckets (Bronze, Silver, Gold)
Bronze Layer: Raw data is initially stored here. It serves as the data landing zone.
Silver Layer: Contains validated data after quality checks, ready for aggregations.
Gold Layer: Stores aggregated and refined data for analytics, BI, and ML.

2. AWS Lambda
Function: Detects data arrival events in the Bronze Layer.
Trigger: Configured with S3 Event Notifications for specific prefixes and paths.
Workflow: Invokes the AWS Glue job upon detection of new data.

3. AWS Glue Job
Role: Executes data quality checks and transformations.
Logic:
Runs SQL-based checks on ingested data.
Filters out invalid records, such as orders with unrecognized statuses, moving them to a discard folder.
Moves valid records to the Silver Layer for further processing.

4. Data Aggregation
After quality checks, data in the Silver Layer is aggregated to generate insights.
Aggregated data is transferred to the Gold Layer, providing a clean and structured dataset for BI tools and ML models.

### Example Use Cases

Order Status Validation:
Checks for valid order statuses. If the status is invalid, the record is moved to a discard folder.
Valid orders are retained in the Silver Layer for further processing.

Aggregation and Insights:
Generate aggregations, such as total orders per status, average order value, and sensor data summaries.
Store aggregated data in the Gold Layer for seamless integration with BI dashboards.

### Technologies Used
AWS S3: Data lake storage for raw, validated, and aggregated data.

AWS Lambda: Event-driven serverless functions for detecting new data arrivals.

AWS Glue: Data integration service for ETL operations, handling quality checks and transformations.

Glue Data Catalog: Metadata management

AWS Athena - Ad-hoc analysis

## Getting Started
Prerequisites
AWS Account with access to S3, Lambda, Glue, and IAM services.
Python 3.8 or above (for Lambda and Glue job development).

IAM Roles:
Role with S3, Glue, and Lambda permissions to allow inter-service access.

Deployment
Configure S3 Buckets:

Create separate buckets for Bronze, Silver, and Gold Layers.
Update the config/s3_paths.yml file with the bucket paths.

Lambda Setup:
Deploy event_detection_lambda.py in AWS Lambda.
Set S3 event notifications on the Bronze Layer bucket to trigger the Lambda function.

Glue Job Setup:
Create a Glue job using data_quality_checks.py.
Configure the job to be triggered by Lambda.

Testing:
Upload sample data to the Bronze Layer.
Verify that Lambda triggers the Glue job and data is moved accordingly.

## Implemented Features
1. Data Validation Checks
Implemented comprehensive data validation checks to ensure data quality:
Data Type Verification: Ensures that each column in the dataset matches the expected data type.
Range Checks: Verifies numerical values fall within a specified range.
Business Logic Validation: Applied business rules to check for valid order statuses or sensor readings, filtering out invalid data.

2. Automated Metadata Management
Automated the tracking of data lineage to maintain transparency and traceability.
Used Glue Catalog to manage metadata and provide insights into the transformations applied to data at each stage of the pipeline.
Ensured that every step of the transformation process is documented and can be traced back for auditing or troubleshooting purposes.

3. Integration with AWS Athena
Integrated AWS Athena to enable ad-hoc querying on the Silver Layer for flexible and dynamic analysis.
Created views for easy exploration of the validated data, enabling users to run SQL queries without needing to move data.

4. Automated Alerting for Data Quality Failures
Set up AWS CloudWatch to monitor the pipeline for data quality issues (e.g., missing, corrupted, or invalid data).
Configured SNS Notifications to automatically alert stakeholders of failures or issues with the incoming data, ensuring timely resolution.

5. Enhanced Data Governance
PII Redaction: Implemented redaction of Personally Identifiable Information (PII) such as email addresses, phone numbers, and other sensitive information.
Applied data privacy regulations (e.g., GDPR and HIPAA) to ensure that sensitive data is securely handled and only authorized personnel can access it.
Introduced data governance policies that restrict unauthorized access and ensure that only compliant, non-sensitive data is retained.

## Conclusion
This project showcases a robust and scalable data pipeline on AWS. By integrating real-time ingestion, validation, and transformation, it supports reliable data storage and downstream analytics for BI and machine learning. The implementation of data validation checks, metadata management, Athena integration, automated alerting, and strong data governance ensures high-quality data delivery, compliance with regulations, and transparency in the data pipeline.

Introduced data governance policies that restrict unauthorized access and ensure that only compliant, non-sensitive data is retained.

