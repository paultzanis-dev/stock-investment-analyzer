import yfinance as yf
import matplotlib.pyplot as plt

symbol = input("Enter stock symbols (separated by commas):")
symbol_list = symbol.split(',')
symbol_list = [s.strip() for s in symbol_list]
investment = float(input("Enter investment amount: $"))

def get_stock(symbol):
    try:
         stock = yf.Ticker(symbol)
         hist = stock.history(period = "10y")
         if hist.empty or len(hist) < 10:
            print("Error: Not enough data.")
            return None, None
         return stock, hist

    except Exception as e:
         print(f"Error occurred: {e}")
         return None, None

results =[]

for sym in symbol_list:
    stock , hist = get_stock(sym)
    if stock is None:
     continue

    first_price = hist['Close'].iloc[0]
    last_price = hist['Close'].iloc[-1]
    percentage_change = ((last_price - first_price)/first_price*100)
    total_dividends = hist['Dividends'].sum()
    stock_value = investment*(1 + percentage_change/100)
    shares = investment/first_price
    dividend_earnings = shares * total_dividends
    total_stock_return = stock_value + dividend_earnings
    bank_value = investment*(1.03 ** 10)
    daily_returns = hist['Close'].pct_change()
    volatility = daily_returns.std()*100
    if volatility < 1.5:
        risk_level = "Low Risk"
    elif volatility < 3.5:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    result = {
        'symbol':sym,
        'total_return':total_stock_return,
        'bank_return':bank_value,
        'hist':hist
    }
    results.append(result)
    print(f"\n=== INVESTMENT COMPARISON FOR 10 YEARS ===")
    print(f"Initial Investment: ${investment}")
    print(f"\nStock ({sym})")
    print(f"  Stock value: ${stock_value:.2f}")
    print(f"  Dividend earnings: ${dividend_earnings:.2f}")
    print(f" Total return ${total_stock_return:.2f}")
    print(f"\nBank (3% interest):")
    print(f"  Total: ${bank_value:.2f}")
    print(f"\nDifference: ${total_stock_return - bank_value:.2f}")
    print(f"  Volatility: {volatility:.2f}%")
    print(f"  Risk Level: {risk_level}")

    if total_stock_return > bank_value:
        print(f"\n✅ RECOMMENDATION: Invest in {sym}!")
    else:
        print(f"\n❌ RECOMMENDATION: Keep money in bank")

plt.figure(figsize=(12,6))
for result in results:
    plt.plot(result['hist'].index, result['hist']['Close'], label=result['symbol'].upper() )

plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('10-Year Price Comparison')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()