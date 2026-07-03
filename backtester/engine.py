# Runs the backtesting on the data using the given strategy.

class Engine():
    def __init__(self, data, strategy, portfolio): # Constructs engine instance
        self.data = data
        self.strategy = strategy
        self.portfolio = portfolio

    def run_backtest(self): # runs day by day using the given data and strategy
        for row in self.data:
            
            signal = self.strategy.generate_signal(row)

            self.portfolio.execute_trade(signal, price)
            # calculate necessary items.. rolling averages, days before, etc. 
            # execute given strategy daily by passing these items into the strategy
            # update as necessary

    def calculate