import asyncio
import websockets
import json

ESP32_IP = ""
ESP32_PORT = 81
uri = f"ws://{ESP32_IP}:{ESP32_PORT}"

async def receber_mensagens():
    async with websockets.connect(uri) as ws:
        print("Conectado")
        while True:
            if ws.recv("Destino: "):
                destino = await ws.recv()
                print(destino)

async def enviar_instrucao(texto):
    async with websockets.connect(uri) as ws:
        msg = {"type": "instruction", "text": texto}
        await ws.send(json.dumps(msg))
        
asyncio.run(enviar_instrucao("Distância: 300 metros"))

asyncio.run(receber_mensagens())