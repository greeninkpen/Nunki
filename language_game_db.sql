-- Create the database
CREATE DATABASE language_game;

-- Select the database
USE language_game;

-- Create the glossary table

 CREATE TABLE glossary (
     glossary_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
     term VARCHAR(50) NOT NULL,
     definition TEXT NOT NULL,
     INDEX (term) -- added this index because I was getting error code 1822 trying to create word table for a missing index
 );



-- Create the word table
 CREATE TABLE word (
     word_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, # Changed all PKs to autoincrement to avoid errors retrieving data
     word_text VARCHAR(255) NOT NULL,
     part_of_speech VARCHAR(50) NOT NULL,
     CONSTRAINT fk_word_glossary
     FOREIGN KEY (part_of_speech)
     REFERENCES glossary (term)
 );


-- Create the sentence table
 CREATE TABLE sentence (
     sentence_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
     sentence_text VARCHAR(255) NOT NULL
 );

-- Create the sentence_word table

 CREATE TABLE sentence_word (
     sentence_id INT,
     word_id INT,
     PRIMARY KEY (sentence_id, word_id),
     CONSTRAINT fk_sentence_word_sentence
     FOREIGN KEY (sentence_id)
     REFERENCES sentence (sentence_id),
     CONSTRAINT fk_sentence_word_word
     FOREIGN KEY (word_id)
     REFERENCES word (word_id)
 );

-- Insert the eight parts of speech into the glossary table
INSERT INTO glossary (glossary_id, term, definition) VALUES
(1, 'noun', 'A word that represents a person, place, thing, or idea.'),
(2, 'pronoun', 'A word that takes the place of a noun.'),
(3, 'verb', 'A word that expresses an action or state of being.'),
(4, 'adjective', 'A word that describes or modifies a noun or pronoun.'),
(5, 'adverb', 'A word that describes or modifies a verb, adjective, or other adverb.'),
(6, 'preposition', 'A word that shows the relationship of a noun or pronoun to another word in the sentence.'),
(7, 'conjunction', 'A word that connects words, phrases, or clauses.'),
(8, 'interjection', 'A word or phrase used to express strong emotion or surprise.'),
(9, 'determiner', 'A modifying word, phrase of affix that appears together with a noun or noun phrase.'),
(10, 'article', 'A word that gives information about a noun');

