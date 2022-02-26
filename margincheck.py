import os
import requests
import threading
import datetime
import time

min_of_fifteen = 0
did_buy = False
count = 0


api_key = "LFJ3zBLrPGgEAkYRurlCFsUtoHloLy7H7njhbG4ADW5BA6rsTXCZnuBNFEGDvN2m"
api_secret = "E3bvOzjJzDpT2I3Yw4DW41KKlFdNkgEP0b0LxUxOCLiddOjvzOaZlyf1ukZ6Sq6C"
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret)


boolean = False
def buy(price):
    # did_buy = True
    order = client.create_futures_order(
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
#orders = client.get_open_orders(symbol='BTCUSDT')
#client.cancel_order(symbol="BTCUSDT",orderId='9566572')
print(client.futures_get_all_orders()[-1])
#print(client.futures_account_balance(symbol="BTCUSDT"))

# def get_tick_size(symbol: str) -> float:
#     info = client.futures_exchange_info()

#     for symbol_info in info['symbols']:
#         if symbol_info['symbol'] == symbol:
#             for symbol_filter in symbol_info['filters']:
#                 if symbol_filter['filterType'] == 'PRICE_FILTER':
#                     return float(symbol_filter['tickSize'])


# def get_rounded_price(symbol: str, price: float) -> float:
#     return round_step_size(price, get_tick_size(symbol))


# price = get_rounded_price(symbol, price)



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

