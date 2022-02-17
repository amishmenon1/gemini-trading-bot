import requests
from talib import RSI, BBANDS, STOCH, STOCHRSI
import pandas_datareader.data as web
import matplotlib.pyplot as plt


# user params
# user_initial_dollar_balance = 0
# user_limit_buy_price = None
# user_limit_sell_price = None
# user_set_aside = None
# user_stop_limit_price = None
# user_max_loss = None
# user_failsafe_price = None
# user_stop_price = None

# def create_stop_loss_below_buy_price(stop_limit_id, quantity):
#     global stop_limit_order
#     global btc_symbol
#     global user_stop_limit_price
#     global sell_side
#     global user_stop_price
#     global stop_limit_made
#
#     stop_limit_order = Order(c.new_limit_order(stop_limit_id, btc_symbol, quantity, user_stop_limit_price,
#                                                sell_side, user_stop_price))
#     stop_limit_made = True
#     print("Stop limit placed: " + str(stop_limit_order.to_string()))
#     return stop_limit_order


# def downloadLatestBtcPricingHistory():
#     latest_btc_pricing_history_link = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1552953789&period2=1584576189&interval=1d&events=history';
#     btc_pricing_history_csv = requests.get(latest_btc_pricing_history_link)
#     open('BTC-USD.csv', 'wb').write(btc_pricing_history_csv.content)


# using ta

    # downloadLatestBtcPricingHistory()
    # pricing_data = pd.read_csv('BTC-USD.csv')
    # pricing_data['ta_rsi'] = RSI(pricing_data['Close'])
    # pricing_data['ta_stoch_k'], pricing_data['ta_stoch_d'] = STOCH(pricing_data['High'], pricing_data['Low'], pricing_data['Close'])
    # pricing_data['ta_stoch_rsi_k'], pricing_data['ta_stoch_rsi_d'] = STOCHRSI(pricing_data['Close'])
    # pricing_data.to_csv('BTC-USD.csv')


 # new buy order

    # if currentBtcPrice > 5000:
    # print("BTC is above $5000. Placing new order to buy.")
    # quantity = '%.5f'%(budget / currentBtcBidPrice)
    # price = 4000
    # side = "buy"
    # options = ["maker-or-cancel"]
    # print("Bitcoin is currently trading at $" + str(currentBtcPrice) + ". I want to buy " + str(quantity) + " bitcoins at $" + str(price) + " each. My budget is $" + str(budget))
    # new_order = c.new_order("men-btc-usd-order-1", btcSymbol, quantity, price, side, type)
    # print("New order: " + str(new_order))

    # new sell order

    # cancelling an order

    # get_active_orders() only works when you stay in the same client session
    # orders = c.get_active_orders()
    # print("Orders: " + str(orders))
    # order = orders[0]
    # orderId = order['order_id']
    # time.sleep(10)
    # c.cancel_order(orderId)

    # check order status

    # orderStatus = c.get_order_status(orderId)
    # amountFilled = orderStatus['executed_amount']
    # print("order is live: " + str(orderStatus['is_live']))
    # print("amount of order filled: " + amountFilled)
    # if int(amountFilled) == 100:
    #     print("order has been filled")
    #

    # TA's RSI

    # df['ta_rsi'] = ta.momentum.rsi(df.Close)
    # print("TA RSI: " + df['ta_rsi'])
    # TA's Stochastic Oscillator
    # df['ta_stoch_k'] = ta.momentum.stoch('%.5f'%(df.High), '%.5f'%(df.Low), '%.5f'%(df.Close))
    # df['ta_stoch_d'] = ta.momentum.stoch_signal('%.5f'%(df.High), '%.5f'%(df.Low), '%.5f'%(df.Close))


    # using ta-lib

    # start = '2015-04-22'
    # end = '2017-04-22'
    # symbol = 'MCD'
    # max_holding = 100
    # price = web.DataReader(name=symbol, data_source='quandl', start=start, end=end)
    # price = price.iloc[::-1]
    # price = price.dropna()
    # close = price['AdjClose'].values
    # up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    # rsi = RSI(close, timeperiod=14)
    # print("RSI (first 10 elements)\n", rsi[14:24])




# def get_current_bid_price():
#     global btc_ticker
#     global btc_symbol
#     btc_ticker = c.get_ticker(btc_symbol)
#     return float(btc_ticker['bid'])


# def get_current_ask_price():
#     global btc_ticker
#     global btc_symbol
#     btc_ticker = c.get_ticker(btc_symbol)
#     return round(float(btc_ticker['ask']), 2)
#
#
# def get_order_status(status_id):
#     return Order(c.get_order_status(status_id))
#
#
# def get_last_btc_order():
#     global btc_ticker
#     global btc_symbol
#     btc_ticker = c.get_ticker(btc_symbol)
#     return float(btc_ticker['last'])
#
#
# def get_usd_volume():
#     global btc_ticker
#     global btc_symbol
#     btc_ticker = c.get_ticker(btc_symbol)
#     volume_dictionary = dict(btc_ticker['volume'])
#     float(volume_dictionary['USD'])
#
#
# def get_btc_volume():
#     global btc_ticker
#     global btc_symbol
#     btc_ticker = c.get_ticker(btc_symbol)
#     volume_dictionary = dict(btc_ticker['volume'])
#     float(volume_dictionary['USD'])
#
#
# def init_client():
#     global client
#     client = Client('account-2BvOkOzJLMs5x7IMT1Lp', '2WrNQYdLUfs7i64bXAuj218xsdb2')
#     return client





######### GUI


# def center(toplevel):
#     window_width = toplevel.winfo_reqwidth()
#     window_height = toplevel.winfo_reqheight()
#     position_right = int(toplevel.winfo_screenwidth() / 2 - window_width / 2)
#     position_down = int(toplevel.winfo_screenheight() / 2 - window_height / 2)
#     toplevel.geometry("+{}+{}".format(position_right, position_down))
#
#
# def render_input_label(window, label, user_entry, row_index, col_index):
#     label.pack(side=LEFT)
#     label.grid(row=row_index, column=col_index, pady=2, sticky=W)
#     globals()[user_entry] = Entry(window)
#     globals()[user_entry].pack(side=RIGHT)
#     globals()[user_entry].grid(row=row_index, column=col_index + 1, pady=2, padx=8, sticky=W)
#     # globals()[user_entry].insert(0, row_index)
#     globals()[user_entry].config(highlightbackground='black')
#
#
# def render_window():
#     window_dimensions = '370x300'
#     window = Tk()
#     window.title("BTC Day Trader")
#     window.geometry(window_dimensions)
#     window.columnconfigure(0, weight=1)
#     return window
#
#
# def render_btc_price_label(window):
#     global btc_price_label
#
#     btc_price_label = Label(window, text='BTC Price: ')
#     btc_price_label.pack(fill=X)
#     # btc_price_label.pack(side=LEFT)
#     btc_price_label.grid(sticky=W, columnspan=2, pady=15)
#
#
# def render_gain_loss_label(window):
#     global gain_loss_label
#
#     gain_loss_label = Label(window, text='Total Gain/Loss: ')
#     gain_loss_label.pack(side=RIGHT, expand=1)
#     gain_loss_label.grid(sticky=E, columnspan=2, pady=15)
#
#
# def render_run_button(window):
#     run_button = Button(window, text="Run", command=run)
#     run_button.pack()
#     run_button.grid(row=7, column=2, pady=6, sticky=E)
#
#
# def render_stop_button(window):
#     stop_button = Button(window, text="Stop", command=stop)
#     stop_button.pack()
#     stop_button.grid(row=7, column=0, pady=6, sticky=W)
#
#
# def draw_gui():
#     global btc_price_label
#     global user_failsafe_price
#     global budget_entry
#     global set_aside_amt_entry
#     global limit_buy_entry
#     global stop_price_entry
#     global failsafe_price_entry
#     global max_loss_entry
#
#     window = render_window()
#     render_btc_price_label(window)
#     render_gain_loss_label(window)
#     center(window)
#
#     budget_row_index = 1
#     set_aside_row_index = 2
#     limit_buy_row_index = 3
#     stop_price_row_index = 4
#     max_loss_row_index = 5
#     failsafe_row_index = 6
#
#     budget_col_index = 0
#     set_aside_col_index = 0
#     limit_buy_col_index = 0
#     stop_price_col_index = 0
#     max_loss_col_index = 0
#     failsafe_col_index = 0
#
#     budget_label = Label(window, text='Budget: ')
#     set_aside_amt_label = Label(window, text='Set Aside: ')
#     stop_price_label = Label(window, text='Stop Price: ')
#     limit_buy_label = Label(window, text='Entry Price: ')
#     max_loss_label = Label(window, text='Max Loss: ')
#     failsafe_price_label = Label(window, text='Failsafe Price: ')
#
#     render_input_label(window, budget_label, 'budget_entry', budget_row_index, budget_col_index)
#     render_input_label(window, set_aside_amt_label, 'set_aside_amt_entry', set_aside_row_index, set_aside_col_index)
#     render_input_label(window, limit_buy_label, 'limit_buy_entry', limit_buy_row_index, limit_buy_col_index)
#     render_input_label(window, stop_price_label, 'stop_price_entry', stop_price_row_index, stop_price_col_index)
#     render_input_label(window, max_loss_label, 'max_loss_entry', max_loss_row_index, max_loss_col_index)
#     render_input_label(window, failsafe_price_label, 'failsafe_price_entry', failsafe_row_index, failsafe_col_index)
#
#     render_run_button(window)
#     render_stop_button(window)
#
#     return window
#
#
# def refresh_price():
#     global btc_price_label
#     global btc_symbol
#     btc_price_label.configure(text='BTC Price: $' + str(tracker.get_current_bid_price(btc_symbol)))
#     root.after(4000, refresh_price)


#############



# draw_gui (old)

### original labels
# global budget_label_text
# global set_aside_label_text
# global stop_price_label_text
# global target_buy_price_label_text
# global max_loss_label_text
# global failsafe_price_label_text

# global btc_price_label
# global budget_entry
# global set_aside_amt_entry
# global limit_buy_entry
# global stop_price_entry
# global failsafe_price_entry
# global max_loss_entry

# budget_row_index = 1
# set_aside_row_index = 2
# limit_buy_row_index = 3
# stop_price_row_index = 4
# max_loss_row_index = 5
# failsafe_row_index = 6
#
# budget_col_index = 0
# set_aside_col_index = 0
# limit_buy_col_index = 0
# stop_price_col_index = 0
# max_loss_col_index = 0
# failsafe_col_index = 0

### original labels
# budget_label = Label(window, text=budget_label_text)
# set_aside_amt_label = Label(window, text=set_aside_label_text)
# stop_price_label = Label(window, text=stop_price_label_text)
# limit_buy_label = Label(window, text=target_buy_price_label_text)
# max_loss_label = Label(window, text=max_loss_label_text)
# failsafe_price_label = Label(window, text=failsafe_price_label_text)

### old labels
# render_input_label(window, budget_label, 'budget_entry', budget_row_index, budget_col_index)
# render_input_label(window, set_aside_amt_label, 'set_aside_amt_entry', set_aside_row_index, set_aside_col_index)
# render_input_label(window, limit_buy_label, 'limit_buy_entry', limit_buy_row_index, limit_buy_col_index)
# render_input_label(window, stop_price_label, 'stop_price_entry', stop_price_row_index, stop_price_col_index)
# render_input_label(window, max_loss_label, 'max_loss_entry', max_loss_row_index, max_loss_col_index)
# render_input_label(window, failsafe_price_label, 'failsafe_price_entry', failsafe_row_index, failsafe_col_index)


# def run():
#     global user_initial_dollar_balance
#     global user_set_aside
#     global user_stop_limit_price
#     global user_limit_buy_price
#     global user_max_loss
#     global user_failsafe_price
#     global user_stop_price
#     global buy_order
#     global buy_order_made
#     global sell_order
#     global order_id_iterator
#     global break_even_stop
#     global stop_limit_order
#     global latest_order_id
#     global break_even_stop_made
#     global sell_order_made
#     global total_loss
#     global total_gain
#     global btc_symbol
#
#     populate_user_values()
#     calculate_gain_and_loss()
#
#     buy_order_id_prefix = 'limit-buy-order-'
#     break_even_stop_id_prefix = 'break-even-stop-'
#
#     if should_run: # is True and user_initial_dollar_balance > 0:
#         while True:
#             purchase_quantity = '%.5f' % (user_initial_dollar_balance / tracker.get_current_bid_price(btc_symbol))
#             sell_price = user_limit_buy_price + 150  # $9 profit if sold
#
#             # check the price and make sure no purchase has been made yet, then buy
#             if buy_order_made is False:
#                 buy_order_id = buy_order_id_prefix + str(order_id_iterator)
#                 buy_order = create_limit_buy_order(buy_order_id, purchase_quantity)
#
#             time.sleep(3)
#
#             # if the buy order has been filled, then submit sell order for higher price
#             try:
#                 if order_filled(buy_order) and sell_order_made is False:
#                     print("Buy status: Filled")
#
#                     # break even stop limit
#                     if should_place_break_even_stop():
#                         break_even_stop_id = break_even_stop_id_prefix + str(order_id_iterator)
#                         break_even_stop = create_break_even_stop_limit(break_even_stop_id, purchase_quantity)
#
#                     # submit sell order once buy has been filled
#                     sell_order_id = 'limit-sell' + str(order_id_iterator)
#                     sell_order = create_limit_sell_order(sell_order_id, sell_price, purchase_quantity)
#
#                     # submit stop limit order
#                     stop_limit_id = 'stop-limit-order' + str(order_id_iterator)
#                     stop_limit_order = create_stop_loss_below_buy_price(stop_limit_id, purchase_quantity)
#
#                     if order_filled(stop_limit_order):
#                         c.cancel_order(sell_order.order_id)
#
#                     if order_filled(sell_order):
#                         c.cancel_order(stop_limit_order.order_id)
#                 else:
#                     print("Buy status: Not filled")
#             except NameError:
#                 print("Order undefined. Skipping sell")
#             except TypeError:
#                 print("Status undefined. Skipping again")
#
#             calculate_gain_and_loss()
#             latest_order_id = order_id_iterator
#             order_id_iterator += 1
#
#             time.sleep(3)


#
# def should_place_break_even_stop():
#     global user_buy_price
#     global btc_symbol
#     return tracker.get_current_bid_price(btc_symbol) - user_buy_price > 25
#
#
# def calculate_gain(new_dollar_balance):
#     global total_loss
#     global user_initial_dollar_balance
#     global total_gain
#
#     gain = new_dollar_balance - user_initial_dollar_balance
#     total_gain += gain
#     if total_loss - gain >= 0:
#         total_loss -= gain
#     else:
#         total_loss = 0
#
#
# def calculate_loss(new_dollar_balance):
#     global total_gain
#     global user_max_loss
#     global user_initial_dollar_balance
#     global total_loss
#
#     loss = user_initial_dollar_balance - new_dollar_balance
#     total_loss += loss
#     if total_gain - loss >= 0:
#         total_gain -= loss
#     else:
#         total_gain = 0
#     if total_loss >= user_max_loss:
#         sys.exit(0)
#
#
# def calculate_gain_and_loss():
#     global total_loss
#     global total_gain
#     global user_initial_dollar_balance
#     global btc_symbol
#
#     lowest_dollar_balance_allowed = user_initial_dollar_balance - user_max_loss
#     quantity_btc_purchased = user_initial_dollar_balance / tracker.get_current_bid_price(btc_symbol)
#     lowest_btc_price_allowed = lowest_dollar_balance_allowed / quantity_btc_purchased
#     new_dollar_balance = quantity_btc_purchased * tracker.get_current_bid_price(btc_symbol)
#
#     if user_initial_dollar_balance < new_dollar_balance:
#         calculate_gain(new_dollar_balance)
#     elif user_initial_dollar_balance > new_dollar_balance:
#         calculate_loss(new_dollar_balance)
#     else:
#         total_loss, total_gain = 0, 0


# def populate_user_values():
    # global user_initial_dollar_balance
    # global user_set_aside
    # global user_stop_limit_price
    # global user_limit_buy_price
    # global user_max_loss
    # global user_failsafe_price
    # global user_stop_price

    # user_initial_dollar_balance = float(interface.budget_entry.get())
    # user_set_aside = float(interface.set_aside_amt_entry.get())
    # user_limit_buy_price = float(interface.limit_buy_entry.get())
    # user_max_loss = float(interface.max_loss_entry.get())
    # user_failsafe_price = float(interface.failsafe_price_entry.get())
    # user_stop_price = float(interface.stop_price_entry.get())



##### WEBSOCKETS

# def connect():
#     # payload = {
#     #     'request': '/v1/order/events',
#     #     'nonce': get_nonce()
#     # }
#     # payload = str.encode(json.dumps(payload))
#     # b64 = base64.b64encode(payload)
#     # signature = hmac.new(str.encode('2WrNQYdLUfs7i64bXAuj218xsdb2'), b64, hashlib.sha384).hexdigest()
#
#     websocket.enableTrace(True)
#     # gets BTC price
#     ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&bids=true",
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close)
#
#     # gets active orders
#     # ws = websocket.WebSocketApp("wss://api.gemini.com/v1/order/events?symbolFilter=btcusd",
#     #                             on_message=on_message,
#     #                             header={
#     #                                 'X-GEMINI-PAYLOAD': b64.decode(),
#     #                                 'X-GEMINI-APIKEY': 'account-2BvOkOzJLMs5x7IMT1Lp',
#     #                                 'X-GEMINI-SIGNATURE': signature
#     #                             })
#     # ws.on_open = on_open
#     ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

####stop limit works
# stop_limit_id = 'stop-limit-' + str(order_id_iterator)
# stop_price = 9800
# q = '%.8f' % (10 / 9800)
# stop_limit_order = client.new_limit_order('client-id', btc_symbol, q, 9800, 'sell', stop_price)



# account_balance = [bal for bal in client.get_balance() if bal['currency'] == 'USD']
    # usd_account_balance = account_balance[0]['amount']
    # enough_funds = user_initial_dollar_balance < float(usd_account_balance)
    # return buy_order_placed() is False # and enough_funds  # and fourmovingaverage.is_moving_up()