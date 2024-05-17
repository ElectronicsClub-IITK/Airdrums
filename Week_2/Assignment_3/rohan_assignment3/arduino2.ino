#include <LiquidCrystal.h>
#include <Wire.h>

volatile byte receiveValue;        //(1)


LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup()
{
 Wire.begin(8);        //(2)            
 Wire.onReceive(dataReceive);       
 lcd.begin(16, 2); 
}

void loop()
{
  lcd.setCursor(0,0);          
  lcd.print(receiveValue); 
  ///lcd.setCursor(2,1);           
  //lcd.print("RaspberryUser");    
  }

void dataReceive(int Number) {        //(4)
  if(Wire.available())        //(5)
    receiveValue = Wire.read();        //(6)   
}