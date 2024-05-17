// Include the required Wire library for I2C
#include<Wire.h>

int celsius = 0;
void setup() {
  pinMode(A0,INPUT);
  // Start the I2C Bus as Master
  Wire.begin(); 
  Serial.begin(9600);
}
void loop() {
  celsius = analogRead(A0)*0.004882814;
  celsius = (celsius - 0.5) * 100.0;
  Wire.beginTransmission(8);
  Wire.write(celsius);
  Wire.endTransmission();
  delay(100);
}