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
