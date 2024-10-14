# main.py

from data.data_fetcher import initialize_api, fetch_historical_data,save_to_csv

# 将你的密钥替换到下面的字段中
API_KEY = 'PKA4MUBEEYYI1OX6EKWV'
SECRET_KEY = '10D9eZLusKy17QekU6qa4tcXEHbOfEooSS1mayQp'
BASE_URL = 'https://paper-api.alpaca.markets'  # 用于测试交易的 sandbox 环境

# 时间区间
start_date = '2023-01-01'
end_date = '2023-12-31'

def main():
    """主函数"""
    # 初始化交易 API
    api = initialize_api(API_KEY, SECRET_KEY, BASE_URL)

    # Fetch all active assets
    assets = api.list_assets(status='active')

    # Filter assets to only include those listed on NASDAQ
    nasdaq_assets = [asset.symbol for asset in assets if asset.exchange == 'NASDAQ']

    # 获取股票历史数据
    historical_data = fetch_historical_data(api, nasdaq_assets, start_date, end_date)

    # 展示前几行数据
    print(historical_data.head())

    # 保存到 CSV
    save_to_csv(historical_data)


if __name__ == "__main__":
    main()
