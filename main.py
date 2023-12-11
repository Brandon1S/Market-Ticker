import os
from polygon import RESTClient

client = RESTClient(api_key=os.environ['POLYGON_API_CLIENT'])

# TODO 
# 1. get a list of tickers. 
#       auto generated based on criteria
#       put that shit into a separate text file
#       OR scan all tickers every time to catch any new ones that come up
#       or ones that fall off

# 2. read through list of tickers in a for loop
#       get all end-of-day data over the course of the last year with daily candles
#


def main():
    print("'ello gov'na")


if __name__=="__main__":
    main()