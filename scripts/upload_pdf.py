import psycopg2
from psycopg2 import Binary
import tkinter as tk
from tkinter import filedialog, messagebox
import os

import getpass

# CONFIGURACIÓN DE LA BASE DE DATOS
DB_CONFIG = {
    "dbname": "mi_investigacion",
    "user": "postgres",
    "password": "TU_CONTRASEÑA_AQUÍ", 
    "host": "localhost",
    "port": "5432"
}

# FORZAR CODIFICACIÓN UTF-8 PARA EVITAR ERRORES EN WINDOWS
os.environ['PGCLIENTENCODING'] = 'utf-8'

def seleccionar_archivo():
    print("\n[Abriendo ventana de selección de archivos...]")
    root = tk.Tk()
    root.withdraw() 
    root.attributes("-topmost", True) # Intentar que aparezca siempre arriba
    path = filedialog.askopenfilename(
        title="Selecciona el archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    root.destroy()
    return path

import traceback

def subir_a_postgres(file_path, nombre_usuario):
    try:
        # 1. Conectarse a la base de datos
        print(f"\nIntentando conectar a DB '{DB_CONFIG['dbname']}' en localhost...")
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor()
        print("¡Conexión exitosa!")

        # 2. Leer el archivo en formato binario
        print(f"Leyendo archivo: {os.path.basename(file_path)}")
        with open(file_path, "rb") as file:
            blob_data = file.read()

        file_name = os.path.basename(file_path)

        # 3. Insertar en la tabla
        print(f"Subiendo a la tabla... (Usuario: {nombre_usuario})")
        query = """
        INSERT INTO documentos_investigacion (nombre_usuario, nombre_archivo, contenido_pdf)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (nombre_usuario, file_name, Binary(blob_data)))

        # 4. Confirmar cambios
        conn.commit()
        print(f"--- ¡ÉXITO! Archivo subido correctamente. ---")
        messagebox.showinfo("Éxito", f"Archivo '{file_name}' subido correctamente.")

    except Exception as e:
        error_msg = str(e)
        print("\n" + "!"*30)
        print("ERROR AL SUBIR:")
        traceback.print_exc()
        print("!"*30)
        messagebox.showerror("Error", f"No se pudo subir el archivo.\n\nDetalle: {error_msg}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    print("========================================")
    print("   SUBIDOR DE PDFs A POSTGRESQL")
    print("========================================")
    
    # Usamos input normal para evitar que parezca colgado en algunos terminales
    if DB_CONFIG["password"] == "TU_CONTRASEÑA_AQUÍ":
        print("\n[Configuración requerida]")
        DB_CONFIG["password"] = input("Introduce tu contraseña de PostgreSQL: ")

    usuario = input("Introduce tu nombre de investigador: ")
    archivo = seleccionar_archivo()

    if archivo:
        print(f"Seleccionado: {archivo}")
        subir_a_postgres(archivo, usuario)
    else:
        print("\n[!] Cancelado: No se seleccionó ningún archivo.")
