class Node:
	def __init__(self,key,value,left=None,right=None,parent=None):
		self.key = key
		self.value = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	#Helpers
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
	#Insert node to the tree	
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

	#Get node's value		   
	def get(self,key):
	   if self.root:
		   result = self._get(key,self.root)
		   if result:
				  return result.value
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


	#Get the minimum value of the tree
	def Min(self):
	  current = self.root.leftChild
	  while current.hasLeftChild():
		  current = current.leftChild
	  return current.key
	#Get the maxium value of the tree
	def Max(self):
		current = self.root.rightChild
		while current.hasRightChild():
			current = current.rightChild
		return current.key
	
	def depth(self):
		if self.root.isLeaf():
			return 1
		else: 
			return self._depth(self.root)
	def _depth(self,currentNode):
		maxDepth = 0
		if currentNode.hasLeftChild():
			maxDepth = max(maxDepth,self._depth(currentNode.leftChild))
		if currentNode.hasRightChild():
			maxDepth = max(maxDepth,self._depth(currentNode.rightChild))
		return maxDepth + 1
	def store(self):
		return self._store(self.root,"")
	def _store(self,currentNode,st):
		if currentNode:
			st+=str(currentNode.key)+" "
			if currentNode.hasLeftChild():  st=str(self._store(currentNode.leftChild,st))
			if currentNode.hasRightChild(): st=str(self._store(currentNode.rightChild,st))
			return st
	def count(self):
		return self._count(self.root)
	def _count(self,currentNode):
		if currentNode is None:
			return 0
		else:
			return self._count(currentNode.leftChild) + self._count(currentNode.rightChild) + 1
			

def main():
	bst = BinarySearchTree()  
	bst.put(5)
	bst.put(30)
	bst.put(2)
	bst.put(40)
	bst.put(25)
	bst.put(4)

	print bst.Max()
	print bst.Min()
	print bst.count()
	print bst.depth()
	print bst.store()

if __name__ == "__main__":
	main()




