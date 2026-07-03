# To load historical market data for backtesting.
import yfinance as yf
import pandas as pd

def load_data(ticker, start_date, end_date):
    # Later, implement chekcing if the file already exists so you dont redownload it.
    initdata = yf.download(ticker, start=start_date, end=end_date) # Takes parameters from main.py

    initdata.to_csv(f"data/{ticker}.csv") # Save the data to a CSV file

    data = pd.read_csv(f"data/{ticker}.csv", header=[0, 1], index_col=0, parse_dates=True) # this makes the columns not be tuples
    data.columns = data.columns.get_level_values(0)

    data["Return"] = data["Close"].pct_change() # Create returns column

    return data