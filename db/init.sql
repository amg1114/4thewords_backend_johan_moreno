SET FOREIGN_KEY_CHECKS=0;

CREATE DATABASE IF NOT EXISTS 4thewords_prueba_johan_moreno CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE 4thewords_prueba_johan_moreno;

DROP TABLE IF EXISTS legend;
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS district;
DROP TABLE IF EXISTS canton;
DROP TABLE IF EXISTS province;

CREATE TABLE province (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE canton (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    province_id INT,
    FOREIGN KEY (province_id) REFERENCES province(id)
);

CREATE TABLE district (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    canton_id INT,
    FOREIGN KEY (canton_id) REFERENCES canton(id)
);

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE `user` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE legend (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    date DATE NOT NULL,
    image_url TEXT NOT NULL,
    category_id INT,
    district_id INT,
    canton_id INT,
    province_id INT,
    publisher_id INT,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (district_id) REFERENCES district(id),
    FOREIGN KEY (canton_id) REFERENCES canton(id),
    FOREIGN KEY (province_id) REFERENCES province(id),
    FOREIGN KEY (publisher_id) REFERENCES `user`(id)
);

-- Insertar datos
INSERT INTO province (name) VALUES 
('San Jose'), ('Alajuela'), ('Cartago'), ('Heredia'), ('Puntarenas');

INSERT INTO canton (name, province_id) VALUES 
('Central SJ', 1), ('Central Alajuela', 2), ('Central Cartago', 3), ('Central Heredia', 4), ('Central Puntarenas', 5);

INSERT INTO district (name, canton_id) VALUES 
('Carmen', 1), ('San Josecito', 2), ('Oriental', 3), ('Mercedes', 4), ('Barranca', 5);

INSERT INTO category (name, description) VALUES
('Leyenda', 'Historias tradicionales'),
('Mito', 'Narraciones sobrenaturales'),
('Cuento', 'Relatos breves'),
('Historia real', 'Basadas en hechos'),
('Tradicion oral', 'Pasadas de generacion en generacion');

INSERT INTO `user` (name, email, password) VALUES
('Alejandro Moreno', 'alejandro@example.com', '$2b$12$1cQR6jSeT1.1CJMlXyUSS.yJEdJtww4/pcuBEtL4L7rSetQGA/tNG'),
('Ana Perez', 'ana@example.com', '$2b$12$1cQR6jSeT1.1CJMlXyUSS.yJEdJtww4/pcuBEtL4L7rSetQGA/tNG'),
('Luis Gomez', 'luis@example.com', '$2b$12$1cQR6jSeT1.1CJMlXyUSS.yJEdJtww4/pcuBEtL4L7rSetQGA/tNG');

INSERT INTO legend (name, description, date, image_url, category_id, district_id, canton_id, province_id, publisher_id) VALUES
('La carreta sin bueyes', 'Una carreta maldita que viaja sola', '2023-01-01', 'http://localhost:8080/images/0952134b8ed24a8cb9adf6c7596bc6a7.jpg', 1, 1, 1, 1, 1),
('El padre sin cabeza', 'Un sacerdote decapitado aparece de noche', '2022-01-02', 'http://localhost:8080/images/f086419f3d1f4d668349abc9612d32f7.jpg', 2, 2, 2, 2, 1),
('La Tulevieja', 'Espíritu femenino que castiga a hombres infieles', '2021-01-03', 'http://localhost:8080/images/262fd081a3c445cbb8e7c493054c4107.jpg', 3, 3, 3, 3, 2),
('El cadejos', 'Perro negro que sigue a los borrachos', '2020-01-04', 'http://localhost:8080/images/3956f481f9ba4878a5b1b5fa865bb36f.jpg', 1, 4, 4, 4, 2),
('La llorona tica', 'Mujer que llora a sus hijos perdidos', '2019-01-05', 'http://localhost:8080/images/f363209527704e9ab1eb9dea707f30ed.webp', 5, 5, 5, 5, 1),
('Los duendes del bosque', 'Criaturas traviesas en las montañas', '2018-01-06', 'http://localhost:8080/images/42a6338e7b7c43c39830dddfb8810afc.webp', 4, 1, 1, 1, 2),
('La monja del colegio', 'Aparece en escuelas abandonadas', '2017-01-07', 'http://localhost:8080/images/3c482bf058fe4f09bc40e035d9650bf9.jpg', 2, 2, 2, 2, 1),
('El jinete nocturno', 'Caballo fantasma sin jinete visible', '2016-01-08', 'http://localhost:8080/images/272aefe0e3b344b6aafe7201535f5ac4.jpg', 3, 3, 3, 3, 1),
('El pozo maldito', 'Lugar donde desaparecen animales', '2015-01-09', 'http://localhost:8080/images/9ee875bcd3c74e43bd70ee2178980256.jpg', 1, 4, 4, 4, 2),
('La sombra del río', 'Figura oscura junto al agua', '2014-01-10', 'http://localhost:8080/images/48abff99e9b642c882d68afa783902eb.jpg', 5, 5, 5, 5, 2);

SET FOREIGN_KEY_CHECKS=1;
