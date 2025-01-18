import datetime
import sqlite3
import firebase_admin
from firebase_admin import credentials, firestore
import time
import random
import json
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env en el directorio superior
load_dotenv(dotenv_path='../../.env')

# Inicializa la aplicación Firebase
# cred = credentials.Certificate("firebase.json")

jsonFirebase = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}

cred = credentials.Certificate(jsonFirebase)
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
    # print(f"Data sent to Firestore: {pre_data}")

# Simula la lectura de un input que cambia su valor
def read_input():
    # return random.randint(0, 100)
    text = '{"temperatura-ambiente": '+str(random.randint(10, 40))+', "humedad-ambiente": '+str(random.randint(0, 30))+', "luz": '+str(random.randint(0, 1))+', "humedad-suelo": '+str(random.randint(0, 100))+'}'

    print(f"Lectura de input: {text}")
    return text

def lastValueSensorSqlite(nombre_sensor):
    db = sqlite3.connect('sensores.db')
    cursor = db.cursor()
    cursor.execute("SELECT sr.valor FROM sensores_registros sr JOIN sensores s ON sr.id_sensor = s.id WHERE s.nombre = ? ORDER BY sr.id DESC LIMIT 1", (nombre_sensor,))
    result = cursor.fetchone()
    current_value = result[0] if result is not None else None
    db.close()
    return current_value

def insertValueSensorSqlite(nombre_sensor, valor, fecha):
    db = sqlite3.connect('sensores.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO sensores_registros (id_sensor, valor, fecha_registro) VALUES ((SELECT id FROM sensores WHERE nombre = ?), ?, ?)", (nombre_sensor, valor, fecha))
    db.commit()
    db.close()

# Función principal
def main():
    while True:
        dateStringActual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"@@@@@ Fecha lectura de input: {dateStringActual}")
        current_value = json.loads(read_input())

        temperatura_ambiente = current_value['temperatura-ambiente']
        humedad_ambiente = current_value['humedad-ambiente']
        luz = current_value['luz']
        humedad_suelo = current_value['humedad-suelo']

        last_value = lastValueSensorSqlite("temperatura-ambiente")
        if temperatura_ambiente != last_value:
            insertValueSensorSqlite("temperatura-ambiente", temperatura_ambiente, dateStringActual)
            send_to_firestore("temperatura-ambiente", temperatura_ambiente)
            print(f"***** Firestore temperatura-ambiente: {temperatura_ambiente}, antes: {last_value}")
        else:
            print(f"xxxxx Los valores de TEMPERATURA-AMBIENTE son iguales", temperatura_ambiente, last_value)
        

        last_value = lastValueSensorSqlite("humedad-ambiente")
        if humedad_ambiente != last_value:
            insertValueSensorSqlite("humedad-ambiente", humedad_ambiente, dateStringActual)
            send_to_firestore("humedad-ambiente", humedad_ambiente)
            print(f"***** Firestore humedad-ambiente: {humedad_ambiente}, antes: {last_value}")
        else:
            print(f"xxxxx Los valores de HUMEDAD-AMBIENTE son iguales", humedad_ambiente, last_value)

        last_value = lastValueSensorSqlite("luz")
        if luz != last_value:
            insertValueSensorSqlite("luz", luz, dateStringActual)
            luzFirestore = True if luz == 1 else False
            send_to_firestore("luz", luzFirestore)
            print(f"***** Firestore luz: {luzFirestore}, antes: {last_value}")
        else:
            print(f"xxxxx Los valores de LUZ son iguales", luz, last_value)

        last_value = lastValueSensorSqlite("humedad-suelo")
        if humedad_suelo != last_value:
            insertValueSensorSqlite("humedad-suelo", humedad_suelo, dateStringActual)
            send_to_firestore("humedad-suelo", humedad_suelo)
            print(f"***** Firestore humedad-suelo: {humedad_suelo}, antes: {last_value}")
        else:
            print(f"xxxxx Los valores de HUMEDAD-SUELO son iguales", humedad_suelo, last_value)

        
        # Tiempo de espera antes del loop
        wait_time = 5
        print(f"========== Esperando {wait_time} segundos... ==========")
        print()
        time.sleep(wait_time)  

if __name__ == "__main__":
    main()