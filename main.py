import requests
import time


def cotizacion_en_euros(moneda):
    url = "https://api.coinbase.com/v2/exchange-rates?currency=%s" % moneda
    r = requests.get()
    valor = r.json()["data"]["rates"]["EUR"]
    print "{%s}: {%s}" % (moneda, valor)


while(True):
    cotizacion_en_euros('BTC')
    cotizacion_en_euros('ETH')
    time.sleep(5)
