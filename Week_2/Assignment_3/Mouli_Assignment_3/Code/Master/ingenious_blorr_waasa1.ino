#include <Wire.h>

const int LM35_PIN = A0;
float temperature;

void setup() {
  Wire.begin();        // join I2C bus
  Serial.begin(9600);  // initialize serial communication
}

void loop() {
  temperature = getTemperature();
  
  Serial.print("Temperature sent: ");
  Serial.println(temperature);
  
  Wire.beginTransmission(9); // transmit to device with address 9
  Wire.write((byte*)&temperature, sizeof(temperature)); // send temperature data
  Wire.endTransmission();    // stop transmitting
  
  delay(1000);
}

float getTemperature() {
  int raw = analogRead(LM35_PIN);
  float voltage = (raw / 1024.0) * 5.0;
  float temp = voltage * 100.0; // Convert voltage to Celsius
  return temp;
}
