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

    def test_piglatin_single_word_multi_consonant_translation2(self):
        #If the word starts with multiple consonants move ALL of them to the end of the word and append "ay"
        #add this functionality wihtout making changes to current if statements
        translator=PigLatin("kntwn")
        self.assertEqual("kntwnay", translator.translate())

    def test_piglatin_multi_word_translation(self):
        # if the phrase contains multiple words seperated by " " or "-" apply all of the translation rules to each word
        #If the phrase contains "-" keep it in between the translated words in the output
        translator = PigLatin("hello world")
        self.assertEqual("ellohay orldway", translator.translate())

    def test_piglatin_multi_word_translation2(self):
        # if the phrase contains multiple words seperated by " " or "-" apply all of the translation rules to each word
        #If the phrase contains "-" keep it in between the translated words in the output
        #create a seperate testcase fo words which have a "-" character and then split them to apply translations. then add the "-" in betwween the translated words and make them a single word again
        translator = PigLatin("well-being")
        self.assertEqual("ellway-eingbay", translator.translate())

    def test_piglatin_multi_word_punctuation_translation(self):
        #if the phrase contains any of the following punctuation marks ".,:;'?!()" keep them in the same place in the translated phrase
        translator = PigLatin("hello world!")
        self.assertEqual("ellohay orldway!", translator.translate())


