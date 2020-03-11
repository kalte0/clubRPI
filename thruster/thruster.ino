#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver (0x40, Wire);

#define SERVO_FREQ 60 

int pot = analogRead(3); 
int speed; 
 
void setup() { 
pwm.begin();
pwm.setOscillatorFrequency(27000000);
pwm.setPWMFreq(SERVO_FREQ);

pinMode(LED_BUILTIN, OUTPUT);

digitalWrite(LED_BUILTIN, LOW); 
//pwm.writeMicroseconds(0, 0);
//delay(6000);
//pwm.writeMicroseconds(0, 1500); 
//delay(8000); 
}  

void loop() {
pot = analogRead(3); 
speed = map(pot, 0, 1023, 1100, 1900);  
pwm.writeMicroseconds(0, speed); 
delay(10); 
}
