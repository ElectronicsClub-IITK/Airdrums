#include <Wire.h>

const int sensorPin = A0;
void setup(){
  Wire.begin(8);

}

void loop() {

  	float celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125); 


	
  Wire.beginTransmission(8); // Transmit to device #8
  Wire.write((int)celsius); // Send temperature as integer
  Wire.endTransmission(); // Stop transmitting

  delay(1000); // Wait for 1 second
}
