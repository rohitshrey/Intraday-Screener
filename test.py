from data_fetcher import fetch_stock_data
from indicators import *
from strategy import generate_signal

df = fetch_stock_data("RELIANCE.NS")

df = calculate_vwap(df)
df = calculate_rsi(df)
df = calculate_macd(df)
df = calculate_moving_averages(df)

signal = generate_signal(df)

print("Signal:", signal)