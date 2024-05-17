#include <Wire.h>
#include <LiquidCrystal.h>

// Variables to store temperature data
int celsius = 0; 
float farenheit = 0;

// Variables to store the lcd connection pin numbers
int rs_pin = 12;
int enable_pin = 11;
int d4_pin = 5;
int d5_pin = 4;
int d6_pin = 3;
int d7_pin = 2;

// LiquidCrystal object
LiquidCrystal lcd(rs_pin, enable_pin, d4_pin, d5_pin, d6_pin, d7_pin);


void setup() {
  
  	// Setting number of columns and rows
  	lcd.begin(16, 2);
  
  	// Initializing Serial Monitor
  	Serial.begin(9600);

  	// Displaying the placeholder text
  	lcd.setCursor(0, 0);
  	lcd.print("Waiting for data...");	
  	lcd.setCursor(0, 1);
  	lcd.print("Please wait...");

  	// Initializing the I2C bus
  	Wire.begin(9);
  	Wire.onReceive(tempDataReceived);

}


void tempDataReceived(int bytes) {

  	// Reading the temperature data
	celsius = Wire.read();
  	if (celsius >= 216) celsius -= 256;

  	Serial.print("Recieved: ");
  	Serial.println(celsius);

  	// Converting celsius to farenheit
  	farenheit = (9 * celsius / 5) + 32;

  	// Displaying the temperature data
  	displayTemp(celsius, farenheit);

}

void displayTemp(int temp_c, float temp_f) {

  	// Clearing the lcd screen
  	lcd.clear();

  	// Displaying the temperature in celsius
  	lcd.setCursor(0,0);
  	lcd.print("Celsius: ");
  	lcd.print(temp_c);

  	// Displaying the temperature in farenheit
  	lcd.setCursor(0, 1);
  	lcd.print("Farenheit: ");
  	lcd.print(temp_f);
}


void loop() {
}