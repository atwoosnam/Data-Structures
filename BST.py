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
		if start_node.right == None or start_node.right.val == None:
			return start_node
		return findMax(start_node.right)


	def findMin(self, start_node):
		if start_node.left == None or start_node.left.val == None:
			return start_node
		return self.findMin(start_node.left)


	def delete(self, val):

		this_node = self.search(val, self.root)

		if this_node == None:
			print ("No such node to delete: {0}".format(val))
			return None

		print ("\nDeleting {0}".format(this_node.val))

		if this_node == self.root:
			# print("DELETING ROOT")
			replacement = self.findMax(this_node.left)

			if replacement.val == None:
				replacement = self.findMin(this_node.right)

			elif replacement == this_node:
				raise Exception("No viable replacement")

			this_node.val = replacement.val
			print("del'ing replacement")
			replacement.__del__()

		# no children: Delete this node
		elif this_node.left == None and this_node.right == None:
			print("del'ing childless node")
			this_node.__del__()

		# one child? splice this node out to join its parent and its child
		elif this_node.left != None and this_node.right == None:
			# give child new parent
			this_node.left.parent = this_node.parent
			# give parent new child
			if this_node.parent.left == this_node:
				this_node.parent.left = this_node.left
			elif this_node.parent.right == this_node:
				this_node.parent.right = this_node.left
			else:
				raise Exception("Unexpected lineage: node to delete is not a child of its parent")

			print("del'ing spliced-out node (l)")
			this_node.__del__()

		elif this_node.left == None and this_node.right != None:
			# give child new parent
			this_node.right.parent = this_node.parent
			# give parent new child
			if this_node.parent.left == this_node:
				this_node.parent.left = this_node.right
			elif this_node.parent.right == this_node:
				this_node.parent.right = this_node.right
			else:
				raise Exception("Unexpected lineage: node to delete is not a child of its parent")

			print("del'ing spliced-out node (r)")
			this_node.__del__()

		# two children
		elif this_node.left != None and this_node.right != None:
			# find largest leaf in left subtree, swap values & delete that leaf
			maxLeaf = self.findMax(this_node.left)
			if maxLeaf == this_node:
				raise Exception("Maximum Node Error: node to delete is greater than its right child")

			this_node.val = maxLeaf.val

			print("del'ing swapped max leaf")
			maxLeaf.__del__()


	def printout(self, root):
		v = root.val
		l = root.left.val if root.left != None else None
		r = root.right.val if root.right != None else None
		print("Node: {0}    L: {1}		R:{2}".format(v if v >=10 else ' ' + str(v), l, r))
		if root.left != None:
			self.printout(root.left)
		if root.right != None:
			self.printout(root.right)


	def populateArray(self, node):
		if node == self.root:
			self.nodesArray = []
			self.nodesArray.append(node.val)

		l = None if node.left == None else node.left.val
		self.nodesArray.append(l)

		r = None if node.right == None else node.right.val
		self.nodesArray.append(r)


		''' This level done, proceed to next level '''
		if node.left != None:
			if node.left.val != None:
				self.populateArray(node.left)
		if node.right != None:
			if node.right.val != None:
				self.populateArray(node.right)

		return self.nodesArray


	def graph(self):
		new_window = Tk()
		new_window.geometry("1200x800")
		new_window.mainloop()


if __name__ == '__main__':
	tree = BST()

	tree.insert(14, tree.root)
	tree.insert(16, tree.root)
	tree.insert(1, tree.root)
	tree.insert(18, tree.root)
	tree.insert(13, tree.root)
	tree.insert(8, tree.root)
	tree.insert(15, tree.root)
	tree.insert(20, tree.root)
	tree.insert(5, tree.root)
	tree.insert(27, tree.root)
	tree.insert(3, tree.root)
	tree.insert(17, tree.root)
	tree.insert(29, tree.root)
	tree.insert(26, tree.root)
	tree.insert(4, tree.root)


	tree.printout(tree.root)
	print("\n")

	print(str(tree.populateArray(tree.root)) + " : " + str(len(tree.nodesArray)))

	# print(tree.search(20, tree.root))

	# tree.delete(20)
	# print(str(tree.populateArray(tree.root)) + " : " + str(len(tree.nodesArray)))

	# tree.delete(18)
	# print(str(tree.populateArray(tree.root)) + " : " + str(len(tree.nodesArray)))

	for i in range(1,30):
		if tree.search(i, tree.root) != None:
			tree.delete(i)
			print(str(tree.populateArray(tree.root)) + " : " + str(len(tree.nodesArray)))



	# tree.graph()







