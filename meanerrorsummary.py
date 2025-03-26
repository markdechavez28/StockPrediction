import os
import pandas as pd

def summarize_errors():
    folder = "StockMeanError 1"
    summary_data = []

    for file in os.listdir(folder):
        if file.endswith("_mae.txt"):
            stock = file.split("_")[0] 
            file_path = os.path.join(folder, file)

            with open(file_path, "r") as f:
                lines = f.readlines()
                mae = float(lines[1].split(":")[1].strip())
                mse = float(lines[2].split(":")[1].strip())
                rmse = float(lines[3].split(":")[1].strip())
                mape = float(lines[4].split(":")[1].strip().replace("%", ""))  

            summary_data.append([stock, mae, mse, rmse, mape])

    df = pd.DataFrame(summary_data, columns=["Stock", "MAE", "MSE", "RMSE", "MAPE"])

    avg_row = ["Average", df["MAE"].mean(), df["MSE"].mean(), df["RMSE"].mean(), df["MAPE"].mean()]
    df.loc[len(df)] = avg_row  

    summary_path = os.path.join(folder, "summary.csv")
    df.to_csv(summary_path, index=False)

    print(f"Summary saved to {summary_path}")
    print(df)

summarize_errors()
