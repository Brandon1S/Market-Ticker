import os
import string
from polygon import RESTClient

import indicators
import tickersfile

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])

SMA_DAYS_SHORT = 7
SMA_DAYS_LONG = 30


def main():
    print("'ello gov'na")

    list_of_tickers = tickersfile.getListOfTickersFromFile()

    # Get a list of candidates based on RSI being too high or too low
    # rsi_candidates = findRSICandidates(list_of_tickers)

    golden_cross, dead_cross = indicators.getSMA(list_of_tickers=list_of_tickers,
                                    client=client, 
                                    number_of_days_short=SMA_DAYS_SHORT, 
                                    number_of_days_long=SMA_DAYS_LONG)

    # From list of RSI candidates, get MACD and determine acceleration
    # Looking for decelerating MACD over several days
    print("===============================")


#Ensures main function is called when the script is executed
if __name__=="__main__":
    main()
