import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']

print(f'Cotação do dólar: R${cotacao_dolar}')
print(f'Cotação do euro: R${cotacao_euro}')
print(f'Cotação do bitcoin: R${cotacao_bitcoin}')