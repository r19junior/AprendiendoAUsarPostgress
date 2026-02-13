# 🗺️ Mi Ruta de Trabajo: PostgreSQL + Python

¡Entiendo! Aquí tienes tu mapa maestro. Sigue este orden de arriba hacia abajo para no perderte nunca.

## 🟢 ETAPA 1: Preparación (Ya lo hicimos)
1.  **Instalar PostgreSQL**: El "motor" donde viven los datos. ([Guía Detallada](file:///d:/proyecto%20de%20investigacion/usoPOstgress/guia_instalacion.md))
2.  **Configurar pgAdmin**: La "ventana" para ver los datos visualmente.
3.  **Instalar Python y Librerías**: El "puente" para conectar tu PC con Postgres.
    *   Comando usado: `pip install psycopg2-binary`

---

## 🔵 ETAPA 2: El Script de Subida (Tu herramienta diaria)
Cada vez que quieras subir un PDF a tu base de datos, haz esto:

1.  **Abre tu terminal** en VS Code.
2.  **Activa tu entorno** (si es necesario): `.\.venv\Scripts\activate`
3.  **Ejecuta el script**:
    ```powershell
    python scripts/upload_pdf.py
    ```
4.  **Sigue las instrucciones en pantalla**:
    *   Pon tu contraseña.
    *   Pon tu nombre.
    *   Elige el archivo en la ventana que se abre.

---

## 🟡 ETAPA 3: ¿Cómo reviso mis datos? (pgAdmin)
Si quieres ver qué hay guardado, haz esto:

1.  Abre **pgAdmin 4**.
2.  Busca tu tabla: `Databases` > `mi_investigacion` > `Schemas` > `public` > `Tables`.
3.  Haz clic derecho sobre **`documentos_investigacion`**.
4.  Elige **View/Edit Data** > **All Rows**.

---

## 📂 Organización de tus archivos
*   `scripts/setup.sql`: Contiene el código para "construir" la tabla (si borraras la BD, usas esto para reconstruirla).
*   `scripts/upload_pdf.py`: Tu aplicación para subir PDFs.
*   `introduccion_postgres.md`: Diccionario de conceptos por si olvidas qué es cada cosa.

---

## 🚀 ¿Qué sigue?
Ahora que ya sabes subir archivos, podrías:
*   Crear una tabla para **Notas de Investigación** que se relacionen con tus PDFs.
*   Hacer un script para **Descargar/Extraer** los PDFs de la base de datos a tu escritorio.

**¿Ves el camino más claro ahora?** Guarda este archivo como tu referencia principal.
