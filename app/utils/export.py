import pandas as pd
from fpdf import FPDF
from db.models import Session, Respuesta, Estudiante

def export_excel():
    session = Session()
    data = []
    for r in session.query(Respuesta).all():
        estudiante = session.query(Estudiante).get(r.estudiante_id)
        data.append({
            "Nombre": estudiante.nombre,
            "Documento": estudiante.documento,
            "Email": estudiante.email,
            "Prueba": r.prueba_id,
            "Pregunta": r.pregunta_id,
            "Respuesta": r.respuesta,
            "Nota": r.nota
        })
    df = pd.DataFrame(data)
    df.to_excel("resultados.xlsx", index=False)

def export_pdf():
    session = Session()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for r in session.query(Respuesta).all():
        estudiante = session.query(Estudiante).get(r.estudiante_id)
        pdf.cell(200, 10, txt=f"{estudiante.nombre} ({estudiante.documento}) - Nota: {r.nota}", ln=True)
    pdf.output("resultados.pdf")
