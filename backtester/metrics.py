# Tracks the strategy's performance metrics during backtesting

class Metrics():
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital

    def print_all_metrics(self, trades, total_returns, profitable_trades, max_pv): 
        print("Initial Capital: " self.initial_capital " $")
        print("Total Trades: " get_total_trades())
        print("Final Portfolio Value: " get_final_portfolio_value())
        print("Total Returns: " get_total_returns() " %")
        print("Average Return: " get_avg_return() " %")
        print("Win Rate: " get_win_rate() " %")
        print("Highest Portfolio Value: " get_max_pv())



    # def get_initial_capital(): # get before engine run 
    #   return .. dont need fcn for this

    def get_total_trades(): # count during engine run

    def get_final_portfolio_value(): # cash + (shares*priceofsharesatclose(last day))

    def get_total_returns(): 

    def get_avg_return(): # totalreturn/totaltrades

    def get_win_rate(): # 100* profitable trades/total trades

    def get_max_pv(): # max portfolio value (use for max drawdown)

    

    # Initial capital
    # Total trades
    # Final Portfolio Value
    # Total Return
    # Avg Return
    # Win rate (% profitable trades -- 100* profitable trades/total trades)

    # Later: Max Drawdown, Sharpe Ratio (return/unit risk)