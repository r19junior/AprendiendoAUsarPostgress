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

## 3. Verificación
Una vez finalizado:
1.  Busca en tu menú de inicio **pgAdmin 4** y ábrelo.
2.  Despliega "Servers" en el lado izquierdo.
3.  Te pedirá la contraseña que configuraste. Ponla y ya estarás dentro del sistema de base de datos.

## 4. Crear tu DB
Puedes hacer clic derecho en "Databases" -> "Create" -> "Database..." y ponerle el nombre `mi_investigacion`.
