import pandas as pd

def calculate_vwap(df):
    df['Typical Price'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['TPV'] = df['Typical Price'] * df['Volume']
    
    df['Cumulative TPV'] = df['TPV'].cumsum()
    df['Cumulative Volume'] = df['Volume'].cumsum()
    
    df['VWAP'] = df['Cumulative TPV'] / df['Cumulative Volume']
    
    return df

def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

def calculate_macd(df):
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()
    
    df['MACD'] = df['EMA12'] - df['EMA26']
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    
    return df


def calculate_moving_averages(df):
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    
    return df