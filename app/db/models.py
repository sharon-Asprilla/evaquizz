import firebase_admin
from firebase_admin import credentials, firestore
import os

def init_db():
    if not firebase_admin._apps:
        # Asegúrate de tener tu llave de firebase en esta ruta
        path = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
        if os.path.exists(path):
            cred = credentials.Certificate(path)
            firebase_admin.initialize_app(cred)
        else:
            print("Error: No se encontró serviceAccountKey.json en app/db/")

def get_db():
    init_db()
    return firestore.client()
