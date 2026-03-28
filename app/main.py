import streamlit as st
from db.models import get_db

st.set_page_config(page_title="EvaQuizz", layout="wide")

# Estilo para el logo multicolor
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    .logo-e {
        font-size: 120px;
        font-weight: bold;
        color: #FF69B4;
        text-align: center;
        text-shadow: 2px 2px #FFB6C1;
    }
    .main-title { 
        text-align: center; 
        font-size: 45px; 
        color: #D81B60; 
        font-family: 'Arial'; 
        margin-top: -30px;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
    }
    </style>
    <div class="logo-e">E</div>
    <div class="main-title">EvaQuizz</div>
    """, unsafe_allow_html=True)

# Manejo de sesión
if 'user_role' not in st.session_state:
    st.session_state['user_role'] = None

if st.session_state['user_role'] is None:
    st.subheader("🌸 Sistema de Evaluación Inteligente")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📖 ¿Para qué sirve?
        EvaQuizz es una herramienta diseñada para **simplificar la creación de exámenes** y la **gestión de notas**. 
        Permite a los profesores subir preguntas en segundos y a los estudiantes responder desde cualquier dispositivo.
        
        st.write("### Cómo usarla paso a paso:")
        1. **Registro Docente**: Ingresa tu correo en el panel de la derecha.
        2. **Creación**: Ve a 'Crear Prueba', define un nombre y una palabra clave.
        3. **Preguntas**: Añade las preguntas que desees.
        4. **Acceso Estudiante**: El estudiante usa su nombre y la **palabra clave** para entrar.
        5. **Reporte**: El profe descarga el reporte en la sección 'Resultados'.
        """)

    with col2:
        st.write("### 🔑 Iniciar Sesión")
        tipo_usuario = st.radio("Seleccione su rol:", ["Profesor", "Estudiante"])
        
        if tipo_usuario == "Profesor":
            correo = st.text_input("Correo electrónico institucional")
            if st.button("Acceder como Docente"):
                if correo:
                    st.session_state['user_role'] = "Profesor"
                    st.session_state['user_email'] = correo
                    st.rerun()
        else:
            nombre = st.text_input("Tu nombre completo")
            clave_test = st.text_input("Palabra clave de la prueba", type="password")
            if st.button("Entrar para presentar prueba"):
                if nombre and clave_test:
                    db = get_db()
                    pruebas_ref = db.collection('pruebas').where('clave', '==', clave_test).stream()
                    prueba_doc = next(pruebas_ref, None)
                    if prueba_doc:
                        st.session_state['user_role'] = "Estudiante"
                        st.session_state['estudiante_nombre'] = nombre
                        st.session_state['prueba_id'] = prueba_doc.id
                        st.session_state['clave_acceso'] = clave_test
                        st.rerun()
                    else:
                        st.error("Clave de prueba no válida")

else:
    st.sidebar.write(f"Conectado como: **{st.session_state['user_role']}**")
    if st.button("Cerrar Sesión"):
        st.session_state['user_role'] = None
        st.rerun()

    # Menú filtrado por Rol
    if st.session_state['user_role'] == "Profesor":
        menu = st.sidebar.selectbox("Menú", ["Inicio", "Crear Prueba", "Resultados"])
    else:
        menu = st.sidebar.selectbox("Menú", ["Inicio", "Presentar Prueba"])

    if menu == "Inicio":
        st.success(f"Bienvenido de nuevo. Use el menú lateral para navegar.")
        
    elif menu == "Crear Prueba":
        st.info("Diríjase a la página 'Crear Prueba' en el menú lateral.")
        
    elif menu == "Presentar Prueba":
        st.info("Diríjase a la página 'Presentar Prueba' en el menú lateral.")

    elif menu == "Resultados":
        st.info("Diríjase a la página 'Resultados' en el menú lateral.")

st.markdown("---")
st.caption("EvaQuizz - 2024")
