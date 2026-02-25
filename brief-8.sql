create database Biblio_Tech;

use Biblio_Tech;

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    type_doc ENUM('livre','magazine') NOT NULL,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE livres (
    document_id INT PRIMARY KEY,
    auteur VARCHAR(100) NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id) 
);


CREATE TABLE magazines (
    document_id INT PRIMARY KEY,
    numero INT NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id) 
);


CREATE TABLE membres (
    id_membre INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) UNIQUE NOT NULL
);


CREATE TABLE emprunts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    membre_id INT NOT NULL,
    document_id INT NOT NULL,
    date_emprunt DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_retour DATETIME NULL,

    FOREIGN KEY (membre_id) REFERENCES membres(id_membre),
    FOREIGN KEY (document_id) REFERENCES documents(id) 
);

select * from livres;

