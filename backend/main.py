from fastapi import FastAPI
from engine import generate_signal

app = FastAPI()

@app.get("/api/status")
def status():
    return {
        "service": "Aquila AI Backend",
        "status": "online",
        "version": "1.0"
    }

@app.get("/api/signal")
def signal():
    fake_indicators = {
        "rsi": 34,
        "macd": 0.7,
        "ema_distance": 0.5,
        "votes": 4
    }

    result = generate_signal(fake_indicators)
    if not result:
        return {"signal": "NO_TRADE"}

    return result
