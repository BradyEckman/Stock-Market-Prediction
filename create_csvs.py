import json
import time
import requests
'''
This is the code to create the CSV
'''

tickers = ['AAPL','WFC','TSLA','ADBE','AMZN','BAC','COKE','GOOG','INTC','NVDA']
for ticker in tickers:
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    req = requests.get(url)

    time.sleep(12)

    req_dct = json.loads(req.text)

    key_series = "Time Series (Daily)"
    key_open = '1. open'
    key_hi = '2. high'
    key_lo = '3. low'
    key_close = '4. close'

    prices = []
    for date in req_dct[key_series]:
    #     print(date, req_dct[key_series][date][key_open], \
    #     req_dct[key_series][date][key_hi], \
    #     req_dct[key_series][date][key_lo], \
    #     req_dct[key_series][date][key_close])

        row = []
        row.append(date)
        row.append(req_dct[key_series][date][key_open])
        row.append(req_dct[key_series][date][key_hi])
        row.append(req_dct[key_series][date][key_lo])
        row.append(req_dct[key_series][date][key_close])

        prices.append(row)

    prices.reverse()

    print(prices)

    csv_file = open("data/" + ticker + ".csv", "w")
    csv_file.write("date" + "," + "open" + "," + "high" + "," + "low" + "," + "close" + "\n")

    for row in prices:
        csv_file.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "\n")

csv_file.close()



