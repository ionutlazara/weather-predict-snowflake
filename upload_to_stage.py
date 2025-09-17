from snowflake.snowpark import Session

def upload_to_stage(session: Session, local_path: str, stage_location: str):
    # This uploads the local file to the specified Snowflake stage
    put_result = session.file.put(
        local_file_name=local_path,
        stage_location=stage_location,
        auto_compress=False,
        overwrite=True  # Overwrite if exists
    )
    print(put_result)
    
