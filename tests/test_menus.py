"""
Noah Hefner
Test Classes for nhefner_pygame_menus
Last Edit: 19 August 2020
"""

# Imports
import unittest
from menus import *

# Initialize pygame
pygame.init()

class TestButtonPicture (unittest.TestCase):

    def setUp(self):

        button = ButtonPicture()

    def tearDown (self):

        pass

def suite():

    suite = unittest.TestSuite()
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(suite())
