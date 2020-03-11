#include <Adafruit_LEDBackpack.h>
#include <Wire.h> 
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40, Wire);
#define SERVO_FREQ 60 // Analog servos run at ~60 Hz updates
void setup() {
	Serial.begin(9600);
	pwm.begin();
	pwm.setOscillatorFrequency(27000000);
	pwm.setPWMFreq(SERVO_FREQ);

	pwm.writeMicroseconds(0, 1500);
	delay(6000);
}

void loop() {
	pwm.writeMicroseconds(0,1900); 
	delay(3000);
	pwm.writeMicroseconds(0,1100); 
	delay(3000);
}
