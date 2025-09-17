import os

from snowflake.snowpark import Session


def execute_sql_files(session: Session, folder_path: str):
    # Iterate over each .sql file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".sql"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                sql_statements = file.read()
            try:
                # Execute all SQL statements in the file
                session.sql(sql_statements).collect()
                print(f"Executed {filename} successfully.")
            except Exception as e:
                print(f"Error executing {filename}: {e}")
