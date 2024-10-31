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
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_piglatin_single_word_vowel_translation3(self):
        #only translate if the input phrase is one word and starts with a vowel
        #if the word ends with a consonant append "ay"
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_piglatin_single_word_consonant_translation(self):
        #only translate if the input phrase is one word and starts with a single consonant
        #if this is the case remove the single consonant in the beginning append it ot the end and append "ay" after it
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_piglatin_single_word_multi_consonant_translation(self):
        #If the word starts with multiple consonants move ALL of them to the end of the word and append "ay"
        #add this functionality wihtout making changes to current if statements
        translator=PigLatin("known")
        self.assertEqual("ownknay", translator.translate())