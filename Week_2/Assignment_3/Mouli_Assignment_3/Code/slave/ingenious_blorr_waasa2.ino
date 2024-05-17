
#include <Wire.h>
#include <LiquidCrystal.h>

const int LCD_RS = 12;
const int LCD_EN = 11;
const int LCD_D4 = 5;
const int LCD_D5 = 4;
const int LCD_D6 = 3;
const int LCD_D7 = 2;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

float temperature;

void setup() {
  Wire.begin(9);                // join I2C bus with address 9
  Wire.onReceive(receiveData);  // register event
  lcd.begin(16, 2);             // set up the LCD's number of columns and rows
}

void loop() {
  // Display received temperature
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temperature:");
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  lcd.print(" C");
  delay(1000);
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    Wire.readBytes((byte*)&temperature, sizeof(temperature)); // receive temperature data
  }
}
