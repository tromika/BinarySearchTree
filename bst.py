class Node:
	def __init__(self,key,value,left=None,right=None,parent=None):
		self.key = key
		self.value = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)



class BinarySearchTree:

	def __init__(self):
		self.root = None

	def put(self,key,val=None):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = Node(key,val)

	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				   self._put(key,val,currentNode.leftChild)
			else:
				   currentNode.leftChild = Node(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				   self._put(key,val,currentNode.rightChild)
			else:
				   currentNode.rightChild = Node(key,val,parent=currentNode)


	def get(self,key):
	   if self.root:
		   res = self._get(key,self.root)
		   if res:
				  return res.value
		   else:
				  return None
	   else:
		   return None

	def _get(self,key,currentNode):
	   if not currentNode:
		   return None
	   elif currentNode.key == key:
		   return currentNode
	   elif key < currentNode.key:
		   return self._get(key,currentNode.leftChild)
	   else:
		   return self._get(key,currentNode.rightChild)



	def Min(self):
	  current = self.root.leftChild
	  while current.hasLeftChild():
		  current = current.leftChild
	  return current.key

	def Max(self):
		current = self.root.rightChild
		while current.hasRightChild():
			current = current.rightChild
		return current.key
	


def main():
	bst = BinarySearchTree()  
	bst.put(3)
	bst.put(7)
	bst.put(6)
	bst.put(1)
	bst.put(2)

	print bst.Max()
	print bst.Min()

if __name__ == "__main__":
	main()




