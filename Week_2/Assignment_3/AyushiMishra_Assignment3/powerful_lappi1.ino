
/*
  LiquidCrystal Library
  
  The circuit:
  * LCD RS pin to digital pin 12
  * LCD Enable pin to digital pin 11
  * LCD D4 pin to digital pin 5
  * LCD D5 pin to digital pin 4
  * LCD D6 pin to digital pin 3
  * LCD D7 pin to digital pin 2
  * LCD R/W pin to ground
  * LCD VSS pin to ground
  * LCD VCC pin to 5V
  * 10K resistor:
  * ends to +5V and ground
  * wiper to LCD VO pin (pin 3)
  
*/
#include <Wire.h>

const int tempPin = A0;

void setup() {
  Wire.begin();
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(tempPin);
  float temperature = (sensorValue * 0.004882814) * 100.0; // TMP36 conversion to Celsius
  Serial.println(temperature); // For debugging
  Wire.beginTransmission(9); // Address of receiving Arduino
  Wire.write((byte*)&temperature, sizeof(temperature)); // Send temperature data
  Wire.endTransmission();
  delay(1000); // Adjust delay as needed
}