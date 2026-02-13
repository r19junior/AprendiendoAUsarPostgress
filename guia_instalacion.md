# Guía de Instalación de PostgreSQL en Windows

Sigue estos pasos detallados para tener tu base de datos lista:

## 1. Descarga
Vete a la página oficial de descargas: [PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) y elige la versión más reciente para Windows (ej. 16.x o 17.x).

## 2. Instalación Paso a Paso
1.  **Directorio de Instalación**: Puedes dejar el por defecto (`C:\Program Files\PostgreSQL\16`).
2.  **Componentes**: Asegúrate de que estén marcados todos:
    *   PostgreSQL Server
    *   pgAdmin 4 (Interfaz gráfica)
    *   Stack Builder
    *   Command Line Tools (psql)
3.  **Directorio de Datos**: Por defecto está bien.
4.  **Contraseña**: **IMPORTANTE**. Escribe una contraseña para el usuario `postgres` y guárdala bien. La necesitarás cada vez que quieras entrar.
5.  **Puerto**: El estándar es `5432`. Déjalo así a menos que sepas que está ocupado.
6.  **Configuración Regional (Locale)**: Puedes elegir `Spanish, Spain` o `Spanish, Mexico` según tu preferencia, o dejarlo en `[Default locale]`.

## 3. Acceso inicial y creación de la BD (pgAdmin 4)
Al finalizar, busca en tu inicio de Windows una aplicación llamada **pgAdmin 4**. Ábrela.

1. **Conexión**: En la columna de la izquierda, haz clic en **Servers** (te pedirá la contraseña que anotaste).
2. **Crear la base de datos**: 
   * Haz clic derecho sobre **Databases** > **Create** > **Database...**
   * Ponle un nombre, por ejemplo: `mi_investigacion` y dale a **Save**.

## 4. Crear tu primera tabla (Query Tool)
1. Haz clic derecho sobre tu nueva base de datos (`mi_investigacion`).
2. Selecciona la opción **Query Tool**. Se abrirá un panel en blanco a la derecha.
3. Copia y pega el código de creación de tablas:
```sql
CREATE TABLE documentos_investigacion (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    nombre_archivo VARCHAR(255),
    contenido_pdf BYTEA, 
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
4. Presiona el icono del **rayo** o la tecla **F5**. Si abajo dice "Query returned successfully", ¡ya tienes tu estructura!

## 5. ¿Cómo ver los datos?
1. En el árbol de la izquierda, busca: `Databases` > `mi_investigacion` > `Schemas` > `public` > `Tables`.
2. Haz clic derecho sobre `documentos_investigacion`.
3. Selecciona **View/Edit Data** > **All Rows**.
