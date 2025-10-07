# código teste para enviar instruções via WebSocket para um ESP32

import asyncio
import websockets
import json

ESP32_IP = "192.168.4.1"
ESP32_PORT = 81
uri = f"ws://{ESP32_IP}:{ESP32_PORT}"

async def enviar_instrucao(texto):
    async with websockets.connect(uri) as ws:
        msg = {"type": "instruction", "text": texto}
        await ws.send(json.dumps(msg))
        print(f"Enviado: {texto}")

asyncio.run(enviar_instrucao("Iniciar mapa"))