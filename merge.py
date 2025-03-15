import os
import pandas as pd

stock_data_path = "StockDataClean/JGS Historical Data_Cleaned.csv"
prediction_data_path = "StockPredictions/JGS_Predictions.csv"
output_path = "StockMerge"

os.makedirs(output_path, exist_ok=True)

output_filename = "JGS.csv"

output_path = os.path.join(output_path, output_filename)

def merge_stock_data(stock_data_path, prediction_data_path, output_path):
    stock_df = pd.read_csv(stock_data_path, usecols=["Date", "Price"])
    prediction_df = pd.read_csv(prediction_data_path, usecols=["Date", "Predicted_Price"])

    merged_df = pd.merge(stock_df, prediction_df, on="Date", how="outer")

    merged_df["Price_Merged"] = merged_df["Price"].combine_first(merged_df["Predicted_Price"])

    merged_df = merged_df[["Date", "Price_Merged"]]

    merged_df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

merge_stock_data(stock_data_path, prediction_data_path, output_path)