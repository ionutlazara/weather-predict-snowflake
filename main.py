import os

from get_snowflake_df import get_snowpark_session, get_weather_df
from train_weather_model import train_weather_model, deploy_weather_model
from evaluate_model import evaluate_model


if __name__ == "__main__":
    path_to_sql_folder = "/snowflake"
    stage_location = ""

    snowpark_session = get_snowpark_session()

    # Load parsed weather data from Snowflake view
    weather_df = get_weather_df(snowpark_session, "seattle_weather_parsed").dropna()

    model, test_df = train_weather_model(weather_df)

    deploy_weather_model(model, snowpark_session, stage_location)

    metrics = evaluate_model(model, test_df)

    print/(metrics)