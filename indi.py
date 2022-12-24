import talib as ta 
from ser import Services
import pandas as pd
class INDI():
    def rsi(symbol) :
        a = Services.kline(symbol= symbol)
        df = pd.DataFrame(a)
        df.columns = [
            'open_time', 'Open_price', 'High_price', 'Low_price', 'Close_price',
        'Volume', 'Close_time', 'Quote_asset_volume', 'Number_of_trades', 
        'buy_base_asset_volume', 'buy_quote_asset_volume', 'ignore'
            ]
        rs = ta.RSI(df['Close_price'], timeperiod = 14)
        rs = rs[len(rs) - 1]
        rs = float(rs)
        rs = round(rs, 2)
        return rs
    def macd(symbol):
        a = Services.kline(symbol= symbol)
        df = pd.DataFrame(a)
        df.columns = [
            'open_time', 'Open_price', 'High_price', 'Low_price', 'Close_price',
        'Volume', 'Close_time', 'Quote_asset_volume', 'Number_of_trades', 
        'buy_base_asset_volume', 'buy_quote_asset_volume', 'ignore'
            ]
        macd, macdsignal, macdhist = ta.MACD(df['Close_price'], fastperiod=12, slowperiod=26, signalperiod=9)
        macd = macd[len(macd) -1]
        macd = float(macd)
        macd = round(macd, 2)
        macdsignal = macdsignal[len(macdsignal) -1]
        macdsignal = float(macdsignal)
        macdsignal = round(macdsignal, 2)
        macdhist = macdhist[len(macdhist) -1]
        macdhist = float(macdhist)
        macdhist = round(macdhist,2)
        return macd, macdsignal, macdhist
    def obv(symbol):
        a = Services.kline(symbol= symbol)
        df = pd.DataFrame(a)
        df.columns = [
            'open_time', 'Open_price', 'High_price', 'Low_price', 'Close_price',
        'Volume', 'Close_time', 'Quote_asset_volume', 'Number_of_trades', 
        'buy_base_asset_volume', 'buy_quote_asset_volume', 'ignore'
            ]
        obv = ta.OBV(df['Close_price'], df['Volume'])
        obv = obv[len(obv) -1]
        obv = float(obv)
        obv = round(obv, 1)
        return obv