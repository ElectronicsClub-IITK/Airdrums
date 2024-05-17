// C++ code
//
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address, 16 columns, 2 rows

void setup() {
  Wire.begin(8); // Address of this Arduino as slave
  Wire.onReceive(receiveEvent);
  lcd.init();
  lcd.backlight();
}

void loop() {
  // Nothing here, as we're using I2C communication
}

void receiveEvent(int bytes) {
  float temperature;
  Wire.readBytes((byte*)&temperature, sizeof(temperature)); // Receive temperature data
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");
}