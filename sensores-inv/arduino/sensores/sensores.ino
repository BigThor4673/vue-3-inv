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
    /*************************************************************/
    /***** DHT11: Lee la temperatura y la humedad ambiental ******/
    /*************************************************************/
    int chk = DHT.read11(DHT11_PIN);
    // Serial.print("{'temperatura-ambiente': "+DHT.temperature+", 'humedad-ambiente': "+DHT.humidity+"}");
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
    /******************* FOTORESISTENCIA ***********************************/

    /*********************************************/
    /***** YL69: Lee la humedad de la tierra *****/
    /*********************************************/
    sueloValue = analogRead(rainPin);
    // Serial.println("{ 'humedad-suelo': sueloValue }");
    /**************** YL69 **********************/

    Serial.println("{\"temperatura-ambiente\": " + String(DHT.temperature) + ", \"humedad-ambiente\": " + String(DHT.humidity) + ", \"luz\": " + String(luzValor) + ", \"humedad-suelo\": " + String(sueloValue) + "}");
    delay(2000);
}
