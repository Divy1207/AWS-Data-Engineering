# AWS_data_engineering
Data Engineering Project on AWS

## Project Overview
This project establishes an end-to-end data pipeline using AWS for ingesting, validating, and transforming data from IoT sensors and websites. The pipeline is designed to handle real-time data, perform quality checks, and aggregate insights, enabling downstream analytics and machine learning.

## Architecture
### --> Workflow

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

Serving Layer:
Aggregated data is loaded into the S3 Gold Layer (Serving Zone) to support BI dashboards and machine learning models.
