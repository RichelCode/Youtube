"""Rebuild seattle_weather_daily.csv: daily rain and maximum temperature at the Fremont Bridge.

Source: Open-Meteo Historical Weather API. Weather data by Open-Meteo.com, licensed CC BY 4.0.
Run from this folder:  python build_seattle_weather.py
"""
import json
import urllib.parse
import urllib.request
import pandas as pd

params = {"latitude": 47.6475, "longitude": -122.3497,          # the Fremont Bridge, Seattle
          "start_date": "2023-01-01", "end_date": "2026-09-30",
          "daily": "precipitation_sum,temperature_2m_max", "timezone": "America/Los_Angeles"}
url = "https://archive-api.open-meteo.com/v1/archive?" + urllib.parse.urlencode(params)
with urllib.request.urlopen(url, timeout=60) as response:
    d = json.load(response)["daily"]
weather = pd.DataFrame({"date": d["time"], "rain_mm": d["precipitation_sum"], "max_temp_c": d["temperature_2m_max"]})
weather.to_csv("seattle_weather_daily.csv", index=False)
print(f"Saved {len(weather):,} days")
