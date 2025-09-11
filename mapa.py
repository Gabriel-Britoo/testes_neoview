import requests
import json
from deep_translator import GoogleTranslator as Translator

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjY4MGU3ZmVlOGRiNGMwZTFmMmNlN2NmZDg0OTg5YjczNmQ1NDM0NDBkZTk0NjVhZDI2ZmI4NjQ2IiwiaCI6Im11cm11cjY0In0="

origem = (-45.70995866888095, -23.10623100450314)
destino = (-45.710132020008736, -23.106053337439732)

start = f"{origem[0]},{origem[1]}"
end = f"{destino[0]},{destino[1]}"

url = f"https://api.openrouteservice.org/v2/directions/foot-walking?start={start}&end={end}"

headers = {
    "Authorization": API_KEY
}

response = requests.get(url, headers=headers)
data = response.json()

segmento = data["features"][0]["properties"]["segments"][0]
distancia = segmento["distance"]
duracao = segmento["duration"]
passos = [step["instruction"] for step in segmento["steps"]]

traduzidos = [Translator(source='en', target='pt').translate(passo) for passo in passos]

payload = {
    "distancia": int(distancia),
    "duracao": int(duracao),
    "proximos_passos": traduzidos
}

print(json.dumps(payload, indent=4, ensure_ascii=False))