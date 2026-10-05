#include "WebServer.h"
#include "WiFi.h"
#include "esp32cam.h"
#include <Stepper.h>

//datos del WiFi y URL de la cámara
const char* RED_WIF = "nombre_del_wifi"; 
const char* PSW_WIF = "la_clave_del_wifi"; 
const char* URL_DIR = "/cam.jpg";

//resolución de imagen y creación del servidor web
static auto RES_CAM = esp32cam::Resolution::find(800, 600);
WebServer srv_web(80);

//setup del motor
#define pasosPorRevolucion 2048
Stepper Motor(pasosPorRevolucion, 10, 11, 12, 13); 
int fotorresistencia = A3;

//variable para conectar al Wi-Fi solo una vez
bool conecto = false;

//saca la foto y la envía por red
void srv_jpg() {
  auto frm_cap = esp32cam::capture();
  if (frm_cap == nullptr) {
    Serial.println("¡FALLO LA CAPTURA!");
    srv_web.send(503, "", "");
    return;
  }
  Serial.printf("CAPTURA OK %dx%d %db\n", frm_cap->getWidth(), frm_cap->getHeight(), static_cast<int>(frm_cap->size()));

  srv_web.setContentLength(frm_cap->size());
  srv_web.send(200, "image/jpeg");

  WiFiClient cli_red = srv_web.client();
  frm_cap->writeTo(cli_red);
}

//confirma la resolución y pide enviar la foto
void hnd_jpg() {
  if (!esp32cam::Camera.changeResolution(RES_CAM)) {
    Serial.println("¡NO SE PUDO CAMBIAR LA RESOLUCION!");
  }
  srv_jpg();
}

//prende y configura la cámara
void ini_cam() {
  using namespace esp32cam;
  Config cfg_cam;
  cfg_cam.setPins(pins::AiThinker);
  cfg_cam.setResolution(RES_CAM);
  cfg_cam.setBufferCount(2);
  cfg_cam.setJpeg(80);

  int est_cam = Camera.begin(cfg_cam); 
  if (est_cam == 1) {
    Serial.println("CAMARA CONFIGURADA");
  } else {
    Serial.println("ERROR EN CAMARA");
  }
}

//conecta al WiFi e imprime la IP 
void ini_wif() {
  WiFi.persistent(0); 
  WiFi.mode(WIFI_STA);
  WiFi.begin(RED_WIF, PSW_WIF);
  
  while (WiFi.status() != WL_CONNECTED); // Espera conexión
    
  Serial.printf("http://%s%s\n", WiFi.localIP().toString().c_str(), URL_DIR);
}

//servidor alterno para mandar el estado del satelite
void estado_srv(){
  srv_web.send(200, "text/html", "<p>RECALCULAR</p>");
}

//activa el servidor de la foto
void ini_srv() {
  srv_web.on(URL_DIR, hnd_jpg);
  srv_web.on("/estado", estado_srv);
  srv_web.begin();
}

void setup() {
  Serial.begin(115200);
  
  Motor.setSpeed(10);
  pinMode(fotorresistencia,INPUT);

  ini_cam();

}

void loop() {
  srv_web.handleClient(); //mantiene vivo el servidor web
  
  int luz=analogRead(fotorresistencia);

  if (luz<260){
    Motor.step(10); 

  } else{
    if (!conecto) {
      ini_wif();
      ini_srv();
      conecto = true;
    }
  }
  delay(10);      //pausa rápida para no cortar el WiFi
}