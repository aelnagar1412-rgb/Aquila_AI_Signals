from strategies.rsi import rsi_signal
from strategies.ema import ema_crossover

def strategy_engine(data):
    signals = [
        rsi_signal(data["rsi"]),
        ema_crossover(data["ema_fast"], data["ema_slow"])
    ]
    if signals.count("BUY") > signals.count("SELL"):
        return "BUY"
    if signals.count("SELL") > signals.count("BUY"):
        return "SELL"
    return "HOLD"