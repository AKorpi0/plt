import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_piglatin_creation(self):
        translator = PigLatin("this is a test phrase")
        self.assertEqual("this is a test phrase", translator.get_phrase())

    def test_piglatin_empty_translate(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_piglatin_single_word_vowel_translation(self):
        #only translate if the input phrase is one word and starts with a vowel
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_piglatin_single_word_vowel_translation2(self):
        #only translate if the input phrase is one word and starts with a vowel
        #if the word ends with a vowel that is not "y" append yay
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())