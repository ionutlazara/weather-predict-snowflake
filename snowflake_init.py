import os

from get_snowflake_df import get_snowpark_session
from execute_sql_files import execute_sql_files
from upload_to_stage import upload_to_stage


if __name__ == "__main__":
    path_to_sql_folder = "/snowflake"
    path_to_dataset = "/dataset"
    stage_location = "@prediction_model.weather.seattle_weather_stage"

    snowpark_session = get_snowpark_session()

    #execute ddl statements
    execute_sql_files(session, os.path.join(path_to_sql_folder, 'ddl'))

    #put file into internal stage
    upload_to_stage(session, os.path.join(path_to_sql_folder, 'seattle-weather.csv'), stage_location)

    #execute dml statements
    execute_sql_files(session, os.path.join(path_to_sql_folder, 'dml'))
