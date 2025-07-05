import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo"
r = requests.get(url)
data = r.json()

df = pd.DataFrame.from_dict(data["Weekly Time Series"], orient="index")
df.columns = [c.split(". ")[-1] for c in df.columns]
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df["close"] = pd.to_numeric(df["close"])

short_window = 5
long_window = 20
df["sma_short"] = df["close"].rolling(window=short_window).mean()
df["sma_long"] = df["close"].rolling(window=long_window).mean()
df["signal"] = np.where(df["sma_short"] > df["sma_long"], 1, 0)
df["position"] = df["signal"].diff()

buy = df[df["position"] == 1]
sell = df[df["position"] == -1]

plt.style.use("classic")
plt.figure(figsize=(14, 6))
plt.plot(df.index, df["close"], label="Close price", color="blue")
plt.plot(df.index, df["sma_short"], label="SMA (10)", color="orange")
plt.plot(df.index, df["sma_long"], label="SMA (50)", color="green")
plt.scatter(buy.index, buy["close"], marker="^", color="limegreen", edgecolors="black", s=120, zorder=5, label="Buy")
plt.scatter(sell.index, sell["close"], marker="v", color="red", edgecolors="black", s=120, zorder=5, label="Sell")

plt.title("SMA strategy buy/sell signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

trades = []

for i in range(len(df)):
    row = df.iloc[i]
    
    if row["position"] == 1:
        position = {"buy_price": row["close"], "buy_date": df.index[i]}
    
    elif row["position"] == -1:
        sell_price = row["close"]
        profit = sell_price - position["buy_price"]
        
        trades.append({"profit": profit})

total_profit = sum(trade["profit"] for trade in trades)
print(f"Total profit: {total_profit:.2f}")
