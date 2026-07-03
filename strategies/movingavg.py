# Simple Moving Average Strategy.

class MovingAvg():
    def __init__(self, short_window, long_window): # Needs to be constructed in main or engine
        self.short_window = short_window
        self.long_window = long_window

    def prep_data(self, data): # To create necesesary columns in the data frame for this strategy
        data = data.copy() # so original df isnt modified

        raw_short = data["Close"].rolling(self.short_window).mean()  # to prevent look ahead bias, shift rolling averages by 1 day so that the current day doesn't use the current day's closing price to calculate the average
        raw_long = data["Close"].rolling(self.long_window).mean() 

        data[f"{self.short_window}SMA"] = raw_short.shift(1)
        data[f"{self.long_window}SMA"] = raw_long.shift(1)
        return data

    def generate_signal(self, uptodf): # CHANGE: needs to take all data up to the current date (index). DON'T LET IT SEE ALL DATA (look ahead bias)
        shortma_name = f"{self.short_window}SMA"
        longma_name = f"{self.long_window}SMA"
        date = uptodf.iloc[-1]
        if date[shortma_name] > date[longma_name]:
            return "BUY"
        elif date[shortma_name] < date[longma_name]:
            return "SELL"
        return "HOLD"
        