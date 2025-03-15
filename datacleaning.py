import pandas as pd
import os

# Set relative file path
#file_path = os.path.join("StockData", "Add .csv here")

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

numeric_cols = ["Price", "Open", "High", "Low"]
df[numeric_cols] = df[numeric_cols].astype(str).apply(lambda x: x.str.replace(',', '')).astype(float)

def convert_volume(vol):
    if isinstance(vol, str):
        if 'K' in vol:
            return float(vol.replace('K', '')) * 1_000
        elif 'M' in vol:
            return float(vol.replace('M', '')) * 1_000_000
    try:
        return float(vol)
    except ValueError:
        return None  

df["Vol."] = df["Vol."].apply(convert_volume)

df["Change %"] = df["Change %"].astype(str).str.replace('%', '').astype(float)

df.rename(columns={"Change %": "Change_Percent", "Vol.": "Volume"}, inplace=True)

date_range = pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="B")
df = df.set_index("Date").reindex(date_range).reset_index().rename(columns={"index": "Date"})

df[numeric_cols + ["Change_Percent", "Volume"]] = df[numeric_cols + ["Change_Percent", "Volume"]].interpolate()

output_folder = "StockDataClean"
os.makedirs(output_folder, exist_ok=True)  

original_filename = os.path.basename(file_path)
cleaned_filename = os.path.splitext(original_filename)[0] + "_Cleaned.csv"
output_path = os.path.join(output_folder, cleaned_filename)

df.to_csv(output_path, index=False)

print(f"Data cleaning complete. Saved as '{output_path}'.")
