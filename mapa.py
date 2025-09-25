import requests
import json
import geocoder

API_KEY = "SUA_CHAVE_API_AQUI"

def geoCode(endereco):
    url = "https://api.openrouteservice.org/geocode/search"
    params = {
        "api_key": API_KEY,
        "text": endereco,
        "size": 1
    }

    resp = requests.get(url, params=params)
    dados = resp.json()

    if "features" in dados and len(dados["features"]) > 0:
        coords = dados["features"][0]["geometry"]["coordinates"]
        label = dados["features"][0]["properties"]["label"]
        return coords, label
    else:
        raise ValueError(f"Endereço não encontrado: {endereco}")

usar_localizacao = True  

if usar_localizacao:
    g = geocoder.ip('me')
    origem_coords = [g.lng, g.lat]
    origem_label = "Sua localização aproximada"
else:
    origem_txt = input("Digite a origem: ")
    origem_coords, origem_label = geoCode(origem_txt)

destino_txt = input("Digite o destino: ")

try:
    destino_coords, destino_label = geoCode(destino_txt)
except ValueError as e:
    print(e)
    exit()

print(f"Origem encontrada: {origem_label}")
print(f"Destino encontrado: {destino_label}")

url = f"https://api.openrouteservice.org/v2/directions/foot-walking?start={origem_coords[0]},{origem_coords[1]}&end={destino_coords[0]},{destino_coords[1]}"
headers = {"Authorization": API_KEY}

response = requests.get(url, headers=headers)
data = response.json()

if "features" not in data:
    print("Erro ao calcular rota!")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    exit()

segmento = data["features"][0]["properties"]["segments"][0]
distancia = segmento["distance"]
duracao = segmento["duration"]
passos = [step["instruction"] for step in segmento["steps"]]

payload = {
    "distancia_metros": int(distancia),
    "distancia_km": round(distancia / 1000, 2),
    "duracao_segundos": int(duracao),
    "duracao_minutos": round(duracao / 60, 1),
    "proximos_passos": passos
}

print(json.dumps(payload, indent=4, ensure_ascii=False))