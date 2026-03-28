import requests
import pandas as pd

def get_stock_data(stock_id):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_id}.TW"

    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)

    data = res.json()

    result = data['chart']['result'][0]
    quote = result['indicators']['quote'][0]

    df = pd.DataFrame({
        "close": quote['close'],
        "high": quote['high'],
        "low": quote['low']
    })

    return df.dropna()
