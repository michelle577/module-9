# module-8
import pandas as pd
import yfinance as yf
import datetime
import time
import io
import requests
import itertools

download_url =  "https://finance.yahoo.com/quote/ELF/history?p=ELF"
#r = requests.request(url=download_url)
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2021,3,7)

def DownloadStockData(start,end):
    # create empty dataframe
    stockData = pd.DataFrame()
    Symbols = ["ELF","AAPL","IBM","JJ","GOOGL","TSLA","TWX","DIS"]
    # iterate over each symbol
    for i in Symbols:
        # print the symbol which is being downloaded
        print(str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)
        try:
            # download the stock price
            stock = []
            stock = yf.download(i, start=start, end=end, progress=False)
            # append the individual stock prices
            if len(stock) == 0:
                None
            else:
                stock['Name'] = i
                stockData = stockData.append(stock, sort=False)
        except Exception:
            None
    return stockData
#Download stock data from start to end date
stockData = DownloadStockData(start,end)


OneThroughTen = [1,2,3,4,5,6,7,8,9,10]
i = 0
iterator = itertools.cycle(OneThroughTen)
for n in iterator:
    print(stockData.iloc[n, :]) #Prints the nth line of stock data
    i=i+1
    if i == 10:
        i = 0
        break

print("NEXT ITERATOR","\n")
Sentence = "I am repeating myself"
for n in itertools.repeat(Sentence):
    print(n)
    i=i+1
    if i == 10:
        i = 0
        break

#Infinite sequence. Show every other row of stock data starting from row 50
for n in itertools.count(50,2):
    print(stockData.iloc[n, :])
    i=i+1
    if i == 30: #Break the loop after 30 iterations
        i = 0
        break


#Function that checks if i is greater than 10. Returns either true or false
def iIsGreaterThan10equalsTrue(i):
    TrueOrFalse = int(i) > 10
    return TrueOrFalse
#Iterate until i > 10
for n in itertools.dropwhile(iIsGreaterThan10equalsTrue,OneThroughTen):
    print(stockData.iloc[n,:])
    i=i+1


print("e")



import unittest
class TestStringMethods(unittest.TestCase):
    #This test will test to see if the start date is correctly a datetime object
    def test_dateTime(self):
        print("FIRST TEST")
        #Test to see that the datetime library dependency works the same as before
        import datetime as dt
        end = datetime.datetime(2021, 3, 7)
        #print(type(end))
        self.assertTrue(isinstance(end,datetime.datetime))

    def test_downloadFunction(self):
        print("SECOND TEST")
        #Code to make sure works properly
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime(2021, 3, 7)
        stockData = DownloadStockData(start,end)
        #Test to see if the data is populated
        self.assertTrue(len(stockData)>0)
        # Test to see if the data object is correctly a dataframe
        self.assertTrue(isinstance(stockData, pd.core.frame.DataFrame))
        print("Success")


#RUN THE TEST
if __name__ == '__main__':
    unittest.main()
