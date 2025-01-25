import os
from datetime import datetime
from polygon import RESTClient

import tickersfile

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])
TWO_YEARS_AGO = (datetime.today().replace(year=datetime.today().year - 2)).strftime('%Y-%m-%d')

def main():
    today = datetime.today().strftime('%Y-%m-%d')

    # Get list of tickers
    tickers = tickersfile.getListOfTickers()

    # For each ticker, get historical SMA data, determine if there is a cross
    pass

if __name__ == "__main__":
    main()