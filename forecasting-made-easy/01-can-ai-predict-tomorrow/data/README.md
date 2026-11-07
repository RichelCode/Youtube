# Data

| File | What it is |
|---|---|
| `accra_hourly_2026.csv` | Hourly weather for Accra, Ghana, 1 August to 25 October 2026 (2,064 hours) |

| Column | Meaning |
|---|---|
| `time` | Hour, local time (Accra is UTC+0 all year, so there are no daylight-saving jumps) |
| `temperature_2m` | Air temperature 2 m above the ground, °C. **This is what we forecast** |
| `relative_humidity_2m` | Relative humidity, % |
| `cloud_cover` | Cloud cover, % |

**Source:** [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), retrieved 3 November 2026. Weather data by Open-Meteo.com, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

This is reanalysis: a model-based reconstruction of the weather, not readings from one thermometer. Values can differ slightly from a local weather station. The whole period comes after Chronos-2 was released (October 2025), so the model cannot have seen it during training.
