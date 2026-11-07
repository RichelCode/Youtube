"""Rebuild fremont_bridge_daily.csv from the City of Seattle's hourly bike counts.

Source: Fremont Bridge Bicycle Counter, City of Seattle Open Data (public domain)
https://data.seattle.gov/d/65db-xm6k

Run from this folder:  python build_fremont_daily.py
The city can revise past counts, so a fresh download may differ slightly from the committed file.
"""
import pandas as pd

URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

hourly = pd.read_csv(URL)
hourly.columns = ["ds", "total", "west", "east"]
hourly["ds"] = pd.to_datetime(hourly["ds"], format="%m/%d/%Y %I:%M:%S %p")
hourly = hourly[(hourly.ds >= "2023-01-01") & (hourly.ds < "2026-10-01")]

by_day = hourly.set_index("ds")["total"].resample("D")
daily = pd.DataFrame({"bikes": by_day.sum(min_count=1), "hours_counted": by_day.count()})
daily.index.name = "date"
daily["bikes"] = daily["bikes"].astype("Int64")
daily.to_csv("fremont_bridge_daily.csv")
print(f"Saved {len(daily):,} days, {daily.index.min():%d %b %Y} to {daily.index.max():%d %b %Y}")
