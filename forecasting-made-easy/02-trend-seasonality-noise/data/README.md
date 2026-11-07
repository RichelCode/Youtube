# Data

| File | What it is |
|---|---|
| `fremont_bridge_daily.csv` | Bikes crossing the Fremont Bridge in Seattle, one row per day, 1 January 2023 to 30 September 2026 |
| `accra_hourly_2026.csv` | Hourly temperature (°C), relative humidity (%) and cloud cover (%) in Accra, Ghana, 1 August to 25 October 2026 (the same file as Episode 1) |
| `build_fremont_daily.py` | The script that made `fremont_bridge_daily.csv` from the city's hourly counts |

## Fremont Bridge bikes

**Source:** [Fremont Bridge Bicycle Counter](https://data.seattle.gov/d/65db-xm6k), City of Seattle Open Data. Public domain. Downloaded 7 November 2026.

The counter uses sensors in the paths on both sides of the bridge and counts every bike, every hour. We add up the 24 hours of each day.

| Column | Meaning |
|---|---|
| `date` | The day |
| `bikes` | Total bikes counted that day (both sides of the bridge) |
| `hours_counted` | How many hours of that day the counter reported. Normally 24. It is 23 on the day the clocks go forward in March, which is normal. **18 April 2023 has only 13**, because the counter was not working for part of the day, so that day's total is too low |

The city can revise past counts, so running `build_fremont_daily.py` later may give slightly different numbers. The committed file is the one used in the video.

## Accra temperature

**Source:** [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). Weather data by Open-Meteo.com, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

This is reanalysis, a model-based reconstruction of the weather rather than readings from one weather station.
