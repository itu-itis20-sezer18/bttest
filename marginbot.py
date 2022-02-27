import os
import requests
import threading
import datetime
import time
import sys
sys.setrecursionlimit(1000000)


min_of_fifteen = 999999
did_buy = False
count = 0

api_key = "LFJ3zBLrPGgEAkYRurlCFsUtoHloLy7H7njhbG4ADW5BA6rsTXCZnuBNFEGDvN2m"
api_secret = "E3bvOzjJzDpT2I3Yw4DW41KKlFdNkgEP0b0LxUxOCLiddOjvzOaZlyf1ukZ6Sq6C"

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.helpers import round_step_size

client = Client(api_key, api_secret)

client.futures_change_leverage(symbol="AVAXUSDT", leverage=5)


def get_tick_size(symbol: str) -> float:
    info = client.futures_exchange_info()

    for symbol_info in info['symbols']:
        if symbol_info['symbol'] == symbol:
            for symbol_filter in symbol_info['filters']:
                if symbol_filter['filterType'] == 'PRICE_FILTER':
                    return float(symbol_filter['tickSize'])


def get_rounded_price(symbol: str, price: float) -> float:
    return round_step_size(price, get_tick_size(symbol))



did_make_first_order = False

def has_buy_order():
    global client
    orders = client.futures_get_open_orders(symbol='AVAXUSDT')
    if(len(orders) == 0):
        return False
    for order in orders:
        if((order["status"] == "NEW" or order["status"] == "PARTIALLY_FILLED") and order["side"] == "BUY"):
            return True
    return False
def has_sell_order():
    global client
    orders = client.futures_get_open_orders(symbol='AVAXUSDT')
    if(len(orders) == 0):
        return False
    for order in orders:
        if((order["status"] == "NEW" or order["status"] == "PARTIALLY_FILLED") and order["side"] == "SELL"):
            return True
    return False
def futures_cancel_order():
    global client
    orders = client.futures_get_open_orders(symbol='AVAXUSDT')
    print("order",orders)
    if(len(orders) == 0):
        print("There is no order to cancel!")
        return
    for order in orders:
        if(order["status"] == "NEW" and order["side"] == "BUY"):
            print("Order cancelling...")
            client.futures_cancel_order(symbol="AVAXUSDT",orderId=order['orderId'])
            return


#api_key = "vIRsfYdBfur4Rh6mpYnrD0MbVTUeIqcueDUaJN2Xg8ydYLfVormfTAvp9u0JOO0U"
#api_secret = "iL3MItSyzwnDxwkiZHCHlGnDex1xm0ufF0chAATgKNp9S6TXvwqPu5KPzwqcHdSN"

def get_buying_price():
    print("Checking should buy...")
    global client
    if(has_buy_order() or has_sell_order()):
        return
    else:
        time.sleep(15)
        orders = client.futures_get_all_orders(symbol='AVAXUSDT')
        last_order = orders[-1]
        print("Last orders: ",last_order)
        if(last_order["side"] == "SELL"):
            return
        last_order_price = last_order["price"]
        last_order_price = (float(last_order_price)*1.006)
        print("Sell order is creating at price: ",last_order_price)
        last_order_price = get_rounded_price("AVAXUSDT", last_order_price)
        order = client.futures_create_order(
        symbol='AVAXUSDT',
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce='GTC',
        price=str(last_order_price),
        quantity=21.5)





#BUY ORDER
def buy(price):
    price = get_rounded_price("AVAXUSDT", price)
    print("Buying from price: ",price)
    order = client.futures_create_order(
    symbol='AVAXUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_LIMIT,
    timeInForce='GTC',
    price=str(price),
    quantity=21.5)
    #create sell order
    


#print(client.get_account())

#GET AVAX PRICE
def get_price():
    global did_make_first_order
    global min_of_fifteen
    price = client.get_ticker(symbol='AVAXUSDT')["lastPrice"]
    price = float(price)
    if(did_make_first_order):
        get_buying_price()
    if(price < min_of_fifteen):
        print("New low price for period: ",price)
        min_of_fifteen = price
    print(price)
    now = datetime.datetime.now()
    global did_buy
   # print(now.minute)
    #print(client.futures_get_open_orders())
    if(now.minute in [0,15,30,45]):
        print("Buy order: ",has_buy_order())
        print("Sell order: ",has_sell_order())
        if(not(has_buy_order()) and not(has_sell_order())):
            print("1")
            did_make_first_order = True
            buy(min_of_fifteen)
            min_of_fifteen = 9999999
            time.sleep(60)
        else: #satın aldıysa ama order gerçekleşmediyse
            print("2")
            if(has_buy_order()):
                futures_cancel_order()
                buy(min_of_fifteen)
                min_of_fifteen = 9999999
                time.sleep(60)

     



def printit():
  global did_buy
  time.sleep(1)
  get_price()
  printit()

printit()





#buy(100)


#trades = client.get_my_trades(symbol='AVAXUSDT')
#print(trades)
# print("Here")
# orders = client.futures_get_open_orders(symbol='AVAXUSDT')
# print("order",orders)


# for order in orders:
#      if(order["status"] == "NEW"):
#          print(order["side"],order["status"],order["price"])
    #time.sleep(1)
    #print(order['orderId'])



