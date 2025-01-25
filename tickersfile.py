from polygon import RESTClient


def getListOfTickersFromFile() -> list:
        # Open and read the file
    with open('tickers.txt', 'r') as file:
        all_tickers = file.readlines()
    return all_tickers


# Get all of the tickers that Polygon supports
# Using CS for Common Stock.
def getListOfTickers(client: RESTClient) -> list:
    list_of_tickers = []
    try:
        for ticker in client.list_tickers(type='CS', market='stocks', limit=1000, sort='ticker'):
            list_of_tickers.append(ticker.ticker)
    except Exception as e:
        print(f"Warning - Error fetching tickers: {e}")
    return list_of_tickers


def printListOfTickers(list_of_tickers: list):
    try:
        for ticker in list_of_tickers:
            print(ticker)
    except:
        print("Warning - List of tickers is too long: {e}")