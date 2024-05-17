#include <Wire.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
float temperature = 0;

void setup() {
  Wire.begin(8); // Join I2C bus with address #8
  Wire.onReceive(receiveEvent); // Register event
  lcd.begin(16, 2); // Initialize the LCD
  lcd.print("Temp: ");
}

void loop() {
  lcd.clear();
  lcd.setCursor(6, 0); // Set cursor position to display temperature
  lcd.print(temperature);
  lcd.print(" C   ");
  delay(500);
}
void receiveEvent(int howMany) {
  while (Wire.available()) {
    temperature = Wire.read(); // Receive temperature as integer
  }
}
