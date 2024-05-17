#include <Wire.h>

#define TEMP_SENSOR A0

void setup() {
  Wire.begin(); 
  Serial.begin(9600);
}

void loop() {
  int tempValue = analogRead(TEMP_SENSOR); 
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100; 

  Wire.beginTransmission(8); 
  Wire.write((int)temperature); 
  Wire.endTransmission(); 

  delay(1000); 
}