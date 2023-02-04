import unittest

from final_project.machinetranslation.translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None).result['translations'][0]['translation'], 'Néant')
        self.assertEqual(english_to_french('Hello').result['translations'][0]['translation'], 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None).result['translations'][0]['translation'], 'None')
        self.assertEqual(french_to_english('Bonjour').result['translations'][0]['translation'], 'Hello')


unittest.main()
