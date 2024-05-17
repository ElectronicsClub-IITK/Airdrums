#include<LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; 
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); 

float celsius;
int temp = A1;


void setup(){
  pinMode(temp,INPUT);
  Serial.begin(9600);
}


void loop(){
  int inc = 0;
  
  char t[10];
  Serial.readBytes(t,4);
  Serial.println(t);
  inc = atoi(t);
  celsius = (inc*0.004882814 - 0.5) * 100.0;
  	
  lcd.setCursor(0,1);
  lcd.print("Temp: ");
  lcd.print(celsius);
  lcd.print("°C");	
}
