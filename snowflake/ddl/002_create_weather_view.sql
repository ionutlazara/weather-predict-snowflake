CREATE OR REPLACE VIEW prediction_model.weather.seattle_weather_parsed AS
SELECT
  data:"MinTemp"::FLOAT AS MinTemp,
  data:"Humidity9am"::FLOAT AS Humidity9am,
  data:"Pressure9am"::FLOAT AS Pressure9am,
  data:"WindSpeed9am"::FLOAT AS WindSpeed9am,
  data:"MaxTemp"::FLOAT AS MaxTemp
FROM seattle_weather_raw;
