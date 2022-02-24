import os
import requests
import threading
import datetime
import time

min_of_fifteen = 0
did_buy = False
count = 0


api_key = "27RUHaP5jFMNkRIJs6jpvgnDtJLCd18aFYtwnfE2OPTjMAa9RBSp1xZHDf1CDmGh"
api_secret = "o1r21BS7sLyOqUCtLvdEtB3FjttYxWZIQtXlNDx7VEittrhBgsFNp6NzCje9jeGb"
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret,testnet=True)

boolean = False
def buy(price):
    # did_buy = True
    order = client.create_order(
    symbol='ETHUSDT',
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    #timeInForce='GTC',
    #price=str(price),
    quantity=1.0)
    # #create sell order
    # orderr = client.create_order(
    # symbol='ETHUSDT',
    # side=Client.SIDE_SELL,
    # type=Client.ORDER_TYPE_LIMIT,
    # timeInForce='GTC',
    # price=str(price*1.004),
    # quantity=0.01)



#buy(35070.0)
orders = client.get_open_orders(symbol='ETHUSDT')
#client.cancel_order(symbol="ETHUSDT",orderId='9566572')
print("order",orders)
#print(client.get_account())

# def has_buy_order():
#     global client
#     orders = client.get_open_orders(symbol='ETHUSDT')
#     if(len(orders) == 0):
#         return False
#     for order in orders:
#         if(order["status"] == "NEW" and order["side"] == "BUY"):
#             return True
#     return False

# print(has_buy_order())

