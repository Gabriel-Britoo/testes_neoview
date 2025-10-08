#include <Wifi.h>
#include <WebSocketsServer.h>

const char* ssid = "";
const char* password = "";

WebSocketsServer webSocket = WebSocketsServer(81);

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t lenght) {
  if(type == WStype_TEXT) {
    String msg = String((char*)payload);
    Serial.printf("Mensagem recebida do cliente %u: %s\n", num, msg.c_str());
    // continuar com voz...
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.print("AP iniciado. IP do ESP32: ");
  Serial.println(WiFi.softAPIP());

  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
}