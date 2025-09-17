from snowflake.snowpark import Session


def get_snowpark_session() -> Session:
    # Connection parameters - replace with your Snowflake account details
    connection_parameters = {
        "account": "<account>",
        "user": "<user>",
        "password": "<pass>",
        "role": "<role>",
        "warehouse": "<compute_wh>",
        # "database": "<database>",
        # "schema": "<schema>"
    }
    
    # Create Snowflake session
    session = Session.builder.configs(connection_parameters).create()
    return session


def get_weather_df(session: Session, table_name: str):

    # Load data from the view as Snowpark DataFrame
    weather_df = session.table(table_name)
    
    return weather_df
