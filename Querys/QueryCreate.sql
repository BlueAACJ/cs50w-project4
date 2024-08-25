CREATE DATABASE MapaInteractivo;
USE MapaInteractivo;

-- Crear la tabla 'departamento' 
CREATE TABLE departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(24) NOT NULL UNIQUE
);

-- Crear la tabla 'Imagen'
CREATE TABLE Imagen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url_imagen1 TEXT,
    url_imagen2 TEXT,
    url_imagen3 TEXT,
    url_imagen4 TEXT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

-- Crear la tabla 'Historia' 
CREATE TABLE Historia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parrafo1 TEXT,
    parrafo2 TEXT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

-- Crear la tabla 'Cultura' 
CREATE TABLE Cultura (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parrafo1 TEXT,
    parrafo2 TEXT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

-- Crear la tabla 'Geografia'
CREATE TABLE Geografia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parrafo1 TEXT,
    parrafo2 TEXT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

-- Crear la tabla 'Puntuacion'
CREATE TABLE Puntuacion(
	id INT auto_increment primary key,
    usuario text,
    puntuacion  text
);