import unittest
from app.models import Quotes
from app import db


class QuotesTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Quote class
  '''
  def setUp(self):
    '''
    Set up method that will run before every Test.
    '''
    self.new_quote = Quotes("David", "Let it all work out..")

  def test_instance(self):
    '''
    Uses 'isinstance()' function to check if the object 'self.new_quote' is an instance of the 'Quote class'.
    '''
    self.assertTrue(isinstance(self.new_quote,Quotes))


if __name__ == '__main__':
    unittest.main()

