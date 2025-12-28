from fastapi import FastAPI, WebSocket
from telegram import send_telegram
from strategies.engine import strategy_engine
from market.websocket import price_stream

app = FastAPI(title="Aquila AI Backend", version="1.0")

@app.get("/api/backend/status")
def status():
    return {"service":"Aquila AI Backend","status":"online","version":"1.0"}

@app.websocket("/ws/prices")
async def prices_ws(ws: WebSocket):
    await ws.accept()
    await price_stream(ws)

@app.post("/api/signal")
def generate_signal(payload: dict):
    decision = strategy_engine(payload)
    if payload.get("send_telegram"):
        send_telegram(
            payload["telegram_token"],
            payload["chat_id"],
            f"📊 Signal: {decision} | {payload['symbol']}"
        )
    return {"symbol":payload["symbol"],"signal":decision}
