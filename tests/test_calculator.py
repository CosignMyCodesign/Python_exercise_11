import unittest
import sys
sys.path.append('../')
from calculator import Calculator

# Do your setUpModule(), tearDownModule(), setUpClass(), tearDownClass() like this everytime you do a test file
def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests
    cls.calc = Calculator()

  @classmethod
  def tearDownClass(cls):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)
        # or
    # result = self.calc.add(2, 7)
    # expected = 9
    # self.assertEqual(result, expected)

  # Write test methods for subtract, multiply, and divide
  def test_subtract(self):
    self.assertEqual(self.calc.subtract(10, 5), 5)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(4, 4), 16)  

  def test_divide(self):
      self.assertEqual(self.calc.divide(20, 5), 4)  
  

if __name__ == '__main__':
    unittest.main()