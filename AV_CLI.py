#!/usr/bin/env python3
import argparse
import datetime
import json
import os
from Portfolio import Portfolio
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

def load_api_key():
    if os.path.isfile("api_key.json"):
        with open(os.path.join(os.getcwd(), "api_key.json"), 'r') as f:
            k = json.load(f)
    else:
        k = create_api_file()
    return k


def help_function():
    m = f"\u2022 Enter \"load\" to access portfolio"\
        f"\n\u2022 Enter \"exit\" to quit the program"
    return m

def load_interface(portfolio):
    acceptable_inputs = ["buy", "deposit", "search","sell", "exit"]
    portfolio_option = input(" Portfolio >>> ")
    if portfolio_option.strip() in acceptable_inputs:
        if portfolio_option.strip() == "buy":
            ticker = input(" Portfolio >>> Input Stock Ticker: ")
            price = input(" Portfolio >>> Input Buying Price: ")
            number_of_shares = input(" Portfolio >>> Input Number of Shares: ")
            confirm = input(f" Portfolio >>> Confirm {int(number_of_shares)} shares of"\
                            f" {ticker.upper()} at {round(float(price), 4)} Y|n: ")
            if confirm == "Y":
                portfolio.buy_action(ticker, price, number_of_shares)
                return True
        elif portfolio_option.strip() == "sell":
            ticker = input(" Portfolio >>> Input Stock Ticker: ")
            price = input(" Portfolio >>> Input Selling Price: ")
            number_of_shares = input(" Portfolio >>> Input Number of Shares: ")
            confirm = input(f" Portfolio >>> Confirm {int(number_of_shares)} shares of"\
                            f" {ticker.upper()} at {round(float(price), 4)} Y|n: ")
            if confirm == "Y":
                portfolio.sell_action(ticker, price, number_of_shares)
                return True
        elif portfolio_option.strip() == "deposit":
            amount = input(" Portfolio >>> Input Deposit Amount: $")
            confirm = input(f" Portfolio >>> Confirm Deposit of ${round(float(amount), 2)} Y|n: ")
            if confirm == "Y":
                portfolio.deposit_action(amount)
                return True
        elif portfolio_option.strip() == "search":
            ticker = input(" Portfolio >>> Input Search Ticker: ")
            if portfolio.search_portfolio(ticker):
                print(f" Portfolio >>> {portfolio.search_portfolio(ticker)}")
            else:
                print(f" Portfolio >>> {ticker.upper().strip()} Not Found in Portfolio")
            return True
        elif portfolio_option.strip() == "exit":
            return False
    else:
        print(" Portfolio >>> Invalid Input! --help to view options")
        return True

def main():
    f = True
    acceptable_inputs = ["--help", "load", "exit"]
    while f:
        t = input(" Home >>> ")
        if t in acceptable_inputs:
            if t == "--help":
                print(help_function())
            elif t == "load":
                p = Portfolio()
                load_flag = True
                while load_flag:
                    load_flag = load_interface(p)
            elif t == "exit":
                f = False
        else:
            print(" Home >>> Input Not Found! --help to view options")


if __name__ =="__main__":
    main()


