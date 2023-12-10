-- Create the database
CREATE DATABASE language_game;

-- Select the database
USE language_game;

-- Create the glossary table
CREATE TABLE glossary (
    glossary_id INT PRIMARY KEY,
    term VARCHAR(50) NOT NULL,
    definition TEXT NOT NULL,
    INDEX (term)  -- Add this line to create an index on the 'term' column
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

-- Insert the eight parts of speech into the glossary table
INSERT INTO glossary (glossary_id, term, definition) VALUES
(1, 'Noun', 'A word that represents a person, place, thing, or idea.'),
(2, 'Pronoun', 'A word that takes the place of a noun.'),
(3, 'Verb', 'A word that expresses an action or state of being.'),
(4, 'Adjective', 'A word that describes or modifies a noun or pronoun.'),
(5, 'Adverb', 'A word that describes or modifies a verb, adjective, or other adverb.'),
(6, 'Preposition', 'A word that shows the relationship of a noun or pronoun to another word in the sentence.'),
(7, 'Conjunction', 'A word that connects words, phrases, or clauses.'),
(8, 'Interjection', 'A word or phrase used to express strong emotion or surprise.');
