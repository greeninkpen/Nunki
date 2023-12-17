import random
import requests
import json
from app import get_random_sentence, get_game_dictionary, app
from random import shuffle


def display_welcome():
    welcome_title = ''' 
    Welcome to the Language Learning Odyssey! 🌟\n
    '''
    welcome_nunki = '''
       /\   /\   
      //\\_//\\     ____
      \_     _/    /   /
       / * * \    /^^^]
       \_\O/_/    [   ]
        /   \_    [   /
        \     \_  /  /
         [ [ /  \/ _/
        _[ [ \  /_/
    '''

    welcome_message = ''' 
    +++ 🎮 GAME ON 🎮 +++
    \n\n
    What Awaits You:\n
        🌈 Dive into enchanting phrases and unveil the hidden parts of speech. Are you up for the challenge?\n
        🔍 Think you can unravel the mystery of distinguishing a 'noun' from an 'adjective'?\n
        🌟 Face captivating challenges to test your prowess with nouns, adjectives, and beyond!\n
        🧠 Experience interactive quizzes crafted for learners, teachers, and language aficionados!\n
    \n \n'''

    print(welcome_title)
    print(welcome_nunki)
    view_rules = input("Would you like to see the game rules? (yes/no): ")
    if view_rules.lower() == 'yes':
        game_rules = '''
        +++ 🚀 UNLEASH THE THRILLING RULES! 🚀 +++\n\n
        Ready to embark on a linguistic journey? The adventure begins now!\n\n
        🌟 Game Rules 🌟\n
            Encounter mind-bending phrases – your mission is to unveil the secret roles of words as nouns, adjectives, and more!\n
            Dare to explore the mesmerizing realm of English grammar with challenges that spark excitement!\n
            Lost between a noun and an article? Fear not! A whimsical glossary awaits below, ready to transform you into a language maestro.\n\n
        '''
        print(game_rules)

    view_glossary = input("Would you like to see the glossary? (yes/no): ")
    if view_glossary.lower() == 'yes':
        db_glossary = '''
         +++ 🌈 WHIMSICAL GLOSSARY 🌈 +++\n
        +------------------+---------------------------------------------------------------+
        | Part of Speech   | Definition                                                    |
        +------------------+---------------------------------------------------------------+
        | Noun             | A word that represents a person, place, thing, or idea.       |
        +------------------+---------------------------------------------------------------+
        | Pronoun          | A word that takes the place of a noun in a sentence.          |
        +------------------+---------------------------------------------------------------+
        | Verb             | A word that expresses an action, occurrence, or state of being.|
        +------------------+---------------------------------------------------------------+
        | Adjective        | A word that describes or modifies a noun or pronoun.          |
        +------------------+---------------------------------------------------------------+
        | Adverb           | A word that modifies a verb, adjective, or another adverb.    |
        +------------------+---------------------------------------------------------------+
        | Preposition      | A word that shows the relationship between a noun and another |
        |                  | element in the sentence.                                      |
        +------------------+---------------------------------------------------------------+
        | Conjunction      | A word that connects words, phrases, or clauses.              |
        +------------------+---------------------------------------------------------------+
        | Interjection     | A word or phrase that expresses strong emotion or surprise.   |
        +------------------+------------------------------------------------------------------------------------------------------+
        | Article          | A type of adjective that specifies whether a noun is definite or indefinite (e.g., "a," "an," "the").|
        +------------------+------------------------------------------------------------------------------------------------------+
        | Determiner       | A modifying word, phrase of affix that appears together with a noun or noun phrase.                  | 
        +------------------+------------------------------------------------------------------------------------------------------+
        \n
        '''
        print(db_glossary)

    print("Seize the chance to elevate your language skills in a unique way")
    print("🚀 Hit play now and set forth on your Language Learning Odyssey!")


display_welcome()


def add_sentence_and_words(full_sentence, words):
    sentence = {
        "sentence": full_sentence
    }
    sentence_request = requests.post("http:127.0.0.1:5000/save_phrase",
                                     headers={'content-type': 'application/json'},
                                     json=sentence
                                     )
    sentence_result = sentence_request.json()

    words = {
        "sentence_id": sentence_result["sentence_id"],
        "words": words
    }
    words_request = requests.post("http:127.0.0.1:5000/save_phrase",
                                  headers={'content-type': 'application/json'},
                                  json=words
                                  )
    words_result = words_request.json()


with app.app_context():
    game_phrase = get_random_sentence()
    game_phrase_dict = get_game_dictionary()


    class GameError(Exception):
        pass


    def language_game(game_phrase, game_phrase_dict):
        try:
            # test to make sure phrase is the same
            game_phrase_from_dict = ' '.join(d["word_text"] for d in game_phrase_dict)

            print("Here is your sentence: {}".format(game_phrase_from_dict))
            parts_of_speech = {d["part_of_speech"]: d["word_text"] for d in game_phrase_dict}

            keys = list(parts_of_speech.keys())
            random.shuffle(keys)

            for pos in keys:
                user_input = input("In the sentence, what word is the {}? ".format(pos))
                print(user_input.lower())

                if user_input.lower() == parts_of_speech[pos].lower():
                    print("Correct! {} is the {}! Great job!".format(parts_of_speech[pos], format(pos)))
                else:
                    print("You're not quite right! Check the glossary & try again!")
        except Exception:
            raise GameError("Uh-Oh! Something went wrong! Please restart the program to try again")
        finally:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == 'yes':
                language_game(game_phrase, game_phrase_dict)
            else:
                print("Thanks for playing!")

language_game(game_phrase, game_phrase_dict)
