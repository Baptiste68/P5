DROP DATABASE foodexo;
CREATE DATABASE foodexo;
USE foodexo;

DROP TABLE IF EXISTS Users ;
CREATE TABLE Users (
id_Users SMALLINT AUTO_INCREMENT NOT NULL,
name_Users VARCHAR(40),
first_name_Users VARCHAR(40),
username_Users VARCHAR(40),
pwd_Users VARCHAR(40),
PRIMARY KEY (id_Users))ENGINE=InnoDB;

DROP TABLE IF EXISTS Categories ;
CREATE TABLE Categories (
id_Categories SMALLINT AUTO_INCREMENT NOT NULL,
name_Categories VARCHAR(40),
PRIMARY KEY (id_Categories))ENGINE=InnoDB;

DROP TABLE IF EXISTS Food ;
CREATE TABLE Food (
id_Food SMALLINT AUTO_INCREMENT NOT NULL,
name_Food TEXT,
quantity_Food VARCHAR(40),
dangers_Food TEXT,
store_Food VARCHAR(40),
nutri_score_Food CHAR(1),
link_Food TEXT,
PRIMARY KEY (id_Food))ENGINE=InnoDB;

DROP TABLE IF EXISTS saved ;
CREATE TABLE saved (
id_Users SMALLINT NOT NULL,
id_Food SMALLINT NOT NULL,
CONSTRAINT PK_saved PRIMARY KEY (id_Users, id_Food),
FOREIGN KEY (id_Users) REFERENCES Users (id_Users),
FOREIGN KEY (id_Users) REFERENCES Users (id_Users))ENGINE=InnoDB;

DROP TABLE IF EXISTS foodcate ;
CREATE TABLE foodcate (
id_Food SMALLINT NOT NULL,
id_Categories SMALLINT NOT NULL,
CONSTRAINT PK_oodcate PRIMARY KEY (id_Food, id_Categories),
FOREIGN KEY (id_Food) REFERENCES Food (id_Food),
FOREIGN KEY (id_Categories) REFERENCES Categories (id_Categories))ENGINE=InnoDB;