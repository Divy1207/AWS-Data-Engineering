import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
S3_data_node = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://test-divy/datasets/payment.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1736611043146")

# Script generated for node Amazon S3
additional_options = {"hoodie.table.name": "my_hudi_table_trial", "hoodie.datasource.write.table.type": "COPY_ON_WRITE", "hoodie.datasource.write.operation": "insert", "hoodie.datasource.write.recordkey.field": "payment_id", "hoodie.datasource.write.precombine.field": "order_id", "hoodie.datasource.write.hive_style_partitioning": "true", "hoodie.parquet.compression.codec": "gzip", "hoodie.datasource.hive_sync.enable": "true", "hoodie.datasource.hive_sync.database": "default", "hoodie.datasource.hive_sync.table": "hudi_test", "hoodie.datasource.hive_sync.partition_extractor_class": "org.apache.hudi.hive.MultiPartKeysValueExtractor", "hoodie.datasource.hive_sync.use_jdbc": "false", "hoodie.datasource.hive_sync.mode": "hms"}
AmazonS3_node1736611082945_df = AmazonS3_node1736611043146.toDF()
AmazonS3_node1736611082945_df.write.format("hudi").options(**additional_options).mode("append").save("s3://testing-hudi-divy/myTest/")

job.commit()

#Note
#Hudi Parameters to mention in Glue job Parameters
--datalake-formats = hudi
--conf = spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.hive.convertMetastoreParquet=false