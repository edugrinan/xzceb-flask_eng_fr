import unittest
from translator import english_to_french, french_to_english
class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french(''), '')  # test when '' is given as input the output is ''.
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(french_to_english(''), '')  # test when '' is given as input the output is ''.