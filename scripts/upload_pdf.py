import psycopg2
from psycopg2 import Binary
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# CONFIGURACIÓN DE LA BASE DE DATOS
# Cambia estos valores según tu configuración en pgAdmin
DB_CONFIG = {
    "dbname": "mi_investigacion",
    "user": "postgres",
    "password": "TU_CONTRASEÑA_AQUÍ", # <--- CAMBIA ESTO
    "host": "localhost",
    "port": "5432"
}

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw() # Ocultar la ventana principal de tkinter
    path = filedialog.askopenfilename(
        title="Selecciona el archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    return path

def subir_a_postgres(file_path, nombre_usuario):
    try:
        # 1. Conectarse a la base de datos
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. Leer el archivo en formato binario
        with open(file_path, "rb") as file:
            blob_data = file.read()

        file_name = os.path.basename(file_path)

        # 3. Insertar en la tabla
        query = """
        INSERT INTO documentos_investigacion (nombre_usuario, nombre_archivo, contenido_pdf)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (nombre_usuario, file_name, Binary(blob_data)))

        # 4. Confirmar cambios
        conn.commit()
        print(f"¡Éxito! Archivo '{file_name}' subido correctamente.")
        messagebox.showinfo("Éxito", f"Archivo '{file_name}' subido correctamente.")

    except Exception as e:
        print(f"Error al subir: {e}")
        messagebox.showerror("Error", f"No se pudo subir el archivo: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    print("--- Subidor de PDFs a PostgreSQL ---")
    
    usuario = input("Introduce tu nombre: ")
    archivo = seleccionar_archivo()

    if archivo:
        print(f"Subiendo {archivo}...")
        subir_a_postgres(archivo, usuario)
    else:
        print("No se seleccionó ningún archivo.")
