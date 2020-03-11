#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_LEDBackpack.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_7segment matrix = Adafruit_7segment(); //"matrix." commands control the 7 segment display. 
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40, Wire); //"pwm." commands control the Servo driver. 

#define REVERSE '0'
#define BRAKE '1'
#define FORWARD '2'

#define SERVO_FREQ 60 //necessary for the PWMServoDriver commands to work

int state; // for the basic control scheme switch statement.  

void setup() {
Serial.begin(9600); 

matrix.begin(0x70); 
matrix.print(0,DEC);
matrix.writeDisplay(); 

pwm.begin(); 
pwm.setOscillatorFrequency(27000000);
pwm.setPWMFreq(SERVO_FREQ); 

pinMode(LED_BUILTIN, OUTPUT); 

}


void loop() {
/*pwm.writeMicroseconds(0,1500);
delay(5000); 
pwm.writeMicroseconds(0,1700);
delay(5000); */

	if (Serial.available()) { //When the code gets the latest Serial input:
		int inChar = Serial.read(); 
		state = (char)inChar; //Run one of these states depending on what the code read from Serial. 
			switch (state) 
			{
				case REVERSE: 
					matrix.print(13, DEC); 
					matrix.writeDisplay(); 
					digitalWrite(LED_BUILTIN, HIGH);
					pwm.writeMicroseconds(0, 1300); 
					break;

				case BRAKE:
					matrix.print(15, DEC); 
					matrix.writeDisplay(); 
					digitalWrite(LED_BUILTIN, LOW); 
					pwm.writeMicroseconds(0,1500); 
					break;

				case FORWARD: 
					matrix.print(17, DEC);
					matrix.writeDisplay();
					digitalWrite(LED_BUILTIN, HIGH); 
					pwm.writeMicroseconds(0,1700); 
					break; 

			}
	}
}
