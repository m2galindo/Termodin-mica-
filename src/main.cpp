#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

unsigned long intervalo = 1000; // 1 segundo
unsigned long tiempoAnterior = 0;

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  unsigned long tiempoActual = millis();
  
  if (tiempoActual - tiempoAnterior >= intervalo) {
    tiempoAnterior = tiempoActual;
    
    sensors.requestTemperatures();
    float temp = sensors.getTempCByIndex(0);
    
    Serial.println(temp);
  }
}
