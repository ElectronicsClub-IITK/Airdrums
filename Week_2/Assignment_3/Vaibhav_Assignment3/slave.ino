#include <Wire.h>
#include <LiquidCrystal.h>


LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int receivedTemp = 0;

void setup() {
  Wire.begin(8); 
  Wire.onReceive(receiveEvent); 
  lcd.begin(16, 2); 
  lcd.print("Temp: ");
}

void loop() {
  lcd.setCursor(6, 0); 
  lcd.print(receivedTemp);
  lcd.print(" C");
  delay(500); 
}

void receiveEvent(int howMany) {
  if (Wire.available()) {
    receivedTemp = Wire.read(); 
  }
}
