import os
import requests
import threading
import datetime
import time

min_of_fifteen = 0
did_buy = False
count = 0


api_key = "02c8566371e57c60a87213daf59cf184322bf70f33cb43506f6929436b582218"
api_secret = "a8e399e83af674e259ae506e15ed1fe5ebf17c16dd8639aff7f63047bc264aa6"
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret,testnet=True)

boolean = False
def buy(price):
    # did_buy = True
    order = client.create_order(
    symbol='BTCUSDT',
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    #timeInForce='GTC',
    #price=str(price),
    quantity=1.0)
    # #create sell order
    # orderr = client.create_order(
    # symbol='BTCUSDT',
    # side=Client.SIDE_SELL,
    # type=Client.ORDER_TYPE_LIMIT,
    # timeInForce='GTC',
    # price=str(price*1.004),
    # quantity=0.01)



#buy(35070.0)
orders = client.get_open_orders(symbol='BTCUSDT')
#client.cancel_order(symbol="BTCUSDT",orderId='9566572')
print("order",orders)
#print(client.get_account())

# def has_buy_order():
#     global client
#     orders = client.get_open_orders(symbol='BTCUSDT')
#     if(len(orders) == 0):
#         return False
#     for order in orders:
#         if(order["status"] == "NEW" and order["side"] == "BUY"):
#             return True
#     return False

# print(has_buy_order())

