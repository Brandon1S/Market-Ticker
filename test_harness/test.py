import os
import sys
from datetime import datetime
from polygon import RESTClient

import tickersfile
from datetime import timedelta

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])
YESTERDAY = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
TWO_YEARS_AGO = (datetime.today().replace(year=datetime.today().year - 2) + timedelta(1)).strftime('%Y-%m-%d')

def get_closing_price(ticker, date):
    try:
        response = client.get_aggs(ticker, 1, "day", date, date)

        if len(response) > 0:
            return response[0].close
        else:
            return None
    except Exception as e:
        print(f"Error fetching closing price for {ticker} on {date}: {e}")
        return None

def main():
    today = datetime.today().strftime('%Y-%m-%d')

    # Get list of tickers
    tickers = tickersfile.getListOfTickersFromFile()

    # For each ticker, get historical SMA data, determine if there is a cross
    for ticker in tickers:
        ticker_symbol = ticker.strip()
        # print ticker name
        print(f"Checking {ticker_symbol}")
        closing_price_two_years_ago = get_closing_price(ticker_symbol, TWO_YEARS_AGO)
        closing_price_today = get_closing_price(ticker_symbol, YESTERDAY)

        print(f"Closing price for {ticker_symbol} on {TWO_YEARS_AGO}: {closing_price_two_years_ago}")
        print(f"Closing price for {ticker_symbol} on {today}: {closing_price_today}")
    pass

if __name__ == "__main__":
    main()