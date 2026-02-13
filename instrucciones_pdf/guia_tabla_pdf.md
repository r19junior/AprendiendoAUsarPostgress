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

> [!TIP]
> Si los PDFs son muy grandes (más de 10MB), lo ideal es guardar el PDF en una carpeta de tu computadora y en la base de datos solo guardar la **ruta del archivo** (un texto como `C:/documentos/archivo.pdf`).
