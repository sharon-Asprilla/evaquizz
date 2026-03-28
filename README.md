# evaquizz
Es una web donde los profesores pueden crear sus propias evaluaciones personalizadas con un diseño moderno en tonos rosados.

## 🚀 Características
- **Base de Datos**: Utiliza **Firebase Firestore** para almacenamiento en tiempo real y alta disponibilidad.
- **Roles**: Diferenciación entre Profesor (creador) y Estudiante (usuario).
- **Seguridad**: Acceso mediante palabras clave únicas por examen.
- **Reportes**: Generación de resultados en Excel y PDF.

## 🛠️ Configuración
1. Instalar dependencias: `pip install streamlit firebase-admin pandas fpdf`.
2. Colocar el archivo `serviceAccountKey.json` en `app/db/`.
3. Ejecutar: `streamlit run app/main.py`.

## 🎨 Estilo
La aplicación cuenta con una identidad visual basada en el color **Rosado (Pink)** para una interfaz amigable y clara.
