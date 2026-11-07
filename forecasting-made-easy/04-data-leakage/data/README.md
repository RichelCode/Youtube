# Data

| File | What it is |
|---|---|
| `fremont_bridge_daily.csv` | Bikes crossing the Fremont Bridge in Seattle, one row per day, 1 January 2023 to 30 September 2026 |
| `seattle_weather_daily.csv` | Daily rain (mm) and maximum temperature (°C) at the bridge, same dates |
| `build_fremont_daily.py` | Rebuilds the bike file from the city's hourly counts |
| `build_seattle_weather.py` | Rebuilds the weather file from Open-Meteo |

## Fremont Bridge bikes

**Source:** [Fremont Bridge Bicycle Counter](https://data.seattle.gov/d/65db-xm6k), City of Seattle Open Data. Public domain. Downloaded 7 November 2026.

| Column | Meaning |
|---|---|
| `date` | The day |
| `bikes` | Total bikes counted that day (both sides of the bridge) |
| `hours_counted` | How many hours of that day the counter reported. Normally 24, and 23 on the day the clocks go forward in March. **18 April 2023 has only 13**, because the counter was not working for part of the day. We replace that day with the same weekday one week earlier |

The city can revise past counts, so a fresh download may differ slightly. The committed file is the one used in the video.

## Seattle weather

**Source:** [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), for latitude 47.6475, longitude −122.3497 (the bridge), Seattle local time. Weather data by Open-Meteo.com, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

| Column | Meaning |
|---|---|
| `date` | The day |
| `rain_mm` | Total rain and other precipitation that day, in millimetres |
| `max_temp_c` | The day's highest temperature, in °C |

This is the weather that **really happened**. In this episode we feed it to a model on purpose, as **leak 4**, to show how much a forecast score improves when the model is quietly told the future.
