CREATE DATABASE language_game;
--  Language Learning Game Database

USE language_game;

--  create blank tables to store AI generated learning phrases
CREATE TABLE beginner_level(
  phrase_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  generated_phrase VARCHAR(255)
);
CREATE TABLE elementary_level(
  phrase_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  generated_phrase VARCHAR(355)
);
CREATE TABLE intermediate_level(
  phrase_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  generated_phrase VARCHAR(600)
);

 --  adding foreign keys to link learner phrases(user progression in skill) to one another
ALTER TABLE elementary_level
ADD CONSTRAINT fk_phrase_ID
FOREIGN KEY (phrase_ID)
REFERENCES beginner_level(phrase_ID);

ALTER TABLE intermediate_level
ADD CONSTRAINT fk_phrase_ID
FOREIGN KEY (phrase_ID)
REFERENCES beginner_level(phrase_ID);
