# To execute the entire backtesting process, using the components inside backtester/.
from backtester.engine import Engine
from backtester.metrics import Metrics
# from backtester.broker import Broker
from backtester.portfolio import Portfolio
from backtester.data import load_data
# from backtester.plotting import Plotting
from strategies.movingavg import MovingAvg

def main():
    # load data
    data = load_data('AAPL', '2020-01-01', '2023-01-01') 
    print(data.head())
    print(data.columns)

    # construct portfolio
    portfolio = Portfolio(initial_cash=100000)

    # construct strategy (also get necessary data columns)
    strategy = MovingAvg(short_window = 20, long_window = 50)

    # construct metrics instance
    metrics = Metrics(initial_capital=portfolio.cash) # sets initial_capital to portfolio cash before running
    # create and run engine
    engine = Engine(data, strategy, portfolio)
    engine.run_backtest()

    # calculate metrics
    # metrics.calculate_metrics()

if __name__ == "__main__":
    main()