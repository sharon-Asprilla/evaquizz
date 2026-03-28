import streamlit as st
from db.models import Session, Prueba, Pregunta, Estudiante, Respuesta

session = Session()

st.header("Presentar prueba")

# Verificación de acceso
if st.session_state.get('user_role') != "Estudiante":
    st.warning("Por favor, inicie sesión como Estudiante en la página principal.")
    st.stop()

nombre = st.session_state.get('estudiante_nombre')
clave = st.session_state.get('clave_acceso')
documento = st.text_input("Confirme su Número de documento para el registro")

prueba = session.query(Prueba).filter_by(clave=clave).first()

if prueba and nombre and documento:
    st.subheader(f"Evaluación: {prueba.titulo}")
    estudiante = Estudiante(nombre=nombre, documento=documento, email="")
    session.add(estudiante)
    session.commit()

    preguntas = session.query(Pregunta).filter_by(prueba_id=prueba.id).all()
    respuestas_guardadas = []

    for p in preguntas:
        st.write(p.texto)
        if p.tipo == "multiple":
            opciones = p.opciones.split(",")
            respuesta = st.radio("Selecciona una opción", opciones, key=p.id)
        else:
            respuesta = st.text_area("Respuesta", key=p.id)

        if st.button(f"Guardar respuesta {p.id}"):
            r = Respuesta(estudiante_id=estudiante.id, prueba_id=prueba.id,
                          pregunta_id=p.id, respuesta=respuesta, nota=0)
            session.add(r)
            session.commit()
            st.success("Respuesta guardada")
else:
    st.warning("Ingrese sus datos y la clave para continuar")
