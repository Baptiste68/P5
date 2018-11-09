USE foodexo;
DELETE FROM foodcate;
DELETE FROM Categories;
DELETE FROM Food;

INSERT INTO Food ( name_food, quantity_food, dangers_food, store_food, nutri_score_food, link_food )
VALUES ('Tomates', '200g', 'Eau, Fruit', 'SuperU', 'A', 'http://ici.com'),
('Pommes de terre', '1kg', 'Terre', 'Leclerc', 'C', 'http://ici.com'),
('Poireaux', '100g', 'Eau', 'Lidl', 'B',  'http://ici.com'),
('Anchois', '200g', 'Eau, Poissons', 'Lidl', 'B', 'http://ici.com'),
('Pain', '350g', 'Farine', 'Aldi', 'A', 'http://ici.com'),
('Jus de pomme', '1L', 'Eau, Fruit', 'SuperU', 'D', 'http://ici.com');


INSERT INTO Categories ( name_categories )
VALUES ('Fruit'), ('Legumes'), ('Poissons'), ('Liquide'), ('Divers');


INSERT INTO foodcate
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Tomates') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Fruit' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Tomates') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Legumes' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Pommes de terre') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Legumes' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Anchois') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Poissons' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Pain') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Divers' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Jus de pomme') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Liquide' ) AS c
UNION ALL
SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = 'Poireaux') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = 'Legumes' ) AS c;