#!/usr/bin/python

#Return array with all values in a binary search tree that are within two values x and y

class Node:
	#constructor
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

	#function to print all values of BST within given range
def BST_search(root,k1,k2):
	# at first checking if root exists
	if root is None:
		return

	# BST is already sorted. We search the left sub-tree first. if root.data is greater than k1, then search left sub-tree
	if k1<root.data:
		BST_search(root.left,k1,k2)

	#if root's data lies in range, then print root data
	if k1<=root.data and k2>=root.data:
		print root.data

	#if root data is smaller than k2, then search right tree
	if k2>root.data:
		BST_search(root.right,k1,k2)

###########################################################
#testing the above functions
k1=10
k2=23
root=Node(20)
root.left=Node(12)
root.right=Node(25)
root.left.left=Node(10)
root.left.right=Node(15)
root.right.left=Node(21)
root.right.right=Node(35)

BST_search(root,k1,k2)
