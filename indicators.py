import string
from polygon import RESTClient

RSI_DAYS = 3
MACD_DAYS = 3
RSI_UPPER_BOUND = 70
RSI_LOWER_BOUND = 30

GOLDEN_CROSS: int = 1
DEAD_CROSS: int = -1
NO_CROSS: int = 0

SMA_DAYS_SHORT = 7
SMA_DAYS_LONG = 30

def findRSICandidates(list_of_tickers: list, client: RESTClient) -> list:
    rsi_candidates = []
    for ticker in list_of_tickers:
        if (findRSI(ticker.strip(), client, RSI_DAYS)):
            rsi_candidates.append(ticker)

    print("List of RSI Candidates: ")
    for rsi_candidate in rsi_candidates:
        print(rsi_candidate)
    return rsi_candidates


def findRSI(ticker: string, client: RESTClient, number_of_days: int):
    print("Finding RSI")
    rsi_out_of_bounds = True

    rsi_data = client.get_rsi(ticker=ticker, timespan='day', adjusted=True, window=14, series_type='close', order='desc', limit=number_of_days)
    
    # Determine if RSI is out-of-bounds. AKA very overbought/oversold
    for result in rsi_data.values:
        print(result.value)
        if result.value < RSI_UPPER_BOUND and result.value > RSI_LOWER_BOUND:
            rsi_out_of_bounds = False
            break
    return rsi_out_of_bounds

# Dont think we actually need this as its a trailing indicator and not a leading one 
# Might be able to use momentum though, so will keep here
def findMACD(ticker: string, client: RESTClient, number_of_days: int):
    # Get MACD data from API
    macd_data = client.get_macd(ticker=ticker, timespan='day', adjusted=True, short_window=12, long_window=26, signal_window=9, series_type='close', order='desc', limit=number_of_days)

    # Determine if the MACD is decelerating
    
    # Determine gap between current and next value
    print(macd_data)
    for result in macd_data.values:
        print(result.histogram)



# SMA Data needs to fit the following format:
    #0: Short SMA previous day 
    #1: Short SMA current day   
    #2: Long SMA previous day
    #3: Long SMA current day
def getSMACrossOver(sma_data: list) -> int:
    if sma_data[0] < sma_data[2] and sma_data[1] > sma_data[3]:
        return GOLDEN_CROSS
    elif sma_data[0] > sma_data[2] and sma_data[1] < sma_data[3]:
        return DEAD_CROSS
    return NO_CROSS


def getSMA(list_of_tickers: list, client: RESTClient, number_of_days_short: int, number_of_days_long: int) -> tuple[list, list]:
    golden_cross = []
    dead_cross = []
    for ticker in list_of_tickers:
        # Get short and long SMA data, and format it into a list. Then, determine if the SMA has crossed over
        sma_data_short = client.get_sma(ticker=ticker.strip(), timespan='day', adjusted=True, window=number_of_days_short, series_type='close', order='desc', limit=2)
        sma_data_long = client.get_sma(ticker=ticker.strip(), timespan='day', adjusted=True, window=number_of_days_long, series_type='close', order='desc', limit=2)
        sma_data = [sma_data_short.values[0].value, sma_data_short.values[1].value, sma_data_long.values[0].value, sma_data_long.values[1].value]
        
        cross_type = getSMACrossOver(sma_data)
        if cross_type == GOLDEN_CROSS:
            golden_cross.append(ticker)
        elif cross_type == DEAD_CROSS:
            dead_cross.append(ticker)

    return golden_cross, dead_cross


# TODO
def isMACDDecelerating():
    print("read last X values of MACD and determine if slowing down")