#include <Servo.h>
Servo servo1;

const byte cuarto=9;
const byte cocina=8;
const byte sala=7;
const byte bano=6;
const byte puerta=2;
const byte ventilador=4;
const byte seguridad=3;
char lecturaSerial = 'N';

void setup() {
  Serial.begin(115200);
  pinMode(cuarto,OUTPUT);
  pinMode(cocina,OUTPUT);
  pinMode(sala,OUTPUT);
  pinMode(bano,OUTPUT);
  servo1.attach(puerta);
  pinMode(ventilador,OUTPUT);
  pinMode(seguridad,OUTPUT);
}

void loop() {
  if(Serial.available()){
    lecturaSerial = Serial.read();
    Serial.println(lecturaSerial);
    delay(50);
    //CUARTO
    if(lecturaSerial == 'C'){
      digitalWrite(cuarto,HIGH);
    }
    else if (lecturaSerial == 'c'){
      digitalWrite(cuarto,LOW);
    }
    //COCINA
    if(lecturaSerial == 'O'){
      digitalWrite(cocina,HIGH);
    }
    else if (lecturaSerial == 'o'){
      digitalWrite(cocina,LOW);
    }
    //SALA
    if(lecturaSerial == 'S'){
      digitalWrite(sala,HIGH);
    }
    else if (lecturaSerial == 's'){
      digitalWrite(sala,LOW);
    }
    //BAÑO
    if(lecturaSerial == 'B'){
      digitalWrite(bano,HIGH);
    }
    else if (lecturaSerial == 'b'){
      digitalWrite(bano,LOW);
    }
    //PUERTA
    if(lecturaSerial == 'P'){
      servo1.write(110);
    }
    else if (lecturaSerial == 'p'){
      servo1.write(10);
    }
    //VENTILADOR
    if(lecturaSerial == 'V'){
      digitalWrite(ventilador,HIGH);
    }
    else if (lecturaSerial == 'v'){
      digitalWrite(ventilador,LOW);
    }
    //Cortina
    if(lecturaSerial == 'E'){
      digitalWrite(seguridad,HIGH);
      delay(5000);
      digitalWrite(seguridad,LOW);
    }
    else if (lecturaSerial == 'e'){
      digitalWrite(seguridad,LOW);
    }
  }
}
