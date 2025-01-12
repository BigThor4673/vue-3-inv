import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import time
import random
import json

# Inicializa la aplicación Firebase
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

# Obtén una referencia a la base de datos Firestore
db = firestore.client()

# Función para leer el input y enviar los datos a Firestore
def send_to_firestore(document_name, data):
    #Almacenar en una variable el valor de la fecha actual en formato dd/MM/yyyy HH:mm
    dateStringActual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    doc_ref = db.collection("inv-data/Inv-001/maceteros/ma-z01/sensores").document(document_name)
    pre_data = {"valor": data, "fecha_update": firestore.SERVER_TIMESTAMP, "fecha_string": dateStringActual}
    doc_ref.update(pre_data)
    print(f"Data sent to Firestore: {pre_data}")

# Simula la lectura de un input que cambia su valor
def read_input():
    # return random.randint(0, 100)
    text = '{"temperatura-ambiente": '+str(random.randint(10, 40))+', "humedad-ambiente": '+str(random.randint(0, 30))+', "luz": '+str(random.randint(0, 1))+', "humedad-suelo": '+str(random.randint(0, 100))+'}'
    
    print(f"Data read from input: {text}")

    return text

def main():
    last_value = None
    while True:
        current_value = json.loads(read_input())
        temperatura_ambiente = current_value['temperatura-ambiente']
        humedad_ambiente = current_value['humedad-ambiente']
        luz = True if current_value['luz'] == 1 else False
        humedad_suelo = current_value['humedad-suelo']

        send_to_firestore("temperatura-ambiente", temperatura_ambiente)
        send_to_firestore("humedad-ambiente", humedad_ambiente)
        send_to_firestore("luz", luz)
        send_to_firestore("humedad-suelo", humedad_suelo)

        # if current_value != last_value:
            # send_to_firestore("humedad-suelo", {"valor": current_value, "fecha_update": firestore.SERVER_TIMESTAMP})
            
        last_value = current_value
        
        # Espera 5 segundo antes de leer el input nuevamente
        time.sleep(2)  

if __name__ == "__main__":
    main()