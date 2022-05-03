import yfinance as yf
import pandas as pd
import time


def downloadTimeTickers(start,end):
    return end-start  

def GetTickers(listTickers,pickleFileName):
    # Set the start and end date
    start_date = '2012-04-01'
    end_date = '2022-04-01'

    #42 STOCKS lets time this as it is slow
    a = time.perf_counter()

    tickerStrings = listTickers
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, start_date, end_date, group_by="Ticker")
        data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)

    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)

    b = time.perf_counter()  # A few seconds later
    #compute time 
    downloadTimeTickers(a,b)
    # save to pickle
    df.to_pickle('%s.pkl' % pickleFileName)
    df.to_csv('%s.csv' % pickleFileName)

#GetTickers(['F','GM','TSLA','BA'],'motorAndAero')
GetTickers( ['AAPL','MSFT','NVDA','AMD','GOOG','WFG','HD','CAT','NEM','NFLX','DIS','BMY','MS','JPM','GS','V','DPZ','SBUX','COST','KR','TGT','PG'], 'portfolio')
#