def high_of_day_breakout(df):
    high_of_day = df['High'].max()
    current_price = df['Close'].iloc[-1]
    
    return current_price >= high_of_day



def vwap_breakout(df):
    current_price = df['Close'].iloc[-1]
    current_vwap = df['VWAP'].iloc[-1]
    
    return current_price > current_vwap




def volume_spike(df):
    avg_volume = df['Volume'].rolling(window=20).mean().iloc[-1]
    current_volume = df['Volume'].iloc[-1]
    
    return current_volume > 2 * avg_volume



def rsi_bullish(df):
    return df['RSI'].iloc[-1] > 60




def macd_bullish(df):
    macd = df['MACD']
    signal = df['Signal']
    
    return macd.iloc[-2] < signal.iloc[-2] and macd.iloc[-1] > signal.iloc[-1]






def ma_crossover(df):
    return df['MA20'].iloc[-1] > df['MA50'].iloc[-1]








def generate_signal(df):
    score = 0
    details = {}

    

    if high_of_day_breakout(df):
        details['High Breakout'] = True
        score += 1
    else:
        details['High Breakout'] = False

    if vwap_breakout(df):
        details['VWAP Break'] = True
        score += 1
    else:
        details['VWAP Break'] = False

    if volume_spike(df):
        details['Volume Spike'] = True
        score += 1
    else:
        details['Volume Spike'] = False

    if rsi_bullish(df):
        details['RSI Bullish'] = True
        score += 1
    else:
        details['RSI Bullish'] = False

    if macd_bullish(df):
        details['MACD Cross'] = True
        score += 1
    else:
        details['MACD Cross'] = False

    if ma_crossover(df):
        details['MA Trend Up'] = True
        score += 1
    else:
        details['MA Trend Up'] = False

    if score >= 4:
        signal = "STRONG BUY"
    elif score >= 3:
        signal = "BUY"
    else:
        signal = "NO SIGNAL"
        
    return {
        "signal": signal,
        "score": score,
        "details": details
    }




def opening_range_breakout(df):
    opening_range = df.iloc[:15]

    opening_high = opening_range['High'].max()
    opening_low = opening_range['Low'].min()

    current_price = df['Close'].iloc[-1]

    if current_price > opening_high:
        return "BUY"
    elif current_price < opening_low:
        return "SELL"
    else:
        return "NO"