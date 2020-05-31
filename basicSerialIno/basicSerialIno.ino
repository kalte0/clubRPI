// Arduino file vvv
// ~/clubRPI/basicSerialIno.ino

#include <ArduinoJson.h>

char hotgos;
String payload;

void setup() {
	Serial.begin(9600);
	pinMode(LED_BUILTIN, OUTPUT);
	digitalWrite(LED_BUILTIN, HIGH);
	delay(1000);
	digitalWrite(LED_BUILTIN, LOW);
	delay(1000);
	Serial.println("test"); 
}

void loop() {
//	serialReadNumber();
	serialReadJson();
}

int serialReadNumber() {
	if (Serial.available()) { //when get Serial info:
		int inChar = Serial.read(); 
		hotgos = (char)inChar;
		if (hotgos == (char)'4') {
			digitalWrite(LED_BUILTIN, HIGH);	
		}
		else { 
			digitalWrite(LED_BUILTIN, LOW);
		}
	}
}

int serialReadJson() {
	if (Serial.available()) { 
		Serial.println("Serial Available");
		payload = Serial.readStringUntil('/n');	
	}
	StaticJsonDocument<512> doc; //This creates a temporary JsonDocument called doc. 
	DeserializationError error = deserializeJson(doc, payload); 

	if (error) {
		 Serial.println("Failed to read file"); 
	}
	if (doc["Joy1"] == 0.56) {
		Serial.println("You succeeded");
	}
	else {
		Serial.println("Bruh you failed"); 
	}
	
}

