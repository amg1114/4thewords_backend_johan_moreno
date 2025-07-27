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
('Alejandro Moreno', 'alejandro@example.com', '123456'),
('Ana Perez', 'ana@example.com', '123456'),
('Luis Gomez', 'luis@example.com', '123456');

INSERT INTO legend (name, description, date, image_url, category_id, district_id, canton_id, province_id, publisher_id) VALUES
('La carreta sin bueyes', 'Una carreta maldita que viaja sola', '2024-01-01', 'http://example.com/img1.jpg', 1, 1, 1, 1, 1),
('El padre sin cabeza', 'Un sacerdote decapitado aparece de noche', '2024-01-02', 'http://example.com/img2.jpg', 2, 2, 2, 2, 1),
('La Tulevieja', 'Espíritu femenino que castiga a hombres infieles', '2024-01-03', 'http://example.com/img3.jpg', 3, 3, 3, 3, 2),
('El cadejos', 'Perro negro que sigue a los borrachos', '2024-01-04', 'http://example.com/img4.jpg', 1, 4, 4, 4, 2),
('La llorona tica', 'Mujer que llora a sus hijos perdidos', '2024-01-05', 'http://example.com/img5.jpg', 5, 5, 5, 5, 1),
('Los duendes del bosque', 'Criaturas traviesas en las montañas', '2024-01-06', 'http://example.com/img6.jpg', 4, 1, 1, 1, 2),
('La monja del colegio', 'Aparece en escuelas abandonadas', '2024-01-07', 'http://example.com/img7.jpg', 2, 2, 2, 2, 1),
('El jinete nocturno', 'Caballo fantasma sin jinete visible', '2024-01-08', 'http://example.com/img8.jpg', 3, 3, 3, 3, 1),
('El pozo maldito', 'Lugar donde desaparecen animales', '2024-01-09', 'http://example.com/img9.jpg', 1, 4, 4, 4, 2),
('La sombra del río', 'Figura oscura junto al agua', '2024-01-10', 'http://example.com/img10.jpg', 5, 5, 5, 5, 2);

SET FOREIGN_KEY_CHECKS=1;
