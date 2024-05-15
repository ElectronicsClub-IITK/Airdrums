#include <Wire.h>
#include <LiquidCrystal.h>

const int LM35_PIN = A0;
const int LCD_RS = 12;
const int LCD_EN = 11;
const int LCD_D4 = 5;
const int LCD_D5 = 4;
const int LCD_D6 = 3;
const int LCD_D7 = 2;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  Wire.begin();        // join I2C bus
  Serial.begin(9600);  // initialize serial communication
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows
}

void loop() {
  float temperature = getTemperature();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temperature:");
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  lcd.print(" C");
  delay(1000);
}

float getTemperature() {
  int raw = analogRead(LM35_PIN);
  float voltage = (raw / 1024.0) * 5.0;
  float temperature = voltage * 100.0;
  return temperature;
}