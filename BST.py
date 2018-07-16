# BST.py

import numpy as np 

class Node:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class BST:
	def __init__(self):
		# self.nodes = []
		self.root = None


	def search(val, start_node=self.root):
		if start_node.val == val:
			return start_node
		elif start_node.val > val:
			return search(val, start_node.left)
		elif start_node.val < val:
			return search(val, start_node.right)
		 

	def insert(val):
		n = Node(val=val)
		if self.root == None:
			self.root = n
		elif 

