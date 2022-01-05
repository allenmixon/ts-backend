--CREATE DATABASE treedb;

--Run in already created treedb

CREATE EXTENSION pgcrypto;

CREATE SCHEMA IF NOT EXISTS users;

CREATE TABLE users.credentials (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);

--INSERT INTO users.credentials (username, password) VALUES ('johndoe', crypt('buckslayer', gen_salt('bf')));

/*
   SELECT id 
     FROM users.crendentials
    WHERE username = 'johndoe' 
      AND password = crypt('buckslayer', password);

    id
   ----
     1
   (1 row)


   SELECT id 
     FROM users
    WHERE email = 'johndoe' 
      AND password = crypt('buckslayer', password);

    id
   ----
   (0 rows)
*/

CREATE SCHEMA IF NOT EXISTS inventory;

CREATE TABLE inventory.callready(
   CALL_ID SERIAL PRIMARY KEY NOT NULL,
   CUSTOMER_NAME VARCHAR(255) NOT NULL,
   SHIPPING_ADDRESS VARCHAR(255),
   PHONE VARCHAR(255),
   EMAIL VARCHAR(255),
   CUSTOMER_REP VARCHAR(255),
   CUSTOMER_PO VARCHAR(255),
   GLC_BOL VARCHAR(255),
   GLC_BOL2 VARCHAR(255),
   CREATION_TIMESTAMP timestamp WITH TIME ZONE
    DEFAULT current_timestamp
);

--INSERT INTO inventory.callready (CUSTOMER_NAME, SHIPPING_ADDRESS) VALUES ('Troy Homes', 'Lol Main 47');
--INSERT INTO inventory.callready (CUSTOMER_NAME, SHIPPING_ADDRESS) VALUES ('Berkshire Hathaway', '888 Buttguard Ln');

CREATE TABLE inventory.pieces(
   NUMID SERIAL PRIMARY KEY NOT NULL,
   ROW INT NOT NULL,
   CALL_ID INT NOT NULL,
   THICKNESS NUMERIC(8,2),
   WIDTH NUMERIC(8,2),
   LENGTH NUMERIC(8,2),
   CONSTRAINT fk_call_id
      FOREIGN KEY(CALL_ID) 
         REFERENCES inventory.callready(CALL_ID)
);

--INSERT INTO inventory.pieces (ROW, CALL_ID, THICKNESS, WIDTH, LENGTH) VALUES (1, 1, 2.2, 3.3, 4.4);
--INSERT INTO inventory.pieces (ROW, CALL_ID, THICKNESS, WIDTH, LENGTH) VALUES (2, 1, 6.2, 6.3, 6.4);
--INSERT INTO inventory.pieces (ROW, CALL_ID, THICKNESS, WIDTH, LENGTH) VALUES (1, 2, 2.2, 3.3, 4.4);