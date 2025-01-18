#include <dht.h>
 
dht DHT;
#define DHT11_PIN 2

int fotoPin = A5;
int fotoValor;
int luzValor;

int rainPin = A0;
int thresholdValue = 800;

int sueloValue;

void setup()
{
    Serial.begin(9600);
    pinMode(fotoPin, INPUT);
    pinMode(rainPin, INPUT);
}

void loop()
{
    //Genera un array de dos posiciones para almacenar el nombre del sensor en la primera posición, y el valor del sensor en la segunda.
    // String sensorData[2];
    // sensorData[0] = "DHT11";
    // sensorData[1] = "Temperature = " + String(DHT.temperature) + " Humidity = " + String(DHT.humidity);
    // Serial.println(sensorData[0] + " " + sensorData[1]);

    /*************************************************************/
    /***** DHT11: Lee la temperatura y la humedad ambiental ******/
    /*************************************************************/
    int chk = DHT.read11(DHT11_PIN);
    // Serial.print("{'temperatura-ambiente': "+DHT.temperature+", 'humedad-ambiente': "+DHT.humidity+"}");
    // delay(2000);
    /*********************** DHT11 ******************************/

    /***********************************************************************/
    /***** FOTORESISTENCIA: Detecta si la luz está encendida o apagada *****/
    /***********************************************************************/
    //Arroja 900 con luz apagada. Si el valor es menor a 700, esta encendida.

    fotoValor = analogRead(fotoPin);
    if(fotoValor < 700){
        luzValor = 1;
    }
    else{
        luzValor = 0;
    }
    // Serial.println("{'luz': luzValor}");
    // Serial.println(fotoValor);
    // delay(2000); 
    /******************* FOTORESISTENCIA ***********************************/

    /*********************************************/
    /***** YL69: Lee la humedad de la tierra *****/
    /*********************************************/
    sueloValue = analogRead(rainPin);
    // Serial.println("{ 'humedad-suelo': sueloValue }");
    // if(sueloValue < thresholdValue){
    // }
    // else {
    //     Serial.println(" - Time to water your plant");
    // }
    // delay(2000);
    /**************** YL69 **********************/

    Serial.print("{'temperatura-ambiente': "+DHT.temperature+", 'humedad-ambiente': "+DHT.humidity+", 'luz': "+luzValor+", 'humedad-suelo': "+sueloValue+"}");
    delay(5000);
}

