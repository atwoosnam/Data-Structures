# BST.py


# import numpy as np
import math
try:
	# for Python2
	from Tkinter import *

except ImportError:	
	# for Python3
	from tkinter import *


class Node:
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None
		self.grid_col = None
		self.grid_row = None

	def __del__(self):
		# print("__del__({0})".format(self.val))
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
		if val == None:
			raise Exception("Can't insert a null value")

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
		print("Node: {0}    L: {1}		R:{2}, 		Parent:{3}".format(v if v >=10 else ' ' + str(v), l, r, root.parent.val if root.parent != None else None))
		if root.left != None:
			self.printout(root.left)
		if root.right != None:
			self.printout(root.right)


	def getNodesArray(self):
		self.nodesArray = [self.root]
		i = 0
		while (i < len(self.nodesArray)):
			current = self.nodesArray[i]
			if current != None and current.val != None:
				self.nodesArray.append(current.left)
				self.nodesArray.append(current.right)
			i += 1

		return self.nodesArray


	def graph(self):
		new_window = Tk()
		new_window.geometry("1280x800")
		arr = self.getNodesArray()

		depth = self.calculateDepth()
		w = Plot(new_window, arr, depth)
		new_window.mainloop()


	def calculateDepth(self):
		# self.printout(self.root)
		arr = self.getNodesArray()
		start_node = arr[0]

		# find last node in nodesArray (aka "deepest" node)
		for node in arr: 	# this would be quicker starting at the end of the array
			if node != None:
				end_node = node

		depth = self.DFS(start_node, end_node) + 1
		print("deepest node: {0}, depth: {1}".format(end_node.val, depth))
		return depth


	def DFS(self, start_node, end_node):
		''' Find distance from start_node to end_node '''
		if start_node == None: return None

		if start_node.left == end_node or start_node.right == end_node:
			return 1
		elif start_node.left == None and start_node.right == None:
			return None
		
		else:
			l = self.DFS(start_node.left,end_node)
			if l == None:
				r = self.DFS(start_node.right, end_node) 
				if r == None:
					raise Exception("end_node is unreachable by DFS")
				else: return 1 + r
			else: return 1 + l



class Plot(Frame):

	# Define settings upon initialization. Here you can specify
	def __init__(self, master, arr, depth):
		
		# parameters that you want to send through the Frame class. 
		Frame.__init__(self, master)   

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)
              
		self.master = master
		self.master.title("BST")
		self.canvas = Canvas(self, width=1270, height=800)



		# root = arr[0]
		# numLeft = 0
		# numRight = 0
		# numLeaves = 0
		# numRows = 0
		# for i in range(len(arr)):		# efficiency can be improved from O(n) here
		# 	if arr[i] != None:
		# 		if arr[i].val < root.val:
		# 			numLeft += 1
		# 		else:
		# 			numRight += 1
		# 	else:
		# 		numLeaves += 1


		# print("numLeft: {0}, numRight: {1}".format(numLeft, numRight))

		# maxrows = max(numLeft, numRight)
		# columns = int(2**math.ceil(math.log(numLeaves,2)))*2
		# columns = int(2**math.ceil(math.log(numLeaves,2))) # round to next highest power of 2
		# columns = numLeaves*2


		# print("len(arr) = {0}".format(len(arr)))
		# maxcols = len(arr)
		# columns = maxcols
		# maxrows = maxcols/2
		# mid = columns/2



		


		# print("maxrows: {0}, cols: {1}, numLeaves: {2}, mid: {3}".format(maxrows, columns, numLeaves, mid))
		# n = 0
		# for row in range(10):
		# 	for col in range(10):
		# 		x =Label(self.canvas, text=" ")
		# 		x.grid(row=row, column=col, ipadx=1, pady=10)
		# 		x.config(font=('times',6,'bold'))
		# 		n += 1

		# self.placeOnGrid(node=arr[0], row=1, leftmost_col=0, rightmost_col=num_columns, depth)
		# self.placeOnGrid(arr[0], 0, 8, 2)

		num_columns = 2**depth + 1
		print("columns: {0}".format(num_columns))

		''' Calculate grid coordinates for all nodes '''
		for i in range(len(arr)):
			node = arr[i]
			if node != None:

				if i == 0:
					''' root '''
					node.grid_row = 0
					node.grid_col = num_columns/2
					n = Label(self.canvas, text=node.val)
					n.grid(row=node.grid_row, column=node.grid_col, columnspan=1) 

				else:

					parent = node.parent
					grandparent = parent.parent

					if grandparent == None:
						''' 1st row '''
						if parent != arr[0]: raise Exception("Missing grandparent of non-root child: {0}".format(node.val))

						elif node.val < parent.val:
							leftmost_col = 0
							rightmost_col = parent.grid_col
						elif node.val > parent.val:
							leftmost_col = parent.grid_col
							rightmost_col = num_columns
						else: raise Exception("Unexpected duplicate value: {0}".format(node.val))

					elif node.val < parent.val:
						# print("node val: {0}, parent val: {1}".format(node.val, parent.val))
						# node.grid_col = parent.grid_col/2
						rightmost_col = parent.grid_col

						if parent.val < grandparent.val:
							leftmost_col = 0

						elif parent.val > grandparent.val:
							leftmost_col = grandparent.grid_col

						else: raise Exception("Unexpected duplicate value: {0}".format(parent.val))


					elif node.val > parent.val:
						# print("node val: {0}, parent val: {1}".format(node.val, parent.val))
						# node.grid_col = (parent.grid_col*3)/2
						leftmost_col = parent.grid_col

						if parent.val < grandparent.val:
							rightmost_col = grandparent.grid_col

						elif parent.val > grandparent.val:
							rightmost_col = num_columns

						else: raise Exception("Unexpected duplicate value: {0}".format(parent.val))
						
					else: raise Exception("Unexpected duplicate value: {0}".format(node.val))

					node.grid_row = parent.grid_row + 1
					node.grid_col = (leftmost_col+rightmost_col)/2

					n = Label(self.canvas, text=node.val)
					n.grid(row=node.grid_row, column=node.grid_col, columnspan=1) 

				print("Val: {0}, Row: {1}, Col: {2}".format(node.val,node.grid_row, node.grid_col))



		self.canvas.pack(fill=Y, expand=True)

	
	# def placeOnGrid(self, node, row, leftmost_col, rightmost_col, depth):
	# 	labelfont = ('times', 10, 'bold')
	# 	print("placing {0} at ({1},{2})".format(node.val, row, col))

	# 	if node != None:

	# 		# grid self
	# 		n = Label(self.canvas, text=node.val)
	# 		n.grid(row=node.grid_row, column=node.grid_col, columnspan=1) 
	# 		n.config(font=labelfont)

	# 		# shift_amt = 2**(depth-row) 
	# 		# if shift_amt < 1:
	# 		# 	raise Exception("Shift Amount Too Small")
	# 		# print("shift_amt = 2^({0}-{1}) = 2^{2} = {3}".format(depth, row, depth-row,shift_amt))

	# 		# grid children
	# 		new_row = row + 1
	# 		if node.left != None:
	# 			new_col = col-shift_amt
	# 			if new_col < 0: raise Exception("Incorrect column placement")
	# 			self.placeOnGrid(node.left, row, new_col, depth)
	# 		if node.right != None:
	# 			new_col = col+shift_amt
	# 			# if new_col > : raise Exception("Incorrect column placement")
	# 			self.placeOnGrid(node.right, row, new_col, depth)


	def client_exit(self):
		exit()

	def warn(self,msg):
		messagebox.showerror("Error", msg)

	def quit(self):
		self.master.destroy()



class unitTester():
	def __init__(self):
		self.tree = BST()

	def runTests(self):
		self.tree.insert(15, self.tree.root)
		self.tree.insert(20, self.tree.root)
		self.tree.insert(27, self.tree.root)
		self.tree.insert(3, self.tree.root)
		self.tree.insert(18, self.tree.root)
		self.tree.insert(13, self.tree.root)
		self.tree.insert(8, self.tree.root)
		# self.tree.insert(5, self.tree.root)
		# self.tree.insert(17, self.tree.root)
		# self.tree.insert(29, self.tree.root)
		# self.tree.insert(26, self.tree.root)
		# self.tree.insert(4, self.tree.root)
		# self.tree.insert(14, self.tree.root)
		# self.tree.insert(16, self.tree.root)
		# self.tree.insert(1, self.tree.root)

		# self.tree.insert(20, self.tree.root)
		# self.tree.insert(5, self.tree.root)
		# self.tree.insert(30, self.tree.root)
		# self.tree.insert(15, self.tree.root)
		# self.tree.insert(10, self.tree.root)

		# for i in range(15):
		# 	self.tree.insert(i, self.tree.root)




		# self.tree.printout(self.tree.root)

		test_results = self.tree.getNodesArray()
		# convert node objects to node values
		for i in range(len(test_results)):
			node = test_results[i]
			test_results[i] = node.val if node != None else None

		# expected_results = [15,3,20,1,13,18,27,None,None,8,14,17,None,26,29,5,None,None,None,16,None,None,None,None,None,4,None,None,None,None,None]
		# assert (test_results == expected_results), "TEST CASE FAILURE: BST.insert()\nResult  :\t {0}\nExpected:\t {1}".format(test_results, expected_results)

		# self.tree.delete(20)
		# self.tree.printout(self.tree.root)

		# depth = self.tree.calculateDepth()
		# print("depth: {0}".format(depth))
		

		self.tree.graph()



		# expected_results = [15,3,20,1,13,18,27,None,None,8,14,17,None,26,29,5,None,None,None,16,None,None,None,None,None,4,None,None,None,None,None]



if __name__ == '__main__':
	tester = unitTester()
	tester.runTests()

	







