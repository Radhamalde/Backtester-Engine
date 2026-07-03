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
    data = load_data('NVDA', '2023-01-01', '2025-12-01') 
    print(data.head())
    print(data.columns)

    # construct portfolio
    portfolio = Portfolio(initial_cash=1000)

    # construct strategy (also get necessary data columns)
    strategy = MovingAvg(short_window = 20, long_window = 50)

    # construct metrics instance
    metrics = Metrics(portfolio) # sets initial_capital to portfolio cash before running
    # create and run engine

    print(f"Initial Capital: ${metrics.get_initial_capital():,.2f}")
    engine = Engine(data, strategy, portfolio, metrics)
    engine.run_backtest()

    print(f"Total Orders/Transactions: {metrics.get_total_orders()}")
    print(f"Total Completed Round-Trip Trades: {metrics.get_total_trades()}")
    print(f"Final Portfolio Value: ${metrics.get_final_portfolio_value():,.2f}")
    print(f"Total Returns: {metrics.get_total_returns():.2f}%")
    print(f"Average Return: {metrics.get_avg_return():.2f}%")
    print(f"Win Rate: {metrics.get_win_rate():.2f}%")
    print(f"Highest Portfolio Value: ${metrics.get_max_pv():,.2f}")

    # calculate metrics
    # metrics.calculate_metrics()

if __name__ == "__main__":
    main()