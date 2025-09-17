TRUNCATE TABLE prediction_model.weather.seattle_weather_raw;

COPY INTO prediction_model.weather.seattle_weather_raw
FROM (
  SELECT PARSE_JSON($1) AS data
  FROM @prediction_model.weather.seattle_weather_stage/seattle-weather.csv
)
FILE_FORMAT = (TYPE = 'CSV', FIELD_OPTIONALLY_ENCLOSED_BY='"', SKIP_HEADER=1);
