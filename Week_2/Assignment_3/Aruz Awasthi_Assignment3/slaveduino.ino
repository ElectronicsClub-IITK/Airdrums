
#include <Wire.h>
#include <LiquidCrystal.h>

// Variables setup
int celsius = 0; 
int rs = 7;
int e =8;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

// LiquidCrystal object
LiquidCrystal lcd(rs, e, d4, d5, d6, d7);


void setup() {
  	lcd.begin(16, 2);
  	Serial.begin(9600);
  	lcd.setCursor(0, 0);
    lcd.print("temp:");
  	// Initializing the I2C bus
  	Wire.begin(9);
  	Wire.onReceive(receiveData);

}

void receiveData(int num) {
	  celsius = Wire.read();
  	Serial.print("Recieved: ");
  	Serial.println(celsius);
}

void loop() {
  lcd.setCursor(6, 0); // Set cursor position to display temperature
  lcd.print(celsius);
  lcd.print(" C ");
  delay(200);
}
