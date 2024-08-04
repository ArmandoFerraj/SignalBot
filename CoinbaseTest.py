import config
import ccxt

# Initialize the Coinbase exchange
coinbase = ccxt.coinbase({
    'apiKey': config.api_key,
    'secret': config.api_secret,
    'enableRateLimit': True,
    'options': {
        'createMarketBuyOrderRequiresPrice': False,
    },
})


symbol = 'BTC/USD'
usd_amount = .00001  # The amount of USD to spend

# sell_order = coinbase.create_market_sell_order(symbol, usd_amount)
# print(sell_order)

# balance = coinbase.fetch_balance()
# print(balance)


# def get_unit():
#     balance = coinbase.fetch_balance()
#     usd_balance = balance['free']['USD']
#     unit = usd_balance * .2
#     return unit

# print(get_unit())
def get_holdings(symbol):
    balance = coinbase.fetch_balance()
    holdings = {currency: amounts for currency, amounts in balance['total'].items()}
    holdings = holdings[symbol]
    return holdings
print(get_holdings('BTC'))