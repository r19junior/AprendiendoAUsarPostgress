-- ARCHIVO DE CONFIGURACIÓN INICIAL DE POSTGRESQL

-- 1. Crear la base de datos (Ejecuta esto en la consola de 'postgres' o pgAdmin)
-- CREATE DATABASE mi_investigacion;

-- 2. Esquema de ejemplo (Asegúrate de estar conectado a 'mi_investigacion' antes de correr lo siguiente)

-- Tabla para almacenar proyectos de investigación
CREATE TABLE IF NOT EXISTS proyectos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,
    investigador_nombre VARCHAR(100),
    fecha_inicio DATE DEFAULT CURRENT_DATE,
    estado VARCHAR(20) DEFAULT 'en_progreso'
);

-- Insertar datos iniciales para probar
INSERT INTO proyectos (titulo, descripcion, investigador_nombre)
VALUES 
('Análisis de Datos con Postgres', 'Estudio sobre el rendimiento de consultas relacionales.', 'Usuario Investigador');

-- Consulta de verificación
-- SELECT * FROM proyectos;
