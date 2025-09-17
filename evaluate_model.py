from snowflake.snowpark import functions as F

def evaluate_model(model, test_df):
    # Generate predictions on the test data
    predictions_df = model.predict(test_df)

    # Calculate residuals and error terms
    errors_df = predictions_df.with_columns({
        "residual": F.col("MaxTemp") - F.col("prediction"),
        "abs_error": F.abs(F.col("MaxTemp") - F.col("prediction")),
        "squared_error": (F.col("MaxTemp") - F.col("prediction")) ** 2
    })

    # Aggregate RMSE and MAE metrics
    metrics = errors_df.agg(
        F.sqrt(F.avg("squared_error")).alias("RMSE"),
        F.avg("abs_error").alias("MAE")
    ).collect()[0]

    return {"RMSE": metrics["RMSE"], "MAE": metrics["MAE"]}
