#!/usr/bin/python
import random
# create a BST from a sorted array

# class to create nodes of BST
class Node:
	#cosntructor
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None 

#recursively create BST from array	
def arrToBSTcalc(num, begin, end):
		if begin>end:
			return None
		mid=(begin+end)//2
		root=Node(num[mid])
		root.left=arrToBSTcalc(num, begin, mid-1)
		root.right= arrToBSTcalc(num, mid+1, end)
		print root.data
		return root

sorted_arr=[1,4,6,8,10,14,18,21,24,25,32,35,36,40]

arrToBSTcalc(sorted_arr, 0, len(sorted_arr)-1)

