# Contains the portfolio of the trader, including the cash, position, etc. Updates according to engine

class Portfolio():
    def __init__(self, initial_cash):
        self.initial_cash = initial_cash # might be cleaner way to do this
        self.cash = initial_cash
        self.shares = 0
        self.total_orders = 0
        # self.last_price = 0 # last price of the stock, updated daily in engine
        self.last_pf_value = initial_cash
        self.current_pf_value = initial_cash
        self.max_pf_value = initial_cash
        self.profitable_trades = 0

    def execute_trade(self, signal, price):
        # buy/sell as many as possible shares for now
        # Later on, record each transaction and its details (price, shares, date, etc.) for metrics and plotting.
        self.last_pf_value = self.current_pf_value # updates to last day (review logic for first day- fixed

        if signal == "BUY":
            shares_to_buy = self.cash//price # 2 slashes rounds down to nearest whole
            if shares_to_buy > 0:
                self.cash -= shares_to_buy*price
                self.shares += shares_to_buy
                self.total_orders += 1

        elif signal == "SELL":
            self.cash += self.shares * price
            self.shares = 0

        self.current_pf_value = self.shares*price + self.cash # updates current day

        if self.current_pf_value > self.last_pf_value: # This is wrong bc its not counting profitable "trades" its counting pf value increase
            self.profitable_trades += 1
        
        self.max_pf_value = max(self.max_pf_value, self.current_pf_value)

        print(self.cash)
        print(self.shares)
    