import psycopg2
import os
import fitz # PyMuPDF

DB_CONFIG = {
    "dbname": "mi_investigacion",
    "user": "postgres",
    "password": "TU_CONTRASEÑA_AQUÍ", 
    "host": "localhost",
    "port": "5432"
}

os.environ['PGCLIENTENCODING'] = 'utf-8'

def generar_resumen_ia(texto):
    # Por ahora, simulamos un resumen extrayendo los primeros 500 caracteres
    # Aquí es donde se podría integrar la API de Llama, OpenAI, etc.
    if not texto:
        return "No se pudo extraer texto del documento."
    
    resumen = texto[:500].strip() + "..."
    return f"[RESUMEN AUTOMÁTICO]: {resumen}"

def procesar_nuevos_pdfs():
    if DB_CONFIG["password"] == "TU_CONTRASEÑA_AQUÍ":
        DB_CONFIG["password"] = input("Contraseña de Postgres: ")

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 1. Buscar documentos que no tengan resumen
        cur.execute("SELECT id, nombre_archivo, contenido_pdf FROM documentos_investigacion WHERE resumen IS NULL;")
        filas = cur.fetchall()

        if not filas:
            print("No hay documentos nuevos para resumir.")
            return

        for doc_id, nombre, contenido in filas:
            print(f"Procesando resumen para: {nombre}...")
            
            # 2. Guardar temporalmente el binario para que PyMuPDF lo lea
            temp_path = f"temp_{nombre}"
            with open(temp_path, "wb") as f:
                f.write(contenido)

            # 3. Extraer texto
            texto_completo = ""
            doc = fitz.open(temp_path)
            for pagina in doc:
                texto_completo += pagina.get_text()
            doc.close()
            os.remove(temp_path)

            # 4. Generar resumen
            resumen = generar_resumen_ia(texto_completo)

            # 5. Guardar resumen en la base de datos
            cur.execute("UPDATE documentos_investigacion SET resumen = %s WHERE id = %s;", (resumen, doc_id))
            conn.commit()
            print(f"¡Resumen guardado para {nombre}!")

    except Exception as e:
        print(f"Error al procesar resúmenes: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    procesar_nuevos_pdfs()
