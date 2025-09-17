SELECT
  MinTemp,
  Humidity9am,
  Pressure9am,
  WindSpeed9am,
  TEMPERATURE_PREDICTOR(MinTemp, Humidity9am, Pressure9am, WindSpeed9am) AS PredictedMaxTemp
FROM prediction_model.weather.seattle_weather_parsed
WHERE MaxTemp IS NOT NULL
LIMIT 10;
