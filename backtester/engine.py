# Runs the backtesting on the data using the given strategy.

class Engine():
    def __init__(self, data, strategy, portfolio, metrics): # Constructs engine instance
        self.data = data
        self.strategy = strategy
        self.portfolio = portfolio
        self.metrics = metrics

    def run_backtest(self): # runs day by day using the given data and strategy

        prepped_data = self.strategy.prep_data(self.data) # creates necessary columns for particular strategy
        for i in range(len(prepped_data)): 
            uptodf = prepped_data.iloc[:i+1,:] # selects rows up to row+1, and all columns FIX OPTIMIZATION (dont need to send copy each day)
            
            # Signal uses yesterday's SMA values, then executes at today's open.
            signal = self.strategy.generate_signal(uptodf) # gets signal from stratgy
            price = prepped_data.iloc[i]["Open"] # get closing price of day for the portfolio
            self.portfolio.execute_trade(signal, price) # updates portfolio

