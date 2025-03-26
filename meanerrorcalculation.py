import pandas as pd
import numpy as np
import os

def calculate_errors(pred_file, true_file):
    
    pred_df = pd.read_csv(pred_file, parse_dates=["Date"])
    true_df = pd.read_csv(true_file, parse_dates=["Date"])

    true_df.rename(columns={"Price": "True_Price"}, inplace=True)

    merged_df = pd.merge(pred_df, true_df, on="Date", how="inner")

    predicted = merged_df["Predicted_Price"].values
    actual = merged_df["True_Price"].values

    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100

    abbrev = os.path.basename(pred_file).split("_")[0]
    output_filename = f"StockMeanError/{abbrev}_mae.txt"

    with open(output_filename, "w") as f:
        f.write(f"Stock: {abbrev}\n")
        f.write(f"MAE: {mae:.4f}\n")
        f.write(f"MSE: {mse:.4f}\n")
        f.write(f"RMSE: {rmse:.4f}\n")
        f.write(f"MAPE: {mape:.2f}%\n")

    print(f"✅ Error metrics saved to {output_filename}")

os.makedirs("StockMeanError", exist_ok=True)

pred_file = "StockPredictions/URC_predictions.csv"
true_file = "StockTruePrices/URC_true.csv"

calculate_errors(pred_file, true_file)
