'''
A test suite for reversing words in phrases'''


import unittest

from production import reverse_word

class TestReverseWord(unittest.TestCase):
    '''Test class for the reverse word function'''

    def test_reverse_word(self):
        '''Test the reverse word function'''

        self.assertEqual(reverse_word("hello"), "olleh")
        self.assertEqual(reverse_word("world"), "dlrow")
        self.assertEqual(reverse_word("Python"), "nohtyP")
        self.assertEqual(reverse_word("TDD"), "DDT")
        self.assertEqual(reverse_word("test"), "tset")
