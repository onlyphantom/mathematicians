-- sqlite3 library.db < initial-data.sql

-- Countries
INSERT INTO country (name) VALUES ('German');
INSERT INTO country (name) VALUES ('England');
INSERT INTO country (name) VALUES ('Greek');
INSERT INTO country (name) VALUES ('France');

-- Person
INSERT INTO person (country_id, name) VALUES (2, 'Isaac Newton');
INSERT INTO person (country_id, name) VALUES (4, 'Pierre de Fermat');
INSERT INTO person (country_id, name) VALUES (4, 'Rene Descartes');
INSERT INTO person (country_id, name) VALUES (3, 'Euclid');
INSERT INTO person (country_id, name) VALUES (1, 'Carl Friedrich Gauss');
