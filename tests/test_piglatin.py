import unittest
from piglatin import converter
from piglatin import app

class TestConvert(unittest.TestCase):

    def test_word_vowels(self):
        self.assertEqual(converter.convert_word("pig"),"igpay")
        self.assertEqual(converter.convert_word("banana"),"ananabay")
        self.assertEqual(converter.convert_word("trash"),"ashtray")
        self.assertEqual(converter.convert_word("happy"),"appyhay")
        self.assertEqual(converter.convert_word("duck"),"uckday")
        self.assertEqual(converter.convert_word("glove"),"oveglay")

    def test_word_consonants(self):
        self.assertEqual(converter.convert_word("eat"),"eatyay")
        self.assertEqual(converter.convert_word("omlet"),"omletyay")
        self.assertEqual(converter.convert_word("are"),"areyay")

    def test_word_spetical_chars(self):
        self.assertEqual(converter.convert_word("1234"),"1234")
        self.assertEqual(converter.convert_word("-"),"-")
        self.assertEqual(converter.convert_word("$40"),"$40")


    def test_word_capital(self):
        self.assertEqual(converter.convert_word("Python"),"Onpythay")
        self.assertEqual(converter.convert_word("Hello"),"Ellohay")
        self.assertEqual(converter.convert_word("Grammarly"),"Ammarlygray")
        #self.assertEqual(converter.convert_word("Yuliia's"),"Uliiayay'say") # ?
        self.assertEqual(converter.convert_word("USA"),"USAay")

    def test_text_spetial_words(self):
        self.assertEqual(converter.convert_text("behind-the-wheel"),"ehindbay-ethay-eelwhay")
        self.assertEqual(converter.convert_text("Anna's"),"Anna'say")
        self.assertEqual(converter.convert_text("M&M's"),"May&'sMay")
        self.assertEqual(converter.convert_text("one/two"),"oneyay/otway")

    def test_text_sentences(self):
        line ='The "Python library" contains several, different - kinds of (components). Right!?'
        right ='Ethay "Onpythay ibrarylay" ontainscay everalsay, ifferentday - indskay ofyay (omponentscay). Ightray!?'
        self.assertEqual(converter.convert_text(line), right)

if __name__ == '__main__':
    unittest.main()
