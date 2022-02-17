from json import JSONEncoder
import json


class Order:
    order_id = None
    id = None
    symbol = None
    exchange = None
    avg_execution_price = None
    side = None
    tyoe = None
    timestamp = None
    is_live = None
    is_cancelled = None
    is_hidden = None
    was_forced = None
    executed_amount = None
    options = None
    price = None
    original_amount = None
    remaining_amount = None
    timestampms = None

    def __init__(self, api_order):
        self.order_id = api_order['order_id'] if 'order_id' in api_order else None
        self.id = api_order['id'] if 'id' in api_order else None
        self.symbol = api_order['symbol'] if 'symbol' in api_order else None
        self.exchange = api_order['exchange'] if 'exchange' in api_order else None
        self.avg_execution_price = api_order['avg_execution_price'] if 'avg_execution_price' in api_order else None
        self.side = api_order['side'] if 'side' in api_order else None
        self.tyoe = api_order['type'] if 'tyoe' in api_order else None
        self.timestamp = api_order['timestamp'] if 'timestamp' in api_order else None
        self.timestampms = api_order['timestampms'] if 'timestampms' in api_order else None
        self.is_live = api_order['is_live'] if 'is_live' in api_order else None
        self.is_cancelled = api_order['is_cancelled'] if 'is_cancelled' in api_order else None
        self.is_hidden = api_order['is_hidden'] if 'is_hidden' in api_order else None
        self.was_forced = api_order['was_forced'] if 'was_forced' in api_order else None
        self.executed_amount = api_order['executed_amount'] if 'executed_amount' in api_order else None
        self.options = api_order['options'] if 'options' in api_order else None
        self.price = api_order['price'] if 'price' in api_order else None
        self.original_amount = api_order['original_amount'] if 'original_amount' in api_order else None
        self.remaining_amount = api_order['remaining_amount'] if 'remaining_amount' in api_order else None

    def to_string(self):
        return OrderEncoder().encode(self)


class OrderEncoder(JSONEncoder):

    def default(self, order_object):
        if isinstance(order_object, Order):
            return order_object.__dict__

        else:
            return json.JSONEncoder.default(self, order_object)
