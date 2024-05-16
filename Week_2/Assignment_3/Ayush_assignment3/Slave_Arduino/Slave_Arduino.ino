#include<LiquidCrystal.h>
int celcius;
LiquidCrystal lcd (8,7,6,5,4,3); //RS, E, D4, D5, D6, D7


void setup()
{ 
  lcd.begin(16,2);
  lcd.begin(16,2);
  Serial.begin(9600);
 
    lcd.print("   START   ");
    delay(500);
  	lcd.clear();
}


void loop() 
{
	celcius=Serial.read();
  	Serial.println(celcius);
 	lcd.print(celcius);
  	delay(500);
  	lcd.clear();
  	delay(500);

}







