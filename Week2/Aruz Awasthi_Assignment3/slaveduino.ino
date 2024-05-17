
#include <Wire.h>
#include <LiquidCrystal.h>
// Variables to store temperature data
int celsius = 0;

void setup() {
  	pinMode(A0, INPUT);

	// Initializing Serial Monitor
  	Serial.begin(9600);

  	// Initializing the I2C bus
  	Wire.begin(9);

}

void loop() {

  	// Reading the temperature data
	celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125);

	// Sending the temperature
  	Wire.beginTransmission(9);
  	Wire.write(celsius);
  	Wire.endTransmission(9);
  	delay(200);

}