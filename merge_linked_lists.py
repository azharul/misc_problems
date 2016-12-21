#!/usr/bin/python

####  NOT COMPLETE ###
#the following class can create linked lists 
class Node:
	def __init__(self,cargo=None,next=None):
		self.cargo=cargo
		self.next=next
	def __str__(self):
		return str(self.cargo)
	def printlist(node):
		while node:
			print node
			node=node.next
		print

#merging two linked list
	Node MergeLists(Node list1, Node list2) {
		  if (list1 == null) return list2;
		  if (list2 == null) return list1;

		  if (list1.data < list2.data) {
    			list1.next = MergeLists(list1.next, list2);
    			return list1;
  } else {
    list2.next = MergeLists(list2.next, list1);
    return list2;
  }
}
# node1 creates a linked list that links node1,2,3,4
node1=Node(1)
node2=Node(4)
node3=Node(6)
node4=Node(8)

node1.next=node2
node2.next=node3
node3.next=node4

#node 5 creates a linked list that links node5,6,7,8
node5=Node(3)
node6=Node(5)
node7=Node(7)

node5.next=node6
node6.next=node7

Node.printlist(node1)

Node.printlist(node5)
print merge_lists(node1,node5)
