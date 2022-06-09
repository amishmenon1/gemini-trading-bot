from datetime import datetime

from gemini.classes.Order import Order
# from gemini.orderwebsocketclient import OrderEventsWS
from gemini.restclient import Client
import time
import sys
import gemini.tracker as tracker
import gemini.interface as interface
import os
import threading
import gemini.logger
import logging
import gemini.fourmovingaverage as fourmovingaverage

try:
    import thread
except ImportError:
    import _thread as thread
import time
import logging


with open('gem.txt', "r") as text_file:
    text_string = text_file.readlines()
    public_key = text_string[2].split(':')[1].rstrip() # public key with heartbeat
    api_secret = text_string[3].split(':')[1].rstrip() # API secret with heartbeat

run_thread = None
marketdata_websocket_thread = None
activeorder_websocket_thread = None
should_run = False
speak = False
use_websocket = False
if use_websocket:
    client = websocketclient.initiate_restclient_connection()
else:
    client = Client(public_key, api_secret, False)
purchase_quantity = 0
start_time = None
num_seconds = None
request_count = 0

# user params
user_initial_dollar_balance = 0
user_buy_price = 0
user_sell_price1 = 0
user_sell_price2 = 0
user_sell_price3 = 0
user_sell_price4 = 0
user_sell_price5 = 0
user_stop_limit_price = 0
user_speak_input = 'n'

order_type = "exchange limit"
buy_order_made = False
buy_order = None
sell_order = None
sell_order_1 = None
sell_order_2 = None
sell_order_3 = None
sell_order_4 = None
sell_order_5 = None
stop_limit_order = None
buy_side = "buy"
sell_side = "sell"
options = ["maker-or-cancel"]
token_symbol = "ftmusd"
latest_order_id = None
order_id_iterator = 0
total_loss = 0
total_gain = 0
break_even_stop = None
stop_limit_order = None
break_even_stop_made = False
stop_limit_made = False
sell_order_made = False

sell_order_1_coefficient = .8
sell_order_2_coefficient = .2
sell_order_3_coefficient = None
sell_order_4_coefficient = None
sell_order_5_coefficient = None

one_sell_price = False
two_sell_prices = False
three_sell_prices = False
four_sell_prices = False
five_sell_prices = False


def build_interface():
    window = interface.draw_gui(run, stop)
    return window


def convert_to_float(entry):
    return float(entry) if entry != '' else 0


def populate_user_values():
    global token_symbol
    global user_buy_price
    global user_sell_price1
    global user_sell_price2
    global user_sell_price3
    global user_sell_price4
    global user_sell_price5
    global user_stop_limit_price
    global user_initial_dollar_balance
    global one_sell_price
    global two_sell_prices
    global three_sell_prices
    global four_sell_prices
    global five_sell_prices
    global user_speak_input
    global speak

    token_symbol = interface.token_symbol_input_label_entry.get()
    user_initial_dollar_balance = convert_to_float(interface.initial_balance_entry.get())
    user_buy_price = convert_to_float(interface.target_buy_price_entry.get())
    user_sell_price1 = convert_to_float(interface.target_sell_price1_entry.get())
    # user_sell_price2 = convert_to_float(interface.target_sell_price2_entry.get())
    # user_sell_price3 = convert_to_float(interface.target_sell_price3_entry.get())
    # user_sell_price4 = convert_to_float(interface.target_sell_price4_entry.get())
    # user_sell_price5 = convert_to_float(interface.target_sell_price5_entry.get())
    user_stop_limit_price = convert_to_float(interface.target_stop_limit_price_entry.get())
    user_speak_input = interface.speak_label_entry.get()
    speak = True if user_speak_input == 'y' else False

    # TODO for dollar cost averaging
    one_sell_price = user_sell_price1 > 0 and user_sell_price2 == 0 and user_sell_price3 == 0 and user_sell_price4 == 0 and user_sell_price5 == 0
    # two_sell_prices = user_sell_price1 > 0 and user_sell_price2 > 0 and user_sell_price3 == 0 and user_sell_price4 == 0 and user_sell_price5 == 0
    # three_sell_prices = user_sell_price1 > 0 and user_sell_price2 > 0 and user_sell_price3 > 0 and user_sell_price4 == 0 and user_sell_price5 == 0
    # four_sell_prices = user_sell_price1 > 0 and user_sell_price2 > 0 and user_sell_price3 > 0 and user_sell_price4 > 0 and user_sell_price5 == 0
    # five_sell_prices = user_sell_price1 > 0 and user_sell_price2 > 0 and user_sell_price3 > 0 and user_sell_price4 > 0 and user_sell_price5 > 0


def create_limit_buy_order(buy_order_id, quantity):
    global buy_order_made
    global buy_order
    global token_symbol
    global user_buy_price
    global buy_side
    global speak

    buy_order = Order(client.new_order(buy_order_id, token_symbol, quantity, user_buy_price, buy_side))
    buy_order_made = True
    # print("New buy order made: " + str(buy_order.to_string()))
    logging.info("New buy order made")
    if speak:
        os.system('say "New buy order has been placed"')
    return buy_order


def get_token_price():
    global token_symbol
    try:
        price = tracker.get_current_bid_price(token_symbol)
        # price = websocketclient.get_btc_price()
    except:
        pass
    return price

def create_stop_limit(order_id, quantity):
    global token_symbol
    global user_buy_price
    global sell_side
    global stop_limit_made
    global stop_limit_order
    global user_stop_limit_price #.3395
    global speak
    buffer = 0.005 #if token_symbol == "ustusd" else 50
    buffer2 = 0.0005
    print('making stop limit order')
    stop_price = user_stop_limit_price + buffer #.3344
    if stop_price >= float(get_token_price()):
        stop_price = float("{0:.4f}".format(float(get_token_price()) - (buffer2)))
        user_stop_limit_price = stop_price - buffer
    stop_limit_order = Order(
        client.new_limit_order(order_id, token_symbol, quantity, float("{0:.4f}".format(user_stop_limit_price)), sell_side, float("{0:.4f}".format(stop_price))))
    stop_limit_made = True
    print("Stop limit made.")
    if speak:
        os.system('say "Stop limit order has been placed"')
    return stop_limit_order


def create_limit_sell_order(sell_order_id, sell_price, quantity):
    global sell_order
    global sell_side
    global token_symbol
    global sell_order_made
    global speak

    sell_order = Order(client.new_order(sell_order_id, token_symbol, quantity, sell_price, sell_side))
    sell_order_made = True
    print("New limit sell order placed.")
    if speak:
        os.system('say "New sell order has been placed"')

    return sell_order


def order_filled(order, stop_limit_price=None):
    filled = False
    if hasattr(order, 'order_id'):
        order_status = tracker.get_order_status(order.order_id)
        if order_status and hasattr(order_status, 'remaining_amount') and order_status.remaining_amount:
            filled = bool(float(order_status.remaining_amount) == 0)
        # filled = websocketclient.order_filled(order, stop_limit_price)
        return filled


def buy_order_placed():
    global buy_order_made
    return buy_order_made
    # return websocketclient.buy_order_placed()


def sell_order_placed():
    global sell_order_made
    return sell_order_made
    # return websocketclient.sell_order_placed()


def order_cancelled(order):
    cancelled = False
    if hasattr(order, 'order_id'):
        order_status = tracker.get_order_status(order.order_id)
        if order_status and hasattr(order_status, 'is_cancelled'):
            cancelled = bool(order_status.is_cancelled)
        # cancelled = websocketclient.order_cancelled(order)
        return cancelled


def get_sell_quantity():
    global sell_order_1_coefficient
    global sell_order_2_coefficient
    global sell_order_3_coefficient
    global sell_order_4_coefficient
    global sell_order_5_coefficient
    global purchase_quantity
    global one_sell_price
    global two_sell_prices
    global three_sell_prices
    global four_sell_prices
    global five_sell_prices

    sell_quantities = {}

    if one_sell_price:
        sell_quantities['sell_quantity'] = purchase_quantity
    elif two_sell_prices:
        sell_quantities['sell_quantity1'] = sell_order_1_coefficient * purchase_quantity
        sell_quantities['sell_quantity2'] = sell_order_2_coefficient * purchase_quantity
    elif three_sell_prices:
        sell_quantities['sell_quantity1'] = sell_order_1_coefficient * purchase_quantity
        sell_quantities['sell_quantity2'] = sell_order_2_coefficient * purchase_quantity
        sell_quantities['sell_quantity3'] = sell_order_3_coefficient * purchase_quantity
    elif four_sell_prices:
        sell_quantities['sell_quantity1'] = sell_order_1_coefficient * purchase_quantity
        sell_quantities['sell_quantity2'] = sell_order_2_coefficient * purchase_quantity
        sell_quantities['sell_quantity3'] = sell_order_3_coefficient * purchase_quantity
        sell_quantities['sell_quantity4'] = sell_order_4_coefficient * purchase_quantity
    elif five_sell_prices:
        sell_quantities['sell_quantity1'] = sell_order_1_coefficient * purchase_quantity
        sell_quantities['sell_quantity2'] = sell_order_2_coefficient * purchase_quantity
        sell_quantities['sell_quantity3'] = sell_order_3_coefficient * purchase_quantity
        sell_quantities['sell_quantity4'] = sell_order_4_coefficient * purchase_quantity
        sell_quantities['sell_quantity5'] = sell_order_5_coefficient * purchase_quantity
    else:
        stop()

    return sell_quantities


def should_buy():
    global user_initial_dollar_balance
    global client

    return buy_order_placed() is False


def start_timer():
    global start_time
    global num_seconds
    global request_count

    start_time = time.time()
    num_seconds = 60
    request_count = 0
    return start_time


def run_in_new_thread():
    global user_buy_price
    global user_sell_price1
    global user_sell_price2
    global user_sell_price3
    global user_sell_price4
    global user_sell_price5
    global user_stop_limit_price
    global buy_order
    global user_initial_dollar_balance
    global purchase_quantity
    global sell_order_1
    global sell_order_2
    global sell_order_3
    global sell_order_4
    global sell_order_5
    global stop_limit_order
    global one_sell_price
    global two_sell_prices
    global three_sell_prices
    global four_sell_prices
    global five_sell_prices
    global should_run
    global run_thread
    global start_time
    global num_seconds
    global request_count
    global speak
    global sell_order_made

    populate_user_values()

    if user_stop_limit_price == 0:
        print('Missing stop limit price.')
        should_run = False
    else:
        should_run = True

    while True and should_run is True:
        lock = threading.Lock()
        start_time = start_timer()
        with lock:
            current_time = time.time()
            elapsed_time = current_time - start_time
            print("Elapsed Time: {} seconds".format(elapsed_time))
            buy_order_id_prefix = 'buy-order-'
            sell_order_id_prefix = 'sell-order-'
            stop_order_prefix = 'stop-limit-'
            # purchase_quantity = '%.8f' % (user_initial_dollar_balance / user_buy_price) #btc
            # purchase_quantity = '%.6f' % (user_initial_dollar_balance / user_buy_price)  #eth
            purchase_quantity = '%.4f' % (user_initial_dollar_balance / user_buy_price)  #ftm
            # purchase_quantity = '%.3f' % (user_initial_dollar_balance / user_buy_price)  #ust
            # user_sell_price1 could be the threshold price?

            if should_buy():
                buy_order_id = buy_order_id_prefix + str(order_id_iterator)
                buy_order = create_limit_buy_order(buy_order_id, purchase_quantity)
                time.sleep(5)

            if order_filled(buy_order):
                if sell_order_placed() is False:
                    print('Buy Order 1 has been filled.')
                # this is a Mac/Linux feature only
                if speak:
                    os.system('say "Buy order has been filled. Making stop limit now."')

                if stop_limit_made is False and get_token_price() <= user_stop_limit_price:
                    stop_limit_id = stop_order_prefix + str(order_id_iterator)
                    print('purchase qty: {}'.format(purchase_quantity))
                    if sell_order_placed() is True:
                        print('sell order ID: ' + sell_order_id)
                        client.cancel_all_orders()
                        sell_order_made = False
                        time.sleep(2)
                    stop_limit_order = create_stop_limit(stop_limit_id, purchase_quantity)
                    time.sleep(2)

                if sell_order_placed() is False and stop_limit_made is False:
                    print('Making sell order...')
                    # this is a Mac/Linux feature only
                    if speak:
                        os.system('say "Making sell order now"')

                    if one_sell_price:
                        sell_quantity = float(get_sell_quantity()['sell_quantity'])
                        sell_order_id = sell_order_id_prefix + str(order_id_iterator)
                        sell_order_1 = create_limit_sell_order(sell_order_id, user_sell_price1, sell_quantity)
                        time.sleep(4)
                    # TODO: add logic for multiple sell quantities

                    print('Waiting for sell order to be filled...')
                    # this is a Mac/Linux feature only
                    if speak:
                        os.system('say "Waiting for sell order to be filled."')

                if sell_order_placed() is False and get_token_price() >= user_sell_price1:
                    sell_quantity = float(get_sell_quantity()['sell_quantity'])
                    sell_order_id = sell_order_id_prefix + str(order_id_iterator)
                    sell_order_1 = create_limit_sell_order(sell_order_id, user_sell_price1, sell_quantity)
                    time.sleep(4)

            elif order_cancelled(buy_order):
                print('Buy order has been cancelled. Exiting')
                if speak:
                    os.system('say "Buy order has been cancelled. Check connection. Exiting."')
                stop()

            if order_filled(sell_order_1):
                print('Sell order 1 has been filled.')
                # this is a Mac/Linux feature only
                if speak:
                    os.system('say "Sell order 1 has been filled."')
                print('Cancelling stop limit order.')
                client.cancel_session_orders()
                stop()

            # elif order_cancelled(sell_order_1):
            #     print('Sell order 1 has been cancelled. Exiting')
            #     # this is a Mac/Linux feature only
            #     if speak:
            #         os.system('say "Sell order 1 has been cancelled. Exiting."')
            #     stop()

            if order_filled(stop_limit_order, user_stop_limit_price):
                print('Stop limit order has been filled. Exiting.')
                # this is a Mac/Linux feature only
                if speak:
                    os.system('say "Stop limit order has been filled. Exiting."')
                print('Cancelling sell order.')
                client.cancel_session_orders()
                stop()

            elif order_cancelled(stop_limit_order):
                print('Stop limit order has been cancelled. Exiting')
                # this is a Mac/Linux feature only
                if speak:
                    os.system('say "Stop limit order has been cancelled. Exiting."')
                stop()

            time.sleep(3)

            # try:
            #     tracker.send_heartbeat()
            #     print('{}: Heartbeat sent'.format(datetime.now()))
            # except:
            #     print('{}: HEARTBEAT FAILED'.format(datetime.now()))
            #     pass


def run():
    global run_thread
    run_thread = threading.Thread(target=run_in_new_thread)
    run_thread.daemon = True
    run_thread.name = 'run_thread'
    run_thread.start()


def stop():
    global run_thread
    sys.exit()


def open_websocket_connections():
    global marketdata_websocket_thread
    global activeorder_websocket_thread

    marketdata_websocket_thread = threading.Thread(target=websocketclient.open_marketdata_websocket)
    marketdata_websocket_thread.daemon = True
    marketdata_websocket_thread.name = 'marketdata_websocket_thread'
    marketdata_websocket_thread.start()

    activeorder_websocket_thread = threading.Thread(target=websocketclient.open_active_order_websocket)
    activeorder_websocket_thread.daemon = True
    activeorder_websocket_thread.name = 'activeorder_websocket_thread'
    activeorder_websocket_thread.start()


# open_websocket_connections()
root = build_interface()
interface.refresh_price(root, token_symbol)
root.mainloop()
