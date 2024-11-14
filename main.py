import os
import string
from polygon import RESTClient

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])


RSI_DAYS = 3
MACD_DAYS = 3
RSI_UPPER_BOUND = 70
RSI_LOWER_BOUND = 30


def findRSICandidates(list_of_tickers: list) -> list:
    rsi_candidates = []
    for ticker in list_of_tickers:
        if (findRSI(ticker.strip(), RSI_DAYS)):
            rsi_candidates.append(ticker)

    print("List of RSI Candidates: ")
    for rsi_candidate in rsi_candidates:
        print(rsi_candidate)
    return rsi_candidates


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


# Dont think we actually need this as its a trailing indicator and not a leading one 
# Might be able to use momentum though, so will keep here
def findMACD(ticker: string, number_of_days: int):
    # Get MACD data from API
    macd_data = client.get_macd(ticker=ticker, timespan='day', adjusted=True, short_window=12, long_window=26, signal_window=9, series_type='close', order='desc', limit=number_of_days)

    # Determine if the MACD is decelerating
    
    # Determine gap between current and next value
    print(macd_data)
    for result in macd_data.values:
        print(result.histogram)


# Get all of the tickers that Polygon supports
# Using CS for Common Stock.
def getListOfTickers() -> list:
    list_of_tickers = []
    try:
        for ticker in client.list_tickers(type='CS', market='stocks', limit=1000, sort='ticker'):
            list_of_tickers.append(ticker.ticker)
    except:
        print("Warning - List of tickers is too long")
    return list_of_tickers


def getListOfTickersFromFile() -> list:
        # Open and read the file
    with open('tickers.txt', 'r') as file:
        all_tickers = file.readlines()
    return all_tickers


def printListOfTickers(list_of_tickers: list):
    try:
        for ticker in list_of_tickers:
            print(ticker)
    except:
        print("Warning - List of tickers is too long")


# TODO
def isMACDDecelerating():
    print("read last X values of MACD and determine if slowing down")


def main():
    print("'ello gov'na")
    list_of_tickers = getListOfTickersFromFile()

    # Get a list of candidates based on RSI being too high or too low
    rsi_candidates = findRSICandidates(list_of_tickers)

    # From list of RSI candidates, get MACD and determine acceleration
    # Looking for decelerating MACD over several days
    print("===============================")




#Ensures main function is called when the script is executed
if __name__=="__main__":
    main()
