



void setup() {
	Serial.begin(9600);
	pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
	if (Serial.available()) { //when get Serial info:
		int inChar = Serial.read(); 
		int hotgos = (char)inChar;
		if (hotgos == '3') {
			digitalWrite(LED_BUILTIN, HIGH);	
		}
		else { 
			digitalWrite(LED_BUILTIN, LOW);
		}
	}
}
