from os import system
import time
from ser import Services, client
from indi import INDI
import json
class BOT():
    def st_rsi_obv_macd(symbol, pairs , stop_lose, take_profit, qty, rein):
        price = client.get_avg_price(pairs)
        if INDI.rsi(symbol= pairs) <= 50 and INDI.rsi(symbol = pairs) >= 10 :
            f = open('buy.json')
            data = json.load(f)
            for i in data :
                bu = i['bu']
                price = i['price']
                qtty = i['qnt']
            if bu == "" :
                qty = Services.quantity(symbol= pairs, amount= (qty - rein))
                buy = client.order_market_buy(symbol = pairs ,quantity = qty )
                orderID = buy['orderId']
                origQty = buy["origQty"]
                avg_price_buy = float(buy['cummulativeQuoteQty']) / float(buy['origQty'])
                with open('buy.json', 'r+') as f:
                    data = json.load(f)
                    data['bu'] = 'done'
                    data['price'] = f'{avg_price_buy}'
                    data['qnt'] = f'{origQty}'
                    f.seek(0)  
                    json.dump(data, f, indent=3)
                    f.truncate() 
                print(f'buy order done ...\n{buy}\norderId : {orderID}\nqty : {origQty} \n price : {avg_price_buy}')
            elif bu == "done":
                if float(client.get_avg_price(symbol = pairs)) >=  price + take_profit :
                    qty = qtty 
                    qty = Services.quantity(symbol=pairs , amount= qty)
                    sell = client.order_market_sell(symbol = pairs, quantity = qty)
                    orderID = sell['orderId']
                    price= sell['fills'][0]['price']
                    with open('buy.json', 'r+') as f:
                        data = json.load(f)
                        data['bu'] = ''
                        data['price'] = ''
                        data['qnt'] = ''
                        f.seek(0)  
                        json.dump(data, f, indent=3)
                        f.truncate()
                    print(f'Sell order done ...\n{sell}\norderId : {orderID} price= {price}')
                elif float(client.get_avg_price(symbol = pairs)) <=  price - stop_lose :
                    qty = qtty 
                    qty = Services.quantity(symbol=pairs , amount= qty)
                    sell = client.order_market_sell(symbol = pairs, quantity = qty)
                    orderID = sell['orderId']
                    price= sell['fills'][0]['price']
                    with open('buy.json', 'r+') as f:
                        data = json.load(f)
                        data['bu'] = ''
                        data['price'] = ''
                        data['qnt'] = ''
                        f.seek(0)  
                        json.dump(data, f, indent=3)
                        f.truncate()
                    print(f'Sell order done with lose ...\n{sell}\norderId : {orderID} price= {price}')
                elif float(client.get_avg_price(symbol = pairs)) < price and INDI.rsi(symbol= pairs) < 50 :
                    f = open('buy.json')
                    data = json.load(f)
                    for i in data :
                        bu = i['bu']
                        price = i['price']
                        qtty = i['qnt']
                    if bu == '':
                        qty = Services.quantity(symbol= pairs, amount= (qty - rein))
                        buy = client.order_market_buy(symbol = pairs ,quantity = qty )
                        orderID = buy['orderId']
                        origQty = buy["origQty"]
                        avg_price_buy = float(buy['cummulativeQuoteQty']) / float(buy['origQty'])
                        with open('buy.json', 'r+') as f:
                            data = json.load(f)
                            data['bu'] = 'done'
                            data['price'] = f'{avg_price_buy}'
                            data['qnt'] = f'{origQty}'
                            f.seek(0)  
                            json.dump(data, f, indent=3)
                            f.truncate() 
                        print(f'buy order done support ...\n{buy}\norderId : {orderID}\nqty : {origQty} \n price : {avg_price_buy}')
                    elif bu == 'done':
                        qty = qtty 
                        qty = Services.quantity(symbol=pairs , amount= qty)
                        sell = client.order_market_sell(symbol = pairs, quantity = qty)
                        orderID = sell['orderId']
                        price= sell['fills'][0]['price']
                        with open('buy.json', 'r+') as f:
                            data = json.load(f)
                            data['bu'] = ''
                            data['price'] = ''
                            data['qnt'] = ''
                            f.seek(0)  
                            json.dump(data, f, indent=3)
                            f.truncate()
                        print(f'Sell order done  support...\n{sell}\norderId : {orderID} price= {price}')
                    else :
                        print('pass Second for this time')
            else :
                print('Pass first buy for this time...!')
        else:
            print('bad RSI for start for now \npass ')

while True:
    try:
        while True:
            time.sleep(5)
            p = BOT.st_rsi_obv_macd(symbol= "")
    except Exception as e:
        if "HTTPSConnectionPool" in str(e) and connection == "OK":
            print("Connection timeout ...")
            connection = "Erorr"
            time.sleep(2)
        pass
