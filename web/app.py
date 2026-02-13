from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "mi_investigacion",
    "user": "postgres",
    "password": "TU_CONTRASEÑA_AQUÍ", 
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre_usuario, nombre_archivo, resumen, fecha_subida FROM documentos_investigacion ORDER BY fecha_subida DESC;")
        documentos = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', documentos=documentos)
    except Exception as e:
        return f"Error de conexión: {e}. Asegúrate de configurar la contraseña en el archivo scripts/upload_pdf.py o app.py"

if __name__ == '__main__':
    # Obtener contraseña si no está configurada
    if DB_CONFIG["password"] == "TU_CONTRASEÑA_AQUÍ":
        print("\n[!] Configuración del Dashboard:")
        DB_CONFIG["password"] = input("Introduce tu contraseña de PostgreSQL para iniciar el servidor: ")
    
    app.run(debug=True, port=5000)
