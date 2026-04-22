import pandas as pd
import re

df = pd.read_csv("I:\Social Media Analytics\practical\data_cleaning_regional.csv")

print("BEFORE CLEANING:\n")
print(df)

# cleaning
df["Name"] = df["Name"].str.lower()
df = df.dropna()
df = df.drop_duplicates()

# remove emojis, hashtags, URLs
df["Caption"] = df["Caption"].str.replace(r'http\S+|#\w+|[^\w\s]', '', regex=True)

print("\nAFTER CLEANING:\n")
print(df)

df.to_csv("cleaned_data.csv", index=False)
