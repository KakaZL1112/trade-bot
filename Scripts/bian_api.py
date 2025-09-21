from binance.client import Client

class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
    
    def get_balance(self, asset='USDT'):
        info = self.client.get_asset_balance(asset=asset)
        return info

    def place_order(self, symbol, side, quantity, order_type='MARKET'):
        order = self.client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )
        return order