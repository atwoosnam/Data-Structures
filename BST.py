# BST.py


# import numpy as np
# try:
# 	# for Python2
# 	from Tkinter import *

# except ImportError:	
# 	# for Python3
# 	from tkinter import *


class Node:
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None

	def __del__(self):
		print("__del__({0})".format(self.val))
		self.val = None
		self.parent = None
		self.left = None
		self.right = None

	def isEmpty(self):
		if (self.val == None):
			return True



class BST:
	def __init__(self):
		self.nodesArray = []
		self.root = None


	def search(self, val, start_node):

		if start_node.val == val:
			return start_node
		elif start_node.val > val and start_node.left != None:
			return self.search(val, start_node.left)
		elif start_node.val < val and start_node.right != None:
			return self.search(val, start_node.right)

		return None
		 

	def insert(self, val, start_node):
		n = Node(val=val)
		if self.root == None:
			self.root = n
			start_node = self.root

		elif start_node.val == val:
			raise ValueError("Not yet equipped to handle duplicate entries.")

		elif start_node.val > val:
			if start_node.left == None:
				start_node.left = n
				n.parent = start_node
			else:
				self.insert(val, start_node.left)

		elif start_node.val < val:
			if start_node.right == None:
				start_node.right = n
				n.parent = start_node
			else:
				self.insert(val, start_node.right)


	def findMax(self, start_node):
		if start_node.right == None or start_node.right.isEmpty():
			return start_node
		return findMax(start_node.right)


	def findMin(self, start_node):
		if start_node.left == None or start_node.left.isEmpty():
			return start_node
		return self.findMin(start_node.left)


	def delete(self, val):

		this_node = self.search(val, self.root)

		deletingRoot = False	

		if this_node == None or this_node.isEmpty():
			print ("No such node to delete: {0}".format(val))
			return None

		if this_node == self.root:
			print ("\nDeleting ROOT {0}".format(this_node.val))
			deletingRoot = True
		else:
			print ("\nDeleting {0}".format(this_node.val))


		if this_node.left == None or this_node.left.isEmpty():
			if this_node.right == None or this_node.right.isEmpty():
				# scenario = 0 	# no children --> delete node
				print("del'ing childless node")
				this_node.__del__()

			else:
				# scenario = 1 	# 1 (right) child --> splice this node out to join its parent and its child
				# give child new parent
				this_node.right.parent = this_node.parent

				if not deletingRoot:
					# give parent new child
					if this_node.parent.left == this_node:
						this_node.parent.left = this_node.right
					elif this_node.parent.right == this_node:
						this_node.parent.right = this_node.right
					else:
						raise Exception("Unexpected lineage: node to delete is not a child of its parent")
				else:
					self.root = this_node.right


				print("del'ing spliced-out node (r)")
				this_node.__del__()

		else:
			if this_node.right == None or this_node.right.isEmpty():
				# scenario = 2 	# 1 (left) child --> splice this node out to join its parent and its child
				# give child new parent
				this_node.left.parent = this_node.parent

				if not deletingRoot:
					# give parent new child
					if this_node.parent.left == this_node:
						this_node.parent.left = this_node.left
					elif this_node.parent.right == this_node:
						this_node.parent.right = this_node.left
					else:
						raise Exception("Unexpected lineage: node to delete is not a child of its parent")
				else:
					self.root = this_node.left

				print("del'ing spliced-out node (l)")
				this_node.__del__()

			else:
				# scenario = 3 	# two children
				print("del'ing 2-child node")
				# find max of left subtree
				replacement = self.findMax(this_node.left)

				if replacement == this_node:
					raise Exception("No left subtree")
					# use min of right subtree instead

				if replacement.right != None:
					raise Exception("Max of left subtree has a right child (it shouldn't)")

				if replacement.left == None:	# replacement has no children
					this_node.val = replacement.val
					replacement.__del__()

				else: 	# replacement has 1 child
					child = replacement.left
					replacement.parent.right = child
					replacement.__del__()



	def printout(self, root):
		v = root.val
		l = root.left.val if root.left != None else None
		r = root.right.val if root.right != None else None
		print("Node: {0}    L: {1}		R:{2}".format(v if v >=10 else ' ' + str(v), l, r))
		if root.left != None:
			self.printout(root.left)
		if root.right != None:
			self.printout(root.right)


	def populateArray(self):
		self.nodesArray = [self.root]
		i = 0
		while (i < len(self.nodesArray)):
			current = self.nodesArray[i]
			if current != None and current.val != None:
				self.nodesArray.append(current.left)
				self.nodesArray.append(current.right)
			i += 1

		for i in range(len(self.nodesArray)):
			node = self.nodesArray[i]
			self.nodesArray[i] = node.val if node != None else None

		return self.nodesArray


	def graph(self):
		new_window = Tk()
		new_window.geometry("1200x800")
		new_window.mainloop()



class unitTester():
	def __init__(self):
		self.tree = BST()

	def testInsert(self):
		self.tree.insert(15, self.tree.root)
		self.tree.insert(20, self.tree.root)
		self.tree.insert(27, self.tree.root)
		self.tree.insert(3, self.tree.root)
		self.tree.insert(18, self.tree.root)
		self.tree.insert(13, self.tree.root)
		self.tree.insert(8, self.tree.root)
		self.tree.insert(5, self.tree.root)
		self.tree.insert(17, self.tree.root)
		self.tree.insert(29, self.tree.root)
		self.tree.insert(26, self.tree.root)
		self.tree.insert(4, self.tree.root)
		self.tree.insert(14, self.tree.root)
		self.tree.insert(16, self.tree.root)
		self.tree.insert(1, self.tree.root)
		self.tree.printout(self.tree.root)

		test_results = self.tree.populateArray()
		expected_results = [15,3,20,1,13,18,27,None,None,8,14,17,None,26,29,5,None,None,None,16,None,None,None,None,None,4,None,None,None,None,None]
		assert (test_results == expected_results), "TEST CASE FAILURE: BST.insert()\nResult  :\t {0}\nExpected:\t {1}".format(test_results, expected_results)



if __name__ == '__main__':
	tester = unitTester()
	tester.testInsert()

	







