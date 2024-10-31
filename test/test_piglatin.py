import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_piglatin_creation(self):
        translator = PigLatin("this is a test phrase")
        self.assertEqual("this is a test phrase", translator.get_phrase())
