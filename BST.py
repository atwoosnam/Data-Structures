# BST.py

import numpy as np
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
		self.nodesArray = []


class BST:
	def __init__(self):
		# self.nodes = []
		self.root = None


	def search(self, val, start_node):
		if start_node.val == val:
			return start_node
		elif start_node.val > val:
			return self.search(val, start_node.left)
		elif start_node.val < val:
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

	def printout(self, root):
		v = root.val
		l = root.left.val if root.left != None else None
		r = root.right.val if root.right != None else None
		print("Node: {0}	L: {1}	R:{2}".format(v, l, r))
		if root.left != None:
			self.printout(root.left)
		if root.right != None:
			self.printout(root.right)

	# def graph(self):

	def populateArray(self, node):
		if node == self.root:
			self.nodesArray = []
			self.nodesArray.append(node.val)

		if node.left == None:
			self.nodesArray.append(None)
		else:
			self.nodesArray.append(node.left.val)

		if node.right == None:
			self.nodesArray.append(None)
		else:
			self.nodesArray.append(node.right.val)

		''' This level done, proceed to next level '''
		if node.left != None:
			self.populateArray(node.left)
		if node.right != None:
			self.populateArray(node.right)

		return self.nodesArray



if __name__ == '__main__':
	tree = BST()
	tree.insert(14, tree.root)
	tree.insert(16, tree.root)
	tree.insert(18, tree.root)
	tree.insert(13, tree.root)
	tree.insert(15, tree.root)
	tree.insert(20, tree.root)

	tree.printout(tree.root)
	print("\n" + str(tree.populateArray(tree.root)))







