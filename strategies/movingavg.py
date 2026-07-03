# Simple Moving Average Strategy.

def movingavgsignal(row): # Takes in data from engine and makes decision
    date = row["Date"]
    open = row["High"]
    high = row["Low"]
    close = row["Close"]
    volume = row["Volume"]
    movingavg = row["Moving Average"]
    if price > movingavg:
        return "BUY"
    elif price = x:
        return "HOLD"
    else:
        return "SELL"
    