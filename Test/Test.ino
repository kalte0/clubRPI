
void setup() {
pinMode(LED_BUILTIN, OUTPUT); 
Serial.begin(9600);
}

void loop() { 
digitalWrite(LED_BUILTIN, HIGH); 
Serial.write("Hi");
delay(1000); 
digitalWrite(LED_BUILTIN, LOW); 
Serial.write("Hello");
delay(1000); 
}
