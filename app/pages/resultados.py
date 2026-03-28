import streamlit as st
from utils.export import export_excel, export_pdf

# Verificación de seguridad
if st.session_state.get('user_role') != "Profesor":
    st.error("Solo los profesores pueden ver los resultados.")
    st.stop()

st.header("Resultados de pruebas")

if st.button("Exportar Excel"):
    export_excel()
    st.success("Archivo Excel generado")

if st.button("Exportar PDF"):
    export_pdf()
    st.success("Archivo PDF generado")
