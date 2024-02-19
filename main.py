import os
import string
from polygon import RESTClient

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])


RSI_DAYS = 3
MACD_DAYS = 3
RSI_UPPER_BOUND = 35
RSI_LOWER_BOUND = 25

# TODO 
# 1. get a list of tickers. 
#       auto generated based on criteria
#       put that shit into a separate text file
#       OR scan all tickers every time to catch any new ones that come up
#       or ones that fall off

# 2. read through list of tickers in a for loop
#       get all end-of-day data over the course of the last year with daily candles
#

def findRSI(ticker: string, number_of_days: int):
    print("Finding RSI")
    rsi_out_of_bounds = True

    rsi_data = client.get_rsi(ticker=ticker, timespan='day', adjusted=True, window=14, series_type='close', order='desc', limit=number_of_days)
    
    # Determine if RSI is out-of-bounds. AKA very overbought/oversold
    for result in rsi_data.values:
        print(result.value)
        if result.value < RSI_UPPER_BOUND and result.value > RSI_LOWER_BOUND:
            rsi_out_of_bounds = False
            continue
    return rsi_out_of_bounds

def findMACD(ticker: string, number_of_days: int):
    # Get MACD data from API
    macd_data = client.get_macd(ticker=ticker, timespan='day', adjusted=True, short_window=12, long_window=26, signal_window=9, series_type='close', order='desc', limit=number_of_days)

    # Determine if the MACD is decelerating
    
    # Determine gap between current and next value
    print(macd_data)
    for result in macd_data.values:
        print(result.histogram)
        


def isMACDDecelerating():
    print("read last X values of MACD and determine if slowing down")

def main():
    print("'ello gov'na")
    
    # Open and read the file
    with open('tickers.txt', 'r') as file:
        all_tickers = file.readlines()

    # Get a list of candidates based on RSI being too high or too low
    rsi_candidates = []
    for ticker in all_tickers:
        if (findRSI(ticker.strip(), RSI_DAYS)):
            rsi_candidates.append(ticker)
    
    print("List of RSI Candidates: ")
    for rsi_candidate in rsi_candidates:
        print(rsi_candidate)
        findMACD(rsi_candidate.strip(), MACD_DAYS)
    print("===============================")

    # From list of RSI candidates, get MACD and determine acceleration
    # Looking for decelerating MACD over several days


#Ensures main function is called when the script is executed
if __name__=="__main__":
    main()
