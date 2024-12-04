def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    df = dfc.select(list(dfc.keys())[0]).toDF()
    from pyspark.sql.functions import when
    result_df = df.withColumn(
        'CustomerSegment',
        when(df['LoyaltyPoints'] < 1000, 'Bronze')
        .when((df['LoyaltyPoints'] >= 1000) & (df['LoyaltyPoints'] < 2000), 'Silver')
        .otherwise('Gold')
    )
    dyf_segmented = DynamicFrame.fromDF(result_df, glueContext, 'segmented_loyalty_points')
    return(DynamicFrameCollection({'CustomTransform0': dyf_segmented}, glueContext))
