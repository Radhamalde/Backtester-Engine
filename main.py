# To execute the entire backtesting process, using the components inside backtester/.
import backtester.engine as engine
import backtester.metrics as metrics
import backtester.broker as broker
import backtester.portfolio as portfolio
import backtester.data as data
import backtester.plotting as plotting
import strategies.movingavg as strategy

def main():
    # load data
    data = data.load_data('AAPL', '2020-01-01', '2023-01-01') 

    # run engine
    engine.run_backtest(data, strategy)

    # calculate metrics
    metrics.calculate_metrics()