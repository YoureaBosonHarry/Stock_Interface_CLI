import argparse
import json
import os
import requests


class Price_Interface():
    def __init__(self, ticker, key):
        self.main_url = "https://www.alphavantage.co"
        self.ticker = ticker
        self.api_key = key

    def recent_json(self):
        url = os.path.join(self.main_url,
                           f"query?function=TIME_SERIES_INTRADAY&symbol={self.ticker}&interval=5min&apikey={self.api_key}")
        r = requests.get(url)
        return r.json()

    def last_price(self):
        r = self.recent_json()
        times = [key for key in r["Time Series (5min)"].keys()]
        print(times[0])
        for i, j in r["Time Series (5min)"][times[0]].items():
            print(f"{i}: {j}")

def create_api_file():
    api_key = input("Please Enter API Key: ")
    k = {"key": str(api_key.upper().strip())}
    with open(os.path.join(os.getcwd(), "api_key.json"), 'w+') as f:
        json.dump(k, f, indent=4)
    return k

def main():
    try:
        with open(os.path.join(os.getcwd(), "api_key.json"), 'r') as f:
            k = json.load(f)
    except FileNotFoundError:
        k = create_api_file()
    t = input("Input Stock Ticker: ")
    ui = Price_Interface(t, k["key"])
    ui.last_price()

if __name__ =="__main__":
    main()


