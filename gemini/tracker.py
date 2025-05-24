# import gemini
# from gemini.classes.Order import Order
from gemini.classes.Order import Order
from gemini.restclient import Client


with open('../../gem.txt', "r") as text_file:
    text_string = text_file.readlines()
    public_key = text_string[0].split(
        ':')[1].rstrip()  # public key with heartbeat
    api_secret = text_string[1].split(
        ':')[1].rstrip()  # API secret with heartbeat

client = Client(public_key, api_secret, False)


def get_current_bid_price(symbol):
    ticker = client.get_ticker(symbol)
    if ticker:
        return float(ticker['bid'])


def get_current_ask_price(symbol):
    ticker = client.get_ticker(symbol)
    if ticker:
        return round(float(ticker['ask']), 2)


def get_order_status(status_id):
    try:
        response = client.get_order_status(status_id)
    except:
        response = None
        pass
    if response:
        return Order(response)


def send_heartbeat():
    client.send_heartbeat()


def get_last_btc_order(symbol):
    ticker = client.get_ticker(symbol)
    if ticker:
        return float(ticker['last'])


def get_usd_volume(symbol):
    ticker = client.get_ticker(symbol)
    if ticker:
        volume_dictionary = dict(ticker['volume'])
        if volume_dictionary:
            return float(volume_dictionary['USD'])


def get_btc_volume(symbol):
    ticker = client.get_ticker(symbol)
    if ticker:
        volume_dictionary = dict(ticker['volume'])
        if volume_dictionary:
            return float(volume_dictionary['USD'])
