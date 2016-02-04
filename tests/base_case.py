from unittest import TestCase
from jarvis import JARVIS
import os


class JARVISTestCase(TestCase):

    def setUp(self):
        self.jarvis = JARVIS()

    def random_string(self, start=0, end=9000):
        """
        Generate a string based on a random number.
        """
        from random import randint
        return str(randint(start, end))
