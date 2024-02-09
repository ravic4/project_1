
"""
Ravi's Code: 
All 'Strings' indicate the different steps taken to write my code. 
All # commented lines indicate a coding check, or notes for developer explicitly for a specific line (or lines) of code. 
"""

"""
All imports are as follows: 
"""
import pandas as pd 
from pathlib import Path 
from dotenv import load_dotenv 
import os
import matplotlib.pyplot as plt
import hvplot.pandas
import numpy as np
import alpaca_trade_api as tradeapi
import panel as pn
"""
Loading in my environments: dotenv and 
"""
load_dotenv("api.env")
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

"""
Setting up my Alpaca API Keys and creating the Alpaca API object: 
"""
apikey = os.getenv("ALPACA_API_KEY")
secret = os.getenv("ALPACA_SECRET_KEY")

api = tradeapi.REST(
    apikey, secret,
    api_version = "v2"
)
# print(api) print checks out. 

"""
Calling in my securities and setting up a mock portfolio 
"""
assets = ["ARKK","SPY"]
portfolio = [200,100]


"""
Getting my ticker information from Alpaca API 
"""
timeframe = "1Day"
start_date = pd.Timestamp("2018-12-31", tz = "America/New_York").isoformat()
end_date = pd.Timestamp("2023-12-29", tz = "America/New_York").isoformat()

"""
Getting my ticker information for the funds: ARKK and SPY 
"""
df_assets = api.get_bars(
    assets,
    timeframe,
    start = start_date,
    end = end_date
).df 
# print(df_assets) printed out successfully 

df_pivot = df_assets.pivot(columns = 'symbol', values = 'close')
# print(df_pivot) printed out successfully 

df_portfolio = pd.DataFrame(
    {
        'symbol':assets,
        'weight':portfolio
    }
)
# print(df_portfolio) printed out successfully 
df_pivot = df_pivot.reset_index()
#reset the index to create portfolio 

# df_pivot = df_pivot.set_index(["ARKK","SPY"])
# print(df_pivot)
# print(df_pivot.columns) had to double check heads 
df_pivot["ARKK invest"] = df_portfolio["weight"][0] * df_pivot["ARKK"]
df_pivot["SPY invest"] = df_portfolio["weight"][1] * df_pivot["SPY"]

# df_pivot.set_index("timestamp", inplace = True)
# print(df_pivot)


# df_pivot_sum = df_pivot["ARKK invest"] + df_pivot["SPY invest"]
arkk_portfolio = df_pivot["ARKK invest"]
spy_portfolio = df_pivot["SPY invest"]

merged = pd.DataFrame((arkk_portfolio + spy_portfolio))
df_pivot["Portfolio"] = merged
# print(df_pivot)

percent_changed = []
first_position = df_pivot["Portfolio"][0]
for change in df_pivot["Portfolio"]:
    percent_change = ((change/first_position)-1)
    percent_changed.append(percent_change)

df_pivot["Percent Change"] = percent_changed
# print(df_pivot)

df_plot = df_pivot.hvplot.line(x = 'timestamp', y = ['Percent Change'])
df_plot






