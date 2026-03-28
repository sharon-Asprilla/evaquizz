import streamlit as st
from db.models import get_db
import datetime

db = get_db()

# Verificación de seguridad
if st.session_state.get('user_role') != "Profesor":
    st.error("Acceso denegado. Solo profesores.")
    st.stop()

st.header("Crear nueva prueba")
titulo = st.text_input("Título de la prueba")
clave = st.text_input("Clave (6-15 caracteres)")
duracion = st.number_input("Duración en minutos", min_value=1)
fecha = st.date_input("Fecha de aplicación")

if st.button("Crear Prueba Base"):
    nueva_prueba = {
        "titulo": titulo,
        "clave": clave,
        "duracion": duracion,
        "fecha": str(fecha)
    }
    doc_ref = db.collection('pruebas').add(nueva_prueba)
    st.success(f"Prueba '{titulo}' creada. Ahora añade las preguntas abajo.")
    st.session_state['ultima_prueba_id'] = doc_ref[1].id

if 'ultima_prueba_id' in st.session_state:
    st.divider()
    st.subheader("Añadir Preguntas a la prueba")
    texto_p = st.text_area("Texto de la pregunta")
    tipo_p = st.selectbox("Tipo", ["multiple", "abierta"])
    opciones_p = st.text_input("Opciones (separadas por coma si es múltiple)")
    correcta_p = st.text_input("Respuesta correcta")
    
    if st.button("Guardar Pregunta"):
        pregunta_data = {
            "texto": texto_p,
            "tipo": tipo_p,
            "opciones": opciones_p,
            "respuesta_correcta": correcta_p,
            "prueba_id": st.session_state['ultima_prueba_id']
        }
        db.collection('preguntas').add(pregunta_data)
        st.success("Pregunta añadida correctamente")
