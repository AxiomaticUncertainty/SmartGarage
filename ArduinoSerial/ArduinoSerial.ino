void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  pinMode(12, OUTPUT);
}

void loop() {
  char inByte = ' ';
  if(Serial.available() > 0){
    while (Serial.available() > 0) {
      Serial.read();
    }
    Serial.println("test");
    digitalWrite(12, HIGH);
    delay(30000);
    digitalWrite(12, LOW);
    delay(200);
  }
}
