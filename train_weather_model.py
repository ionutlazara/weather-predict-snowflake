from snowflake.snowpark import Session
from snowflake.snowpark.ml.modeling.linear_model import LinearRegression
from snowflake.snowpark.ml.write import save_model


def train_weather_model(weather_df):
    # Split into 70% train, 30% test
    train_df, test_df = weather_df.random_split([0.7, 0.3], seed=42)

    features = ["MinTemp", "Humidity9am", "Pressure9am", "WindSpeed9am"]
    label = ["MaxTemp"]

    # Initialize and train Linear Regression model
    lr = LinearRegression(input_cols=features, label_cols=label)
    model = lr.fit(train_df)

    # Return both model and test data for evaluation
    return model, test_df


def deploy_weather_model(model, session: Session, stage_location: str = "@my_stage"):
    # Save the trained model as a Snowflake UDF for predictions
    save_model(
        model=model,
        model_name="TEMPERATURE_PREDICTOR",
        session=session,
        stage_location=stage_location
    )
