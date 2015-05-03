CREATE USER 'domuspi'@'localhost' IDENTIFIED BY 'domuspi';
GRANT ALL PRIVILEGES ON *.* TO 'domuspi'@'localhost' WITH GRANT OPTION;
CREATE DATABASE domuspi;
USE domuspi;

CREATE TABLE users(
  id INTEGER AUTO_INCREMENT NOT NULL,
  name VARCHAR(255) NOT NULL,
  login VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE log(
  id INTEGER AUTO_INCREMENT NOT NULL,
  user_id INTEGER NOT NULL REFERENCES users(id),
  action TEXT NOT NULL,
  date_time TIMESTAMP NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE switchs(
  id INTEGER AUTO_INCREMENT NOT NULL,
  label VARCHAR(255),
  code INTEGER,
  state INTEGER,
  PRIMARY KEY(id)
);


-- SEED
INSERT INTO users(name,login,password) VALUES('ADMIN','domuspi','domuspi');


INSERT INTO switchs (label,state,code) VALUES ('Quarto', 0, 0);
INSERT INTO switchs (label,state,code) VALUES ('Rele 2', 0, 1);
INSERT INTO switchs (label,state,code) VALUES ('Rele 3', 0, 2);
INSERT INTO switchs (label,state,code) VALUES ('Rele 4', 0, 3);
INSERT INTO switchs (label,state,code) VALUES ('Rele 5', 0, 4);
INSERT INTO switchs (label,state,code) VALUES ('Rele 6', 0, 5);
INSERT INTO switchs (label,state,code) VALUES ('Rele 7', 0, 6);
INSERT INTO switchs (label,state,code) VALUES ('Rele 8', 0, 7);
INSERT INTO switchs (label,state,code) VALUES ('Rele 9', 0, 8);
INSERT INTO switchs (label,state,code) VALUES ('Rele 10', 0, 9);
INSERT INTO switchs (label,state,code) VALUES ('12 Volts - GPB2', 0, 10);
INSERT INTO switchs (label,state,code) VALUES ('12 Volts - GPB3', 0, 11);
INSERT INTO switchs (label,state,code) VALUES ('12 Volts - GPB4', 0, 12);

