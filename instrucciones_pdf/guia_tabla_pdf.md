# Cómo crear una tabla para Nombres y PDFs

Para guardar documentos como PDFs en PostgreSQL, existen dos enfoques principales. Aquí te explicamos el más directo para tu investigación.

## 1. El tipo de dato `BYTEA`
En Postgres, usamos `BYTEA` para guardar datos binarios (como archivos).

### El comando SQL:
```sql
CREATE TABLE documentos_investigacion (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    nombre_archivo VARCHAR(255),
    contenido_pdf BYTEA, -- Aquí se guarda el archivo real
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 2. ¿Cómo se visualizaría "en un costado"?
Aunque la base de datos guarda los datos en filas, la idea de "subir en un costado" se resuelve en la **Interfaz de Usuario**:

- **En la Tabla**: Tendrás una columna con el nombre y otra que indica si hay un PDF.
- **En la Interfaz**: Puedes diseñar una aplicación donde a la izquierda veas la lista de nombres y a la derecha un visor de PDF o un botón de "Subir".

## 3. Ejemplo de Insert (Concepto)
Para insertar un nombre y un archivo desde una aplicación, la consulta se vería así:
```sql
INSERT INTO documentos_investigacion (nombre_usuario, nombre_archivo, contenido_pdf)
VALUES ('Juan Perez', 'tesis_v1.pdf', <datos_binarios_del_archivo>);
```

## 4. ¿Cómo subir el PDF si soy principiante?
PostgreSQL no permite "arrastrar y soltar" un archivo PDF directamente en la cuadrícula de pgAdmin. Normalmente, esto se hace mediante una pequeña aplicación (en Python, Node.js o C#) que convierte el archivo en bits y los manda a la columna `BYTEA`.

### La alternativa fácil: "La Ruta"
Si te parece muy complicado manejar archivos binarios (`BYTEA`), puedes usar este enfoque:
1. Crea una carpeta en tu Windows llamada `C:\MisPDFs`.
2. En tu tabla de Postgres, en lugar de `contenido_pdf BYTEA`, usa `ruta_pdf VARCHAR(500)`.
3. Simplemente escribe el texto de dónde está el archivo: `C:\MisPDFs\tesis_juan.pdf`.

> [!TIP]
> **¿Te gustaría que te ayude con un script pequeño de Python?** Podrás seleccionar un archivo de tu computadora y se subirá automáticamente a la tabla que acabamos de crear. ¡Es la forma más rápida de verlo funcionar!

## 5. Instrucciones para usar el script de Python
He creado el script en `scripts/upload_pdf.py`. Para usarlo:

1.  **Instala Python** (si no lo tienes) desde [python.org](https://www.python.org/).
2.  **Instala la librería necesaria**: Abre una terminal y escribe:
    ```bash
    pip install psycopg2-binary
    ```
3.  **Configura el script**: Abre `scripts/upload_pdf.py` y pon tu contraseña de Postgres donde dice `TU_CONTRASEÑA_AQUÍ`.
4.  **Ejecuta el script**:
    ```bash
    python scripts/upload_pdf.py
    ```
5.  **Sigue los pasos**: Te pedirá tu nombre y se abrirá una ventana para elegir el PDF.
