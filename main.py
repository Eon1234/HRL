import alpaca_trade_api as tradeapi

# 将你的密钥替换到下面的字段中
API_KEY = 'PKA4MUBEEYYI1OX6EKWV'
SECRET_KEY = '10D9eZLusKy17QekU6qa4tcXEHbOfEooSS1mayQp'
BASE_URL = 'https://paper-api.alpaca.markets'  # 用于测试交易的 sandbox 环境

# 创建交易 API 对象
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# 示例：获取当前账户信息
account = api.get_account()
print(account)
