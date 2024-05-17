#include <Wire.h>

const int tempPin = A0;
void setup() {
  Wire.begin(); // Join I2C bus as master
  Serial.begin(9600);
}

void loop() {
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = voltage * 100.0; // for LM35

  Wire.beginTransmission(8); // Address of the slave
  Wire.write((int)temperature); // Send temperature as integer
  Wire.endTransmission();
  delay(1000); // Send data every second
}
