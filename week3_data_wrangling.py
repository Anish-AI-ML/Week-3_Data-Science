"""Week 3 – Python & Data Wrangling
Run: python week3_data_wrangling.py data.xlsx
Requires: pandas, numpy, matplotlib, openpyxl
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else "data.xlsx"
df = pd.read_excel(path)

# Inspect
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Clean date formatting (remove stray apostrophes and parse compact date)
date_text = df["Date"].astype("string").str.strip().str.replace("'", "", regex=False)
date_text = date_text.replace({"20201226": "2020-12-26"})
df["Date"] = pd.to_datetime(date_text, errors="coerce")

# Fill missing Calories with the median. Leave unknown Date as NaT.
df["Calories"] = df["Calories"].fillna(df["Calories"].median())
df["Date_Missing_Flag"] = df["Date"].isna()

# Create derived columns
df["Calories_Per_Minute"] = df["Calories"] / df["Duration"].replace(0, float("nan"))
df["Pulse_Category"] = pd.cut(
    df["Pulse"], bins=[-float("inf"), 99, 119, float("inf")],
    labels=["Low", "Moderate", "High"]
)
df["Duration_Category"] = pd.cut(
    df["Duration"], bins=[-float("inf"), 30, 60, float("inf")],
    labels=["Short", "Standard", "Long"]
)

# Filter rows with valid dates for time-based analysis
dated = df[df["Date"].notna()].copy()
print("\nValid-date rows:\n", dated.head())

# Flag suspicious values without changing source measurements
print("\nDuration > 120 minutes:\n", df[df["Duration"] > 120])
print("\nPulse > Maxpulse:\n", df[df["Pulse"] > df["Maxpulse"]])

# Visualizations
plt.figure()
plt.plot(dated.sort_values("Date")["Date"], dated.sort_values("Date")["Calories"], marker="o")
plt.title("Calories Over Time"); plt.xlabel("Date"); plt.ylabel("Calories")
plt.xticks(rotation=45); plt.tight_layout(); plt.savefig("calories_over_time.png")

plt.figure()
plt.hist(df["Calories"], bins=8)
plt.title("Distribution of Calories"); plt.xlabel("Calories"); plt.ylabel("Frequency")
plt.tight_layout(); plt.savefig("calories_distribution.png")

plt.figure()
plt.scatter(df["Duration"], df["Calories"])
plt.title("Duration vs Calories"); plt.xlabel("Duration"); plt.ylabel("Calories")
plt.tight_layout(); plt.savefig("duration_vs_calories.png")

# Save cleaned data
df.to_csv("week3_cleaned_data.csv", index=False)
df.to_excel("week3_cleaned_data.xlsx", index=False)
print("\nSaved cleaned CSV and Excel files.")
