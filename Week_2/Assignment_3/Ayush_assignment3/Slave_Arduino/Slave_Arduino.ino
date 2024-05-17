#include <Wire.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8,7,6,5,4,3);

float celsius=18;

void setup() {
  lcd.begin(16, 2);
  Wire.begin(8); 
  Wire.onReceive(receiveEvent);
  lcd.print("Temperature Reading");
  delay(1000);


}

void loop() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(celsius);
  lcd.print(" C");

  delay(1000);
}
void receiveEvent(int howMany) {
  while (Wire.available()) {
    celsius = Wire.read(); // Receive byte as an integer
  }
}


