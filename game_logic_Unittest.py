import unittest
from unittest.mock import patch
from io import StringIO
#from app import LanguageGame, GameError


'''The testing for this function had to be hard-coded to ensure that the expected response was issued by the program
If we had not, we would not have had control of the input, having very little control over what the API chat generation AI 
returns. This would need to be something that is taken into consideration for future implementation '''
class TestLanguageGame(unittest.TestCase):

    def setUp(self):
        self.game_instance = LanguageGame()

    def test_language_game_correct_input(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        input_values = ['The', 'cat', 'is', 'sleeping', 'no']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game_instance.language_game(game_phrase, game_phrase_dict)

        expected_output = (
            "Here is your sentence: The cat is sleeping\n"
            "In the sentence, what word is the article? Correct! The is the article! Great job!\n"
            "In the sentence, what word is the noun? Correct! cat is the noun! Great job!\n"
            "In the sentence, what word is the verb? Correct! is is the verb! Great job!\n"
            "In the sentence, what word is the adjective? Correct! sleeping is the adjective! Great job!\n"
            "Do you want to play again? (yes/no): Thanks for playing!\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_language_game_incorrect_input(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        input_values = ['A', 'dog', 'are', 'awake', 'no']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game_instance.language_game(game_phrase, game_phrase_dict)

        expected_output = (
            "Here is your sentence: The cat is sleeping\n"
            "In the sentence, what word is the article? You're not quite right! Check the glossary & try again!\n"
            "In the sentence, what word is the noun? You're not quite right! Check the glossary & try again!\n"
            "In the sentence, what word is the verb? You're not quite right! Check the glossary & try again!\n"
            "In the sentence, what word is the adjective? You're not quite right! Check the glossary & try again!\n"
            "Do you want to play again? (yes/no): Thanks for playing!\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_language_game_exception_handling(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        with patch('builtins.input', side_effect=['The', 'cat', 'is', 'sleeping', 'yes']):
            with patch('sys.stdout', new_callable=StringIO):
                with self.assertRaises(GameError):
                    self.game_instance.language_game(game_phrase, game_phrase_dict)

    def test_language_game_uppercase_input(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        input_values = ['THE', 'CAT', 'IS', 'SLEEPING', 'no']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game_instance.language_game(game_phrase, game_phrase_dict)

        expected_output = (
            "Here is your sentence: The cat is sleeping\n"
            "In the sentence, what word is the article? Correct! The is the article! Great job!\n"
            "In the sentence, what word is the noun? Correct! cat is the noun! Great job!\n"
            "In the sentence, what word is the verb? Correct! is is the verb! Great job!\n"
            "In the sentence, what word is the adjective? Correct! sleeping is the adjective! Great job!\n"
            "Do you want to play again? (yes/no): Thanks for playing!\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_language_game_wrong_data_type_input(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        input_values = [123, 456, True, 'sleeping', 'no']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game_instance.language_game(game_phrase, game_phrase_dict)

        expected_output = (
            "Here is your sentence: The cat is sleeping\n"
            "Uh-Oh! Something went wrong! Please restart the program to try again\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_language_game_special_characters_input(self):
        game_phrase = "The cat is sleeping"
        game_phrase_dict = {
            'article': 'The',
            'noun': 'cat',
            'verb': 'is',
            'adjective': 'sleeping'
        }

        input_values = ['?', '!', '"', '£', 'no']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game_instance.language_game(game_phrase, game_phrase_dict)

        expected_output = (
            "Here is your sentence: The cat is sleeping\n"
            "You're not quite right! Check the glossary & try again!\n"
            "You're not quite right! Check the glossary & try again!\n"
            "You're not quite right! Check the glossary & try again!\n"
            "You're not quite right! Check the glossary & try again!\n"
            "Do you want to play again? (yes/no): Thanks for playing!\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
