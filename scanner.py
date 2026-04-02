from data_fetcher import fetch_stock_data
from indicators import *
from strategy import *
from nifty500 import NIFTY_100

import pandas as pd
import time

from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()


# ===== COLOR FUNCTIONS =====
def get_signal_color(signal):
    if signal == "BUY":
        return "bold black on green"
    elif signal == "SELL":
        return "bold white on red"
    else:
        return "white"


def get_arrow(signal):
    if signal == "BUY":
        return "[green]↑[/green]"
    elif signal == "SELL":
        return "[red]↓[/red]"
    else:
        return "-"


def get_rsi_color(rsi):
    if rsi > 60:
        return "green"
    elif rsi < 40:
        return "red"
    else:
        return "white"


# ===== TABLE BUILDER =====
def build_table(results):
    table = Table(title="📊 LIVE STOCK SCANNER", expand=True, padding=(0, 2))

    table.add_column("Stock")
    table.add_column("Price")
    table.add_column("RSI")
    table.add_column("VWAP")
    table.add_column("Score")
    table.add_column("ORB")
    table.add_column("Trend")
    table.add_column("Signal")

    for row in results:
        signal_color = get_signal_color(row["Signal"])
        arrow = get_arrow(row["Signal"])
        rsi_color = get_rsi_color(row["RSI"])

        table.add_row(
            row["Stock"],
            str(row["Price"]),
            f"[{rsi_color}]{row['RSI']}[/{rsi_color}]",
            str(row["VWAP"]),
            str(row["Score"]),
            row["ORB"],
            arrow,
            f"[{signal_color}]{row['Signal']}[/{signal_color}]"
        )

    return table


# ===== LIVE SCANNER =====
with Live(refresh_per_second=1) as live:
    while True:
        results = []

        for stock in NIFTY_100:
            try:
                df = fetch_stock_data(stock)

                if df is None or len(df) < 50:
                    continue

                # indicators
                df = calculate_vwap(df)
                df = calculate_rsi(df)
                df = calculate_macd(df)
                df = calculate_moving_averages(df)

                # ORB
                orb_signal = opening_range_breakout(df)

                # strategy
                result = generate_signal(df)
                signal = result["signal"]

                # scoring
                score = 0
                if df['Close'].iloc[-1] >= df['High'].max():
                    score += 1
                if df['Close'].iloc[-1] > df['VWAP'].iloc[-1]:
                    score += 1
                if df['Volume'].iloc[-1] > 1.5 * df['Volume'].rolling(20).mean().iloc[-1]:
                    score += 1
                if df['RSI'].iloc[-1] > 60:
                    score += 1
                if df['MACD'].iloc[-1] > df['Signal'].iloc[-1]:
                    score += 1
                if df['MA20'].iloc[-1] > df['MA50'].iloc[-1]:
                    score += 1
                if orb_signal == "BUY":
                    score += 2

                # filter
                if score >= 2:
                    results.append({
                        "Stock": stock.replace(".NS", ""),
                        "Price": round(df['Close'].iloc[-1], 2),
                        "RSI": round(df['RSI'].iloc[-1], 2),
                        "VWAP": round(df['VWAP'].iloc[-1], 2),
                        "Score": score,
                        "ORB": orb_signal,
                        "Signal": signal
                    })

            except:
                continue

        # sort strongest first
        results = sorted(results, key=lambda x: (x["Score"], x["RSI"]), reverse=True)

        # build UI
        table = build_table(results)

        # update screen
        live.update(table)

        time.sleep(5)

  