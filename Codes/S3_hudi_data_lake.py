import sys
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Parse job arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from Amazon S3
input_s3_path = "s3://test-divy/datasets/payment.csv"
AmazonS3_source = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": "\"",
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [input_s3_path],
        "recurse": True
    },
    transformation_ctx="AmazonS3_source"
)

# Define Hudi options
hudi_options = {
    # Table configuration
    "hoodie.table.name": "my_hudi_table_trial2",
    "hoodie.datasource.write.table.type": "MERGE_ON_READ",
    "hoodie.datasource.write.operation": "insert",
    
    # Key and partition configuration
    "hoodie.datasource.write.recordkey.field": "payment_id",
    "hoodie.datasource.write.precombine.field": "order_id",
    "hoodie.datasource.write.hive_style_partitioning": "true",
    
    # Compression settings
    "hoodie.parquet.compression.codec": "gzip",
    
    # Hive sync settings
    "hoodie.datasource.hive_sync.enable": "true",
    "hoodie.datasource.hive_sync.database": "default",
    "hoodie.datasource.hive_sync.table": "hudi_test_2",
    "hoodie.datasource.hive_sync.partition_extractor_class": "org.apache.hudi.hive.MultiPartKeysValueExtractor",
    "hoodie.datasource.hive_sync.use_jdbc": "false",
    "hoodie.datasource.hive_sync.mode": "hms"
}

# Write data to Hudi
output_s3_path = "s3://testing-hudi-divy/myTest/"
AmazonS3_source_df = AmazonS3_source.toDF()
AmazonS3_source_df.write.format("hudi").options(**hudi_options).mode("append").save(output_s3_path)

# Commit the job
job.commit()


#Note
#Hudi Parameters to mention in Glue job Parameters
--datalake-formats = hudi
--conf = spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.hive.convertMetastoreParquet=false
