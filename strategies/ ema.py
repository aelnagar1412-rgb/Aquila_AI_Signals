def ema_crossover(fast, slow):
    if fast > slow: return "BUY"
    if fast < slow: return "SELL"
    return "HOLD"
