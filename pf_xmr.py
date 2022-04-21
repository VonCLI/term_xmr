# install:  pip3 install pycoingecko
# API documentation: https://github.com/man-c/pycoingecko

import time
import os

from  pycoingecko import CoinGeckoAPI
from termcolor import cprint
from datetime import datetime


cg = CoinGeckoAPI()
pf = float(input("Amount of $XMR: "))

def monero_price():

    now = datetime.now()
    cprint(f"{now:%Y-%m-%d %H:%M:%S}", "red")

    xmrus = cg.get_coins_markets(ids='monero', vs_currency='usd',include_market_cap='True')
    xmrbtc = cg.get_coins_markets(ids='monero', vs_currency='btc')
    xmreur = cg.get_coins_markets(ids='monero', vs_currency='eur')

    for i in xmrus:

        monero = i['name']
        price_us = i['current_price']
        mkt_cap = i['market_cap']
        mcr= i['market_cap_rank']
        circ_sup= i['circulating_supply']
        dayvol= i['total_volume']
        high= i['high_24h']
        low= i['low_24h']

    for i in xmrbtc:

        price_btc = i['current_price']

    for i in xmreur:

        price_eur = i['current_price']

    print(f"""
    {monero}: {price_us} us$ | {price_btc} ₿ | {price_eur} €
    Market cap: {mkt_cap} us$
    Rank: {mcr}
    Supply: {circ_sup}
    Volume/24h: {dayvol} us$
    High/24h: {high} us$
    Low/24h: {low} us$
    """)

def major():
    btc = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')
    eth = cg.get_coins_markets(ids='ethereum', vs_currency='usd')

    for i in btc:
        bitcoin = i['name']
        btcprice = i['current_price']
    for i in eth:
        ethereum = i['name']
        ethprice = i['current_price']
        
    print(f"""    
    {bitcoin}:{btcprice} us$
    {ethereum}: {ethprice} us$
    """)


def portfolio():
    xmrus = cg.get_coins_markets(ids='monero', vs_currency='usd',include_market_cap='True')
    xmrbtc = cg.get_coins_markets(ids='monero', vs_currency='btc')
    xmreur = cg.get_coins_markets(ids='monero', vs_currency='eur')
    
    for i in xmrus:
        price_us = i['current_price']
    for i in xmrbtc:
        price_btc = i['current_price']
    for i in xmreur:
        price_eur = i['current_price']
    
    usd = pf * float(price_us)
    btc = pf * float(price_btc)
    eur = pf * float(price_eur)

    print(f"""
    Value of your portfolio: {usd:.2f} $us | {btc:.8f} ₿ | {eur:.2f} €
    """)


def clear():
    os.system('clear')

while True:
    try:
        monero_price()
        major()
        portfolio()
        time.sleep(30)    #results updated each 30 seconds.
        clear()
    except KeyboardInterrupt:
        cprint(" Exiting ...", "magenta")
        exit(0)
