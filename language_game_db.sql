-- Create the database
CREATE DATABASE language_game;

-- Select the database
USE language_game;

-- Create the glossary table
CREATE TABLE glossary (
    glossary_id INT PRIMARY KEY,
    term VARCHAR(50) NOT NULL,
    definition TEXT NOT NULL
);

-- Create the word table
CREATE TABLE word (
    word_id INT PRIMARY KEY,
    word_text VARCHAR(255) NOT NULL,
    part_of_speech VARCHAR(50) NOT NULL,
    CONSTRAINT fk_word_glossary
    FOREIGN KEY (part_of_speech)
    REFERENCES glossary (term)
);

-- Create the sentence table
CREATE TABLE sentence (
    sentence_id INT PRIMARY KEY,
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
