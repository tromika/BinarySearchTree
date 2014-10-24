import unittest
from bst import *

class TestBst(unittest.TestCase):
	def setUp(self):
		self.bst = BinarySearchTree()
		self.bst.put(3)
		self.bst.put(7)
		self.bst.put(6)
		self.bst.put(1)
		self.bst.put(2)
	def test_max(self):
		self.assertEqual(self.bst.Max(), 7)
	def test_min(self):
		self.assertEqual(self.bst.Min(), 1)
def main():
    unittest.main()

if __name__ == '__main__':
    main()