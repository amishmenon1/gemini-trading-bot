from tkinter.ttk import Label, Entry
import gemini.tracker as tracker
from tkinter import *
# import gemini.trader as trader

# budget_label_text = 'Budget: '
# set_aside_label_text = 'Set Aside: '
# stop_price_label_text = 'Stop Price: '
# target_buy_price_label_text = 'Entry Price: '
# max_loss_label_text = 'Max Loss: '
# failsafe_price_label_text = 'Failsafe Price: '

token_symbol_input_label_text = 'Symbol (\'ethusd\',\'btcusd\'...): '
initial_balance_label_text = 'USD Amount: '
target_buy_price_label_text = 'Entry Price: '
target_sell_price1_label_text = 'Sell Price 1: '
target_sell_price2_label_text = 'Sell Price 2: '
target_sell_price3_label_text = 'Sell Price 3: '
target_sell_price4_label_text = 'Sell Price 4: '
target_sell_price5_label_text = 'Sell Price 5: '
target_stop_limit_price_label_text = 'Stop Limit Price: '
speak_label_text = '[Mac Only] Sound On? (y/n)'

# old labels
# budget_entry = None
# set_aside_amt_entry = None
# stop_price_entry = None
# limit_buy_entry = None
# max_loss_entry = None
# failsafe_price_entry = None

token_symbol_input_label_entry = ''
initial_balance_entry = None
target_buy_price_entry = None
target_sell_price1_entry = None
target_sell_price2_entry = None
target_sell_price3_entry = None
target_sell_price4_entry = None
target_sell_price5_entry = None
target_stop_limit_price_entry = None
speak_label_entry = None


token_price_label = None
gain_loss_label = None
symbol_label = None


def center(toplevel):
    window_width = toplevel.winfo_reqwidth()
    window_height = toplevel.winfo_reqheight()
    position_right = int(toplevel.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(toplevel.winfo_screenheight() / 2 - window_height / 2)
    toplevel.geometry("+{}+{}".format(position_right, position_down))


def render_input_label(window, label, user_entry, row_index, col_index):
    # Mac feature only
    # label.pack(side=LEFT)
    label.grid(row=row_index, column=col_index, pady=2, sticky=W)
    globals()[user_entry] = Entry(window)
    # Mac feature only
    # globals()[user_entry].pack(side=RIGHT)
    globals()[user_entry].grid(row=row_index,
                               column=col_index + 1, pady=2, padx=8, sticky=W)
    # globals()[user_entry].insert(0, row_index)
    globals()[user_entry].config(highlightbackground='black')


def render_window():
    window_dimensions = '420x340'
    window = Tk()
    window.title("ETH Day Trader")
    window.geometry(window_dimensions)
    window.columnconfigure(0, weight=1)
    return window


def render_btc_price_label(window):
    global token_price_label
    global symbol_label

    price_label_text = 'ETH Price: ${}'.format(
        str(tracker.get_current_bid_price('ethusd')))
    token_price_label = Label(window, text='ETH Price: ')
    # Mac feature only
    # btc_price_label.pack(fill=X)
    token_price_label.grid(sticky=W, columnspan=2, pady=15)
    token_price_label.configure(text=price_label_text)


def render_gain_loss_label(window):
    global gain_loss_label

    gain_loss_label = Label(window, text='Total Gain/Loss: ')
    # Mac feature only
    # gain_loss_label.pack(side=RIGHT, expand=1)
    gain_loss_label.grid(sticky=E, columnspan=2, pady=15)


def render_run_button(row_index, window, command):
    run_button = Button(window, text="Run", command=command)
    # Mac feature only
    # run_button.pack()
    run_button.grid(row=row_index, column=2, pady=6, sticky=E)


def render_stop_button(row_index, window, command):
    stop_button = Button(window, text="Stop", command=command)
    # Mac feature only
    # stop_button.pack()
    stop_button.grid(row=row_index, column=0, pady=6, sticky=W)


def draw_gui(run_command, stop_command):
    # new labels
    global target_buy_price_label_text
    global target_sell_price1_label_text
    global target_sell_price2_label_text
    global target_sell_price3_label_text
    global target_sell_price4_label_text
    global target_stop_limit_price_label_text
    global initial_balance_label_text
    global token_symbol_input_label_text
    global speak_label_text

    window = render_window()
    render_btc_price_label(window)
    render_gain_loss_label(window)
    center(window)

    token_symbol_row_index = 1
    initial_balance_row_index = 2
    limit_buy_row_index = 3
    sell_price1_row_index = 4
    # sell_price2_row_index = 4
    # sell_price3_row_index = 5
    # sell_price4_row_index = 6
    # sell_price5_row_index = 7
    stop_limit_row_index = 5
    speak_row_index = 6
    last_row_index = 7
    label_col_index = 0

    # new labels
    token_symbol_input_label = Label(
        window, text=token_symbol_input_label_text)
    initial_balance_label = Label(window, text=initial_balance_label_text)
    limit_buy_label = Label(window, text=target_buy_price_label_text)
    sell_price1_label = Label(window, text=target_sell_price1_label_text)
    # sell_price2_label = Label(window, text=target_sell_price2_label_text)
    # sell_price3_label = Label(window, text=target_sell_price3_label_text)
    # sell_price4_label = Label(window, text=target_sell_price4_label_text)
    # sell_price5_label = Label(window, text=target_sell_price5_label_text)
    stop_limit_label = Label(window, text=target_stop_limit_price_label_text)
    speak_label = Label(window, text=speak_label_text)

    # new labels
    render_input_label(window, token_symbol_input_label,
                       'token_symbol_input_label_entry', token_symbol_row_index, label_col_index)
    render_input_label(window, initial_balance_label, 'initial_balance_entry',
                       initial_balance_row_index, label_col_index)
    render_input_label(window, limit_buy_label, 'target_buy_price_entry',
                       limit_buy_row_index, label_col_index)
    render_input_label(window, sell_price1_label, 'target_sell_price1_entry',
                       sell_price1_row_index, label_col_index)
    # render_input_label(window, sell_price2_label, 'target_sell_price2_entry', sell_price2_row_index, label_col_index)
    # render_input_label(window, sell_price3_label, 'target_sell_price3_entry', sell_price3_row_index, label_col_index)
    # render_input_label(window, sell_price4_label, 'target_sell_price4_entry', sell_price4_row_index, label_col_index)
    # render_input_label(window, sell_price5_label, 'target_sell_price5_entry', sell_price5_row_index, label_col_index)
    render_input_label(window, stop_limit_label, 'target_stop_limit_price_entry',
                       stop_limit_row_index, label_col_index)
    render_input_label(window, speak_label, 'speak_label_entry',
                       speak_row_index, label_col_index)

    render_run_button(last_row_index, window, run_command)
    render_stop_button(last_row_index, window, stop_command)

    return window


def refresh_price(root, symbol):
    global token_price_label
    price_label_text = 'CHILLGUYUSD Price: ${}'.format(
        str(tracker.get_current_bid_price('chillguyusd')))
    try:
        token_price_label.configure(text=price_label_text)
        root.after(4500, refresh_price, root, symbol)
    except Exception as e:
        pass
