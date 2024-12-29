#include <dht.h>
 
dht DHT;
#define DHT11_PIN 2

int fotoPin = A5;
int fotoValor;

int rainPin = A0;
int thresholdValue = 800;

void setup()
{
    Serial.begin(9600);
    pinMode(fotoPin, INPUT);
    pinMode(rainPin, INPUT);
}

void loop()
{
    //Genera un array de dos posiciones para almacenar el nombre del sensor en la primera posición, y el valor del sensor en la segunda.
    /*String sensorData[2];
    sensorData[0] = "DHT11";
    sensorData[1] = "Temperature = " + String(DHT.temperature) + " Humidity = " + String(DHT.humidity);
    Serial.println(sensorData[0] + " " + sensorData[1]);*/

    /***** DHT11: Lee la temperatura y la humedad ambiental *****/
    int chk = DHT.read11(DHT11_PIN);
    Serial.print("Temperature = ");
    Serial.println(DHT.temperature);
    Serial.print("Humidity = ");
    Serial.println(DHT.humidity);
    delay(2000);
    /***** DHT11 *****/

    /***** FOTORESISTENCIA: Detecta si la luz está encendida o apagada *****/
    //Arroja 900 con luz apagada.
    //Si el valor es menor a 700, esta encendida.
    fotoValor = analogRead(fotoPin);
    Serial.println(fotoValor);
    delay(2000); 
    /***** FOTORESISTENCIA *****/

    /***** YL69: Lee la humedad de la tierra *****/
    int sensorValue = analogRead(rainPin);
    Serial.print(sensorValue);
    if(sensorValue < thresholdValue){
        Serial.println(" - Doesn't need watering");
    }
    else {
        Serial.println(" - Time to water your plant");
    }
    delay(2000);
    /***** YL69 *****/
}
