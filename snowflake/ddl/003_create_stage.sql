CREATE OR REPLACE STAGE prediction_model.weather.seattle_weather_stage
  FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1);
