import asyncio, random
async def price_stream(ws):
    while True:
        await ws.send_json({"symbol":"EURUSD","price":round(random.uniform(1.08,1.1),5)})
        await asyncio.sleep(1)