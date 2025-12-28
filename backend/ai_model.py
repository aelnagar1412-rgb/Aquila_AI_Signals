import random

def ai_decision(features: dict):
    """
    Features example:
    {
      "rsi": 32,
      "macd": 0.8,
      "ema_distance": 0.6,
      "votes": 4
    }
    """

    base_confidence = (
        features["votes"] * 20 +
        (50 - abs(50 - features["rsi"])) * 0.5
    )

    confidence = min(100, base_confidence)

    if confidence >= 75:
        decision = "BUY" if features["rsi"] < 40 else "SELL"
    else:
        decision = "NO_TRADE"

    return decision, round(confidence, 1)
