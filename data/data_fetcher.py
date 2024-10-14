# data_fetcher.py

import alpaca_trade_api as tradeapi
import pandas as pd
import time


def initialize_api(api_key, secret_key, base_url):
    """初始化 Alpaca API"""
    return tradeapi.REST(api_key, secret_key, base_url, api_version='v2')

def get_account_info(api):
    try:
        account = api.get_account()
        return account
    except Exception as e:
        print(f"Error occurred while fetching account information: {e}")
        return None

def get_historical_data(api, symbol, start_date, end_date):
    """获取历史市场数据"""
    try:
        barset = api.get_barset(symbol, 'day', start=start_date, end=end_date)
        return barset[symbol]
    except Exception as e:
        print(f"Error occurred while fetching historical data for {symbol}: {e}")
        return None



def fetch_historical_data(api, symbols, start_date, end_date, batch_size=5):
    """从 Alpaca API 获取历史日线数据并保存到 CSV"""

    all_data = pd.DataFrame()  # 准备一个空的 DataFrame 来存储所有数据

    for i in range(0, len(symbols), batch_size):
        batch_symbols = symbols[i:i + batch_size]  # 每次获取的股票代码批次

        # 尝试获取这批股票的历史日线数据
        try:
            for symbol in batch_symbols:
                # 使用 get_bars 获取数据，时间间隔设置为 '1Day'
                bars = api.get_bars(symbol, timeframe='1Day', start=start_date, end=end_date).df

                # 从索引中提取时间戳并添加股票代码
                bars['timestamp'] = bars.index
                bars['symbol'] = symbol  # 添加股票代码

                # 选择所需的列
                bars = bars[['symbol', 'open', 'high', 'low', 'close', 'volume', 'timestamp']]

                # 打印以检查数据列
                print(f"Fetched data for {symbol}: {bars.shape[0]} rows")

                # 追加到总 DataFrame
                all_data = pd.concat([all_data, bars], axis=0)

        except Exception as e:
            print(f"Error fetching data for {batch_symbols}: {e}")

    return all_data


def save_to_csv(data, filename='data/nasdaq_stocks_data.csv'):
    try:
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
