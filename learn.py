# import numpy as np
import json
import pandas as pd

# How to read dataset
df = pd.read_json("spells.json")

# Get more info about data
print(df.info())

# Display the first 5 rows from dataset
print(df.head())
# Display the first 10 rows from dataset
print(df.head(10))

# Display the last 5 rows from dataset
print(df.tail())

# Display everything in json file
print(df.to_string())

# Display first and last 5 rows if more than 60 rows
# Check max rows with: print(pd.options.display.max_rows)
print(df)

# Create a simple DataFrame
data = {
    "name": ["fire ball", "ice shaft", "stone wall", "whirl wind"],
    "school": ["fire", "ice", "earth", "air"]
}
df = pd.DataFrame(data)
print(df)

# Return row 0 and 2 from above DataFrame
print(df.loc[[0, 2]])

# Give name to each row
df = pd.DataFrame(data, index = ["spell1", "spell2", "spell3", "spell4"])
print(df)

# Locate named index
print(df.loc["spell4"])