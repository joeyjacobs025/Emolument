Stock Scoring & Ranking System (High School Project)

Overview
  This Python project analyzes and ranks approximately 500 U.S. stocks based on historical price trends, trading volume, sector-adjusted P/E ratios, and market beta. 
  The system assigns scores to each stock to identify top candidates for potential investment, demonstrating early applied data science and financial modeling skills.

Features
  Historical Price Analysis: Examines the past 30 days of stock data (open, close, high, low, and volume) to evaluate short-term performance trends.
  Custom Scoring System: Calculates a score for each stock based on price changes, sector-relative P/E ratios, and 52-week range percentiles.
  Beta Calculation: Measures stock volatility relative to the SPY ETF using linear regression to inform scoring adjustments.
  Stock Ranking: Aggregates all scores to produce a ranked list of top-performing stocks.

Applied Data Science Tools: Uses pandas, numpy, statsmodels, and yfinance for data retrieval, manipulation, and analysis.

Technologies
  Python
  pandas
  numpy
  yfinance
  statsmodels
  matplotlib

Example Output
  The top 5 stocks based on aggregate scoring:
  {'AAPL': 52, 'MSFT': 49, 'GOOG': 47, 'AMZN': 45, 'NVDA': 44}

Note: Example results are illustrative and based on 30-day historical data.

Learning Outcomes  
  Gained practical experience with financial data retrieval and analysis in Python.
  Developed a custom scoring system integrating multiple stock metrics.
  Applied linear regression for market beta calculation and volatility assessment.
  Practiced algorithmic thinking and project structuring for data-driven decision-making.

Notes
  Original high school project; code is functional but intended for educational purposes.
  Demonstrates early interest in data science, financial analysis, and applied quantitative modeling.
