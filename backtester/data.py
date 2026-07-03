# To load historical market data for backtesting.
import yfinance as yf
import pandas as pd

def load_data(ticker, start_date, end_date):
    """
    Load historical market data for a given ticker symbol from Yahoo Finance.

    Parameters:
    - ticker (str): The ticker symbol of the stock (e.g., 'AAPL').
    - start_date (str): The start date for the historical data in 'YYYY-MM-DD' format.
    - end_date (str): The end date for the historical data in 'YYYY-MM-DD' format.

    Returns:
    - pd.DataFrame: A DataFrame containing the historical market data with columns: 
      ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'].
    """
    initdata = yf.download(ticker, start=start_date, end=end_date) # Takes parameters from main.py
    initdata.to_csv(f"data/{ticker}.csv")  # Save the data to a CSV file to be read by pandas.
    data = pd.read_csv(f"data/{ticker}.csv", index_col='Date', parse_dates=True)  # Read the CSV file into a DataFrame.
    data["Return"] = data["Close"].pct_change()
    data["20SMA"] = data["Close"].rolling(20).mean() # Don't keep this once you add more strategies
    data["3SMA"] = data["Close"].rolling(3).mean() # Make adding data columns up to the strategy. 
    return data # Returns the pandas DataFrame for specific stock.