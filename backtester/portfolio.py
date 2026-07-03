# Contains the portfolio of the trader, including the cash, position, etc. Updates according to engine

class Portfolio():
    def __init__(self, initial_cash):
        self.cash = initial_cash
        self.shares = 0

    def execute_trade(self, signal, price):
        # buy/sell as many as possible shares for now
        if signal == "BUY":
            shares_to_buy = self.cash//price
                self.cash -= shares_to_buy*price
                self.shares += shares_to_buy
        elif signal == "SELL":
                self.cash += self.shares * price
                self.shares = 0

