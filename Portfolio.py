import datetime
import json
import os

class Portfolio():
    def __init__(self):
        self.stock_list = []

    def populate_portfolio(self):
        if os.path.isfile("portfolio.json"):
            with open(os.path.join(os.getcwd(), "portfolio.json"), 'r') as f:
                data = json.load(f)
            return data
        else:
            self.create_portfolio()

    def create_portfolio(self):
        with open(os.path.join(os.getcwd(), "portfolio.json"), 'w+') as f:
            pass

    def buy_action(self, ticker, price, number):
        try:
            with open(os.path.join(os.getcwd(), "portfolio.json"), 'r') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
        try:
            data[ticker].append({f"{datetime.date.today()}": {"action": "buy",
                                                              "price": round(float(price), 4),
                                                              "shares": int(number)}})
        except KeyError:
            data[ticker] = [{f"{datetime.date.today()}": {"action": "buy",
                                                          "price": round(float(price), 4),
                                                          "shares": int(number)}}]
        with open(os.path.join(os.getcwd(), "portfolio.json"), 'w') as fw:
            json.dump(data, fw, indent=4)
            
    def sell_action(self, ticker, price, number):
        try:
            with open(os.path.join(os.getcwd(), "portfolio.json"), 'r') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
        try:
            data[ticker].append({f"{datetime.date.today()}": {"action": "sell",
                                                              "price": round(float(price), 4),
                                                              "shares": int(number)}})
        except KeyError:
            data[ticker] = [{f"{datetime.date.today()}": {"action": "sell",
                                                          "price": round(float(price), 4),
                                                          "shares": int(number)}}]
        with open(os.path.join(os.getcwd(), "portfolio.json"), 'w') as fw:
            json.dump(data, fw, indent=4)

    def deposit_action(self, amount):
        try:
            with open(os.path.join(os.getcwd(), "portfolio.json"), 'r') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
        try:
            data["WALLET"].append({f"{datetime.date.today()}": {"action": "deposit",
                                                              "amount": round(float(amount), 2)}})
        except KeyError:
            data["WALLET"] = [{f"{datetime.date.today()}": {"action": "deposit",
                                                              "amount": round(float(amount), 2)}}]
        with open(os.path.join(os.getcwd(), "portfolio.json"), 'w') as fw:
            json.dump(data, fw, indent=4)

    def search_portfolio(self, ticker):
        try:
            with open(os.path.join(os.getcwd(), "portfolio.json"), 'r') as f:
                data = json.load(f)
            try:
                if ticker.upper() == "WALLET":
                    total = 0
                    for d in data[ticker.upper()]:
                        for i in d:
                            print(d[i]["action"])
                            if d[i]["action"] == "deposit":
                                total += float(d[i]["amount"])
                            elif d[i]["action"] == "withdrawl":
                                total -= float(d[i]["amount"])
                    return f"{ticker.upper()}: Total: {total}"
                else:
                    total_amount = 0
                    total_shares = 0
                    for d in data[ticker.upper()]:
                        for i in d:
                            if d[i]["action"] == "buy":
                                total_shares += float(d[i]["shares"])
                            elif d[i]["action"] == "sell":
                                total_shares -= float(d[i]["shares"])
                    return f"{ticker.upper()}: Total Number of Shares: {total_shares}"
            except KeyError:
                return False
        except json.decoder.JSONDecodeError:
            return False


