USE foodexo;

DELETE FROM Users;
INSERT INTO Users ( name_Users, first_name_Users, username_Users, pwd_Users )
VALUES ('Baptiste', 'Simon', 'Bsim', 'mdp'), 
('Jean', 'Emarre', 'Jema', 'mdp111');


DELETE FROM Food;
INSERT INTO Food ( name_Food, quantity_Food, dangers_Food, store_Food, nutri_score_Food, link_Food )
VALUES ('Tomates', '200g', 'Eau, Fruit', 'SuperU', 'A', 'http://ici.com'),
('Pommes de terre', '1kg', 'Terre', 'Leclerc', 'C', 'http://ici.com'),
('Anchois', '200g', 'Eau, Poissons', 'Lidl', 'B', 'http://ici.com'),
('Pain', '350g', 'Farine', 'Aldi', 'A', 'http://ici.com'),
('Jus de pomme', '1L', 'Eau, Fruit', 'SuperU', 'D', 'http://ici.com');


DELETE FROM Categories;
INSERT INTO Categories ( name_Categories )
VALUES ('Fruit'), ('Legumes'), ('Poissons'), ('Liquide'), ('Divers');


DELETE FROM foodcate;
INSERT INTO foodcate
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Tomates') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Fruit' ) AS c
UNION ALL
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Tomates') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Legumes' ) AS c
UNION ALL
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Pommes de terre') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Legumes' ) AS c
UNION ALL
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Anchois') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Poissons' ) AS c
UNION ALL
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Pain') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Divers' ) AS c
UNION ALL
SELECT f.id_Food, c.id_Categories FROM ( SELECT id_Food FROM Food WHERE name_Food = 'Jus de pomme') AS f CROSS JOIN ( SELECT id_Categories FROM Categories WHERE name_Categories = 'Liquide' ) AS c;