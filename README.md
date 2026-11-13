# Week 3 – Python & Data Wrangling

Based on the uploaded Week 3 PDF and `data.xlsx`.

## Course topics covered
- Python basics / Pandas data manipulation
- Reading data, filtering and creating columns
- Matplotlib visualizations

## Cleaning decisions
- Removed exact duplicate rows.
- Removed stray apostrophes from date strings and parsed dates.
- Parsed the compact `20201226` date as 2020-12-26.
- Filled missing `Calories` with the median of available Calories.
- Kept the missing `Date` as missing rather than guessing its value.
- Flagged unusual measurements (Duration > 120 and Pulse > Maxpulse) without changing source values.

## New columns
`Date_Missing_Flag`, `Calories_Per_Minute`, `Pulse_Category`, `Duration_Category`.

## Files
- `Week3_Cleaned_Data_Analysis.xlsx`
- `week3_cleaned_data.csv`
- `week3_data_wrangling.py`
- `week3_summary.json`
- Three PNG visualizations.
