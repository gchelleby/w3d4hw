# Take the Shopping Cart application that you wrote for homework (or use the one I sent in slack)
# You can choose between the functional program or OOP version
# Write AT LEAST 3 different test cases that make sense for your cart.
# You may have to modify your code to make it work for tests.

# I thought I had turned this one in, it didn't show up on the missing page. 
# for some reason it's on the current assignments page and I just missed it I guess?

from shopping_cart import add, delete
import unittest

class CartTest(unittest.TestCase):
    def test_add(self):
        result_1: add('banana', 2, 3)
        self.assertDictEqual(result_1, {'banana': (2, 3)})
        result_2: add('orange', 5, 8)
        self.assertDictEqual(result_2, {'orange': (5, 8)})
        result_5: add('tomato', 1, 2)
        self.assertDictEqual(result_5, {'tomato': (1, 2)})
    
    def test_delete(self):
        result_3: delete('banana', 2, 3)
        self.assertDictEqual(result_3, {'banana': (2, 3)})
        result_4: delete('orange', 5, 8)
        self.assertDictEqual(result_4, {'orange': (5, 8)})
        # result_6: delete('tOmaTo', 2, 7)
        # self.assertDictEqual(result_6, {'tOmaTo': (2, 7)})
        # wanted to make a failed test to make sure all the others are passing correctly 
        # (if that makes sense)