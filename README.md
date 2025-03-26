# 📈 LSTM-Based Stock Forecasting for the Philippines' Top 16 Companies

## 🏆 Project Overview
This project utilizes a **Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN)** to forecast stock price movements of the largest companies in the Philippines. The model predicts the next 7 days of stock prices based on **over 10 years of historical data** per company.

## 📅 Timeline
- **March 2025**
- **Principal Developer:** [Your Name]

## 🛠 Features
✅ **Python-based ETL Pipeline**: Processed **100,000+ data points** for efficient analysis and storage.  
✅ **16 LSTM Models**: Each trained on an individual company’s historical data.  
✅ **Time-Series Forecasting**: Predicts the next 7 business days' stock prices (**March 17 to March 25, 2025**).  
✅ **Performance Evaluation**: Mean error calculations for model assessment.

## 📊 Model Performance Summary
| Metric  | Value |
|---------|-------|
| **Average MAE**  | 18.49 |
| **Average MSE**  | 1232.56 |
| **Average RMSE** | 20.99 |
| **Average MAPE** | 5.64% |

📌 **Interpretation:** With an average **MAPE of 5.64%**, the model provides a fairly accurate prediction, with errors averaging around 5.64% of actual stock prices.

## 📂 Project Structure
```
📁 ForecastNotebooks/  # Jupyter notebooks for LSTM implementation
📁 StockData/          # Raw stock data since 2010 (if available), some from 2011-2012
📁 StockDataClean/     # Normalized stock data for model training
📁 StockMeanError/     # Contains TXT files with MAE, MSE, RMSE, and MAPE results for each company
📁 StockMerge/         # Merged datasets of predictions and cleaned stock data
📁 StockModels/        # Trained LSTM models (.h5 files)
📁 StockPredictions/   # 7-day stock price predictions (March 17 - March 25, 2025)
📁 StockTruePrices/    # Actual stock prices for comparison (March 17 - March 25, 2025)
📄 main.py            # LSTM training and forecasting script
📄 evaluate.py        # Computes mean error metrics
📄 README.md          # Project documentation
```

## 🚀 How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/lstm-stock-forecasting.git
   cd lstm-stock-forecasting
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Forecasting Model**:
   ```bash
   python main.py
   ```
4. **Evaluate Performance**:
   ```bash
   python evaluate.py
   ```

## 📌 Future Improvements
🔹 Enhance feature engineering with technical indicators (e.g., RSI, MACD, Bollinger Bands).  
🔹 Optimize hyperparameters to further reduce prediction errors.  
🔹 Experiment with hybrid models (CNN-LSTM, Transformer-based forecasting).  
