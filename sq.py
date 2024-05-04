import unittest

from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area(10)
        self.asserteEqual(area,100)
        
    def test_length_with_wrong_type(self):
        