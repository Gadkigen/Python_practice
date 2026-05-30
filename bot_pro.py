import ccxt
import time
import pandas as pd
import numpy as np
import json
from datetime import datetime

# ================= BINANCE SETUP =================
exchange = ccxt.binance({
    'apiKey': 'NAbXSaEU2FC6WX0xmoTx3xifVOQtplWCOsQlsEjsdU64B3AIsCTl3e0uPNrU8Fmn',
    'secret': 'ME9F5py83Vj45arAh71s657K6sD5sMmbp8J1DlN1jomtnEn8o5tpx2tHt2wHfrkq',
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'}
})

symbol = 'SOL/USDT'
timeframe = '1m'

risk_usdt = 3
cooldown = 10
max_trades_per_day = 15

paper_trading = True  # 👈 IMPORTANT: start with True

log_file = "pro_trades.json"

trade_count = 0
last_trade_time = 0
day_tracker = datetime.now().date()


# ================= MARKET DATA =================
def get_data():
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=100)
    df = pd.DataFrame(ohlcv, columns=['time','open','high','low','close','volume'])
    return df


# ================= INDICATORS =================
def EMA(series, period):
    return series.ewm(span=period, adjust=False).mean()


def RSI(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def MACD(df):
    ema12 = EMA(df['close'], 12)
    ema26 = EMA(df['close'], 26)
    macd = ema12 - ema26
    signal = EMA(macd, 9)
    return macd, signal


def ATR(df, period=14):
    high_low = df['high'] - df['low']
    high_close = abs(df['high'] - df['close'].shift())
    low_close = abs(df['low'] - df['close'].shift())

    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean()


# ================= SIGNAL ENGINE =================
def get_signal():
    df = get_data()

    df['rsi'] = RSI(df)
    df['ema50'] = EMA(df['close'], 50)
    macd, signal = MACD(df)
    df['macd'] = macd
    df['signal'] = signal

    latest = df.iloc[-1]

    rsi = latest['rsi']
    price = latest['close']
    ema50 = latest['ema50']
    macd_val = latest['macd']
    signal_val = latest['signal']

    print(f"RSI:{rsi:.2f} PRICE:{price:.2f}")
    if rsi < 35:
        return "buy"
    
    elif rsi > 55:
        return "sell"
    
    return "hold"


# ================= PRICE =================
def get_price():
    return exchange.fetch_ticker(symbol)['last']


# ================= ORDER FUNCTIONS =================
def buy():
    price = get_price()
    amount = risk_usdt / price

    if not paper_trading:
        order = exchange.create_market_buy_order(symbol, amount)
        print("BUY EXECUTED:", order)
    else:
        print("PAPER BUY:", amount)

    return price, amount


def sell(amount):
    if not paper_trading:
        order = exchange.create_market_sell_order(symbol, amount)
        print("SELL EXECUTED:", order)
    else:
        print("PAPER SELL:", amount)


# ================= LOGGING =================
def log_trade(data):
    try:
        with open(log_file, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)


# ================= TRADE MANAGEMENT =================
def monitor(entry_price, amount):
    df = get_data()
    atr = ATR(df).iloc[-1]

    take_profit = entry_price + (atr * 2)
    stop_loss = entry_price - (atr * 1.2)

    print(f"TP:{take_profit:.2f} SL:{stop_loss:.2f}")

    while True:
        price = get_price()

        if price >= take_profit:
            sell(amount)
            log_trade({
                "time": str(datetime.now()),
                "type": "TP",
                "entry": entry_price,
                "exit": price
            })
            break

        elif price <= stop_loss:
            sell(amount)
            log_trade({
                "time": str(datetime.now()),
                "type": "SL",
                "entry": entry_price,
                "exit": price
            })
            break

        time.sleep(2)


# ================= MAIN LOOP =================
def run():
    global trade_count, last_trade_time, day_tracker

    while True:
        try:
            # reset daily counter
            if datetime.now().date() != day_tracker:
                trade_count = 0
                day_tracker = datetime.now().date()

            if trade_count >= max_trades_per_day:
                print("Max trades reached today.")
                time.sleep(60)
                continue

            signal = get_signal()
            print("Signal:", signal)

            now = time.time()

            if signal == "buy" and (now - last_trade_time > cooldown):
                entry_price, amount = buy()
                monitor(entry_price, amount)

                trade_count += 1
                last_trade_time = time.time()

            else:
                print("No trade")

            time.sleep(5)

        except Exception as e:
            print("ERROR:", e)
            time.sleep(5)


run()