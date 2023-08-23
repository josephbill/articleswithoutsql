import sys
import os

# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from articlesapp.author import Author


class TestAuthor(unittest.TestCase):
    # what needs to happen before a unit test is ran on a logic
    # create an object of the class 
    def setUp(self):
        self.author = Author("Joseph")

    # testing out outputs we use two key methods 
    # assertEqual : used for strings, integers and booleans 
    # assertIn : used to check for collections/sequences




if __name__ == '__main__':
    unittest.main()