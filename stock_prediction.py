# enabling requests,json,time
import requests
import json
import time

# creating the mean reversion function
def meanReversionStrategy(prices):
    # defining variables in order to keep track
    i = 0
    buy = 0
    short = 0
    total_profit = 0
    # creating loop to go through prices
    for price in prices:
        if i >= 5:
            # creating moving average variable
            moving_average = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) / 5
            # buys if threshold is met
            if price < moving_average * 0.95 and buy == 0:
                print("buying at: ", price)
                buy = price
                # if statement that tests a buy signal today
                if i == len(prices) - 1:
                    print("Buying Today")
                    # if statement with shorting technique
                if short != 0 and buy != 0:
                    total_profit += short - buy
                    print("trade profit", short - buy)
                    print("total profit: ", total_profit)
                short = 0
            # elif that sells if things are met
            elif price > moving_average * 1.05 and buy != 0:
                print("selling at: ", price)
                print("trade profit: ", price - buy)
                total_profit += price - buy
                buy = 0
                # sell today
                if i == len(prices) - 1:
                    print("Selling Today")
        # keep track within the loop
        i += 1
    # defining final percentage
    final_percentage = (total_profit / prices[0]) * 100
    # print statements to show output
    print("total profit: ", total_profit)
    print("final percentage: ", final_percentage, "%")
    print("-----------------------")
    # statement that returns certain variables when called on
    return total_profit, final_percentage


# creating simple moving average strategy function
def simpleMovingAverageStrategy(prices):
    # defining variables in order to keep track
    i = 0
    buy = 0
    short = 0
    total_profit = 0
    # creating loop to go through prices
    for price in prices:
        if i >= 5:
            # creating moving average variable
            moving_average = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) / 5
            # buys if threshold is met
            if price > moving_average and buy == 0:
                print("buying at: ", price)
                buy = price
                # if statement that tests a buy signal today
                if i == len(prices) - 1:
                    print("Buying Today")
                # shorting technique
                if short != 0 and buy != 0:
                    total_profit += short - buy
                    print("trade profit", short - buy)
                    print("total profit: ", total_profit)
                short = 0
            # elif that sells if threshold is met
            elif price < moving_average and buy != 0:
                print("selling at: ", price)
                print("trade profit: ", price - buy)
                total_profit += price - buy
                buy = 0
                # sell today
                if i == len(prices) - 1:
                    print("Selling Today")
        # keeps track
        i += 1
    # define final percentage
    final_percentage = (total_profit / prices[0]) * 100
    # print output
    print("total profit: ", total_profit)
    print("final percentage: ", final_percentage, "%")
    print("------------------------")
    # statement that returns certain variables when called on
    return total_profit, final_percentage


# create the Bollinger Band strategy
def bollingerstrat(prices):
    # define variables
    i = 0
    buy = 0
    short = 0
    total_profit = 0
    # loop through prices
    for price in prices:
        if i >= 5:
            # define moving average
            moving_average = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) / 5
            # buys
            if price > moving_average * 0.95 and buy == 0:
                print("buying at: ", price)
                buy = price
                # buy today
                if i == len(prices) - 1:
                    print("Buying Today")
                # shorting technique
                if short != 0 and buy != 0:
                    total_profit += short - buy
                    print("trade profit", short - buy)
                    print("total profit: ", total_profit)
                short = 0
            # sells
            elif price < moving_average * 1.05 and buy != 0:
                print("selling at: ", price)
                print("trade profit: ", price - buy)
                total_profit += price - buy
                buy = 0
                # sell today
                if i == len(prices) - 1:
                    print("Selling Today")
        # keeps track
        i += 1
    # define final percentage
    final_percentage = (total_profit / prices[0]) * 100
    # print output
    print("total profit: ", total_profit)
    print("final percentage: ", final_percentage, "%")
    print("------------------------")
    # statement that returns certain variables when called on
    return total_profit, final_percentage


# create saveResults function
def saveResults(prices):
    # saves results to a json in my folder
    json.dump(results, open("results.json", "w"), indent=4)


# create append_data function
def append_data():
    # list of tickers to pull
    tickers = ['AAPL', 'WFC', 'TSLA', 'ADBE', 'AMZN', 'BAC', 'COKE', 'GOOG', 'INTC', 'NVDA']
    # loop through tickers
    for ticker in tickers:
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
        # print(url)
        req = requests.get(url)

        time.sleep(12)

        req_dct = json.loads(req.text)

        # defining keys to know what to pull from alphavantage
        key_series = "Time Series (Daily)"
        key_open = '1. open'
        key_hi = '2. high'
        key_lo = '3. low'
        key_close = '4. close'

        # defining last_date
        last_date = open("data/" + ticker + ".csv").readlines()[-1].split(",")[0]

        prices = []

        # loop through dates
        for date in req_dct[key_series]:
            row = []
            row.append(date)
            row.append(req_dct[key_series][date][key_open])
            row.append(req_dct[key_series][date][key_hi])
            row.append(req_dct[key_series][date][key_lo])
            row.append(req_dct[key_series][date][key_close])
            # append if the date isn't in the csv
            if date > last_date:
                prices.append(row)

            # prices.append(row)
        # oldest to newest prices
        prices.reverse()

        # access to append csv
        csv_file = open("data/" + ticker + ".csv", "a")

        # loop through row
        for row in prices:
            csv_file.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "\n")

    # close file once appended
    csv_file.close()


# calling append_data function
append_data()

# defining variables and creating list of tickers
best_return = 0
best_stock = ""
best_strat = ""
tickers = ['AAPL', 'WFC', 'TSLA', 'ADBE', 'AMZN', 'BAC', 'COKE', 'GOOG', 'INTC', 'NVDA']

# creating results dictionary
results = {}

# loop through tickers
for ticker in tickers:
    prices = [float(line.split(",")[4]) for line in
              open("data/" + ticker + ".csv").readlines()[1:]]

    # calling strategies
    mr_returns = meanReversionStrategy(prices)
    sma_returns = simpleMovingAverageStrategy(prices)
    bol_returns = bollingerstrat(prices)

    # defining sma_returns, mr_returns, bol_returns and creating if statements to see best performance
    results[ticker + "_sma_returns"] = sma_returns
    if sma_returns[1] > best_return:
        best_return = sma_returns[1]
        best_stock = ticker
        best_strat = "Simple Moving Average"
    results[ticker + "_mr_returns"] = mr_returns
    if mr_returns[1] > best_return:
        best_return = mr_returns[1]
        best_stock = ticker
        best_strat = "Mean Reversion"
    results[ticker + "_bol_returns"] = bol_returns
    if bol_returns[1] > best_return:
        best_return = bol_returns[1]
        best_stock = ticker
        best_strat = "Bollinger Strategy"

# print statements to tell me which stock did best and what strategy did best
print("Best Performing Stock: ", best_stock + ": " + (str(best_return)))
print("Best Strategy: ", best_strat)

# calling saveResults function
saveResults(prices)
