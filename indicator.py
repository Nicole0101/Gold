import pandas as pd

# ===== KD 指標 =====
def calculate_kd(df, n=9):
    low_min = df['low'].rolling(window=n).min()
    high_max = df['high'].rolling(window=n).max()

    rsv = (df['close'] - low_min) / (high_max - low_min) * 100

    k = rsv.ewm(com=2).mean()
    d = k.ewm(com=2).mean()

    df['K'] = k
    df['D'] = d
    return df


# ===== 布林通道 =====
def calculate_bollinger(df, n=20):
    df['MA'] = df['close'].rolling(window=n).mean()
    std = df['close'].rolling(window=n).std()

    df['BB_upper'] = df['MA'] + 2 * std
    df['BB_lower'] = df['MA'] - 2 * std

    return df


# ===== 主整合 =====
def add_indicators(df):
    df = calculate_kd(df)
    df = calculate_bollinger(df)
    return df
