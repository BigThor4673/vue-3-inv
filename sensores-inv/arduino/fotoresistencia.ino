int fotoPin = A5;
int fotoValor;

void setup(){
  Serial.begin(9600);
  pinMode(fotoPin, INPUT);
    
}

void loop(){
  //Arroja 900 con luz apagada.
  //Si el valor es menor a 700, esta encendida.
  fotoValor = analogRead(fotoPin);
  Serial.println(fotoValor);
  delay(1000);  
}