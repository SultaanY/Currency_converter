import yfinance as yf 
import datetime
import argparse
import sys

def get_market_price(base, quote, amount):
    symbol = base+quote+"=X"
    today_date = datetime.date.today()
    print(f"Getting price for symbol: {symbol} for date: {today_date}")
    data = yf.download(symbol, start=today_date, end=today_date)
    print(data)
    if len(data) == 0:
        print("Dataframe empty. Could not get data. Exiting..")
        sys.exit(1)
    price = data.loc[str(today_date)]['Close']
    print(f"Price: {price}")
    print(f"Amount In: {amount}, Amount Out: {amount*price}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gets market data.')
    parser.add_argument('--base', type=str, help='Base currency for pair')
    parser.add_argument('--quote', type=str, help='Quote currency for pair')
    parser.add_argument('--amount', type=float, help='Amount to swap')
    args = parser.parse_args()
    if args.base is None:
        print("Error you did not give a --base option. Exiting...")
        sys.exit(1)
    if args.quote is None:
        print("Error you did not give a --quote option. Exiting...")
        sys.exit(1)
    if args.amount is None:
        print("Error you did not give a --amount option. Exiting...")
        sys.exit(1)

    get_market_price(args.base, args.quote, args.amount)