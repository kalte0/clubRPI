#include <Adafruit_LEDBackpack.h>
#include <Wire.h>
#include <Adafruit_GFX.h> //graphics, for 7 seg

Adafruit_7segment matrix = Adafruit_7segment(); //control 7 seg display

void setup() {
	Serial.begin(9600); 

	matrix.begin(0x70); 
	matrix.print(0, DEC); 
	matrix.writeDisplay(); 

}

void loop() {
	if (Serial.available()) {
		int inChar = Serial.read(); 
		matrix.print(inChar, DEC); 
		matrix.writeDisplay(); 
	}
}
