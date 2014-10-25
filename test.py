import unittest
from bst import *

class TestBst(unittest.TestCase):
	def setUp(self):
		self.bst = BinarySearchTree()
		self.bst.put(5)
		self.bst.put(30)
		self.bst.put(2)
		self.bst.put(40)
		self.bst.put(25)
		self.bst.put(4)
	def test_max(self):
		self.assertEqual(self.bst.max(), 40)
	def test_min(self):
		self.assertEqual(self.bst.min(), 2)
	def test_count(self):
		self.assertEqual(self.bst.count(), 6)
	def test_depth(self):
		self.assertEqual(self.bst.depth(), 3)
	def test_store(self):
		self.assertEqual(self.bst.store(), '5 2 4 30 25 40 ')
def main():
    unittest.main()

if __name__ == '__main__':
    main()