#include <Wire.h>
#include <LiquidCrystal.h>

// defining the pins for lcd
int rs = 7;
int en = 8;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
int celsius; // variable for temperature value

void setup()
{
  lcd.begin(16,2);
  Wire.begin(1); // Initialise I2C bus
  Wire.onReceive(receiveEvent); //register function to be called when peripheral receives a transmission
  Serial.begin(9600); // setting the baud rate
}

void loop()
{
  
  delay(100);
}

void receiveEvent(int h){

  celsius = Wire.read(); // reads byte that was transmitted
  Serial.println(celsius); // printing on serial monitor
  
  lcd.setCursor(0,0); // set the cursor
  lcd.print(celsius); // diplay the temperature on lcd
  delay(100);
}