import unittest
from Homework1 import Classify_triangle

class TestApp(unittest.TestCase):
    """check the test cases"""
    def test_Classify_triangle(self):
        self.assertEqual(Classify_triangle(3,3,3),"Equilateral triangle")
        self.assertEqual(Classify_triangle(3,3,4),"Isoscale triangle")
        self.assertEqual(Classify_triangle(3,4,5),"right triangle")
        self.assertEqual(Classify_triangle(3,4,6),"scalene triangle")
        self.assertNotEqual(Classify_triangle(3,3,6),"scalene triangle")
        self.assertEqual(Classify_triangle(3,0,6),"can't form triangle")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
        
        
        
