CREATE OR REPLACE DATABASE prediction_model;

CREATE OR REPLACE SCHEMA prediction_model.weather;

CREATE OR REPLACE TABLE prediction_model.weather.seattle_weather_raw (
  data VARIANT
);
