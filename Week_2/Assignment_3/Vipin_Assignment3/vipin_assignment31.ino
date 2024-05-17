#include<Wire.h>
#include<LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; 
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); 

volatile byte receiveValue;   

void setup(){
    Wire.begin(8);                
    Wire.onReceive(dataReceive); 
    lcd.begin(16, 2); 
}


void loop(){
  	int temp = receiveValue
  	lcd.setCursor(0,1);
	lcd.print("Temp: ");
  	lcd.print(temp);
	lcd.print(" C");
  	delay(500);
  	lcd.clear();
	
}

void dataReceive(int Number) {     
  if(Wire.available())        
    receiveValue = Wire.read();          
}
