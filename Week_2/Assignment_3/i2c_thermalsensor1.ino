#include <Wire.h>

int voutPin = A2; // assign the pin

void setup()
{
  pinMode(voutPin, INPUT); // setting the pin mode
  Serial.begin(9600); // setting the baud rate
  Wire.begin(); // initialise I2C bus
}

void loop()
{
  int val = analogRead(voutPin); // reading the value from analog pin
  int celsius = map(((val - 20) * 3.04) ,0,1023,-40,125);
  // calculating the celsius value from the output of tmp36 temperature sensor
  Serial.println(celsius); // printing the temperature on serial monitor
  
  Wire.beginTransmission(1); //begins queueing up the transmission
  Wire.write(celsius); // writes data to be transmitted
  
  Wire.endTransmission();
  delay(500);
}