# Runs the backtesting on the data using the given strategy.

class Engine():
    def __init__(self, data, strategy, portfolio): # Constructs engine instance
        self.data = data
        self.strategy = strategy
        self.portfolio = portfolio

    def run_backtest(self): # runs day by day using the given data and strategy
        prepped_data = self.strategy.prep_data(self.data) # creates necessary columns for particular strategy
        for i in range(len(prepped_data)): # change to correct syntax
            uptodf = prepped_data.iloc[:i+1, :] # selects rows up to row+1, and all columns
            
            signal = self.strategy.generate_signal(uptodf) # gets signal from stratgy
            price = prepped_data.iloc[i]["Close"] # get closing price of day for the portfolio
            self.portfolio.execute_trade(signal, price) # updates portfolio
            # calculate necessary items.. rolling averages, days before, etc. 
            # execute given strategy daily by passing these items into the strategy
            # update as necessary
        # call metrics w parameters caluclated during run.
   # def calculate_items(self, ): for metrics -- finish later
