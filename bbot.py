import os
import requests
import threading
import datetime
import time
import sys
sys.setrecursionlimit(10000)


min_of_fifteen = 999999
did_buy = False
count = 0

api_key = "5WgQTKKp4IZHC9Tn2ZvZIbl174xxw7J5RHqEatJgVn81u8HIJ56yRzt5iLWn1sfW"
api_secret = "raJFtIR2bgfkrvLg4XwmFmr9Y9N2S9XbunEimaJiEJtvNivr4zMEEzj8cgpORvif"
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret,testnet=True)

did_make_first_order = False

def has_buy_order():
    global client
    orders = client.get_open_orders(symbol='BTCUSDT')
    if(len(orders) == 0):
        return False
    for order in orders:
        if((order["status"] == "NEW" or order["status"] == "PARTIALLY_FILLED") and order["side"] == "BUY"):
            return True
    return False
def has_sell_order():
    global client
    orders = client.get_open_orders(symbol='BTCUSDT')
    if(len(orders) == 0):
        return False
    for order in orders:
        if((order["status"] == "NEW" or order["status"] == "PARTIALLY_FILLED") and order["side"] == "SELL"):
            return True
    return False
def cancel_order():
    global client
    orders = client.get_open_orders(symbol='BTCUSDT')
    print("order",orders)
    if(len(orders) == 0):
        print("There is no order to cancel!")
        return
    for order in orders:
        if(order["status"] == "NEW" and order["side"] == "BUY"):
            print("Order cancelling...")
            client.cancel_order(symbol="BTCUSDT",orderId=order['orderId'])
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
        orders = client.get_all_orders(symbol='BTCUSDT')
        last_order = orders[-1]
        print("Last orders: ",last_order)
        last_order_price = last_order["price"]
        last_order_price = "{:.2f}".format(float(last_order_price)*1.008)
        print("Sell order is creating at price: ",last_order_price)
        order = client.create_order(
        symbol='BTCUSDT',
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce='GTC',
        price=str(last_order_price),
        quantity=1)





#BUY ORDER
def buy(price):
    print("Buying from price: ",price)
    order = client.create_order(
    symbol='BTCUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_LIMIT,
    timeInForce='GTC',
    price=str(price),
    quantity=1)
    #create sell order
    


print(client.get_account())

#GET AVAX PRICE
def get_price():
    global did_make_first_order
    global min_of_fifteen
    price = client.get_ticker(symbol='BTCUSDT')["lastPrice"]
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
    #print(client.get_open_orders())
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
                cancel_order()
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


#trades = client.get_my_trades(symbol='BTCUSDT')
#print(trades)
# print("Here")
# orders = client.get_open_orders(symbol='BTCUSDT')
# print("order",orders)


# for order in orders:
#      if(order["status"] == "NEW"):
#          print(order["side"],order["status"],order["price"])
    #time.sleep(1)
    #print(order['orderId'])



