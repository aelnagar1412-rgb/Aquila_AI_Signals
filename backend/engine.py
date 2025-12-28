from ai_model import ai_decision
from market import market_open

def generate_signal(indicators):
    if not market_open():
        return None

    votes = indicators["votes"]

    decision, confidence = ai_decision({
        "rsi": indicators["rsi"],
        "macd": indicators["macd"],
        "ema_distance": indicators["ema_distance"],
        "votes": votes
    })

    if decision == "NO_TRADE":
        return None

    return {
        "signal": decision,
        "confidence": confidence,
        "votes": votes
    }
