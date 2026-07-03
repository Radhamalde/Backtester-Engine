# Runs the backtesting on the data using the given strategy.


def run_backtest(data, strategy): # runs day by day using the given data and strategy
    for date in data:
        # calculate necessary items.. rolling averages, days before, etc. 
        # execute given strategy daily by passing these items into the strategy
        # update as necessary

def calculate