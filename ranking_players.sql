--
-- File generated with SQLiteStudio v3.2.1 on mi. may. 22 12:21:27 2019
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: RegistreDragon
DROP TABLE IF EXISTS RegistreDragon;
CREATE TABLE RegistreDragon (id INTEGER PRIMARY KEY AUTOINCREMENT, pseudonim VARCHAR (12) NOT NULL, nivell INTEGER NOT NULL, email VARCHAR (24) NOT NULL, nacionalitat VARCHAR (12) NOT NULL, puntuacio INTEGER NOT NULL);
INSERT INTO RegistreDragon (id, pseudonim, nivell, email, nacionalitat, puntuacio) VALUES (1, 'Jimmes', 3, 'jim34@gm.com', 'United State', 123);
INSERT INTO RegistreDragon (id, pseudonim, nivell, email, nacionalitat, puntuacio) VALUES (2, 'Jhonatan', 4, 'jhona@sd.com', 'Colombia', 156);
INSERT INTO RegistreDragon (id, pseudonim, nivell, email, nacionalitat, puntuacio) VALUES (3, 'Charls', 2, 'cha122@qw.com', 'England', 97);

-- View: ranking dels jugadors
DROP VIEW IF EXISTS "ranking dels jugadors";
CREATE VIEW "ranking dels jugadors" AS select pseudonim, nivell, nacionalitat, puntuacio
        from RegistreDragon ORDER BY puntuacio desc;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
