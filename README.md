# stock-investment-analyzer

Analyze stocks vs bank interest with risk. assessment
A python tool that analyzes stocks over 10 years and compares returns against bank interest rates. Helps investor to make a decision by calculating returns, tracking dividends and assessing risk through volatility analysis.

# Features

- compare multiple stocks 
- 10 years historical analysis
- Dividend tracking and calculations
- Volatility-based risk assessment (Low/Medium/High)
- Visual price comparison charts
- Investment recommendations vs 3% bank interest

# Technologies used

- Python 3.13.5
I Used this libraries:
- yfinance - Real-time stock market data
- pandas- Data manipulation and analysis
- matplotlib - Data visualization and charting

# How to use 

1.Install required libraries:
pip install yfinance matplotlib pandas

2.Run the program:
python stock_analyzer.py

3.Enter stock symbols when prompted (e.g., O, AAPL, IBM)

4.Enter you investment amount

5.View results:
- Investment analysis for each stock
- Risk assessment
- Comparison chart
- Investment recommendation

# Example Output
=== INVESTMENT COMPARISON FOR 10 YEARS ===
Initial Investment: $1000

Stock (AAPL)
  Stock value: $9275.43
  Dividend earnings: $380.13
  Total return: $9655.56

Bank (3% interest):
  Total: $1343.92

Difference: $8311.64
  Volatility: 2.15%
  Risk Level: Medium Risk

✅ RECOMMENDATION: Invest in AAPL!



## Future Improvements
- Add more risk metrics
- Export results to PDF
- Add news sentiment analysis
- Web interface with Flask

**Author:** Paul Tzanis
**Contact:** [paulvtzanis@gmail.com]
