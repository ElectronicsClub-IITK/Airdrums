#include <Wire.h>


int celsius = 0;


void setup()
{
  
  pinMode(A0, INPUT);
  
  Serial.begin(9600);
  Wire.begin(); 
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop()
{
 
  
  celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125);
  
  Serial.print(celsius);
  
  Wire.beginTransmission(8);         //(6)
  Wire.write(celsius);        //(7)
  Wire.endTransmission();        //(8)
  
  delay(1000); 
}
