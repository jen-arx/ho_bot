from binance.client import Client
import pandas as pd
import math
api_key = 'FNy2gKEWzs8mYjW0y60UWsNgtvSM9Dak9qypZEEzDtFhgIGgCsslrG5bXFz9HBVE'
api_secreat = 'quXmaGLmCj8AAT5stEtOGpC1I3C6lrIE8wkrDC27f0Pm4ghmvaJsteNr6D8q6D7z'
client = Client(api_key, api_secreat)

class Services():
    def kline(symbol):
        klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
        return klines
    def precision(symbol):
       infos = client.get_symbol_info(symbol)
       precision_qty = float(infos['filters'][1]['stepSize'])
       precision_qty = round(-math.log(precision_qty, 10), 0)
       precision_qty = int(precision_qty)
       precision_price = float(infos['filters'][0]['minPrice'])
       precision_price = round(-math.log(precision_price, 10), 0)
       precision_price = int(precision_price)
       return precision_qty, precision_price
    def quantity(symbol, amount):
        prec_qty, prec_price = Services.precision(symbol)
        avg_price = client.get_avg_price(symbol = symbol)
        avg_price = float(avg_price['price'])
        quantity = (amount / avg_price)
        quantity = round(quantity, prec_qty)
        return quantity
    def balance(symbol):
        info = client.get_account()
        df = pd.DataFrame(info["balances"], columns=['asset', 'free'])
        df = df.loc[df['asset'] == symbol]
        balance = df.iloc[0][1]
        return balance
    def server_time():
        time_srv = client.get_server_time()
        time = pd.to_datetime(time_srv['serverTime'], unit = "ms")
        time = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z")
        return time