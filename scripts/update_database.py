import psycopg2
import getpass
import os

DB_CONFIG = {
    "dbname": "mi_investigacion",
    "user": "postgres",
    "password": "TU_CONTRASEÑA_AQUÍ", 
    "host": "localhost",
    "port": "5432"
}

os.environ['PGCLIENTENCODING'] = 'utf-8'

def actualizar_base_datos():
    if DB_CONFIG["password"] == "TU_CONTRASEÑA_AQUÍ":
        DB_CONFIG["password"] = input("Introduce tu contraseña de PostgreSQL para actualizar la tabla: ")

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        print("Añadiendo columna 'resumen' a la tabla 'documentos_investigacion'...")
        # Intentar añadir la columna (usamos un bloque para que no falle si ya existe)
        try:
            cur.execute("ALTER TABLE documentos_investigacion ADD COLUMN resumen TEXT;")
            conn.commit()
            print("¡Éxito! Columna 'resumen' añadida correctamente.")
        except psycopg2.errors.DuplicateColumn:
            conn.rollback()
            print("La columna 'resumen' ya existe.")

    except Exception as e:
        print(f"Error al actualizar la base de datos: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    actualizar_base_datos()
