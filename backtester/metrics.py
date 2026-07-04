# Tracks the strategy's performance metrics during backtesting

class Metrics():
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def get_initial_capital(self): 
        return self.portfolio.initial_cash 

    def get_total_trades(self): # count during engine run in portfolio
        return self.portfolio.total_orders // 2 # each round trip trade has 2 orders
    
    def get_total_orders(self): # count during engine run
        return self.portfolio.total_orders

    def get_final_portfolio_value(self): # cash + (shares*priceofsharesatclose(last day))
        return self.portfolio.current_pf_value

    def get_total_returns(self): 
        return (self.get_final_portfolio_value() - self.get_initial_capital()) / self.get_initial_capital() * 100
    
    def get_avg_return(self): # totalreturn/totaltrades
        return self.get_total_returns() / self.get_total_trades() if self.get_total_trades() > 0 else 0

    def get_win_rate(self): # 100* profitable trades/total trades !!! STILL NEED TO IMPLEMENT - not correct bc profitable trades is wrong
        return self.portfolio.profitable_trades / self.get_total_trades() if self.get_total_trades() > 0 else 0
    
    def get_max_pv(self): # max portfolio value (use for max drawdown)
        return self.portfolio.max_pf_value
    
    # TO ADD: avg winning trade, avg losing trade
    # Initial capital
    # Total trades
    # Final Portfolio Value
    # Total Return
    # Avg Return
    # Win rate (% profitable trades -- 100* profitable trades/total trades)

    # Later: Max Drawdown, Sharpe Ratio (return/unit risk)