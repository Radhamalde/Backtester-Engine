# Backtesting Engine
## Author
Radha Malde, University of Michigan Student
## Description
A modular backtesting engine written in Python for evaluating algorithmic trading strategies on historical stock market data.

The engine simulates portfolio performance by executing trading signals generated from customizable strategies, while tracking performance metrics such as portfolio value, returns, trade statistics, and win rates.

The project is designed with an object-oriented architecture so new strategies can be added without modifying the core backtesting engine.

## Features
- Modular object-oriented design
- Historical price data loading
- Moving Average Crossover strategy
- Portfolio simulation with buy/sell execution
- Performance metrics including:
  - Initial capital
  - Final portfolio value
  - Total return
  - Average return per trade
  - Win rate
  - Maximum portfolio value

## Architecture and Project Structure
```text
Backtester/
    ├── backtester
    │   ├── __init__.py
    │   ├── broker.py
    │   ├── data.py
    │   ├── engine.py
    │   ├── metrics.py
    │   ├── plotting.py
    │   └── portfolio.py
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── strategies
        ├── __init__.py
        ├── base.py
        └── movingavg.py
```

The project is organized into independent components:

- Engine – runs the backtest day by day
- Strategy – generates buy/sell/hold signals according to its strategy
- Portfolio – executes trades and tracks holdings which get used in Metrics
- Metrics – calculates performance statistics
- Data – loads historical market data
- Main - pulls all components together by creating instances of strategy, portfolio, metrics, and data, and passes them into Engine.
         After the engine runs the backtest, main prints the updated metrics.
        
- The default configuration in main uses:
    - Ticker: SPY
    - Start: 2020-01-01, End: 2025-01-01
    - Moving Average Crossover strategy (Short SMA: 20, Long SMA: 50)
    - Initial Capital: $ 1000

## Installation
1. Clone the repository

    git clone git@github.com:Radhamalde/Backtester-Engine.git

2. Navigate to the project

    cd backtester

3. Install dependencies

    pip install -r requirements.txt

## Running
Run the project with

python main.py

Default Configuration:

- Ticker: SPY
- Start: 2020-01-01, End: 2025-01-01
- Moving Average Crossover strategy (Short SMA: 20, Long SMA: 50)
- Initial Capital: $ 1000

But these can be changed in main.

## Example Output
(For 'NVDA', '2023-01-01', '2025-12-01', initial cash: 1000)

```text
Initial Capital: $1,000.00
Total Orders/Transactions: 7
Total Completed Round-Trip Trades: 3
Final Portfolio Value: $4,612.43
Total Returns: 361.24%
Average Return: 120.41%
Win Rate: 91.00%
Highest Portfolio Value: $5,338.25
```

## Future Improvements
- Add command-line arguments for backtest configuration
- Transaction cost support
- Support for multiple assets
- Position sizing and risk management
- Sharpe ratio and additional risk metrics (Volatility, Drawdowns, etc.)
- Interactive performance visualization (plotting, etc.)
- New strategies to test
