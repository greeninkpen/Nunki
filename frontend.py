
import requests
import json

def display_welcome():
    welcome_nunki = '''
     Welcome to Nunki: A Language Learning Odyssey!🌟
    
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
    Embark on an exhilarating quest to conquer English grammar in our Language Learning Game!\n\n
    +++ 🎮 GAME ON 🎮 +++
    \n
    What Awaits You:\n
        🌈 Dive into enchanting phrases and unveil the hidden parts of speech. Are you up for the challenge?\n
        🔍 Think you can unravel the mystery of distinguishing a 'noun' from an 'adjective'?\n
        🌟 Face captivating challenges to test your prowess with nouns, adjectives, and beyond!\n
        🧠 Experience interactive quizzes crafted for learners, teachers, and language aficionados!\n
    \n \n'''

    print(welcome_nunki)
    print(welcome_message)


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
        +------------------+---------------------------------------------------------------+
        \n
        '''
        print(db_glossary)


print(welcome_fox)
print(welcome_message)
print(game_rules)
print(glossary_message)
#print(db-glossary)


def add_sentence(full_sentence):
    sentence = {
        "sentence": full_sentence
    }
    request = requests.post("http:127.0.0.1:5000/sentence",
                            headers={'content-type': 'application/json'},
                            json=sentence
                            )
    result = request.json()


def add_words(sentence_id, words):
    data = {
        "sentence_id": sentence_id,
        "words": words
    }
    request = requests.post("http:127.0.0.1:5000/words",
                            headers={'content-type': 'application/json'},
                            json=data
                            )
    result = request.json()


def run():
    # add new sentence/ sentence words + part of speech
    add_sentence()


if __name__ == '__main__':
    run()

    print("Seize the chance to elevate your language skills in a unique way")
    print("🚀 Hit play now and set forth on your Language Learning Odyssey!")

display_welcome()

