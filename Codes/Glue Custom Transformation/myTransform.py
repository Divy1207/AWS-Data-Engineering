from awsglue import DynamicFrame
from pyspark.sql.functions import *

def segment_loyalty_pts(self,fieldName):

    df = self.toDF()

    result_df = df.withColumn(
            'CustomerSegment',
             when(df[fieldName] < 1000, 'Bronze')
            .when((df[fieldName] >= 1000) & (df[fieldName] < 2000), 'Silver')
            .otherwise('Gold')
        )

    return DynamicFrame.fromDF(result_df, self.glue_ctx, self.name)
    
DynamicFrame.segment_loyalty_pts = segment_loyalty_pts