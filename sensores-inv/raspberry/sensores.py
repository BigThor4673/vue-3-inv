import firebase_admin
from firebase_admin import credentials, firestore
import time

# Inicializa la aplicación Firebase
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

# Obtén una referencia a la base de datos Firestore
db = firestore.client()

# Función para leer el input y enviar los datos a Firestore
def send_to_firestore(collection_name, document_name, data):
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.set(data)
    print(f"Data sent to Firestore: {data}")

# Simula la lectura de un input que cambia su valor
def read_input():
    # Aquí puedes reemplazar esto con la lógica para leer el input real
    import random
    return random.randint(0, 100)

def main():
    last_value = None
    while True:
        current_value = read_input()
        if current_value != last_value:
            send_to_firestore("inv-data/Inv-001/maceteros/ma-z01/sensores", "humedad-suelo", {"valor": current_value, "fecha-update": firestore.SERVER_TIMESTAMP})
            last_value = current_value
        
        # Espera 5 segundo antes de leer el input nuevamente
        time.sleep(5)  

if __name__ == "__main__":
    main()