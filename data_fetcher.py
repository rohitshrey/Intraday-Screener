def fetch_stock_data(symbol):
    import yfinance as yf

    try:
        stock = yf.Ticker(symbol)
        df = stock.history(interval="1m", period="1d")

        if df.empty:
            return None

        df.reset_index(inplace=True)
        return df

    except Exception:
        return None